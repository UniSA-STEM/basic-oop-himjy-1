"""
File: Rig.py
Description: Rig class representing a hacker's rig used to store and manage assets.
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
import random

class Rig:
    """
    Represents a hacker's rig with damage tracking, upgrade level, storage, and data spike capabilities.

    Attributes:
        __name (str): Name of the rig.
        __damage_counter (int): Tracks damage inflicted on the rig.
        __broken_state (bool): Indicates if the rig is broken.
        __storage (list): Stores Asset objects contained in the rig.
        __data_spike (int): Remaining data spike capacity.
        __removable_drive (int): Number of removable drives available for asset extraction.
        __upgrade_level (int): Level of rig upgrades applied.
    """

    def __init__(self):
        self.__name = "RB26DETT"
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__data_spike = 2
        self.__removable_drive = 1
        self.__upgrade_level = 0

    def storage(self, asset):
        """
         Adds an Asset to the rig's storage if valid.

         Prints:
             Confirmation of storage or error if object is not an Asset.
         """

        if not isinstance(asset, Asset): # Checks to see if it's an asset
            print("not an asset")
            return
        self.__storage.append(asset)
        print(f"{asset}")

    def repair(self, token):
        """
        Repairs the rig using a CryptoToken asset in storage.

        Prints:
            Confirmation of repair or error if token is missing.
        """

        for asset in self.rig_storage:
            if asset.AssetName == "CryptoToken":
                self.rig_storage.remove(asset)
                self.damage_counter = 0
                self.broken = False
                print(f"Rig repaired\n"
                      f"Damage counter: {self.damage_counter}\n"
                      f"Broken state: {self.broken}\n")
                return
        print(f"requires a CryptoToken to repair rig")

    def upgrade(self, hacker):
        """
        Upgrades the rig using a Hardware Patch asset from the hacker's inventory.

        Prints:
            Confirmation of upgrade or error if hardware patch is missing.
        """

        for asset in hacker.inventory:
            if asset.asset_name == "Hardware Patch":
                hacker.inventory.remove(asset)
                self.upgrade_level += 1
                print(f"Rig Upgraded {self.upgrade_level}\n")
                return

            print("No Hardware Patch found in hacker inventory")

    def damaged(self, damage):
        """
        Applies damage to the rig, increasing its damage counter and potentially breaking it.

        Returns:
            bool: True if rig is broken, False otherwise.

        Prints:
            Status of damage and if rig is broken.
        """

        if damage <= 0:
            return

        self.damage_counter += damage
        print(f"Rig has been hit with {damage} Data Spike!!!\n"
              f"Damage counter increased to {self.damage_counter}\n")

        if self.upgrade_level == 0 and self.damage_counter >= 2:
            self.broken = True
            print("Rig is broken")
        elif self.upgrade_level == 1 and self.damage_counter >= 4:
            self.broken = True
            print("Rig is broken")
        return self.broken


    def generate_asset(self):
        """
        Generates a random asset and adds it to the rig storage.

        Prints:
            Name of the generated asset.
        """

        available_assets = [
            ("Security Chip", "Used to encrypt assets."),
            ("Hardware Patch", "Used to upgrade rigs."),
            ("CryptoToken", "Used to acquire or repair rigs."),
            ("Removable Drive", "Used to extract assets.")
        ]

        name, description = random.choice(available_assets)
        generated_asset = Asset(name, description)
        self.rig_storage.append(generated_asset)
        print(f"{generated_asset}")
        return

    def decrypt(self, asset, decrypt):
        """
        Decrypts an asset in rig storage if a Security Chip is present.

            asset (Asset): Asset to decrypt.
            decrypt (bool): True to decrypt, False to prevent transfer.

        Prints:
            Status messages for encryption/decryption process.
        """

        for item in self.rig_storage:
            if item.asset_name == "Security Chip":
                self.rig_storage.remove(item)

        for asset in self.rig_storage:
            if asset.encrypted and not decrypt:
                print(f"cannot be transferred until decrypted.")
                return

            elif asset.encrypted and decrypt:
                asset.encrypted = False
                print(f"{asset.asset_name} has been decrypted.")
                return
        print(f"{asset.asset_name} not encrypted")

    def condition(self):
        """
        Prints the current condition of the rig based on upgrade level and damage.

        Prints:
            'Pristine' if minimal damage and high upgrade level,
            'Broken' otherwise.
        """

        if self.upgrade_level >= 2 and self.damage_counter <1:
            print(f"Rig condition is Pristine (Level {self.upgrade_level})")
        else:
            print(f"Rig condition is Broken (Level {self.upgrade_level})")

    def __str__(self):
        """
        Returns a formatted string representation of the rig.

        Returns:
            str: Name, upgrade level, and stored assets.
        """

        stored_assets = []
        for asset in self.rig_storage:
            stored_assets.append(str(asset))

        return (f"Rig Name: {self.rig_name}\n"
                f"Condition: {self.upgrade_level}\n"
                f"Upgrade Level: {self.upgrade_level}\n"
                f"Stored Assets: {stored_assets}\n")

    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_counter

    def set_damage_counter(self, damage_counter):
        self.__damage_counter = damage_counter

        if damage_counter == 2:
            self.BrokenState = True

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

    rig_name = property(get_name)
    damage_counter = property(get_damage_counter, set_damage_counter)
    broken = property(get_broken_state, set_broken_state)
    rig_storage = property(get_storage)
    data_spike = property(get_data_spike, set_data_spike)
    removable_drive = property(get_removable_drive, set_removable_drive)
    upgrade_level = property(get_upgrade_level, set_upgrade_level)









