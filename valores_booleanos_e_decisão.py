#(==) siginifica igual a:
var = 0  
print(var == 0)

var = 1  
print(var == 0)


#(!=) seginifica diferente de:
var = 0  
print(var != 0)

var = 1  
print(var != 0)


#(>) significa maior que:
black_sheep = 2
white_sheep = 1
black_sheep > white_sheep


#(<) significa maior que:
black_sheep = 1
white_sheep = 2
black_sheep > white_sheep


#(>= e <=) significa maior ou igual a, e menor ou igual a, respectivamente
black_sheep = 3
white_sheep = 2
black_sheep >= white_sheep
black_sheep <= white_sheep


#Prioridade	crescente	
#1	+, -	unário
#2	**	
#3	*, /, //, %	
#4	+, -	binário
#5	<, <=, >, >=	
#6	==, !=


#Declarações if-else nested

"""if the_weather_is_good:
        if nice_restaurant_is_found:
            have_lunch()
        else:
            eat_a_sandwich()
    else:
        if tickets_are_available:
            o_to_the_theater()
        else:
            go_shopping()"""

#A declaração elif
"""if the_weather_is_good:
        go_for_a_walk()
    elif tickets_are_available:
        go_to_the_theater()
    elif table_is_available:
        go_for_lunch()
    else:
        play_chess_at_home()"""


# A função max() vê o maior numero, já a função min() vê o menor
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

#atividade para tomada de decisão
plant = input("Say Spathiphyllum: ")

if (plant == "Spathiphyllum"):
    resp = "Yes - Spathiphyllum is the best plant ever!"
elif (plant == "spathiphyllum"):
    resp = "No, I want a big Spathiphyllum!"
else:
    resp = f"Spathiphyllum! Not {plant}"
print(resp)



#atividade decisão
income = float(input("Enter the annual income: "))

if (income <= 0):
    tax = 0
elif (income <= 85528):
    tax = ((income * 18) / 100) - 556.2
    if (tax <= 0):
        tax = 0
elif (income > 85528):
    tax = (((income - 85528) * 32) / 100) + 14839.2


tax = float(round(tax, 0))
print(f"The tax is: {tax} thalers")


#atividade decisão para ver se o ano é bissexto
year = int(input("Enter a year: "))

if (year <= 1581):
    year = "Not within the Gregorian calendar period"
elif ((year % 4)!=0):
    year = "Common year"
elif ((year % 100)!=0):
    year = "Leap year"
elif ((year % 400)!= 0):
    year = "Common year"
else:
    year = "Leap year"

print(year)


