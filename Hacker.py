"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Jamie Him
ID: 110375225
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    def __init__(self):
        self.name = 'Hacker'
        self.CryptoToken = 1
        self.rig = 0
        self.trace_level = 0

    def trace_level(self):
        trace_level = self.trace_level + 1
        if trace_level >= 5:
            print(f"Hacker is exposed")

