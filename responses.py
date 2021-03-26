
responses = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    responce = input('Wich mountain would like to clim somebody? ')
    responses[name] = responce  # sochranyaetcya v slovare
    repeat = input("Would you like to le another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print('\n___Poll results___')
for name, responce in responses.items():
    print(f"{name} would like to climb {responce}.")