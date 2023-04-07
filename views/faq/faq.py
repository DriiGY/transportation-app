from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.label import Label
from widgets.box import BackBox
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import rgba
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock
import json
import os

#Clock.max_iteration = 50  # changed clock iteration on app/__init__.py. Works but should be properly fixed.
FAQ_DIR = os.path.dirname(os.path.abspath(__file__))
Builder.load_file('views/faq/faq.kv')


class ReviewContent(BoxLayout, ButtonBehavior):
    stars = NumericProperty(0)
    """Review dialog box content"""
    def on_click_star(self, id, *args):
        #print(id)
        if id == "star1":
            self.ids["star1"].icon = "star"
            self.ids["star2"].icon = self.ids["star3"].icon = self.ids["star4"].icon = self.ids["star5"].icon = "star-outline"
            ReviewContent.stars = 1
        if id == "star2":
            self.ids["star1"].icon = self.ids["star2"].icon = "star"
            self.ids["star3"].icon = self.ids["star4"].icon = self.ids["star5"].icon = "star-outline"
            ReviewContent.stars = 2
        if id == "star3":
            self.ids["star1"].icon = self.ids["star2"].icon = self.ids["star3"].icon = "star"
            self.ids["star4"].icon = self.ids["star5"].icon = "star-outline"
            ReviewContent.stars = 3
        if id == "star4":
            self.ids["star1"].icon = self.ids["star2"].icon = self.ids["star3"].icon = self.ids["star4"].icon = "star"
            self.ids["star5"].icon = "star-outline"
            ReviewContent.stars = 4
        if id == "star5":
            self.ids["star1"].icon = self.ids["star2"].icon = self.ids["star3"].icon = self.ids["star4"].icon = self.ids["star5"].icon = "star"
            ReviewContent.stars = 5



class Faq(BoxLayout):
    dialog = None
    dicard_dialog = None
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        self.questions = []
        self.answers = []
        Clock.schedule_once(self.render, .5)
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
            if len(word)>2:
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
                #toast("Not found")
                
                #print(self.ids)
            else:
                #print("Not foundddd")
                # wid.opacity, wid.disabled,wid.size_hint_y , wid.height = 0,True, None,0
                # lookup_box.add_widget(Label(text="Not Found", color=[0,0,0,1]))

                # lookup_box.opacity = 1
                
                # lookup_box.size_hint_y = None
                # lookup_box.height = self.ids.lookup_questions.minimum_height
                # lookup_box.disabled = False
                # self.ids.search_bar.disabled = True
                pass
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
    
    def show_review_dialog(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Review: Helps us improve your experience!", 
                type="custom",
                content_cls=ReviewContent(),
                buttons=[
                    MDRaisedButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=rgba("#ffffff"),
                        md_bg_color="grey",
                        on_release=self.closeDialog
                    ),
                    MDRaisedButton(
                        text="REVIEW",
                        theme_text_color="Custom",
                        text_color=rgba("#ffffff"),
                        md_bg_color=rgba("#6167E9"),
                        font_style="Button",
                        on_release=self.submitReview
                    ),
                ]
            )
        self.dialog.open()
    
    def submitReview(self, *args):
        print("YOU NEED TO CREATE A SUBMIT FORM!!!!")
        # self.dialog.content_cls.ids gets all ids
        #print(self.dialog.content_cls.stars)
        #add new review by creating ReviewCard()

    def closeDialog(self, *args):
        self.dialog.dismiss()
        if not self.dicard_dialog:
            self.dicard_dialog = MDDialog(
            title="Discard?", 
            type="custom",
            buttons=[
                MDRaisedButton(
                    text="Yes",
                    theme_text_color="Custom",
                    text_color=rgba("#ffffff"),
                    md_bg_color="grey",
                    on_release=self.closeDiscardDialog
                ),
                MDRaisedButton(
                    text="No",
                    theme_text_color="Custom",
                    text_color=rgba("#ffffff"),
                    md_bg_color=rgba("#6167E9"),
                    font_style="Button",
                    on_release=self.saveReview
                ),
            ]
            )
        self.dicard_dialog.open()
        
    
    
    def closeDiscardDialog(self, *args):
        self.dialog.content_cls.ids["star1"].icon = self.dialog.content_cls.ids["star2"].icon = self.dialog.content_cls.ids["star3"].icon  = \
        self.dialog.content_cls.ids["star4"].icon = self.dialog.content_cls.ids["star5"].icon = "star-outline"
        self.dialog.content_cls.ids["review_text"].text = ""
        self.dicard_dialog.dismiss()
    
    def saveReview(self, *args):
        self.dicard_dialog.dismiss()

 

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


class StarBar(BoxLayout):
    total_stars = NumericProperty(1)
    stars = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #StarBar.total_stars = 100  # Initiate from data here!! request api

class ReviewCard(BackBox):
    profile_pic = StringProperty("assets/imgs/unknown_pic.png")
    name = StringProperty("Anonymous")
    stars = ListProperty([1,1,1,2,0])  # 0 empty star, 1 full star, 2 half-star
    date = StringProperty("dd/mm/yy")
    review_text = StringProperty("")
    menu = None
    def open_dropdown_dots(self):
       
        items_d = ['flag']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "height": dp(40),
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in items_d
        ]
        
        fots_flag_button = self.ids["dots_flag"]
        if not self.menu:
            self.menu = MDDropdownMenu(
                caller=fots_flag_button,
                items=menu_items,
                width_mult=2,
            )
        self.menu.open()

    def menu_callback(self, text_item):
        """Acts on release flag button, DOESN'T DO ANYTHING"""
        #print(text_item)
        self.menu.dismiss()

    def which_star(self, value, *args):
        if value == 1:
            return "star"
        elif value == 2 :
            return "star-half-full" 
        else:
            return "star-outline" 
    
    def helpful_question_yes(self, *args):
        self.ids["no"].text_color = rgba("#616161")
        self.ids["no"].line_color = rgba("#444444")
        self.ids["yes"].text_color = rgba("#0F9D58")
        self.ids["yes"].line_color = rgba("#0F9D58")

    def helpful_question_no(self, *args):
        self.ids["no"].text_color = [1,0,0,1]
        self.ids["no"].line_color = [1,0,0,1]
        self.ids["yes"].text_color = rgba("#616161")
        self.ids["yes"].line_color = rgba("#444444")
    
    
    
    
    
    
    
    
    
    """
Note:

    feedback deve ter estrelas uma caixa de texto com um dropdown sobre do que fala o feedback:
    improve, experience,...
    o feedback deve ter o nome e imagem do user??????
    ver examplo playstore e cada app.
    # Limit to 250 characters when creating review



    Change color of reviewcard helppful button and add vote to DB
    Add to 3 point button flag option
    """
