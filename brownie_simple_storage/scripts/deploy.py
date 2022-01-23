from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    # V-V-V to add from local ganach-cli chain
    account = accounts[0]
    # this step of deploying is much quicker than web3.py
    # b4 we had to get ABI, nonce, create contract, create transaction, sign, and send
    # brownie knows to Transact or Call
    SimpleStorage.deploy({"from": account})
    # V-V-V add account from brownie encrypted metamask account we put the private key in for
    # account = accounts.load("fccsolidity")
    # print(account)
    # V-V-V add metamask account from local .env file configured in .yaml file
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


def main():
    deploy_simple_storage()
