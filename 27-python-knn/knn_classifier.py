'''
Data Set Information:

Data were extracted from images that were taken from genuine and forged banknote-like specimens. 
For digitization, an industrial camera usually used for print inspection was used. 
The final images have 400x 400 pixels.
Due to the object lens and distance to the investigated object gray-scale pictures with 
a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

URL : https://archive.ics.uci.edu/ml/datasets/banknote+authentication


Attribute Information:

1. variance of Wavelet Transformed image (continuous)
2. skewness of Wavelet Transformed image (continuous)
3. curtosis of Wavelet Transformed image (continuous)
4. entropy of image (continuous)
5. class (integer)

'''
# importing python packages
import pandas as pd
import numpy as np
from scipy.stats import mode
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# Loading data set

file_path = 'data/data_banknote_authentication.txt'

col_names = ["variance", "skewness", "curtosis", "entropy", "class"]

df = pd.read_csv(file_path, sep=',', header=None, names=col_names)

# Looking into dataset
print(f"size of the dataset: {df.shape}")

sns.heatmap(df.corr())

plt.savefig("plots/correlation_heatmap.png")

ax = df['class'].plot(kind='hist')
ax.get_figure().savefig('plots/class_distribution.png')

# Get X and Y value (dependent and target values)

X = df.drop("class", axis=1).values
y = df["class"].values

# Spliting dataset into train, test using scikit learn

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

print(f"Shape of X_train: {X_train.shape}, Shape of y_train: {y_train.shape}")
print(f"Shape of X_test: {X_test.shape}, Shape of y_test: {y_test.shape}")

# Find euclidean distance
# d(p, q) = sqrt((p1-q1)^2 + (p2-q2)^2 + ....+ (pn-qn)^2)

def calc_euclidean_distance(p, q):
    '''
        This function calculates eculidean distance
        get two points as input 
        return distance between the two points
    '''

    dist = np.sqrt(np.sum((p-q) ** 2))
    return dist


# KNN classifier

def knn_predict(train, y, test, k=3):
    preds = [] # save prediction labels

    # Loop through test data
    for i in test:

        # store distances
        distances = []
        # loop through training data
        for j in range(len(train)):
            d = calc_euclidean_distance(np.array(train[j,:]), i)
            # adding into distances list
            distances.append(d)
        
        distances = np.array(distances) # converting list into numpy array
        
        # sort array & keep the K datapoints
        dist = np.argsort(distances)[:k]

        # labels of the K data points 
        labels = y[dist]

        # Majority calculation
        mc = mode(labels)
        mc = mc.mode[0]

        preds.append(mc)

    return preds

# Prediction

y_pred = knn_predict(X_train, y_train, X_test, 3)

# Results

print(f"accuracy score with k = 3: {accuracy_score(y_test, y_pred)}")

print(f"F1  score with k = 3: {f1_score(y_test, y_pred)}")

print(classification_report(y_test, y_pred))

clf_report = classification_report(y_test, y_pred, output_dict=True)

sns.heatmap(pd.DataFrame(clf_report).iloc[:-1, :].T, annot=True)

plt.savefig("plots/Classification_report_with_k_3.png")

# Different K 


for k in range(1, 32, 2):

    y_pred = knn_predict(X_train, y_train, X_test, k)

    print(f"accuracy score with k = {k}: {accuracy_score(y_test, y_pred)}")

    print(f"F1  score with k = {k}: {f1_score(y_test, y_pred)}")

    print(classification_report(y_test, y_pred))