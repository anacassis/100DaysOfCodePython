#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#12/100 = 12/100  150 * 1.2 / 18.0 / 150+18 = 168

#Welcome to the tip calculator!
#What was the total bill?
#How much tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 7


print("Welcome tothe tip calculator!")
total= float(input("What was the total bill? $"))
gorjeta =int(input(f"How much tip would you like to give? 10 ,  12, or 15?"))
pessoas =int(input("How many people to split the bill?"))

tip_porcentagem = gorjeta / 100
total_gasto_porc = total * tip_porcentagem
total_gasto = total + total_gasto_porc
total_gasto_pessoa = total_gasto / pessoas
valor_final = round(total_gasto_pessoa,2)

print(f" Cada pessoa deve pagar ${valor_final}")

