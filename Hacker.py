"""
File: Hacker.py
Description: Hacker class representing a hacker who manages rigs and digital assets.
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig
from Asset import Asset

class Hacker:
    def __init__(self):
        """
        Attributes:
            __name (str): The hacker's name.
            __rig (Rig or int): The hacker's rig. Defaults to 0 (no rig).
            __trace_level (int): Current trace level of the hacker.
            __inventory (list): List of Asset objects owned by the hacker.
            __crypto_token (int): Number of crypto tokens available for acquiring rigs.
        """
        self.__name = 'Hacker'
        self.__rig = 0
        self.__trace_level = 0
        self.__inventory = []
        self.__crypto_token = 1

    def retrieve_assets(self, asset):
        """
        Adds an Asset to the hacker's inventory if valid.
        asset (Asset): The asset to retrieve.

        Prints:
            Confirmation of retrieval or error if the object is not an Asset.
        """

        if not isinstance(asset, Asset): # Checks to see if it's an asset
            print("not an asset")
            return
        self.inventory.append(asset)
        print(f"{asset}")

    def acquire_rig(self, rig):
        """
        Allows the hacker to acquire a rig if they have sufficient CryptoTokens.
        rig (Rig): The rig to acquire.

        Prints:
            Confirmation of rig activation and remaining crypto tokens.
        """

        if not isinstance(rig, Rig):
            print(f"acquire rig with CryptoToken")
            return

        elif self.crypto_token >= 1:
            self.crypto_token -= 1
            self.rig = rig
            print(f"Rig activation")
            print(f"CryptoToken remaining: {self.crypto_token}")

    def trace_level(self, asset):
        """
        Increases trace level by 1 when an asset is added to the inventory.
        Alerts the hacker if trace level reaches 5.

        Prints:
            Current trace level or exposure warning.
        """
        self.inventory.append(asset)
        self.__trace_level += 1
        print(f"Trace level: {self.hacker_trace_level}")

        if self.hacker_trace_level == 5:
            print(f"EXPOSED, reduce your trace level")

        return self.hacker_trace_level

    def launch_data_spike(self, spike):
        """
        Launches a data spike using the hacker's rig, affecting its damage counter.

        Prints:
            Remaining data spike and sets rig as broken if spike >= 2.
        """

        if spike:
            self.hacker_trace_level += 1
            self.rig.data_spike -= spike
            self.rig.damage_counter += spike
            print(f"amount of data spike remaining {self.rig.data_spike}")

            if spike >= 2:
                self.rig.broken = True

    def extract_asset(self):
        """
        Extracts assets from the rig if the rig is broken.
        Reduces the number of removable drives.

        Prints:
            Status messages and assets being transferred.
        """
        if not self.rig.broken:
            print(f"rig not broken, cannot be extracted")

        elif self.rig.broken:
            self.rig.removable_drive -= 1
            print("rig is broken, using removable drive to extract ")
            print(f"remaining removable drive: {self.rig.removable_drive}")

            for asset in self.rig.rig_storage:
                print(f"transferring {asset} from rig storage")

    def encrypt_assets(self, asset_name):
        """
        Encrypts a specified asset in the inventory if a 'Security Chip' is in inventory.

        Prints:
            Confirmation messages or error if asset/security chip not found.
        """
        for item in self.inventory:
            if item.asset_name == "Security Chip":
                self.inventory.remove(item)

                for asset in self.inventory:
                    if asset.asset_name == asset_name:
                        asset.encrypted = True
                        print(f"{asset_name} Encrypted")
                        return

                print(f"{asset_name} not found in inventory")
                return
        print("requires security chip")

    def upgrade_rig(self):
        """
        Upgrades the hacker's rig if a 'Hardware Patch' is present in inventory.
        Increases rig level and storage.

        Prints:
            Confirmation messages or error if hardware patch not available.
        """
        if self.rig:
            for asset in self.inventory:
                if asset.asset_name == "Hardware Patch":
                    self.inventory.remove(asset)

                    self.rig.upgrade_level += 1
                    self.rig.rig_storage.extend("")
                    print(f"Consumed: {asset.asset_name}")
                    print(f"Rig level: {self.rig.upgrade_level}\n"
                          f"Storage increased")
                    return
            print(f"requires hardware patch to upgrade the rig")

    def search_inventory(self, asset_name):
        """
        Searches for an asset by name in the hacker's inventory.
        Returns:
            Asset if found, else Acquire a rig.

        Prints:
            Status of search results.
        """
        for asset in self.inventory:
            if asset.asset_name == asset_name:
                print(f"Asset found: {asset.asset_name}")
                return asset
        print(f"asset not found in hacker inventory: {asset_name}.")

    def __str__(self):
        """
        Returns a formatted string representation of the hacker.

        Includes:
            Hacker's name, rig name, trace level, and inventory.
        """
        if self.rig:
            rig_name = self.rig.rig.name
        else:
            rig_name = "Acquire a rig"

        inventory_str = []
        for asset in self.inventory:
            inventory_str.append(str(asset))

        return (f"Name: {self.hacker_name}\n"
                f"Rig name: {rig_name}\n"
                f"Trace level: {self.trace_level()}\n"
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
    hacker_name = property(get_name)
    crypto_token = property(get_crypto_token, set_crypto_token)
    hacker_rig = property(get_rig)
    hacker_trace_level = property(get_trace_level, set_trace_level)
    inventory = property(get_inventory)
