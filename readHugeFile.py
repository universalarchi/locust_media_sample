import random

filesize = 17                 #size of the really big file
offset = random.randrange(filesize)

f = open('test.csv')
f.seek(offset)                  #go to random position
f.readline()                    # discard - bound to be partial line
random_line = f.readline()      # bingo!
print(random_line)
# extra to handle last/first line edge cases
if len(random_line) == 0:       # we have hit the end
    f.seek(0)
    random_line = f.readline()  # so we'll grab the first line instead
    print(random_line)
