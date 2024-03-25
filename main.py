import argparse
from my_spellchecker import my_sp
from good_spellchecker import g_sp
from best_spellchecker import b_sp



if __name__ == '__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--test', required = False, help = 'test help correct', action = argparse.BooleanOptionalAction)
    ap.add_argument('-msp', '--my_spellchecker', required = False, help = 'my implementation of spellchecker', action = argparse.BooleanOptionalAction)
    ap.add_argument('-gsp', '--good_spellchecker', required = False, help = 'good implementation of spellchecker', action = argparse.BooleanOptionalAction)
    ap.add_argument('-bsp', '--best_spellchecker', required = False, help = 'best implementation of spellchecker', action = argparse.BooleanOptionalAction)
    args = vars(ap.parse_args())
    
    if args['test']:
        print('test message')

    if args['my_spellchecker']:
        my_sp.get_words()
       
    if args['good_spellchecker']:
        g_sp.get_words()

    if args['best_spellchecker']:
        model = b_sp.load_model()
        model.get_answer()
