import os
import sys
from typing import List, Tuple

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


def genArray(alphabet="0123456789abcdefghijklmnopqrstwvuxyzABCDEFGHIJKLMNOPQRSTWVUXYZ,. \t\n", file="file.txt"):
    tmp_array_of_compartments: List[Compartment] = []

    for i, val in enumerate(alfarray(alphabet, file)):
        tmp_elem = 0.0 if i == 0 else tmp_array_of_compartments[i - 1].range[1]
        tmp_array_of_compartments.append(Compartment(
            (tmp_elem, tmp_elem + val[1]),
            val[0]
        ))

    print(tmp_array_of_compartments)
    return tmp_array_of_compartments


def encode(alphabet: str = "0123456789abcdefghijklmnopqrstwvuxyzABCDEFGHIJKLMNOPQRSTWVUXYZ,. \t\n",
           file: str = "file.txt", output: str = "out_file.txt") -> None:
    array_of_compartments = genArray(alphabet, file)
    if os.path.exists(output):
        os.remove(output)
    with open(file, "r") as input_file:
        for line in input_file.readlines():
            tmp_str = ''
            print(line)
            for elem in line.split():
                print(line.split())
                number = 0.0
                tmp_array = array_of_compartments
                for sign in elem:
                    compartment = next(x for x in tmp_array if x.letter == sign)
                    first = compartment.range[0]
                    last = compartment.range[1]
                    size = last - first
                    for itr, val in enumerate(array_of_compartments):
                        value1: float = tmp_array[itr - 1].range[1] if itr != 0 else first
                        value2: float = value1 + size * val.range[1] if itr != len(array_of_compartments) else last
                        tmp_array[itr].set_range((value1, value2))
                number = (tmp_array[0].range[0] + tmp_array[-1].range[1]) / 2
                with open(output, "a+") as output_file:
                    output_file.write(f'{number} {len(elem)}#')
            with open(output, "a+") as output_file:
                output_file.write("\n")


def decode(array_of_compartment,
           file: str = "file.txt", output: str = "out_file.txt") -> None:
    with open(file, "r") as input_file:
        for line in input_file.readlines():
            for numbers in line.split("#"):
                point, number = numbers.split()[0], numbers.split()[1]
                tmp_array = array_of_compartment
                for i in range(1, number):
                    tmp_array

    return None


encode()
