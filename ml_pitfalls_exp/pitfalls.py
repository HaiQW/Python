# Corpwrite : HaiQW
# URL = http://blog.yhathq.com/posts/measuring-model-performance-1.html
# Decription : "How good" can mean a lot of things and it varies over domain
# and problems sets. But it is the developer's responsibility to provide a fair
# measurement in the first place. That task is surprisingly easy to mess up.
import numpy as np

import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import r2_score

import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split

from sklearn.neighbors import KNeighborsRegressor

from sklearn.cross_validation import KFold

def main():
    df = pd.read_csv("heights_and_weights.csv")[:100]
    df.head()

    # Separate the data into "predictive features" and "thing to predict."
    # thing we'll be trying to predict is "weight"
    feats = df.drop("weight",axis = 1)# drop the weight

    # Creat a good old X and Y combination, Our features and targets
    x = feats.values
    y = df["weight"].values

    # Fit a LinearRegression model
    x_scaled = StandardScaler().fit_transform(x) # regular

    lr = LinearRegression()
    lr.fit(x_scaled,y)

    # Measure the model.How good is the fitted model. There are a lot of measurement
    # we can use, but fundamentally they all ask the same question: how close is the
    # models's prediction to the truth?  In our case, how close is the predicted
    # weight of a person to their actual weight?
    y_pred = lr.predict(x_scaled)

    # Next we have to pick a metric R. This metric uses some fancy calculations with
    # squares and means, but the biggest trait to note is that it penalizes outliers
    # more heavily than other methods. It produces a single number: a value of 1.01.
    # 01.0 for perfectly performing model with lower values being worse.
    r2_score(y,y_pred)
    # plot
    plot_r2(y, y_pred, "Performance of Linear Regression")


    # Fit a KNN model
    # a very serious algorithm
    knn = KNeighborsRegressor(n_neighbors= 1)
    knn.fit(x_scaled,y)

    # how good is k-nearest neighbors
    y_pred = knn.predict(x_scaled)
    plot_r2(y,y_pred,"Performance of KNN(K=1)")

    # Holdout validation
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3)
    t = StandardScaler().fit(x_train)
    x_train_scaled = t.transform(x_train) #always regularize features()
    lr = LinearRegression()
    lr.fit(x_train_scaled,y_train)

    x_test_scaled = t.transform(x_test)
    y_test_pred = lr.predict(x_test_scaled)
    plot_r2(y_test, y_test_pred, "holdout performance of Linear Regression")

    # k-fold cross validation
    # Always use shuffer = True to produce random folds.  If you need non
    # random splits, you're probably doing something wrong
    kf = KFold(len(y),n_folds= 25, shuffle = True)

    # By choosing n_folds = 10,we'll run 10 train-test splits and actually train
    # 10 separate models, one for each split.
    y_pred = np.zeros(len(y),dtype = y.dtype)
    lr = LinearRegression()

    # train_index and test_index never have the same values,test_index never
    # overlap
    for train_index,test_index in kf:
        # for each interation of the for loop we will do a test train split
        x_train,x_test = x[train_index],x[test_index]
        y_train,y_test = y[train_index],y[test_index]

        t = StandardScaler()
        x_train = t.fit_transform(x_train)
        lr.fit(x_train,y_train)

        x_test = t.transform(x_test)
        y_pred[test_index] = lr.predict(x_test)

    plot_r2(y, y_pred, "k-fold cross validation of Linear Regression")


################################################################################
#
# Customize plot function
#
################################################################################

def plot_r2(y,y_pred,title):
    plt.figure()
    plt.grid()
    plt.scatter(y,y_pred,c = 'g',marker = (5,1),lw = 0.1,label = r"$comparison$")
    plt.xlabel("Actual Target")
    plt.ylabel("Predicted Target")
    plt.title(title)

    xmn,xmx = plt.xlim()
    ymn,ymx = plt.ylim()
    mx = max(xmx,ymx)
    buff = mx * .1
    plt.text(xmn+buff,mx-buff,"R2 Score: %f"%(r2_score(y,y_pred),), size = 15)
    plt.plot([0., mx], [0., mx])
    plt.xlim(xmn, mx)
    plt.ylim(ymn, mx)
    plt.show()



###############################################################################
#
# This is a pythonism.  Rather than putting code directly at the "root"
# level of the file we instead provide a main method that is called
# whenever this python script is run directly.
#
###############################################################################

if __name__ == "__main__":
    main()
