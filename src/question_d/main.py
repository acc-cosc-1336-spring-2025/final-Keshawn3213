def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    len_s1 = len(dna_string1)
    len_s2 = len(dna_string2)

    for i in range(len_s1 - len_s2 + 1):
        if dna_string1[i:i + len_s2] == dna_string2:
            positions.append(i + 1)  # +1 for 1-based index

    return tuple(positions)
