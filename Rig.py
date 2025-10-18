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
        self.__name = "Rig"
        self.__damage_counter = 0
        self.__broken_state = False
        self.__upgrade_level = 0
        self.__storage = []

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
        if damaged:
            self.DamageCounter += damaged
            print(f"Rig has been hit with {damaged} Data Spike!!!\n"
                  f"Damaged counter increased to {self.DamageCounter}")

            if self.DamageCounter >= 2 and self.UpgradeLevel == 0:
                print(f"Rig is broken")
        return damaged


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


    def get_data_spike(self):
        return self.__data_spike

    def set_data_spike(self, data_spike):
        self.__data_spike = data_spike

    def get_removeable_drive(self):
        return self.__removeable_drive

    def get_upgrade_level(self):
        return self.__upgrade_level

    def set_upgrade_level(self, upgrade_level):
        self.__upgrade_level = upgrade_level

    def get_storage(self):
        return self.__storage

    Name = property(get_name)
    DamageCounter = property(get_damage_counter, set_damage_counter)
    BrokenState = property(get_broken_state)
    UpgradeLevel = property(get_upgrade_level, set_upgrade_level)
    Storage = property(get_storage)








