from __future__ import annotations
from typing import List, Dict


class BankAccount:
    accounts: Dict[str, BankAccount] = {}

    def __init__(self, account_number, account_type, currency, balance=0.0):
        self._account_number = account_number
        self._account_type = account_type
        self._balance = balance
        self._currency = currency
        self.accounts[account_number] = self

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_type(self):
        return self._account_type

    @property
    def currency(self):
        return self._currency

    @property
    def balance(self):
        return self._balance

    @account_type.setter
    def account_type(self, new_type):
        if new_type not in ("savings", "checking"):
            raise ValueError("Account type must be either \"savings\" or \"checking\".")
        self._account_type = new_type

    @balance.setter
    def balance(self, new_balance):
        if not isinstance(new_balance, (int, float)):
            raise TypeError("Amount must be a number.")
        self._balance = new_balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Please enter a non-negative amount.")
        if not isinstance(amount, float):
            raise TypeError("Amount must be a floating-point number.")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Please enter a non-negative amount.")
        if not isinstance(amount, float):
            raise TypeError("Amount must be a floating-point number.")
        if amount > self._balance:
            raise Exception(f"Insufficient funds. The current account balance is {self._balance} {self._currency}")
        self._balance -= amount

    @classmethod
    def from_dict(cls, data: dict):
        return cls(account_number=data["account_number"], account_type=data["account_type"],
                   currency=data["currency"],
                   balance=data.get("balance", 0.0))

    @classmethod
    def multiple_accounts(cls, multi_data: List[Dict]):
        for data in multi_data:
            cls(account_number=data["account_number"], account_type=data["account_type"],
                currency=data["currency"], balance=data.get("balance", 0.0))

    def update_attribute(self, attr_name, value):
        if attr_name in ("account_number", "currency"):
            raise Exception("Cannot modify this attribute.")
        if hasattr(self, attr_name):
            setattr(self, attr_name, value)
        else:
            raise Exception("Invalid attribute.")
