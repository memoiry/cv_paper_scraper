# cv_paper_scraper

cv_paper_scraper is tiny script for downloading pdfs from CVFoundation Open Access Repository: 
http://openaccess.thecvf.com/menu.py

And also NIPS (range from 1988-2016, currently 2017 is not supported since it's not released and there is a repo scraping nips 2017 papers' abstract from arxiv, you can `git clone -r https://github.com/memoiry/cv_paper_scraper` to download both the repo)

## Requirements

- Python 2 or 3 (it should works in both)

Simply 

```bash
git clone -r https://github.com/memoiry/cv_paper_scraper
cd cv_paper_scraper
pip install -r requirements.txt
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




