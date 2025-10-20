"""
File: Asset.py
Description: This class represents a digital asset for the hacker and rig.
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        """
                Initializes a new Asset instance with a name and description.
        """

        self.__name = name                          # Private attribute for the asset name
        self.__description = description            # Private attribute for the asset description
        self.__encrypted = False                    # Indicates whether the asset is encrypted

        """
        Attributes:
            __name (str): The name of the asset.
            __description (str): A description of the asset.
            __encrypted (bool): Indicates whether the asset is encrypted.
        """

    # Returns a formatted string containing asset details.
    def __str__(self):
        if self.Encrypted:
            return f"{self.AssetName}: {self.Description} Encrypted"
        else:
            return f"{self.AssetName}: {self.Description}"

    # Getters for encapsulated data
    def get_name(self):
        """Returns the name of the asset."""

        return self.__name

    def get_description(self):
        """Returns the description of the asset."""

        return self.__description

    def get_encrypted(self):
        """Returns True if the asset is encrypted, False otherwise."""

        return self.__encrypted

    # Setter for encryption property
    def set_encrypted(self, encrypted):

        """
        Updates the encryption status of the asset.
        """

        self.__encrypted = encrypted

    # Properties to access private attributes
    AssetName = property(get_name)
    Description = property(get_description)
    Encrypted = property(get_encrypted, set_encrypted)


