import argparse, os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset1', type=str, help="path to Datasets")
    parser.add_argument('dataset2', nargs='+', type=str, help="path to Dataset 2 or how many they are")
    parser.add_argument('outpath', type=str, help="path to where merged data will be stored")
    args = parser.parse_args()
    return args


def validate_paths(*args):
    return True


def merge(dataset1, dataset2, outpath, label='0'):
    pass


def checklabels(dataset1, dataset2):
    return '0'


def main(args):

    dataset1 = args.dataset1
    datasets = set(args.dataset2)
    outpath = args.outpath
    
    if not validate_paths(dataset1, *datasets, outpath):
        return False

    print(
        "Path to Dataset 1:", dataset1,
        *[f"\nPath to Dataset {i}: {path}" for i,path in zip(range(2, len(datasets)+2), datasets)],
        "\nPath to output merged folder:", outpath
    )

    for dataset2 in datasets:
        label = checklabels(dataset1, dataset2)
        merge(dataset1, dataset2, outpath, label=label)
        dataset1 = outpath
        
    x = input() # to halt it



if __name__ == "__main__":
    args = parse_args()
    main(args)