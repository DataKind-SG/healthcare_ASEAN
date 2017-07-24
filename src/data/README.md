# Files
"""
  |-- download_scripts - folder for scripts called by download_raw_data.py
  |   +-- *.py
  |
  |-- clean_scripts - folder for scripts called by clean_data.py
  |   +-- *.py
  |
  |-- download_raw_data.py - script to download and update raw data  
  |-- clean_data.py - script to clean raw data into interim folder
  |-- preprocess_data.py - script to process the data into processed folder for visualization and analysis
"""
# Steps to run:

1. python download_raw_data.py
2. python clean_data.py
3. python preprocess_data.py

# Processed Data Structure (End goal for data scripting)
## Weekly
| location    | year   | week | dengue | malaria | MaxTempC | MeanTempC | MinTempC | DewPointC | ... etc.
| Singapore | 2012 | 1       | 1          | 0          | 32             | 30               | 28             | 20            | ... etc.

## Yearly
| location    | year   | dengue | malaria | MaxTempC | MeanTempC | MinTempC | DewPointC | ... etc.
| Singapore | 2012 | 100       | 10        | 32             | 30               | 28             | 20            | ... etc.

If data does not exist for that location (e.g. weekly Malaysia malaria), it will not be recorded as an observation in the table (e.g. weekly table).
