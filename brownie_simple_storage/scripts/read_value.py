from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]  # Latest deployment
    # ABI -> stored on build/contracts/SimpleStorage.json
    # Address -> stored on build/deployments/4/{address}

    current_value = simple_storage.retrieve()
    print("Current value: {}".format(current_value))


def update_contract():
    simple_storage = SimpleStorage[-1]  # Latest deployment
    # ABI -> stored on build/contracts/SimpleStorage.json
    # Address -> stored on build/deployments/4/{address}

    tx = simple_storage.store(31, {"from": accounts.add(config["wallets"]["from_key"])})
    tx.wait(1)
    print(tx)


def main():
    read_contract()
    # update_contract()
