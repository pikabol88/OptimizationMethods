from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

from recognition.utils import title, plot_gallery


def SMO():
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

    # Metrics
    print(f"Confusion matrix:\n{confusion_matrix(y_test, y_pred)}")
    score = accuracy_score(y_test, y_pred)
    print(f"Accuracy score: {score}")
    
    # Plots
    prediction_titles = [title(y_pred, y_test, digits.target, i) for i in range(y_pred.shape[0])]
    plot_gallery(X_test, prediction_titles, h, w)