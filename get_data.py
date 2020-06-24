import shutil
from bs4 import BeautifulSoup
import requests

# TODO: create a class?


def safe_get_request(*args, **kwargs):
    response = requests.get(*args, **kwargs)
    if not response.status_code == 200:
        raise ValueError(f'Could not get information from website. Response code is {response.status_code}')
    else:
        return response


def get_most_recent_comic_num():
    base_url = 'https://xkcd.com/'
    base_end_url = 'info.0.json'
    most_recent_comic = safe_get_request(f'{base_url}{base_end_url}').json()
    return most_recent_comic['num']


def get_image(comic_num: int):
    base_url = 'https://xkcd.com/'
    base_end_url = 'info.0.json'
    comic_info = safe_get_request(f'{base_url}{comic_num}/{base_end_url}').json()
    try:
        image_url = comic_info['img']
    except KeyError:
        print(f'no image associated with Comic number {comic_num}.')
        return
    image = safe_get_request(image_url, stream=True)
    filename = f"{comic_num}.{image_url.split('.')[-1]}"
    with open(filename, 'wb') as image_file:
        shutil.copyfileobj(image.raw, image_file)


def get_transcript(comic_num):
    all_html = requests.get(f'https://explainxkcd.com/{comic_num}')
    soup = BeautifulSoup(all_html.text, 'html.parser')
    transcript_title = soup.find(text='Transcript')
    transcript_header = transcript_title.parent.parent
    transcript = ''
    for tag in transcript_header.next_siblings:
        if tag == '\n':
            continue
        elif tag.name == 'dl':
             transcript += tag.text
        else:
            break

    return transcript
