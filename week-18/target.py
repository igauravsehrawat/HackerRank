#!/bin/python

# target
import math

def hypotenuse(base, height) :
	# x is base, y is height
	return math.sqrt(math.pow(base, 2) + math.pow(height, 2))

def find_possible_index(number, array_to_search) :
	try :
		got_index = array_to_search.index(number)
		return got_index
	except :
		return find_possible_index(number + 1, array_to_search)

def main() :
	k_radiuses, n_points = raw_input().strip().split(' ')
	k_radiuses, n_points = [int(k_radiuses), int(n_points)]
	k_radiuses_array = map(int,raw_input().strip().split(' '))
	hypotenuses = []
	for every_point in xrange(n_points) :
		coordinates = map(int,raw_input().strip().split(' '))
		hypotenuse_distance = hypotenuse(coordinates[0], coordinates[1])
		hypotenuses.append(hypotenuse_distance)
	hypotenuses.sort()

	radius_score_map = {}
	for each_radius in k_radiuses_array :
		radius_score_map[each_radius] = k_radiuses_array.index(each_radius) + 1

	hypotenuse_iterator = iter(hypotenuses)
	radius_iterator = iter(k_radiuses_array)
	last_success_radius = next(radius_iterator)
	next_radius = 0
	score = 0
	
	for each_hypotenuse in hypotenuses :
		if (radius_score_map.has(int(math.ceil(each_hypotenuse)))) :
			score += radius_score_map(int(math.ceil(each_hypotenuse)))
		else :
			get_index = find_possible_index(int(math.ceil(each_hypotenuse)), k_radiuses_array)
			score += radius_score_map(get_index)

	print score