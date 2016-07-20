.PHONY: clean raw-data data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

BUCKET = [OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')
log = warning

#################################################################################
# COMMANDS                                                                      #
#################################################################################

requirements:
	pip install -q -r requirements.txt

raw-data: requirements
	python src/data/download_raw_data.py --log=$(log)

data: requirements
	python src/data/make_dataset.py

clean:
	find . -name "*.pyc" -exec rm {} \;

lint:
	flake8 --exclude=lib/,bin/ .

sync_data_to_s3:
	aws s3 sync data/ s3://$(BUCKET)/data/

sync_data_from_s3:
	aws s3 sync s3://$(BUCKET)/data/ data/

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################
