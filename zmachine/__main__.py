import sys
from zmachine import zmachine
from voice import voice

def main():
    game = zmachine(sys.argv[1])
    voice(game)

if __name__ == '__main__':
    main()
