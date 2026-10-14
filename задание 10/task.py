class BankError(Exception):
    def __init__(self):
        pass
class InvalidAmountError(BankError):
    def __init__(self):
        super().__init__()
class InsufficientFundsError(BankError):
    def __init__(self):
        super().__init__()
class AccountBlockedError(BankError):
    def __init__(self):
        super().__init__()
def withdraw(balance,amount):
    if amount <= 0:
        raise InvalidAmountError("Снимтие положительное число средств.")
    elif balance - amount < 0:
        raise InsufficientFundsError("Недостаточно средств")
    else:
        print("Успешный выввод")
        return (balance - amount)
balance = 100_000
while True:
    amount = int(input(f"Ваш баланс {balance}. Введите сумму, которую хотите снять " ))
    balance = withdraw(balance,amount)
