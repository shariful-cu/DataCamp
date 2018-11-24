#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:52:11 2018

=========utility functions in aomaly detection using deep learining=======

scipy_distance: 
    compute distances between two set of vectors using 
    scipy.spatial.distance

@author: Shariful
"""

import plotly.offline as py
import plotly.graph_objs as go
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
print(__version__)
init_notebook_mode(connected=True)
cf.go_offline()

from scipy.spatial import distance
import pandas as pd
import numpy as np
from  sklearn import metrics
from matplotlib import pyplot as plt


def plot_ROC(test_labels, test_predictions):
    fpr, tpr, thresholds = metrics.roc_curve(
            test_labels, test_predictions, pos_label=1)
    auc = "%.2f" % metrics.auc(fpr, tpr)
    title = 'ROC Curve, AUC = '+str(auc)
    with plt.style.context(('ggplot')):
        fig, ax = plt.subplots()
        ax.plot(fpr, tpr, "#000099", label='ROC curve')
        ax.plot([0, 1], [0, 1], 'k--', label='Baseline')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.legend(loc='lower right')
        plt.title(title)
    return fig 




#====Loading data
trn_nml = pd.read_csv('/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/train_normal.csv')
test_atk = pd.read_csv('/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/test_attack.csv')
test_nml = pd.read_csv('/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)/test_normal.csv')

# ======set the threshold
val_test_nml = test_nml.head(1312) #30% test normal
dist_val_to_nrml = distance.cdist(val_test_nml, \
                                  trn_nml, metric='euclidean')
dist_val_to_nrml = dist_val_to_nrml.mean(axis=1)
th0 = dist_val_to_nrml.mean()
dist_val_to_nrml = dist_val_to_nrml[dist_val_to_nrml <= 15]
th1 = dist_val_to_nrml.mean()

test_set = test_atk.append(test_nml.tail(len(test_nml)-1312))
test_labels = np.hstack((np.ones(len(test_atk), dtype = int), \
                          np.zeros(len(test_nml)-1312, dtype = int)))

dist_test = distance.cdist(test_set, trn_nml, metric='euclidean')
test_predictions = dist_test.mean(axis=1)


plot_ROC(test_labels, test_predictions)

#response0 = dist_test >= th0
#response1 = dist_test >= th1







#th0 = dist_val_to_nrml.mean()

##plotting mean of nomal dist on val set
#x_val = np.linspace(0, 1, len(dist_val_to_nrml))
## Create a trace
#trace = go.Scatter(
#    x = x_val,
#    y = dist_val_to_nrml
#)
#data = [trace]
#py.plot(data, 'scatter')
#==============================



#trn_nml_sub = trn_nml.iloc[1:5, 1:5]





#def linalg_norm(data):
#    a, b = data
#    return numpy.linalg.norm(a-b, axis=1)
#
#
#def sqrt_sum(data):
#    a, b = data
#    return numpy.sqrt(numpy.sum((a-b)**2, axis=1))


#def scipy_distance(data):
#    a, b = data
#    return list(map(distance.euclidean, a, b))
#
#
#a = (1, 2, 3)
#b = (4, 5, 6)
#dst = distance.euclidean(trn_nml, trn_nml)




#def mpl_dist(data):
#    a, b = data
#    return list(map(matplotlib.mlab.dist, a, b))
#
#
#def sqrt_einsum(data):
#    a, b = data
#    a_min_b = a - b
#    return numpy.sqrt(numpy.einsum('ij,ij->i', a_min_b, a_min_b))
#
#
#perfplot.show(
#    setup=lambda n: numpy.random.rand(2, n, 3),
#    n_range=[2**k for k in range(20)],
#    kernels=[linalg_norm, scipy_distance, mpl_dist, sqrt_sum, sqrt_einsum],
#    logx=True,
#    logy=True,
#    xlabel='len(x), len(y)'
#    )