#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import os
import copy
from typing import List

from DataStruct import Compartment


def alfarray(alphabet="0123456789abcdefghijklmnopqrstwvuxyzABCDEFGHIJKLMNOPQRSTWVUXYZ,. \t\n", file="file.txt"):
    # generating array of signs based on given alphabet and file which is preparation to encode and decode
    toret = []
    signgs = 0
    for sign in alphabet:
        toret.append([sign, 0])
    with open(file, 'r') as f:
        for sign in f.read():
            signgs += 1
            for val in toret:
                if val[0] == sign:
                    val[1] = val[1] + 1
                    break
        f.close()
    return sorted([[val[0], val[1] / signgs] for val in toret if val[1] != 0], key=lambda v: v[1])


def genArrayOfCompartments(alphabet="0123456789abcdefghijklmnopqrstwvuxyzABCDEFGHIJKLMNOPQRSTWVUXYZ,. \t\n", file="file.txt"):
    # Array of ranges
    tmp_array_of_compartments: List[Compartment] = []
    for i, val in enumerate(alfarray(alphabet, file)):
        tmp_elem = 0.0 if i == 0 else tmp_array_of_compartments[i - 1].range[1]
        tmp_array_of_compartments.append(Compartment(
            (tmp_elem, tmp_elem + val[1]),
            val[0]
        ))
    return tmp_array_of_compartments


def encode(alphabet: str = "0123456789abcdefghijklmnopqrstwvuxyzABCDEFGHIJKLMNOPQRSTWVUXYZ,. \t\n",
           file: str = "file.txt", output: str = "out_file.txt") -> None:
    # function writing outfile with strings  encoding in style "{float} {length}#" where # - word break
    array_of_compartments = genArrayOfCompartments(alphabet, file)
    print(array_of_compartments)
    if os.path.exists(output):
        os.remove(output)
    with open(output, "a+") as f:
        f.write(str(array_of_compartments) + "\n")
    with open(file, "r") as input_file:
        for line in input_file.readlines():
            tmp_str = ''
            for elem in line.split():
                number = 0.0
                tmp_array = copy.deepcopy(array_of_compartments)
                for sign in elem:
                    compartment = next(x for x in tmp_array if x.letter == sign)
                    first = compartment.range[0]
                    last = compartment.range[1]
                    size = last - first
                    print('Litera {} zakres: {}, {} wielkość: {}'.format(compartment.letter, compartment.range[0],
                                                                         compartment.range[1], size))
                    for itr, val in enumerate(array_of_compartments):
                        value1: float = first + (size * val.range[0])
                        value2: float = first + (size * val.range[1])
                        tmp_array[itr].set_range((value1, value2))
                        # print('Value: {}, {} array val: {}, {}'.format(value1, value2, val.range[0], val.range[1]))
                print(tmp_array[0], tmp_array[-1])
                number = math.fsum([tmp_array[0].range[0], tmp_array[-1].range[1]]) / 2
                print(number)
                with open(output, "a+") as output_file:
                    output_file.write(f'{number} {len(elem)}#')
            with open(output, "a+") as output_file:
                output_file.write("\n")


def decode(file: str = "out_file.txt", output: str = "decodet_out_file.txt") -> None:
    # decoding
    array_of_compartment: List[Compartment]
    if os.path.exists(output): os.remove(output)
    with open(file, "r") as input_file:
        for index, line in enumerate(input_file.readlines()):
            print("{} {}".format(index, line))
            if index == 0:
                array_of_compartment = eval(line[:-1])
                continue
            for numbers in line.split("#"):
                if numbers == '\n':
                    continue
                point: float = float(numbers.split()[0])
                number: int = int(numbers.split()[1])
                tmp_array: List[Compartment] = copy.deepcopy(array_of_compartment)
                for i in range(number):
                    compartment = next(x for x in tmp_array if x.range[0] <= point <= x.range[1])
                    first = compartment.range[0]
                    last = compartment.range[1]
                    size = last - first
                    for itr, val in enumerate(array_of_compartment):
                        value1: float = first + (size * val.range[0])
                        value2: float = first + (size * val.range[1])
                        # print('Value: {}, {} array val: {}, {}'.format(value1, value2, val.range[0], val.range[1]))
                        tmp_array[itr].set_range((value1, value2))
                    with open(output, 'a+') as output_file:
                        output_file.write(compartment.letter)
                with open(output, 'a+') as output_file:
                    output_file.write(" ")
            with open(output, 'a+') as output_file:
                output_file.write('\n')


encode()

decode()
