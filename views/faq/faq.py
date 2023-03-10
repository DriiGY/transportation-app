from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty

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
 

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    pass

class Question(BoxLayout):
    '''Question to be added to each topic in FAQ'''
    question = StringProperty("")
    answer = StringProperty("")
    def min_max_answer(self, button, answer_id, answer_box_id):
        # print(button)
        # print(answer_id.text)
        if button.icon == "arrow-down-drop-circle-outline":
            button.icon = "arrow-up-drop-circle-outline"
            answer_id.shorten = False
            answer_id.halign = "left"
            answer_id.text_size = (answer_id.width, None)
            answer_id.size_hint = (1, None)
            answer_id.height = answer_id.texture_size[1]
            answer_id.opacity = 1
            answer_box_id.size_hint = (1, None)
            answer_box_id.height = answer_id.texture_size[1]
            answer_box_id.opacity = 1
        else:
            button.icon = "arrow-down-drop-circle-outline"
            answer_id.height = 0
            answer_id.opacity = 0
            answer_box_id.height = 0
            answer_box_id.opacity = 0

class TopicQuestion(BoxLayout):
    '''Topic to be added to FAQ'''
    topic = StringProperty("")


"""
Note:
    Add scrollview to FAQS

    """
