import pytest
from bank import Account

def test_initial_balance():
    account = Account("John Doe", 1000)
    assert account.owner == "John Doe", "Owner should be set correctly"
    assert account.balance == 1000, "Initial balance should be set correctly"

# def test_deposit():
#     pass
#     # TODO

# def test_withdraw():
#     # TODO
#     pass
   
   