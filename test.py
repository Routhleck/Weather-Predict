import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")