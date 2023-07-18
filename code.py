import re

title_pattern = re.compile(r'#[*].')
index_pattern = re.compile(r'#index\d+')
year_pattern = re.compile(r'#t\d{4}')
venue_pattern = re.compile(r'#c.')
authors_pattern = re.compile(r'#@.')
abstract_pattern = re.compile(r'#!.')
citations_pattern = re.compile(r'#%\d')


title = 'NULL '
index = 'NULL '
year = 'NULL '
venue = 'NULL '
authors = 'NULL '
abstract = 'NULL '
citation = []

title_list = []
index_list = []
year_list = []
venue_list = []
authors_list = []
abstract_list = []
citation_list = []

text_file = open("PAPERS.sql", "w", encoding='utf-8')

def conv(line):
    line = line.replace("'", "")
    line = line.replace('"', "")
    return line

def citations(paperIndex, citedList):
    list = []
    for citedPaper in citedList:
        list.append((paperIndex[: -1], citedPaper[: -1]))
    return list

i = 1
for line in open("test1.txt", encoding='utf-8'):
    if title_pattern.search(line):
        title = line[2:]
    elif index_pattern.search(line):
        index = line[6:]
    elif year_pattern.search(line):
        year = line[2:]
    elif venue_pattern.search(line):
        venue = line[2:]
    elif authors_pattern.search(line):
        authors = line[2:]
    elif abstract_pattern.search(line):
        abstract = line[2:]
    elif citations_pattern.search(line):
        citation.append(line[2:])
    elif line == '\n':
        print(f"Processed book-{i}")
        i = i+1
        title_list.append(conv(title[: -1]))
        index_list.append(conv(index[: -1]))
        year_list.append(conv(year[: -1]))
        venue_list.append(conv(venue[: -1]))
        authors_list.append(conv(authors[: -1]))
        abstract_list.append(conv(abstract[: -1]))
        citation_list = citation_list + citations(index, citation)
        
        title = 'NULL '
        index = 'NULL '
        year = 'NULL '
        venue = 'NULL '
        authors = 'NULL '
        abstract = 'NULL '
        citation = []
    else :
        pass

text_file.write("INSERT INTO PAPERS (Title, Ind, WrittenYear, Venue, WrittenBy, Abstract) VALUES ")
i = 0
while i < len(title_list):
    text_file.write(f"('{title_list[i]}', {index_list[i]}, {year_list[i]}, '{venue_list[i]}', '{authors_list[i]}', '{abstract_list[i]}')")
    if i != len(title_list)-1 :
        text_file.write(",")
    else:
        text_file.write(";")
    i = i+1
text_file.write("\n")
text_file.write("INSERT INTO CITATIONS (Ind, CitedInd) VALUES ")

i = 0
while i < len(citation_list):
    text_file.write(f"{citation_list[i]}")
    if i != len(citation_list)-1 :
        text_file.write(",")
    else:
        text_file.write(";")
    i = i+1


text_file.close()
