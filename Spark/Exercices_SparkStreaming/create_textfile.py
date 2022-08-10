import time
import random

def create_text():
    i = 1
    with open('fichier.txt', 'r') as file:
        lines = file.readlines()
        while i <= 30:
            totalline = len(lines)
            linenumber = random.randint(0, totalline -1)
            with open('./test/log{}.txt'.format(i), 'w') as writefile:
                writefile.write(' '.join(line for line in lines[linenumber:totalline]))
            print('creating file log{}.txt'.format(i))
            i += 1
            time.sleep(5)

if __name__ =='__main__':
  create_text()


