"""
@author: Vladimir Iglovikov
"""
from __future__ import division

from keras.models import Sequential

from keras.layers.convolutional import Convolution2D, MaxPooling2D, \
    ZeroPadding2D

from keras.optimizers import Adam
from keras.layers import Dense, Dropout, Flatten
import datetime
import os

from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import History
import pandas as pd

img_rows = 64
img_cols = 64


def simple_cnn():
    print '[{}] Creating model'.format(str(datetime.datetime.now()))
    model = Sequential()
    model.add(ZeroPadding2D((1, 1), input_shape=(3,
                                                 img_rows, img_cols)))

    model.add(Convolution2D(64, 3, 3, activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(64, 3, 3, activation='relu'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    return model


def save_model(model, suffix):
    json_string = model.to_json()
    json_name = 'architecture_' + suffix + '.json'
    weights_name = 'model_weights_' + suffix + '.h5'
    open(json_name, 'w').write(json_string)
    model.save_weights(weights_name, overwrite=True)


def save_history(history, suffix):
    filename = 'history_' + suffix + '.csv'
    pd.DataFrame(history.history).to_csv(filename, index=False)


if __name__ == '__main__':
    batch_size = 128

    history = History()

    data_path = '../data'

    train_path = os.path.join(data_path, 'train')
    val_path = os.path.join(data_path, 'val')
    test_path = os.path.join(data_path, 'test')

    train_datagen = ImageDataGenerator(
            rescale=1.0 / 255,
    )

    val_datagen = ImageDataGenerator(rescale=1.0 / 255)

    train_generator = train_datagen.flow_from_directory(
        train_path,
        target_size=(img_rows, img_cols),
        batch_size=batch_size,
        class_mode='binary')

    validation_generator = val_datagen.flow_from_directory(
        val_path,
        target_size=(img_rows, img_cols),
        class_mode='binary')

    model = simple_cnn()
    adam = Adam(lr=1e-5, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
    model.compile(optimizer=adam,
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit_generator(
        train_generator,
        samples_per_epoch=train_generator.N,
        nb_epoch=10,
        validation_data=validation_generator,
        nb_val_samples=validation_generator.N,
        callbacks=[history]
    )

    print '[{}] Saving model'.format(str(datetime.datetime.now()))
    now = datetime.datetime.now()
    suffix = str(now.strftime("%Y-%m-%d-%H-%M"))
    save_model(model, suffix)

    print '[{}] Saving history'.format(str(datetime.datetime.now()))
    save_history(history, suffix)

    print '[{}] Evaluating on test set'.format(str(datetime.datetime.now()))
    test_datagen = ImageDataGenerator(rescale=1.0 / 255)
    test_generator = test_datagen.flow_from_directory(
        test_path,
        target_size=(img_rows, img_cols),
        class_mode='binary')

    print model.evaluate_generator(test_generator, test_generator.N)
