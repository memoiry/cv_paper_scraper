# cv_paper_scraper

cv_paper_scraper is tiny script for downloading pdfs from CVFoundation Open Access Repository: 
http://openaccess.thecvf.com/menu.py

And also NIPS

This script also make all paper list as html file.

## Requirements

- Python 2 or 3 (it should works in both)

Simply 

```bash
pip -r requirements.txt
```

## Usage

### ICCV or CVPR

```bash
python cv_paper_scraper.py cvpr2017 # You can choose either 2013-2017 for cvpr
python cv_paper_scraper.py iccv2017 # You can choose either 2013, 2015, 2017 for iccv
```


### NIPS
 

```bash
#python cv_paper_scraper.py nips year_range num_thread
#For example
python cv_paper_scraper.py nips 2013-2016 4
```

Enjoy!




