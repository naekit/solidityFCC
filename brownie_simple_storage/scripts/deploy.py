from brownie import accounts, config, SimpleStorage, network
import os


# 10 lines to deploy, retrieve, transact in brownie
def deploy_simple_storage():
    # V-V-V to add from local ganach-cli chain
    # account = accounts[0]
    account = get_account()
    # this step of deploying is much quicker than web3.py
    # b4 we had to get ABI, nonce, create contract, create transaction, sign, and send
    # brownie knows to Transact or Call also line 15 V-V
    # this will return a contract object line 78 in web3.py
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    # retrieve VIEW function call in brownie
    stored_value = simple_storage.retrieve()
    print(stored_value)
    # transact with store function and wait for the transaction
    transaction = simple_storage.store(13, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)
    # NEXT IS TESTING better to write in python vs solidity
    # V-V-V add account from brownie encrypted metamask account we put the private key in for
    # account = accounts.load("fccsolidity")
    # print(account)
    # V-V-V add metamask account from local .env file configured in .yaml file
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


# import network keyword, and check which network account should deploy on
def get_account():
    if network.show_active() == "development":
        return accounts(0)
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
