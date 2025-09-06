import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO



modelo = ResNet50(weights="imagenet")


def carregar_imagem_url(url):
    headers = {"User-Agent": "Mozilla/5.0"}  
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()  
    img = Image.open(BytesIO(response.content)).convert("RGB")
    img = img.resize((224, 224))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x


 ## """" Determinate URL """" ##

url = "https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg"


 ## """" Determinate URL """" ##



img, x = carregar_imagem_url(url)



preds = modelo.predict(x)
resultado = decode_predictions(preds, top=3)[0]


plt.imshow(img)
plt.axis("off")
plt.title(f"Previsto :  {resultado[0][1]} ({resultado[0][2]*100:.2f}%)")
plt.show()




print("Top 3 previsões:")
for (_, nome, prob) in resultado:
    print(f"{nome}: {prob*100:.2f}%")



