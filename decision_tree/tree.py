#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author  :  swolf.qu
# E-mail  :  swolf.qu@gmail.com
# Date    :  2018-01-11 18:17:29

import math
import json

from collections import defaultdict, Counter


def create_dataset():
    dataset = [
        [1, 1, "yes"],
        [1, 1, "yes"],
        [1, 0, "no"],
        [0, 1, "no"],
        [0, 1, "no"]
    ]
    labels = ["no surfacing", "flippers"]
    return dataset, labels


def calculate_shannon_entropy(dataset):
    num_entries = len(dataset)
    label_counter = Counter()
    for feat_vec in dataset:
        cur_label = feat_vec[-1]
        label_counter[cur_label] += 1

    entropy = 0.0
    for k in label_counter:
        prob = float(label_counter[k])/num_entries
        entropy -= prob * math.log(prob, 2)
    return entropy


def split_dataset(dataset, axis, value):
    ret = []
    for feat_vec in dataset:
        if feat_vec[axis] == value:
            reduce_feature_vec = feat_vec[:axis]
            reduce_feature_vec.extend(feat_vec[axis+1:])
            ret.append(reduce_feature_vec)
    return ret


def choose_best_feature(dataset):
    best_feature = -1
    max_gain = 0.0
    num_features = len(dataset[0]) - 1
    base_entropy = calculate_shannon_entropy(dataset)
    for i in range(num_features):
        column_values = set([x[i] for x in dataset])
        new_entropy = 0.0
        for val in column_values:
            new_dataset = split_dataset(dataset, i, val)
            prop = float(len(new_dataset)) / len(dataset)
            entropy = calculate_shannon_entropy(new_dataset)
            new_entropy += prop * entropy
            print("{} {} entropy: {}".format(i, val, new_entropy))
        info_gain = base_entropy - new_entropy
        print("Feature {} entorpy: {} info_gain: {}".format(
            i, new_entropy, info_gain))
        if info_gain > max_gain:
            max_gain = info_gain
            best_feature = i
    print("best_feature: {}".format(best_feature))
    print(dataset)
    return best_feature


def majority_count(class_list):
    """
    :param class_list:
    :return: The class that occurs with the greatest frequency.
    """

    class_count = Counter()
    for vote in class_list:
        class_count[vote] += 1
    return class_count.most_common(1)


def create_tree(dataset, labels):
    dtree = defaultdict(dict)
    class_list = [x[-1] for x in dataset]

    # All in one class
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    # Only one column in dataset
    if len(dataset[0]) == 1:
        return majority_count(class_list)

    best_feat = choose_best_feature(dataset)
    best_feat_label = labels[best_feat]
    del labels[best_feat]
    feat_values = set([x[best_feat] for x in dataset])
    for value in feat_values:
        sublabels = labels[:]
        subdataset = split_dataset(dataset, best_feat, value)
        dtree[best_feat_label][value] = create_tree(subdataset, sublabels)
    return dtree


if __name__ == "__main__":
    dataset, labels = create_dataset()
    print(dataset)
    print(labels)
    entropy = calculate_shannon_entropy(dataset)
    print(entropy)
    ret = split_dataset(dataset, 0, 1)
    print(ret)

    choose_best_feature(dataset)
    mytree = create_tree(dataset, labels)
    print("my tree----------------------------")
    print(mytree)
    print(json.dumps(mytree, indent=4))
