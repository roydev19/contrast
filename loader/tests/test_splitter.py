from pathlib import Path
from loader.splitter import split_dir

def test_chunking(tmp_path: Path):
    dr = tmp_path / "docs"
    dr.mkdir()
    (dr / "a.txt").write_text("hello " * 300)     # ~1500 chars
    out = tmp_path / "out.tsv"
    split_dir(dr, out)
    lines = out.read_text().splitlines()
    assert len(lines) == 2                        # chunk + overlap maths
    meta0, text0 = lines[0].split("\t", 1)
    assert "a.txt" in meta0 and text0.startswith("hello")
