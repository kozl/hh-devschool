# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:21:47 2015

@author: kozl
"""
import sys


def convert_to_base(num, base):
    res = ''
    if num < base:
        res = str(num) if num < 10 else chr(num + 55)  # if base > 10 use alphabet
        return res
    q = num
    while q != 0:
        q, r = divmod(q, base)
        res = str(r) + res if r < 10 else chr(r + 55) + res
    return res


def divide(a, b, base):
    """ Convert a/b to the number in another base. If there is a periodical fractal part, then write it in brackets"""
    q, r = divmod(a, b)
    integer_part = convert_to_base(q, base)  # if there is a integer part
    finished = False
    frac_part = ''
    r_list = []  # r_list stores all remainders, needed to helps us to find a periodical part
    while not finished:
        r_list.append(r)
        r *= base
        while r <= b:
            frac_part += '0'
            r_list.append(r)
            r *= base
        q, r = divmod(r, b)
        frac_part += convert_to_base(q, base)
        if r == 0:
            res = integer_part + '.' + frac_part            
            finished = True
        elif r in r_list:  # in case of periodical fraction
            res = integer_part + '.' + frac_part[:r_list.index(r)] + '(' + frac_part[r_list.index(r):] + ')'
            finished = True
    return res

if __name__ == '__main__':
    for line in sys.stdin:
        s = line.rstrip().rsplit(' ')
        if s != ['']:
            print divide(int(s[0]), int(s[1]), int(s[2]))
