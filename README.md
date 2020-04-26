# TV Series File Renamer

# Description

This package allows you to rename your tv series episodes by extracting episodes names from [imdb](https://www.imdb.com/).

For example:

Before running the script: Better.Call.Saul.S01E02.Mijo.720p.WEB-DL.2CH.x265.HEVC-PSA

After running the script: 2 - Mijo

# Requirements

* Python 3
* Pip 3

# Instructions to run the script

* Download the package
* Navigate to the package folder in the terminal
* In the command line run `$ pip3 install -r requirements.txt`
* Make sure your folders are in the following format

  Better Call Saul/
                
  | -- S1/
 
  | -- S2/
  
  | -- S3/
           
  | -- S4/

  | -- S5/
  
* Keep only episode files in the season folders.
* In the command line run python3 main.py path to TV Series Name folder TV Series Name
  
  For example
  
  On Linux or Mac OS
  
  `$ python3 main.py "/home/user/Better Call Saul/" "better call saul"`
  
  # Screenshot
  
  ![Image](https://imgur.com/N2wZGb1.png)
  
  On Windows
  
  `> python3 main.py "C:\\\New folder\\\Better Call Saul\\\\" "better call saul"`
  
  # Screenshot
  
  ![Image](https://i.imgur.com/1rm0uxe.png)
  
# Video Demo

  ![Video](https://imgur.com/macIIWh.gif)
