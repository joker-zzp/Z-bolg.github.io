# /usr/bin/python3
# -*- encoding: utf-8 -*-
#
# @filename      : hello.py
# @author        : joker-zzp
# @created       : Mon Mar 18 2019 13:13:18 GMT+0800 (中国标准时间)
# @last-modified : Tue Mar 26 2019 21:36:22 GMT+0800 (中国标准时间)
# @description   : test
#


class Sudoku_Puzzle:
    # 数独的二维数组
    sudoku_list = []
    # 猜测数据字典
    # {'result': 3, 'number': 2, 'x': 0, 'y': 0, 'calc':[], 'guess_num':}
    guess_dictionary = [{
        'result': 8,
        'number': 2,
        'position': [{'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}],
        'calc': [],
        'guess_num': []
    }]

    def __init__(self):
        pass

    def init_sudoku_list(self):
        if self.sudoku_list:
            return self.sudoku_list
        else:
            self.sudoku_list = [[i + 1 for i in range(9)] for j in range(9)]
            return self.sudoku_list

    def init_guess_dictionary(self):
        if self.guess_dictionary:
            for i in range(len(self.guess_dictionary)):
                # self.guess_dictionary['result'] = self.guess_dictionary[i]
                print(self.guess_dictionary[i])
            return self.guess_dictionary
        else:
            return "无猜测结果"

    def __probably(self):
        guess_maybe = []
        while True:
            guess_maybe.append([i + 1 for i in range(9)])
            tmp = [i + 1 for i in range(9)]
            print(tmp)
            break
        return guess_maybe

    def print(self):
        for i in range(len(self.sudoku_list)):
            print(self.sudoku_list[i])


test = Sudoku_Puzzle()
# test.sudoku_list = [1, 2, 3, 4, 5]
# test.guess_dictionary = [3, 3, 4, 5, 14]
test.init_sudoku_list()
test.init_guess_dictionary()
# print(test.guess_dictionary)
test.print()
print(test.sudoku_list[0][0])
print("数独test")
