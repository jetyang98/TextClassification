"""
朴素贝叶斯
"""

import datetime
from sklearn.naive_bayes import MultinomialNB
import pickle
import joblib
import os
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics

categories = ['china', 'country', 'culture', 'education', 'entertainment', 'finance', 'pe', 'shares', 'society', 'technology']
class_code = {'china':0, 'country':1, 'culture':2, 'education':3, 'entertainment':4, 'finance':5, 'pe':6, 'shares':7, 'society':8, 'technology':9}

label = []
for te in categories:
	label.extend([te]*50000)

ConfusionMatrix = np.zeros([len(class_code),len(class_code)])

def showPredictResult():
        for i in range(len(ConfusionMatrix)):
            keyWord = ""
            for key in class_code:
                if class_code[key] == i:
                    keyWord = key
                    break
            print ("===================================================")
            print (keyWord + "类预测总数为:", np.sum([ConfusionMatrix[i]]))
            print (keyWord + "类预测正确数为:", ConfusionMatrix[i][i])
            for j in range(len(ConfusionMatrix[0])):
                if j == i:
                    continue
                predictKey = ""
                for key in class_code:
                    if class_code[key] == j:
                        predictKey = key
                        break
                print (keyWord+"类预测为"+predictKey+"数为:", ConfusionMatrix[i][j])
        print ("===================================================")

def metrics_result(label, predict):
        print('精度:{0:.3f}'.format(metrics.precision_score(label, predict, average='weighted')))
        print('召回:{0:0.3f}'.format(metrics.recall_score(label, predict, average='weighted')))
        print('f1-score:{0:.3f}'.format(metrics.f1_score(label, predict, average='weighted')))
        print(classification_report(label, predict))

def trainProcess():
    """
    训练朴素贝叶斯分类器
    """
    # 训练集特征矩阵保存路径
    train_matrix_path = 'matrix/train/matrix.pkl'
    # 后验概率保存路径
    prob_clf_path = 'results/baselineModel.pkl'
    
    # 加载数据
    matrix = joblib.load(train_matrix_path)

    # 计算每一类中每个特征的后验概率
    prob_clf = []
    for clf in range(0, 10):
        start_row = clf

        end_row = clf+1

        vector = matrix[start_row:end_row].sum(axis=0)
        total_word = matrix[start_row:end_row].sum()

        prob = np.log((vector+1)/float(total_word))
        prob_clf.append(prob)

    # 保存后验概率
    joblib.dump(prob_clf, prob_clf_path)

def predictProcess():

		modelPath = r'C:\Users\12391\Desktop\TextClassification-master\results\NBModel.pkl'
		clf = joblib.load(modelPath)

		print ("加载模型成功")

		tfidfmetrix = joblib.load(r'C:\Users\12391\Desktop\TextClassification-master\matrix\test\matrix.pkl')
		# 预测分类结果
		predicted = clf.predict(tfidfmetrix)

		print(len(label))
		for flabel, expct_cate in zip(label, predicted):
			ConfusionMatrix[class_code[flabel]][class_code[expct_cate]] += 1

		print("预测完成")
		showPredictResult()
		metrics_result(label, predicted)
		print ("混淆矩阵为:")
		# 显示所有列
		# pd.set_option('display.max_columns', None)
		# 显示所有行
		# pd.set_option('display.max_rows', None)
		print (pd.DataFrame(confusion_matrix(label, predicted), columns=categories, index=categories))


if __name__ == "__main__":
	trainProcess()
	# predictProcess()
