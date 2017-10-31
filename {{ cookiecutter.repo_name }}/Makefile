.PHONY: clean create_environment install_src test lint requirements sync_data_to_s3 sync_data_from_s3 git-config

#################################################################################
# GLOBALS                                                                       #
#################################################################################

SHELL := /bin/bash

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = {{ cookiecutter.s3_bucket }}
PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}


ifeq (,$(shell which conda))
	HAS_CONDA=False
	CONDA_PATH=$(shell which conda)
else
	HAS_CONDA=True
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	flake8 --exclude='lib/,bin/,docs/conf.py,src/rules/.snakemake.*' .

## Upload Data to S3
sync_data_to_s3:
ifeq (default,$(PROFILE))
	aws s3 sync data/ s3://$(BUCKET)/data/
else
	aws s3 sync data/ s3://$(BUCKET)/data/ --profile $(PROFILE)
endif

## Download Data from S3
sync_data_from_s3:
ifeq (default,$(PROFILE))
	aws s3 sync s3://$(BUCKET)/data/ data/
else
	aws s3 sync s3://$(BUCKET)/data/ data/ --profile $(PROFILE)
endif


## Set up python interpreter environment
create_environment:
ifeq (True,$(HAS_CONDA))
	@echo ">>> Detected conda, creating conda environment."
	conda env create -n $(PROJECT_NAME) python=3 --file environment.yml
	@echo ">>> New conda env created. Activate with:\nsource activate $(PROJECT_NAME)\n or make env"
else
	@echo ">>> No conda env detected, please launch and retry."
endif


## install the src library into pip
install_src: create_environment
ifneq (,$(findstring $(PROJECT_NAME),$(CONDA_PATH)))
	source activate $(PROJECT_NAME) && \
	pip install -e .
	@">>> Installed src into the $(PROJECT_NAME) env can now be loaded with `src.data`
else
	@">>> $(PROJECT_NAME) is not activated please activate
endif


## run tests
test:
	pytest --cov=src

## create coverage report
cov:
	pytest --cov=src --cov-report html --cov-report term --doctest-module


#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

## plot the DAG of the current Snakefile to pdf and open
dag :
	snakemake --dag | dot -Tpdf > reports/figures/dag.pdf
	open reports/figures/dag.pdf


## plot the rulegraph of the current Snakefile to pdf and open
rulegraph :
	snakemake --rulegraph | dot -Tpdf > reports/figures/rulegraph.pdf \
		&& open reports/figures/rulegraph.pdf

## show the summary and statistics of the current snakemake state
snakestats :
	snakemake -S | csvlook -t


## generate Sphinx HTML documentation, including API docs
docs:
	rm -f docs/src.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ src src/rules
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := show-help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' 
