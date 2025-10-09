"""
File: Asset.py
Description: Asset class
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self):
        self.name = "asset"
        self.description = ""
        self.encrypted = False

    def __str__(self):
        if self.encrypted:
            return f"{self.name} {self.description} Encrypted"
        else:
            return f"{self.name} {self.description}"


