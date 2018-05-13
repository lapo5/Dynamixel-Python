#!/usr/bin/env python
# coding: UTF-8

# This Python porting of the original Dynamixel Workbench Toolbox from ROBOTIS
# was written by Patrick Roncagliolo and Marco Lapolla as part of a project
# developed at the DIBRIS BIOLab of the University of Genoa, Italy.

import control_table_item as ct_item

# Type of Servo-Motors
AX_12A = 12
AX_12W = 300
AX_18A = 18
RX_10 = 10
RX_24F = 24
RX_28 = 28
RX_64 = 64
EX_106 = 107
MX_12W = 360
MX_28 = 29
MX_28_2 = 30
MX_64 = 310
MX_64_2 = 311
MX_106 = 320
MX_106_2 = 321
XL_320 = 350
XL430_W250 = 1060
XM430_W210 = 1030
XM430_W350 = 1020
XM540_W150 = 1130
XM540_W270 = 1120
XH430_V210 = 1050
XH430_V350 = 1040
XH430_W210 = 1010
XH430_W350 = 1000
PRO_L42_10_S300_R = 35072
PRO_L54_30_S400_R = 37928
PRO_L54_30_S500_R = 37896
PRO_L54_50_S290_R = 38176
PRO_L54_50_S500_R = 38152
PRO_M42_10_S260_R = 43288
PRO_M54_40_S250_R = 46096
PRO_M54_60_S250_R = 46352
PRO_H42_20_S300_R = 51200
PRO_H54_100_S500_R = 53768
PRO_H54_200_S500_R = 54024

BYTE = 1
WORD = 2
DWORD = 4

class ModelInfo:
    def __init__(self):
        self.velocity_to_value_ratio = None
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = None
        self.value_of_0_radian_position = None
        self.value_of_max_radian_position = None
        self.min_radian = None
        self.max_radian = None

    def setAXInfo(self):
        self.velocity_to_value_ratio = 86.03
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 512
        self.value_of_max_radian_position = 1023
        self.min_radian = -2.61799
        self.max_radian = 2.61799

    def setRXInfo(self):
        self.velocity_to_value_ratio = 86.03
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 512
        self.value_of_max_radian_position = 1023
        self.min_radian = -2.61799
        self.max_radian = 2.61799

    def setEXInfo(self):
        self.velocity_to_value_ratio = 86.03
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -2.18969008
        self.max_radian = 2.18969008

    def setMXInfo(self):
        self.velocity_to_value_ratio = 86.81
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def setMX2Info(self):
        self.velocity_to_value_ratio = 41.70
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def setExtMXInfo(self):
        self.velocity_to_value_ratio = 86.81
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def setExtMX2Info(self):
        self.velocity_to_value_ratio = 41.70
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def setXL320Info(self):
        self.velocity_to_value_ratio = 86.03
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 512
        self.value_of_max_radian_position = 1023
        self.min_radian = -2.61799
        self.max_radian = 2.61799

    def setXLInfo(self):
        self.velocity_to_value_ratio = 41.70
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def setXMInfo(self):
        self.velocity_to_value_ratio = 41.70
        self.torque_to_current_value_ratio = 149.795386991
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def setExtXMInfo(self):
        self.velocity_to_value_ratio = 41.70
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def setXHInfo(self):
        self.velocity_to_value_ratio = 41.71
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = 0
        self.value_of_0_radian_position = 2048
        self.value_of_max_radian_position = 4095
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def setPROInfo(self):
        self.velocity_to_value_ratio = 4792.8
        self.torque_to_current_value_ratio = None
        self.value_of_min_radian_position = -250961
        self.value_of_0_radian_position = 0
        self.value_of_max_radian_position = 250961
        self.min_radian = -3.14159265
        self.max_radian = 3.14159265

    def getModelInfo(self, num):
        if num in [AX_12A, AX_12W, AX_18A]:
            self.setAXInfo()
        elif num in [RX_10, RX_24F, RX_28, RX_64]:
            self.setRXInfo()
        elif num == EX_106:
            self.setEXInfo()
        elif num in [MX_12W, MX_28]:
            self.setMXInfo()
        elif num in [MX_64, MX_106]:
            self.setExtMXInfo()
        elif num == MX_28_2:
            self.setMX2Info()
        elif num in [MX_64_2, MX_106_2]:
            self.setExtMX2Info()
        elif num == XL_320:
            self.setXL320Info()
        elif num == XL430_W250:
            self.setXLInfo()
        elif num in [XM430_W210, XM430_W350]:
            self.setXMInfo()
        elif num in [XM540_W150, XM540_W270]:
            self.setExtXMInfo()
        elif num in [XH430_V210, XH430_V350, XH430_W210, XH430_W350]:
            self.setXHInfo()
        elif num in [PRO_L42_10_S300_R, PRO_L54_30_S400_R, PRO_L54_30_S500_R,
                     PRO_L54_50_S290_R, PRO_L54_50_S500_R, PRO_M42_10_S260_R,
                     PRO_M54_40_S250_R, PRO_M54_60_S250_R, PRO_H42_20_S300_R,
                     PRO_H54_100_S500_R,PRO_H54_200_S500_R]:
            self.setPROInfo()
        else:
            self.setXMInfo()
        return self


class ControlTable:
    def __init__(self):
        self._item = []

    def setAXItem(self):
        self._item = []
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(2, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(3, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(4, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(5, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(6, "CW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(8, "CCW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(11, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Min_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Max_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(14, "Max_Torque", WORD))
        self._item.append(ct_item.ControlTableItem(16, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(17, "Alarm_LED", BYTE))
        self._item.append(ct_item.ControlTableItem(18, "Shutdown", BYTE))
        self._item.append(ct_item.ControlTableItem(24, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(25, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(26, "CW_Compliance_Margin", BYTE))
        self._item.append(ct_item.ControlTableItem(27, "CCW_Compliance_Margin", BYTE))
        self._item.append(ct_item.ControlTableItem(28, "CW_Compliance_Slope", BYTE))
        self._item.append(ct_item.ControlTableItem(29, "CCW_Compliance_Slope", BYTE))
        self._item.append(ct_item.ControlTableItem(30, "Goal_Position", WORD))
        self._item.append(ct_item.ControlTableItem(32, "Moving_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Torque_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "Present_Position", WORD))
        self._item.append(ct_item.ControlTableItem(38, "Present_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Present_Load", WORD))
        self._item.append(ct_item.ControlTableItem(42, "Present_Voltage", BYTE))
        self._item.append(ct_item.ControlTableItem(43, "Present_Temperature", BYTE))
        self._item.append(ct_item.ControlTableItem(44, "Registered", BYTE))
        self._item.append(ct_item.ControlTableItem(46, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(47, "Lock", BYTE))
        self._item.append(ct_item.ControlTableItem(48, "Punch", WORD))

    def setRXItem(self):
        self._item = []
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(2, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(3, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(4, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(5, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(6, "CW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(8, "CCW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(11, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Min_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Max_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(14, "Max_Torque", WORD))
        self._item.append(ct_item.ControlTableItem(16, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(17, "Alarm_LED", BYTE))
        self._item.append(ct_item.ControlTableItem(18, "Shutdown", BYTE))
        self._item.append(ct_item.ControlTableItem(24, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(25, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(26, "CW_Compliance_Margin", BYTE))
        self._item.append(ct_item.ControlTableItem(27, "CCW_Compliance_Margin", BYTE))
        self._item.append(ct_item.ControlTableItem(28, "CW_Compliance_Slope", BYTE))
        self._item.append(ct_item.ControlTableItem(29, "CCW_Compliance_Slope", BYTE))
        self._item.append(ct_item.ControlTableItem(30, "Goal_Position", WORD))
        self._item.append(ct_item.ControlTableItem(32, "Moving_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Torque_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "Present_Position", WORD))
        self._item.append(ct_item.ControlTableItem(38, "Present_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Present_Load", WORD))
        self._item.append(ct_item.ControlTableItem(42, "Present_Voltage", BYTE))
        self._item.append(ct_item.ControlTableItem(43, "Present_Temperature", BYTE))
        self._item.append(ct_item.ControlTableItem(44, "Registered", BYTE))
        self._item.append(ct_item.ControlTableItem(46, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(47, "Lock", BYTE))
        self._item.append(ct_item.ControlTableItem(48, "Punch", WORD))

    def setEXItem(self):
        self._item = []
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(2, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(3, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(4, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(5, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(6, "CW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(8, "CCW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(10, "Drive_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(11, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Min_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Max_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(14, "Max_Torque", WORD))
        self._item.append(ct_item.ControlTableItem(16, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(17, "Alarm_LED", BYTE))
        self._item.append(ct_item.ControlTableItem(18, "Shutdown", BYTE))
        self._item.append(ct_item.ControlTableItem(24, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(25, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(26, "CW_Compliance_Margin", BYTE))
        self._item.append(ct_item.ControlTableItem(27, "CCW_Compliance_Margin", BYTE))
        self._item.append(ct_item.ControlTableItem(28, "CW_Compliance_Slope", BYTE))
        self._item.append(ct_item.ControlTableItem(29, "CCW_Compliance_Slope", BYTE))
        self._item.append(ct_item.ControlTableItem(30, "Goal_Position", WORD))
        self._item.append(ct_item.ControlTableItem(32, "Moving_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Torque_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "Present_Position", WORD))
        self._item.append(ct_item.ControlTableItem(38, "Present_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Present_Load", WORD))
        self._item.append(ct_item.ControlTableItem(42, "Present_Voltage", BYTE))
        self._item.append(ct_item.ControlTableItem(43, "Present_Temperature", BYTE))
        self._item.append(ct_item.ControlTableItem(44, "Registered", BYTE))
        self._item.append(ct_item.ControlTableItem(46, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(47, "Lock", BYTE))
        self._item.append(ct_item.ControlTableItem(48, "Punch", WORD))
        self._item.append(ct_item.ControlTableItem(56, "Sensored_Current", WORD))

    def setMXItem(self):
        self._item = []
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(2, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(3, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(4, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(5, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(6, "CW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(8, "CCW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(11, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Min_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Max_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(14, "Max_Torque", WORD))
        self._item.append(ct_item.ControlTableItem(16, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(17, "Alarm_LED", BYTE))
        self._item.append(ct_item.ControlTableItem(18, "Shutdown", BYTE))
        self._item.append(ct_item.ControlTableItem(20, "Multi_Turn_Offset", WORD))
        self._item.append(ct_item.ControlTableItem(22, "Resolution_Divider", BYTE))
        self._item.append(ct_item.ControlTableItem(24, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(25, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(26, "D_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(27, "I_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(28, "P_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(30, "Goal_Position", WORD))
        self._item.append(ct_item.ControlTableItem(32, "Moving_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Torque_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "Present_Position", WORD))
        self._item.append(ct_item.ControlTableItem(38, "Present_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Present_Load", WORD))
        self._item.append(ct_item.ControlTableItem(42, "Present_Voltage", BYTE))
        self._item.append(ct_item.ControlTableItem(43, "Present_Temperature", BYTE))
        self._item.append(ct_item.ControlTableItem(44, "Registered", BYTE))
        self._item.append(ct_item.ControlTableItem(46, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(47, "Lock", BYTE))
        self._item.append(ct_item.ControlTableItem(48, "Punch", WORD))
        self._item.append(ct_item.ControlTableItem(73, "Goal_Acceleration", BYTE))

    def setMX2Item(self):
        self._item = []
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(6, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(7, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(8, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(9, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(10, "Drive_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(11, "Operating_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Secondary_ID", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Protocol_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(20, "Homing_Offset", DWORD))
        self._item.append(ct_item.ControlTableItem(24, "Moving_Threshold", DWORD))
        self._item.append(ct_item.ControlTableItem(31, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(32, "Max_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Min_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "PWM_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Acceleration_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(44, "Velocity_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(48, "Max_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(52, "Min_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(63, "Shutdown", BYTE))

        self._item.append(ct_item.ControlTableItem(64, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(65, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(68, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(69, "Registered_Instruction", BYTE))
        self._item.append(ct_item.ControlTableItem(70, "Hardware_Error_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(76, "Velocity_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(78, "Velocity_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(80, "Position_D_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(82, "Position_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(84, "Position_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(88, "Feedforward_2nd_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(90, "Feedforward_1st_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(98, "Bus_Watchdog", BYTE))
        self._item.append(ct_item.ControlTableItem(100, "Goal_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(104, "Goal_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(108, "Profile_Acceleration", DWORD))
        self._item.append(ct_item.ControlTableItem(112, "Profile_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(116, "Goal_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(120, "Realtime_Tick", WORD))
        self._item.append(ct_item.ControlTableItem(122, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(123, "Moving_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(124, "Present_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(126, "Present_Load", WORD))
        self._item.append(ct_item.ControlTableItem(128, "Present_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(132, "Present_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(136, "Velocity_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(140, "Position_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(144, "Present_Input_Voltage", WORD))
        self._item.append(ct_item.ControlTableItem(146, "Present_Temperature", BYTE))

    def setExtMXItem(self):
        self._item = []
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(2, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(3, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(4, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(5, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(6, "CW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(8, "CCW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(11, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Min_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Max_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(14, "Max_Torque", WORD))
        self._item.append(ct_item.ControlTableItem(16, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(17, "Alarm_LED", BYTE))
        self._item.append(ct_item.ControlTableItem(18, "Shutdown", BYTE))
        self._item.append(ct_item.ControlTableItem(20, "Multi_Turn_Offset", WORD))
        self._item.append(ct_item.ControlTableItem(22, "Resolution_Divider", BYTE))

        self._item.append(ct_item.ControlTableItem(24, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(25, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(26, "D_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(27, "I_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(28, "P_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(30, "Goal_Position", WORD))
        self._item.append(ct_item.ControlTableItem(32, "Moving_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Torque_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "Present_Position", WORD))
        self._item.append(ct_item.ControlTableItem(38, "Present_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Present_Load", WORD))
        self._item.append(ct_item.ControlTableItem(42, "Present_Voltage", BYTE))
        self._item.append(ct_item.ControlTableItem(43, "Present_Temperature", BYTE))
        self._item.append(ct_item.ControlTableItem(44, "Registered", BYTE))
        self._item.append(ct_item.ControlTableItem(46, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(47, "Lock", BYTE))
        self._item.append(ct_item.ControlTableItem(48, "Punch", WORD))
        self._item.append(ct_item.ControlTableItem(68, "Current", WORD))
        self._item.append(ct_item.ControlTableItem(70, "Torque_Control_Mode_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(71, "Goal_Torque", WORD))
        self._item.append(ct_item.ControlTableItem(73, "Goal_Acceleration", BYTE))

    def setExtMX2Item(self):
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(6, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(7, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(8, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(9, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(10, "Drive_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(11, "Operating_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Secondary_ID", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Protocol_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(20, "Homing_Offset", DWORD))
        self._item.append(ct_item.ControlTableItem(24, "Moving_Threshold", DWORD))
        self._item.append(ct_item.ControlTableItem(31, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(32, "Max_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Min_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "PWM_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Current_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Acceleration_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(44, "Velocity_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(48, "Max_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(52, "Min_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(63, "Shutdown", BYTE))

        self._item.append(ct_item.ControlTableItem(64, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(65, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(68, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(69, "Registered_Instruction", BYTE))
        self._item.append(ct_item.ControlTableItem(70, "Hardware_Error_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(76, "Velocity_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(78, "Velocity_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(80, "Position_D_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(82, "Position_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(84, "Position_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(88, "Feedforward_2nd_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(90, "Feedforward_1st_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(98, "Bus_Watchdog", BYTE))
        self._item.append(ct_item.ControlTableItem(100, "Goal_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(102, "Goal_Current", WORD))
        self._item.append(ct_item.ControlTableItem(104, "Goal_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(108, "Profile_Acceleration", DWORD))
        self._item.append(ct_item.ControlTableItem(112, "Profile_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(116, "Goal_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(120, "Realtime_Tick", WORD))
        self._item.append(ct_item.ControlTableItem(122, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(123, "Moving_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(124, "Present_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(126, "Present_Current", WORD))
        self._item.append(ct_item.ControlTableItem(128, "Present_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(132, "Present_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(136, "Velocity_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(140, "Position_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(144, "Present_Input Voltage", WORD))
        self._item.append(ct_item.ControlTableItem(146, "Present_Temperature", BYTE))

    def setXL320Item(self):
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(2, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(3, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(4, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(5, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(6, "CW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(8, "CCW_Angle_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(11, "Control_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Min_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(14, "Max_Voltage_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(15, "Max_Torque", WORD))
        self._item.append(ct_item.ControlTableItem(17, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(18, "Shutdown", BYTE))

        self._item.append(ct_item.ControlTableItem(24, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(25, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(27, "D_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(28, "I_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(29, "P_gain", BYTE))
        self._item.append(ct_item.ControlTableItem(30, "Goal_Position", WORD))
        self._item.append(ct_item.ControlTableItem(32, "Moving_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Torque_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(37, "Present_Position", WORD))
        self._item.append(ct_item.ControlTableItem(39, "Present_Speed", WORD))
        self._item.append(ct_item.ControlTableItem(41, "Present_Load", WORD))
        self._item.append(ct_item.ControlTableItem(45, "Present_Voltage", BYTE))
        self._item.append(ct_item.ControlTableItem(46, "Present_Temperature", BYTE))
        self._item.append(ct_item.ControlTableItem(47, "Registered", BYTE))
        self._item.append(ct_item.ControlTableItem(49, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(50, "Hardware_Error_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(51, "Punch", WORD))

    def setXLItem(self):
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(6, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(7, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(8, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(9, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(10, "Drive_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(11, "Operating_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Secondary_ID", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Protocol_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(20, "Homing_Offset", DWORD))
        self._item.append(ct_item.ControlTableItem(24, "Moving_Threshold", DWORD))
        self._item.append(ct_item.ControlTableItem(31, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(32, "Max_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Min_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "PWM_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Acceleration_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(44, "Velocity_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(48, "Max_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(52, "Min_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(63, "Shutdown", BYTE))

        self._item.append(ct_item.ControlTableItem(64, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(65, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(68, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(69, "Registered_Instruction", BYTE))
        self._item.append(ct_item.ControlTableItem(70, "Hardware_Error_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(76, "Velocity_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(78, "Velocity_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(80, "Position_D_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(82, "Position_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(84, "Position_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(88, "Feedforward_2nd_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(90, "Feedforward_1st_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(98, "Bus_Watchdog", BYTE))
        self._item.append(ct_item.ControlTableItem(100, "Goal_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(104, "Goal_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(108, "Profile_Acceleration", DWORD))
        self._item.append(ct_item.ControlTableItem(112, "Profile_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(116, "Goal_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(120, "Realtime_Tick", WORD))
        self._item.append(ct_item.ControlTableItem(122, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(123, "Moving_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(124, "Present_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(126, "Present_Load", WORD))
        self._item.append(ct_item.ControlTableItem(128, "Present_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(132, "Present_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(136, "Velocity_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(140, "Position_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(144, "Present_Input_Voltage", WORD))
        self._item.append(ct_item.ControlTableItem(146, "Present_Temperature", BYTE))


    def setXMItem(self):
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(6, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(7, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(8, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(9, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(10, "Drive_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(11, "Operating_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Secondary_ID", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Protocol_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(20, "Homing_Offset", DWORD))
        self._item.append(ct_item.ControlTableItem(24, "Moving_Threshold", DWORD))
        self._item.append(ct_item.ControlTableItem(31, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(32, "Max_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Min_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "PWM_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Current_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Acceleration_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(44, "Velocity_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(48, "Max_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(52, "Min_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(63, "Shutdown", BYTE))

        self._item.append(ct_item.ControlTableItem(64, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(65, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(68, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(69, "Registered_Instruction", BYTE))
        self._item.append(ct_item.ControlTableItem(70, "Hardware_Error_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(76, "Velocity_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(78, "Velocity_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(80, "Position_D_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(82, "Position_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(84, "Position_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(88, "Feedforward_2nd_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(90, "Feedforward_1st_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(98, "Bus_Watchdog", BYTE))
        self._item.append(ct_item.ControlTableItem(100, "Goal_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(102, "Goal_Current", WORD))
        self._item.append(ct_item.ControlTableItem(104, "Goal_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(108, "Profile_Acceleration", DWORD))
        self._item.append(ct_item.ControlTableItem(112, "Profile_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(116, "Goal_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(120, "Realtime_Tick", WORD))
        self._item.append(ct_item.ControlTableItem(122, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(123, "Moving_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(124, "Present_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(126, "Present_Current", WORD))
        self._item.append(ct_item.ControlTableItem(128, "Present_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(132, "Present_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(136, "Velocity_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(140, "Position_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(144, "Present_Input_Voltage", WORD))
        self._item.append(ct_item.ControlTableItem(146, "Present_Temperature", BYTE))

    def setExtXMItem(self):
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(6, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(7, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(8, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(9, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(10, "Drive_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(11, "Operating_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Secondary_ID", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Protocol_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(20, "Homing_Offset", DWORD))
        self._item.append(ct_item.ControlTableItem(24, "Moving_Threshold", DWORD))
        self._item.append(ct_item.ControlTableItem(31, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(32, "Max Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Min Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "PWM_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Current_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Acceleration_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(44, "Velocity_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(48, "Max_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(52, "Min_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(56, "External_Port_Mode_1", BYTE))
        self._item.append(ct_item.ControlTableItem(57, "External_Port_Mode_2", BYTE))
        self._item.append(ct_item.ControlTableItem(58, "External_Port_Mode_3", BYTE))
        self._item.append(ct_item.ControlTableItem(63, "Shutdown", BYTE))

        self._item.append(ct_item.ControlTableItem(64, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(65, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(68, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(69, "Registered_Instruction", BYTE))
        self._item.append(ct_item.ControlTableItem(70, "Hardware_Error_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(76, "Velocity_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(78, "Velocity_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(80, "Position_D_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(82, "Position_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(84, "Position_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(88, "Feedforward_2nd_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(90, "Feedforward_1st_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(98, "Bus_Watchdog", BYTE))
        self._item.append(ct_item.ControlTableItem(100, "Goal_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(102, "Goal_Current", WORD))
        self._item.append(ct_item.ControlTableItem(104, "Goal_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(108, "Profile_Acceleration", DWORD))
        self._item.append(ct_item.ControlTableItem(112, "Profile_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(116, "Goal_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(120, "Realtime_Tick", WORD))
        self._item.append(ct_item.ControlTableItem(122, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(123, "Moving_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(124, "Present_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(126, "Present_Current", WORD))
        self._item.append(ct_item.ControlTableItem(128, "Present_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(132, "Present_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(136, "Velocity_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(140, "Position_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(144, "Present_Input_Voltage", WORD))
        self._item.append(ct_item.ControlTableItem(146, "Present_Temperature", BYTE))

    def setXHItem(self):
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(6, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(7, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(8, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(9, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(10, "Drive_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(11, "Operating_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(12, "Secondary_ID", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Protocol_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(20, "Homing_Offset", DWORD))
        self._item.append(ct_item.ControlTableItem(24, "Moving_Threshold", DWORD))
        self._item.append(ct_item.ControlTableItem(31, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(32, "Max_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(34, "Min_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(36, "PWM_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Current_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(40, "Acceleration_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(44, "Velocity_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(48, "Max_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(52, "Min_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(63, "Shutdown", BYTE))

        self._item.append(ct_item.ControlTableItem(64, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(65, "LED", BYTE))
        self._item.append(ct_item.ControlTableItem(68, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(69, "Registered_Instruction", BYTE))
        self._item.append(ct_item.ControlTableItem(70, "Hardware_Error_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(76, "Velocity_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(78, "Velocity_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(80, "Position_D_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(82, "Position_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(84, "Position_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(88, "Feedforward_2nd_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(90, "Feedforward_1st_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(98, "Bus_Watchdog", BYTE))
        self._item.append(ct_item.ControlTableItem(100, "Goal_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(102, "Goal_Current", WORD))
        self._item.append(ct_item.ControlTableItem(104, "Goal_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(108, "Profile_Acceleration", DWORD))
        self._item.append(ct_item.ControlTableItem(112, "Profile_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(116, "Goal_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(120, "Realtime_Tick", WORD))
        self._item.append(ct_item.ControlTableItem(122, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(123, "Moving_Status", BYTE))
        self._item.append(ct_item.ControlTableItem(124, "Present_PWM", WORD))
        self._item.append(ct_item.ControlTableItem(126, "Present_Current", WORD))
        self._item.append(ct_item.ControlTableItem(128, "Present_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(132, "Present_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(136, "Velocity_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(140, "Position_Trajectory", DWORD))
        self._item.append(ct_item.ControlTableItem(144, "Present_Input_Voltage", WORD))
        self._item.append(ct_item.ControlTableItem(146, "Present_Temperature", BYTE))

    def setPROItem(self):
        self._item.append(ct_item.ControlTableItem(0, "Model_Number", WORD))
        self._item.append(ct_item.ControlTableItem(6, "Firmware_Version", BYTE))
        self._item.append(ct_item.ControlTableItem(7, "ID", BYTE))
        self._item.append(ct_item.ControlTableItem(8, "Baud_Rate", BYTE))
        self._item.append(ct_item.ControlTableItem(9, "Return_Delay_Time", BYTE))
        self._item.append(ct_item.ControlTableItem(11, "Operating_Mode", BYTE))
        self._item.append(ct_item.ControlTableItem(13, "Homing_Offset", DWORD))
        self._item.append(ct_item.ControlTableItem(17, "Moving_Threshold", DWORD))
        self._item.append(ct_item.ControlTableItem(21, "Temperature_Limit", BYTE))
        self._item.append(ct_item.ControlTableItem(22, "Max_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(24, "Min_Voltage_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(26, "Acceleration_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(30, "Torque_Limit", WORD))
        self._item.append(ct_item.ControlTableItem(32, "Velocity_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(36, "Max_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(40, "Min_Position_Limit", DWORD))
        self._item.append(ct_item.ControlTableItem(44, "External_Port_Mode_1", BYTE))
        self._item.append(ct_item.ControlTableItem(45, "External_Port_Mode_2", BYTE))
        self._item.append(ct_item.ControlTableItem(46, "External_Port_Mode_3", BYTE))
        self._item.append(ct_item.ControlTableItem(47, "External_Port_Mode_4", BYTE))
        self._item.append(ct_item.ControlTableItem(48, "Shutdown", BYTE))

        self._item.append(ct_item.ControlTableItem(562, "Torque_Enable", BYTE))
        self._item.append(ct_item.ControlTableItem(563, "LED_RED", BYTE))
        self._item.append(ct_item.ControlTableItem(564, "LED_GREEN", BYTE))
        self._item.append(ct_item.ControlTableItem(565, "LED_BLUE", BYTE))
        self._item.append(ct_item.ControlTableItem(586, "Velocity_I_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(588, "Velocity_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(594, "Position_P_Gain", WORD))
        self._item.append(ct_item.ControlTableItem(596, "Goal_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(600, "Goal_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(604, "Goal_Torque", WORD))
        self._item.append(ct_item.ControlTableItem(606, "Goal_Acceleration", DWORD))
        self._item.append(ct_item.ControlTableItem(610, "Moving", BYTE))
        self._item.append(ct_item.ControlTableItem(611, "Present_Position", DWORD))
        self._item.append(ct_item.ControlTableItem(615, "Present_Velocity", DWORD))
        self._item.append(ct_item.ControlTableItem(621, "Present_Current", WORD))
        self._item.append(ct_item.ControlTableItem(623, "Present_Input_Voltage", WORD))
        self._item.append(ct_item.ControlTableItem(625, "Present_Temperature", BYTE))
        self._item.append(ct_item.ControlTableItem(626, "External_Port_Mode_1", WORD))
        self._item.append(ct_item.ControlTableItem(628, "External_Port_Mode_2", WORD))
        self._item.append(ct_item.ControlTableItem(630, "External_Port_Mode_3", WORD))
        self._item.append(ct_item.ControlTableItem(632, "External_Port_Mode_4", WORD))
        self._item.append(ct_item.ControlTableItem(890, "Registered_Instruction", BYTE))
        self._item.append(ct_item.ControlTableItem(891, "Status_Return_Level", BYTE))
        self._item.append(ct_item.ControlTableItem(892, "Hardware_Error_Status", BYTE))

    def getControlTableItem(self, num):
        if num in [AX_12A, AX_12W, AX_18A]:
            self.setAXItem()
        elif num in [RX_10, RX_24F, RX_28, RX_64]:
            self.setRXItem()
        elif num == EX_106:
            self.setEXItem()
        elif num in [MX_12W, MX_28]:
            self.setMXItem()
        elif num in [MX_64, MX_106]:
            self.setExtMXItem()
        elif num == MX_28_2:
            self.setMX2Item()
        elif num in [MX_64_2, MX_106_2]:
            self.setExtMX2Item()
        elif num == XL_320:
            self.setXL320Item()
        elif num == XL430_W250:
            self.setXLItem()
        elif num in [XM430_W210, XM430_W350]:
            self.setXMItem()
        elif num in [XM540_W150, XM540_W270]:
            self.setExtXMItem()
        elif num in [XH430_V210, XH430_V350, XH430_W210, XH430_W350]:
            self.setXHItem()
        elif num in [PRO_L42_10_S300_R, PRO_L54_30_S400_R, PRO_L54_30_S500_R,
                     PRO_L54_50_S290_R, PRO_L54_50_S500_R, PRO_M42_10_S260_R,
                     PRO_M54_40_S250_R, PRO_M54_60_S250_R, PRO_H42_20_S300_R,
                     PRO_H54_100_S500_R,PRO_H54_200_S500_R]:
            self.setPROItem()
        else:
            self.setXMItem()
        return self._item

    def getTheNumberOfControlItem(self):
        return len(self._item)
