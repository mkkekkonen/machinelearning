import numpy

class Perceptron(object):
  def __init__(self, eta=0.01, n_iter=50, random_state=1):
    self.eta = eta
    self.n_iter = n_iter
    self.random_state = random_state

  def fit(self, X, y):
    rgen = numpy.random.RandomState(self.random_state)
    self.w = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
    self.errors = []

    for i in range(self.n_iter):
      errors = 0
      for xi, target in zip(X, y):
        update = self.eta * (target - self.predict(xi))
        self.w[1:] += update * xi
        self.w[0] += update
        errors += int(update != 0.0)
      self.errors.append(errors)
    
    return self

  def net_input(self, X):
    return numpy.dot(X, self.w[1:]) + self.w[0]

  def predict(self, X):
    return numpy.where(self.net_input(X) >= 0.0, 1, -1)
