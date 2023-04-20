from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.clock import Clock
from plyer import tts,filechooser
from .round_image import round_image


Builder.load_file('views/personal_info/personal.kv')

# use plyer filechooser, works in android depending on root directory path: https://stackoverflow.com/questions/72430198/plyer-filechooser-working-perfectly-on-windows-but-does-not-work-on-android
class PersonalScreen(MDBoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        
        

    def go_back(self):
        self.parent.manager.current = "scrn_settings"



    def open_filechooser(self):
        filechooser.open_file(on_selection=self.on_selection)

    def on_selection(self, selection):
        if selection:
            #print(selection[0])
            show_img_path = round_image(selection[0])
            self.ids.profile_pic.source = show_img_path  # selection[0]   
    
    


    """Adicionar quando faco upload a imagem 'a DB e adiciona la a imagem. Deve ser sequencial mandar para db, depois ir buscar 'a db.
    Quando faco render da class devo ir logo buscar a base de dados quando o user esta logged in"""

    """Quando apertar cada campo do field deve abrir outro screen e pedir para alterar nome, password, a passsword deve ser mandado email e numero deve ser mandado numero para novo numero ou entao nao muda"""