from django.test import LiveServerTestCase
from selenium import  webdriver
import time
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

        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso ...')

        buscar_animal_input.send_keys('leão')
        # time.sleep(2)
        self.browser.find_element_by_css_selector('form button').click()
        
        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)