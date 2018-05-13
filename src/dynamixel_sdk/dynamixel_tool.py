#!/usr/bin/env python
# coding: UTF-8

# This Python porting of the original Dynamixel Workbench Toolbox from ROBOTIS
# was written by Patrick Roncagliolo and Marco Lapolla as part of a project
# developed at the DIBRIS BIOLab of the University of Genoa, Italy.

import dynamixel_item as dyn_item

class DXLInfo:
    def __init__(self, model_name, model_num, dxl_id):
        self.model_name = model_name
        self.model_num = model_num
        self.id = dxl_id


class DynamixelTool:
    def __init__(self):
        self.dxl_info = []
        self.control_table = dyn_item.ControlTable()
        self.model_info = dyn_item.ModelInfo()

    def addTool(self, model, dxl_id):
        if dxl_id in self.dxl_info:
                return
        if type(model) == str:
            self.dxl_info.append(DXLInfo(model, self.setModelNum(model), dxl_id))
        elif type(model) == int:
            self.dxl_info.append(DXLInfo(self.setModelName(model), model, dxl_id))
        self.setControlTable(model)

    def addDXL(self, model, dxl_id):
        if dxl_id in self.dxl_info:
                return
        if type(model) == str:
            self.dxl_info.append(DXLInfo(model, self.setModelNum(model), dxl_id))
        elif type(model) == int:
            self.dxl_info.append(DXLInfo(self.setModelName(model), model, dxl_id))

    def setControlTable(self, model):
        num = self.setModelNum(model) if type(model) == str else model
        self.model_info.getModelInfo(num)
        self.control_table.getControlTableItem(num)

    def setModelNum(self, model):
        if type(model) != str:
            return
        name = str(model)
        if name == "AX-12A":
            return dyn_item.AX_12A
        elif name == "AX-12W":
            return dyn_item.AX_12W
        elif name == "AX-18A":
            return dyn_item.AX_18A
        elif name == "RX-10":
            return dyn_item.RX_10
        elif name == "RX-24F":
            return dyn_item.RX_24F
        elif name == "RX-28":
            return dyn_item.RX_28
        elif name == "RX-64":
            return dyn_item.RX_64
        elif name == "EX-106":
            return dyn_item.EX_106
        elif name == "MX-12W":
            return dyn_item.MX_12W
        elif name == "MX-28":
            return dyn_item.MX_28
        elif name == "MX-28-2":
            return dyn_item.MX_28_2
        elif name == "MX-64":
            return dyn_item.MX_64
        elif name == "MX-64-2":
            return dyn_item.MX_64_2
        elif name == "MX-106":
            return dyn_item.MX_106
        elif name == "MX-106-2":
            return dyn_item.MX_106_2

    def setModelName(self, model):
        if type(model) != int:
            return
        num = int(model)
        if num == dyn_item.AX_12A:
            return "AX-12A"
        elif num == dyn_item.AX_12W:
            return "AX-12W"
        elif num == dyn_item.AX_18A:
            return "AX-18A"
        elif num == dyn_item.RX_10:
            return "RX-10"
        elif num == dyn_item.RX_24F:
            return "RX-24F"
        elif num == dyn_item.RX_28:
            return "RX-28"
        elif num == dyn_item.RX_64:
            return "RX-64"
        elif num == dyn_item.EX_106:
            return "EX-106"
        elif num == dyn_item.MX_12W:
            return "MX-12W"
        elif num == dyn_item.MX_28:
            return "MX-28"
        elif num == dyn_item.MX_28_2:
            return "MX-28-2"
        elif num == dyn_item.MX_64:
            return "MX-64"
        elif num == dyn_item.MX_64_2:
            return "MX-64-2"
        elif num == dyn_item.MX_106:
            return "MX-106"
        elif num == dyn_item.MX_106_2:
            return "MX-106-2"

    def getVelocityToValueRatio(self):
        return self.model_info.velocity_to_value_ratio

    def getTorqueToCurrentValueRatio(self):
        return self.model_info.torque_to_current_value_ratio

    def getValueOfMinRadianPosition(self):
        return self.model_info.value_of_min_radian_position

    def getValueOfMaxRadianPosition(self):
        return self.model_info.value_of_max_radian_position

    def getValueOfZeroRadianPosition(self):
        return self.model_info.value_of_0_radian_position

    def getMinRadian(self):
        return self.model_info.min_radian

    def getMaxRadian(self):
        return self.model_info.max_radian

    def getTheNumberOfItem(self):
        return self.control_table.getTheNumberOfControlItem()

    #TODO use dictionaries like ("action: [code, len]")
    def getControlItem(self, item_name):
        for i in range(0, self.getTheNumberOfItem()):
            if item_name == self.control_table._item[i].item_name:
                return self.control_table._item[i]
