from pathlib import Path
from loader.splitter import split_dir
from loader.embed import embed_chunks
import json

def test_embed(tmp_path: Path):
    docs = tmp_path / "docs"; docs.mkdir()
    (docs / "a.md").write_text("hello world " * 100)
    split_tsv = tmp_path / "split.tsv"
    split_dir(docs, split_tsv)

    out_jsonl = tmp_path / "vec.jsonl"
    embed_chunks(split_tsv, out_jsonl)

    rec = json.loads(out_jsonl.read_text().splitlines()[0])
    assert len(rec["embedding"]) == 384
    assert "hello" in rec["text"]
