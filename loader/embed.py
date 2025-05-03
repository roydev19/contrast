# loader/embed.py
from pathlib import Path
from typing import List, Dict
import json
from sentence_transformers import SentenceTransformer

_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"   # 384-dim
_model: SentenceTransformer | None = None


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(_MODEL_NAME)
    return _model


def embed_chunks(tsv_path: Path, out_path: Path) -> None:
    """
    Read TSV (“meta<TAB>text”) from splitter, write JSONL with embedding vector.
    """
    model = _get_model()
    out_path.parent.mkdir(exist_ok=True, parents=True)

    with tsv_path.open() as inp, out_path.open("w") as out:
        for line in inp:
            meta_str, text = line.rstrip("\n").split("\t", 1)
            meta: Dict = json.loads(meta_str)
            emb: List[float] = model.encode(text).tolist()   # numpy -> python list
            rec = {"text": text, "meta": meta, "embedding": emb}
            out.write(json.dumps(rec) + "\n")
