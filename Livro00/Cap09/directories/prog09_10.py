#Programa 9.10 - Árvore de diretórios sendo percorrida
import os
import sys
for root, directories, files in os.walk(sys.argv[1]):
    print("\nCaminho:", root)
    for d in directories:
        print(f" {d}/")
    for f in files:
        print(f" {f}")
    print(f"{len(directories)} diretório(s), {len(files)} arquivo(s)")