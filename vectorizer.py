"""
分词之后向量化
"""

import os
import time
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib


def readTerm(term_file_folder_path):
    """
    读取Term文件,返回Term字符串生成器和类别生产器
    """
    def getTerm():
        classification = os.listdir(term_file_folder_path)
        for clsf in classification:
            print (clsf)
            # term = ''
            i=1
            for term_filename in os.listdir(term_file_folder_path + clsf):
                if i % 200 == 0:
                    print(i)

                path = term_file_folder_path + clsf + '/' + term_filename
                with open(path, 'rb') as f:
                    term_list = pickle.load(f)
                # term += ' '.join(term_list)
                term = ' '.join(term_list)
                i += 1

                yield term

    def getTarget():
        classification = os.listdir(term_file_folder_path)
        for num, clsf in enumerate(classification):
            for term_filename in os.listdir(term_file_folder_path+clsf):
                yield num

    # Term字符串生成器
    term_generator = getTerm()
    # Term的类别生成器
    target_generator = getTarget()

    return term_generator, target_generator


def generateMatrix(x):
    """
    生成特征矩阵
    """
    vectorizer = TfidfVectorizer(min_df=0.001)

    # 分词数据的文件夹路径
    term_file_folder_path = 'C:/Users/12391/Desktop/data/%s/term/' % x
    # 特征矩阵保存路径
    matrix_path = 'matrix/%s/matrix.pkl' % x

    # 读取数据
    term_generator, target_generator = readTerm(term_file_folder_path)

    # 训练集拟合后转换为矩阵，测试集根据拟合好的矢量器直接转换为矩阵
    if x == 'train':
        matrix = vectorizer.fit_transform(term_generator)
        joblib.dump(vectorizer.vocabulary_, 'matrix/vocabulary.pkl')

    elif x == 'test':
        vocabulary = joblib.load(r'C:\Users\12391\Desktop\TextClassification-master\matrix\vocabulary.pkl')
        vectorizer = TfidfVectorizer(min_df=0.001, vocabulary=vocabulary)
        matrix = vectorizer.fit_transform(term_generator)

    print(matrix.shape)
    # 保存特征矩阵
    joblib.dump(matrix, matrix_path)


if __name__ == '__main__':

    time_start = time.time()
    # train 或者 test
    generateMatrix('test')
    print ('Transform time:', time.time()-time_start, 's')
