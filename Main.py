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

hacker = Hacker()
rig = Rig()

CryptoToken = Asset("CryptoToken", "Used to acquire or repair rigs")
DataSpike = Asset("Data Spike", "Used in battle")
RemovableDrive = Asset("Removable Drive", "Found in rigs and used for extrac�on.")
SecurityChip = Asset("Security Chip", "Used to encrypt or decrypt assets")
HardwarePatch = Asset("Hardware Patch", "Used to upgrade rigs.")


assets = [CryptoToken, DataSpike, RemovableDrive, SecurityChip, HardwarePatch]
hacker.retrieve_assets(CryptoToken)
hacker.retrieve_assets(DataSpike)
hacker.retrieve_assets(HardwarePatch)
hacker.retrieve_assets(SecurityChip)



rig.storage(DataSpike)

hacker.acquire_rig(rig)
hacker.launch_data_spike(2)
hacker.extract_asset()
hacker.search_inventory("CryptoToken")
hacker.search_inventory("Data Spike")
hacker.search_inventory("Hardware Patch")
hacker.search_inventory("Security Chip")
hacker.upgrade_rig()
hacker.encrypt_assets("CryptoToken")

for asset in hacker.Inventory:
    print(asset)


