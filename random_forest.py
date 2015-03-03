#random_forest example
from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
#create the training &test sets,skipping the header row with [1:]
dataset = genfromtxt(open('data/train.csv','r'), delimiter=',', dtype='f8')[1:]
train = [x[1:] for x in dataset]
target = [x[0] for x in dataset]
test = genfromtxt(open('data/test.csv','r'), delimiter=',', dtype='f8')[1:]

#create an train the random forest
#multi - core CPUs can use: rf = RandomForestClassifier(n_estimators=100, n_jobs=2)
rf = RandomForestClassifier(n_estimators = 100)
rf.fit(train,target)
predicted_probs = [[index + 1, x[1]] for index, x in enumerate(rf.predict_proba(test))]

savetxt('data/submission.csv', predicted_probs, delimiter=',', fmt='%d,%f',
        header='MoleculeId,PredictedProbability', comments = '')
