import pandas as pd
# dataframe
from sklearn.naive_bayes import MultinomialNB, GaussianNB
# bayers rule
from sklearn.feature_extraction.text import CountVectorizer
# use to count words occurance
from sklearn import svm
# classifier
from sklearn.model_selection import GridSearchCV

# import data

data = pd.read_csv("dataset.csv")

# split into training data and testing data
EmailTextData = data["EmailText"]
LabelData = data["Label"]

EmailTextTrainingData = EmailTextData[0:4457]
LabelTrainingData = LabelData[0:4457]

EmailTextTestData = EmailTextData[4457:]
LabelTestData = LabelData[4457:]

# extract features
# count words appearance in the string
CountVectorizer = CountVectorizer()
features = CountVectorizer.fit_transform(EmailTextTrainingData)

# implement model
model = svm.SVC()
model.fit(features,LabelTrainingData)

# Testing Accuracy
features_test = CountVectorizer.transform(EmailTextTestData)

print("Accuracy of this model: ",model.score(features_test,LabelTestData))
