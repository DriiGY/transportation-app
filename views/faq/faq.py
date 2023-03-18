from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.label import Label
from kivymd.icon_definitions import md_icons
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
import json
import os

FAQ_DIR = os.path.dirname(os.path.abspath(__file__))
Builder.load_file('views/faq/faq.kv')


class Faq(BoxLayout):
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        self.questions = []
        self.answers = []
        Clock.schedule_once(self.render, .1)
    # def on_start(self):
    #     for name_tab in list(md_icons.keys())[15:30]:
    #         self.root.ids.tabs.add_widget(Tab(icon=name_tab, title=name_tab))
    # def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
    #         instance_tab.ids.label.text = tab_text
    def render(self, _):
        path = FAQ_DIR + "/data_topics.json"
        f = open(path)
        data = json.load(f)
        j=0
        for i in data['faqs']:
            topic = TopicQuestion(topic=i['topic'],)
            self.ids.base_for_topics.add_widget(topic)
            id=i["id"]
            
            self.ids[id] = topic
            for j in range(0, len(i["questions"])):
                self.questions.append(i["questions"][j])
                self.answers.append(i["answers"][j])
                self.ids[id].add_widget(Question(
                    question=i["questions"][j],
                    answer=i["answers"][j]
                ))
           
     
        # print(self.ids.base_for_topics.children)
        # print(self.ids.search_bar.ids)
        # print()
        # print(self.ids)

        self.ids.search_bar.ids.mag_glass.bind(on_release= self.find_question)
        f.close()
        
    def find_question(self, *args ):
        word = str(self.ids.search_bar.ids.search_field.text).lower()
        questions = self.questions
        answers = self.answers
        wid = self.ids.base_for_topics
        lookup_box = self.ids.lookup_questions
        try:
            #matching has all the indexes of questions list that match the word searched 
            if len(word)>0:
                matching = [i for i in range(0,len(questions)) if word in questions[i].lower()] # gives indexed of questions in self.questions
                #print(questions[matching[0]], answers[matching[0]], matching)
                wid.opacity, wid.disabled,wid.size_hint_y , wid.height = 0,True, None,0
                #print(matching)
                #lookup_box = self.ids.lookup_questions
                x =0
                for ind in matching:
                    question = Question(question=self.questions[ind], answer=self.answers[ind])
                    id = "lookup_question_{}".format(x)
                    self.ids[id] = question
                    lookup_box.add_widget(question)
                    x+=1
                for id in self.ids:
                    #print(id)
                    if "not_found_label" in id:
                        self.ids.lookup_questions.remove_widget(self.ids[id])
                lookup_box.opacity = 1
               
                lookup_box.size_hint_y = None
                lookup_box.height = self.ids.lookup_questions.minimum_height
                lookup_box.disabled = False
                self.ids.search_bar.disabled = True
                
                
                #print(self.ids)
            else:
                #print("Not foundddd")
                wid.opacity, wid.disabled,wid.size_hint_y , wid.height = 0,True, None,0
                lookup_box.add_widget(Label(text="Not Found", color=[0,0,0,1]))

                lookup_box.opacity = 1
                
                lookup_box.size_hint_y = None
                lookup_box.height = self.ids.lookup_questions.minimum_height
                lookup_box.disabled = False
                self.ids.search_bar.disabled = True
        except:
            #print("Not found!")
            wid.opacity, wid.disabled,wid.size_hint_y , wid.height = 0,True, None,0
            label = Label(text="Not Found", color=[0,0,0,1])
            id = "not_found_label"
            self.ids[id] = label
            lookup_box.add_widget(label)
            lookup_box.opacity = 1
           
            lookup_box.size_hint_y = None
            lookup_box.height = self.ids.lookup_questions.minimum_height
            lookup_box.disabled = False
            self.ids.search_bar.disabled = True
        # print(self.questions)
        # print(self.answers)
    def close_lookup_box(self):
        
        for id in self.ids:
            #print(id)
            if "lookup_question_" in id:
                self.ids.lookup_questions.remove_widget(self.ids[id])

        lookup_wid = self.ids.lookup_questions
        lookup_wid.opacity, lookup_wid.disabled,lookup_wid.size_hint_y , lookup_wid.height  = 0, True, None, 0

        base = self.ids.base_for_topics
        base.opacity, base.disabled, base.size_hint_y , base.height= 1,False,None, self.ids.base_for_topics.minimum_height

        self.ids.search_bar.disabled = False
        

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
    id = StringProperty("")
    topic = StringProperty("")


"""
Note:
    Add scrollview to FAQS
    while search bar is activated should search for what is being searched every 2 secs? id of textfield in searchbar :search_field
    """
