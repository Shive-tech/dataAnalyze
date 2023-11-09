import pandas as pd 

df = pd.read_csv("code/countries.csv")
countryCol = df["Country"]
uniqueCountry = countryCol.str.lower().unique()


def getOption(): 
    #find out if the user wants the data per year, per year, or for the whole thing 
    print("You can choose between three options for what data you want to represent.")
    print("1. Data for a particular country")
    print("2. Data for a particular year")
    print("3. Data for a particular country and year")
    print("4. Data for everything")

    while True: 
        try: 
            optionPrompt = int(input("Give a number between 1 and 4: "))
            if 1 <= optionPrompt <= 4: 
                break
            else:
                print(f"{optionPrompt} isn't a valid number, give a number between 1 and 4")
        except ValueError: #makes sure that the input is a number and that there is no problem in converting the input to int 
            print("Invalid input. Give an actual number")

def getCountry(countries): 
    while True:
        userInput = input("Give the name of the country").lower()
        if userInput in countries: 
            break 
        else: 
            print(f"{userInput} isn't a valid country. Give a valid country")
    return userInput
        
def getYr():   
 #get the input for which year they want the population and temperature for 
    while True: 
        try: 
            yrPrompt = int(input("Give a year between 2000 and 2020: "))
            if 2000 <= yrPrompt <= 2020: 
                break #we will get a proper input atp
            else: 
                print(f"{yrPrompt} isn't a valid number, give a number between 2000 and 2020")
        except ValueError: #makes sure that the input is a number and that there is no problem in converting the input to int 
            print("Invalid input. Give an actual number")
    return yrPrompt