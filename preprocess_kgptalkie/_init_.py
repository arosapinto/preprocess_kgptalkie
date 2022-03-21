from preprocess_kgptalkie import utils

__version__ = '0.0.1'

def get_wordcouts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get