import random
import hashlib
from pathlib import Path

words = open('words/eng.txt').read().split('\n')
answer = open('answer').read()
file_count = 3999


def md5(data):
	return hashlib.md5(data.encode()).hexdigest()

def create(line):
	hashed_line = md5(line)
	# print(line, [h for h in hashed_line])
	path = '/'.join([h for h in hashed_line])
	Path(f"files/{path}").mkdir(parents=True, exist_ok=True)
	open(f"files/{path}/file",'w').write(line)

for i in range(file_count):
	line = ' '.join([w.capitalize() for w in random.choices(words, k=random.randint(3, 10))])
	create(line)

create(answer)
