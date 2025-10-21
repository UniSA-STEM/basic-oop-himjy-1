from Hacker import Hacker
from Rig import Rig
from Asset import Asset

crypto_token = Asset("CryptoToken", "Used to acquire or repair rigs")
data_spike = Asset("Data Spike", "Used in battle")
removable_drive = Asset("Removable Drive", "Used for extraction.")
security_chip = Asset("Security Chip", "Used to encrypt or decrypt assets")
hardware_patch = Asset("Hardware Patch", "Used to upgrade rigs.")

#Upgrade rig
print("UPGRADE RIG")
hacker_class = Hacker()
my_rig = Rig()

# acquire rig
hacker_class.acquire_rig(my_rig)

# Add hardware patch to inventory
hacker_class.retrieve_assets(hardware_patch)

# Call the function to upgrade the rig
my_rig.upgrade(hacker_class)


print("ENCRYPT")
# Create hacker and rig
hacker_class2 = Hacker()
my_rig2 = Rig()

hacker_class2.acquire_rig(my_rig2)

# Add a security chip and a data asset to inventory
hacker_class2.retrieve_assets(security_chip)
hacker_class2.retrieve_assets(data_spike)

# Encrypt asset in inventory
hacker_class2.encrypt_assets("Data Spike")

# Place crypto token into rig storage
my_rig2.storage(data_spike)

print('\n')
print('TRACE MANAGEMENT')
hacker_class3 = Hacker()
my_rig3 = Rig()

# Add a crypto token to inventory so rig can be acquired
hacker_class3.retrieve_assets(crypto_token)
hacker_class3.acquire_rig(my_rig3)

# Adding assets to inventory simulates risky actions
hacker_class3.trace_level(crypto_token)
hacker_class3.trace_level(crypto_token)
hacker_class3.trace_level(crypto_token)
hacker_class3.trace_level(crypto_token)
hacker_class3.trace_level(crypto_token)

print('\n')
print("SIMULATED BATTLE")
hacker_class4 = Hacker()
my_rig4 = Rig()

hacker_class4.retrieve_assets(crypto_token)
hacker_class4.acquire_rig(my_rig4)

# launch data spikes
hacker_class4.launch_data_spike(2)

# Verify rig condition
my_rig4.condition()

# Extract from rig storage
hacker_class4.extract_asset()

# Generate assets fromt the rig
print('GENERATE ASSET')
my_rig5 = Rig()
my_rig5.generate_asset()
my_rig5.generate_asset()
my_rig5.generate_asset()
my_rig5.generate_asset()