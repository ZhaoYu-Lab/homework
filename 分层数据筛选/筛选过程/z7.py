import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

vector1 = np.array([1,2,3])
vector2 = np.array([4,5,6])
dist=np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))
print(dist)


