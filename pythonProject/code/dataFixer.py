#import libraries here 
import pandas as pd
import numpy as np


#import classes/functions from other files here
# from popDensity import * #import all the functions from popDensity 

def fixData():
    with open ("dataset\countryTemp.csv", "r+") as countryData: 
        dfTemp = pd.read_csv(countryData)
        # selectCol = ["Country", "Year","AvgTemperature"] 
        dfTemp = dfTemp.iloc[:,[1,6,7]]
        dfTemp = dfTemp[dfTemp['Year'] >= 2000] #delete all the rows with the years previous to 2000 
        #used groupby to group the data by country and year and then take the average of that
        grouped = dfTemp.groupby(['Country', 'Year'])['AvgTemperature'].mean().reset_index() #reset_index() will reset the index in the modified dataframe

        #Round the average to one decimal place 
        grouped['AvgTemperature'] = grouped['AvgTemperature'].round(1)
        grouped.to_csv("code\countries.csv", sep=",",index=False)

    # get the population and land area in sepereate files
    with open ("dataset/population.csv", "r+") as population:
        dfPopulation = pd.read_csv(population)
        selected_columns = ["Country Name", "2000 [YR2000]", "2001 [YR2001]", "2002 [YR2002]", "2003 [YR2003]", "2004 [YR2004]", "2005 [YR2005]", "2006 [YR2006]", "2007 [YR2007]", "2008 [YR2008]", "2009 [YR2009]", "2010 [YR2010]", "2011 [YR2011]", "2012 [YR2012]", "2013 [YR2013]", "2014 [YR2014]", "2015 [YR2015]", "2016 [YR2016]", "2017 [YR2017]", "2018 [YR2018]", "2019 [YR2019]", "2020 [YR2020]"]
        dfPopulation = dfPopulation[selected_columns]
        dfPopulation.to_csv("code\populationProper.csv", sep=',', index=False)

    with open ("dataset/land.csv", "r+") as land:
        dfLand = pd.read_csv(land)
        selected_columns = ["Country Name", "2000 [YR2000]", "2001 [YR2001]", "2002 [YR2002]", "2003 [YR2003]", "2004 [YR2004]", "2005 [YR2005]", "2006 [YR2006]", "2007 [YR2007]", "2008 [YR2008]", "2009 [YR2009]", "2010 [YR2010]", "2011 [YR2011]", "2012 [YR2012]", "2013 [YR2013]", "2014 [YR2014]", "2015 [YR2015]", "2016 [YR2016]", "2017 [YR2017]", "2018 [YR2018]", "2019 [YR2019]", "2020 [YR2020]"]
        dfLand = dfLand[selected_columns]
        dfLand.to_csv("code\landProper.csv", sep=',', index=False)

fixData()