import random

words = open('words/eng.txt').read().split('\n')
answer = open('answer').read()
file_count = 1999
wordlist = {}
for word in words:
	key = len(word)
	if key in wordlist.keys():
		wordlist[key].append(word)
	else:
		wordlist[key] = [word]

def make_math():
	operations = ['*', '**', '+', '-']
	out = ""
	k = 4
	while True:
		ops = random.choices(operations, k=k)
		if ops.count('**') == 1:
			break
	for i in range(k):
		out += str(random.randint(1, 9))
		out += ops[i]
	out += str(random.randint(1, 8))
	return out.replace('**','^'), eval(out)


def get_math():
	while True:
		expression, result = make_math()
		if result > 20 and result < 200:
			return expression, result

def find_words(limit):
	out = ""
	f = limit
	while f > max(wordlist.keys()):
		random_key = random.choices([k for k in wordlist.keys()], k=1)[0]
		random_word = random.choices(wordlist[random_key], k=1)[0]
		out += random_word.capitalize() + " "
		f = limit - len(out)
	out += random.choices(wordlist[f], k=1)[0].capitalize()
	return out



for i in range(file_count):
	exp, res = get_math()
	data = ""
	while True:
		try:
			data = find_words(res)
			break
		except Exception as e:
			pass
	print(exp, res, data)	
	open(f"files/{exp}", 'w').write(data)
open(f"files/3^9*3^8-2", 'w').write(answer)

