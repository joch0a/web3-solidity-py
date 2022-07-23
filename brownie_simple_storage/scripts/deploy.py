from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()  # --> brownie test accounts
    simple_storage = SimpleStorage.deploy({"from": account})
    tx = simple_storage.store(15, {"from": account})
    tx.wait(1)


def get_account():
    if network.show_active() == "development":
        return accounts[0]  # --> brownie test accounts
    else:
        return accounts.add(
            config["wallets"]["from_key"]
        )  # --> Pulling the information from yaml


def main():
    deploy_simple_storage()
