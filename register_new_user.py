import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'D:\Documents\Curso de Selenium Platzi\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_new_user(self):
        driver = self.driver
        #le decimos al driver que encuentre la opción de cuenta por su Xpath y le haga click para desplegar el menu
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_xpath('//*[@id="header-account"]/div/ul/li[6]/a').click()


        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        #validamos que el botón esté visible y habilitado
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled)
        create_account_button.click()

        #comprueba que estamos en el sitio de crear cuenta
        self.assertEqual('Create New Customer Account', driver.title)

        #creación de variables con el nombre del selector correspondiente
        firstname = driver.find_element_by_id('firstname')
        lastname = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        newsletterSuscription = driver.find_element_by_id('is_subscribed')
        submit_buttom = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

         #veremos si los elementos están habilitados
        self.assertTrue(firstname.is_enabled() and lastname.is_enabled() and email_address.is_enabled()
        and password.is_enabled() and confirm_password.is_enabled() and newsletterSuscription.is_enabled() and submit_buttom.is_enabled())

        #mandamos los datos al formulario
        firstname.send_keys('Test')
        lastname.send_keys('Test name')
        email_address.send_keys('test@test.com')
        password.send_keys('Contraseñita123')
        confirm_password.send_keys('Contraseñita123')
        submit_buttom.click()

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)