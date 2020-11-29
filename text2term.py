"""
分词，读取原文件，保存成分词文件
"""

import os
import logging
import pickle
import multiprocessing
import re
import jieba


def convertText2Term(*args):
    """
    将Text文本文件转为Term分词文件
    此函数作为一个进程
    """

    jieba.setLogLevel(logging.INFO)

    text_path = args[0]
    term_path = args[1]
    stopwords_list = args[2]

    # 读取Text文件
    with open(text_path, 'r', encoding='utf8') as f:
        text = f.read()
    
    # 分词
    term_list = [x for x in jieba.cut(text)]

    # 过滤分词
    filter_pattern = re.compile(r'\d+|零|一|二|三|四|五|六|七|八|九|十|百|千|万|亿')
    filtered_term_list = []
    for term in term_list:

        # 被过滤的分词：长度小于2, 包含数字或字母或中文数词, 停用词
        if len(term)<2 or filter_pattern.search(term) or (term in stopwords_list):
            pass
        else:
            filtered_term_list.append(term)

    # 存储分词
    with open(term_path, 'wb') as f:
        pickle.dump(filtered_term_list, f)


def processText(text_file_folder_path, term_file_folder_path):
    """
    处理指定路径下的所有Text文件
    """
    # 创建进程池,参数为池中进程数
    # pool = multiprocessing.Pool(6)

    # 获取停用词表
    with open('stopwords.txt', 'r', encoding='utf8') as f:
        stopwords_list = [line.strip() for line in f.readlines()]

    # classification = os.listdir(text_file_folder_path)
    classification = ['pe']
    # print(classification)
    for clsf in classification:
        print (clsf)
        for text_filename in os.listdir(text_file_folder_path+clsf):
            text_path = text_file_folder_path + clsf + '/' + text_filename
            term_path = term_file_folder_path + clsf + '/' + text_filename.split('.')[0] + '.pkl'
            # print (term_path)
            args = (text_path, term_path, stopwords_list)

            # 调用文本转分词的进程
            # pool.apply_async(convertText2Term, args)
            print (text_path)
            convertText2Term(*args)
            
    # pool.close()
    # pool.join()


if __name__ == '__main__':
    # 训练集文本数据的文件夹路径
    text_file_folder_path = 'C:/Users/12391/Desktop/data/train/raw/'
    # 训练集分词数据的文件夹路径
    term_file_folder_path = 'C:/Users/12391/Desktop/data/train/term/'
    # 处理训练集文本
    processText(text_file_folder_path, term_file_folder_path)


    # # 测试集文本数据的文件夹路径
    # text_file_folder_path = 'data/test/raw/'
    # # 测试集分词数据的文件夹路径
    # term_file_folder_path = 'data/test/term/'
    # # 处理测试集文本
    # processText(text_file_folder_path, term_file_folder_path)
