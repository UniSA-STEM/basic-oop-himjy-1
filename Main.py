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

a1 = Asset("CryptoToken", "Used to acquire or repair rigs")
a2 = Asset("SecretFile", "Top secret")

assets = [a1, a2]
Hacker.retrieve_assets(assets[1])


rig = Rig()
rig.Storage = a1


Hacker.acquire_rig()
Hacker.launch_data_spike(5)
rig.data_spike(2)



#    Hacker.launch_data_spike()
 #   Hacker.launch_data_spike()
  #  Hacker.launch_data_spike()
   # Hacker.launch_data_spike()
#Hacker.trace_level()

#rig = Rig()
#rig.repaired(0)
#rig.upgraded(1)
#rig.data_spike(3)
#rig = Rig()
#print(rig)


#print(a)
#a.crypto_token()
#a.data_spike()

