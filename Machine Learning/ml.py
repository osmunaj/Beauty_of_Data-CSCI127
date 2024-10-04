# --------------------------------------
# Simple Machine Learning Demo
# --------------------------------------

from sklearn import datasets, svm
from sklearn.tree import DecisionTreeClassifier

# --------------------------------------

def learn(classifier, dataset):
    n = len(dataset.data)
    classifier.fit(dataset.data[:-n//2], dataset.target[:-n//2])
    predicted_answers = classifier.predict(dataset.data[-n//2:])
    correct_answers = dataset.target[-n//2:]

    correct = 0
    for predicted, target in zip(predicted_answers, correct_answers):
        if predicted == target:
            correct += 1
    print("Percentage correct = {:.2f}\n".format(100 * correct / (n // 2)))

# --------------------------------------

def dataset_demonstration(dataset): 
    print("Dataset Data")
    print(dataset.data)
    print("Length:", len(dataset.data))
    print("Dataset Classifications")
    print(dataset.target)
    print("Length:", len(dataset.target))

# --------------------------------------

def main():
    digits = datasets.load_digits()
    dataset_demonstration(digits)

    classifier = svm.SVC(gamma=0.001, C=100.0)
    print("Support Vector Machine")
    learn(classifier, digits)

    for depth in range(1, 11):
        classifier = DecisionTreeClassifier(max_depth = depth)
        print("Decision Tree of Depth", depth)
        learn(classifier, digits)

# --------------------------------------

if __name__ == "__main__":
    main()