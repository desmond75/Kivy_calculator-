
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
	Window.size = (400, 280)
	#accepted_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/' , '.'] 

	def build(self):

		#self.text_input = FloatInputRight(font_size=20, size_hint_y=.05)
		b = BoxLayout(orientation='vertical')
		self.text_input = TextInput( size_hint_y=.4,
								    font_size=20, 
								    foreground_color=[1,0,0,1], 
								    #hint_text = 'Your name', 
								    hint_text_color = [0.5, 0.5, 0.5, 1.0],
								    input_filter='int'
		)

		gridlayout = GridLayout(cols=4,row_force_default=True, row_default_height=40)
		clear = Button(text='C', size_hint_x=None, width=100, background_color=(1,0,1,1))
		divide = Button(text='/', size_hint_x=None, width=100)
		multiply = Button(text='*', size_hint_x=None, width=100)
		delete = Button(text='Del', size_hint_x=None, width=100)
		seven = Button(text='7', size_hint_x=None, width=100)
		eight = Button(text='8', size_hint_x=None, width=100)
		nine = Button(text='9', size_hint_x=None, width=100)
		minus = Button(text='-', size_hint_x=None, width=100)
		four = Button(text='4', size_hint_x=None, width=100)
		five = Button(text='5', size_hint_x=None, width=100)
		six = Button(text='6', size_hint_x=None, width=100)
		plus = Button(text='+', size_hint_x=None, width=100)
		one = Button(text='1', size_hint_x=None, width=100)
		two = Button(text='2', size_hint_x=None, width=100)
		three = Button(text='3', size_hint_x=None, width=100)
		curl_brace = Button(text='()', size_hint_x=None, width=100)
		zero = Button(text='0', size_hint_x=None, width=100)
		dot = Button(text='.', size_hint_x=None, width=100)
		plus_divide_minus = Button(text='+/-', size_hint_x=None, width=100)
		equal_to = Button(text='=', size_hint_x=None, width=100)

		gridlayout.add_widget(clear)
		clear.bind(on_press=self.clear_memory)
		gridlayout.add_widget(divide)
		divide.bind(on_press=self._divide)
		gridlayout.add_widget(multiply)
		multiply.bind(on_press=self._multiply)
		gridlayout.add_widget(delete)
		delete.bind(on_press=self.delete_)
		gridlayout.add_widget(seven)
		seven.bind(on_press=self._seven)
		gridlayout.add_widget(eight)
		eight.bind(on_press=self._eight)
		gridlayout.add_widget(nine)
		nine.bind(on_press=self._nine)
		gridlayout.add_widget(minus)
		minus.bind(on_press=self._minus)
		gridlayout.add_widget(four)
		four.bind(on_press=self._four)
		gridlayout.add_widget(five)
		five.bind(on_press=self._five)
		gridlayout.add_widget(six)
		six.bind(on_press=self._six)
		gridlayout.add_widget(plus)
		plus.bind(on_press=self._add)
		gridlayout.add_widget(one)
		one.bind(on_press=self._one)
		gridlayout.add_widget(two)
		two.bind(on_press=self._two)
		gridlayout.add_widget(three)
		three.bind(on_press=self._three)
		gridlayout.add_widget(curl_brace)
		curl_brace.bind(on_press=self._curl_brace)
		gridlayout.add_widget(zero)
		zero.bind(on_press=self._zero)
		gridlayout.add_widget(dot)
		dot.bind(on_press=self._dot)
		gridlayout.add_widget(plus_divide_minus)
		plus_divide_minus.bind(on_press=self._plus_slash_minus)
		gridlayout.add_widget(equal_to)
		equal_to.bind(on_press=self._equal_to)

		b.add_widget(self.text_input)
		# self.text_input.bind(text=self.print_txt_to_console)
		# self.text_input.bind(focus=self.on_focus)

		b.add_widget(gridlayout)

		return b

	# def check_if_character_is_accepted(self, character):
	# 	if str(character) in self.accepted_characters:
	# 		return str(character)
	# 	else:
	# 		return ''

	def _seven(self,obj):
		"""Adds the current press button to the list"""
		self.text_input.text += str(7)#self.check_if_character_is_accepted('g')

	def _eight(self, obj):
		self.text_input.text += str(8)

	def _nine(self, obj):
		self.text_input.text += str(9)

	def _four(self, obj):
		self.text_input.text += str(4)

	def _five(self, obj):
		self.text_input.text += str(5)

	def _six(self, obj):
		self.text_input.text += str(6)

	def _one(self, obj):
		self.text_input.text += str(1)

	def _two(self, obj):
		self.text_input.text += str(2)

	def _three(self, obj):
		self.text_input.text += str(3)

	def _zero(self, obj):
		self.text_input.text += str(0)

	def _dot(self, obj):
		self.text_input.text += '.'

	def _plus_slash_minus(self, obj):
		self.text_input.text += str('')

	def _divide(self, obj):
		self.text_input.text += str(' / ')

	def _multiply(self, obj):
		self.text_input.text += ' * '

	def _minus(self, obj):
		self.text_input.text += ' - '

	def _add(self, obj):
		self.text_input.text += ' + '

	def _curl_brace(self, obj):
		return ''

	def _equal_to(self, obj):
	
		if len(self.text_input.text) < 1:
			self.text_input.text = ""
		else:
			try:
				self.text_input.text = str(eval(self.text_input.text))
			except Exception as e:
				print(str(e))
				self.text_input.text = 'Error'

	def delete_(self, obj):
		text = self.text_input.text
		text_len = len(self.text_input.text)
		new_text = self.text_input.text[:-1]#removes the last two text inputs
		self.text_input.text = new_text #update the new text

	def clear_memory(self, obj):
		#Deletes everything in the text_input field
		self.text_input.text = ""

if __name__ == '__main__':
	CalculatorApp().run()
