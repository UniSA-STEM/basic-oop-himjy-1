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
        if not isinstance(asset, Asset): # Checks to see if it's an asset
            print("not an asset")
            return
        self.Inventory.append(asset)
        print(f"{asset}")

    def acquire_rig(self, rig):
        if not isinstance(rig, Rig):
            print(f"acquire rig with CryptoToken")
            return

        elif self.CryptoToken >= 1:
            self.CryptoToken -= 1
            self.rig = rig
            print(f"Rig activation")
            print(f"CryptoToken remaining: {self.CryptoToken}")

    def trace_level(self, asset):
        if self.Inventory.append(asset):
            self.__trace_level += 1
            print(self.TraceLevel)
        if self.TraceLevel == 5:
            print(f"EXPOSED, reduce your trace level")

    def launch_data_spike(self, spike):
        if spike:
            self.rig.DataSpike -= spike
            self.rig.DamageCounter += spike
            print(f"amount of data spike remaining {self.rig.DataSpike}")

            if spike >= 2:
                self.rig.BrokenState = True

    def extract_asset(self):
        if not self.rig.BrokenState:
            print(f"rig not broken, cannot be extracted")

        elif self.rig.BrokenState:
            self.rig.RemovableDrive -= 1
            print("rig is broken, using removable drive to extract ")
            print(f"remaining removable drive: {self.rig.RemovableDrive}")

            for asset in self.rig.Storage:
                print(f"transferring {asset} from rig storage")

    def encrypt_assets(self, asset_name):
        for item in self.Inventory:
            if item.AssetName == "Security Chip":
                self.Inventory.remove(item)

                for asset in self.Inventory:
                    if asset.AssetName == asset_name:
                        asset.Encrypted = True
                        print(f"{asset_name} Encrypted")
                        return

                print(f"{asset_name} not found in inventory")
                return
        print("requires security chip")

    def upgrade_rig(self):
        if self.rig:
            for asset in self.Inventory:
                if asset.AssetName == "Hardware Patch":
                    self.Inventory.remove(asset)

                    self.rig.UpgradeLevel += 1
                    self.rig.Storage.extend("")
                    print(f"Consumed: {asset.AssetName}")
                    print(f"Rig level: {self.rig.UpgradeLevel}\n"
                          f"Storage increased")
                    return
            print(f"requires hardware patch to upgrade the rig")

    def search_inventory(self, asset_name):
        for asset in self.Inventory:
            if asset.AssetName == asset_name:
                print(f"Asset found: {asset.AssetName}")
                return asset
        print(f"asset not found in hacker inventory: {asset_name}.")

    def __str__(self):
        if self.Rig:
            rig_name = self.rig.Name
        else:
            rig_name = "Acquire a rig"

        inventory_str = []
        for asset in self.Inventory:
            inventory_str.append(str(asset))

        return (f"Name: {self.Name}\n"
                f"Rig name: {rig_name}\n"
                f"Trace level: {self.TraceLevel}\n"
                f"Inventory: {inventory_str}")

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

        """
        Set the trace level.
        Caps the value at 5 so it cannot exceed the maximum.
        """
        if trace_level == 5:
            self.__trace_level = 5

    def get_inventory(self):
        return self.__inventory

    # Properties
    Name = property(get_name)
    CryptoToken = property(get_crypto_token, set_crypto_token)
    Rig = property(get_rig)
    TraceLevel = property(get_trace_level, set_trace_level)
    Inventory = property(get_inventory)
