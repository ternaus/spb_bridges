"""
@author: Vladimir Iglovikov
Script reads images, corresponding to up and down positions of the bridge and splits into folders:

train,
val,
test
"""

import datetime
import os
import shutil

from sklearn.cross_validation import train_test_split

random_state = 2016
data_path = '../data'

print '[{}] Defining path variables'.format(str(datetime.datetime.now()))

up_path = os.path.join(data_path, 'up')
down_path = os.path.join(data_path, 'up')

train_path = os.path.join(data_path, 'train')
val_path = os.path.join(data_path, 'val')
test_path = os.path.join(data_path, 'test')

train_up_path = os.path.join(train_path, 'up')
train_down_path = os.path.join(train_path, 'down')

val_up_path = os.path.join(val_path, 'up')
val_down_path = os.path.join(val_path, 'down')

test_up_path = os.path.join(test_path, 'up')
test_down_path = os.path.join(test_path, 'down')

print '[{}] Splitting'.format(str(datetime.datetime.now()))
up_filenames = os.listdir(up_path)
down_filenames = os.listdir(down_path)

print '[{}] Cuting test'.format(str(datetime.datetime.now()))
train_up_filenames, test_up_filenames = train_test_split(up_filenames,
                                                         test_size=0.2,
                                                         random_state=random_state)
train_down_filenames, test_down_filenames = train_test_split(down_filenames,
                                                             test_size=0.2,
                                                             random_state=random_state)

print '[{}] Cuting validation'.format(str(datetime.datetime.now()))
train_up_filenames, val_up_filenames = train_test_split(train_up_filenames,
                                                        test_size=0.25,
                                                        random_state=random_state)
train_down_filenames, val_down_filenames = train_test_split(train_down_filenames, test_size=0.25,
                                                            random_state=random_state)

print '[{}] Copying train'.format(str(datetime.datetime.now()))
os.mkdir(train_path)
os.mkdir(train_up_path)
os.mkdir(train_down_path)
print '[{}] Copying train up'.format(str(datetime.datetime.now()))

for file_name in train_up_filenames:
    shutil.copy(os.path.join(up_path, file_name), os.path.join(train_up_path, file_name))

print '[{}] Copying train down'.format(str(datetime.datetime.now()))
for file_name in train_down_filenames:
    shutil.copy(os.path.join(down_path, file_name), os.path.join(train_down_path, file_name))

print '[{}] Copying val'.format(str(datetime.datetime.now()))
os.mkdir(val_path)
os.mkdir(val_up_path)
os.mkdir(val_down_path)

print '[{}] Copying val up'.format(str(datetime.datetime.now()))
for file_name in val_up_filenames:
    shutil.copy(os.path.join(up_path, file_name), os.path.join(val_up_path, file_name))

print '[{}] Copying val down'.format(str(datetime.datetime.now()))
for file_name in val_down_filenames:
    shutil.copy(os.path.join(down_path, file_name), os.path.join(val_down_path, file_name))

print '[{}] Copying test'.format(str(datetime.datetime.now()))
os.mkdir(test_path)
os.mkdir(test_up_path)
os.mkdir(test_down_path)

print '[{}] Copying test up'.format(str(datetime.datetime.now()))
for file_name in test_up_filenames:
    shutil.copy(os.path.join(up_path, file_name), os.path.join(test_up_path, file_name))

print '[{}] Copying test down'.format(str(datetime.datetime.now()))
for file_name in test_down_filenames:
    shutil.copy(os.path.join(down_path, file_name), os.path.join(test_down_path, file_name))
