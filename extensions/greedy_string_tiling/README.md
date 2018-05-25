# Greedy String Tiling

This Python package implements a C++ extension of the Greedy String Tiling algorithm [1], which can be used for source code similarity detection as has been done with the JPlag system [2].
When used using the provided wrapper/adapter `matcher.jplag_ext.match`, it can be expected to behave exactly as the pure Python implementation `matcher.jplag.match`, except faster.

## Installing

Activate the virtual environment used by Radar and run the below command to build and install the extension:

```pip install -e .```

To make sure everything works correctly, it is a good idea to run some tests for the extension:

```python3 ./test.py```

## References

[1] Wise, M.J., 1993. String similarity via greedy string tiling and running Karp-Rabin matching. Online Preprint, Dec, 119. https://www.researchgate.net/publication/262763983_String_Similarity_via_Greedy_String_Tiling_and_Running_Karp-Rabin_Matching (Accessed 24th May 2018)

[2] Prechelt, L., Malpohl, G. and Philippsen, M., 2002. Finding plagiarisms among a set of programs with JPlag. J. UCS, 8(11), p.1016. https://page.mi.fu-berlin.de/prechelt/Biblio/jplagTR.pdf (Accessed 24th May 2018)

