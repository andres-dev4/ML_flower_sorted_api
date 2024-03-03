import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC



full_train = pd.read_csv('train.csv', header=None)
full_test = pd.read_csv('test.csv', header=None)
trainLabels = pd.read_csv('trainLabels.csv', names=['y'])



full_train.head()


breakpoint()
full_train.shape,full_test.shape,trainLabels.shape




