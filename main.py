import argparse
from my_spellchecker import my_sp





if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--test', required = False, help = 'test help correct', action = argparse.BooleanOptionalAction)
    ap.add_argument('-msp', '--my_spellchecker', required = False, help = 'my implementation of spellchecker', action = argparse.BooleanOptionalAction)
    args = vars(ap.parse_args())

    if args['test']:
        print('test message')

    if args['my_spellchecker']:
        my_sp.get_words()
