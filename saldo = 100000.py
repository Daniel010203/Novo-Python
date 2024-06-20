saldo = 100
saque = 50

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao se realizar o saque")