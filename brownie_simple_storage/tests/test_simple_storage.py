from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy({"from": account})

    # Assert
    start_value = simple_storage.retrieve()  # assert 0
    expected = 0

    assert start_value == expected


def test_update_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})
    end_value = simple_storage.retrieve()

    # assert
    assert end_value == expected
