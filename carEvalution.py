import numpy as np
from numpy.lib.arraysetops import unique
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler

def importdata():
	df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data',sep= ',', header = None)

	print ("Dataset Length: ", len(df))
	print ("Dataset Shape: ", df.shape)

	df.columns = ['buying','maint','doors','persons','lug_boot','safety','class']

	buyingMapping = {"low": 1, "med": 2, "high": 3, "vhigh": 4}
	df['buying'] = df['buying'].map(buyingMapping)

	maintMapping = {"low": 1, "med": 2, "high": 3, "vhigh": 4}
	df["maint"] = df["maint"].map(maintMapping)

	doorsMapping = {"2": 2, "3": 3, "4": 4, "5more": 5}
	df["doors"] = df["doors"].map(doorsMapping)

	personsMapping = {"2": 2, "4": 4, "more": 6}
	df["persons"] = df["persons"].map(personsMapping)

	lugBootMapping = {"small": 1, "med": 2, "big": 3}
	df["lug_boot"] = df["lug_boot"].map(lugBootMapping)

	safetyMapping = {"low": 1, "med": 2, "high": 3}
	df["safety"] = df["safety"].map(safetyMapping)

	print ("Dataset: \n",df.head())
	return df
def print_count(y):
    list = unique(y)
    individual_values = {}
    for i in list:
        individual_values[i] = 0
    for i in y:
        individual_values[i]+=1

    print("Count: ",individual_values)

def do_over_sampling(imb_df):
    X = imb_df.values[:,0:5]
    y = imb_df.values[:,6]
    print("Y count before over Sampling")
    print_count(y)
    ros = RandomOverSampler(random_state=0)
    X_resampled, y_resampled = ros.fit_resample(X, y)
    print("Y count after over Sampling")
    print_count(y_resampled)
    print("Resampled data length:",len(y_resampled))

    return X_resampled,y_resampled


def splitdataset(X,Y):

	X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)
	
	return X, Y, X_train, X_test, y_train, y_test
	
def train_using_gini(X_train, X_test, y_train):

	clf_gini = DecisionTreeClassifier(criterion = "gini",random_state = 100,max_depth=3, min_samples_leaf=7)

	clf_gini.fit(X_train, y_train)
	return clf_gini
	
def tarin_using_entropy(X_train, X_test, y_train):

	clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,max_depth = 3, min_samples_leaf = 7)

	clf_entropy.fit(X_train, y_train)
	return clf_entropy


def prediction(X_test, clf_object):

	y_pred = clf_object.predict(X_test)
	
	return y_pred
	
def cal_accuracy(y_test, y_pred):
	
	print("Confusion Matrix:\n ",
		confusion_matrix(y_test, y_pred))
	
	print ("Accuracy :\n ",
	accuracy_score(y_test,y_pred)*100)
	
	print("Report : \n",
	classification_report(y_test, y_pred,zero_division=0))

# Driver code
def main():
	
	data = importdata()
	x_resampled,y_resampled = do_over_sampling(data)

	X, Y, X_train, X_test, y_train, y_test = splitdataset(x_resampled,y_resampled)


	clf_gini = train_using_gini(X_train, X_test, y_train)
	clf_entropy = tarin_using_entropy(X_train, X_test, y_train)
	
	print("Results Using Gini Index:")
	
	y_pred_gini = prediction(X_test, clf_gini)
	cal_accuracy(y_test, y_pred_gini)
	
	print("Results Using Entropy:")
	y_pred_entropy = prediction(X_test, clf_entropy)
	cal_accuracy(y_test, y_pred_entropy)
	
	
# Calling main function
if __name__=="__main__":
	main()
