# ai that can detect if an image is a tie-fighter or a butterfly

import numpy as np
import tensorflow as tf
import keras
from tensorflow import keras
import matplotlib.pyplot as plt

# Load the model
model = keras.load_model('model.h5')

# Load an image
img_path = f"r'{input('Enter the path to the image: ')}'"
img = keras.image.load_img(img_path, target_size=(150, 150))
img_array = keras.image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# Predict the image
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

# Print results
print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(["tie-fighter", "butterfly"][np.argmax(score)], 100 * np.max(score))
)

# Display the image
plt.imshow(img)
plt.show()