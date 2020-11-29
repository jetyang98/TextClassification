"""
朴素贝叶斯预测过程
"""
import pickle as pkl
import numpy as np
from scipy import sparse
from sklearn import metrics
import joblib

len_features = 5000
# ========== 开始读入数据 ===========
print("data read begin")
tfidf = joblib.load(r'C:\Users\12391\Desktop\TextClassification-master\matrix\train\matrix.pkl')
y = []
for i in range(10):
    y.extend([i]*50000)
print("data read end")
# ========== 结束读入数据 ===========

# scores = np.load('./data/NBscores_{}.npy'.format(len_features))
# y_pred = []
# i = 1
# for doc in tfidf:
#     doc = doc.toarray().flatten()
#     # for i, key in enumerate(doc):
#     #     if key != 0:
#     #         doc[i] = 1
#     tmp = scores.dot(doc)
#     y_pred.append(tmp.argmax())
# joblib.dump(y_pred, 'data/y_pred.pkl')

y_pred = joblib.load('data/y_pred.pkl')

print(metrics.confusion_matrix(y, y_pred))
print(metrics.accuracy_score(y, y_pred))
print(metrics.f1_score(y, y_pred, average="macro"))