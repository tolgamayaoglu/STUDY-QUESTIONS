## Duplicates

def has_any_duplicates(l):
	seen_elements = {}
	for elem in l:
		if elem in seen_elements:
			return True
		else:
			seen_elements[elem] = 1
	return False

print("DUPLICATES")
print(has_any_duplicates([1,2,3,4,5,6,7]))
print(has_any_duplicates([1,2,3,4,5,6,7,1]))
print(has_any_duplicates([1,2,2,22,3,4,5,6,7]))



# I think you can assume no duplicate elements in the lists
def random_question_sol1(l1, l2):
	# this is the first and worst solution :)
	count = 0
	for elem1 in l1:
		for elem2 in l2:
			if elem1 == elem2:
				count += 1
				break
	return count

print("RANDOM QUESTION SOLUTION 1")
print(random_question_sol1([1,2,3,4,5],[3,4,5,6,7,8]))
print(random_question_sol1([1,2,3,4,5],[1,2,3,4,5,6,7,8]))
print(random_question_sol1([1,2,3,4,5],[6,7,8]))

# I think you can assume no duplicate elements in the lists
def random_question_sol2(l1, l2):
	# this is better with extra storage
	elements_of_l2 = {} # instead of dictionary, you can directly use set, it has a constant access too.
	for elem2 in l2:
		elements_of_l2[elem2] = 1
	count = 0
	for elem1 in l1:
		if elem1 in elements_of_l2: # THIS IS IMPORTANT, IT PROVIDES CONSTANT ACCESS and SEARCH
			count += 1
	return count

print("RANDOM QUESTION SOLUTION 2")
print(random_question_sol2([1,2,3,4,5],[3,4,5,6,7,8]))
print(random_question_sol2([1,2,3,4,5],[1,2,3,4,5,6,7,8]))
print(random_question_sol2([1,2,3,4,5],[6,7,8]))


