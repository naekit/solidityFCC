# Make sure to add test, pytest will look for that syntax for file name
# set it up like we set up the deploy function
from brownie import SimpleStorage, accounts


def test_deploy():
    # testing is always seperated into 3 categories
    # Arrange - set up what we need
    account = accounts[0]
    # Act - execute the contract
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert - check if everything is lined up
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 13
    simple_storage.store(expected, {"from": account})
    # Assert
    assert expected == simple_storage.retrieve()
