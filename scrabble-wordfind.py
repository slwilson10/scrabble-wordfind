##
## Scrabble Word Find
##

## Open and view wordlist
import string

WORDLIST_FILENAME = "words.txt"
wordlist = []

def load_words():
    ## Returns a list of valid words. Words are strings of lowercase letters.
    print ("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    for w in inFile:
        word = (w.rstrip())
        wordlist.append(word)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

## Get letters from player
def get_letters():
	letters = []
	letter = str(input('Enter your letters --> '))
	## Only 7 tiles allowed in a hand
	if len(letter) > 7:
		print ('You entered too many letters.')
		get_letters()
	else:
		for i in letter:
			letters.append(i)
	return letters

def get_board_letter():
	i = False
	while i == False:
		letter = str(input('Enter your board letter --> '))
		if len(letter) > 1:
			print ('You entered too many letters.')
			i = False
		else:
			i = True

	print ('ending loop')
	return letter




## Check if letters are equal
def check_letters(l1, l2):
	if l1 == l2:
		return True
	else:
		return False

## See if there are duplicate letters in given letters
def get_duplicate_in_letters(letters):
	pos = 0
	loop = 0
	dupes = []
	## Only loop through as many letters that are in the word
	## Might be able to replace with "for" loop
	while loop < len(letters):
		count  =0
		l1 = letters[pos]
		## Match each letter in the word one-by-one with each other letter in the word
		for l2 in letters:
			if check_letters(l1,l2):
				count = count + 1
			else: pass
		## If the letter matches with any other than itself
		if count >= 2:
			## And it not already in dupes list
			if (l1, count) not in dupes:
				## Add tuple of letter and its amount
				dupes.append((l1, count))
			else: pass
		else: pass
		## After one letter has gone through each, start at the beg with new letter
		if pos +1 >= len(letters):
			pos = 0
		else:
			pos = pos +1
		loop = loop +1
	return dupes

## Find words that match the length given 
def find_words(wordlist, length):
	new_wordlist = []
	for i in wordlist:
		if len(i) == length:
			new_wordlist.append(i)
		else: pass
	return new_wordlist 

## Filters word that contain a letter given
def add_matching_words(letters, new_wordlist):
	match_list = []
	for i in new_wordlist:
		split = list(i)
		for t in split:
			if t in letters:
				if i not in match_list:
					match_list.append(i)
				else: pass
			else: pass
	return match_list

## Filters words that have letters that do not match letters that were given
def remove_mismatch_words(letters, i, length):
	count = 0
	split = list(i)
	for t in split:
		if t in letters:
			count = count + 1
		else: pass
	if count == length:
		return False
	else: return True

## Filters words that have duplicate letters that dont match letters given 
def check_dupe_in_words(i, dupes):
	pos = 0
	loop = 0
	new_dupes = []
	split = list(i)
	## Only loop through as many letters that are in the word
	## Might be able to replace with "for" loop
	while loop < len(i):
		count  =0
		l1 = split[pos]
		## Match each letter in the word one-by-one with each other letter in the word
		for l2 in split:
			if check_letters(l1,l2):
				count = count + 1
			else: pass
		## If the letter matches with any other than itself
		if count >= 2:
			if (l1, count) not in new_dupes:
				new_dupes.append((l1, count))
			else: pass
		else: pass
		if pos +1 >= len(i):
			pos = 0
		else:
			pos = pos +1
		loop = loop +1
	for a in new_dupes:
		if a not in dupes:
			return True
		else: return False 

## Large function that runs smaller functions
def filter_words(wordlist, length, letters, dupes):
	new_wordlist = find_words(wordlist, length)
	new_wordlist = add_matching_words(letters, new_wordlist)
	## Loops through all words in match_list
	for i in new_wordlist[0:]:
		## If a letter was found in a word that was not given or non-matching dupe letters:
		if remove_mismatch_words(letters, i, length) or check_dupe_in_words(i, dupes): 
			## Remove it
		 	new_wordlist.remove(i)
		else: pass
	return new_wordlist

## Main Loop
def main():
	wordlist = load_words()
	letters = get_letters()
	board_letter = get_board_letter()
	print (board_letter)
	if len(board_letter) != 0:
		letters.append(board_letter)
	print ('Your letters are -->  %s ' % (letters))
	dupes = get_duplicate_in_letters(letters)
	length = 2
	## Run loop for each possible length of words
	while length <= 8:
		final_wordlist = filter_words(wordlist, length, letters, dupes)
		if len(final_wordlist) > 0:
			print ('Words with length of: %d' % length)
			print (final_wordlist)
		else: pass
		length = length + 1


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

## Account for tile that might be on the board