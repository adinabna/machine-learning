#!/usr/bin/python
import random

def make_terrain_data(n_points=1000):
    ### make the toy dataset
    random.seed(42)
    grade = [random.random() for point in range(0, n_points)]
    bumpy = [random.random() for point in range(0, n_points)]
    error = [random.random() for point in range(0, n_points)]
    y_axis = [round(grade[point]*bumpy[point]+0.3+0.1*error[point])
              for point in range(0, n_points)]
    for point in range(0, len(y_axis)):
        if grade[point] > 0.8 or bumpy[point] > 0.8:
            y_axis[point] = 1.0

    ### split into train/test sets
    x_axis = [[gg, ss] for gg, ss in zip(grade, bumpy)]
    split = int(0.75*n_points)
    x_axis_train = x_axis[0:split]
    x_axis_test = x_axis[split:]
    y_axis_train = y_axis[0:split]
    y_axis_test = y_axis[split:]

    #grade_sig = [xx_train[ii][0] for ii in range(0, len(xx_train)) if y_train[ii] == 0]
    #bumpy_sig = [xx_train[ii][1] for ii in range(0, len(xx_train)) if y_train[ii] == 0]
    #grade_bkg = [xx_train[ii][0] for ii in range(0, len(xx_train)) if y_train[ii] == 1]
    #bumpy_bkg = [xx_train[ii][1] for ii in range(0, len(xx_train)) if y_train[ii] == 1]

    #training_data = {"fast":{"grade":grade_sig, "bumpiness":bumpy_sig},
    #                 "slow":{"grade":grade_bkg, "bumpiness":bumpy_bkg}}


    #grade_sig = [xx_test[ii][0] for ii in range(0, len(xx_test)) if y_test[ii] == 0]
    #bumpy_sig = [xx_test[ii][1] for ii in range(0, len(xx_test)) if y_test[ii] == 0]
    #grade_bkg = [xx_test[ii][0] for ii in range(0, len(xx_test)) if y_test[ii] == 1]
    #bumpy_bkg = [xx_test[ii][1] for ii in range(0, len(xx_test)) if y_test[ii] == 1]

    #test_data = {"fast":{"grade":grade_sig, "bumpiness":bumpy_sig},
    #             "slow":{"grade":grade_bkg, "bumpiness":bumpy_bkg}}

    return x_axis_train, y_axis_train, x_axis_test, y_axis_test
    #return training_data, test_data
