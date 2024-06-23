from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def string_to_gene(s:str) ->Gene:
    gene: Gene =[]
    for i in range(0, len(s), 3):
        if (i+2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene

my_gene: Gene = string_to_gene(gene_str)

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.B, Nucleotide.C)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene)
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mind + 1
        elif gene[mid] > key_codon:
            high = mid -1
        else:
            return True
    return False

my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))

from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callble, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop
T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq_(self, other: Any): -> bool:

    def __lt__(self, other: C) -> bool:

    def __gt__(self: C, other:C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other

    def binary_contains(sequence: Sequence[C], key: C) -> bool:
        low: int = 0
        high: int = len(sequence) - 1
        while low <= high:
            mid: int = (low + high)//2
            if sequence[mid] < key:
                low = mid + 1
            elif sequence[mid] > key:
                high = mid - 1
            else:
                return True
        return False

if __name__ == "__main__":
    print(linear_contain([1, 5, 15, 15, 15, 20], 5))
    print(binary_contains(["a", "d", "e", "f", "z"], "f"))
    print(binary_contains(["jonh", "mark", "ronald", "sarah"], "sheila"))



