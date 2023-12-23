#Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

import requests
import re

romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet)
words = response.text
words = re.sub(r'[.,;"-]', '', words)
words = re.sub(r'[:\n]', ' ', words) 
words = re.split(' ', words)
count = []
for i in words:
    if (words.count(i), i) not in count:
        count.append((words.count(i), i))
s_count = sorted(count, reverse=True)
print(f'The most frequent words in {romeo_and_juliet} is: {s_count[ : 10]}')

'''Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats'''

cat_pi = requests.get('https://api.thecatapi.com/v1/breeds')
data = cat_pi.json()


def metric_weights(data):
    metric_weights = []

    for breed in data:
        metric_weights.append(
            (int(breed['weight']['metric'].split()[0]) + int(breed['weight']['metric'].split()[-1])) / 2)

    median = numpy.median(metric_weights)
    mean = numpy.mean(metric_weights)
    min_metric = min(metric_weights)
    max_metric = max(metric_weights)
    sd = numpy.std(metric_weights)
    print("WEIGHT DATA")
    print("Standard Deviation: %0.2f" % sd)
    print("Minimum:", min_metric)
    print("Maximum:", max_metric)
    print("Median:", median)
    print("Mean: %0.2f" % mean)
metric_weights(data)

#II
def life_spans(data):
    lifespans = []
    for breed in data:
        lifespans.append((int(breed['life_span'].split()[0]) + int(breed['life_span'].split()[-1])) / 2)

    median = numpy.median(lifespans)
    mean = numpy.mean(lifespans)
    min_span = min(lifespans)
    max_span = max(lifespans)
    sd = numpy.std(lifespans)
    print("LIFESPAN DATA")
    print("Standard Deviation: %0.2f" % sd)
    print("Minimum:", min_span)
    print("Maximum:", max_span)
    print("Median:", median)
    print("Mean: %0.2f" % mean)
life_spans(data)

cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)

if response.status_code == 200:
    cat_breeds = response.json()
else:
    print("Failed to retrieve information from API")
    
#III
from collections import defaultdict 
frequency_table = defaultdict(int)
breed_info = {}
for breed in cat_breeds:
    breed_info[breed['name']] = breed['origin']
for breed in breed_info.values():
    frequency_table[breed] += 1

print(frequency_table)

#3
from collections import defaultdict
frequency_table = defaultdict(int)
breed_info = {}
for breed in cat_breeds:
    breed_info[breed['name']] = breed['origin']
for breed in breed_info.values():
    frequency_table[breed] += 1

print(frequency_table)


#UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', {'border': '1'})
rows = table.find_all('tr')[1:]
for row in rows:
    cells = row.find_all('td')
    name = cells[0].text.strip()
    print(f'{name}')