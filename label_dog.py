import os
import sys

import silence_tensorflow.auto
import tensorflow as tf


def hot_dog_or_not(image):

    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    print(bundle_dir)
    txtfile = os.path.join(bundle_dir, 'assets/models/hot_dog_labels.txt')
    pbfile = os.path.join(bundle_dir, 'assets/models/hot_dog_graph.pb')
    image_file = tf.io.gfile.GFile(image, 'rb')
    data = image_file.read()
    classes = [line.rstrip() for line in tf.io.gfile.GFile(txtfile)]
    with tf.io.gfile.GFile(pbfile, 'rb') as inception_graph:
        definition = tf.compat.v1.GraphDef()
        definition.ParseFromString(inception_graph.read())
        _ = tf.import_graph_def(definition, name='')

    with tf.compat.v1.Session() as session:
        tensor = session.graph.get_tensor_by_name('final_result:0')
        result = session.run(tensor, {'DecodeJpeg/contents:0': data})

        top_results = result[0].argsort()[-len(result[0]):][::-1]

        for type in top_results:
            if type is not None:
                hot_dog_or_not = classes[type]
                return hot_dog_or_not
