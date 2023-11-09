import pandas as pd
import numpy as np
import os
from dataFixer import fixData
from typeConvert import Country #import 
from userInput import getCountry, getOption, getYr

fixData()

# path to the files 
dataPath = "code/countries.csv"
populationPath = "code/populationProper.csv"
landPath = "code/landProper.csv"

# Reading CSV files
dfData = pd.read_csv(dataPath)
dfPopulation = pd.read_csv(populationPath)
dfLand = pd.read_csv(landPath)

# Convert read DataFrames to NumPy arrays
data = dfData.to_numpy()
population = dfPopulation.to_numpy()
land = dfLand.to_numpy()

countries = [] #create an empty array 

optionPrompt = getOption()

if optionPrompt == 1: 
    countryPrompt = getCountry(dfData["Country"].str.lower().unique())
        # Extract the values from each row in dfData
    for index, row in dfData.iterrows(): #iterates through each row 
        country = row['Country']
        yr = row['Year']
        temp = row['AvgTemperature']

        if country.lower() == countryPrompt.lower():    
            # match the countries from the data.csv and the other files first
            population_row = population[population[:, 0] == country]
            land_row = land[land[:, 0] == country]

                    # Check if the country and the year exist in the other files for that particular country in that particular year
            if not (population_row.size == 0 or land_row.size == 0):
                #execute the code below if condition is not met
                population_val = population_row[0, yr - 2000 + 1]  #access the location through the integer rather than name of the column
                land_val = land_row[0, yr - 2000 + 1]

                # Create a Country object and append it to the list
                countryObj = Country(country, yr, population_val, land_val, temp)
                countries.append(countryObj)
    
    for country in countries:
        print(country)

elif optionPrompt == 2: 
    yrPrompt = getYr()
    for index, row in dfData.iterrows(): #iterates through each row 
        country = row['Country']
        yr = row['Year']
        temp = row['AvgTemperature']

        if yr == yrPrompt: 
            # match the countries from the data.csv and the other files first
            population_row = population[population[:, 0] == country]
            land_row = land[land[:, 0] == country]

            # Check if the country and the year exist in the other files for that particular country in that particular year
            if not (population_row.size == 0 or land_row.size == 0):
                #execute the code below if condition is not met
                population_val = population_row[0, yr - 2000 + 1]  #access the location through the integer rather than name of the column
                land_val = land_row[0, yr - 2000 + 1]

                # Create a Country object and append it to the list
                countryObj = Country(country, yr, population_val, land_val, temp)
                countries.append(countryObj)
    
    for country in countries:
        print(country)


elif optionPrompt == 3: 
    countryPrompt = countryPrompt = getCountry(dfData["Country"].str.lower().unique())
    yrPrompt = getYr()
    for index, row in dfData.iterrows():
        country = row['Country']
        yr = row['Year']
        temp = row['AvgTemperature']

        if yr == yrPrompt and country.lower() == countryPrompt.lower(): 
            # match the countries from the data.csv and the other files first
            population_row = population[population[:, 0] == country]
            land_row = land[land[:, 0] == country]

            # Check if the country and the year exist in the other files for that particular country in that particular year
            if not (population_row.size == 0 or land_row.size == 0):
                #execute the code below if condition is not met
                population_val = population_row[0, yr - 2000 + 1]  #access the location through the integer rather than name of the column
                land_val = land_row[0, yr - 2000 + 1]

                # Create a Country object and append it to the list
                countryObj = Country(country, yr, population_val, land_val, temp)
                countries.append(countryObj) 
    for country in countries:
        print(country)
else: 
    print("Retrieving full data: ")
    for index, row in dfData.iterrows():
        country = row['Country']
        yr = row['Year']
        temp = row['AvgTemperature']

        # match the countries from the data.csv and the other files first
        population_row = population[population[:, 0] == country]
        land_row = land[land[:, 0] == country]

        # Check if the country and the year exist in the other files for that particular country in that particular year
        if not (population_row.size == 0 or land_row.size == 0):
            #execute the code below if condition is not met
            population_val = population_row[0, yr - 2000 + 1]  #access the location through the integer rather than name of the column
            land_val = land_row[0, yr - 2000 + 1]

            # Create a Country object and append it to the list
            countryObj = Country(country, yr, population_val, land_val, temp)
            countries.append(countryObj)

    for country in countries:
        print(country)

# Remove the files after the run
removePrompt = input("Do you want to remove the files:")

if removePrompt.lower() == "y" or removePrompt.lower() == "yes":
    if os.path.exists("Code/populationProper.csv"):
        os.remove("Code/populationProper.csv")
    if os.path.exists("Code/landProper.csv"):
        os.remove("Code/landProper.csv")
    if os.path.exists("Code/countries.csv"):
        os.remove("Code/countries.csv")


#notes:
#for inheritance you can use a child class to get temperature in farenhetit 
#can also use child class out of the original country class for population density and get those values in integer format


