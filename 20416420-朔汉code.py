import scipy.io as sio
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from MATLAB files
Train_x = sio.loadmat(r"D:\Documents\Changzhou University\7th Semester\Thesis 2024\Train_x.mat")['Train_x']
Train_y = sio.loadmat(r"D:\Documents\Changzhou University\7th Semester\Thesis 2024\Train_y.mat")['Train_y'].reshape(-1)

Test_x = sio.loadmat(r"D:\Documents\Changzhou University\7th Semester\Thesis 2024\Test_x.mat")['Test_x']
Test_y = sio.loadmat(r"D:\Documents\Changzhou University\7th Semester\Thesis 2024\Test_y.mat")['Test_y'].reshape(-1)

# Standardize/Normalize the data
scaler = StandardScaler()
Train_x = scaler.fit_transform(Train_x)
Test_x = scaler.transform(Test_x)

# Initialize SVM classifier with an RBF kernel
svm_classifier = svm.SVC(kernel='rbf')

# Perform grid search for hyperparameter tuning
param_grid = {'C': [0.1, 1, 10], 'gamma': [0.01, 0.1, 1]}
grid_search = GridSearchCV(svm_classifier, param_grid, cv=5)
grid_search.fit(Train_x, Train_y)

# Best hyperparameters
best_params = grid_search.best_params_
print("Best Hyperparameters:", best_params)

# Updated SVM classifier with best hyperparameters
svm_classifier = svm.SVC(**best_params)

# Perform 5-fold cross-validation
cv_scores = cross_val_score(svm_classifier, Train_x, Train_y, cv=5)

# Print cross-validation scores
print("Cross-Validation Scores:", cv_scores)
print("Mean Cross-Validation Accuracy: {:.2f}".format(cv_scores.mean()))

# Train the SVM classifier on the entire training set
svm_classifier.fit(Train_x, Train_y)

# Make predictions on the test set
predictions = svm_classifier.predict(Test_x)

# Calculate accuracy
accuracy = accuracy_score(Test_y, predictions)
print(f"Accuracy on Test Set: {accuracy:.2f}")

# Display classification report
print("Classification Report:")
print(classification_report(Test_y, predictions))

# Plot confusion matrix
conf_mat = confusion_matrix(Test_y, predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()
