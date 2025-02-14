
from pyexpat import model
from tensorflow import keras

mnist = keras.datasets.mnist

(X_train , y_train) , (X_test, y_test) = mnist.load_data()


X_train , X_test = X_train /255.0 , X_test/255.0


model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28,28)),

    keras.layers.Dense(128,activation = 'relu'),
    keras.layers.Dense(10,activation = 'softmax'),

])
model.compile(optimizer = 'adam',
            loss  = 'sparse_categorical_crossentropy',
            metrics = ['accuracy'])
        
model.fit(X_train, y_train , epochs = 5)

model.save("mnist_model.h5")
print("sAVE")