# Automação de encaminhamento de mensagens no whatsapp
# Usando a funcionalidade nativa do whatsapp de encaminhar mensagem para diminuir o risco de ser bloqueado
# Encaminhar de 5 em 5 mensagens 

# Ferramentas 
# -> Selenium, para intagir com a web
# -> piperclip, para permitir dar ctrl c e ctrl v
# -> webdriver-manager, ele vai conversar com o selenium


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get('http://web.whatsapp.com')

