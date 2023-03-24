

from kivymd.app import MDApp
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp
from kivy.core.window import Window
from .view import MainWindow
from kivy.clock import Clock
Clock.max_iteration = 50 

class MainApp(MDApp):
   
    colors = QueryDict()
    colors.primary = rgba("#6167E9")
    colors.secondary = rgba("#F87974")
    colors.success = rgba("#43C07B")
    colors.warning = rgba("#FFD166")
    colors.danger = rgba("#EF476F")
    colors.tertiary = rgba("#1184B2")
    #colors.tertiary_light = rgba("#C4C4C4")
    colors.grey_dark = rgba("#575757")
    colors.grey_light = rgba("#D1D1D1")
    colors.black = rgba("#222222")
    colors.white = rgba("#FFFFFF")

    fonts = QueryDict()
    fonts.size = QueryDict()
    fonts.size.h1 = dp(24)
    fonts.size.h2 = dp(22)
    fonts.size.h3 = dp(18)
    fonts.size.h4 = dp(16)
    fonts.size.h5 = dp(14)
    fonts.size.h6 = dp(12)

    fonts.heading = 'assets/fonts/Roboto/Roboto-Bold.ttf'
    fonts.subheading = 'assets/fonts/Roboto/Roboto-Regular.ttf'
    fonts.body = 'assets/fonts/Roboto/Roboto-Light.ttf'
    
    window_size = QueryDict()
    window_size.height = Window.height
    window_size.width = Window.width
    def build(self):
        return MainWindow()
    