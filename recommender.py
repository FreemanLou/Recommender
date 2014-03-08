import math

data = {"a": {"ts": 2, "mu":3},
	"b": {"ts": 1, "mu":4},
	"c": {"ts": 4, "mu":2},
	"d": {"ts": 2, "mu":5},
	"e": {"ts": 5, "mu":2},
	"f": {"ts": 3, "mu":5},
	"you": {"ts": 3, "mu":5}	
}

#Input: Ratings for user and another user
def getSimilarity(a, b):
	distance = 0
	for movie, rating in a.items():
		if (( movie in b.keys() and b.get(movie) != 0) and (rating != 0)):
			distance += math.pow( rating - b.get(movie), 2)
		else:
			continue
	return 1 / math.sqrt((distance + 1))
 
#Input: Dataset and username
def getMostSimilar(data, user):
	current = 0
	mostSimilar = ""
	for person, ratings in data.items():
		if (person != user):
			temp = getSimilarity(ratings, data.get(user))
			if (temp > current):
				current = temp
				mostSimilar = person
		else:
			continue

	return mostSimilar

print getMostSimilar(data, "you")
