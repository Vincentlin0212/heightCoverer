#!/usr/bin/env python

import wx

class HightFrame(wx.Frame):
	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Height Coverer")
		
		self.panel = wx.Panel(self)
		
		self.prompt = wx.StaticText(self.panel, label="Enter your name:", pos=(40, 10))
		
		self.nameBox = wx.TextCtrl(self.panel, pos=(200, 10))
		
		self.ShowIandF = wx.CheckBox(self.panel, label='From inches and feet to centimeter', pos=(20, 30))
		self.ShowIandF.SetValue(False)
		self.ShowIandF.Bind(wx.EVT_CHECKBOX, self.OnToggleShowIandF)
		
		self.ShowT = wx.CheckBox(self.panel, label='From centimeter to inches and feet', pos=(20, 50))
		self.ShowT.SetValue(False)
		self.ShowT.Bind(wx.EVT_CHECKBOX, self.OnToggleShowT)
		
		self.Show()
		
		
		# First one:
		self.prompt2 = wx.StaticText(self.panel, label="Inches:", pos=(40, 80))
		self.inchesBox = wx.TextCtrl(self.panel, pos=(100, 80))
		
		self.prompt3 = wx.StaticText(self.panel, label="Feet:", pos=(40, 110))
		self.feetBox = wx.TextCtrl(self.panel, pos=(100, 110))
		

		self.response = wx.StaticText(self.panel, pos=(40, 350))
		
		self.btnSubmitIandF = wx.Button(self.panel, label="Submit", pos=(150, 140))
		self.btnSubmitIandF.Bind(wx.EVT_BUTTON, self.OnSubmitIandF)
		
		
		# The next one:
		
		self.prompt4 = wx.StaticText(self.panel, label="Tall(cm):", pos=(40, 180))
		self.tallBox = wx.TextCtrl(self.panel, pos=(100, 180))
		
		self.btnSubmitT = wx.Button(self.panel, label="Submit", pos=(150, 210))
		self.btnSubmitT.Bind(wx.EVT_BUTTON, self.OnSubmitT)
		
		self.response2 = wx.StaticText(self.panel, pos=(40, 380))
		
		self.prompt2.Show(False)
		self.inchesBox.Show(False)
		self.prompt3.Show(False)
		self.feetBox.Show(False)
		self.response.Show(False)
		self.btnSubmitIandF.Show(False)
		self.prompt4.Show(False)
		self.tallBox.Show(False)
		self.btnSubmitT.Show(False)
		self.btnSubmitT.Show(False)
		self.response2.Show(False)


	def OnSubmitIandF(self, e):
		name = self.nameBox.GetValue()
		feet = int(self.feetBox.GetValue())
		inches = int(self.inchesBox.GetValue())
		tall = feet * 2.54 + inches * 30.48
		if feet >= 12:
			newfeet = feet % 12
			inch = (feet - newfeet)/12
			newinches = inches + inch
			self.feetBox.SetValue(str(newfeet))
			self.inchesBox.SetValue(str(newinches))
			wx.MessageBox("Feet can't be bigger than 12, I help you translate it to inches.", "Info", wx.CANCEL)
		if len(name) > 0:
			self.response.SetLabel("Hi {}, you are {}cm tall.".format(name, tall))
		else:
			self.nameBox.SetValue("Secret Human")
			self.OnSubmitIandF(None)
			wx.MessageBox("Hey, you didn't enter a name! I will call you \"Secret Human\"", "Info", wx.CANCEL)
			
	def OnSubmitT(self, e):
		name = self.nameBox.GetValue()
		tall = int(self.tallBox.GetValue())
		left = tall % 30.48
		feet = round(left / 2.54, 2)
		inches = (tall - left)/30.48
		if len(name) > 0:
			self.response2.SetLabel("Hi {}, you are {}inches and {}feet tall.".format(name, inches, feet))
		else:
			self.nameBox.SetValue("Secret Human")
			self.OnSubmitT(None)
			wx.MessageBox("Hey, you didn't enter a name! I will call you \"Secret Human\"", "Info", wx.CANCEL)
	
	def OnToggleShowIandF(self, e):
		isChecked = self.ShowIandF.GetValue()
		if isChecked:
			self.prompt2.Show(True)
			self.inchesBox.Show(True)
			self.prompt3.Show(True)
			self.feetBox.Show(True)
			self.response.Show(True)
			self.btnSubmitIandF.Show(True)
		else:
			self.prompt2.Show(False)
			self.inchesBox.Show(False)
			self.prompt3.Show(False)
			self.feetBox.Show(False)
			self.response.Show(False)
			self.btnSubmitIandF.Show(False)
	
	def OnToggleShowT(self, e):
		isChecked = self.ShowT.GetValue()
		if isChecked:
			self.prompt4.Show(True)
			self.tallBox.Show(True)
			self.btnSubmitT.Show(True)
			self.btnSubmitT.Show(True)
			self.response2.Show(True)
		else:
			self.prompt4.Show(False)
			self.tallBox.Show(False)
			self.btnSubmitT.Show(False)
			self.btnSubmitT.Show(False)
			self.response2.Show(False)

# ----------- Main Program Below -----------------
app = wx.App(False)
frame = HightFrame(None)
app.MainLoop()
