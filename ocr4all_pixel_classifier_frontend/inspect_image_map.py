import argparse

from ocr4all.image_map import ImageMap


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('vars', metavar='IMAGEMAP', type=str, nargs='+',
                        help='image map json files')
    opt_args = parser.add_argument_group("optional arguments")
    opt_args.add_argument("-h", "--help", action="help", help="show this help message and exit")
    args = parser.parse_args()

    for imap in args.vars:
        map = ImageMap.load(imap)
        for k, v in map.mapping.items():
            print(f"\x1b[48;2;{k[0]};{k[1]};{k[2]}m    \x1b[0m  \x1b[38;2;{k[0]};{k[1]};{k[2]}m{v}\x1b[0m\n")


if __name__ == '__main__':
    main()
