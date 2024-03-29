import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from collections import Counter
#import matplotlib as plt
from matplotlib.colors import ListedColormap
cmap=ListedColormap(['#FF0000','#00FF00','#0000FF'])
iris=datasets.load_iris()
X,y=iris.data,iris.target
X_train, X_test, y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1234)


plt.figure()  #A blank figure where you can plot the figure
plt.scatter(X[:,2],X[:,3],c=y,cmap=cmap,edgecolor='k',s=20) #plotting the graph of third feature and fourth feature of the dataset
plt.show()

def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)
        return accuracy

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Sort by distance and return indices of the first k neighbors
        k_idx = np.argsort(distances)[: self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        # return the most common class label
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]


k = 3
clf = KNN(k=k)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print("KNN classification accuracy", accuracy(y_test, predictions)*100)


