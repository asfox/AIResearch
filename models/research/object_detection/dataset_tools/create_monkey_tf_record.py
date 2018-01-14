#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:23:20 2018

@author: rurikoimai
"""

import tensorflow as tf
import matplotlib.image as mpimg
from object_detection.utils import dataset_util


flags = tf.app.flags
#flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
flags.DEFINE_string('output_path', '', 'Users/rurikoimai/AIResearch/models/research/object_detection/')
flags.DEFINE_string('data_dir', 'Users/rurikoimai/Desktop/images/', 'Root directory to raw monkey dataset')
flags.DEFINE_string('label_map_path', 'data/monkey_label_map.pbtxt', 'Path to lavel map proto')
FLAGS = flags.FLAGS


def create_tf_example( roi_file ):
      # TODO(user): Populate the following variables from your example.
  
    image_file = roi_file[:-4]+'.png'
  
    img = mpimg.imread(image_file)
    height = img.shape[0] # Image height
    width = img.shape[0] # Image width
  
    with open(roi_file) as fp:
        roi_list = [x.strip().split(',') for x in fp.readlines()]
      
    xmins = [] # List of normalized left x coordinates in bounding box (1 per box)
    xmaxs = [] # List of normalized right x coordinates in bounding box
             # (1 per box)
    ymins = [] # List of normalized top y coordinates in bounding box (1 per box)
    ymaxs = [] # List of normalized bottom y coordinates in bounding box
             # (1 per box)
    for roi in roi_list:
        coords = [float(coord) for coord in roi]
        xmins.append(coords[0])
        xmaxs.append(coords[2])
        ymins.append(coords[1])
        ymaxs.append(coords[3])
  
    filename = image_file # Filename of the image. Empty if image is not from file
    encoded_image_data = str(img.dtype) # Encoded image bytes
    image_format = b'png' # b'jpeg' or b'png'

    classes_text = ['Monkey'] # List of string class name of bounding box (1 per box)
    classes = [1 for x in xmins] # List of integer class id of bounding box (1 per box)

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_image_data),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):

    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)

    # TODO(user): Write code to read in your dataset to examples variable

    for roi_file in file_list:
        tf_example = create_tf_example(roi_file)
        writer.write(tf_example.SerializeToString())

    writer.close()


if __name__ == '__main__':
  tf.app.run()