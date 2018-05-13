#!/usr/bin/env python
# coding: UTF-8

# This Python porting of the original Dynamixel Workbench Toolbox from ROBOTIS
# was written by Patrick Roncagliolo and Marco Lapolla as part of a project
# developed at the DIBRIS BIOLab of the University of Genoa, Italy.

import dynamixel_driver as dyn_driver

X_SERIES_CURRENT_CONTROL_MODE = 0
X_SERIES_VELOCITY_CONTROL_MODE = 1
X_SERIES_POSITION_CONTROL_MODE = 3
X_SERIES_EXTENDED_POSITION_CONTROL_MODE = 4
X_SERIES_CURRENT_BASED_POSITION_CONTROL_MODE = 5
X_SERIES_VOLTAGE_CONTROL_MODE = 16

PRO_SERIES_TORQUE_CONTROL_MODE = 0
PRO_SERIES_VELOCITY_CONTROL_MODE = 1
PRO_SERIES_POSITION_CONTROL_MODE = 3
PRO_SERIES_EXTENDED_POSITION_CONTROL_MODE = 4


class DynamixelWorkbench:
    def __init__(self):
        self._driver = dyn_driver.DynamixelDriver()
        self._dxl = ""

    def begin(self, device_name, baud_rate, protocol_version=None):
        return self._driver.init(device_name, baud_rate, protocol_version)

    def scan(self, id_range):
        return self._driver.scan(id_range)

    def ping(self, dxl_id):
        return self._driver.ping(dxl_id)

    def reboot(self, dxl_id):
        return self._driver.reboot(dxl_id)

    def reset(self, dxl_id):
        return self._driver.reset(dxl_id)

    def setID(self, old_id, new_id):
        self.torque(old_id, False)
        comm_result = self._driver.writeRegister(old_id, "ID", new_id)
        time.sleep(1)
        return comm_result

    def setBaud(self, dxl_id, new_baud):
        comm_result = False
        self.torque(dxl_id, False)
        if self._driver.getProtocolVersion() == 1.0:
            if new_baud == 9600:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 207)
            elif new_baud == 19200:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 103)
            elif new_baud == 57600:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 34)
            elif new_baud == 115200:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 16)
            elif new_baud == 200000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 9)
            elif new_baud == 250000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 7)
            elif new_baud == 400000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 4)
            elif new_baud == 500000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 3)
            elif new_baud == 1000000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 1)
            else:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 34)
        elif self._driver.getProtocolVersion() == 2.0:
            if new_baud == 9600:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 0)
            elif new_baud == 57600:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 1)
            elif new_baud == 115200:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 2)
            elif new_baud == 1000000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 3)
            elif new_baud == 2000000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 4)
            elif new_baud == 3000000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 5)
            elif new_baud == 4000000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 6)
            elif new_baud == 4500000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 7)
            elif new_baud == 10500000:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 8)
            else:
                comm_result = self._driver.writeRegister(dxl_id, "Baud_Rate", 1)
        time.sleep(2)
        return comm_result

    def setPacketHandler(self, protocol_version):
        return self._driver.setPacketHandler(protocol_version)

    def getModelName(self, dxl_id):
        return self._driver.getModelName(dxl_id)

    def ledOn(self, dxl_id):
        if self.getModelName(dxl_id)[:3] == "PRO":
            return self._driver.writeRegister(dxl_id, "LED_RED", 1)
        else:
            return self._driver.writeRegister(dxl_id, "LED", 1)

    def ledOff(self, dxl_id):
        if self.getModelName(dxl_id)[:3] == "PRO":
            return self._driver.writeRegister(dxl_id, "LED_RED", 0)
        else:
            return self._driver.writeRegister(dxl_id, "LED", 0)

    def jointMode(self, dxl_id, vel, acc=0):
        self._dxl = self._driver.getModelName(dxl_id)
        comm_result = self.torque(dxl_id, False)
        comm_result = self.setPositionControlMode(dxl_id)
        comm_result = self.torque(dxl_id, True)
        if self._driver.getProtocolVersion() == 1.0:
            if (self._dxl == "MX-28-2" or self._dxl == "MX-64-2" or self._dxl == "MX-106-2" or
                    self._dxl == "XL430" or self._dxl[:2] == "XM" or self._dxl[:2] == "XH"):
                comm_result = self._driver.writeRegister(dxl_id, "Profile_Acceleration", acc)
                comm_result = self._driver.writeRegister(dxl_id, "Profile_Velocity", vel)
            else:
                comm_result = self._driver.writeRegister(dxl_id, "Moving_Speed", vel)
        elif self._driver.getProtocolVersion() == 2.0:
            if self._dxl == "XL-320" or self._dxl[:3] == "PRO":
                comm_result = self._driver.writeRegister(dxl_id, "Moving_Speed", vel)
            else:
                comm_result = self._driver.writeRegister(dxl_id, "Profile_Acceleration", acc)
                comm_result = self._driver.writeRegister(dxl_id, "Profile_Velocity", vel)
        return comm_result

    def wheelMode(self, dxl_id, vel, acc):
        self._dxl = self._driver.getModelName(dxl_id)
        comm_result = self.torque(dxl_id, False)
        comm_result = self.setVelocityControlMode(dxl_id)
        comm_result = self.torque(dxl_id, True)
        if self._driver.getProtocolVersion() == 1.0:
            if (self._dxl == "MX-28-2" or self._dxl == "MX-64-2" or self._dxl == "MX-106-2" or
                    self._dxl == "XL430" or self._dxl[:2] == "XM" or self._dxl[:2] == "XH"):
                comm_result = self._driver.writeRegister(dxl_id, "Profile_Acceleration", acc)
                comm_result = self._driver.writeRegister(dxl_id, "Profile_Velocity", vel)
        elif self._driver.getProtocolVersion() == 2.0:
            if self._dxl == "XL-320" or self._dxl[:3] == "PRO":
                comm_result = self._driver.writeRegister(dxl_id, "Moving_Speed", vel)
        return comm_result

    def currentMode(self, dxl_id, cur):
        self._dxl = self._driver.getModelName(dxl_id)
        comm_result = self.torque(dxl_id, False)
        comm_result = self.setCurrentControlMode(dxl_id)
        comm_result = self.torque(dxl_id, True)
        if self._dxl[:1] == "X" or self._dxl == "MX-64-2" or self._dxl == "MX-106-2":
            comm_result = self._driver.writeRegister(dxl_id, "Goal_Current", cur)
        return comm_result

    def goalPosition(self, dxl_id, goal):
        return self._driver.writeRegister(dxl_id, "Goal_Position", goal)

    def goalSpeed(self, dxl_id, goal):
        comm_result = False
        self._dxl = self._driver.getModelName(dxl_id)
        if self._driver.getProtocolVersion() == 1.0:
            if (self._dxl == "MX-28-2" or self._dxl == "MX-64-2" or self._dxl == "MX-106-2" or
                    self._dxl == "XL430" or self._dxl[:2] == "XM" or self._dxl[:2] == "XH"):
                comm_result = self._driver.writeRegister(dxl_id, "Goal_Velocity", goal)
            else:
                if goal < 0:
                    goal = (-1) * goal
                    goal |= 1024
                comm_result = self._driver.writeRegister(dxl_id, "Moving_Speed", goal)
        elif self._driver.getProtocolVersion() == 2.0:
            if self._dxl != "XL-320":
                if goal < 0:
                    goal = (-1) * goal
                    goal |= 1024
                comm_result = self._driver.writeRegister(dxl_id, "Moving_Speed", goal)
            else:
                comm_result = self._driver.writeRegister(dxl_id, "Goal_Velocity", goal)
        return comm_result

    def itemWrite(self, dxl_id, item_name, value):
        return self._driver.writeRegister(dxl_id, item_name, value)

    def syncWrite(self, item_name, value):
        return self._driver.syncWrite(item_name, value)

    def bulkWrite(self):
        return self._driver.bulkWrite()

    def itemRead(self, dxl_id, item_name):
        res, data = self._driver.readRegister(dxl_id, item_name)
        return data if res else 0

    def syncRead(self, item_name):
        res, data = self._driver.syncRead(item_name)
        return data if res else 0

    def bulkRead(self, dxl_id, item_name):
        res, data = self._driver.bulkRead(dxl_id, item_name)
        return data if res else 0

    def addSyncWrite(self, item_name):
        self._driver.addSyncWrite(item_name)

    def addSyncRead(self,  item_name):
        self._driver.addSyncRead(item_name)

    def initBulkWrite(self):
        self._driver.initBulkWrite()

    def initBulkRead(self):
        self._driver.initBulkRead()

    def addBulkWriteParam(self, dxl_id, item_name, data):
        return self._driver.addBulkWriteParam(dxl_id, item_name, data)

    def addBulkReadParam(self, dxl_id, item_name):
        return self._driver.addBulkReadParam(dxl_id, item_name)

    def setBulkRead(self):
        return self._driver.sendBulkReadPacket()

    def convertDxlRadian2Value(self, dxl_id, radian):
        return self._driver.convertRadian2Value(dxl_id, radian)

    def convertDxlValue2Radian(self, dxl_id, value):
        return self._driver.convertValue2Radian(dxl_id, value)

    def convertRadian2Value(self, radian, max_position, min_position, max_radian, min_radian):
        return self._driver.convertRadian2Value(radian, max_position, min_position, max_radian, min_radian)

    def convertValue2Radian(self, value, max_position, min_position, max_radian, min_radian):
        return self._driver.convertValue2Radian(value, max_position, min_position, max_radian, min_radian)

    def convertVelocity2Value(self, id, velocity):
        return self._driver.convertVelocity2Value(id, velocity)

    def convertValue2Velocity(self, id, value):
        return self._driver.convertValue2Velocity(id, value)

    def convertTorque2Value(self, id, torque):
        return self._driver.convertTorque2Value(id, torque)

    def convertValue2Torque(self, id, value):
        return self._driver.convertValue2Torque(id, value)

	def setPositionControlMode(self, id):
		comm_result = False
        self._dxl = self._driver.getModelName(id)

        if self._driver.getProtocolVersion() == 1.0:
            if (self._dxl == "MX-28-2"
                    or self._dxl == "MX-64-2"
                    or self._dxl == "MX-106-2"
                    or self._dxl == "XL430"
                    or self._dxl[:2] == "XM"
                    or self._dxl[:2] == "XH"
                    or self._dxl[:3] == "PRO"):
                comm_result = self._driver.writeRegister(id, "Operating_Mode", X_SERIES_POSITION_CONTROL_MODE)
            elif self._dxl[:2] == "AX" or self._dxl[:2] == "RX":
                comm_result = self._driver.writeRegister(id, "CW_Angle_Limit", 0)
                comm_result = self._driver.writeRegister(id, "CCW_Angle_Limit", 1023)
            else:
                comm_result = self._driver.writeRegister(id, "CW_Angle_Limit", 0)
                comm_result = self._driver.writeRegister(id, "CCW_Angle_Limit", 4095)
        elif self._driver.getProtocolVersion() == 2.0:
            if self._dxl == "XL-320":
                comm_result = self._driver.writeRegister(id, "CW_Angle_Limit", 0)
                comm_result = self._driver.writeRegister(id, "CCW_Angle_Limit", 1023)
            else:
                comm_result = self._driver.writeRegister(id, "Operating_Mode", X_SERIES_POSITION_CONTROL_MODE)
        time.sleep(0.01)
        return comm_result

    def setVelocityControlMode(self, id):
        comm_result = False
        self._dxl = self._driver.getModelName(id)

        if self._driver.getProtocolVersion() == 1.0:
            if (self._dxl == "MX-28-2"
                    or self._dxl == "MX-64-2"
                    or self._dxl == "MX-106-2"
                    or self._dxl == "XL430"
                    or self._dxl[:2] == "XM"
                    or self._dxl[:2] == "XH"
                    or self._dxl[:3] == "PRO"):
                comm_result = self._driver.writeRegister(id, "Operating_Mode", X_SERIES_VELOCITY_CONTROL_MODE)
            else:
                comm_result = self._driver.writeRegister(id, "CW_Angle_Limit", 0)
                comm_result = self._driver.writeRegister(id, "CCW_Angle_Limit", 0)
        elif self._driver.getProtocolVersion() == 2.0:
            if self._dxl == "XL-320":
                comm_result = self._driver.writeRegister(id, "CW_Angle_Limit", 0)
                comm_result = self._driver.writeRegister(id, "CCW_Angle_Limit", 0)
            else:
                comm_result = self._driver.writeRegister(id, "Operating_Mode", X_SERIES_VELOCITY_CONTROL_MODE)
        time.sleep(0.01)
        return comm_result

    def setCurrentControlMode(self, id):
        comm_result = False
        self._dxl = self._driver.getModelName(id)
        if self._dxl[:1] == "X" or self._dxl == "MX-64-2" or self._dxl == "MX-106-2":
            comm_result = self._driver.writeRegister(id, "Operating_Mode", X_SERIES_CURRENT_BASED_POSITION_CONTROL_MODE)
        time.sleep(0.01)
        return comm_result
