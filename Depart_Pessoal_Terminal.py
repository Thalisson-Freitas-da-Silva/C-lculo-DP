#---------------------------------------------------------------------------------
# Departamento Pessoal - Thalisson Freitas da Silva | Antonio Batista da Silva
#---------------------------------------------------------------------------------

# Separação por funções
print("-"*15)
OPC = int(input("Digite 1 - Ganho Diário\nDigite 2 - Cálculo de férias\nDigite 3 - Para o cálculo do 13° Salário: "))
print("-"*15)

# Valor ganho mensal
GANHO_MENSAL = float(input("Digite o valor ganho por mês: R$ "))

# Meses trabalhados
MESES_TRABALHADOS = int(input("Digite a quantidade de meses trabalhados: "))

# Ganho Diário e Mensal
if OPC == 1:
    GANHO_DIARIO = GANHO_MENSAL / 30
    print("Ganho Diário: ","{:.2f}".format(GANHO_DIARIO))
# Cálculo de Férias
elif OPC == 2:
    PROPORCIONAL_FERIAS = ((GANHO_MENSAL/12)*MESES_TRABALHADOS)
    FERIAS_TOTAL = ((PROPORCIONAL_FERIAS/3)+PROPORCIONAL_FERIAS)
    print("Minhas Férias serão R$ ","{:.2f}".format(FERIAS_TOTAL))
# Cálculo de décimo terceiro
elif OPC == 3:
    DECIMO_TERCEIRO = ((GANHO_MENSAL/12)*MESES_TRABALHADOS)
    print("O decimo terceiro é igual a R$ ", "{:.2f}".format(DECIMO_TERCEIRO))
else:
    print("-"*15)
    print("FIM DO PROGRAMA")
    print("-"*15)