from selenium import webdriver
import unittest



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Guilherme acessa o site e ve sua homepage
        self.browser.get('http://localhost:8000')

        # Ele ve se acessou o site que ele quer acessar , se é um site de TO-DO listas
        self.assertIn('To-Do' , self.browser.title)
        self.fail('FINISH the test!')
    
        #Ele é convidado a inserir um item de tarefa imediatamente

        #Ele digita "aprender testes funcionais" em uma caixa de texto

        #QUando ele aperta Enter a pagina é atualizada e agora possui
        # "1:aprender testes funcionais" como em uma lista normal

        #Ele agora insere um novo item "user testes funcionais para facilitar minha vida"

        # Agora a pagina é atualizada e mostra os dois itens em sua lista

        #Guilherme se pergunta se o site se lembrará de sua lista. Entao ele nota
        #que o site gerou um URL unico para mim -- há um pequeno texto
        #explicando isso.

        #Ele acessa a url e sua lista está la


        #Satisfeito ele volta a dormir
if __name__ == '__main__':
    unittest.main(warnings='ignore')
