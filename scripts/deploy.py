from brownie import accounts, config, VendingMachine, network
from web3 import Web3
from scripts.helpful_sctripts import get_account


def deploy_vending_machine():

    # print("\nthe first step of deploy_vending_machine\n")
    account = get_account()
    account_1 = accounts[1]
    print(f"the current account that we use is : {account}")

    # deploy contract
    vending_machine = VendingMachine.deploy({"from": account})
    print(
        f"\nthe first full balance of our machine is : {vending_machine.donutBalances(vending_machine.address)}\n"
    )

    # get amount of donuts
    print(f"\nthe current amount is:  {vending_machine.getVendingMachineBalance()}\n")

    # restock amount of donuts
    restock_amount = 10
    vending_restock = vending_machine.restock(restock_amount, {"from": account})
    vending_restock.wait(1)
    print(
        f"\nadded {restock_amount} to the vending machine and the current amount is:  {vending_machine.getVendingMachineBalance()}\n"
    )

    # purchase donuts
    donate_amount = 2
    donate_price = donate_amount * 2
    purchase_donuts = vending_machine.purchase(
        donate_amount,
        {"from": account, "value": Web3.toWei(donate_price, "ether")},
    )
    purchase_donuts.wait(1)
    print(
        f"the account with this address {account} buy {donate_amount} donut at the cost of {donate_price} ether.\n"
    )
    print(f"the left over donuts are : {vending_machine.getVendingMachineBalance()}\n")
    # buyer tracking
    print(
        f"this account {account} purchase until now is: {vending_machine.donutBalances(account)}"
    )


def main():
    deploy_vending_machine()
