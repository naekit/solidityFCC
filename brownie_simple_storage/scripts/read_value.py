# this will read from rinkeby blockchain
# terminal command -- brownie run scripts/read_value.py --network rinkeby
from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    # to get most recent deployment put -1 (index that's one less the length)
    # ABI - brownie already has both things needed to interact w contract
    # Address
    print(simple_storage.retrieve())


def main():
    read_contract()
