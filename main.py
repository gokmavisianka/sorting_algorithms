import pygame
from random import randint, choice, shuffle
from threading import Thread
import numpy as np


clock = pygame.time.Clock()

ARRAY = list(range(1, 1001, 1))
shuffle(ARRAY)
COPY = ARRAY[:]

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 1000))

    def draw_and_update(self, array, case=1):
        LENGTH = len(array)
        SIZE = round(1000 / LENGTH)
        for i in range(len(array)):
            value = array[i]
            height = value
            y = 1000 - height
            if case == 0:
                pygame.draw.rect(self.screen, (0, 0, 0), (i * SIZE, 0, SIZE, 1000))
                pygame.draw.rect(self.screen, (255, 255, 255), (i * SIZE, y, SIZE, SIZE))
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), (i * SIZE, 0, SIZE, 1000))
                pygame.draw.rect(self.screen, (255, 255, 255), (i * SIZE, y, SIZE, height))

        pygame.display.update()
        clock.tick(144)
        

def quick_sort(array):  # n * (1 + 2^n) comparisons
    length = len(array)
    if length == 1:
        return array
    else:
        average = sum(array) / length
        left, right = [], []
        for element in array:
            if element < average:
                left.append(element)
            else:
                right.append(element)

        return quick_sort(left) + quick_sort(right)

def index_sort(array):  # (2^n) * (2^n) comparisons
    length = len(array)
    copy = array[:]
    for x in range(length):
        index = 0
        for y in range(length):
            if x != y:
                index += copy[x] >= copy[y]
        array[index] = copy[x]
        game.draw_and_update(array=array)

    return array

def min_sort(array):
    length = len(array)
    copy = array[:]
    for i1 in range(length):
        MIN = min(copy)
        array[i1] = MIN
        copy.remove(MIN)
        game.draw_and_update(array=array)
    return array

def bubble_sort(array):  # (2^n) * (2^n) comparisons
    length = len(array)
    a = float("inf")
    while True:
        condition = False
        for index in range(length):
            b = array[index]
            if b < a and index != 0:
                array[index - 1], array[index] = array[index], array[index - 1]
                condition = True
            a = b
        game.draw_and_update(array=array)
        if condition is False:
            break

    return array

def lineer_interpolation_sort(array):
    length = len(array)
    my_min = min(array)
    my_max = max(array)
    copy = array[:]
    c = (my_max - my_min) / (length - 1)
    print(c)
    for i1 in range(length):
        i2 = round((copy[i1] - my_min) / c)
        array[i2] = copy[i1]
        game.draw_and_update(array=array)
    return array

def function(ARRAY=ARRAY):
    print(index_sort(ARRAY))
    ARRAY = COPY[:]
    print(bubble_sort(ARRAY))
    ARRAY = COPY[:]
    print(min_sort(ARRAY))
    ARRAY = COPY[:]
    print(lineer_interpolation_sort(ARRAY))
    print("YAY")

game = Game()

Thread(target=function).start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

    clock.tick(30)
    
