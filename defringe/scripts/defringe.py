from argparse import ArgumentParser

from defringe.defringe import do_defringe


def main():
    p = ArgumentParser()
    p.add_argument('-o', '--option', action='store_true', help='An option')

    args = p.parse_args()

    if args.option:
        print('OPTION!')
    else:
        print('NO OPTION!')


if __name__ == '__main__':
    main()
