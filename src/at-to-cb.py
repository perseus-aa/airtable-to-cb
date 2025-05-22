import argparse
from sys import stdout
from models import CBTable


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact_csv",
                        type=str,
                        help="artifact csv file from AirTable")

    parser.add_argument("image_csv",
                        type=str,
                        help="image csv file from AirTable")

    parser.add_argument("out",
                       type=str,
                       help="output file")



    args = parser.parse_args()
    cbtable = CBTable(args.artifact_csv, args.image_csv)
    cbtable.dump(args.out)
