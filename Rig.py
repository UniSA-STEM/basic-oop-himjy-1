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
        self.__damage = 0
        self.__broken_state = False
        self.__storage = 0
        self.__data_spike = 2
        self.__removeable_drive = 1
        self.__upgrade_level = 0

    def repaired(self):
        pass

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

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage = damage

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
        return self.

    Name = property(get_name)
    Damage = property(get_damage, set_damage)
    BrokenState = property(get_broken_state)
    Storage = property(get_storage)
    DataSpike = property(get_data_spike, set_data_spike)
    RemoveableDrive = property(get_removeable_drive)
    UpgradeLevel = property(get_upgrade_level)








