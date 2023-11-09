# from yearInput import prompt

#create Class called Country here
class Country(): 
    
    '''
    Object that will hold the following: country name, 
    population, land area, average temperature and population density 
    
    Attributes 
    ---------- 
    country: str
             This will be the name of the country 
    population: int 
             This will will be the population of each country 
    land: int 
             This will be the area of the land(in sq.km)
    avgTemp: float 
             THis will be the average temperature in the country

    Methods 
    ------- 
    
    '''

    def __init__ (self, country, year, population, land, avgTemp):
        self.country = country 
        self.year = year
        self.population = population 
        self.land = land 
        # self.popDensity = popDensity
        self.avgTemp = avgTemp 


    def Density(population, area):
        '''
        Find the population density 

        Parameters 
        ----------
        population : int 
            the population of a country 
        area: int 
            the land area of a country 
        
        Returns 
        ------- 
        str: A message containing density of each country 
        '''
        
        density = (population / area)
        density.round(2)
        
        # densityPercent = int(density * 100)
        return f"Density: {density} people/sq km"
    
    
    def __temperature (self, temp): 
        return int(temp * 1.8 + 32) #conversion from celesius to farenheit 

    # def __country (Self, country):
    #     return country
    
    def __str__(self): 
        return f"Country: {self.country}, Year: {self.year}, Populataion: {self.population}, Land area: {self.land}, Average Temperature:{self.avgTemp}"
