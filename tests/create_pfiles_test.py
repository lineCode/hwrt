#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import nose

# hwrt modules
from hwrt.HandwrittenData import HandwrittenData
import hwrt.preprocessing as preprocessing
import hwrt.features as features
import hwrt.create_pfiles as create_pfiles
import hwrt.data_multiplication as data_multiplication


# Test helper
def get_symbol(raw_data_id):
    current_folder = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_folder, "symbols/%i.json" % raw_data_id)
    return file_path


def get_symbol_as_handwriting(raw_data_id):
    symbol_file = get_symbol(raw_data_id)
    with open(symbol_file) as f:
        data = f.read()
    a = HandwrittenData(data)
    return a


# Tests
def training_set_multiplication_test():
    sample = get_symbol_as_handwriting(292934)
    training_set = [{'id': 1337,
                     'is_in_testset': 0,
                     'formula_id': 42,
                     'handwriting': sample,
                     'formula_in_latex': 'B'}]
    mult_queue = [data_multiplication.Multiply()]
    create_pfiles.training_set_multiplication(training_set, mult_queue)
    # nose.tools.assert_equal(len(feature_list), len(correct))


def parser_test():
    create_pfiles.get_parser()
