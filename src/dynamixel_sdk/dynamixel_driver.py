#!/usr/bin/env python
# coding: UTF-8

# This Python porting of the original Dynamixel Workbench Toolbox from ROBOTIS
# was written by Patrick Roncagliolo and Marco Lapolla as part of a project
# developed at the DIBRIS BIOLab of the University of Genoa, Italy.

import time

import dynamixel_item as dyn_item
import dynamixel_tool as dyn_tool

import group_bulk_read as bulk_read
import group_bulk_write as bulk_write
import group_sync_read as sync_read
import group_sync_write as sync_write

import packet_handler
import port_handler
import protocol1_packet_handler as pr1_packet_handler
import protocol2_packet_handler as pr2_packet_handler
import robotis_def


MAX_DXL_SERIES_NUM = 3
MAX_HANDLER_NUM = 5

BYTE = 1
WORD = 2
DWORD = 4


# ct_item.ControlTableItem control_table; sync_write.GroupSyncWrite groupSyncWrite;
class SyncWriteHandler:
    def __init__(self):
        self.control_table_item = None
        self.groupSyncWrite = None


# ct_item.ControlTableItem control_table; sync_read.GroupSyncRead groupSyncRead;
class SyncReadHandler:
    def __init__(self):
        self.control_table_item = None
        self.groupSyncRead = None


class DynamixelDriver:
    def __init__(self):
        self.tools = []
        self.syncWriteHandler = []
        self.syncReadHandler = []
        self.portHandler = None
        self.packetHandler = None
        self.packetHandler_1 = None
        self.packetHandler_2 = None
        self.groupBulkWrite = None
        self.groupBulkRead = None

    def __del__(self):
        for x in self.tools:
            for y in x.dxl_info:
                self.writeRegister(y.id, "Torque_Enable", False)
        self.portHandler.closePort()

    def setTools(self, model_number, dxl_id):
        if len(self.tools) > 0 and self.tools[-1].dxl_info[0].model_num == model_number:
            self.tools[-1].addDXL(model_number, dxl_id)
        else:
            tool = dyn_tool.DynamixelTool()
            tool.addTool(model_number, dxl_id)
            self.tools.append(tool)

    def init(self, device_name, baud_rate, protocol_version=None):
		if protocol_version is None:
			return self.setPortHandler(device_name) and self.setBaudrate(baud_rate) and self.setPacketHandler()
		else:
			return self.setPortHandler(device_name) and self.setBaudrate(baud_rate) and self.setPacketHandler(protocol_version)

    def setPortHandler(self, device_name):
        self.portHandler = port_handler.PortHandler(device_name)
        return self.portHandler.openPort()

    def setPacketHandler(self, protocol_version=None):
        if protocol_version is None:
            self.packetHandler_1 = packet_handler.PacketHandler(1.0)
            self.packetHandler_2 = packet_handler.PacketHandler(2.0)
            return self.packetHandler_1.getProtocolVersion() == 1.0 and self.packetHandler_2.getProtocolVersion() == 2.0
        else:
			if protocol_version == 1.0:
				self.packetHandler_1 = packet_handler.PacketHandler(protocol_version)
			elif protocol_version == 2.0:
				self.packetHandler_2 = packet_handler.PacketHandler(protocol_version)
			self.packetHandler = packet_handler.PacketHandler(protocol_version)
			return self.packetHandler.getProtocolVersion() == protocol_version

    def setBaudrate(self, baud_rate):
        return self.portHandler.setBaudRate(baud_rate)

    def getProtocolVersion(self):
        return self.packetHandler.getProtocolVersion()

    def getBaudrate(self):
        return self.portHandler.getBaudRate()

    def getModelName(self, id):
        for x in self.tools:
            for y in x.dxl_info:
                if y.id == id:
                    return y.model_name
        return None

    def getModelNum(self, id):
        for x in self.tools:
            for y in x.dxl_info:
                if y.id == id:
                    return y.model_num
        return None

    def getControlItem(self, id):
        for x in self.tools:
            for y in x.dxl_info:
                if y.id == id:
                    return x.control_table
        return None

    def getTheNumberOfItem(self, id):
        for x in self.tools:
            for y in x.dxl_info:
                if y.id == id:
                    return len(x.control_table)
        return None

    def scan(self, id_range):
        protocol_version = 1.0
        get_ids = []
        self.tools = []

        for dxl_id in range(1, id_range + 1):
            model_number, ok, error = self.packetHandler_1.ping(self.portHandler, dxl_id)
            if ok == robotis_def.COMM_SUCCESS:
                get_ids.append(dxl_id)
                self.setTools(model_number, dxl_id)
                protocol_version = 1.0

		if len(get_ids) == 0:
		    for dxl_id in range(1, id_range + 1):
		        model_number, ok, error = self.packetHandler_2.ping(self.portHandler, dxl_id)
		        if ok == robotis_def.COMM_SUCCESS:
		            get_ids.append(dxl_id)
		            self.setTools(model_number, dxl_id)
		            protocol_version = 2.0

        if get_ids == [] or not self.setPacketHandler(protocol_version):
            return False, 0, []
        else:
            return True, len(get_ids), get_ids

    def ping(self, dxl_id):
        model_number, ok, error = self.packetHandler_1.ping(self.portHandler, dxl_id)
        if ok == robotis_def.COMM_SUCCESS:
            self.setTools(model_number, dxl_id)
            protocol_version = 1.0
        else:
            model_number, ok, error = self.packetHandler_2.ping(self.portHandler, dxl_id)
            if ok == robotis_def.COMM_SUCCESS:
                self.setTools(model_number, dxl_id)
                protocol_version = 2.0
            else:
                return False, 0
        return self.setPacketHandler(protocol_version), model_number

    def reboot(self, dxl_id):
        if self.packetHandler.getProtocolVersion() == 1.0:
            return False

        comm_result, error = self.packetHandler.reboot(self.portHandler, dxl_id)
        time.sleep(2)

        return comm_result == robotis_def.COMM_SUCCESS and error != 0

    def reset(self, dxl_id):
        if self.packetHandler.getProtocolVersion() == 1.0:
            # Reset Dynamixel except ID and Baudrate
            comm_result, error = self.packetHandler.factoryReset(self.portHandler, dxl_id, 0x00)
            time.sleep(2)

            if comm_result == robotis_def.COMM_SUCCESS:
                if error != 0:
                    return False

                for x in self.tools:
                    for y in x.dxl_info:
                        if y.id == id:
                            y.id = 1

                model_name = self.getModelName(1)
                if model_name[:2] == "AX" or model_name == "MX-12W":
                    baud = 1000000
                else:
                    baud = 57600

                if not self.portHandler.setBaudRate(baud):
                    time.sleep(2)
                    return False
                else:
                    time.sleep(2)
                    if model_name == "MX-28-2" or \
                            model_name == "MX-64-2" or \
                            model_name == "MX-106-2" or \
                            model_name[:2] == "XL" or \
                            model_name[:2] == "XM" or \
                            model_name[:2] == "XH" or \
                            model_name[:3] == "PRO":

                        return self.setPacketHandler(1.0)
                    else:
                        return self.setPacketHandler(2.0)
            else:
                return False

        elif self.packetHandler.getProtocolVersion() == 2.0:
            # Reset Dynamixel except ID and Baudrate
            comm_result, error = self.packetHandler.factoryReset(self.portHandler, dxl_id, 0x00)
            time.sleep(2)

            if comm_result == robotis_def.COMM_SUCCESS:
                if error != 0:
                    return False

                for x in self.tools:
                    for y in x.dxl_info:
                        if y.id == id:
                            y.id = 1

                model_name = self.getModelName(1)
                if model_name[:2] == "XL-320":
                    baud = 1000000
                else:
                    baud = 57600

                if not self.portHandler.setBaudRate(baud):
                    time.sleep(2)
                    return False
                else:
                    time.sleep(2)
                    return self.setPacketHandler(2.0)
            else:
                return False
        return False

    def writeRegister(self, dxl_id, item_name, data):
        error = 0
        dxl_comm_result = robotis_def.COMM_TX_FAIL

        cti = self.tools[self.getToolsFactor(dxl_id)].getControlItem(item_name)

        if cti.data_length == BYTE:
            dxl_comm_result, error = self.packetHandler.write1ByteTxRx(self.portHandler, dxl_id, cti.address, data)
        elif cti.data_length == WORD:
            dxl_comm_result, error = self.packetHandler.write2ByteTxRx(self.portHandler, dxl_id, cti.address, data)
        elif cti.data_length == DWORD:
            dxl_comm_result, error = self.packetHandler.write4ByteTxRx(self.portHandler, dxl_id, cti.address, data)

        return dxl_comm_result == robotis_def.COMM_SUCCESS and error == 0

    def readRegister(self, id, item_name):
		error = 0
		dxl_comm_result = robotis_def.COMM_TX_FAIL

		cti = self.tools[self.getToolsFactor(id)].getControlItem(item_name)
		if cti.data_length == BYTE:
			data, dxl_comm_result, error = self.packetHandler.read1ByteTxRx(self.portHandler, id, cti.address)
		elif cti.data_length == WORD:
			data, dxl_comm_result, error = self.packetHandler.read2ByteTxRx(self.portHandler, id, cti.address)
		elif cti.data_length == DWORD:
			data, dxl_comm_result, error = self.packetHandler.read4ByteTxRx(self.portHandler, id, cti.address)

		return dxl_comm_result == robotis_def.COMM_SUCCESS and error == 0, data

    def getToolsFactor(self, dxl_id):
        for i, x in enumerate(self.tools):
            for y in x.dxl_info:
                if y.id == dxl_id:
                    return i
        return -1

    def findModelName(self, model_number):
        d = {dyn_item.AX_12A: "AX-12A",
             dyn_item.AX_12W: "AX-12W",
             dyn_item.AX_18A: "AX-18A",
             dyn_item.RX_10: "RX-10",
             dyn_item.RX_24F: "RX-24F",
             dyn_item.RX_28: "RX-28",
             dyn_item.RX_64: "RX-64",
             dyn_item.EX_106: "EX-106",
             dyn_item.MX_12W: "MX-12W",
             dyn_item.MX_28: "MX-28",
             dyn_item.MX_28_2: "MX-28-2",
             dyn_item.MX_64: "MX-64",
             dyn_item.MX_64_2: "MX-64-2",
             dyn_item.MX_106: "MX-106",
             dyn_item.MX_106_2: "MX-106-2"}
        return d[model_number]

    def addSyncWrite(self, item_name):
        swh = SyncWriteHandler()
        swh.control_table = self.tools[0].getControlItem(item_name)
        swh.groupSyncWrite = sync_write.GroupSyncWrite(self.portHandler,
                                                    self.packetHandler,
                                                    swh.control_table.address,
                                                    swh.control_table.data_length)
        self.syncWriteHandler.append(swh)

    def syncWrite(self, item_name, data):
        cnt = 0
        swh = SyncWriteHandler()
        for x in self.syncWriteHandler:
            if x.control_table.item_name == item_name:
                swh = x
        for x in self.tools:
            for y in x.dxl_info:
                data_byte = [robotis_def.DXL_LOBYTE(robotis_def.DXL_LOWORD(data[cnt])),
                             robotis_def.DXL_HIBYTE(robotis_def.DXL_LOWORD(data[cnt])),
                             robotis_def.DXL_LOBYTE(robotis_def.DXL_HIWORD(data[cnt])),
                             robotis_def.DXL_HIBYTE(robotis_def.DXL_HIWORD(data[cnt]))]

                dxl_add_param_result = swh.groupSyncWrite.addParam(y.id, data_byte)
                if not dxl_add_param_result:
                    return False
                cnt += 1

        if swh.groupSyncWrite.txPacket() != robotis_def.COMM_SUCCESS:
            return False
        else:
            swh.groupSyncWrite.clearParam()
            return True

    def addSyncRead(self, item_name):
        srh = SyncReadHandler()
        cti = srh.control_table_item = self.tools[0].getControlItem(item_name)
        srh.groupSyncRead = sync_read.GroupSyncRead(self.portHandler,
                                                  self.packetHandler,
                                                  cti.address,
                                                  cti.data_length)
        self.syncReadHandler.append(srh)

    def syncRead(self, item_name):
        srh = SyncReadHandler()
        data = []
        for x in self.syncReadHandler:
            if x.control_table_item.item_name == item_name:
                srh = x

        for x in self.tools:
            for y in x.dxl_info:
                if not srh.groupSyncRead.addParam(y.id):
                    return False, data

        dxl_comm_result = srh.groupSyncRead.txRxPacket()
        if dxl_comm_result != robotis_def.COMM_SUCCESS:
            return False, data

        for x in self.tools:
            for y in x.dxl_info:
                dxl_get_data_result = srh.groupSyncRead.isAvailable(y.id, srh.control_table_item.address,
                                                                   srh.control_table_item.data_length)
                if dxl_get_data_result:
                    data.append(srh.groupSyncRead.getData(y.id, srh.control_table_item.address,
                                                          srh.control_table_item.data_length))
                else:
                    return False, data

        srh.groupSyncRead.clearParam()

        return True, data

    def initBulkWrite(self):
        self.groupBulkWrite = bulk_write.GroupBulkWrite(self.portHandler, self.packetHandler)

    def addBulkWriteParam(self, dxl_id, item_name, data):
        cti = self.tools[self.getToolsFactor(dxl_id)].getControlItem(item_name)

        data_byte = [robotis_def.DXL_LOBYTE(robotis_def.DXL_LOWORD(data)),
                	 robotis_def.DXL_HIBYTE(robotis_def.DXL_LOWORD(data)),
                	 robotis_def.DXL_LOBYTE(robotis_def.DXL_HIWORD(data)),
                	 robotis_def.DXL_HIBYTE(robotis_def.DXL_HIWORD(data))]

        return self.groupBulkWrite.addParam(dxl_id, cti.address, cti.data_length, data_byte)

    def bulkWrite(self):
        dxl_comm_result = self.groupBulkWrite.txPacket()
        if dxl_comm_result != robotis_def.COMM_SUCCESS:
            return False

        self.groupBulkWrite.clearParam()
        return True

    def initBulkRead(self):
        self.groupBulkRead = bulk_read.GroupBulkRead(self.portHandler, self.packetHandler)

    def addBulkReadParam(self, dxl_id, item_name):
        cti = self.tools[self.getToolsFactor(dxl_id)].getControlItem(item_name)

        return self.groupBulkRead.addParam(dxl_id, cti.address, cti.data_length)

    def sendBulkReadPacket(self):
        return self.groupBulkRead.txRxPacket()

    def bulkRead(self, dxl_id, item_name):
        cti = self.tools[self.getToolsFactor(dxl_id)].getControlItem(item_name)

        dxl_get_data_result = self.groupBulkRead.isAvailable(dxl_id, cti.address, cti.data_length)
        if not dxl_get_data_result:
            return False, None

        data = self.groupBulkRead.getData(dxl_id, cti.address, cti.data_length)

        return True, data

    def convertDxlRadian2Value(self, dxl_id, radian):
        t = self.tools[self.getToolsFactor(dxl_id)]
        return self.convertValue2Radian(radian,
                                        t.getValueOfMaxRadianPosition(),
                                        t.getValueOfMinRadianPosition(),
                                        t.getMaxRadian(),
                                        t.getMinRadian())

    def convertDxlValue2Radian(self, dxl_id, value):
        t = self.tools[self.getToolsFactor(dxl_id)]
        return self.convertValue2Radian(value,
                                        t.getValueOfMaxRadianPosition(),
                                        t.getValueOfMinRadianPosition(),
                                        t.getMaxRadian(),
                                        t.getMinRadian())

    def convertRadian2Value(self, radian, max_position, min_position, max_radian, min_radian):
        zero_position = (max_position + min_position) / 2
        if radian > 0:
            value = (radian * (max_position - zero_position) / max_radian) + zero_position
        elif radian < 0:
            value = (radian * (min_position - zero_position) / min_radian) + zero_position
        else:
            value = zero_position
        return value

    def convertValue2Radian(self, value, max_position, min_position, max_radian, min_radian):
        zero_position = (max_position + min_position) / 2
        radian = 0
        if value > zero_position:
            radian = float(value - zero_position) * max_radian / float((max_position - zero_position))
        elif value < zero_position:
            radian = float(value - zero_position) * min_radian / float((min_position - zero_position))
        return radian

    def convertVelocity2Value(self, dxl_id, velocity):
        factor = self.getToolsFactor(dxl_id)
        value = velocity * self.tools[factor].getVelocityToValueRatio()
        return value

    def convertValue2Velocity(self, dxl_id, value):
        factor = self.getToolsFactor(dxl_id)
        velocity = value / self.tools[factor].getVelocityToValueRatio()
        return velocity

    def convertTorque2Value(self, dxl_id, torque):
        factor = self.getToolsFactor(dxl_id)
        value = torque * self.tools[factor].getTorqueToCurrentValueRatio()
        return value

    def convertValue2Torque(self, dxl_id, value):
        factor = self.getToolsFactor(dxl_id)
        torque = value / self.tools[factor].getTorqueToCurrentValueRatio()
        return torque
