from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def nb_accuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    predictions = clf.predict(features_test)

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example,
    ### where we just print the accuracy
    ### you might need to import an sklearn module

    # accuracy = no of test points that are classified correctly /
    #            total no of points (in a test set)

    # method#1: write code that compares predictions to y_axis_test, element-by-element
    # method#2: google "sklearn accuracy" and go from there
    # method#3: There's another way you can do this, too
    # print clf.score(features_test, labels_test)
    #accuracy = clf.score(features_test, labels_test)
    accuracy = accuracy_score(predictions, labels_test)
    return accuracy
