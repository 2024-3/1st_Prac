import sys

def croatia_alpa_count(word):
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for alpa in croatia:
        word = word.replace(alpa, ' ')

    print(len(word))


if __name__ == '__main__':
    word = str(sys.stdin.readline().strip())
    croatia_alpa_count(word)