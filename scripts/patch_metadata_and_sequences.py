# Description:
# Python script to format previously 
# extracted metadata and sequences
# for Nextstrain
# as metadata

# Author:
# Caleb Carr

# Imports
import os
import pandas as pd
from Bio import SeqIO

# Functions
def patch_metadata(raw_metadata, metadata_output):
    """
    Function to reformat metadata
    """
    # Read data in as dataframe
    raw_metadata = pd.read_csv(raw_metadata, sep="\t")

    # Columns to replace values in
    columns = [
        "virus",
        "segment",
        "host",
        "accession",
        "date",
        "location",
        "country",
        "database",
        "authors",
        "url",
        "title",
        "journal",
        "paper_url",
    ]
    # Loop through columns and replace incompatible values
    for col in columns:
        raw_metadata[col] = raw_metadata[col].replace({"MISSING" : "?"})
        if col == "country":
            raw_metadata[col] = raw_metadata[col].replace({"Cote d'Ivoire" : "Ivory Coast"})

    # Save dataframe
    raw_metadata.to_csv(metadata_output, sep="\t", index=False)

def edit_fasta_headers(input_sequences, output_sequences):

    # Iterate through headers and remove added info
    with open(output_sequences, "w") as new_sequences:
        for curr_fasta in SeqIO.parse(input_sequences, "fasta"):
            new_name = str(curr_fasta.description).split(" ")[0][:-2]
            curr_fasta.id = new_name
            curr_fasta.description = ""
            SeqIO.write(curr_fasta, new_sequences, "fasta")

    # Close files
    new_sequences.close()


def main():
    """
    Main method
    """

    # Input files
    raw_metadata = str(snakemake.input.raw_metadata)
    input_sequences = str(snakemake.input.raw_sequences)

    # Output files
    metadata_output = str(snakemake.output.metadata)
    output_sequences = str(snakemake.output.sequences)

    # Run functions to patch data
    patch_metadata(raw_metadata, metadata_output)
    edit_fasta_headers(input_sequences, output_sequences)


if __name__ == "__main__":
    main()