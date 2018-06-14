# -*- coding: utf-8 -*- #

import emoji
import numpy as np
from PIL import Image

def load_tsuki_matrix():
    """
    月行列を返す関数

    Args:
        無し
    Return:
        月行列8個, (numpyの行列のリスト)
    """
    tsuki_0000 = np.matrix([[-1, -1, -1, -1],
                            [-1, -1, -1, -1],
                            [-1, -1, -1, -1],
                            [-1, -1, -1, -1]])

    tsuki_0001 = np.matrix([[-1, -1, -1, 1],
                            [-1, -1, -1, 1],
                            [-1, -1, -1, 1],
                            [-1, -1, -1, 1]])

    tsuki_0011 = np.matrix([[-1, -1, 1, 1],
                            [-1, -1, 1, 1],
                            [-1, -1, 1, 1],
                            [-1, -1, 1, 1]])

    tsuki_0111 = np.matrix([[-1, 1, 1, 1],
                            [-1, 1, 1, 1],
                            [-1, 1, 1, 1],
                            [-1, 1, 1, 1]])

    tsuki_1000 = np.matrix([[1, -1, -1, -1],
                            [1, -1, -1, -1],
                            [1, -1, -1, -1],
                            [1, -1, -1, -1]])

    tsuki_1100 = np.matrix([[1, 1, -1, -1],
                            [1, 1, -1, -1],
                            [1, 1, -1, -1],
                            [1, 1, -1, -1]])

    tsuki_1110 = np.matrix([[1, 1, 1, -1],
                            [1, 1, 1, -1],
                            [1, 1, 1, -1],
                            [1, 1, 1, -1]])

    tsuki_1111 = np.matrix([[1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1]])

    return [tsuki_0000, tsuki_0001, tsuki_0011, tsuki_0111,
            tsuki_1000, tsuki_1100, tsuki_1110, tsuki_1111,]


def index2tsuki(index):
    if index==0:
        return emoji.emojize(':new_moon:', use_aliases=True)
    if index==1:
        return emoji.emojize(':waxing_crescent_moon:', use_aliases=True)
    if index==2:
        return emoji.emojize(':first_quarter_moon:', use_aliases=True)
    if index==3:
        return emoji.emojize(':waxing_gibbous_moon:', use_aliases=True)
    if index==4:
        return emoji.emojize(':waning_crescent_moon:', use_aliases=True)
    if index==5:
        return emoji.emojize(':last_quarter_moon:', use_aliases=True)
    if index==6:
        return emoji.emojize(':waning_gibbous_moon:', use_aliases=True)
    else:
        return emoji.emojize(':full_moon:', use_aliases=True)


def preprocess(img_file):


    img = Image.open(img_file)
    img = img.convert('L')


    width = 200
    height = int(width*(img.height/img.width))
    height -= height%4

    img = img.resize((width, height))
    img = np.matrix(img)
    img = ((np.abs(img-255.) / 128.) - 1.0) * (-1)


    return img
