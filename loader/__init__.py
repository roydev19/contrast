from pathlib import Path
import argparse

from .splitter import split_dir


def _cli():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")                       # docs_raw/
    ap.add_argument("--out", default="vector")   # folder, not file
    ns = ap.parse_args()

    split_tsv = Path(ns.out) / "split.tsv"
    embed_jsonl = Path(ns.out) / "mini.jsonl"

    split_dir(ns.src, split_tsv)
    from .embed import embed_chunks
    embed_chunks(split_tsv, embed_jsonl)

    print(f"✓ Chunks: {split_tsv}  |  ✓ Vectors: {embed_jsonl}")


if __name__ == "__main__":
    _cli()
