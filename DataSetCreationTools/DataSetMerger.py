import argparse, os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset1', type=str, help="path to Datasets")
    parser.add_argument('dataset2', nargs='+', type=str, help="path to Dataset 2 or how many they are")
    parser.add_argument('outpath', type=str, help="path to where merged data will be stored")
    args = parser.parse_args()
    return args

def main(args):
    print(
        "Path to Dataset 1:", args.dataset1,
        *[f"\nPath to Dataset {i}: {path}" for path,i in zip(args.dataset2, range(2,len(args.dataset2)+2))],
        "\nPath to output merged folder:", args.outpath
    )
    while 1:
        print(args)


if __name__ == "__main__":
    args = parse_args()
    main(args)