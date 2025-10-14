"""
File: main.py
Description: Used for testing to simulate battles, upgrades, encryption and trace management.
Author: Jamie Him
ID: 110375225
Username: Himjy003
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset


Hacker = Hacker()
Hacker.acquire_rig()
#    Hacker.launch_data_spike()
#    Hacker.launch_data_spike()
 #   Hacker.launch_data_spike()
  #  Hacker.launch_data_spike()
   # Hacker.launch_data_spike()
#Hacker.trace_level()

rig = Rig()
rig.repaired(0)
rig.upgraded(1)
rig.data_spike(3)