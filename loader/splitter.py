from pathlib import Path
import re
import json
from typing import Iterable

CHUNK_SIZE = 1000  # characters
OVERLAP = 200


def _iter_source_files(src_dir: Path) -> Iterable[Path]:
    for p in src_dir.rglob("*"):
        if p.suffix.lower() in {".md", ".txt"} and p.is_file():
            yield p


def _clean_text(txt: str) -> str:
    # remove code-blocks & HTML tags (basic pass)
    txt = re.sub(r"```.*?```", "", txt, flags=re.S)   # code fences
    txt = re.sub(r"<[^>]+>", "", txt)                 # html
    return txt.strip()


def _chunk(text: str, size: int = CHUNK_SIZE, overlap: int = OVERLAP):
    i = 0
    while i < len(text):
        yield text[i : i + size]
        i += size - overlap


def split_dir(src_dir: str, out_path: str) -> None:
    src_dir = Path(src_dir)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as fp:
        for file_path in _iter_source_files(src_dir):
            raw = file_path.read_text(encoding="utf-8", errors="ignore")
            cleaned = _clean_text(raw)

            for idx, chunk in enumerate(_chunk(cleaned)):
                meta = {
                    "source": str(file_path.relative_to(src_dir)),
                    "chunk": idx,
                }

                clean_chunk = chunk.replace("\n", " ").replace("\t", " ")
                fp.write(f"{json.dumps(meta)}\t{clean_chunk}\n")

