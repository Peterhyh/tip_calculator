welcome_msg = 'Welcome to the tip calculator.'
print(welcome_msg)

bill_total = float(input('What was the total of the bill? $'))

user_percent_input = float(
    input('What percentage tip would you like to give? '))

num_people = int(input('How many people to split the bill? '))

tip = (bill_total * user_percent_input)/100

total = bill_total + tip

individual_bill = round(total/num_people, 2)

print('Each person should pay $' + str(individual_bill))
