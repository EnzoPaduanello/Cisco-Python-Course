#a partir daqui ultilizando a função input para a entrada de informações e print como output para a saida de informações


anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something, "\n")



leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo, "\n")



fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".", "\n")#o operador + junta duas strings



print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+\n")#o operador * multiplica uma string, nesse exemplo ele é ultilizado para fazer um quadrado



#atividade para receber um numero em um input realizar operações e depois mostra-las no output
num1 = float(input("Digite um número: "))# input a float value for variable a here
num2 = float(input("Digite outro número: "))# input a float value for variable b here

ad = num1 + num2 
sub = num1 - num2
multi = num1 * num2
divi = num1 / num2
pot = num1 ** num2
restoDiv = num1 % num2

print(num1, "+", num2, "=", ad)# output the result of addition here
print(num1, "-", num2, "=", sub)# output the result of subtraction here
print(num1, "x", num2, "=", multi)# output the result of multiplication here
print(num1, "/", num2, "=", divi)# output the result of division here
print(num1, "elevado à", num2, "=", pot)# output the result of power here
print("O resto da divisão de", num1, "/", num2, "=", restoDiv, "\n")



#atividade para realizar um calculo
x = float(input("Enter value for x: "))

y = 1/(x + 1 /(x + 1 /(x + 1 / x)))

print("y =", y,"\n")



#atividade para calculo de horas
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hourDura = hour + (mins + dura) // 60
minsDura = (mins + dura) % 60

hourSub = hourDura // 24
hourDura -= hourSub * 24 
    
print("\nO evento começará", str(hour) + ":" + str(mins))
print("Durará", dura, "minutos" )
print("E terminará às", str(hourDura) + ":" + str(minsDura))