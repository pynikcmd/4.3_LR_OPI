#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Man (человек), с полями: имя, возраст, пол и вес.
Определить методы переназначения имени, изменения возраста и изменения
веса. Создать производный класс Student, имеющий поле года обучения.
Определить методы переназначения и увеличения года обучения.
"""


class Man:
    def __init__(self, name, age, sex, weight):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__weight = weight

    def change_name(self, new_name):
        self.__name = new_name  # Метод для изменения имени

    def change_age(self, new_age):
        self.__age = new_age  # Метод для изменения возраста

    def change_weight(self, new_weight):
        self.__weight = new_weight  # Метод для изменения веса

    def print_info(self):
        print("Class Man")
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Sex: {self.__sex}")
        print(f"Weight: {self.__weight}")
        print("")


class Student(Man):
    def __init__(self, name, age, sex, weight, study_year):
        super().__init__(name, age, sex, weight)  # Вызов конструктора родительского класса для инициализации полей
        self.__study_year = study_year  # Инициализация приватного поля "год обучения"

    def change_study_year(self, new_st_year):
        self.__study_year = new_st_year  # Метод для изменения года обучения

    def increment_study_year(self):
        self.__study_year += 1  # Метод для увеличения года обучения на 1

    def print_info(self):
        print("Class Student")
        super().print_info()  # Вызов метода print_info() родительского класса
        print(f"Study year: {self.__study_year}")  # Вывод информации о годе обучения
        print("")


if __name__ == '__main__':
    man = Man('Lila', 23, 'female', 89)
    man.print_info()
    man.change_name('Yulia')
    man.change_age(24)
    man.change_weight(95)
    man.print_info()
    st1 = Student('Fin', 20, 'male', 70, 2)
    st1.print_info()
    st1.change_weight(72)
    st1.change_name('Max')
    st1.increment_study_year()
    st1.change_study_year(6)
    st1.print_info()
