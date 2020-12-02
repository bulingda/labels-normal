# -*- coding: utf-8 -*-
""" 
    @author  : dingyaru
    @version : 
    @time    : 2020/12/1 14:50
    @function: 将标签文件中小于0和大于1的值规范化
"""
import os
import numpy as np

np.set_printoptions(suppress=True)
labels_path = r'/home/himap/train/xiamen-project-train-data-3/labels'
for f in os.listdir(labels_path):
    for file in os.listdir(os.path.join(labels_path, f)):  # train val
        data = ''
        with open(os.path.join(labels_path, f, file), 'r+') as labels_file:
            strs = labels_file.readlines()
            labels_list = []
            for line in strs:
                line_list = []
                for i in range(5):
                    line_list.append(float(line.split()[i]))
                labels_list.append(line_list)
            labels_numpy = np.array(labels_list)
            labels_numpy[labels_numpy < 0] = 0
            labels_numpy[labels_numpy > 1] = 1
            for i in range(len(strs)):
                lines = ''
                for j in range(5):
                    if j == 0:
                        lines += str(int(labels_numpy[i][j])) + ' '
                    elif j == 4:
                        lines += str(labels_numpy[i][j])
                    else:
                        lines += str(labels_numpy[i][j]) + ' '
                data += lines + '\n'
        with open(os.path.join(labels_path, f, file), 'w+') as labels_file:
            labels_file.writelines(data)
