# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:17:47 2021

@author: Lluna Sanz Montrull
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

name = ['Yaling', 'Sofia', 'Maria', 'Pablo', 'Inés']
age = [28, 23, 25, 23, 25]
gender = ['Female', 'Female', 'Female', 'Male', 'Female']

# Colección de 3 objetos
class_edem = pd.DataFrame({'name': name, 'age': age, 'gender': gender})
del(name, age, gender)

# Dimensionalidad del dataframe
class_edem.shape
