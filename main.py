from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import math
import re
Builder.load_file("cal.kv")

class MyLayout(Widget):
    def clear(self):
        self.ids.text_input.text="0"
    def squ(self):
        inText=self.ids.text_input.text
        try:
            sq=math.sqrt(float(inText))
            self.ids.text_input.text=f"{sq}"
        except:
            self.ids.text_input.text="Error"

    def pressen(self):
        inText=self.ids.text_input.text
        try:
            k=re.split(pattern=r"[\+\-\/\*\%]",string=inText)
            revv=inText[::-1]
            kk=re.split(pattern=r"[\+\-\/\*]",string=revv, maxsplit=2)
            gh=kk[len(kk)-1]
            final=inText[:len(gh)+1]
            i=len(k)
            
            add= len(k[i-2])+len(k[i-1])
            if len(kk)==2:
                if "+" in str(inText[len(inText)-add:]):
                    ll=float(k[i-2])+((float(k[i-2])*(float(k[i-1]))/100))
                    self.ids.text_input.text=f"{ll}"
                elif "-" in str(inText[len(inText)-add:]):
                    ll=float(k[i-2])-float(k[i-2])*(float(k[i-1])/100)
                    self.ids.text_input.text=f"{ll}"
            elif len(kk)>2:
                if "+" in str(inText[len(inText)-add:]):
                    #ol=(float(k[i-2])*(float(k[i-1]))/100)
                    ll=float(k[i-2])+((float(k[i-2])*(float(k[i-1]))/100))
                    self.ids.text_input.text=f"{final}{ll}"
                elif "-" in str(inText[len(inText)-add:]):
                    ll=float(k[i-2])-float(k[i-2])*(float(k[i-1])/100)
                    self.ids.text_input.text=f"{final}{ll}"
                else:
                    ll=float(k[i-2])*(float(k[i-1])/100)
                    self.ids.text_input.text=f"{ll}"
            else:
                lol=float(inText)/100
                self.ids.text_input.text=f"{lol}"
        except:
            self.ids.text_input.text="Error"
    def AbChange(self):
        inText=self.ids.text_input.text
        if f"{inText[0]}"=="-":
            self.ids.text_input.text=f"{inText[1:]}"
        else:
            self.ids.text_input.text=f"-{inText}"
    def clear_last(self):
        inText=self.ids.text_input.text
        kl=len(inText)
        self.ids.text_input.text=f"{inText[0:kl-1]}"
    def press(self,button):
        inText=self.ids.text_input.text
        if inText=="0":
            self.ids.text_input.text=""
            self.ids.text_input.text=f"{button}"
        else:
            self.ids.text_input.text=f"{inText}{button}"

    def result(self):
        inText=self.ids.text_input.text
        try:
            kl=eval(inText)
            self.ids.text_input.text=f"{kl}"
        except:
            self.ids.text_input.text="Error"
class CalculatorApp(App):
    def build(self):
        return MyLayout()
if __name__=="__main__":
    CalculatorApp().run()