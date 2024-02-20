# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oZIbbOyguSOhJvtNoO3bIa5ApR9wX9AQ
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf



"""Recapultatif

W: weights: le poids qui multiplie l'entree
Loss: fction perte ou l'erreur
en fction de l'erreur on modifie le w pour reduire l'erreur.
On chooisit le pas: vitesse d'apprentissage(le learning rate).
Terme a garder quand on parle du deep.

a chaque Epoch ou entrainement.



autre point : la dérivee c'est le taux de variation.

Entrainer un modele de deep learning c'est minimiser l'erreur
"""

data = tf.keras.datasets.fashion_mnist

data = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = data.load_data()

training_images.shape

test_images.shape

training_labels.shape

"""En deep learning, de façon général on manipule des tenseurs.

pour verifier ndim


"""

test_images.ndim

labels = ["t-shirt/top", "trouser", "pullover", "dress", "coat", "sandals", "shirt",
         "sneaker", "bag", "ankle boot"]

labels[0]

plt.imshow(training_images[67])
plt.title(labels[training_labels[67]])
plt.show()

plt.imshow(training_images[67])
plt.title(labels[training_labels[67]])
plt.show()

"""Comment entrainer les reseaux de neuronne

#Flatten (applatir image)

On considere les pixels comme caracterise individuelles
"""

a_training_images = training_images.reshape((60000, 28*28))
a_test_images = test_images.reshape((-1, 28*28))
#si on met -1 python sait qu'il doit chercher le premier

a_training_images.shape, a_test_images.shape
#on a desormais un reseau de neuronne
#on applatie les image on est passé, d'un shape de (60000,28,28) à un shape (60000,784) pareil pour les donnees de texte

"""Transformation de label: one hot-encoding(une colonne a 1 et les autrres ont 0).
si une image est de 0 : [1,0,0].

On va avoir trois neuronnes qui feront la prediction sur une classe.
"""

#petit exemple sur le one hot encoding
#c'est ce qu'on va appliquer au label
#si le label c'est 9 et qu on a trois class [0,1,2]
#si pour image A le label est 1 on aura [0,1,0]
#si pour image B est de classe 2 on aura [0,0,1]
x = np.array([1,2,9,1,0])
tf.keras.utils.to_categorical(x)

training_labels.shape

training_labels = tf.keras.utils.to_categorical(training_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

#chaque personne a pour label un vecteur de 10,un seul 1 à l'interieur qui a sa position
training_labels.shape

training_labels[67]
#le model aura predit le neuronne qui est chargé de prédire le tee-shirt.

"""#fction softmax
La fonction mathématique softmax peut être utilisée en machine learning pour convertir un score en probabilité dans un contexte de classification multi-classe.

Ainsi, si dans un contexte de classification d’objets nous obtenons :

Un score de 1200 pour la probabilité que l’objet soit une pomme.
Un score de 600 pour la probabilité que l’objet soit une orange.
Un score de 200 pour la probabilité que l’objet soit une poire.
Un score nul pour les autres probabilités.
L’application de la fonction softmax permettra de générer un score de probabilité normalisé, dont la somme totale des probabilités sera égale à 100%, soit 1.

Les résultats de la fonction softmax nous donneront :

pomme: 0.6
orange : 0.3
poire : 0.1


La fonction d’activation softmax est un élément important dans la conception d’un réseau de neurones.
"""

#petit exemple
output = [6,3,2]
6/(6+3+2) + 3/(6+3+2) + 2/(6+3+2)

6/(6+3+2),3/(6+3+2),2/(6+3+2)
#on a 0.54 pour 6, 0.27 pour 3 et on 0.18 pour 2
#cette façon de faire n'offre pas de gradient intéressant.

def sofmax(vect):
  r= np.exp(np.array(vect))
  return r/sum(r)

sofmax(output)
#il a maximisé l'element le plus important et a minimisé les autres.
#c'est ce meme principe qui sera utilisé dans le réseau de neuronne

"""#1er modele de classification"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

a_training_images.min(), a_training_images.max()

#normalisation des données
a_training_images = a_training_images /255.0
a_test_images = a_test_images / 255.0

a_training_images.min(), a_training_images.max()

#accuracy permet de savoir le taux de bonne de classification
model = Sequential([ Dense(units=784, activation="sigmoid"),
                   Dense(units=10, activation="softmax"),
                ])
model.compile(loss="mse", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
h = model.fit(a_training_images, training_labels, epochs=5, validation_data=(a_test_images, test_labels))

#loss: 0.0702 - accuracy: 0.4923 - val_loss: 0.0682 - val_accuracy: 0.5216
#on a 49% de de reussite sur les donnees d'entrainement, sur les donnees de test on a 52% de reussite.
#on peut l'ameliorer en changeant de loss (la maniere de calculer l'erreur).

"""#Cross Entropy ou Log loss

c'est une métrique utilisée pour mesurer la performance d'un modèle de classification en apprentissage automatique. La perte (ou l'erreur) est mesurée par un nombre compris entre 0 et 1, 0 correspondant à un modèle parfait.
"""

#entrainement avce Cross entropy
model = Sequential([ Dense(units=784, activation="sigmoid"),
                   Dense(units=10, activation="softmax"),
                ])
model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
h = model.fit(a_training_images, training_labels, epochs=5, validation_data=(a_test_images, test_labels))

#loss: 0.5440 - accuracy: 0.8108 - val_loss: 0.5519 - val_accuracy: 0.8048
#on a 81% de de reussite sur les donnees d'entrainement, sur les donnees de test on a 80% de reussite.

"""#fction d'activation relu (Rectified linear Unit)

elle permet tout simplement de remplacer les résultats négatifs par zéro
"""

#entrainement avec Relu
model = Sequential([ Dense(units=784, activation="relu"),
                   Dense(units=10, activation="softmax"),
                ])
model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
h = model.fit(a_training_images, training_labels, epochs=5, validation_data=(a_test_images, test_labels))

#loss: 0.4086 - accuracy: 0.8587 - val_loss: 0.4457 - val_accuracy: 0.8423
#on a 85% de de reussite sur les donnees d'entrainement, sur les donnees de test on a 84% de reussite.

"""Comparaison entre les differents entrainenements

MSE:           loss: 0.0703 - accuracy: 0.5186 - val_loss: 0.0682 - val_accuracy: 0.5590

Cross Entropy:  loss: 0.5440 - accuracy: 0.8108 - val_loss: 0.5519 - val_accuracy: 0.8048

Relu:           loss: 0.4086 - accuracy: 0.8587 - val_loss: 0.4457 - val_accuracy: 0.8423
"""

#entrainement avec Relu
model = Sequential([ Dense(units=784, activation="relu"),
                   Dense(units=10, activation="softmax"),
                ])
model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
h = model.fit(a_training_images, training_labels, epochs=20, validation_data=(a_test_images, test_labels))

model.summary()

#on est passé à 3 couches
model = Sequential([ Dense(units=784, activation="relu"),
                    Dense(units=128, activation="relu"),
                   Dense(units=10, activation="softmax"),
                ])
model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
h = model.fit(a_training_images, training_labels, epochs=20, validation_data=(a_test_images, test_labels))

model.summary()

def plot_loss_curve(history):


  plt.plot(list(range(len(history['loss']))), history['loss'], label = "loss")
  plt.plot(list(range(len(history['val_loss']))), history['val_loss'], label="val_loss")
  plt.xlabel('Epochs')
  plt.ylabel("Loss")
  plt.title("Loss Curve")
  plt.legend(loc='upper right')
  plt.show()

def plot_accuracy_curve(history):


  plt.plot(list(range(len(history['accuracy']))), history['accuracy'], label = "accuracy")
  plt.plot(list(range(len(history['val_accuracy']))), history['val_accuracy'], label="val_accuracy")
  plt.xlabel('Epochs')
  plt.ylabel("accuracy")
  plt.title("Accuracy Curve")
  plt.legend(loc='upper right')
  plt.show()

plot_loss_curve(h.history)
plot_accuracy_curve(h.history)

#On a un ecart qui se creuse entre le val_accuracy et Accuracy de l'entrainement, Quand on a un gros écart e ntre les donnees d'entrainement et les donnees de test.
#accuracy: 0.9097 - val_loss: 0.3248 - val_accuracy: 0.8843 Quand les donnees d'entrainement devient superieures on donnees de test, on a un overfitting

"""overfitting :

En pratique, un modèle qui overfit est souvent très facile à détecter. L’overfitting intervient lorsque l’erreur sur les données de test devient croissante. Typiquement, si l’erreur sur les données d’entraînements est beaucoup plus faible que celle sur les données de test, c’est sans doute que votre modèle a trop appris les données

#DropOut
"""

dropout = tf.keras.layers.Dropout(0.5, input_shape=(2,))

x = np.arange(1,11).reshape(5, 2).astype(np.float32)

tf.keras.layers.Dropout

x

#combattre l'overfitting avec dropout
model = Sequential([ Dense(units=784, activation="relu"),
                    tf.keras.layers.Dropout(0.5),
                    Dense(units=128, activation="relu"),
                     tf.keras.layers.Dropout(0.3),
                   Dense(units=10, activation="softmax"),
                ])
model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
h = model.fit(a_training_images, training_labels, epochs=20, validation_data=(a_test_images, test_labels))

model.summary()

"""loss: 0.3261 - accuracy: 0.8824 - val_loss: 0.3371 - val_accuracy: 0.8800.

On retient qu'il n'y a pas un grand écart entre accuracy et val_accuracy. On a réduit le overfitting
"""

plot_loss_curve(h.history)
plot_accuracy_curve(h.history)

"""#Collback - MethodeCheckpoint

On a vu un point qui a des meilleurs resultats. On voudrai garder le meilleur resultat, pour le faire on peut utiliser la fction callback.

Les collback sont des fctions introduit lors de l'entrainement, agissant comme un alerte qui permet de surveiller l'accuracy ett sauvegarde le meilleur accuracy lors dans l'entrainement d'un model.
"""

#il permet de sauvegarder le meilleur moddel encours
from tensorflow.keras.callbacks import ModelCheckpoint

#si c'etait le loss, on allait sauvegarder le min.
#on sauvegarde le meilleur
best_model = "best_model.h9"

model_ckp = ModelCheckpoint(filepath=best_model,
                            monitor="val_accuracy",
                            mode="max",
                            save_best_only=True)

model = Sequential([ Dense(units=784, activation="relu"),
                    tf.keras.layers.Dropout(0.5),
                    Dense(units=128, activation="relu"),
                     tf.keras.layers.Dropout(0.3),
                   Dense(units=10, activation="softmax"),
                ])
model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
h = model.fit(a_training_images, training_labels,
              epochs=30,
              validation_data=(a_test_images, test_labels),
              callbacks =[model_ckp])

model_save = tf.keras.models.load_model('best_model.h9')

model_save.evaluate(a_test_images, test_labels)

"""#Early stopping

Pour arreter l'entrainement plutot, on peut mettre des conditions pour l'arreter.
On peut mettre plusieurs epoch et arreter lorsque le meilleur accucracy se repete dans plusieurs Epoch
"""

#Callbacks sont des fctions qu'on peut ecrire,inserer lors de l'entrainement
stop = tf.keras.callbacks.EarlyStopping(monitor="val_accuracy", patience=2)

model_ckp

model = Sequential([ Dense(units=784, activation="relu"),
                    tf.keras.layers.Dropout(0.5),
                    Dense(units=128, activation="relu"),
                     tf.keras.layers.Dropout(0.3),
                   Dense(units=10, activation="softmax"),
                ])
model.compile(loss="categorical_crossentropy", optimizer=SGD(learning_rate=0.01), metrics=["accuracy"])
h = model.fit(a_training_images, training_labels,
              epochs=1000,
              validation_data=(a_test_images, test_labels),
              callbacks =[model_ckp, stop])

"""#Faire des prédictions  """

model_save = tf.keras.models.load_model('best_model.h9')

model_save.summary()

a_test_images[515].shape

test_labels[515]

np.argmax(test_labels[515])

labels[8]

pred = model_save.predict(a_test_images[515].reshape((1, 784)))

pred

np.argmax(pred)

labels[8]

plt.imshow(training_images[515])
#plt.title(labels[training_labels[8]])
plt.show()