from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import kanjikoohi.constants as const
import os
from kanjikoohi.story_filtration import StoryFiltration


class Koohi(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Koohi, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def signin_page(self):
        self.get(const.url)

    def login(self, my_username=None, my_password=None):
        signin = self.find_element("css selector", 'a[href="/account"]')
        signin.click()
        username = self.find_element("id", 'username')
        username.send_keys(f'{my_username}')
        password = self.find_element("id", 'password')
        password.send_keys(f'{my_password}')
        commit = self.find_element("name", 'commit')
        commit.click()

    def study(self):
        study = self.find_element("css selector", 'a[href="/study/kanji/1"]')
        study.click()

    def search(self, id_or_kanji=None):
        search = self.find_element("id", 'txtSearch')
        search.clear()
        search.send_keys(f'{id_or_kanji}')
        search.send_keys(Keys.ENTER)

    def get_kanji(self):
        kanji = self.find_element("css selector", 'span[lang="ja"]')
        return kanji.text

    def get_most_star_story(self):
        filtration = StoryFiltration(driver=self)
        story = filtration.get_most_fav()
        return story.text

    def get_story_list(self, size: int):
        filtration = StoryFiltration(driver=self)
        story_list = filtration.get_all()
        format_list = []
        for items in story_list:
            if items.text != '':
                format_list.append(items.text)
        return format_list[0:size]

    def next_kanji(self):
        next_but = self.find_element("css selector", 'a[class="study-search_btn is-next"]')
        next_but.click()
        self.check_error_()

    def prev_but(self):
        prev_but = self.find_element("css selector", 'a[class="study-search_btn is-prev"]')
        prev_but.click()
        self.check_error_()

    def check_error_(self):
        while self.title == "Oops, please retry in a short moment":
            self.refresh()
            print(self.title)
            print("Refresh !")
            self.implicitly_wait(5)
            if self.title != "Oops, please retry in a short moment":
                print(self.title)
                break
