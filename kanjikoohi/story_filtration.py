from selenium.webdriver.remote.webdriver import WebDriver


class StoryFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_most_fav(self):
        share_story = self.driver.find_element("id", 'SharedStoriesListComponent')
        story = share_story.find_element("class name", 'story')
        return story

    def get_all(self):
        share_story = self.driver.find_element("id", 'SharedStoriesListComponent')
        story = share_story.find_elements("class name", 'story')
        return story
