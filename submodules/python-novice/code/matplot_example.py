from matplotlib import pyplot

import numpy

data = numpy.loadtxt(fname='../data/inflammation-01.csv', delimiter=',')

image  = pyplot.imshow(data)
pyplot.show() # don't tell it what to show, then it shows you. Like, what?

ave_inflammation = data.mean(axis=0)
ave_plot = pyplot.plot(ave_inflammation)
pyplot.show() # as above

max_plot = pyplot.plot(data.max(axis=0))
pyplot.show() # as above

min_plot = pyplot.plot(data.min(axis=0))
pyplot.show() # as above
