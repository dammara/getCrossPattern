# Markhus Dammar
# 29 September 2021
# This program will take 2 user inputted symbols and create a cross pattern  with them


def getACrossPattern(firstSymbol, secondSymbol):
    cross_template = "\t{}\n{}\t\t{}\n\t{}"
    print(cross_template.format(firstSymbol, secondSymbol, secondSymbol, firstSymbol))


user_symbol_1 = input("Please enter a symbol >>> ")
user_symbol_2 = input("Please enter a second symbol >>> ")

getACrossPattern(user_symbol_1, user_symbol_2)
