import io
from PIL import Image
import numpy as np
# from tensorflow.keras.models import load_model
import joblib as jb
import cv2
from django.http import HttpResponse
MODEL_V1 = jb.load('Models/saved_model/v1/tooth_disease_cnn.h5')

LABELS = ['Cavity', 'Fillings', 'Impacted Tooth', 'Implant', 'Normal']

async def ready_file(file):
    x_ray = file.read()
    image = Image.open(io.BytesIO(x_ray))

    image_np = np.array(image)

    print(image_np.shape)
    return image_np

async def predict_by_model1(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    image_resized = cv2.resize(image_rgb, (70, 70))
    print('image shape:', image_resized.shape)
    prediction = MODEL_V1.predict(np.array([image_resized]))

    label = LABELS[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    result = {
        'title':f"Predicted:{label}\nConfidence: {confidence:.2f} %",
        "confidence": f'{confidence:.2f}',
        "predicted":label,
     }

    return result

async def make_prediction(image):
    image_np = await ready_file(image)

    prediction = await predict_by_model1(image_np)

    return prediction

