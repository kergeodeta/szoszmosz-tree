#! /usr/bin/env python3 
# -*- coding: utf-8 -*-

import random

TREE_HEIGHT = 40
BOUGH_REDUCING = 4
tree = list()

def get_block(placeholder = ' '):
    global TREE_HEIGHT
    return [placeholder] * (TREE_HEIGHT * 2 + 2)

def draw_tree():
    global tree
    global TREE_HEIGHT
    global BOUGH_REDUCING

    l = TREE_HEIGHT
    r = TREE_HEIGHT + 1
    for num in range(TREE_HEIGHT, 0, -1):
        bough = get_block()
        bough[l] = '/'
        bough[r] = '\\'

        if (num + 1) % 2 == 0 and l - 1 < r:
            ornament_pos = random.randint(l, r)
            if bough[ornament_pos] == ' ':
                bough[ornament_pos] = '*'

        l -= 1
        r += 1

        if num % (BOUGH_REDUCING * 2) == 0 and r - l > BOUGH_REDUCING * 2:
            l += BOUGH_REDUCING
            r -= BOUGH_REDUCING

        tree.append(bough)

    bottom_start = tree[-1].index('/')
    bottom_end = tree[-1].index('\\') + 1
    bottom = get_block()
    for pos in range(bottom_start, bottom_end):
        bottom[pos] = '-'
    tree.append(bottom)

def draw_bole():
    global TREE_HEIGHT
    global tree

    bole = get_block()
    bole[TREE_HEIGHT - 2] = bole[TREE_HEIGHT + 2] = '|'
    tree.append(bole)

def draw_ground():
    global tree

    ground = get_block('_')
    tree.append(ground)

def draw_all():
    draw_tree()
    draw_bole()
    draw_ground()

if __name__ == '__main__':
    draw_all()

    for bough in tree:
        print(''.join(bough))