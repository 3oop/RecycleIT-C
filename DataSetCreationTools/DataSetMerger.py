import argparse, os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset1', type=str, help="path to Datasets")
    parser.add_argument('dataset2', nargs='+', type=str, help="path to Dataset 2 or how many they are")
    parser.add_argument('outpath', type=str, help="path to where merged data will be stored")
    args = parser.parse_args()
    return args


def validate_paths(args):
    if not os.path.exists(args.dataset1) or not os.path.isdir(args.dataset1):
        print(f"Path for Dataset 1: \n\t {args.dataset1} \n does not exist or this path is not a directory")
        # return False

    for path in args.dataset2:
        if not os.path.exists(path) or not os.path.isdir(args.dataset1):
            print(f"This path does not exist or is not a directory: \n\t {path}")
            # return False
    
    if args.outpath in args.dataset2 or args.outpath == args.dataset1:
        print("Output Directory path cannot be the same as other datasets or ...??")

    try:
        os.chdir(args.outpath)
    except (FileNotFoundError, NotADirectoryError, PermissionError):
        os.mkdir(args.outpath)
    finally:
        if os.listdir != []:
            print(f"The Output directory path is not Empty! \n\t {args.outpath}")
            # return False



def merge(dataset1, dataset2, outpath, label='0'):
    pass


def checklabels(dataset1, dataset2):
    return '0'


def main(args):

    dataset1 = args.dataset1
    datasets = [path for path in args.dataset2 if path not in datasets]
    args.dataset2 = datasets
    outpath = args.outpath

    if not validate_paths(args):
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