from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons

Builder.load_file('views/faq/faq.kv')


class Faq(BoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
    # def on_start(self):
    #     for name_tab in list(md_icons.keys())[15:30]:
    #         self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab))
    # def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
    #         instance_tab.ids.label.text = tab_text


    ####
    #feedback vai ser uma caixa de texto para mandar um email dando feedback
    #pode ter comentarios de users anteriores
    def min_max_answer(self, ):
        if self.ids.min_max_close.icon == "arrow-down-drop-circle-outline":
            self.ids.min_max_close.icon = "arrow-up-drop-circle-outline"
            self.ids.answer_text.shorten = False
            self.ids.answer_text.halign = "left"
            self.ids.answer_text.text_size = (self.ids.answer_text.width, None)
            self.ids.answer_text.size_hint = (1, None)
            self.ids.answer_text.height = self.ids.answer_text.texture_size[1]
            self.ids.answer_text.opacity = 1
            self.ids.answer_text_box.size_hint = (1, None)
            self.ids.answer_text_box.height = self.ids.answer_text.texture_size[1]
            self.ids.answer_text_box.opacity = 1
        else:
            self.ids.min_max_close.icon = "arrow-down-drop-circle-outline"
            self.ids.answer_text.height = 0
            self.ids.answer_text.opacity = 0
            self.ids.answer_text_box.height = 0
            self.ids.answer_text_box.opacity = 0

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    pass

