__author__ = 'alex'
import numpy as np
import pylab as pl
from Tool import *

data = DataBuilder("trainset.txt")
for data_instance in data.dataset:
    if data_instance.label == 1:
        pl.plot(data_instance.x, data_instance.y, "or")
    else:
        pl.plot(data_instance.x, data_instance.y, "ob")
pl.show()

