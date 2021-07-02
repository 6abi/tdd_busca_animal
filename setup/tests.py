from django.test import LiveServerTestCase
from selenium import  webdriver

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('E:\\tdd_busca_animal\\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_buscanco_um_novo_animal(self):
        """Teste se um usuário encontra um animal pesquisando"""
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca animal', brand_element.text)