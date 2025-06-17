from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
def show_product(*args):
    # إنشاء نافذة منبثقة بسيطة
    content = BoxLayout(orientation='vertical')
    content.add_widget(Label(text="Product"))
    save_button = Button(text="add product", size_hint_y=None, height=53)
    content.add_widget(save_button)
    close_button = Button(text="modify product", size_hint_y=None, height=53)
    content.add_widget(close_button)
    for_button = Button(text="delet product", size_hint_y=None, height=53)
    content.add_widget(for_button)
    tem_button = Button(text="inter bar code manuly", size_hint_y=None, height=53)
    content.add_widget(tem_button)
    close_button = Button(text="close", size_hint_y=None, height=53)
    content.add_widget(close_button)

    popup = Popup(title='Product', content=content, size_hint=(0.5, 0.5))
    close_button.bind(on_release=popup.dismiss)
    popup.open()

def show_my_store(*args):
    # إنشاء نافذة منبثقة بسيطة
    content = BoxLayout(orientation='vertical')
    content.add_widget(Label(text="My_store"))
    save_button = Button(text="dlivary order", size_hint_y=None, height=53)
    content.add_widget(save_button)
    close_button = Button(text="worker daily's", size_hint_y=None, height=53)
    content.add_widget(close_button)
    for_button = Button(text="get analis", size_hint_y=None, height=53)
    content.add_widget(for_button)
    tem_button = Button(text="sitting", size_hint_y=None, height=53)
    content.add_widget(tem_button)
    close_button = Button(text="close", size_hint_y=None, height=53)
    content.add_widget(close_button)
    popup = Popup(title='Store Manager', content=content, size_hint=(0.5, 0.5))
    close_button.bind(on_release=popup.dismiss)
    popup.open()
def sh_popup(*args):
    # إنشاء نافذة منبثقة بسيطة
    content = BoxLayout(orientation='vertical')
    content.add_widget(Label(text="Invoice"))
    save_button = Button(text="delet", size_hint_y=None, height=53)
    content.add_widget(save_button)
    close_button = Button(text="save", size_hint_y=None, height=53)
    content.add_widget(close_button)
    for_button = Button(text="restore", size_hint_y=None, height=53)
    content.add_widget(for_button)
    tem_button = Button(text="replace", size_hint_y=None, height=53)
    content.add_widget(tem_button)
    close_button = Button(text="money back", size_hint_y=None, height=53)
    content.add_widget(close_button)
    close_button = Button(text="E_Invoice", size_hint_y=None, height=53)
    content.add_widget(close_button)
    close_button = Button(text="close", size_hint_y=None, height=53)
    content.add_widget(close_button)
    popup = Popup(title='Invoice', content=content, size_hint=(0.5, 0.5))
    close_button.bind(on_release=popup.dismiss)
    popup.open()

def show_add(*args):
    # إنشاء نافذة منبثقة بسيطة
    content = BoxLayout(orientation='vertical')
    content.add_widget(Label(text="add other product"))
    barcode=BoxLayout(size_hint_y=.3)
    bar = TextInput()
    barcode.add_widget(Label(text='inter barcode',size_hint_x=0.3))
    barcode.add_widget(bar)
    content.add_widget(barcode)
    num=BoxLayout(size_hint_y=.3)
    innum = TextInput()
    num.add_widget(Label(text='how many',size_hint_x=0.3))
    num.add_widget(innum)
    content.add_widget(num)
    done_button = Button(text="done", size_hint_y=None, height=50,size_hint_x=.5)
    content.add_widget(done_button)
    popup = Popup(title='Invoice', content=content, size_hint=(0.5, 0.5))
    done_button.bind(on_release=popup.dismiss)
    popup.open()

def show_pay(*args):
    # إنشاء نافذة منبثقة بسيطة
    content = BoxLayout(orientation='vertical')
    content.add_widget(Label(text="pay"))
    barcode=BoxLayout(size_hint_y=.3)
    bar = TextInput()
    barcode.add_widget(Label(text='total money',size_hint_x=0.3))
    barcode.add_widget(bar)
    content.add_widget(barcode)
    num=BoxLayout(size_hint_y=.3)
    innum = Label()
    num.add_widget(Label(text='back',size_hint_x=0.3))
    num.add_widget(innum)
    content.add_widget(num)
    contents = BoxLayout()
    done_button = Button(text="pay", size_hint_y=None, height=50,size_hint_x=.5)
    contents.add_widget(done_button)
    card=Button(text='pay with card', size_hint_y=None, height=50,size_hint_x=.5)
    contents.add_widget(card)
    close=Button(text='close', size_hint_y=None, height=50,size_hint_x=.5)
    contents.add_widget(close)
    content.add_widget(contents)
    popup = Popup(title='Invoice', content=content, size_hint=(0.5, 0.5))
    done_button.bind(on_release=popup.dismiss)
    card.bind(on_release=popup.dismiss)
    close.bind(on_release=popup.dismiss)
    popup.open()

def show_sAI_popup(*args):
    # إنشاء نافذة منبثقة بسيطة
    content = BoxLayout(orientation='vertical')
    icon=Image(source='Ok.jpg',size_hint_y=None,height=370)
    content.add_widget(icon)
    close_button = Button(text="close", size_hint_y=None, height=53)
    content.add_widget(close_button)

    popup = Popup(title='INVOICE', content=content, size_hint=(0.5, 0.5))
    close_button.bind(on_release=popup.dismiss)
    popup.open()
def show_AI_popup(*args):
    # إنشاء نافذة منبثقة بسيطة
    content = BoxLayout(orientation='vertical')
    content.add_widget(Label(text="Invoice"))
    save_button = Button(text="teach model", size_hint_y=None, height=53)
    content.add_widget(save_button)
    close_button = Button(text='AI sitting', size_hint_y=None, height=53)
    content.add_widget(close_button)
    close_button = Button(text="close", size_hint_y=None, height=53)
    content.add_widget(close_button)

    popup = Popup(title='INVOICE', content=content, size_hint=(0.5, 0.5))
    close_button.bind(on_release=popup.dismiss)
    popup.open()