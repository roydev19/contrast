import argparse
from .splitter import split_dir

def _cli():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out", default="vector/split.tsv")
    ns = ap.parse_args()
    split_dir(ns.src, ns.out)

if __name__ == "__main__":
    _cli()
