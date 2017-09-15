from prep_terrain_data import make_terrain_data
from classify import nb_accuracy

def submit_accuracy():
    features_train, labels_train, features_test, labels_test = make_terrain_data()
    accuracy = nb_accuracy(features_train, labels_train, features_test, labels_test)
    print accuracy
    return accuracy

if  __name__ == '__main__':
    submit_accuracy()
