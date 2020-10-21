# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos
# ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    # Realiza todo lo necesario antes de empezar la prueba
    # metodo para ambientizar el inicio de los casos
    #@classmethod Decorador para que las distintas paginas corran en una sola pestaña
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= r'D:\Documents\Curso de Selenium Platzi\chromedriver.exe')
        driver = cls.driver
        # esperamos 10 seg antes de realizar la siguiente accion
        driver.implicitly_wait(10)

    # metodo para iniciar proceso
    # Caso de prueba donde realizaremos una serie de acciones para que el navegador las automatice
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.youtube.com/')
    
    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org/')

    # metodo para cerrar ventana
    # Cerramos el navegador una vez terminadas las pruebas
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__== "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))