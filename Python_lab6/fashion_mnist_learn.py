from tensorflow.keras.datasets import fashion_mnist
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Dropout
from tensorflow.python.keras.utils.np_utils import to_categorical
from tensorflow.python.keras.callbacks import TensorBoard


def main():

    # Загружаем данные в массивы. x_train - 60000 изображений, y_train - их номера классов. x_test - 10000 
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

    # Преобразуем в одномерный массив, т.к. Sequentlial работает только с одномерными
    x_train = x_train.reshape(60000, 784)

    # Интенсивность пикселя - 255, делим на 255, получаем значения в [0,1]
    x_train = x_train / 255
    x_test = x_test.reshape(10000, 784)
    x_test = x_test / 255

    # Преобразуем данные к категориальному представлению 0 - [1,0,0...]
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    
    # Создаем модель сети
    model = Sequential()

    # 784 нейрона, relu -функция активации
    model.add(Dense(784, input_dim=784, activation="relu"))
    model.add(Dropout(0.2))

    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))

    model.add(Dense(10, activation="softmax"))

    # Компиляция сети 
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.summary()
    callback = [TensorBoard(log_dir='logs', histogram_freq=1, write_images=True)]


    # Обучение модели
    model.fit(x_train,
              y_train,
              batch_size=100,           # Размер мини-выобрки
              epochs=100,
              verbose=1,                # Вывод информации во время обучения               
            #   validation_split=0.2,   # 20% на тесты, остальное на обучение
              callbacks=callback)


    # Сохраняем обученную модель
    model.save("fashion_model.h5")

    # Запускаем на тестовых данных
    score = model.evaluate(x_test, y_test, verbose=1)
    print("Accuracy on test data is", score[1]*100, "percent")


if __name__ == "__main__":
    main()
