configfile: 'config/snakeconfig.yaml'


import munch


# makes the config accessible through dot notation
config = munch.munchify(config)


RAW = config.DIRS.RAW
INT = config.DIRS.INTERIM
PRO = config.DIRS.PROCESSED


#=========================================================================
# https://snakemake.readthedocs.io/en/stable/getting_started/examples.html
#=========================================================================
#
#rule all:
#    input: protect(INTERIM+'/deals.csv')
#
#
#rule report:
#    input:
#        RAW+'/recap_raw.csv',
#        lambda wildcards: config["samples"][wildcards.sample]
#    output: protect/temp(INTERIM+'/deals.csv')
#    threads: 3
#    params:
#        rg = "@RG\tID:{sample}\tSM:{sample}"
#    script: 'src/rules/clean_recap.py'
