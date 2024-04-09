import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np

##Function to detect outliers:
def detect(df):
    outliers = []
    tr = 3
    mean = np.mean(df)
    std = np.std(df)

    for i in df:
        z = (i - mean)/std
        if np.abs(z)>tr:
            outliers.append(i)
    return outliers

##Loading the data:
data15 = pd.read_csv("2015.csv")
data16 = pd.read_csv("2016.csv")
data17 = pd.read_csv("2017.csv")
data18 = pd.read_csv("2018.csv")
data19 = pd.read_csv("2019.csv")

##Running query to seperate the countries with Happiness Score greater than 6.0:
data15_A = data15.loc[((data15['Health (Life Expectancy)'] > 0.5) & (data15['Health (Life Expectancy)'] < 1))]
data15_A = data15_A['Country']
print("B) Countries in 2015 that have Health (Life Expectancy) value between 0.5-1: ")
print(data15_A)

##Top 10 countries with the highest Happiness Score for the year 2016:
data16 = pd.DataFrame(data16)
print("\n\nC) Top 10 countries with the highest Happiness Score for the year 2016: ")
print(data16['Country'][0:10])

##Mean of Happiness Score for the year 2016:
data16_mean = data16.loc[:, 'Happiness Score']
data16_mean = data16_mean.mean()
print("\n\nD) Mean of Happiness Score for the year 2016: ")
print(data16_mean)

data15 = pd.DataFrame(data15)
data16 = pd.DataFrame(data16)
data17 = pd.DataFrame(data17)
data18 = pd.DataFrame(data18)
data19 = pd.DataFrame(data19)

##Outliers for the year 2015:
print("\n\n\nE) Outliers for the year 2015: ")
print("\nStandard Error: ")
y = data15['Standard Error'].to_list()
print(detect(y))

print("\nFamily: ")
y = data15['Family'].to_list()
print(detect(y))

print("\nTrust (Government Corruption): ")
y = data15['Trust (Government Corruption)'].to_list()
print(detect(y))

print("\nGenerosity: ")
y = data15['Generosity'].to_list()
print(detect(y))

print("\nDystopia Residual: ")
y = data15['Dystopia Residual'].to_list()
print(detect(y))

##---------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n\n\nOutliers for the year 2016: ")
print("\nHappiness Score: ")
y = data16['Happiness Score'].to_list()
print(detect(y))

print("\nLower Confidence Interval ")
y = data16['Lower Confidence Interval'].to_list()
print(detect(y))

print("\nUpper Confidence Interval ")
y = data16['Upper Confidence Interval'].to_list()
print(detect(y))

print("\nEconomy (GDP per Capita) ")
y = data16['Economy (GDP per Capita)'].to_list()
print(detect(y))

print("\nFamily ")
y = data16['Family'].to_list()
print(detect(y))

print("\nHealth (Life Expectancy) ")
y = data16['Health (Life Expectancy)'].to_list()
print(detect(y))

print("\nFreedom ")
y = data16['Freedom'].to_list()
print(detect(y))

print("\nTrust (Government Corruption) ")
y = data16['Trust (Government Corruption)'].to_list()
print(detect(y))

print("\nGenerosity ")
y = data16['Generosity'].to_list()
print(detect(y))

print("\nDystopia Residual ")
y = data16['Dystopia Residual'].to_list()
print(detect(y))

##---------------------------------------------------------------------------------------------------------------------------------------------------------

print("\n\n\nOutliers for the year 2017: ")
print("\nHappiness.Score: ")
y = data17['Happiness.Score'].to_list()
print(detect(y))

print("\nWhisker.high ")
y = data17['Whisker.high'].to_list()
print(detect(y))

print("\nWhisker.low ")
y = data17['Whisker.low'].to_list()
print(detect(y))

print("\nEconomy..GDP.per.Capita. ")
y = data17['Economy..GDP.per.Capita.'].to_list()
print(detect(y))

print("\nFamily ")
y = data17['Family'].to_list()
print(detect(y))

print("\nHealth..Life.Expectancy. ")
y = data17['Health..Life.Expectancy.'].to_list()
print(detect(y))

print("\nFreedom ")
y = data17['Freedom'].to_list()
print(detect(y))

print("\nTrust..Government.Corruption. ")
y = data17['Trust..Government.Corruption.'].to_list()
print(detect(y))

print("\nGenerosity ")
y = data17['Generosity'].to_list()
print(detect(y))

print("\nDystopia.Residual ")
y = data17['Dystopia.Residual'].to_list()
print(detect(y))

##-----------------------------------------------------------------------------------------------------------------------------------

print("\n\n\nOutliers for the year 2018: ")
print("\nScore: ")
y = data18['Score'].to_list()
print(detect(y))

print("\nGDP per capita ")
y = data18['GDP per capita'].to_list()
print(detect(y))

print("\nHealthy life expectancy ")
y = data18['Healthy life expectancy'].to_list()
print(detect(y))

print("\nFreedom to make life choices ")
y = data18['Freedom to make life choices'].to_list()
print(detect(y))

print("\nGenerosity ")
y = data18['Generosity'].to_list()
print(detect(y))

print("\nPerceptions of corruption ")
y = data18['Perceptions of corruption'].to_list()
print(detect(y))

##-----------------------------------------------------------------------------------------------------------------------------------

print("\n\n\nOutliers for the year 2019: ")
print("\nScore: ")
y = data19['Score'].to_list()
print(detect(y))

print("\nGDP per capita ")
y = data19['GDP per capita'].to_list()
print(detect(y))

print("\nSocial support ")
y = data19['Social support'].to_list()
print(detect(y))

print("\nHealthy life expectancy ")
y = data19['Healthy life expectancy'].to_list()
print(detect(y))

print("\nFreedom to make life choices ")
y = data19['Freedom to make life choices'].to_list()
print(detect(y))

print("\nGenerosity ")
y = data19['Generosity'].to_list()
print(detect(y))

print("\nPerceptions of corruption ")
y = data19['Perceptions of corruption'].to_list()
print(detect(y))

#----------------------------------------------------------------------------------------------------------------------
print("\n\n")
happiness_score = data15['Happiness Score']
Economy = data15['Economy (GDP per Capita)']
data15_1 = data15.drop('Country', axis=1)
data15_1 = data15_1.drop('Region', axis=1)
Correlation = data15_1.corr()
print(Correlation["Happiness Score"])
print("\n\nF) Happiness Score and Economy of the year 2015 have the strongest relationship")

##------------------------------------------------------------------------------------------------------------------------------------------
print("\n\n")
combinedData = data15['Country']
combinedData = pd.DataFrame(combinedData)
combinedData['Region'] = data15['Region']
combinedData['2015'] = data15['Happiness Score']
combinedData['2016'] = 0
combinedData['2017'] = 0
combinedData['2018'] = 0
combinedData['2019'] = 0


##--------------------------------------------------------I----------------------------------------------------------------------------------

##Running query
data15_I = data15.loc[(data15['Economy (GDP per Capita)'] < 0.5)]
print("\n\nI) Regions that have an Economy (GDP per Capita) values less than 0.5: ")
print(data15_I['Region'])

##--------------------------------------------------------J----------------------------------------------------------------------------------

corr15 = data15[['Happiness Score', 'Standard Error', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]
corr16 = data16[['Happiness Score', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Dystopia Residual']]
corr15 = corr15.corr()
corr16 = corr16.corr()
print("\n\nJ) 2015 Correlations:")
print(corr15)
print("\n\n2016 Correlations:")
print(corr16)
print("\n\n")
print("2015 Column-wise correlation: ")
print(corr15['Happiness Score'])
print("\n")
print(corr15['Standard Error'])
print("\n")
print(corr15['Economy (GDP per Capita)'])
print("\n")
print(corr15['Family'])
print("\n")
print(corr15['Health (Life Expectancy)'])
print("\n")
print(corr15['Freedom'])
print("\n")
print(corr15['Trust (Government Corruption)'])
print("\n")
print(corr15['Generosity'])
print("\n")
print(corr15['Dystopia Residual'])
print("\n")
print("In 2015, Health has the strongest correlation with Economy")

##-------------------------------------------------------------------2016----------------------------------------------------------------------------------------

print("\n\n2016 column-wise correlation: ")

print(corr16['Happiness Score'])
print("\n")
print(corr16['Lower Confidence Interval'])
print("\n")
print(corr16['Upper Confidence Interval'])
print("\n")
print(corr16['Economy (GDP per Capita)'])
print("\n")
print(corr16['Family'])
print("\n")
print(corr16['Health (Life Expectancy)'])
print("\n")
print(corr16['Freedom'])
print("\n")
print(corr16['Trust (Government Corruption)'])
print("\n")
print(corr16['Generosity'])
print("\n")
print(corr16['Dystopia Residual'])
print("\n")
print("In 2016, Health has the strongest correlation with Economy as well")

