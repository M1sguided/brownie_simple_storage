from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("misguided-account")
        print(account)

    # "You can either make a transaction("Transact") or just a call("Call")"
    # print(account)
    # account = accounts.load("theblocdoc-account")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


def main():
    deploy_simple_storage()
