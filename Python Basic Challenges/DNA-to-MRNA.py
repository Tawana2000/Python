# Write a function to transcribe a DNA sequence into an mRNA sequence

def transcribe_to_mrna(dna):
    
    transcription = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(transcription.get(base, '') for base in dna.upper())

print(transcribe_to_mrna('ATGC'))