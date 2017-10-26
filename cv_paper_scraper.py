#!/usr/bin/env python3
# coding: utf-8

import os
import urllib.request
import urllib
import socket
socket.setdefaulttimeout(10) # set timeout length as 10[s]
import fire
from bs4 import BeautifulSoup

import tqdm
from multiprocessing.dummy import Pool as ThreadPool #多线程  

bar = tqdm.tqdm(total=3037)

paper_id = 1
pdf_local_folder_name = 'nips/'
nips_dir = 'NIPS1988-2016'


def main(paper_type, year_range = '2013-2016', thread = 4):

	base_url = 'http://openaccess.thecvf.com/'
	html_url = ''
	pdf_local_folder_name = ''

	if paper_type == 'cvpr2017':
		html_url = 'CVPR2017.py'
		pdf_local_folder_name = paper_type + '/'
	elif paper_type == 'iccv2017':
		html_url = 'ICCV2017.py'
		pdf_local_folder_name = paper_type + '/'
	elif paper_type == 'cvpr2016':
		html_url = 'CVPR2016.py'
		pdf_local_folder_name = paper_type + '/'
	elif paper_type == 'iccv2015':
		html_url = 'ICCV2015.py'
		pdf_local_folder_name = paper_type + '/'
	elif paper_type == 'cvpr2015':
		html_url = 'CVPR2015.py'
		pdf_local_folder_name = paper_type + '/'
	elif paper_type == 'cvpr2014':
		html_url = 'CVPR2014.py'
		pdf_local_folder_name = paper_type + '/'
	elif paper_type == 'iccv2013':
		html_url = 'ICCV2013.py'
		pdf_local_folder_name = paper_type + '/'
	elif paper_type == 'cvpr2013':
		html_url = 'CVPR2013.py'
		pdf_local_folder_name = paper_type + '/'
	elif paper_type == 'nips':
		nips_crawl(year_range, thread)
	else:
		print("Unsupported download type!")
	
	if not os.path.exists(pdf_local_folder_name):
		os.makedirs(pdf_local_folder_name)

	# parsing openaccess page to obtain paper titles using BeautifulSoup4
	#
	print("crawing the main web")
	paper_url = base_url + html_url
	req = urllib.request.Request(paper_url)
	html = urllib.request.urlopen(req)
	soup = BeautifulSoup(html, 'html.parser')

	paper_titles = soup.find_all('a', text = 'pdf')
	print("parse the url")
	paper_urls = []
	for paper in paper_titles:
	    paper_url = base_url + paper['href']
	    paper_urls.append(paper_url)
	paper_id = 1
	downloaded_paper = os.listdir(paper_type + '/')
	downloaded_paper = [paper.split('.')[0] for paper in downloaded_paper]
	print("starting download.... with {} papers in {}".format(len(paper_urls), paper_type))
	for paper in paper_urls:
	    paper_name = paper.split('/')[-1].split('.')[0]
	    print('Downloading {} paper: {}'.format(paper_id, paper_name))
	    paper_id += 1
	    try:
	    	if paper_name not in downloaded_paper:
	    		urllib.request.urlretrieve(paper, pdf_local_folder_name + paper_name + '.pdf')
	    except Exception as e:
	    	pass

def nips_crawl(year_range, thread):
	global start_year, end_year
	print(year_range)
	start_year = year_range.split('-')[0]
	end_year = year_range.split('-')[1]
	all_dir = os.listdir(nips_dir)
	all_dir.remove('.DS_Store')
	pool = ThreadPool(thread)
	pool.map(crawl, all_dir)
	pool.join()
	bar.close()

	
def crawl(dir):
	global start_year, end_year, paper_id
	year_name = dir.split('_')[-1][:4]
	if year_name < start_year or year_name > end_year:
		return
	pdf_local_folder_name_temp = pdf_local_folder_name + year_name + '/'
	if not os.path.exists(pdf_local_folder_name_temp):
		os.makedirs(pdf_local_folder_name_temp)
	url_file = os.path.join(nips_dir, dir, 'urls.txt')
	with open(url_file, 'r') as f:
		urls = f.readlines()
		downloaded = os.listdir(pdf_local_folder_name_temp)
		downloaded = [paper_.split('.')[0] for paper_ in downloaded]
		for url in urls:
			#print(url)
			paper_name = url.split('/')[-1].split('.')[0]
			bar.update(1)
			if paper_name in downloaded:
				continue
			print('Downloading {} year {}th paper: {}'.format(year_name, paper_id, paper_name))
			#print(paper_name)
			#print(url)
			paper_name = pdf_local_folder_name_temp + paper_name + '.pdf'
			#print(paper_name)
			try:
				urllib.request.urlretrieve(url, paper_name)
			except Exception as e:
				pass
			paper_id += 1

if __name__ == '__main__':
	fire.Fire(main)