import pickle
import nltk
from nltk.corpus import brown, reuters

def compute_distribution():
	dist_n = nltk.FreqDist([w.lower() for w in brown.words() + reuters.words()])
	i = 0
	max_weight = 0.0
	for w in dist_n:
		i += 1
		if i == 31:
			max_weight = dist_n[w]
			break
	
	return dict((w, 1000.0 * min((1.0 * dist_n[w]) / max_weight, 1.0)) for w in dist_n)

def save_distribution(dist):
	with open('distribution.pickle', 'wb') as handle:
		pickle.dump(dist, handle)

def load_distribution():
	with open('distribution.pickle', 'rb') as handle:
		return pickle.load(handle)
