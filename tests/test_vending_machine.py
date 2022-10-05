from brownie import config, accounts, VendingMachine
from scripts.helpful_sctripts import get_account
from web3 import Web3


def test_first_balance():
    """
    in this section we want to know that if first balance is 100 or not?!
    """
    # arrange
    account = get_account()

    # act
    vending_machine = VendingMachine.deploy({"from": account})

    # assert
    first_donut_balance = 100

    assert vending_machine.getVendingMachineBalance() == first_donut_balance


def test_only_owner():

    """
    we show that the admin is the deployer or not?!
    """
    # arrange
    account = get_account()

    # act
    vending_machine = VendingMachine.deploy({"from": account})

    # assert
    assert vending_machine.owner() == account
    assert vending_machine.owner() != accounts[1]


def test_admin_can_restock():
    """
    just admin can restock the amount of the machine and by admin restock the balance
    increase.
    """
    # arrange
    admin = get_account()
    buyer = accounts[1]

    # act
    vending_machine = VendingMachine.deploy({"from": admin})

    restock_amount_from_admin = 2
    restock_amount_from_buyer = 2

    vending_machine_default_balance = vending_machine.getVendingMachineBalance()

    vending_machine.restock(restock_amount_from_admin, {"from": admin})
    # vending_machine.restock(restock_amount_from_buyer, {"from": buyer})

    assert (
        vending_machine.getVendingMachineBalance()
        == vending_machine_default_balance + restock_amount_from_admin
    )
    assert vending_machine.owner() == admin.address
    assert vending_machine.owner() != buyer.address


def test_update_amount_restock():
    """
    we want to see if we restock the amount, it will be increased or not
    """
    # arrange
    contract_deployer = get_account()

    # act
    vending_machine = VendingMachine.deploy({"from": contract_deployer})

    vending_machine_primitive_amount = vending_machine.getVendingMachineBalance()
    restock_amount = 2
    restock = vending_machine.restock(restock_amount, {"from": contract_deployer})
    assert (
        vending_machine.getVendingMachineBalance()
        == vending_machine_primitive_amount + restock_amount
    )
    # assert (
    #     vending_machine.restock(restock_amount, {"from": contract_deployer})
    #     == vending_machine_primitive_amount + restock_amount
    # )


def test_purchase_everyone_tracking_and_decrease_amount():
    # arrange

    admin = accounts[0]
    buyer = accounts[1]

    # act
    vending_machine = VendingMachine.deploy({"from": admin})
    donate_price = 2
    donate_amount = 1

    vending_machine_primitive_amount = vending_machine.getVendingMachineBalance()  # 100

    admin_purchase = vending_machine.purchase(
        donate_amount, {"from": admin, "value": Web3.toWei(donate_price, "ether")}
    )
    admin_purchase.wait(1)

    buyer_purchase = vending_machine.purchase(
        donate_amount, {"from": buyer, "value": Web3.toWei(donate_price, "ether")}
    )

    remain_amount = vending_machine.getVendingMachineBalance()  # 98

    assert remain_amount == vending_machine_primitive_amount - 2
