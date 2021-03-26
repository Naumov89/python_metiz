
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit? to end the program. "
message = ""    # bez etoy stroki python ne moget sravnit'. KOD NE BUDET RABOTAT'

while message != 'quit':
    message = input(prompt)
    print(message)

#############################################################################

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit? to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':   # ne vuvoditcja soobschenie 'quit'
        print(message)

##############################################################################

ompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit? to end the program. "

active = True                  # Flag
while active:
    message = input(prompt)
    if message == 'quit':
        active = False         # Flag
    else:
        print(message)

##############################################################################

prompt = "\nPlease enter the name of a city you have visited."
prompt += "\nEnter 'quit? to end the program. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go {city.title()}.")