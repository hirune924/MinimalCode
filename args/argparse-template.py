# -*- encoding: utf-8 -*-
import argparse

def main(args):
    print('required_key: {}'.format(args.required_key))
    print('s_key: {}'.format(args.s_key))
    print('i_key: {}'.format(args.i_key))
    print('f_key: {}'.format(args.f_key))

    print('b_key: {}'.format(args.b_key))

    print('enum_key: {}'.format(args.enum_key))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='description for this program.', add_help=True)

    # required argument
    parser.add_argument('required_key', help='help message for this argument.')
    # option argument
    parser.add_argument('-o', '--option_key', help='help message for this argument.')

    # str, int, float
    parser.add_argument('-s', '--s_key', help='help message for this argument.',
                        type=str, required=False, default='default string')
    parser.add_argument('-i', '--i_key', help='help message for this argument.',
                        type=int, required=True)
    parser.add_argument('-f', '--f_key', help='help message for this argument.',
                        type=float, required=True)

    # bool
    parser.add_argument('-b', '--b_key', help='help message for this argument.', 
                        action='store_true')

    # enum
    parser.add_argument('-e', '--enum_key', help='help message for this argument.',
                       type=str, choices=['x', 'y', 'z'], required=False, default='x')

    args = parser.parse_args()
    main(args)
