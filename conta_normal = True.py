conta_normal = True
conta_universitaria = True
conta_especial = True
saldo = 1000
saque = 3000
cheque_especial = 5000

if conta_normal:
    if saldo >= saque :
        print("Saque realizado com sucesso !")
    elif saque <=(saldo + cheque_especial):
        print("Saque realizado com cheque especial.")
    else:
        print("Não foi possível realizar o saque.Saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso !")
    else:
        print("Saldo insuficiente.")
else:
    print("Sistema não reconheceu o tipo de conta.Entre em contato com o Gerente !")