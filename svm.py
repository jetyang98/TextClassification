"""
SVM
"""

import joblib
from sklearn import metrics, svm
import datetime
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import pandas as pd
import sklearn.decomposition

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

def trainSVM():
	print ("SVM训练过程开始:")
	begintime = datetime.datetime.now()
	clf = svm.LinearSVC()
	f = r'C:\Users\12391\Desktop\TextClassification-master\matrix\train\matrix.pkl'
	tfidfmatrix = joblib.load(f)
	print(tfidfmatrix.shape)

	# pca = sklearn.decomposition.TruncatedSVD(n_components=2500)
	# pca.fit(tfidfmatrix)
	# with open("results/pca_fit_matrix.pkl", "wb") as file_obj:
	# 	pickle.dump(pca, file_obj)
	
	pca = joblib.load("results/pca_fit_matrix.pkl")
	print(pca.get_params())
	tfidfmatrix_pca = pca.transform(tfidfmatrix)
	print(tfidfmatrix_pca.shape)

	endtime1 = datetime.datetime.now()
	span = endtime1 - begintime
	print('时间：', span.seconds)

	clf.fit(tfidfmatrix_pca, label)
	
	with open("results/SVMModel.pkl", "wb") as file_obj:
		pickle.dump(clf, file_obj)

	endtime = datetime.datetime.now()
	span = endtime - endtime1
	print ("SVM训练时间:", span.seconds)

def predictProcess():

		modelPath = r'C:\Users\12391\Desktop\TextClassification-master\results\SVMModel.pkl'
		clf = joblib.load(modelPath)

		print ("加载模型成功")

		# tfidfmetrix = joblib.load(r'C:\Users\12391\Desktop\TextClassification-master\matrix\test\matrix.pkl')
		# pca = joblib.load('results/pca_fit_matrix.pkl')
		# tfidf_pca = pca.transform(tfidfmetrix)
		# print(tfidf_pca.shape)
		
		# # 预测分类结果
		# predicted = clf.predict(tfidf_pca)

		# # 保存predicted
		# joblib.dump(predicted, r'C:\Users\12391\Desktop\TextClassification-master\results\svm_predicted.pkl')

		# 加载predicted
		predicted = joblib.load(r'C:\Users\12391\Desktop\TextClassification-master\results\svm_predicted.pkl')

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

if __name__ == '__main__':
	# trainSVM()
	predictProcess()
	
