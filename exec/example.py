#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def benchmark(func):
    import time
    
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения: {end - start} сек.")
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://www.google.com')


if __name__ == "__main__":
    fetch_webpage()
    