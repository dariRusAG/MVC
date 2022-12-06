# импорт объекта для создания приложения
from flask import Flask

# создание экземпляра объекта приложения
app = Flask(__name__)
# установим секретный ключ для подписи.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# здесь необходимо указать все контроллеры страниц
import controllers.index
import controllers.new_reader
import controllers.search
