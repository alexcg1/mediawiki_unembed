#!/usr/bin/env python3

import urllib.request
import re # Regular exps
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("title")
args = parser.parse_args()

base_url = 'http://remix.digital/index.php'
page_title = args.title
mediawiki_url = base_url+"?title="+page_title+"&action=raw"

with urllib.request.urlopen(mediawiki_url) as response:
   wikitext = response.read()

wikitext = wikitext.decode("utf-8")

pattern = "{{:.*}}"

# Get all matches
list = re.findall(pattern, wikitext)

counter = len(list)
while counter > 0:

	# Return first match of search term
	match = re.search(pattern, wikitext, flags=0)
	
	if match:
		match = match.group() # Convert to string

		# Convert that match into a legitimate page title
		page_title = match[3:-2]
		page_title = page_title.replace(' ', '_')

		# Get that page's wikitext
		with urllib.request.urlopen('http://remix.digital/index.php?title='+page_title+'&action=raw') as response:
			extracted_page = response.read()
		extracted_page = extracted_page.decode("utf-8")

		# Replace the match with the extracted page
		wikitext = wikitext.replace(match, extracted_page)

		# Reset counter to updated list count (we count again since may be recursive embeds)
		list = re.findall(pattern, wikitext)
		counter = len(list)

print(wikitext)