# coding=utf-8

import sys
import autoarg

import numpy as np
import pandas as pd

import tensorflow as tf
import keras
import keras.backend as K
from sklearn.metrics import roc_auc_score


from keras.applications import VGG16
from keras.applications import InceptionV3
from keras.applications import ResNet50
from keras.applications.densenet import DenseNet169

from keras import models
from keras import layers
from keras.utils import multi_gpu_model


from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers

import os, shutil
import glob
import time

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from multi_gpu import make_parallel

#import warnings
#warnings.filterwarnings("ignore")

from datetime import datetime
crt_time = datetime.now().strftime('%Y%m%d%H%M%S')
crt_time = crt_time[:-6]


## Hyper Parameter Setting

VGG = False
ALL_LAYER_TRAIN = True
IMG_CHANNEL = 3
OUT_PUT_LAYES = 1
base_dir = '/data/private/noah/medi_image/'



def tf_train(N_EPOCHS,
             L_RATE,
             MINI_BATCH_SIZE,
             TEST_LABEL):

    print(N_EPOCHS,
          L_RATE,
          MINI_BATCH_SIZE,
          TEST_LABEL)

    tf_graph_dir = os.path.join(base_dir, 'tfgraph', crt_time + '_' + TEST_LABEL)
    saved_model_dir = os.path.join(base_dir, 'saved_model', crt_time + '_' + TEST_LABEL)

    print('Tensorflow Graph Dir : ', tf_graph_dir)
    print('Saved Model Dir : ', saved_model_dir)

    try:
        os.makedirs(tf_graph_dir)
        print(tf_graph_dir, 'Dir Created!!')
    except:
        print(tf_graph_dir, 'Dir already, files removed!!')

    try:
        os.makedirs(saved_model_dir)
        print(saved_model_dir, 'Dir Created!!')
    except:
        print(saved_model_dir, 'Dir already, files removed!!')

    tf.reset_default_graph()
    tf.set_random_seed(42)

    K.clear_session()

    sess = tf.Session()
    K.set_session(sess)

    if VGG:
        IMG_SIZE = 150
        LAYER_NAME = 'block5_conv1'
        conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(IMG_SIZE, IMG_SIZE, 3))
    else:
        IMG_SIZE = 224
        #LAYER_NAME = 'res5a_branch2c'
        conv_base = DenseNet169(weights='imagenet', include_top=False, input_shape=(IMG_SIZE, IMG_SIZE, IMG_CHANNEL))
        #conv_base = ResNet50(weights='imagenet', include_top=False, input_shape=(IMG_SIZE, IMG_SIZE, 3))


    with tf.name_scope('model'):#, tf.device("/gpu:0"):

        model = models.Sequential()
        model.add(conv_base)
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid'))
        logits = model.output

    model = multi_gpu_model(model, gpus=8)

    train_dir = os.path.join(base_dir, 'data/binary', TEST_LABEL, 'train/')
    valid_dir = os.path.join(base_dir, 'data/binary', TEST_LABEL, 'test/')

    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    test_dataget = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=MINI_BATCH_SIZE,
        class_mode='binary')  # 'binary')

    vlaid_generator = test_dataget.flow_from_directory(
        valid_dir,
        target_size=(IMG_SIZE, IMG_SIZE),
        batch_size=MINI_BATCH_SIZE,
        class_mode='binary')  # 'binary')

    chk_file_name = os.path.join(saved_model_dir, TEST_LABEL + '_saved_model.h5')

    tb_hist = keras.callbacks.TensorBoard(log_dir=tf_graph_dir, histogram_freq=0, write_graph=True, write_images=True)
    early_stop = keras.callbacks.EarlyStopping(monitor='val_acc', patience=3)
    chk_point = keras.callbacks.ModelCheckpoint(filepath=chk_file_name, monitor='train_acc', save_best_only=True)

    callbacks_list = [tb_hist, chk_point] #early_stop, chk_point]

    #model = make_parallel(model, 4)

    # with tf.device("/gpu:1"):
    model.compile(loss='binary_crossentropy',
                  optimizer=optimizers.Adam(lr=L_RATE),
                  metrics=['accuracy'])

    # with tf.device("/gpu:1"):


    #with tf.device("/gpu:1"):
    history = model.fit_generator(
            train_generator,
            #        steps_per_epoch=100,
            epochs=N_EPOCHS,
            validation_data=vlaid_generator,
            validation_steps=50,
            callbacks=callbacks_list,  # [tb_hist],
            max_queue_size=MINI_BATCH_SIZE * 2, workers=8,
            use_multiprocessing=True, shuffle=True)

    chk_file_name = os.path.join(saved_model_dir, TEST_LABEL + '_final_model.h5')

    model.save(chk_file_name)





def __main__(n_epochs=200,
             n_lr=1e-5,
             n_batch_size=256,
             s_label_name='Atelectasis'):

#    N_EPOCHS = n_epochs
#    L_RATE = n_lr
#    MINI_BATCH_SIZE = n_batch_size
#    TEST_LABEL = s_label_name

#    print (type(n_epochs),
#           type(n_lr),
#           type(n_batch_size),
#           type(s_label_name))

    print ('Inputed Arg '
           'Num Epochs :', n_epochs,
           'Learn Rate :', n_lr,
           'Batch Size :', n_batch_size,
           'Label Name :', s_label_name)

    tf_train(n_epochs, n_lr, n_batch_size, s_label_name)

    sys.exit(0)

autoarg.run(__main__)





#print('Tensorflow Graph Dir : ', tf_graph_dir)

#try:
#    os.makedirs(tf_graph_dir)
#    print('Dir Created!!')
#except:
#    os.system('rm ' + tf_graph_dir + '/*')
#    print('Dir already, files removed!!')








