import matplotlib.pyplot as plot
import numpy
from iris import get_data_frame

data_frame = get_data_frame()

# select setosa and versicolor
y = data_frame.iloc[0:100, 4].values
y = numpy.where(y == 'Iris-setosa', -1, 1)

X = data_frame.iloc[0:100, [0, 2]].values

plot.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plot.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plot.xlabel('sepal length (cm)')
plot.ylabel('petal length (cm)')
plot.legend(loc='upper left')
plot.show()


