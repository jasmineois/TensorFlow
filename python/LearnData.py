
# coding: utf-8

# In[1]:

import os
import sys
import random

if __name__ == '__main__':
    
    # ファイルを開く
    f = open('../data/train.txt', 'r')
    training = open('../data/training.txt','w')
        
    # データを入れる配列
    train_pass = []
    train_tag = []
    for line in f:
        # 改行を除いてスペース区切りにする
        line = line.rstrip()
        l = line.split()
        
        train_pass.append(l[0])
        train_tag.append(l[1])
    
    n = int(len(train_pass) -1)
    for arr in train_pass:
        i = random.randint(1, n)
        
        t = train_pass[n]
        train_pass[n] = train_pass[i]
        train_pass[i] = t

        t = train_tag[n]
        train_tag[n] = train_tag[i]
        train_tag[i] = t

    print(train_tag)
        
    for i, arr in enumerate(train_pass):
        training.write(train_pass[i] + ' ' + train_tag[i] + '\n')

    f.close()
    training.close()


# In[ ]:



