# Source: https://ccani007.github.io/dissertationData/

import pandas as pd
import numpy as np

### 2023
filepath = 'clean_yrbs_2023.csv'
df = pd.read_csv(filepath)

cols = ["Sex","Age","Grade","Hopelessness","SuicideIdeation",
        "SuicidePlan","SuicideAttempts","SuicideInjuryMedicalAttention",
        "VeryOverweight","WeightLoss","NoFruitJuice","NoFruit","NoSalad",
        "NoPotatoes","NoCarrots","NoOtherVeggies","NoSoda","NoBreakfast",
        "SocialMedia","NotGoodMentalHealth","EightOrMoreHoursSleep",
        "NoSportsDrinks","NoDrinksWater"]
df2023 = df[cols].copy()

### 2021
filepath = 'clean_yrbs_2021.csv'
df = pd.read_csv(filepath)

cols = ["Sex","Age","Grade","Hopelessness","SuicideIdeation",
        "SuicidePlan","SuicideAttempts","SuicideInjuryMedicalAttention",
        "VeryOverweight","WeightLoss","NoFruitJuice","NoFruit","NoSalad",
        "NoPotatoes","NoCarrots","NoOtherVeggies","NoSoda","NoMilk","NoBreakfast",
        "ThreeOrMoreHoursTV","NotGoodMentalHealth","EightorMoreHoursSleep",
        "NoSportsDrinks","NoDrinksWater"]
df2021 = df[cols].copy()

### 2019
filepath = 'clean_yrbs_2019.csv'
df = pd.read_csv(filepath)

cols = ["Sex","Age","Grade","Hopelessness","SuicideIdeation",
        "SuicidePlan","SuicideAttempts","SuicideInjuryMedicalAttention",
        "VeryOverweight","WeightLoss","NoFruitJuice","NoFruit","NoSalad",
        "NoPotatoes","NoCarrots","NoOtherVeggies","NoSoda","NoMilk","NoBreakfast",
        "ThreeOrMoreHoursTV","ThreeOrMoreHoursVideoGames","EightorMoreHoursSleep",
        "NoSportsDrinks","NoDrinksWater"]
df2021 = df[cols].copy()

### 2017
filepath = 'clean_yrbs_2017.csv'
df = pd.read_csv(filepath)
df2021 = df[cols].copy()    # columns are same as 2019



