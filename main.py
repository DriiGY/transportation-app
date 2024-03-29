
from os.path import dirname, join
from kivy.garden.iconfonts import register
from app import MainApp
from dotenv import load_dotenv

register(
    "Feather",
    join(dirname(__file__), "assets/fonts/feather/feather.ttf"),
    join(dirname(__file__), "assets/fonts/feather/feather.fontd"),
)

    

load_dotenv()

MainApp().run()
