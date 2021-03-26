
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print(f"The folloving languages have been mentioned:")

for languages in set(favorite_languages.values()): # set()- mnogestva - izvlekaet dublikaty
    print(languages.title())