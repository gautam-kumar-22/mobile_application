import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import pyautogui
import time

import threading
kivy.require('1.9.0')


class MyWindowApp(App):
	def __init__(self):
	    super(MyWindowApp, self).__init__()
	    self.btn = Button(text= "START")
	    self.btn.font_size = 50
	    self.btn.background_color = (0,255,0,1)
	    self.status = "START"

	    self.btn2 = Button(text= "STOP")
	    self.btn2.font_size = 50
	    self.btn2.background_color = (0,255,0,1)
	    self.status2 = "START"

	def build(self):
	    self.btn.bind(on_press=self.clk)
	    self.btn2.bind(on_press=self.stop_click)
	    layout = BoxLayout()
	    layout.orientation = 'vertical'
	    layout.add_widget(self.btn)
	    layout.add_widget(self.btn2)
	    return layout

	def do_something(self): 
	    print "Doing stuff..."
	    self.th = threading.Timer(1.0, self.do_something).start()
	    print "Hello, World!"
	    
	def stop_click(self, *kwargs):
		# self.root.stop.set()
		print("STOP CLICKED")
		# import pdb; pdb.set_trace()
		self.th._stop()
		App.get_running_app().stop()


	def clk(self, obj):
	    print ('I have been clicked')
	    if self.status == "START":
	        self.status = "STOP"
	        self.btn.text = "STOP"
	        self.btn.background_color = (255,0,0,1)
	        self.do_something()
	    else:
	        self.status = "START"
	        self.btn.text = "START"
	        self.btn.background_color = (0,255,0,1)


window = MyWindowApp()
window.run()

