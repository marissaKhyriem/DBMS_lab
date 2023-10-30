import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing import image
import matplotlib.pyplot as plt
import tensorflow.compat.v2 as tf

# Specify the paths to your training, testing, and evaluation image folders in Google Drive
TrainingImagePath = 'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Tr'
TestingImagePath = 'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Ts'
EvaluationImagePath = 'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Ev'

# Define data generators for training, testing, and evaluation
train_datagen = ImageDataGenerator(
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    rescale=1./255)  # Normalize pixel values to the range [0, 1]

test_datagen = ImageDataGenerator(rescale=1./255)

evaluation_datagen = ImageDataGenerator(rescale=1./255)

# Generate training, testing, and evaluation data
training_set = train_datagen.flow_from_directory(
    TrainingImagePath,
    target_size=(160, 160),
    batch_size=32,
    class_mode='categorical')

test_set = test_datagen.flow_from_directory(
    TestingImagePath,
    target_size=(160, 160),
    batch_size=32,
    class_mode='categorical')

evaluation_set = evaluation_datagen.flow_from_directory(
    EvaluationImagePath,
    target_size=(160, 160),
    batch_size=32,
    class_mode='categorical')

# Build a CNN model for face recognition
model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(160, 160, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))  # Dropout for regularization
model.add(Dense(len(training_set.class_indices), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(
    training_set,
    steps_per_epoch=len(training_set),
    epochs=10,
    validation_data=test_set,
    validation_steps=len(test_set))

# Evaluate the model on the evaluation data
evaluation_results = model.evaluate(evaluation_set, steps=len(evaluation_set))

# Print the evaluation results
print("Evaluation loss:", evaluation_results[0])
print("Evaluation accuracy:", evaluation_results[1])

# Define a function to predict a face in an image
def predict_face(image_path):
    img = image.load_img(image_path, target_size=(160, 160))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize pixel values

    prediction = model.predict(img)
    class_indices = training_set.class_indices
    predicted_class = list(class_indices.keys())[np.argmax(prediction)]

    # Visualize the image
    plt.imshow(img[0])
    plt.title(f"Predicted Class: {predicted_class}")
    plt.axis('off')
    plt.show()

    return predicted_class, prediction

# Specify the path to the image you want to make predictions on
image_paths = [
    'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Predict/1.jpg',
    'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Predict/2.jpg',
    'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Predict/3.jpg',
    'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Predict/4.jpg',
    'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Predict/5.jpg',
    'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Predict/6.jpg',
    'c:/Users/Asus/Documents/CS555_LAB/FRS-20231023T144637Z-001/FRS/Predict/7.jpg',
    

]

# Make predictions
for image_path in image_paths:
    predicted_class, prediction = predict_face(image_path)
    print("Predicted Class:", predicted_class)
    print("Prediction Scores:", prediction)