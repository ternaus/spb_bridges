"""
@author: Vladimir Iglovikov
"""
from __future__ import division
import datetime
import os
import cv2


def _crop_save_image(from_path, to_path):
    """
    Crop images, so that only bride is there. Here we exploit the fact that camera, that both
    camera and bridge are static
    @param: from_path - path to filename that contains original image
    @param: to_path - path to filename that will contain resulting image
    """
    img = cv2.imread(from_path)[20:20+64, 420:420+64]  # Magic numbers from manual image inspection
    cv2.imwrite(to_path, img)


random_state = 2016
data_path = '../data'

print '[{}] Defining path variables'.format(str(datetime.datetime.now()))

up_path = os.path.join(data_path, 'up')
down_path = os.path.join(data_path, 'down')

train_path = os.path.join(data_path, 'train')
val_path = os.path.join(data_path, 'val')
test_path = os.path.join(data_path, 'test')

train_up_path = os.path.join(train_path, 'up')
train_down_path = os.path.join(train_path, 'down')

test_up_path = os.path.join(test_path, 'up')
test_down_path = os.path.join(test_path, 'down')

val_up_path = os.path.join(val_path, 'up')
val_down_path = os.path.join(val_path, 'down')

print '[{}] Splitting'.format(str(datetime.datetime.now()))
up_filenames = os.listdir(up_path)
down_filenames = os.listdir(down_path)


val_up_filenames = [x for x in up_filenames if ('2016-07-20' in x) or ('2016-07-21' in x)]
val_down_filenames = [x for x in down_filenames if ('2016-07-20' in x) or ('2016-07-21' in x)]

test_up_filenames = [x for x in up_filenames if ('2016-07-22' in x) or ('2016-07-23' in x)]
test_down_filenames = [x for x in down_filenames if ('2016-07-22' in x) or ('2016-07-23' in x)]

train_up_filenames = set(up_filenames).difference(set(val_up_filenames)).difference(set(test_up_filenames))
train_down_filenames = set(down_filenames).difference(set(val_down_filenames)).difference(set(test_down_filenames))


print '[{}] Copying train'.format(str(datetime.datetime.now()))
os.mkdir(train_path)
os.mkdir(train_up_path)
os.mkdir(train_down_path)
print '[{}] Copying train up'.format(str(datetime.datetime.now()))

for file_name in train_up_filenames:
    _crop_save_image(os.path.join(up_path, file_name), os.path.join(train_up_path, file_name))

print '[{}] Copying train down'.format(str(datetime.datetime.now()))
for file_name in train_down_filenames:
    _crop_save_image(os.path.join(down_path, file_name), os.path.join(train_down_path, file_name))

print '[{}] Copying val'.format(str(datetime.datetime.now()))
os.mkdir(val_path)
os.mkdir(val_up_path)
os.mkdir(val_down_path)

print '[{}] Copying val up'.format(str(datetime.datetime.now()))
for file_name in val_up_filenames:
    _crop_save_image(os.path.join(up_path, file_name), os.path.join(val_up_path, file_name))

print '[{}] Copying val down'.format(str(datetime.datetime.now()))
for file_name in val_down_filenames:
    _crop_save_image(os.path.join(down_path, file_name), os.path.join(val_down_path, file_name))

print '[{}] Copying test'.format(str(datetime.datetime.now()))
os.mkdir(test_path)
os.mkdir(test_up_path)
os.mkdir(test_down_path)

print '[{}] Copying test up'.format(str(datetime.datetime.now()))
for file_name in test_up_filenames:
    _crop_save_image(os.path.join(up_path, file_name), os.path.join(test_up_path, file_name))

print '[{}] Copying test down'.format(str(datetime.datetime.now()))
for file_name in test_down_filenames:
    _crop_save_image(os.path.join(down_path, file_name), os.path.join(test_down_path, file_name))
