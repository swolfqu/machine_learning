#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author  :   swolf.qu
# E-mail  :   swolf.qu@gmail.com
# Date    :   2018/01/03 15:38:43

"""
Classifying with k-Nearest Neighbors
"""
from collections import Counter

from numpy import array, tile, zeros


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ["A", "A", "B", "B"]
    return group, labels


def classify0(in_x, data_set, labels, k):
    print("data_set.shape: {}".format(data_set.shape))
    data_set_size = data_set.shape[0]
    print("data_set_size: {}".format(data_set_size))
    tile_in_x = tile(in_x, (data_set_size, 1))
    diffmat = tile_in_x - data_set
    print(diffmat)
    sq_diffmat = diffmat ** 2
    print(sq_diffmat)
    sq_distances = sq_diffmat.sum(axis=1)
    print(sq_distances)
    distances = sq_distances ** 0.5
    print(distances)
    sorted_dist_indicies = distances.argsort()
    class_count = Counter()
    for i in range(k):
        vote_label = labels[sorted_dist_indicies[i]]
        class_count[vote_label] += 1
    print(class_count.most_common(3))


def file2matrix(filename):
    labels = []
    with open(filename) as f:
        total_lines = len(f.readlines())
        print("total_lines: {}".format(total_lines))

        ret_mat = zeros((total_lines, 3))

        f.seek(0)
        for index, line in enumerate(f.readlines()):
            line = line.strip().split()
            print(line)
            ret_mat[index, :] = line[0:3]
            labels.append(line[-1])
    return ret_mat, labels


def main():
    # group, labels = create_data_set()
    # classify0([0, 0.05], group, labels, 3)
    # classify0([1, 2.0], group, labels, 3)
    file2matrix("datingTestSet.txt")

if __name__ == "__main__":
    main()
