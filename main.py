# class Product:
#     def __init__(self ,name, price  ):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return f"{self.name} - {self.price} tg."

# class ShoppingCart:
#     def __init__(self):
#         self.cart = [] 
#         self.all_product = [
#             {'name': 'Milk', 'quantity': 2, 'price': 1.50},  
#             {'name': 'Bread', 'quantity': 1, 'price': 0.80}, 
#             {'name': 'Cheese', 'quantity': 3, 'price': 3.00},
#             {'name': 'Eggs', 'quantity': 12, 'price': 0.20}, 
#             {'name': 'Butter', 'quantity': 1, 'price': 2.50}  
#         ]

#     def add_product(self, product_name, quantity):
#         for product in self.all_product:
#             if product['name'] == product_name:
#                 if product['quantity'] >= quantity:
#                     self.cart.append({'name': product_name, 'quantity': quantity, 'price': product['price']})
#                     product['quantity'] -= quantity
#                     print(f"{quantity} {product_name}(s) добавлено в корзину.")
#                 else:
#                     print(f"Недостаточно товара {product_name} в наличии.")
#                 return
#         print(f"Продукт {product_name} не найден.")

#     def remove_product(self, product_name):
#         self.cart = [product for product in self.cart if product['name'] != product_name]
#         print(f"Продукт {product_name} удален из корзины.")

#     def total_cost(self):
#         return sum(product['price'] * product['quantity'] for product in self.cart)

#     def show_cart(self):
#         if not self.cart:
#             print("Корзина пуста.")
#         else:
#             print("Содержимое корзины:")
#             for product in self.cart:
#                 print(f"{product['name']} - {product['quantity']} шт. по {product['price']}$ за штуку.")
#     def show_all_products(self):
#         print("Доступные продукты:")
#         for product in self.all_product:
#             print(f"{product['name']} - {product['quantity']} шт. по {product['price']}$ за штуку.")

# cart = ShoppingCart()
    
# while True:
#     print("\nВыберите действие:")
#     print("1. Посмотреть доступные продукты")
#     print("2. Добавить продукт в корзину")
#     print("3. Удалить продукт из корзины")
#     print("4. Показать содержимое корзины")
#     print("5. Рассчитать общую стоимость")
#     print("6. Выйти")
#     choice = input("Введите номер действия: ")
#     if choice == "1":
#         cart.show_all_products()
#     elif choice == "2":
#         product_name = input("Введите название продукта для добавления в корзину: ")
#         quantity = int(input("Введите количество: "))
#         cart.add_product(product_name, quantity)
#     elif choice == "3":
#         product_name = input("Введите название продукта для удаления из корзины: ")
#         cart.remove_product(product_name)
#     elif choice == "4":
#         cart.show_cart()
#     elif choice == "5":
#         total = cart.total_cost()
#         print(f"Общая стоимость корзины: ${total:.2f}")
#     elif choice == "6":
#         print("Выход из программы...")
#         break
#     else:
#         print("Неверный выбор, попробуйте снова.")

# a = {
#     'add': 1 , 'add' : 2
# }
# for i in a['add']:
#     print(i)

# # Импортируем библиотеки
# import tensorflow as tf
# import numpy as np
# import random

# # Определяем класс ShoppingCart
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}  # {название: (цена, количество)}
#         self.history = []  # История покупок
#         self.promocodes = {"DISCOUNT10": 0.1, "SALE20": 0.2}  # Промокоды 

#         # Данные для обучения модели
#         self.products = [
#             "красный", "синий", "зеленый", "желтый", "оранжевый", "розовый", 
#             "фиолетовый", "черный", "белый", "серый", "коричневый", "голубой", 
#             "пурпурный", "мятный", "березовый", "лавандовый", "песочный", 
#             "бирюзовый", "алый", "гранатовый", "темно-синий", "темно-зеленый", 

#         ]

#         self.history_matrix = np.zeros((len(self.products), len(self.products)))  # Матрица связей товаров

#         # Создаем нейросеть
#         self.model = self.create_model()

#     def create_model(self):
#         """Создает простую нейросеть для рекомендаций"""
#         model = tf.keras.Sequential([
#             tf.keras.layers.Dense(100, activation="relu", input_shape=(len(self.products),)),
#             tf.keras.layers.Dense(70, activation="relu"),
#             tf.keras.layers.Dense(len(self.products), activation="softmax")  # Вероятности рекомендаций
#         ])
#         model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
#         return model

#     def add_item(self, name):
#         """Добавление товара в корзину"""
#         if name in self.items:
#             self.items[name] += 1  # Увеличиваем количество на 1
#         else:
#             self.items[name] = 1  # Добавляем товар с количеством 1

#     def remove_item(self, name):
#         """Удаление товара из корзины"""
#         if name in self.items:
#             del self.items[name]
#         else:
#             print(f"Товар {name} отсутствует в корзине.")

#     def apply_promocode(self, code):
#         """Применение скидки по промокоду"""
#         return self.promocodes.get(code, 0)

#     def get_total_price(self, promocode=None):
#         """Получение итоговой стоимости с учетом промокода"""
#         total = len(self.items) * 50  # Предположим, что каждый товар стоит 50 (например)
#         discount = self.apply_promocode(promocode) if promocode else 0
#         return round(total * (1 - discount), 2)

#     def checkout(self):
#         """Оплата товаров и обучение модели"""
#         total = self.get_total_price()
#         print(f"Списано {total}₽. Покупка завершена!")

#         # Обновляем историю и обучаем модель
#         bought_items = list(self.items.keys())
#         self.update_history_matrix(bought_items)
#         self.train_model()

#         self.items.clear()  # Очищаем корзину

#     def update_history_matrix(self, bought_items):
#         """Обновляет матрицу связей между товарами"""
#         indexes = [self.products.index(item) for item in bought_items if item in self.products]
#         for i in indexes:
#             for j in indexes:
#                 if i != j:
#                     self.history_matrix[i][j] += 1  # Увеличиваем связь между товарами

#     def train_model(self):
#         """Обучает нейросеть на истории покупок"""
#         if np.sum(self.history_matrix) == 0:
#             return  # Если данных нет, обучение не требуется

#         # Данные для обучения (X - вход, Y - выход)
#         X_train = self.history_matrix.copy()
#         Y_train = (X_train > 0).astype(int)  # Ожидаемые результаты (горячие товары)

#         self.model.fit(X_train, Y_train, epochs=10, verbose=0)  # Тренировка модели

#     def recommend_product(self):
#         """ИИ-рекомендация товаров на основе истории"""
#         if not self.items:
#             return "Добавьте товары в корзину для получения рекомендаций."

#         # Генерируем входной вектор (что в корзине сейчас)
#         input_vector = np.zeros((1, len(self.products)))
#         for item in self.items.keys():
#             if item in self.products:
#                 input_vector[0][self.products.index(item)] = 1  # Отмечаем товар

#         # Прогоняем через модель и получаем вероятности
#         predictions = self.model.predict(input_vector)[0]
#         recommended_index = np.argmax(predictions)

#         if predictions[recommended_index] > 0.1:  # Если вероятность выше 10%
#             return f"Рекомендуем добавить: {self.products[recommended_index]}"
#         return "Пока нет рекомендаций."


# shopping_cart = ShoppingCart()


# shopping_cart.add_item("чёрный")
# shopping_cart.add_item("чёрный")
# shopping_cart.add_item("чёрный")
# shopping_cart.add_item("чёрный")
# shopping_cart.add_item("чёрный")
# shopping_cart.add_item("чёрный")

# print(f"Итоговая цена с учетом промокода 'DISCOUNT10': {shopping_cart.get_total_price('DISCOUNT10')}₽")

# print(shopping_cart.recommend_product())

# shopping_cart.checkout()



from unittest import result
from tensorflow import keras
import numpy as np
import cv2
import tkinter as tk 
from tkinter import Canvas
from PIL import Image , ImageGrab

model  = keras.models.load_model('mnist_model.h5')

window = tk.Tk()
window.title("Распознование цифр")

canvas = Canvas(window , width=280 , height=280 , bg = "white")
canvas.pack()


def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 10, y + 10, fill="black", outline="black")

def predict_digit():
    x = window.winfo_rootx()+canvas.winfo_x ()
    y = window.winfo_rooty()+canvas.winfo_y ()
    x1 = x + canvas.winfo_width()
    y1 = y+ canvas.winfo_height()

    img = ImageGrab.grab(bbox= (x,y,x1,y1)).convert("L")
    img = img.resize((28,28))
    img = np.array(img)

    img = cv2 .bitwise_not(img)
    img = img / 255.0
    img = img.reshape(1,28,28)

    prediction = model.predict(img)
    result_label.config(text = f"ИИ думает что это : {np.argmax(prediction)}")



def clear_canvas():
    canvas.delete("all")

canvas.bind("<B1-Motion>" , draw)
predict_button = tk.Button(window,text="Угадай" , command=predict_digit)
predict_button.pack()
clear_button = tk.Button(window,text="Очистить" , command=clear_canvas)
clear_button.pack()
result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack()
window.mainloop()
