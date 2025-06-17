from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty,ObjectProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from classes import *
from pops import *
import logging
from scanner import barcode_reader
from kivy.uix.dropdown import DropDown
class CustomDropDown(DropDown):
    pass

Builder.load_string('''
<Mains>: 
	height: "120 dp"
	size_hint_y : None
	orientation:'vertical'
	BoxLayout:
		Button:
			text:'Invoice'
			on_release:root.sh_popup()
		Button:
			text:'Store'
			on_release:root.show_my_store()
		Button:
			text:'product'
			on_release:root.show_product()
		Button:
			text:'my AI'
			on_release:root.show_AI_popup()
	BoxLayout:
		Label:
			text:'id'
		Label:
			text:'Prouduct'
		Label:
			text:'pice price'
		Label:
			text:'total vat'
		Label:
			text: 'total price'
		Button:
			text:'clearall'
			on_release:root.emp()
			
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True
<TrywidFinal>:
	height: "125 dp"
	size_hint_y : None
''')

#apply=lambda s:s
class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
	pass

class SelectableLabel(RecycleDataViewBehavior, Trywid):
	def __init__(self,**kwargs):
	       super(SelectableLabel , self).__init__(**kwargs)
	       self.index = None
	       self.selected = BooleanProperty(False)
	       self.selectable = BooleanProperty(False)

	def refresh_view_attrs(self, rv, index, data):
		self.index = index
		if rv.parent.parent.head.tell:
			rv.data=[]
			rv.parent.emptyed()
		else:
			self.id_label.text= f"{data['no_text']}"
			self.label.text = f"{data['name']}"
		return super(SelectableLabel, self).refresh_view_attrs(
	            rv, index, data)

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'no_text': str(x),'name':str(f'kind {x}')} for x in range(30)]
    def reset(self):
        self.data=[]

class Mains(BoxLayout):
	show_product=show_product
	sh_popup=sh_popup
	show_my_store=show_my_store
	show_AI_popup=show_AI_popup
	data = [{'no_text': str(x),'name':str(f'kind {x}')} for x in range(10)]
	tell=False
	def emp(self):
		self.parent.parent.Rec.data=[]
	def run_out(self):
		self.tell=True
	def emptyed(self):
		self.tell=False
class TheApp(BoxLayout):
	core=BoxLayout(orientation='vertical')
	head=Mains()
	Rec=RV()
	fot=TrywidFinal()
	def __init__(self,**kwargs):
	       super(TheApp, self).__init__(**kwargs)
	       self.orientation='vertical'
	       self.core.add_widget(self.head)
	       self.core.add_widget(self.Rec)
	       self.core.add_widget(self.fot)
	       self.add_widget(self.core)
class TestyApp(App):
	def build(self):
		return TheApp()
        
 
RV(**{ 'viewclass': 'SelectableLabel'})
if __name__ == '__main__':
    TestyApp().run()