import os
import math
import time
import sys
import random
from statistics import *
import webbrowser
os.system("title Caluclator")
def goback():
    input("Press Enter to Go Back to The Start...")
    os.system("cls")

# def clean_units(unit):
    # unit = unit.rstrip('s')  # remove plural
    # words_to_remove = ['m', 'l', 'g']  # remove type of unit
    # for word in words_to_remove:
        # unit = unit.replace(word, '')
    # return unit

def convert(val, unit_in, unit_out=''):
    SI = {'mm': 0.001, 'cm': 0.01, 'm': 1,
          'i': 0.00393701, 
          'deci': 0.1, '': 1.0, 'deka': 10,
          'hecto': 100, 'kilo': 1000, 'l': 1000, 'ml': 1,
          'mi': 1609, 'km': 1000, 'g': 1, 'kg': 1000, 'p': 453.592}
    return val*SI[unit_in]/SI[unit_out]

def simplify_fraction(numerator, denominator):
    if math.gcd(numerator, denominator) == denominator:
        return int(numerator/denominator)
    elif math.gcd(numerator, denominator) == 1:
        return str(numerator) + "/" + str(denominator)
    else:
        top = numerator / math.gcd(numerator, denominator)
        bottom = denominator / math.gcd(numerator, denominator)
        return str(top) + "/" + str(bottom)

while True:
    try:
        os.system("cls")
        print("Welcome to the Calculator!")
        print("==========V 1 (Python)==========")
        print("PI")
        print("E")
        print("POW")
        print("SQRT")
        print("Square")
        print("Round")
        print("ABS")
        print("AVG")
        print("Conv for Conversions")
        print("Guess for the Guessing Game")
        print("Simp for Simplify Fractions")
        sum = input("Please enter your sum(Type ? for information)- ")
        sum = sum.lower()
        if "=" in sum:
            sum = sum.split("=")
            calc1 = sum[0]
            calc2 = sum[1]
            result = eval(calc1)
            if str(calc2) == str(result):
                print("True")
            else:
                print("False")
            goback()
            continue
        if sum == "power":
            usersum = input("Enter the Number: ")
            userthepower = input("To the Power of: ")
            usersum = float(usersum)
            userthepower = float(userthepower)
            result = (pow(usersum, userthepower))
            print(f"{usersum} to the Power of {userthepower} is {result}")
            goback()
            continue
        if sum == "sqrt":
            usersum = input("Enter the Number: ")
            usersum = float(usersum)
            result = math.sqrt(usersum)
            print(f"The Square Root of {usersum} is {result}")
            goback()
            continue
        if sum == "square":
            usersum = input("Enter the Number to be Squared: ")
            usersum = float(usersum)
            result = (usersum*usersum)
            print(f"The Square of {usersum} is {result}")
            goback()
            continue
        if sum == "round":
            usersum = input("Enter the Number to be Rounded: ")
            userto = int(input("Enter the amount of Decimal Places to Round to: "))
            result = round(float(usersum), userto)
            print(f"{usersum} Rounded to {userto} Decimal Places is {result}")
            goback()
            continue
        if sum == "abs":
            usersum = input("Enter the Number to Find the Absolute Value of: ")
            usersum = float(usersum)
            result = abs(usersum)
            print(f"The Absolute Value of {usersum} is {result}")
            goback()
            continue
        if sum == "avg":
            str1 = input('Enter the Following Syntax: "num1, num2, num3, etc": ')
            result = list(str1.split(','))
            total = 0
            for i in result:
                total += float(i)
            result1 = total / len(result)
            result1 = round(result1, 3)
            print(f"The Average of {str1} is {result1}")
            goback()
            continue
        if sum == "median":
            str1 = input('Enter the Following Syntax: "num1, num2, num3, etc": ')
            result = str1.split(', ')
            result1 = median(result)
            print(f"The Median of {str1} is {result1}")
            goback()
            continue
        if sum == "mode":
            str1 = input('Enter the Following Syntax: "num1, num2, num3, etc": ')
            result = str1.split(', ')
            result1 = mode(result)
            print(f"The Mode of {str1} is {result1}")
            goback()
            continue
        if sum == "floor":
            usersum = input("Enter the Number: ")
            usersum = float(usersum)
            result = math.floor(usersum)
            print(f"The Floor of {usersum} is {result}")
            goback()
            continue
        if sum == "ceiling" or sum == "ceil":
            usersum = input("Enter the Number: ")
            usersum = float(usersum)
            result = math.ceil(usersum)
            print(f"The Ceiling of {usersum} is {result}")
            goback()
            continue

        if sum == "simp":
            nume = int(input("Numerator: "))
            deno = int(input("Denominator: "))
            result = (simplify_fraction(nume, deno))
            print("The / Between The Numbers is the Line in the Middle of the Fraction (Vinculum)")
            print(f"{nume}/{deno} Simplified is {result}")
            goback()
            continue
        
        if sum == "conv" or sum == "convert" or sum == "converter":
            print("1 = Miles to KM")
            print("2 = Pounds to KG")
            print("3 = Celsius to Fahrenheit")
            print("4 = Fractions to Decimals")
            print("5 = Percentages to Fractions")
            print("6 = Percentages to Decimals")
            print("7 = Percent of a number")
            print("8 = Percent off")
            print("9 = Inches to CM")
            print("10 = Tax Calculator")
            print("11 = Add percent to a number")
            print("12 = Language Translation jk Google Translate")
            print("13 = Month Information")
            print("14 = What percentage of a number is in a number")
            convopt = input("What Option Would You Like [1-14]: ")

            if convopt == "1":
                print("1 = Miles to KM")
                print("2 = KM to Miles")
                milesorkm = input("What Option Would You Like? [1,2]: ")
                if milesorkm == "1":
                    miles = input("Miles: ")
                    miles = float(miles)
                    result = convert(miles, 'mi', 'km')
                    print(f"{miles} Miles is {result} KM")
                if milesorkm == "2":
                    km = input("KM: ")
                    km = float(km)
                    result = convert(km, 'km', 'mi')
                    print(f"{km} KM is {result} Miles")

            if convopt == "2":
                print("1 = Pound to KG")
                print("2 = KG to Pound")
                poundorkg = input("What Option Would You Like? [1,2]: ")
                if poundorkg == "1":
                    pound = input("Pound: ")
                    pound = float(pound)
                    result = convert(pound, 'p', 'kg')
                    print(f"{pound} Pounds is {result} KG")
                if poundorkg == "2":
                    kg = input("KG: ")
                    kg = float(kg)
                    result = convert(kg, 'kg', 'p')
                    print(f"{kg} KG is {result} Pounds")

            if convopt == "3":
                print("1 = Celsius to Fahrenheit")
                print("2 = Fahrenheit to Celsius")
                corf = input("What Option Would You Like? [1,2]: ")
                if corf == "1":
                    celsius = input("Celsius: ")
                    celsius = float(celsius)
                    # Manual because it's a Formula
                    calculate = (celsius*9/5)+32
                    calculate = str(calculate)
                    result = eval(calculate)
                    print(f"{celsius} Degrees Celsius is {result} Fahrenheit")
                if corf == "2":
                    fahrenheit = input("Fahrenheit: ")
                    fahrenheit = float(fahrenheit)
                    # Manual because it's a Formula
                    calculate = (fahrenheit-32)*9/5
                    calculate = str(calculate)
                    result = eval(calculate)
                    print(f"{fahrenheit} Degrees Fahrenheit is {result} Celsius")

            if convopt == "4":
                print("1 = Fraction to Decimal")
                print("2 = Decimal to Fraction")
                dorf = input("What Option Would You Like? [1,2]: ")
                if dorf == "1":
                    numerator = input("Numerator: ")
                    denominator = input("Denominator: ")
                    numerator = float(numerator)
                    denominator = float(denominator)
                    calculate = str(numerator / denominator)
                    result = eval(calculate)
                    print("The / Between The Numbers is the Line in the Middle of the Fraction (Vinculum)")
                    print(f"{numerator} / {denominator} Expressed as a Decimal is {result}")
                if dorf == "2":
                    d = input("Decimal: ")
                    d = float(d)
                    result = (d).as_integer_ratio()
                    result = str(result)
                    result = result.replace('(', '')
                    result = result.replace(')', '')
                    result = result.replace(', ', ' / ')
                    print("The / Between The Numbers is the Line in the Middle of the Fraction (Vinculum)")
                    print(f"{d} Expressed as a Fraction is {result}")
            
            if convopt == "5":
                print("1 = Percentage to Fraction")
                print("2 = Fraction to Percentage")
                porf = input("What Option Would You Like? [1,2]: ")
                if porf == "1":
                    p = input("Percentage: ")
                    d = 100
                    p = float(p)
                    d = float(d)
                    print("The / Between The Numbers is the Line in the Middle of the Fraction (Vinculum)")
                    print(f"{p}% Expressed as a Fraction is {p} / {d}")
                if porf == "2":
                    f = input("Fraction (eg. 1/2) (The / Is the Line in the Middle of the Fraction (Vinculum)): ")
                    f1 = eval(f)
                    d = f1 * 100
                    calculate = ((round(d,4)))
                    calculate = str(calculate)
                    result = eval(calculate)
                    print(f"{f} Expressed as a Percentage is {result}%")
                
            if convopt == "6":
                print("1 = Percentages to Decimals")
                print("2 = Decimals to Percentages")
                dorp = input("What Option Would You Like? [1,2]: ")
                if dorp == "1":
                    p = input("Percentage (No Percentage Sign): ")
                    print(f"{p}% as a Decimal is 0.{p}")
                if dorp == "2":
                    d = input("Decimal: ")
                    d = float(d)
                    calculate = str((d*100))
                    result = float(eval(calculate))
                    print(f"{d} as a Percentage is {result}%")

            if convopt == "7":
                p = input("Percentage (No Percentage Sign): ")
                num = input("Number to Find the Percentage of: ")
                p = float(p)
                num = float(num)
                calculate = str((p/100)*num)
                result = eval(calculate)
                print(f"{p}% of {num} is {result}")
            
            if convopt == "8":
                print("1 = Price After Sale")
                print("2 = Price Before Sale")
                porp = input("What Option Would You Like? [1,2]: ")
                if porp == "1":
                    price = input("Origional Price (No Dollar Sign): ")
                    p = input("Percent Off (No Percentage Sign): ")
                    price = float(price)
                    p = float(p)
                    calculate = str((p/100)*price)
                    off = eval(calculate)
                    calculatetotal = str(price-off)
                    result = eval(calculatetotal)
                    print(f"{p}% off ${price} is ${result}")
                if porp == "2":
                    price = input("Discounted Price (No Dollar Sign): ")
                    p = input("Percent Off (No Percentage Sign): ")
                    price = float(price)
                    p = float(p)
                    calculateoutof = str(100-p)
                    outof = eval(calculateoutof)
                    calculateoutofdec = str(outof/100)
                    outofdec = eval(calculateoutofdec)
                    calculateresult = str(price/outofdec)
                    result = eval(calculateresult)
                    print(f"The Origional Price of the Discounted Price ${price} After a Discount of {p}% is ${result}")

            if convopt == "9":
                print("1 = Inches to CM")
                print("2 = CM to Inches")
                iorc = input("What Option Would You Like? [1,2]: ")
                if iorc == "1":
                    inches = input("Inches: ")
                    inches = float(inches)
                    # Flipped because Math and to Correct the Convert Function
                    result = convert(inches, 'cm', 'i')
                    print(f"{inches} Inches to CM is {result}")
                if iorc == "2":
                    cm = input("CM: ")
                    cm = float(cm)
                    result = convert(cm, 'i', 'cm')
                    print(f"{cm} CM to Inches is {result}")

            if convopt == "10":
                price = input("Origional Price (No Dollar Sign): ")
                per = input("Tax Percentage (No Percentage Sign): ")
                price = float(price)
                per = float(per)
                calculateper = str(per/100)
                per = eval(calculateper)
                calculatepercentof = str(price*per)
                percentof = eval(calculatepercentof)
                calculateresult = str(price+percentof)
                result = eval(calculateresult)
                print(f"${price} With Added Tax of {per}% is ${result}")

            if convopt == "11":
                value = input("Origional Value: ")
                per = input("Percentage to Add (No Percentage Sign): ")
                value = float(value)
                per = float(per)
                calculateper = str(per/100)
                per = eval(calculateper)
                calculatepercentof = str(value*per)
                percentof = eval(calculatepercentof)
                calculateresult = str(value+percentof)
                result = eval(calculateresult)
                print(f"{value} With Added Percentage of {per}% is {result}")
            
            if convopt == "12":
                webbrowser.open("translate.google.com")
            
            if convopt == "13":
                print("Month Data: ")
                print("Number - Month - Short Form - Days")
                print("1 - January - Jan - 31")
                print("2 - Feburary - Feb - 28/29")
                print("3 - March - Mar - 31")
                print("4 - April - Apr - 30")
                print("5 - May - May - 31")
                print("6 - June - Jun - 30")
                print("7 - July - Jul - 31")
                print("8 - August - Aug - 31")
                print("9 - September - Sep - 30")
                print("10 - October - Oct - 31")
                print("11 - November - Nov - 30")
                print("12 - December - Dec - 31")
            
            if convopt == "14":
                fracnum = input("Part of a Number: ")
                totnum = input("Total Number: ")
                calculateresult = str((float(fracnum)/float(totnum)*100))
                result = eval(calculateresult)
                print(f"{fracnum} is {result}% of {totnum}")
                

            goback()
            continue



        if sum == "guess":
            randomnumber = random.randint(1, 100)
            guessamnt = 0
            while True:
                guess = input("Guess the Number: ")
                guess = int(guess)
                guessamnt += 1
                if guess == randomnumber:
                    print("Great Job!")
                    print(f"You Guessed It In {guessamnt} Tries!")
                if guess > randomnumber:
                    print("Lower!")
                    continue
                if guess < randomnumber:
                    print("Higher!")
                    continue
                goback()
                break
            continue

        else:
            sum = sum.replace("pi", "3.14159265358979")
            sum = sum.replace("e", "2.71828182845905")
            result = eval(sum)
            print(f"The Answer to {sum} is {result}")
            goback()
            continue
    except:
        print("Error")
        goback()
        continue