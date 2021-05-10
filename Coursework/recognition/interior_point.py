from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

from mlfromscratch.supervised_learning import SupportVectorMachine as SVM
from mlfromscratch.utils.kernels import rbf_kernel
from mlfromscratch.utils import normalize

from recognition.utils import title, plot_gallery, convert_target


def interior_point():
    digits = datasets.load_digits()
    X = normalize(digits.data)
    n_samples, h, w = digits.images.shape
    # print(digits.data) # features
    # print(digits.target) # actual label

    X_train, X_test, y_train, y_test = train_test_split(X, convert_target(digits.target), test_size=0.1)

    clf = SVM(kernel=rbf_kernel, gamma=0.001, C=100) # SVM Classifier

    # fitting the classifier
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
