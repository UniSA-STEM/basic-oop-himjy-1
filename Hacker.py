"""
File: Hacker.py
Description: Hacker class
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig
from Asset import Asset

class Hacker:
    def __init__(self):
        self.__name = 'Hacker'
        self.__rig = 0
        self.__trace_level = 0
        self.__inventory = []
        self.__crypto_token = 1

    def retrieve_assets(self, asset):
        self.Inventory.append(asset)
        print(self.Inventory)

    def acquire_rig(self, token):
        self.rig = Rig()
        self.CryptoToken -= 1
        print(f"Rig activation")
        print(f"CryptoToken: {self.CryptoToken}")

    def trace_level(self):
        if self.TraceLevel == 5:
            print(f"EXPOSED, reduce your trace level")

    def repair(self):
        rig = Rig()
        if rig.DamageCounter == 0 and rig.BrokenState == False:
            self.CryptoToken -= 1
            print("repaired")
        else:
            print("no repair is needed")

    def launch_data_spike(self, spike):
        self.rig = Rig()

        if spike:
            print(f"launching {spike} Data Spikes")

            self.rig.DataSpike -= spike
            print(f"Remaining Data spike in rig: {self.rig.DataSpike}")

            self.TraceLevel += spike
            if self.TraceLevel == 5:
                print(self.TraceLevel)


        print(f"Hacker trace level: {self.TraceLevel}")





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
        return self.__trace_level

    def set_trace_level(self, trace_level):
        self.__trace_level = trace_level

    def get_inventory(self):
        return self.__inventory

    # Properties
    Name = property(get_name)
    CryptoToken = property(get_crypto_token, set_crypto_token)
    Rig = property(get_rig)
    TraceLevel = property(get_trace_level, set_trace_level)
    Inventory = property(get_inventory)
