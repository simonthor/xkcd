from bs4 import BeautifulSoup
import requests

# %%
all_html = requests.get('https://explainxkcd.com/2316')

# %%
soup = BeautifulSoup(all_html.text, 'html.parser')

# %%
transcript_title = soup.find(text='Transcript')
transcript_header = transcript_title.parent.parent

# %%
for tag in transcript_header.next_siblings:
    if tag == '\n':
        continue
    elif tag.name == 'dl':
        print(tag.text)
    else:
        break
