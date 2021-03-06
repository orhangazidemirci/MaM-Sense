from PyQt5.QtWidgets import QPushButton

class Direction:
	UP = 1
	RIGHT = 2
	DOWN = 3
	LEFT = 4

class FocusUtil():

	def __init__(self, gridLayout):
		self.gridLayout = gridLayout
		self.rows = self.gridLayout.rowCount()
		self.cols = self.gridLayout.columnCount()
		self.applyDefaultFocus()

	def getButtonLocation(self, button):
		idx = self.gridLayout.indexOf(button)
		location = self.gridLayout.getItemPosition(idx)
		return location

	def setFirstButton(self):
		self.posData = {"row": 0, "column": 0}
		for j in range(self.rows):
			for i in range(self.cols):
				if (isinstance(self.getItem(j, i), QPushButton)):
					self.posData["row"] = j
					self.posData["column"] = i
					return

	def applyDefaultFocus(self):
		self.setFirstButton()
		w = self.currentWidget()
		self.updateButton(w, True)

	def currentWidget(self):
		return self.getItem(self.posData["row"], self.posData["column"])

	def getItem(self, x, y):
		try:
			return self.gridLayout.itemAtPosition(x, y).widget()
		except:
			return None

	def clickButton(self):
		self.currentWidget().animateClick()
		
	def moveFocus(self, direction):
		startItem = self.currentWidget()
		
		if (direction == Direction.UP):
			for i in reversed(range(0, self.posData["row"])):
				testItem = self.getItem(i, self.posData["column"])
				if (isinstance(testItem, QPushButton) and testItem != startItem):
					self.posData["row"] = i
					break

		elif (direction == Direction.RIGHT):
			for i in range(self.posData["column"] + 1, self.cols):
				testItem = self.getItem(self.posData["row"], i)
				if (isinstance(testItem, QPushButton) and testItem != startItem):
					self.posData["column"] = i
					break

		elif (direction == Direction.DOWN):
			for i in range(self.posData["row"] + 1, self.rows):
				testItem = self.getItem(i, self.posData["column"])
				if (isinstance(testItem, QPushButton) and testItem != startItem):
					self.posData["row"] = i
					break

		elif (direction == Direction.LEFT):
			for i in reversed(range(0, self.posData["column"])):
				testItem = self.getItem(self.posData["row"], i)
				if (isinstance(testItem, QPushButton) and testItem != startItem):
					self.posData["column"] = i
					break
		
		nextItem = self.currentWidget()
		return startItem, nextItem

	def moveFocusUpdate(self, direction):
		current, next = self.moveFocus(direction)
		self.updateButton(current, False)
		self.updateButton(next, True)

	def updateButton(self, button, focused):
		button.setProperty("focusedButton", focused)
		button.style().unpolish(button)
		button.style().polish(button)
		button.update()