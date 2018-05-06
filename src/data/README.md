# Files
  |-- download - folder for scripts to download raw data into raw folder  
  |   +-- download.py - script to download and update raw data   
  |   +-- *.py  - scrips called by download.py  
  |  
  |-- clean - folder for scripts to clean data into interim folder  
  |   +-- clean.py - script to clean raw data  
  |   +-- *.py - scripts called by clean.py  
  |  
  |-- preprocess - folder for scrips to process the data into processed folder for visualization and analysis  
  |   +-- process.py - script to process the data  
  |   +-- *.py - scripts called by process.py  

# Steps to run:
1. python download.py
2. python clean.py
3. python preprocess.py


# Processed Data Structure (End goal for data scripting)
## Weekly
| location    | year   | week | dengue | malaria | MaxTempC | MeanTempC | MinTempC | DewPointC | ... etc.  
| Singapore | 2012 | 1       | 1          | 0          | 32             | 30               | 28             | 20            | ... etc.  

## Yearly
| location    | year   | dengue | malaria | MaxTempC | MeanTempC | MinTempC | DewPointC | ... etc.  
| Singapore | 2012 | 100       | 10        | 32             | 30               | 28             | 20            | ... etc.  

If data does not exist for that location (e.g. weekly Malaysia malaria), it will not be recorded as an observation in the table (e.g. weekly table).
