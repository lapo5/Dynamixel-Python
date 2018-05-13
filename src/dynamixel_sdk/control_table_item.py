#!/usr/bin/env python
# coding: UTF-8

# This Python porting of the original Dynamixel Workbench Toolbox from ROBOTIS
# was written by Patrick Roncagliolo and Marco Lapolla as part of a project
# developed at the DIBRIS BIOLab of the University of Genoa, Italy.

class ControlTableItem:
    def __init__(self, address, item_name, data_length):
        self.address = address
        self.item_name = item_name
        self.data_length = data_length
