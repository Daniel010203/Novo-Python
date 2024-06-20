maior_idade = 18
idade_especial = 17
idade = int(input("Informe sua idade: "))
if idade >= maior_idade:
    print("Pode tirar CNH.")
elif idade == idade_especial:
    print("Pode fazer aulas tetóricas somente.")
else:
    print("Ainda não pode tirar a CNH.")


