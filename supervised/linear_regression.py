from utils.vectors import dot


class LinearRegression:
    """Linear regression with multiple features"""

    def __init__(self, X, Y, learning_procedure):
        self._X = [(1, *x) for x in X]
        self._Y = Y
        self._m = len(X)
        self.predict = None
        self._learning_procedure = learning_procedure
        self._T = [0] * len(X[0])

    @staticmethod
    def h(T):
        """Hypothesis"""
        return lambda X: dot(T, X)

    @property
    def _c(self):
        """Cost function"""
        return sum(
            (self.h(self._T)(x) - y) ** 2 for x, y in zip(self._X, self._Y)
        ) / (2 * self._m)

    def train(self):
        """Train a model"""
        self._T = self._learning_procedure(self._X, self._Y)
        self.predict = self.h(self._T)
