import re
import math
import random

# get words from text
def get_words(text):
	return [w.lower() for w in re.findall(r"[\w']+", text)]


# get unique words from text
def get_words_unique(text):
	return set(get_words(text))


# default ranking function
# text: raw text to rank
# dist: language distribution
def rank_average(text, dist):
	s = 0.0
	words = [(w, dist.get(w) or 0.0) for w in get_words_unique(text)]
	words = sorted(words, reverse=True, key = lambda t: t[1])
	for w in words:
		s += (dist.get(w[0]) or 0.0)
	s = s / len(words)
	return s


# distribution ranking function
# text: raw text to rank
# dist: language distribution
# threshold: how many words from the text are considered
def rank_distribution(text, dist, threshold):
	words = [(w, dist.get(w) or 0.0) for w in get_words(text)]
	words = sorted(words, reverse=True, key = lambda t: t[1])
	i = int(math.ceil(threshold * (len(words) - 1)))
	score = words[i]
	max_n = 100
	n = 10
	min_i = max(0, i-2)
	max_i = min(len(words) - 1, i + n)
	hard_words = words[min_i:max_i]
	random_words = random.sample(hard_words, min(n, len(hard_words)))
	return (score, random_words)


# rank an article
# text: article text
# dist: language distribution
def rank_article(text, dist):
	return rank_distribution(text, dist, 0.85)
