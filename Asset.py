"""
File: Asset.py
Description: This class represents a digital asset for the hacker and rig.
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):          # Asset constructor
        self.__name = name                          # Private attribute for the asset name
        self.__description = description            # Private attribute for the asset description
        self.__encrypted = False                    # Indicates whether the asset is encrypted

    # Returns a formatted string containing asset details.
    def __str__(self):
        if self.Encrypted:
            return f"{self.Name}: {self.Description} Encrypted"
        else:
            return f"{self.Name}: {self.Description}"

    # Getters for encapsulated data
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    # Setter for encryption property
    def set_encrypted(self, encrypted):
        self.__encrypted = encrypted

    # Properties to access private attributes
    Name = property(get_name)
    Description = property(get_description)
    Encrypted = property(get_encrypted, set_encrypted)


