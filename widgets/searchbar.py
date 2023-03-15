from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(
'''
# #:import images_path kivymd.images_path

<SearchBar>:
    canvas.before:
        Color:
            rgba:[0,0,0,0]
        Rectangle:
            pos:self.pos
            size:self.size
    size_hint_y: None
    height: self.minimum_height
  
    MDIconButton:
        id:mag_glass
        icon: 'magnify'
    
    MDTextField:
        id: search_field
        hint_text: 'Search most asked'
    
       


 '''
 )
# <SearchBar>:

    
#     canvas.before:
#         Color:
#             rgba:[0,0,0,0]
#         Rectangle:
#             pos:self.pos
#             size:self.size
#     orientation: 'vertical'
#     spacing: dp(10)
#     padding: dp(20)


# on_text: root.set_list_md_icons(self.text, True)
# RecycleView:
#     id: rv
#     key_viewclass: 'viewclass'
#     key_size: 'height'

#     RecycleBoxLayout:
#         padding: dp(10)
#         default_size: None, dp(48)
#         default_size_hint: 1, None
#         size_hint_y: None
#         height: self.minimum_height
#         orientation: 'vertical'

class SearchBar(BoxLayout):
    pass
    # def set_list_md_icons(self, text="", search=False):
    #     '''Builds a list of icons for the screen MDIcons.'''
    #     for name_icon in md_icons.keys():
    #         if search:
    #             if text in name_icon:
    #                 self.add_icon_item(name_icon)
    #         else:
    #             self.add_icon_item(name_icon)

    # def add_icon_item(self,name_icon):
    #     self.ids.rv.data.append(
    #         {
    #             "viewclass": "CustomOneLineIconListItem",
    #             "icon": name_icon,
    #             "text": name_icon,
    #             "callback": lambda x: x,
    #         }
    #     )

    #     self.ids.rv.data = []
    
    


# class MainApp(MDApp):
#   def __init__(self, **kwargs):
#      super().__init__(**kwargs)
#      self.screen = PreviousMDIcons()

#   def build(self):
#       return self.screen

#   def on_start(self):
#       #self.screen.set_list_md_icons()
#       pass


# MainApp().run()