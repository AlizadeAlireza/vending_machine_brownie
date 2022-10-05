from brownie import network, accounts, config


def menu():
    print("1, enter name ")
    print("2, get the multiple")
    print("3, help")
    print("4, quit from program")


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def help():
    print("help me")


def multiply():
    print(f"your number is :  {2 * 2}")
