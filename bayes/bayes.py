#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author  :  swolf.qu
# E-mail  :  swolf.qu@gmail.com
# Date    :  2018-01-23 11:35:52

import json

import numpy as np


def pretty_print_json(data):
    print(json.dumps(data, indent=4))


def load_train_dataset():
    train_list = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]    # 1 is abusive, 0 not
    return train_list, class_vec


def get_all_words(word_list):
    all_word = []
    [all_word.extend(x) for x in word_list]
    print(all_word)
    return list(set(all_word))


def get_word_list_vector(all_words, word_list):
    result = [0] * len(all_words)
    for word in word_list:
        if word in all_words:
            word_index = all_words.index(word)
            result[word_index] = 1
    return result


def all_words_to_vector(all_words, train_list):
    """
    Convert all_words to word vect according word is appear or not.
    :return: [[len of all_words], [....], ....]
    """
    all_words_vect = []
    for item in train_list:
        words_vec = get_word_list_vector(all_words, item)
        all_words_vect.append(words_vec)
    return all_words_vect


def train_nb(train_words_vec, class_vec):
    """
    Calculate the probability for each word.
    """
    p0_num = 0
    p1_num = 0
    p0_words_vec = np.zeros(len(train_words_vec[0]))
    p1_words_vec = np.zeros(len(train_words_vec[0]))

    for index, values in enumerate(train_words_vec):
        if class_vec[index] == 1:
            p1_num += sum(values)
            p1_words_vec += values
        else:
            p0_num += sum(values)
            p0_words_vec += values

    p0_vec = p0_words_vec / p0_num
    p1_vec = p1_words_vec / p1_num

    return p0_vec.tolist(), p1_vec.tolist()


def classify_nb(p0_vec, p1_vec, word_vec):
    words_p0 = sum(np.array(p0_vec) * np.array(word_vec))
    words_p1 = sum(np.array(p1_vec) * np.array(word_vec))
    print("words_p0: {} words_p1: {}".format(words_p0, words_p1))


def testing_nb():
    train_list, class_vec = load_train_dataset()
    all_words = get_all_words(train_list)
    print("all_words: {}".format(all_words))
    train_words_vec = all_words_to_vector(all_words, train_list)
    print("all_words_vec: {}".format(train_words_vec))
    test_entry = ['love', 'my', 'dalmation']
    print(test_entry)
    words_vector = get_word_list_vector(all_words, test_entry)
    p0_vec, p1_vec = train_nb(train_words_vec, class_vec)
    print("p0_vec: {}\np1_vec: {}".format(p0_vec, p1_vec))

    # Show words probability
    prob_stat = {}
    for index, word in all_words:
        prob_stat[item] = [p0_vec]

    classify_nb(p0_vec, p1_vec, words_vector)


if __name__ == "__main__":
    testing_nb()
