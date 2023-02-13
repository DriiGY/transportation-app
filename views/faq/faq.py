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


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    pass

