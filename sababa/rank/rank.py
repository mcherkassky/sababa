import re
import json

# default ranking function
# text: raw text to rank
# dist: language distribution
def rank_average(text, dist):
	s = 0.0
	words = [w.lower() for w in re.findall(r"[\w']+", text)]
	unique_words = set()
	for w in words:
		if w in unique_words:
			continue
		else:
			unique_words.add(w)
			s += (dist.get(w) or 0.0)
	return s / len(unique_words)

# rank an article
# art: article in JSON format
# dist: language distribution
def rank_article(art, dist):
	return rank_average(art["text"], dist)