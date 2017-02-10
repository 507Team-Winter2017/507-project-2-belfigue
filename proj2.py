#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

story_lst = []
for story_heading in soup.find_all(class_="story-heading"):
	if story_heading.a:
		story_lst.append(story_heading.a.text.replace("\n", " ").strip())
	else:
		story_lst.append(story_heading.contents[0].strip())
	# story_lst.append(story_heading.get_text())
for titles in range(10):
	print (story_lst[titles])

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url = 'https://www.michigandaily.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for section in soup.find_all(class_="panel-pane pane-mostread"):
	for story_heading in section.find_all("li"):
		try: print(story_heading.a.text.replace("\n", " ").strip())
		except: pass

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for image in soup.find_all("img"):
	try: print(image.get('alt', 'No alternative text provided!'))
	except: pass

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
from urllib.parse import urlsplit
url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
parts = urlsplit(url)
base_url = "{0.scheme}://{0.netloc}".format(parts)
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

email_lst = []

for professor in soup.find_all(class_="field field-name-contact-details field-type-ds field-label-hidden"):
	link = professor.find('a')
	node = link.get("href")
	sub_r = requests.get(base_url+node)
	sub_soup = BeautifulSoup(sub_r.text, "html.parser")
	contact = sub_soup.find(class_="field field-name-field-person-email field-type-email field-label-inline clearfix")
	address = contact.find('a')
	email = address.get_text()
	email_lst.append(email)

while True:
	try:
		next_page = soup.find(class_='pager-next last')
		next_link = next_page.find('a')
		next_page = next_link.get('href')
		next_url = requests.get(base_url + next_page)
		soup = BeautifulSoup(next_url.text, "html.parser")
		for professor in soup.find_all(class_="field field-name-contact-details field-type-ds field-label-hidden"):
			link = professor.find('a')
			node = link.get("href")
			sub_r = requests.get(base_url+node)
			sub_soup = BeautifulSoup(sub_r.text, "html.parser")
			contact = sub_soup.find(class_="field field-name-field-person-email field-type-email field-label-inline clearfix")
			address = contact.find('a')
			email = address.get_text()
			email_lst.append(email)

	except: break

for i, text in enumerate(email_lst):
	print (i+1, text)