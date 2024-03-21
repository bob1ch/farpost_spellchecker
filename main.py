import argparse






if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--test', required = False, help = 'test help correct', action = argparse.BooleanOptionalAction)
    args = vars(ap.parse_args())

    if args['test']:
        print('test message')
