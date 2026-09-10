#!/usr/bin/env python3
"""Gera métricas de tamanho e extensões do checkout local do Baluarte."""
from collections import defaultdict
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/ubuntu/Projeto-Baluarte")
by_ext = defaultdict(lambda: [0, 0])
by_top = defaultdict(lambda: [0, 0])
files = []
for path in root.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    size = path.stat().st_size
    rel = path.relative_to(root)
    ext = path.suffix.lower() or "[no-extension]"
    top = rel.parts[0] if rel.parts else "."
    by_ext[ext][0] += 1
    by_ext[ext][1] += size
    by_top[top][0] += 1
    by_top[top][1] += size
    files.append((size, str(rel)))

def mib(value):
    return value / 1024 / 1024

total = sum(size for size, _ in files)
print("# Baluarte storage audit")
print(f"checkout_bytes={total}")
print(f"checkout_mib={mib(total):.2f}")
print("\n## Top-level directories")
for name, (count, size) in sorted(by_top.items(), key=lambda item: item[1][1], reverse=True):
    print(f"{count:7} {mib(size):10.2f} MiB {name}")
print("\n## Extensions")
for ext, (count, size) in sorted(by_ext.items(), key=lambda item: item[1][1], reverse=True):
    print(f"{count:7} {mib(size):10.2f} MiB {ext}")
print("\n## Largest files")
for size, name in sorted(files, reverse=True)[:100]:
    print(f"{mib(size):10.2f} MiB {name}")
