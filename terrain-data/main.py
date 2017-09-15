#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.

    The objective of this exercise is to recreate the decision
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """

from prep_terrain_data import make_terrain_data
from class_vis import pretty_picture, output_image
from classify_nb import classify

FEATURES_TRAIN, LABELS_TRAIN, FEATURES_TEST, LABELS_TEST = make_terrain_data()

### the training data (FEATURES_TRAIN, LABELS_TRAIN) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
GRADE_FAST = [FEATURES_TRAIN[ii][0] for ii in range(0, len(FEATURES_TRAIN))
              if LABELS_TRAIN[ii] == 0]
BUMPY_FAST = [FEATURES_TRAIN[ii][1] for ii in range(0, len(FEATURES_TRAIN))
              if LABELS_TRAIN[ii] == 0]
GRADE_SLOW = [FEATURES_TRAIN[ii][0] for ii in range(0, len(FEATURES_TRAIN))
              if LABELS_TRAIN[ii] == 1]
BUMPY_SLOW = [FEATURES_TRAIN[ii][1] for ii in range(0, len(FEATURES_TRAIN))
              if LABELS_TRAIN[ii] == 1]

# You will need to complete this function imported from the classify_nb script.
# Be sure to change to that code tab to complete this quiz.
CLASSIFIER = classify(FEATURES_TRAIN, LABELS_TRAIN)

### draw the decision boundary with the text points overlaid
pretty_picture(CLASSIFIER, FEATURES_TEST, LABELS_TEST)
output_image("test.png", "png", open("test.png", "rb").read())
