from brownie import accounts, config
import os


def deploy_simple_storage():
    # account = accounts[0] <-- to add from local ganach-cli chain
    # print(account)
    # account = accounts.load("fccsolidity")
    # print(account)
    account = accounts.add(config["wallets"]["from_key"])
    print(account)


def main():
    deploy_simple_storage()
