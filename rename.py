"""
文件重命名
"""

import os

Root_dir = r"C:\Users\12391\Desktop\THUCNews\06教育"
new_dir1 = r"C:\Users\12391\Desktop\THUCNews\education\train"
new_dir2 = r"C:\Users\12391\Desktop\THUCNews\education\test"

files = os.listdir(Root_dir)
# print(os.path.join(Root_dir, files[0]))
count1 = 1
count2 = 1
count = 1
flag = True

for file in files:
	if flag:
		newName = os.path.join(new_dir1, str(count1) + '.txt')
		count1 += 1
		# print(count1)
	else:
		newName = os.path.join(new_dir2, str(count2) + '.txt')
		count2 += 1
		# print(count2)
	flag = not flag
	oldName = os.path.join(Root_dir, file)

	os.rename(oldName, newName)

	print(count)
	if count>=100000:
		break
	count +=1