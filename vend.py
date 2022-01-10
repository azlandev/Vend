import tkinter as tk
import json

WIDTH = 600
HEIGHT = 1024

f = open("assets/drinks.json")
DRINKS = json.loads(f.read())

ADMIN_CODE = "1111"
		
class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		bg = tk.PhotoImage(file="assets/backgrounds/bg-start.png")
		bgLabel = tk.Label(self, image=bg)
		bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
		bgLabel.image = bg
		
		controller.createButton(self, 0, 804, "assets/buttons/btn-start.png", lambda: controller.showFrame(VendPage))
		
class VendPage(tk.Frame):
	code = ""

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		bg = tk.PhotoImage(file="assets/backgrounds/bg-vend.png")
		bgLabel = tk.Label(self, image=bg)
		bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
		bgLabel.image = bg
		
		controller.createButton(self, WIDTH/2, 0, "assets/buttons/btn-shots.png", lambda: controller.showFrame(ShotsPage))
		
		inputFrame = tk.Frame(self, width=340, height=100, bg="black", borderwidth=0, highlightthickness=0)
		inputFrame.pack_propagate(0)
		inputFrame.place(x=WIDTH/2-170, y=230)
		inputLabel = tk.Label(inputFrame, bg="black", fg="white", font=('', 50), text="", anchor="center")
		inputLabel.pack(fill="both", expand=True)
		
		keyPadContainer = tk.Frame(self, width=340, height=580, bg="#2c2d31", borderwidth=0, highlightthickness=0)
		keyPadContainer.place(x=130, y=346)
		
		controller.createButton(keyPadContainer, 0, 0, "assets/buttons/btn-a.png", lambda: self.updateText(controller, inputLabel, "A"))
		controller.createButton(keyPadContainer, 120, 0, "assets/buttons/btn-b.png", lambda: self.updateText(controller, inputLabel, "B"))
		controller.createButton(keyPadContainer, 240, 0, "assets/buttons/btn-c.png", lambda: self.updateText(controller, inputLabel, "C"))
		controller.createButton(keyPadContainer, 0, 120, "assets/buttons/btn-1.png", lambda: self.updateText(controller, inputLabel, "1"))
		controller.createButton(keyPadContainer, 120, 120, "assets/buttons/btn-2.png", lambda: self.updateText(controller, inputLabel, "2"))
		controller.createButton(keyPadContainer, 240, 120, "assets/buttons/btn-3.png", lambda: self.updateText(controller, inputLabel, "3"))
		controller.createButton(keyPadContainer, 0, 240, "assets/buttons/btn-4.png", lambda: self.updateText(controller, inputLabel, "4"))
		controller.createButton(keyPadContainer, 120, 240, "assets/buttons/btn-5.png", lambda: self.updateText(controller, inputLabel, "5"))
		controller.createButton(keyPadContainer, 240, 240, "assets/buttons/btn-6.png", lambda: self.updateText(controller, inputLabel, "6"))
		controller.createButton(keyPadContainer, 0, 360, "assets/buttons/btn-7.png", lambda: self.updateText(controller, inputLabel, "7"))
		controller.createButton(keyPadContainer, 120, 360, "assets/buttons/btn-8.png", lambda: self.updateText (controller, inputLabel, "8"))
		controller.createButton(keyPadContainer, 240, 360, "assets/buttons/btn-9.png", lambda: self.updateText(controller, inputLabel, "9"))
		controller.createButton(keyPadContainer, 0, 480, "assets/buttons/btn-x.png", lambda: self.updateText(controller, inputLabel, "X"))
		controller.createButton(keyPadContainer, 120, 480, "assets/buttons/btn-0.png", lambda: self.updateText(controller, inputLabel, "0"))
		controller.createButton(keyPadContainer, 240, 480, "assets/buttons/btn-confirm.png", lambda: self.confirm(inputLabel))
		
	def updateText(self, controller, label, inputText):
		if inputText == "X":
			label.configure(text="")
			self.code = ""
		else:
			labelText = label.cget("text")
			if len(labelText) < 2:
				label.configure(text=labelText+inputText)
			self.code += inputText
			if self.code == ADMIN_CODE:
				controller.showFrame(AdminPage)
	
	def confirm(self, label):
		error = False
		vendText = label.cget("text")
		if vendText == "": return
		
		if not (vendText[0] in "ABC") or not (vendText[1] in "0123456789"):
			error = True
		if(error):
			label.configure(text="Invalid")
			self.after(500, lambda: label.configure(text=""))
		else:
			## TODO ##
			print(vendText)
		
		
class ShotsPage(tk.Frame):
	numberOfDrinks = len(DRINKS["Drinks"])
	currentDrink = DRINKS["Drinks"][0]
	prevDrink = DRINKS["Drinks"][-1]
	nextDrink = DRINKS["Drinks"][1]
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		bg = tk.PhotoImage(file="assets/backgrounds/bg-shots.png")
		bgLabel = tk.Label(self, image=bg)
		bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
		bgLabel.image = bg
		
		controller.createButton(self, 0, 0, "assets/buttons/btn-vend.png", lambda: controller.showFrame(VendPage))
		
		drinkContainer = tk.Frame(self, width=600, height=450, bg="#2c2d31", borderwidth=0, highlightthickness=0)
		drinkContainer.pack_propagate(0)
		drinkContainer.place(x=0, y=125)
		self.createView(drinkContainer)
		
		inputFrame = tk.Frame(self, width=100, height=100, bg="black", borderwidth=0, highlightthickness=0)
		inputFrame.pack_propagate(0)
		inputFrame.place(x=WIDTH/2-50, y=600)
		inputLabel = tk.Label(inputFrame, bg="black", fg="white", font=('', 50), text="0", anchor="center")
		inputLabel.pack(fill="both", expand=True)
		controller.createButton(self, 150, 600, "assets/buttons/btn-minus.png", lambda: self.updateAmount(inputLabel, "-"))
		controller.createButton(self, 350, 600, "assets/buttons/btn-plus.png", lambda: self.updateAmount(inputLabel, "+"))
		
		totalContainer = tk.Frame(self, width=600, height=100, bg="black", borderwidth=0, highlightthickness=0)
		totalContainer.place(x=0, y=825)
		
		controller.createButton(self, 40, 720, "assets/buttons/btn-half.png", lambda: self.updateTotal(controller, totalContainer, inputLabel, "half"))
		controller.createButton(self, 310, 720, "assets/buttons/btn-full.png", lambda: self.updateTotal(controller, totalContainer, inputLabel, "full"))
		
		controller.createButton(self, 0, 925, "assets/buttons/btn-dispense.png", lambda: self.checkout(controller, "dispense"))
		
		controller.setTotalContainer(totalContainer)
		
	def updateAmount(self, label, operation):
		labelText = int(label.cget("text"))
		if operation == "+" and labelText < 9:
			label.configure(text=str(labelText + 1))
		elif operation == "-" and labelText > 0:
			label.configure(text=str(labelText - 1))
			
	def updateTotal(self, controller, container, inputLabel, halfOrFull):
		inLbl = int(inputLabel.cget("text"))
		if inLbl == 0: return
		
		if halfOrFull == "half":
			self.currentDrink["half"] += inLbl
		else:
			self.currentDrink["full"] += inLbl
		self.currentDrink["addedToTotal"] = True
		
		self.updateTotalContainer(controller, container)
		inputLabel.configure(text="0")
		
	def updateTotalContainer(self, controller, container):
		for child in container.winfo_children():
			child.destroy()	
		
		counter = 0
		yPos = 10
		for drink in DRINKS["Drinks"]:
			if drink["addedToTotal"]:
				if counter >= 2:
					nameLabel = tk.Label(container, bg="black", fg="white", font=('', 15), justify=tk.LEFT, text="...")
					nameLabel.place(x=150, y=yPos)
					break
				nameLabel = tk.Label(container, bg="black", fg="white", font=('', 15), width=50, justify=tk.LEFT, anchor="w", text=drink["name"])
				nameLabel.place(x=150, y=yPos)
				amountLabel = tk.Label(container, bg="black", fg="white", font=('', 15), justify=tk.RIGHT, text="Half: {} | Full {}\n".format(str(drink["half"]), str(drink["full"])))
				amountLabel.place(x=450, y=yPos)
				yPos += 30
				counter += 1
				
		controller.createButton(container, 0, 0, "assets/buttons/btn-edit.png", lambda: self.checkout(controller, "edit"))
		controller.createButton(container, 0, 50, "assets/buttons/btn-clear.png", lambda: self.clearTotal(container))
		
	def changeDrink(self, frame, leftOrRight):
		btnLeft, btnRight, drinkLabel = frame.winfo_children()
		currentId = self.currentDrink["id"]
		
		if leftOrRight == "right":
			currentId = self.getDrinkId(currentId)["next"]
		else:
			currentId = self.getDrinkId(currentId)["prev"]
		self.currentDrink = DRINKS["Drinks"][currentId]
		self.prevDrink = DRINKS["Drinks"][self.getDrinkId(currentId)["prev"]]
		self.nextDrink = DRINKS["Drinks"][self.getDrinkId(currentId)["next"]]
		
		self.animate(frame, btnLeft, btnRight, drinkLabel, leftOrRight, currentId)
		self.createView(frame)
		
	def animate(self, frame, left, right, center, leftOrRight, currentId):
		shift = 0
		step = 65
		total = 325/step
		switched = False
		ms = 32
		
		if leftOrRight == "right":
			nextImg = tk.PhotoImage(file=DRINKS["Drinks"][self.getDrinkId(currentId)["next"]]["image"])
			while shift < total:
				shift += 1
				left.place(x=left.winfo_x()-step, y=0)
				right.place(x=right.winfo_x()-step, y=0)
				center.place(x=center.winfo_x()-step, y=0)
				if not switched and shift*step >= 125:
					left.configure(image=nextImg)
					left.place(x=right.winfo_x()+325, y=0)
					switched = True
				if shift == total:
					left.place(x=475, y=0)
				frame.update()
				frame.after(ms)	
		else:
			prevImg = tk.PhotoImage(file=DRINKS["Drinks"][self.getDrinkId(currentId)["prev"]]["image"])
			while shift < total:
				shift += 1
				left.place(x=left.winfo_x()+step, y=0)
				right.place(x=right.winfo_x()+step, y=0)
				center.place(x=center.winfo_x()+step, y=0)
				if not switched and shift*step >= 125:
					right.configure(image=prevImg)
					right.place(x=left.winfo_x()-325, y=0)
					switched = True
				if shift == total:
					right.place(x=-175, y=0)
				frame.update()
				frame.after(ms)
		left.destroy()
		right.destroy()
		center.destroy()
				
	def createView(self, drinkContainer):
		prevDrinkImg = tk.PhotoImage(file=self.prevDrink["image"])
		btnLeft = tk.Button(drinkContainer, image=prevDrinkImg, borderwidth=0, highlightthickness=0, command=lambda: self.changeDrink(drinkContainer, "left"))
		btnLeft.place(x=-175, y=0)
		btnLeft.image = prevDrinkImg
		
		nextDrinkImg = tk.PhotoImage(file=self.nextDrink["image"])
		btnRight = tk.Button(drinkContainer, image=nextDrinkImg, borderwidth=0, highlightthickness=0, command=lambda: self.changeDrink(drinkContainer, "right"))
		btnRight.place(x=475, y=0)
		btnRight.image = nextDrinkImg
		
		drinkImg = tk.PhotoImage(file=self.currentDrink["image"])
		drinkLabel = tk.Label(drinkContainer, image=drinkImg, borderwidth=0, highlightthickness=0)
		drinkLabel.place(x=150, y=0)
		drinkContainer.image = drinkImg
		
	def checkout(self, controller, button):
		if len(controller.totalContainer.winfo_children()) < 4:
			return
		controller.setTotalPage(button)
		controller.showFrame(TotalPage)
		
		
	def getDrinkId(self, currentId):
		prevId = currentId - 1 if currentId > 0 else self.numberOfDrinks - 1
		nextId = currentId + 1 if currentId + 1 < self.numberOfDrinks else 0
		return {"current": currentId, "prev": prevId, "next": nextId}
		
	def clearTotal(self, container):
		for drink in DRINKS["Drinks"]:
			if drink["addedToTotal"]:
				drink["half"] = 0
				drink["full"] = 0
				drink["addedToTotal"] = False
		for child in container.winfo_children():
			child.destroy()	
			
class TotalPage(tk.Frame):
	items = {"items": []}
	spacing = 100
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.configure(bg="#2c2d31")
		
	def updateTotal(self, controller, btnName):
		for child in self.winfo_children():
			child.destroy()
		self.items = {"items": []}
			
		controller.createButton(self, 0, 0, "assets/buttons/btn-back.png", lambda: controller.setShotsPage())
		
		titleFrame = tk.Frame(self, width=300, height=100, borderwidth=0, highlightthickness=0)
		titleFrame.pack_propagate(0)
		titleFrame.place(x=300, y=0)
		title = tk.Label(titleFrame, bg="#2c2d31", fg="white", font=('', 40), anchor="center")
		title.pack(fill="both", expand=True)
		if btnName == "edit":
			title.configure(text="Edit")
		else:
			title.configure(text="Confirm")
			controller.createButton(self, 0, 925, "assets/buttons/btn-dispense.png", lambda: print("Dispense"))
		
		yPos = 120
		itemId = 0
		for drink in DRINKS["Drinks"]:
			if drink["addedToTotal"]:
				text = "{}\n\tHalf: {}\n\tFull: {}\n".format(drink["name"], str(drink["half"]), str(drink["full"])) + "-"*50
				total = tk.Label(self, bg="#2c2d31", fg="white", justify="left", font=('', 15), text=text)
				total.place(x=0, y=yPos)
				totalBtn = controller.createButton(self, 500, yPos, "assets/buttons/btn-clear.png", lambda id=itemId: self.clearItem(id), ret=True)
				self.items["items"].append({"id": itemId, "drink": drink, "label": total, "button": totalBtn})
				yPos += self.spacing
				itemId += 1
		
	def clearItem(self, id):
		drink = self.items["items"][id]["drink"]
		drink["half"] = 0
		drink["full"] = 0
		drink["addedToTotal"] = False
		self.items["items"][id]["label"].destroy()
		self.items["items"][id]["button"].destroy()
		del self.items["items"][id]
		
		for item in self.items["items"]:
			if item["id"] > id:
				item["label"].place(x=item["label"].winfo_x(), y=item["label"].winfo_y()-self.spacing)
				item["button"].place(x=item["button"].winfo_x(), y=item["button"].winfo_y()-self.spacing)
				item["id"] -= 1
				item["button"].configure(command=lambda newId=item["id"]: self.clearItem(newId))
		
class AdminPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.configure(bg="#2c2d31")
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)
		
		
		btnBack = tk.Button(self, width=20, height=2, text="Back", command=lambda: controller.showFrame(VendPage))
		btnBack.grid(row=0, column=0, pady=(0, 20))
		
		title = tk.Label(self, bg="#2c2d31", fg="white", font=('', 20), text="Admin")
		title.grid(row=0, column=1, pady=(0, 20))
		
		btnClose = tk.Button(self, width=20, height=2, text="Exit", command=controller.destroy)
		btnClose.grid(row=0, column=2, pady=(0, 20))
		
		options = []
		for i in DRINKS["Drinks"]:
			options.append(i["name"])
			
		value = tk.StringVar(self)
		
		self.createPump(1, "Pump 1", options, value)
		self.createPump(3, "Pump 2", options, value)
		self.createPump(5, "Pump 3", options, value)
		self.createPump(7, "Pump 4", options, value)
		self.createPump(9, "Pump 5", options, value)
		self.createPump(11, "Pump 6", options, value)
		
	def createPump(self, pos, name, options, value):
		pumpLbl = tk.Label(self, bg="#2c2d31", fg="white", font=('', 12), text=name)
		pumpLbl.grid(row=pos, column=0, pady=(10, 0))
		
		pumpEnabled = tk.Label(self, bg="#2c2d31", fg="red", font=('', 12), text="Disabled")
		pumpEnabled.grid(row=pos, column=2, pady=(10, 0))
		
		drink = tk.OptionMenu(self, value, *options)
		drink.grid(row=pos+1, column=0)
		
		btnEnable = tk.Button(self, width=20, height=2, text="Enable")
		btnEnable.configure(command=lambda: self.setPump(pumpEnabled, btnEnable))
		btnEnable.grid(row=pos+1, column=2)
		
	def setPump(self, label, button):
		text = label.cget("text")
		if text == "Disabled":
			label.configure(fg="white", text="Enabled")
			button.configure(text="Disable")
		else:
			label.configure(fg="red", text="Disabled")
			button.configure(text="Enable")
		

class MainView(tk.Tk):
	totalContainer = None

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		PAGES = [StartPage, VendPage, ShotsPage, TotalPage, AdminPage]
		
		window = tk.Frame(self, width=WIDTH, height=HEIGHT, borderwidth=0, highlightthickness=0)
		window.pack(fill="both", expand=True)
		
		self.frames = {}
		for Page in PAGES:
			frame = Page(window, self)
			self.frames[Page] = frame
			frame.place(x=0, y=0, relwidth=1, relheight=1)
			
		self.showFrame(StartPage)
		
	def showFrame(self, page):
		frame = self.frames[page]
		frame.tkraise()
		
	def createButton(self, parent, x, y, imagePath, cmd, ret=False):
		btnImg = tk.PhotoImage(file=imagePath)
		btn = tk.Button(parent, image=btnImg, borderwidth=0, highlightthickness=0, command=cmd)
		btn.place(x=x, y=y)
		btn.image = btnImg
		if ret:
			return btn
		
	def setTotalPage(self, btnName):
		self.frames[TotalPage].updateTotal(self, btnName)
	
	def setTotalContainer(self, container):
		self.totalContainer = container
	
	def setShotsPage(self):
		self.frames[ShotsPage].updateTotalContainer(self, self.totalContainer)
		self.showFrame(ShotsPage)
		
main = MainView()
#main.wm_attributes('-type', 'splash')	#Linux only
#main.overrideredirect(1)	#Windows only
main.wm_geometry(str(WIDTH) + "x" + str(HEIGHT))
main.mainloop()
