from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.clock import Clock
from plyer import tts,filechooser
Builder.load_file('views/personal_info/personal.kv')

# use plyer filechooser, works in android depending on root directory path: https://stackoverflow.com/questions/72430198/plyer-filechooser-working-perfectly-on-windows-but-does-not-work-on-android
class PersonalScreen(MDBoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        self.manager_open = False
        

    def go_back(self):
        self.parent.manager.current = "scrn_settings"



    def open_filechooser(self):
        filechooser.open_file(on_selection=self.on_selection)

    def on_selection(self, selection):
        if selection:
            print(selection[0])
            self.ids.profile_pic.source = selection[0]

    def show_file_manager(self):
        print("here")
        self.file_manager  = MDFileManager()
        
        Window.bind(on_keyboard=self.events)
        #print(self.file_manager)
        self.file_manager.bind(
            exit_manager=self.exit_manager,
            select_path=self.select_path
            )
        self.file_manager.previous = True
        self.file_manager_open()
        print(self.file_manager.__dict__)
        #self.exit_manager()





    def file_manager_open(self):
        #print(self.file_manager)
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path, *args):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        print(self.file_manager.current_path)
        self.exit_manager()
        
        print(path)
        
        
    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''
       
        
        print(self.file_manager, "iiiiiiiiiiiiiiiiiii")
        self.file_manager.close()
        self.manager_open = False
        print("gsfdfdfdfghd")
        print("gsfdfdfdfghd")
    

    def events(self, instance, keyboard, keycode, text, modifiers ):  
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        elif keyboard == 70:
            if self.manager_open:
                self.file_manager.back()
        return True
    


    """Adicionar quando faco upload a imagem 'a DB e adiciona la a imagem. Deve ser sequencial mandar para db, depois ir buscar 'a db.
    Quando faco render da class devo ir logo buscar a base de dados quando o user esta logged in"""

    """Quando apertar cada campo do field deve abrir outro screen e pedir para alterar nome, password, a passsword deve ser mandado email e numero deve ser mandado numero para novo numero ou entao nao muda"""