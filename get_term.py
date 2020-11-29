"""
查看分词结果
"""

import joblib
import os

# path = r'C:\Users\12391\Desktop\data\train\term\china'
# files = os.listdir(path)

# for file in files:
# 	term = joblib.load(os.path.join(path, file))
# 	print(term)

path = r'C:\Users\12391\Desktop\TextClassification-master\matrix\vocabulary.pkl'
vocabulary = joblib.load(path)
words = list(vocabulary.keys())[:500]
print(words)