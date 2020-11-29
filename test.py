"""
测试代码用的
"""

trainMatrix = r'C:\Users\12391\Desktop\TextClassification-master\matrix\train\matrix.pkl'
testMatrix = r'C:\Users\12391\Desktop\TextClassification-master\matrix\test\matrix.pkl'
import joblib
import sklearn.decomposition
import numpy as np

# print(joblib.load(trainMatrix).shape)
# print(joblib.load(testMatrix).shape)

a = [
	[1,2,3],
	[2,2,4],
	[2,3,5]
]
a = np.array(a)
# print(a)

b = sklearn.decomposition.TruncatedSVD(n_components=2)
c = b.fit_transform(a)
# b.transform(a)
print(b.components_)
print(b.explained_variance_)
print(b.explained_variance_ratio_)
print(b.singular_values_)
print(c)