import sys # command line arguments read

def validate_sequence(sequence, k):
    # explain what valid DNA nucleotides are
    valid_bases = set("ACGT")  # only valid DNA bases

    # sequence must be long enough for k-mer + next character
    if len(sequence) < k + 1:
        return False

    # ensure every character is a valid DNA base
    return all(base in valid_bases for base in sequence)

def update_kmer_count(kmer_data, kmer, next_char):
    # if this k-mer is not yet in the dictionary, initialize its structure
    if kmer not in kmer_data:
        kmer_data[kmer] = {
            "count": 0,          
            # total number of times k-mer appears
            "next_chars": {}     
            # dictionary of following character frequencies
        }

    # increment total occurrence count of this k-mer
    kmer_data[kmer]["count"] += 1

    # if this next character has not been seen before for this k-mer, initialize it
    if next_char not in kmer_data[kmer]["next_chars"]:
        kmer_data[kmer]["next_chars"][next_char] = 0

    # increment frequency of this next character
    kmer_data[kmer]["next_chars"][next_char] += 1

    # return updated dictionary
    return kmer_data

def count_kmers_with_context(sequence, k, kmer_data):
    # loop through sequence, stopping so that k-mer and next character is valid
    for i in range(len(sequence) - k):

        # extract k-mer substring
        kmer = sequence[i:i + k]

        # get the character immediately after the k-mer
        next_char = sequence[i + k]

        # update counts in the shared dictionary
        update_kmer_count(kmer_data, kmer, next_char)

    # return updated k-mer statistics
    return kmer_data

def write_results_to_file(kmer_data, output_filename):
    # sort k-mers alphabetically for consistent output
    sorted_kmers = sorted(kmer_data.keys())

    # open output file for writing
    with open(output_filename, "w") as f:

        # loop through each k-mer
        for kmer in sorted_kmers:

            # get dictionary of next-character frequencies
            next_chars = kmer_data[kmer]["next_chars"]

            # format next character counts into readable string
            next_char_str = " ".join(
                f"{char}:{freq}"
                for char, freq in sorted(next_chars.items())
            )

            # write k-mer, total count, and next-character distribution
            f.write(f"{kmer} {kmer_data[kmer]['count']} {next_char_str}\n")

def main():
    # First command-line argument: input file with sequences
    sequence_file = sys.argv[1]

    # Second argument: k-mer size
    k = int(sys.argv[2])

    # Third argument: output file name
    output_file = sys.argv[3]

    # Inform user what file is being processed
    print(f"Reading sequences from {sequence_file}...")

    # Dictionary to store ALL k-mer data across ALL sequences
    kmer_data = {}

    # Open input file
    with open(sequence_file, "r") as f:

        # Read each sequence line by line
        for sequence in f:

            # Remove whitespace/newlines and standardize format
            sequence = sequence.strip().upper()

            # Skip invalid sequences
            if not validate_sequence(sequence, k):
                print("  Warning: Skipping invalid sequence")
                continue

            # Extract k-mers and update global dictionary
            count_kmers_with_context(sequence, k, kmer_data)

    # Write final aggregated results once all sequences are processed
    write_results_to_file(kmer_data, output_file)


# Ensures script runs only when executed directly (not imported)
if __name__ == "__main__":
    main()
