import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
import string

# Read in csv as dataframe
df = pd.read_csv('defgh.csv')

# Positive sentiment: reviews w/ scores > 3
# Negative sentiment: reviews w/ scores < 3
# (scores == 3 are removed because neutral)
df = df[df['Score'] != 3]
df['Sentiment'] = np.where(df['Score'] < 3, -1, 1)

# Get positive reviews
positive = df[df['Sentiment'] == 1]
# Get negative reviews
negative = df[df['Sentiment'] == -1]

# Display histogram of positive and negative sentiment
df['Sentiments'] = np.where(df['Sentiment'] == -1, 'negative', 'positive')
fig = px.histogram(df, x="Sentiments")
fig.update_layout(title_text='Apartments Sentiments in Chicago')
fig.show()

# Remove all blank entries
df = df.dropna(subset=['Summary'])

# Remove all punctuations
for category, data in df.items():
    if (category == 'Summary'):
        for text in data:
            text = text.translate(None, string.punctuation)

# Split dataframe into test and train sets: 80% for training, 20% for testing
percentage = 0.8
index = df.index
df['rand_num'] = np.random.randn(len(index))
train = df[df['rand_num'] <= percentage]
test = df[df['rand_num'] > percentage]


# Create bag of words
vectorizer = CountVectorizer()
train_matrix = vectorizer.fit_transform(train['Summary'])
test_matrix = vectorizer.transform(test['Summary'])


# Logistic Regression
log_reg = LogisticRegression()

# Fit logistic regression using training data set
x_train = train_matrix
y_train = train['Sentiment']
log_reg.fit(x_train, y_train)

# Get testing data set
x_test = test_matrix
y_test = test['Sentiment']

# Get prediction using logistic regression
predictions = log_reg.predict(x_test)

# Test model's accuracy:
# Get confusion matrix
print(confusion_matrix(predictions, y_test))

# Print classification report
print(classification_report(predictions, y_test))
