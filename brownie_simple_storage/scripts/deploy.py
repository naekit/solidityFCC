from brownie import accounts


def deploy_simple_storage():
    # account = accounts[0] <-- to add from local ganach-cli chain
    # print(account)
    account = accounts.load("freecodecamp-account")


def main():
    deploy_simple_storage()
