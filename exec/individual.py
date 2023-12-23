#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def dict_transform(func):
    def wrapper(list1, list2):
        dictionary = func(list1, list2)
        return dict(zip(dictionary[0], dictionary[1]))
    return wrapper


@dict_transform
def print_dictionary(list1, list2):
    return list1, list2


if __name__ == "__main__":
    list1 = input("Введите первую строку: ").split()
    list2 = input("Введите вторую строку: ").split()
    result = print_dictionary(list1, list2)
    print(f"Результат: {result}")
    