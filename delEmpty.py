"""
删除空文件
"""

import os
rootdir = r'C:\Users\12391\Desktop\THUCNews\06教育'
dir_list = [rootdir]
for i in dir_list:
	dir_path = os.path.join(rootdir, i)
	print(i)
	file_list=os.listdir(dir_path)

	for i in file_list:
		file_path=os.path.join(dir_path, i)
		
		if not os.path.getsize(file_path):
			os.remove(file_path)
			print (file_path)
