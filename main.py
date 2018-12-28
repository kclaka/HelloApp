'''
Created on Dec 28, 2018

@author: K3NN!
'''

from kivy.app import App
from kivy.uix.button import Label


class HelloApp(App):
    def build(self):
        return Label(text='Hi Kenny')


if __name__ == '__main__':
    HelloApp().run()
