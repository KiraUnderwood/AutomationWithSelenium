import unittest
import time

from selenium import webdriver

'''
work with selectors
'''

class EpamPageTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://epam.github.io/JDI/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_page_title(self):
        assert self.driver.title == "Home Page"
        time.sleep(5)

    def test_perform_login(self):
        self.driver.find_element_by_id("user-icon").click()
        login = self.driver.find_element_by_tag_name('input[id="name"]').send_keys("epam")
        pwd = self.driver.find_element_by_tag_name('input[id="password"]').send_keys("1234")
        self.driver.find_element_by_tag_name('button[type="submit"]').click()
        time.sleep(5)
        assert self.driver.find_element_by_id('user-name').text == 'PITER CHAILOVSKII'

    def test_page_title_2(self):
        assert self.driver.title == "Home Page"

    def test_4_elem_in_header_nav_bar(self):
        navbar = [i.lower() for i in ["HOME", "CONTACT FORM", "SERVICE", "METALS & COLORS"]]
        assert self.driver.find_element_by_xpath('/html/body/header/div/nav/ul[1]/li[1]/a').text.lower() in navbar
        assert self.driver.find_element_by_xpath('/html/body/header/div/nav/ul[1]/li[2]/a').text.lower() in navbar
        assert self.driver.find_element_by_xpath('/html/body/header/div/nav/ul[1]/li[3]/a').text.lower() in navbar
        assert self.driver.find_element_by_xpath('/html/body/header/div/nav/ul[1]/li[4]/a').text.lower() in navbar
        time.sleep(5)

    def test_4_displayed_img(self):
        for image in self.driver.find_elements_by_tag_name("img"):
            assert image.is_displayed()
        time.sleep(5)

    def test_4_texts_below_icon_elements(self):
        expected = ['To include good practices\nand ideas from successful\nEPAM project',
                    'To be flexible and\ncustomizable', 'To be multiplatform',
                    'Already have good base\n(about 20 internal and\nsome external projects),\nwish to get more…']
        read_from_page = [self.driver.find_element_by_css_selector(
            "body > div > div.uui-main-container > main > div.main-content > div > div:nth-child({}) > div > span".format(
                i)).text for i in [1, 2, 3, 4]]
        assert set(expected) == set(read_from_page)

    def test_5_text_in_main_headers(self):
        text1 = r'EPAM FRAMEWORK WISHES…'
        text2 = r'LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISICING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA. UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR.'

        el1 = self.driver.find_element_by_css_selector(
            "body > div > div.uui-main-container > main > div.main-content > h3.main-title.text-center")
        assert el1.text.lower() == text1.lower() and el1.is_displayed()

        el2 = self.driver.find_element_by_css_selector(
            "body > div > div.uui-main-container > main > div.main-content > p")
        assert el2.text.lower() == text2.lower() and el2.is_displayed()

    def test_find_a_frame(self):
        assert self.driver.find_element_by_id("iframe").is_displayed()

    def test_switch_to_frame_find_logo(self):
        self.driver.switch_to.frame(self.driver.find_element_by_id("iframe"))
        assert self.driver.find_element_by_css_selector("#epam_logo").is_displayed()

    def test_switch_back_to_default(self):
        self.driver.switch_to.default_content()

    def test_subheader_text(self):
        sub_header = self.driver.find_element_by_css_selector(
            "body > div > div.uui-main-container > main > div.main-content > h3:nth-child(3) > a")
        assert sub_header.text.lower() == 'JDI GITHUB'.lower()

    def test_link_exists_and_propper(self):
        link = self.driver.find_element_by_link_text("JDI GITHUB")
        assert link.get_attribute("href") == 'https://github.com/epam/JDI'

    def test_side_bar_present(self):
        assert self.driver.find_element_by_css_selector(r'[name="navigation-sidebar"]').is_displayed()

    def test_footer_present(self):
        assert self.driver.find_elements_by_tag_name('footer')


if __name__ == '__main__':
    unittest.main()
