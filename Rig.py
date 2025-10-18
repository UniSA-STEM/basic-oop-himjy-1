"""
File: Rig.py
Description: Rig class
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
import random

class Rig:
    def __init__(self):
        self.__name = "RB26DETT"
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__data_spike = 2
        self.__removable_drive = 1
        self.__upgrade_level = 0

    def storage(self, asset):
        self.Storage.append(asset)

    def repair(self):
        if self.DamageCounter == 0 and self.BrokenState == False:
            print("repaired")
        else:
            print("no repair is needed")

    def upgrade(self, upgrade):
        hardware_patch = upgrade + self.UpgradeLevel
        print(f"Rig has been upgraded with {hardware_patch} hardware patch")
        return hardware_patch

    def data_spike(self, damaged):
        if damaged <= 0:
            return False

        self.DamageCounter += damaged
        print(f"Rig has been hit with {damaged} Data Spike!!!\n"
            f"Damaged counter increased to {self.DamageCounter}")

        if self.DamageCounter >= 2 and self.UpgradeLevel == 0:
            self.BrokenState = True
            print(f"Rig is broken")

        return self.BrokenState


    def generate_asset(self):
        pass


    def __str__(self):
        if self.UpgradeLevel >= 2:
            return f"Rig condition is Pristine (Level {self.UpgradeLevel})"
        else:
            return f"Rig condition is Broken (Level {self.UpgradeLevel})"

    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_counter

    def set_damage_counter(self, damage_counter):
        self.__damage_counter = damage_counter

    def get_broken_state(self):
        return self.__broken_state

    def set_broken_state(self, broken_state):
        self.__broken_state = broken_state

    def get_data_spike(self):
        return self.__data_spike

    def set_data_spike(self, data_spike):

        if data_spike > 5:
            self.__data_spike = 5
        elif data_spike < 0:
            self.__data_spike = 0
        else:
            self.__data_spike = data_spike

    def get_removable_drive(self):
        return self.__removable_drive

    def set_removable_drive(self, driver):
        self.__removable_drive = driver

    def get_upgrade_level(self):
        return self.__upgrade_level

    def set_upgrade_level(self, upgrade_level):
        self.__upgrade_level = upgrade_level

    def get_storage(self):
        return self.__storage

    Name = property(get_name)
    DamageCounter = property(get_damage_counter, set_damage_counter)
    BrokenState = property(get_broken_state, set_broken_state)
    Storage = property(get_storage)
    DataSpike = property(get_data_spike, set_data_spike)
    RemovableDrive = property(get_removable_drive, set_removable_drive)
    UpgradeLevel = property(get_upgrade_level, set_upgrade_level)









