"""Verify archived bytes only; never run training or inference."""
from pathlib import Path
import gzip
import hashlib
import json

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'MANIFEST.json').read_text())
for item in manifest['files']:
    stored = (root / item['path']).read_bytes()
    assert hashlib.sha256(stored).hexdigest() == item['stored_sha256'], item['path']
    if item.get('sanitized'):
        continue  # stored bytes differ from the source by a path-prefix replacement; stored hash checked above
    original = gzip.decompress(stored) if item['encoding'] == 'gzip' else stored
    assert hashlib.sha256(original).hexdigest() == item['source_sha256'], item['path']
    assert len(original) == item['source_bytes'], item['path']
assert json.loads((root / 'VALIDATION.json').read_text())['all_48_match']
print(f"Verified {len(manifest['files'])} archived files; no inference executed.")
