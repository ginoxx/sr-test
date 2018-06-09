
#! python

# work out: 5t + 7c + 3p/g = score

###################################################################
import sys


def findScore(score):

	# setup
	max_tries = int(score)//5
	max_convs = int(score)//7
	max_penalties = int(score)//3

	combs =[]

	for i in range(max_penalties+1):
		if i == 0:
			t = 0
			c = 0
			if 3*int(i) + 5*int(t) + 7*int(c) == int(score) and score > 0:
				found_comb = 'Tries+Conv: %d - Tries: %d - Penalties/Drop Goals): %d' % (c, i, t)
				combs.append(found_comb)

		for t in range(max_tries+1):
			if i == 0 and t == 0:
				c = 0
				if 3*int(i) + 5*int(t) + 7*int(c) == int(score) and score > 0:
					found_comb = 'Tries+Conv: %d - Tries: %d - Penalties/Drop Goals): %d' % (c, i, t)
					combs.append(found_comb)

			for c in range (max_convs+1):
				# print 'converted tries', s      # Only needed for spotting errors
				if 3*int(i) + 5*int(t) + 7*int(c) == int(score) and score > 0:
					found_comb = 'Tries+Conv: %d - Tries: %d - Penalties/Drop Goals): %d' % (c, i, t)
					combs.append(found_comb)

	return combs

#  START
if len(sys.argv)<2:
	print('Please enter score')
	sys.exit()

score = sys.argv[1]

print '-----------'
combs = findScore(score)

if len(combs)==0:
	print "This score is not possible"
else:
	print 'There are %d ways to score %d' % (len(combs),int(score))
	for w in range(len(combs)):
		print combs[w]
