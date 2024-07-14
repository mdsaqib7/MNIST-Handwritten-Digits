import tensorflow as tf

try:
    from tensorflow import keras
    print("Keras is installed and can be imported from TensorFlow.")
    print("TensorFlow version:", tf.__version__)
    print("Keras version:", keras.__version__)
except ImportError as e:
    print("Error importing Keras from TensorFlow:", e)
