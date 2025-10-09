"""
File: Hacker.py
Description: Hacker class
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self):
        self.name = 'Hacker'
        self.CryptoToken = 1
        self.rig = 0
        self.trace_level = 0
        self.inventory = []

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


