DNA = {
  'G': 'C',
  'C': 'G',
  'T': 'A',
  'A': 'U'
}
def to_rna(dna_strand):
    result = ''
    for s in dna_strand:
        result += DNA.get(s)
    return result
