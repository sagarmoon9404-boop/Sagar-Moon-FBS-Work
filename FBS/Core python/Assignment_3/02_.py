# take input
any_alphbet = input("Enter any alphbet:")
# perform operation
if (any_alphbet in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
    print(f"{any_alphbet} is Vowel")
else :
    print(f"{any_alphbet} is Consonant")