import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]]
    true_name = target_names[y_test[i]]
    return 'predicted: %s\ntrue:      %s' % (pred_name, true_name)


def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


def main():
    digits = datasets.load_digits()
    n_samples, h, w = digits.images.shape
    print(digits.data) # features
    print(digits.target) # actual label

    clf = svm.SVC(gamma=0.001, C=100) # SVM Classifier

    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.1)
    
    #fitting the classifier
    clf.fit(X_train, y_train)

    # Predicting
    y_pred = clf.predict(X_test)

    prediction_titles = [title(y_pred, y_test, digits.target, i) for i in range(y_pred.shape[0])]
    plot_gallery(X_test, prediction_titles, h, w)
    plt.show()

    # Metrics
    print(f"Confusion matrix:\n{confusion_matrix(y_test, y_pred)}")
    score = accuracy_score(y_test, y_pred)
    print(f"Accuracy score: {score}")
