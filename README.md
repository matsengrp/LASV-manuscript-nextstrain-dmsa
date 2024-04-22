# LASV manuscript repo for nextstrain w/ `dmsa_pred`

This repository contains a nexstrain build for Lassa virus GPC with predicted antibody escape scores mapped onto the tree. 
The analysis is performed using the [dmsa_pred](https://github.com/matsengrp/dmsa_pred) package. 
This repo is currently set up to run the data as presented in the manuscript [Deep mutational scanning reveals functional constraints and antigenic variability of Lassa virus glycoprotein complex](https://www.biorxiv.org/content/10.1101/2024.02.05.579020v1).

For those unfamiliar with Nextstrain, we recommend checking out the [Nextstrain documentation](https://docs.nextstrain.org/en/latest/) before reading further.

To run the pipeline, 
install snakemake following their 
[documentation](https://snakemake.readthedocs.io/en/v8.4.11/getting_started/installation.html), 
This pipeline has been tested with versions >= 8.4.11 

then clone this repository and the submodules
```
git clone https://github.com/matsengrp/LASV-manuscript-nextstrain-dmsa.git --recurse-submodules
```
Run the pipeline with the following command
```
snakemake --use-conda --cores 2 --configfile config/config.yaml
```
Alternatively, the pipeline can be run on a server via [Slurm](https://slurm.schedmd.com/) with the following command:
```
sbatch run_snakemake_cluster.bash
```
Each rule currently uses the environment specified in 
[my_profiles/dmsa_pred/dmsa_env.yaml](my_profiles/dmsa_pred/dmsa_env.yaml).
The configuration file specified above provides paths to the 
Lassa GPC sequences and escape data within the 
[LASV_Josiah_GP_DMS](https://github.com/dms-vep/LASV_Josiah_GP_DMS.git) submodule. 
The pipeline will output a JSON file(s) under the `auspice/` directory
that can be visualized with [auspice](https://auspice.us/) software.
CSV's of phenotype predictions can be found under `results/dmsa-phenotype/`

## Lassa GPC sequences and metadata

Lassa virus GPC sequences and metadata are downloaded as described in the [LASV_phylogeny_analysis](https://github.com/dms-vep/LASV_Josiah_GP_DMS/tree/main/non-pipeline_analyses/LASV_phylogeny_analysis) directory that is part of the [LASV_Josiah_GP_DMS](https://github.com/dms-vep/LASV_Josiah_GP_DMS.git) repository. 


## Configuration

Configuration takes place within the `Snakefile` and the `config/config.yaml` files. The `Snakefile` can be read top-to-bottom, each rule
specifies its file inputs and output and also its parameters. The `config/config.yaml` is important for configuring the DMSA phenotype prediction component of this build (e.g., paths to the deep mutational scanning directories for escape data). 