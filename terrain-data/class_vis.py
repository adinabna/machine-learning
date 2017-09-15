#!/usr/bin/python

import base64
import json

import warnings

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('agg')

#from udacityplots import *
warnings.filterwarnings("ignore")

#plt.ioff()

def pretty_picture(clf, x_test, y_test):
    x_min = 0.0
    x_max = 1.0

    y_min = 0.0
    y_max = 1.0

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    step_size = .01  # step size in the mesh
    x_axis, y_axis = np.meshgrid(np.arange(x_min, x_max, step_size),
                                 np.arange(y_min, y_max, step_size))
    predictions = clf.predict(np.c_[x_axis.ravel(), y_axis.ravel()])

    # Put the result into a color plot
    predictions = predictions.reshape(x_axis.shape)
    plt.xlim(x_axis.min(), x_axis.max())
    plt.ylim(y_axis.min(), y_axis.max())

    #plt.pcolormesh(x_axis, y_axis, predictions, cmap=plt.cm.seismic)
    plt.pcolormesh(x_axis, y_axis, predictions, cmap=plt.get_cmap('seismic'))

    # Plot also the test points
    grade_sig = [x_test[ii][0] for ii in range(0, len(x_test)) if y_test[ii] == 0]
    bumpy_sig = [x_test[ii][1] for ii in range(0, len(x_test)) if y_test[ii] == 0]
    grade_bkg = [x_test[ii][0] for ii in range(0, len(x_test)) if y_test[ii] == 1]
    bumpy_bkg = [x_test[ii][1] for ii in range(0, len(x_test)) if y_test[ii] == 1]

    plt.scatter(grade_sig, bumpy_sig, color="b", label="fast")
    plt.scatter(grade_bkg, bumpy_bkg, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")

    #plt.savefig("test.png")
    figure = plt.gcf()
    plt.show()
    plt.draw()
    figure.savefig("test.png", dpi=100)

def output_image(name, format, bytes):
    image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.b64encode(bytes)
    print image_start+json.dumps(data)+image_end
