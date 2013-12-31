import re
import math
import random

sentence_regexp = re.compile('[.!?]')

# get words from text
def get_words(text):
    words =  [w for w in re.findall(r"[\w']+", text) if re.match("[a-z'-]+", w)]
    return [word for word in words if len(word) > 3]


# get unique words from text
def get_words_unique(text):
	return set(get_words(text))


# get sentences from text containing words
def get_sentences(text, words):
	sentences = [s + '.' for s in sentence_regexp.split(text)]
	result = dict.fromkeys(words)
	for word in words:
		for s in sentences:
			if word in get_words_unique(s):
				result[word] = s
				break
	return result


# distribution ranking function
# text: raw text to rank
# dist: language distribution
# threshold: how many words from the text are considered
def rank_distribution(text, dist, threshold):
	words = [(w, dist.get(w) or 0.0) for w in get_words(text)]
	words = sorted(words, reverse=True, key = lambda t: t[1])
	if(words is None or len(words) == 0):
		return (0.0, [])
	
	unique_words = sorted(set(words), reverse=True, key = lambda t: t[1])
	score = words[int(math.ceil(threshold * (len(words) - 1)))]
	n = int(float(len(unique_words)) / 20.0)
	i = unique_words.index(score)
	min_i = max(0, i-2)
	max_i = min(len(unique_words) - 1, i + n)
	hard_words = unique_words[min_i:max_i]
	random_words = [w[0] for w in random.sample(hard_words, min(n, len(hard_words)))]
	print(random_words)
	return (score, get_sentences(text, random_words))


# rank an article
# text: article text
# dist: language distribution
def rank_article(text, dist):
	return rank_distribution(text, dist, 0.85)
