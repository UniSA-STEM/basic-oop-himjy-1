"""
File: Asset.py
Description: Asset class
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def crypto_token(self):
        pass

    def data_spike(self):
        pass

    def removeable_drive(self):
        pass

    def security_chip(self):
        pass

    def hardware_patch(self):
        pass

    def __str__(self):
        if self.Encrypted:
            return f"{self.Name} {self.Description} Encrypted"
        else:
            return f"{self.Name} {self.Description}"

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    def set_encrypted(self, encrypted):
        self.__encrypted = encrypted

    Name = property(get_name)
    Description = property(get_description)
    Encrypted = property(get_encrypted, set_encrypted)


