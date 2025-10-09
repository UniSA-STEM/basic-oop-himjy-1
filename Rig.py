"""
File: Rig.py
Description: Rig class
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self):
        self.__name = "Rig"
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = 0
        self.__data_spike = 2
        self.__removeable_drive = 1
        self.__upgrade_level = 0

    def repaired(self):
        if self.DamageCounter == 0 and self.BrokenState == False:
            print(f"damaged")
        else:
            print(f"no repair is needed")




    def upgraded(self):
        pass

    def data_spike(self):
        pass

    def generate_asset(self):
        pass

    def store(self):
        pass

    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_counter

    def set_damage_counter(self, damage_counter):
        self.__damage = damage_counter

    def get_broken_state(self):
        return self.__broken_state

    def get_storage(self):
        return self.__storage

    def get_data_spike(self):
        return self.__data_spike

    def set_data_spike(self, data_spike):
        self.__data_spike = data_spike

    def get_removeable_drive(self):
        return self.__removeable_drive

    def get_upgrade_level(self):
        return self.__upgrade_level

    Name = property(get_name)
    DamageCounter = property(get_damage_counter, set_damage_counter)
    BrokenState = property(get_broken_state)
    Storage = property(get_storage)
    DataSpike = property(get_data_spike, set_data_spike)
    RemoveableDrive = property(get_removeable_drive)
    UpgradeLevel = property(get_upgrade_level)








