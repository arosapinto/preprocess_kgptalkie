from preprocess_kgptalkie import utils

__version__ = '0.0.2'

def get_wordcouts(x):
	return utils._get_wordcounts(x)

def get_charcounts(x):
	return utils._get_charcounts(x)

def get_avg_wordlength(x):
	return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):
	return utils._get_stopwords_counts(x)

def get_hastag_counts(x):
	return utils._get_hastag_counts(x)

def get_mentions_counts(x):
	return utils._get_mentions_counts(x)

def get_digit_counts(x):
	return utils._get_digit_counts(x)

def get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)

def count_exp(x):
	return utils._count_exp(x)

def get_emails(x):
	return utils._get_emails(x)

def get_remove_emails(x):
	return utils._get_remove_emails(x)

def get_urls(x):
	return utils._get_urls(x)

def get_remove_urls(x):
	return utils._get_remove_urls(x)

def get_remove_rt(x):
	return utils._get_remove_rt(x)

def get_remove_special_chars(x):
	return utils._get_remove_special_chars(x)

def get_remove_html_tags(x):
	return utils._get_remove_html_tags(x)

def get_remove_accent(x):
	return utils._get_remove_accent(x)

def get_remove_stopwords(x):
	return utils._get_remove_stopwords(x)

def make_to_base(x):
	return utils._make_to_base(x)
    
def get_value_counts(df, col):
    return utils._get_value_counts(df, col)

def remove_common_words(x, freq, n=20):
	return utils._remove_common_words(x, freq, n)

def remove_rarewords(x, freq, n=20):
	return utils._remove_rarewords(x, freq, n)

def spelling_correction(x):
	return utils._spelling_correction(x)
