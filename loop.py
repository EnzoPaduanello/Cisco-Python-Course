odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)


#Atv com uso da função while 
secret_number = 777

number = 1

while number != secret_number:
    number = print(int(input(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)))
print("Congratulations")


#while com exponenciação
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2


#atividade com for
time = int(input("Digite a quantidade de rios: "))

for i in range(1,time):
    i += 1
    print(i,"mississipi")
    

#break and continue
# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


#atividade usando break
while True:
    palavra = input("Digite a palavra secreta: ")
    palavra = palavra.upper()
    
    if palavra == "CHUPACABRA":
        print("Parabéns a palavra era chupacabra")
        break


#atividade usando continue para tirar as vogais das palavras usando o comando letter
user_word = input("Digite uma palavra: ")
user_word = user_word.upper()
for letter in user_word:
    if letter in 'AEIOU':
        continue
    print(letter)



#atividade para tirar vogais de uma string em uma variavel e coloca-las em outra
word_without_vowels = ""
word_without_consoants = ""
# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Digite uma palavra: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        word_without_consoants += letter
        continue
    word_without_vowels += letter
    

# Print the word assigned to word_without_vowels.
print(word_without_vowels)
print(word_without_consoants)


#os loops podem ter o ramo else também, como if.
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#mais um exemplo
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)


#atividade para ver a quantidade de blocos da base da pirâmide
blocks = int(input("Digite o número de blocos: "))

# Inicializar variáveis
height = 0
current_layer = 1

while blocks >= current_layer:
    blocks -= current_layer
    current_layer += 1
    height += 1

print("A altura da pirâmide:", height)


#atividade para uso de logica com variavel
c0 = int(input("Digite um número natural: "))
steps = 0

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    steps += 1

print(1)


print(f"Passos necessários para alcançar o objetivo: {steps}")