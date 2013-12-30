import re
import math

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
	words = get_words_unique(text)
	for w in words:
		s += (dist.get(w) or 0.0)
	return s / len(words)


# distribution ranking function
# text: raw text to rank
# dist: language distribution
# threshold: how many words from the text are considered
def rank_distribution(text, dist, threshold):
	words = [(dist.get(w) or 0.0) for w in get_words(text)]
	words.sort(reverse=True)
	return words[int(math.ceil(threshold * (len(words) - 1)))]


# rank an article
# text: article text
# dist: language distribution
def rank_article(text, dist):
	return rank_distribution(text, dist, 0.90)
	#return rank_average(text, dist)
