# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:02:32 2015

@author: kozl
"""
import numpy as np
import sys


def calculate_distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5


def create_distance_matrix(points):
    """ Create matrix NxN with distances between points """
    N = len(points)
    distance_matrix = np.zeros((N, N), dtype=np.float_)
    for i in range(0, N-1):
        for k in xrange(i+1, N):
            distance_matrix[i, k] = distance_matrix[k, i] = calculate_distance(points[i], points[k])
    return distance_matrix


def get_neighbours(distance_vector, R=0):
    """ Find R - distance to nearest point and neighbours - points, closer than 2R """
    i = 0
    while R == 0:  # choose the first value as R, bit not 0
        R = distance_vector[i]
        i+=1
    neighbours = []
    for L in distance_vector[i:]:
        if R <= L:  # find neighbours according to current R value
            if R*2 >= L:
                neighbours.append(L)
        # but if we find lower L, than it will be our new R
        elif R <= L*2:  # if L < R <= L*2 than we should check all neighbours that was found earlier
            neighbours = get_neighbours(neighbours, L)[1]
            neighbours.append(R)
            R = L
        elif L != 0:
            neighbours = []  # else we forget about them
            R = L
    return R, neighbours


if __name__ == '__main__':
    points = []
    for line in sys.stdin:
        s = line.rstrip().rsplit(' ')
        if s != ['']:
            points.append((int(s[0]), int(s[1])))
    for line in create_distance_matrix(points):
        R, n = get_neighbours(line)
        print 'R = {0}, neighbours = {1}'.format(R, len(n) + 1)  # +1 - our nearest point is also a neighbour
