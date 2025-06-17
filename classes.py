from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from pops import show_add,show_sAI_popup,show_pay
class Trywid(BoxLayout):
    ''' Add selection support to the Label '''
    name=ObjectProperty('')
    no_text=ObjectProperty('')
    def __init__(self,id=None,price=79,**kwargs):
	       super(Trywid , self).__init__(**kwargs)
	       self.product_data={'name':self.name,'price':price}
	       if id == None:
		       self.id_label=Label(text='no',size_hint=(0.125,1))
		       self.add_widget(self.id_label)
		       self.label=Label(text=self.product_data['name'],size_hint_x=2.395)
		       self.add_widget(self.label)
		       self.price='price'
		       self.coun=TextInput(text='1',size_hint=(1,1),multiline=False,on_text_validate=self.mult)
		       self.add_widget(self.coun)
		       self.pice_price=Label(text=str(self.product_data['price']),size_hint=(1,1))
		       self.add_widget(self.pice_price)
		       self.vat=Label(text=str((0.15)*self.product_data['price']),size_hint=(1,1))
		       self.add_widget(self.vat)
		       self.total=Label(text=str((1.15)*self.product_data['price']),size_hint=(1,1))
		       self.add_widget(self.total)
		       self.add_widget(Button(text='delet',size_hint=(1,1),on_release=self.delete_item))
    def mult(self,tec):
    	open('t.txt','w',encoding='utf-8').write(str(tec))
    	self.price=str(float(self.coun.text)*(self.product_data['price'])).split('.')[0]+'.'+str(float(self.coun.text)*(self.product_data['price'])).split('.')[1][:3]
    	self.vat.text=str(float(self.coun.text)*(0.15)*self.product_data['price']).split('.')[0]+'.'+str(float(self.coun.text)*(0.15)*self.product_data['price']).split('.')[1][:3]
    	self.total.text=str(float(self.coun.text)*(1.15)*self.product_data['price']).split('.')[0]+'.'+str(float(self.coun.text)*(1.15)*self.product_data['price']).split('.')[1][:3]

    def delete_item(self, instance):
        ''' دالة لحذف العنصر '''
        parent = self.parent  # الحصول على الوالد (المجموعة التي تحتوي العنصر)
        if parent:
            parent.remove_widget(self)  # حذف العنصر من الوالد

class TrywidFinal(BoxLayout):
	def __init__(self,id=None,product_data={'name':'very expensive','price':79},**kwargs):
	       super(TrywidFinal, self).__init__(**kwargs)
	       if True:
		       self.add_widget(Button(text='voice\n command  ',size_hint=(1,1),on_release=show_sAI_popup))
		       self.add_widget(Button(text='add',on_release=show_add,size_hint=(1,1)))
		       self.add_widget(Label(text='total\n without\n vat',size_hint=(1,1)))
		       self.add_widget(Label(text='vat',size_hint=(1,1)))
		       self.add_widget(Label(text='total with vat',size_hint=(1,1)))
		       self.add_widget(Button(text='pay',size_hint=(1,1),on_release=show_pay))
	def delete_item(self, instance):
		''' دالة لحذف العنصر '''
		parent = self.parent.reset()  # الحصول على الوالد (المجموعة التي تحتوي العنصر)
		if parent:
			parent.clean_up()  # حذف العنصر من الوالد

class MyApp(App):
	pass

if __name__ == '__main__':
    MyApp().run()