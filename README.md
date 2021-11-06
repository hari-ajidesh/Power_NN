# Power_NN
This repository contains an implementation of neural networks to determine ship effective power at operating conditions based on one of the technical papers published in Naval Engineers Journal.We have implemented this model with real-world data that was scraped from Fleetmon which contains most of the attributes which were present in the original dataset used in the paper. Scraped data and the code for scraping is also provided in the scraping folder.

Language : TensorFlow

Video : https://youtu.be/bORmY2huy2o

## Neural Network Model Architecture Used:
-Input Layer : Normalizer Layer

-Hidden Layers : 3 stacked layers where each is Dense Layer with swish activation function

-Output Layer : Dense Layer

