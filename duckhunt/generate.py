import random
import hashlib
from pathlib import Path

words = open('words/eng.txt').read().split('\n')
answer = open('answer').read()
file_count = 9999
answer_num = 1337


def md5(data):
	return hashlib.md5(data.encode()).hexdigest()

Path(f"files").mkdir(parents=True, exist_ok=True)

data = []
for i in range(file_count):
	if i == answer_num-1:
		data.append(answer)
	line = ' '.join([w.capitalize() for w in random.choices(words, k=random.randint(3, 10))])
	data.append(line)

open("files/flag",'w').write('\n'.join(data))

