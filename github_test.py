import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GithubTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "https://github.com"


    def test_github_signup(self):
        """Return True if Join GitHub is found on the Sign up page of Github."""
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_link_text("Sign up")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Join GitHub" in driver.page_source


    def test_github_fork_and_star_repo_annonymous_user_redirects_to_login(self):
        """Return True if anonymous user is redirected to login page when clicked on fork/star."""
        login_url = "https://github.com/login?return_to=%2Fsysters%2Fmailman3"
        driver = self.driver
        driver.get("{0}/systers/mailman3".format(self.base_url))
        elem = driver.find_element_by_partial_link_text("Fork")
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        assert login_url == driver.current_url

        driver.get("{0}/systers/mailman3".format(self.base_url))
        elem = driver.find_element_by_partial_link_text("Star")
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        assert login_url == driver.current_url


    def test_github_explore(self):
        """Return True if the clicking on explore, trending lands on the right URL."""
        python_trending_url = "https://github.com/trending/python"
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_link_text("Explore")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        trending_elem = driver.find_element_by_partial_link_text("Trending")
        trending_elem.send_keys(Keys.ENTER)
        time.sleep(2)
        python_lang = driver.find_element_by_link_text("Python")
        python_lang.send_keys(Keys.ENTER)
        time.sleep(2)
        assert python_trending_url == driver.current_url


    def test_github_systers_automated_testing(self):
        """Return True if the automated testing README URL is achieved after appropriate clicks."""
        automated_testing_url = self.base_url + "/systers/automated-testing"
        readme_url = automated_testing_url + "/blob/master/README.md"
        driver = self.driver
        driver.get("{0}/systers/automated-testing".format(self.base_url))
        wiki_elem = driver.find_element_by_partial_link_text("webdriveriki")
        wiki_elem.send_keys(Keys.ENTER)
        time.sleep(2)
        readme_elem = driver.find_element_by_link_text("Setup Steps")
        readme_elem.send_keys(Keys.ENTER)
        time.sleep(2)
        assert driver.current_url == readme_url


    def test_github_repo_search_with_invalid_string(self):
        """Return True if the invalid search gives the correct suggestions."""
        driver = self.driver
        driver.get(self.base_url)
        search_box = driver.find_element_by_name("q")
        search_box.send_keys("**************")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "search help section"  in driver.page_source


    def tearDown(self):
        self.driver.close()
