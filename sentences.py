#!/usr/bin/python
import re
import sys

def find_sentences(text):
	return map(lambda sentence: sentence.strip(), re.split('\n|\.\s', text))

def get_length(sentence):
	return len(sentence.split(' '))

def get_stats(sentences):
	return map(lambda sentence: (sentence, get_length(sentence)), sentences)

def filter_by_length(tuples, min_length):
	return filter(lambda tuple: tuple[1] >= min_length, tuples)

def to_str(tuples):
	return map(lambda tuple: str(tuple[1]) + ': ' + tuple[0], tuples)

def sort(tuples):
	return sorted(tuples, key=lambda tuple: -1*tuple[1])

def open_file(name):
	f = open(name, 'r');
	return f.read()

def main():
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		s = find_sentences(open_file(filename))

		#s = find_sentences('Test sentence. This is another test sentence. This tests, e.g., abbreviations.\n\nThis is the last one. No, actually this is the last one.')
		print('\n'.join(to_str(sort(filter_by_length(get_stats(s), 20)))))
	else:
		print('Usage: python sentences.py filename')
		raise ValueError('No filename specified')

main()