import calendar
from datetime import datetime
from pprint import PrettyPrinter
from tokenize import String

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict, get_random_color
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty, NumericProperty, ColorProperty, BooleanProperty

from widgets.labels import Text
from widgets.buttons import RoundedButton, CircleButton

Builder.load_string("""
#: import IconButton widgets.buttons.IconButton
#: import RoundedButton widgets.buttons.RoundedButton
#: import Text widgets.labels.Text
#: import ShadowBox widgets.shadow.ShadowBox

<MiniCalender>:
    orientation: 'vertical'
    padding: dp(8)
    spacing: dp(8)
    BoxLayout:
        size_hint_y: None
        height: dp(32)
        spacing: dp(8)
        AnchorLayout:
            size_hint_x: None
            width: self.height
            padding: dp(8)
            FlatButton:
                text: icon("icon-chevron-left")
                font_size: app.fonts.size.h1
                color: app.colors.primary
        BoxLayout:
            Text:
                text: root.title + " " + str(root.year)
                halign: 'center'
                color: app.colors.primary
        AnchorLayout:
            size_hint_x: None
            width: self.height
            padding: dp(8)
            FlatButton:
                text: icon("icon-chevron-right")
                font_size: app.fonts.size.h1
                color: app.colors.primary
    GridLayout:
        id: cal_keys
        rows: 1
        spacing: dp(4)
        size_hint_y: None
        height: dp(32)
    GridLayout:
        id: cal_data
        cols: 7
        spacing: dp(4)
""")
class MiniCalender(BoxLayout):
    tc = calendar.TextCalendar(firstweekday=calendar.SUNDAY)
    title = StringProperty("March")
    calender_keys = ListProperty([])
    year = NumericProperty(2022)
    month = NumericProperty(3)
    day_entries = ListProperty([])
    day_title = StringProperty("")
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        self.btn_size = 0.0
        Clock.schedule_once(self.render, .1)
        self.bind(size=self.update_sizes)
        self.today = datetime.now()

    def render(self, _):
        self.calender_keys = ['SUN', 'MON', 'TUE', 'WED', 'THUR', 'FRI', 'SAT']

        self.ids.cal_keys.clear_widgets()
        for k in self.calender_keys:
            key = Text()
            key.halign = "center"
            key.font_size = sp(10)
            key.text = k
            key.color = App.get_running_app().colors.black

            self.ids.cal_keys.add_widget(key)
        
        month = self.get_month(4)
        self.month = 4
        self.refresh_calender(month, type='month')
    
    def update_sizes(self, *args):
        for c in self.ids.cal_data.children:
            c = c.children[0]
            c.size_hint_x = None
            c.width = self.width*.08
            c.height = c.width
            c.radius = [c.height]
            self.btn_size = c.width


    def on_day_entries(self, *args):
        pass

    def change_month(self, next=True):
        if next:
            if self.month == 12:
                self.year += 1
                self.month = 1
            else:
                self.month += 1
        else:
            if self.month == 1:
                self.year -= 1
                self.month = 12
            else:
                self.month -= 1

        month = self.get_month(self.month)
        Clock.schedule_once(lambda x: self.refresh_calender(month), .2)

    def refresh_calender(self, data, type='month'):
        grid = self.ids.cal_data
        grid.clear_widgets()

        if type == 'month':
            grid.cols = 7
            grid.rows = 8
            self.title = data['month_str'].split(" ")[0].strip()

            # Fill Missing Values With Previous Month Days
            first_week = data['weeks'][0]
            empties = 0
            for f in first_week:
                if f == '':
                    empties += 1

            if empties > 0:
                prev_month = self.get_month(max(1, self.month-1))
                last_week = prev_month['weeks'][-1][:empties]

                for i, l in enumerate(last_week):
                    first_week[i] = l
                data['weeks'][0] = first_week
            
            # Fill Missing values With Next Month Values
            last_week = data['weeks'][-1]
            rempties = 0
            for f in last_week:
                if f == '':
                    rempties += 1

            if rempties > 0:
                next_month = self.get_month(min(12, self.month+1))
                first_week = next_month['weeks'][0][(7-rempties):]

                first_week = list(reversed(first_week))
                for i, l in enumerate(first_week):
                    last_week[6-i] = l

            dayx = 0
            prev = 0

            for week in data['weeks']:
                for day in week:

                    anchor = AnchorLayout()
                    ce = CircleButton()
                    ce.font_size = App.get_running_app().fonts.size.h6
                    anchor.add_widget(ce)

                    if self.btn_size > 8:
                        ce.size_hint_x = None
                        ce.width = self.width*.08
                        ce.height = ce.width
                    # ce.size_hint = [None, None]
                    # ce.height = dp(64)
                    ce.color = App.get_running_app().colors.black
                    ce.bcolor = [1,1,1,1]

                    dy = self.today.day
                    mnth = self.today.month
                    yr = self.today.year


                    if day != '':
                        day = str(day).zfill(2)
                        if dayx < empties:
                            ce.active = False
                        else:
                            if prev > 27 and int(day) < 28:
                                ce.active = False
                            prev += 1
                    else:
                        ce.active = False

                    ce.text = day
                    if dy == int(day) and mnth == self.month and yr == self.year:
                        ce.bcolor = App.get_running_app().colors.tertiary
                        ce.color = App.get_running_app().colors.white

                    grid.add_widget(anchor)
                    dayx += 1
    
    def view_day(self, day):
        self.day_entries = day.entries
        self.day_title = "%s %s %s"%(self.month, day.text, self.year)
        self.ids.scrn_mngr.current = 'scrn_day'

    def get_month(self, month):
        """
                March 2022
            Mo Tu We Th Fr Sa Su
                1  2  3  4  5  6
            7  8  9 10 11 12 13
            14 15 16 17 18 19 20
            21 22 23 24 25 26 27
            28 29 30 31
        """

        month = self.tc.formatmonth(self.year, month)

        data = month.split("\n")
        weeks = data[2:-1]
        
        weeks = [x.strip() for x in weeks]
        last = weeks[-1]
        first = weeks[0]
        while len(first) < 20:
            first = " "+first
        while len(last) < 20:
            last += ' '

        weeks[0] = first
        weeks[-1] = last
        weeks = [x.replace("  ", ',').replace(" ", ",") for x in weeks]

        weeks = [x.split(",") for x in weeks]
        first = reversed(list(reversed(weeks[0]))[0:7])
        last = weeks[-1][0:7]
        weeks[0] = list(first)
        weeks[-1] = last

        return {'month_str': data[0].strip(), 'weeks': weeks}