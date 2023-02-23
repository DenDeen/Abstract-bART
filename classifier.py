
import cv2
import numpy as np
import tensorflow as tf
from keras.models import Model,  load_model
from tensorflow.keras.applications.resnet import preprocess_input

def classifier_image(image_path):

    # Load model
    model = load_model('resnet50_trained.h5')
    img = cv2.imread(image_path)
    img = cv2.resize(img,(224,224))
    img_np = np.array(img) 

    # Preprocessing
    img_batch = np.expand_dims(img_np, axis = 0)
    processed_image = preprocess_input(img_batch.copy()) 
    predictions = model.predict(processed_image) 
    decoded_preds = decode_binary_predictions(predictions, top=1)
    return decoded_preds[0][0][0]

def decode_binary_predictions(preds, top=1):
    # Return top predicted class label and score for binary classification
    class_indices = ['AI Generated', 'Not AI Generated']  # Replace with your actual class labels
    results = []
    for pred in preds:
        top_indices = pred.argsort()[-top:][::-1]
        result = [(class_indices[i], pred[i]) for i in top_indices]
        results.append(result)
    return results
