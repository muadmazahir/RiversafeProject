from web_scrapper import WebScrapper
import pytest

#Pytests
def test_scrap_web_method():
    web_scrapper = WebScrapper("http://www.learningaboutelectronics.com")
    web_scrapper.scrap_web()
    assert "1234" == web_scrapper.get_content()

#testing the write_file method. Testing to see if opening a file that doesn't exist raises an error.
def test_missing_file_name_raises_error():
    web_scrapper = WebScrapper("jkl")
    web_scrapper.write_file('jj')
    with pytest.raises(FileNotFoundError):
        f = open('zz', 'r', encoding="utf-8")
    web_scrapper.delete_file('jj')
