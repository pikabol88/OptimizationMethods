"""
Source: https://towardsdatascience.com/support-vector-machines-learning-data-science-step-by-step-f2a569d90f76
"""

import numpy as np

from scipy import optimize
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

from recognition.utils import title, plot_gallery, convert_target

class MaxMarginClassifier:
    
    def __init__(self):
        self.alpha = None
        self.w = None
        self.supportVectors = None
    
    def fit(self, X, y):
        N = len(y)
        # Gram matrix of (X.y)
        Xy = X * y[:, np.newaxis]
        GramXy = np.matmul(Xy, Xy.T)

        # Lagrange dual problem
        def Ld0(G, alpha):
            return alpha.sum() - 0.5 * alpha.dot(alpha.dot(G))

        # Partial derivate of Ld on alpha
        def Ld0dAlpha(G, alpha):
            return np.ones_like(alpha) - alpha.dot(G)

        # Constraints on alpha of the shape :
        # -  d - C*alpha  = 0
        # -  b - A*alpha >= 0
        A = -np.eye(N)
        b = np.zeros(N)
        constraints = ({'type': 'eq',   'fun': lambda a: np.dot(a, y), 'jac': lambda a: y},
                       {'type': 'ineq', 'fun': lambda a: b - np.dot(A, a), 'jac': lambda a: -A})

        # Maximize by minimizing the opposite
        optRes = optimize.minimize(fun=lambda a: -Ld0(GramXy, a),
                                   x0=np.ones(N), 
                                   method='SLSQP', 
                                   jac=lambda a: -Ld0dAlpha(GramXy, a), 
                                   constraints=constraints)
        self.alpha = optRes.x
        self.w = np.sum((self.alpha[:, np.newaxis] * Xy), axis=0)  
        epsilon = 1e-6
        self.supportVectors = X[self.alpha > epsilon]
        # Any support vector is at a distance of 1 to the separation plan
        # => use support vector #0 to compute the intercept, assume label is in {-1, 1}
        supportLabels = y[self.alpha > epsilon]
        self.intercept = supportLabels[0] - np.matmul(self.supportVectors[0].T, self.w)
    
    def predict(self, X):
        """ Predict y value in {-1, 1} """
        assert(self.w is not None)
        assert(self.w.shape[0] == X.shape[1])
        return 2 * (np.matmul(X, self.w) > 0) - 1


def slsqp():
    digits = datasets.load_digits()
    n_samples, h, w = digits.images.shape
    # print(digits.data) # features
    # print(digits.target) # actual label

    clf = MaxMarginClassifier() # SVM Classifier

    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.1)
    
    # Fitting the classifier
    clf.fit(X_train, y_train)

    # Predicting
    y_pred = clf.predict(X_test)

    # Metrics
    # print(f"Confusion matrix:\n{confusion_matrix(y_test, y_pred)}")
    score = accuracy_score(y_test, y_pred)
    print(f"Accuracy score: {score}")
    
    # Plots
    prediction_titles = [title(y_pred, y_test, digits.target, i) for i in range(y_pred.shape[0])]
    plot_gallery(X_test, prediction_titles, h, w)