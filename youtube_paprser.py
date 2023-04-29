from bs4 import Beautiful5oup as BS
from urllib.parse import urlencode
from selenium import webdriver


class ParseYoutube:
    def __init__(self) -> None:
        self_link = 'https://www.youtube.com/'
    
    @classmethod
    def one_request(cls, requset: str):
        self = cls.__new__(cls)
        self._link = "https://www.youtube.com/results?" + urlencode({"search_query": request})
        return self
    
    def parse(self, n: int) -> list[str]:
        match self_link:
            case 'https://www.youtube.com/': return self._parse_main(n)
            case _: return self._parse_by_link(n)

    def _parse_main(self, n: int) -> list[str]:
        links: list[str] = [] #ссылки на видео 

        browser = webdriver.Ghrome()
        browser.get(self._link)
        html = browser.page_source
        browser.quit()

        soup = BS(html, 'html.parser')
        contents = soup.find_all('div', {'class': 'style-scope ytd-rich-item-rendere', 'id':'content' })

        for video in contents:
            video - video.find_next('a', {'id': 'thumbnail'})
            links.append(f'https://www.youtube.com{video.attrs["href"]}') 
            if len(links) == n:
                break

        return links

    def _parse_by_link(self, n: int) -> list[str]:
        links: list[str] =[] #список видео

        browser = webdriver.Chrome()
        browser.get(self._link)
        html = browser.page_source
        browser.quit()

        soup = BS(html, "html.parser")
        contents = soup.find_all("ytd-thumbnail", {"class": "style-scope ytd-video-renderer"})

        for video in contents:
            video = video.find_next('a', {"id": "thumbnail"})
            links.append(f"https://www.youtube.com{video.attrs['href']}")
            if len(links) == n:
                break

        return links
if __name__ == "__main__":
    parserYt = ParserYoutube()
    print(*parserYt.parse(5), sep='\n')

    parserLinkYt = ParserYoutube().one_request("Майнкрафт")
    print(*parserLinkYt.parse(5), sep='\n') 