# -*- coding: utf-8 -*-
"""Untitled33.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UyxGwe9DE3AQ3Kt6pQXFHUX1A7p_lli3
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset into a pandas DataFrame
iris_df = pd.read_csv("iris.csv")

# Display the first few rows of the DataFrame
print(iris_df.head())

# Summary statistics of the dataset
print(iris_df.describe())

# Pairplot for visualizing relationships between variables
sns.pairplot(iris_df, hue='species', markers=['o', 's', 'D'])
plt.title('Pairplot of Iris Dataset')
plt.show()

# Boxplot to visualize distribution and detect outliers
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris_df.drop(columns='species'))
plt.title('Boxplot of Iris Dataset Features')
plt.show()

# Violin plot for better visualization of distribution
plt.figure(figsize=(10, 6))
sns.violinplot(x="species", y="petal_length", data=iris_df)
plt.title('Violin Plot of Petal Length by Species')
plt.show()

# Correlation heatmap to visualize the correlation between features
plt.figure(figsize=(8, 6))
sns.heatmap(iris_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Iris Dataset Features')
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset into a pandas DataFrame
iris_df = pd.read_csv("iris.csv")

# Add some missing values and outliers for demonstration
iris_df.loc[10:15, 'sepal_length'] = np.nan
iris_df.loc[30:35, 'petal_width'] = 8.0

# Visualize the distribution of the numeric columns before handling missing values and outliers
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.histplot(data=iris_df, x='sepal_length', kde=True)
plt.title('Distribution of Sepal Length')

plt.subplot(2, 2, 2)
sns.histplot(data=iris_df, x='sepal_width', kde=True)
plt.title('Distribution of Sepal Width')

plt.subplot(2, 2, 3)
sns.histplot(data=iris_df, x='petal_length', kde=True)
plt.title('Distribution of Petal Length')

plt.subplot(2, 2, 4)
sns.histplot(data=iris_df, x='petal_width', kde=True)
plt.title('Distribution of Petal Width')

plt.tight_layout()
plt.show()

# Handling missing values by mean imputation
iris_df_mean_imputed = iris_df.fillna(iris_df.mean())

# Handling outliers by clipping or winsorization
iris_df_mean_imputed['petal_width'] = iris_df_mean_imputed['petal_width'].clip(upper=iris_df_mean_imputed['petal_width'].quantile(0.95))

# Visualize the distribution after handling missing values and outliers
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
sns.histplot(data=iris_df_mean_imputed, x='sepal_length', kde=True)
plt.title('Distribution of Sepal Length (Mean Imputation)')

plt.subplot(2, 2, 2)
sns.histplot(data=iris_df_mean_imputed, x='sepal_width', kde=True)
plt.title('Distribution of Sepal Width (Mean Imputation)')

plt.subplot(2, 2, 3)
sns.histplot(data=iris_df_mean_imputed, x='petal_length', kde=True)
plt.title('Distribution of Petal Length (Mean Imputation)')

plt.subplot(2, 2, 4)
sns.histplot(data=iris_df_mean_imputed, x='petal_width', kde=True)
plt.title('Distribution of Petal Width (Mean Imputation)')

plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the Iris dataset into a pandas DataFrame
iris_df = pd.read_csv("iris.csv")

# Extract numeric columns for transformation
numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
numeric_data = iris_df[numeric_cols]

# Visualization of the original data distribution
plt.figure(figsize=(12, 6))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(2, 2, i)
    sns.histplot(data=iris_df, x=col, kde=True)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# Data Transformation Techniques

# Normalization
normalized_data = (numeric_data - numeric_data.min()) / (numeric_data.max() - numeric_data.min())

# Standardization
standardized_data = (numeric_data - numeric_data.mean()) / numeric_data.std()

# Logarithmic Transformation
log_transformed_data = np.log1p(numeric_data)

# Scaling using Min-Max scaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(numeric_data)

# Visualize the transformed data distributions
plt.figure(figsize=(12, 12))

# Original Data
plt.subplot(3, 2, 1)
sns.histplot(data=numeric_data, kde=True)
plt.title('Original Data')

# Normalization
plt.subplot(3, 2, 2)
sns.histplot(data=normalized_data, kde=True)
plt.title('Normalized Data')

# Standardization
plt.subplot(3, 2, 3)
sns.histplot(data=standardized_data, kde=True)
plt.title('Standardized Data')

# Logarithmic Transformation
plt.subplot(3, 2, 4)
sns.histplot(data=log_transformed_data, kde=True)
plt.title('Log-Transformed Data')

# Scaling using Min-Max scaler
scaled_df = pd.DataFrame(scaled_data, columns=numeric_cols)
plt.subplot(3, 2, 5)
sns.histplot(data=scaled_df, kde=True)
plt.title('Scaled Data')

plt.tight_layout()
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load the original Iris dataset into a pandas DataFrame
iris_df_original = pd.read_csv("iris.csv")

# Load the pre-processed Iris dataset (if available)
# For simplicity, let's assume the pre-processed dataset is already available and stored in a DataFrame called iris_df_preprocessed

# Splitting the dataset into features (X) and target variable (y)
X_original = iris_df_original.drop(columns=['species'])
y_original = iris_df_original['species']

# Splitting the original dataset into training and testing sets
X_train_original, X_test_original, y_train_original, y_test_original = train_test_split(X_original, y_original, test_size=0.2, random_state=42)

# Initialize classifiers
classifiers = {
    'KNN': KNeighborsClassifier(),
    'SVM': SVC(),
    'Naive Bayes': GaussianNB(),
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier()
}

# Function to train and evaluate classifiers
def train_and_evaluate(classifiers, X_train, X_test, y_train, y_test):
    results = {}
    for name, clf in classifiers.items():
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(f"{name}: Accuracy = {accuracy:.2f}")
    return results

# Train and evaluate classifiers on the original dataset
print("Results on original dataset:")
original_results = train_and_evaluate(classifiers, X_train_original, X_test_original, y_train_original, y_test_original)

# Pre-processing (e.g., standardization)
scaler = StandardScaler()
X_preprocessed = scaler.fit_transform(X_original)

# Splitting the pre-processed dataset into training and testing sets
X_train_preprocessed, X_test_preprocessed, y_train_preprocessed, y_test_preprocessed = train_test_split(X_preprocessed, y_original, test_size=0.2, random_state=42)

# Train and evaluate classifiers on the pre-processed dataset
print("\nResults on pre-processed dataset:")
preprocessed_results = train_and_evaluate(classifiers, X_train_preprocessed, X_test_preprocessed, y_train_preprocessed, y_test_preprocessed)

from sklearn.metrics import confusion_matrix, classification_report

# Function to display confusion matrix and classification report
def display_evaluation_metrics(y_true, y_pred):
    # Confusion Matrix
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

    # Classification Report
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))

# Train and evaluate classifiers on the original dataset
print("Results on original dataset:")
for name, clf in classifiers.items():
    clf.fit(X_train_original, y_train_original)
    y_pred = clf.predict(X_test_original)
    print(f"\n{name}:")
    display_evaluation_metrics(y_test_original, y_pred)

# Train and evaluate classifiers on the pre-processed dataset
print("\nResults on pre-processed dataset:")
for name, clf in classifiers.items():
    clf.fit(X_train_preprocessed, y_train_preprocessed)
    y_pred = clf.predict(X_test_preprocessed)
    print(f"\n{name}:")
    display_evaluation_metrics(y_test_preprocessed, y_pred)