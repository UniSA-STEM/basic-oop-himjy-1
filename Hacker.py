"""
File: Hacker.py
Description: Hacker class
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig

class Hacker:
    def __init__(self):
        self.__name = 'Hacker'
        self.__crypto_token = 1
        self.__rig = 0
        self.__trace_level = 0
        self.__inventory = []

    def acquire_rig(self):
        self.rig = Rig()
        self.CryptoToken -= 1
        print(f"Rig activation {self.CryptoToken}")


    def trace_level(self):
        trace_level = self.trace_level + 1
        if trace_level >= 5:
            print(f"Hacker is exposed")

    def launch_data_spike(self):
        pass


    def encrypt_assets(self, security_chip):
        pass


    def upgrade_rig(self, hardware_patch):
        pass


    def store(self):
        pass


    def get_name(self):
        return self.__name

    def get_crypto_token(self):
        return self.__crypto_token

    def set_crypto_token(self, crypto_token):
        self.__crypto_token = crypto_token

    def get_rig(self):
        return self.rig

    def get_trace_level(self):
        return self.trace_level

    def get_inventory(self):
        return self.__inventory

    # Properties
    Name = property(get_name)
    CryptoToken = property(get_crypto_token, set_crypto_token)
    Rig = property(get_rig)
    TraceLevel = property(get_trace_level)
    Inventory = property(get_inventory)
