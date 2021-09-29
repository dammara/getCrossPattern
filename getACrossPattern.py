# Markhus Dammar
# 29 September 2021
# This program will take 2 user inputted symbols and create a cross pattern  with them


def getACrossPattern(firstSymbol, secondSymbol):
    cross_template = "\t{}\n{}\t\t{}\n\t{}"
    print(cross_template.format(firstSymbol, secondSymbol, secondSymbol, firstSymbol))


firstSymbol = input("Please enter a symbol >>> ")
secondSymbol = input("Please enter a second symbol >>> ")

getACrossPattern(firstSymbol, secondSymbol)
