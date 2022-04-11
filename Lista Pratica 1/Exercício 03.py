# DNA para RNA. Os nucleotídeos de RNA (chamados ribonucleotídeos) contêm as
# bases adenina (A), guanina (G), citosina (C) e uracila (U), mas esta última pirimidina, está presente
# em lugar de timina que está no DNA. Escreva uma função que recebe um string de DNA (A, C, G,
# T) e retorna a seqüência de RNA (A, C, G, U).


def DNAtoRNA():
    dna = 'A C G T'
    rna = dna.replace('T', 'U')
    return rna


print(DNAtoRNA())
