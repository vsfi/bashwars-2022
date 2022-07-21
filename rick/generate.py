import ffmpeg
import random
import concurrent.futures
import string
import pathlib
from leet import leet

ANSWER = open('task','r').read()

templates = ['eminem.txt','metallica.txt','rihanna.txt','wintersun.txt','jayz.txt']
wrong_lines = []
for t in templates:
    wrong_lines += open(f"lyrics/{t}", 'r').read().strip().split('\n')
words = open('words/eng.txt','r').read().split('\n')
r_words = open('lyrics/rick.txt','r').read().split('\n')

RANGE = 300
WORKERS = 30
MP3 = 'initial_mp3_file.mp3'

def ffmpegify(output, metadata, stdout=False):
    stream = ffmpeg.input(MP3)
    stream = ffmpeg.output(stream, output, metadata=metadata)
    stream = ffmpeg.overwrite_output(stream)
    ffmpeg.run(stream, capture_stdout=stdout, capture_stderr=True)
    return output, metadata

def rand_dir(n=3):
    return '/'.join(random.choices([f for f in string.hexdigits], k=n))

with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
    future_ffmpegify = []
    for i in range(RANGE):
        new_dir = rand_dir()
        pathlib.Path(f'audio/{new_dir}').mkdir(parents=True, exist_ok=True)
        word = leet(random.choices(words, k=1)[0])
        line = random.choices(wrong_lines, k=1)[0]
        future_ffmpegify.append(executor.submit(ffmpegify, f'audio/{new_dir}/{word}.mp3', f'lyrics={line}'))
    for r in concurrent.futures.as_completed(future_ffmpegify):
        print(r.result())
    
    future_ffmpegify = []

    for i, word in enumerate(ANSWER.split('_')):
        new_dir = rand_dir()
        pathlib.Path(f'audio/{new_dir}').mkdir(parents=True, exist_ok=True)
        future_ffmpegify.append(executor.submit(ffmpegify, f'audio/{new_dir}/{word}.mp3', f'lyrics={r_words[i]}'))
    for r in concurrent.futures.as_completed(future_ffmpegify):
        print(r.result())
