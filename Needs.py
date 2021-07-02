from FocusUtil import Direction, FocusUtil
from PyQt5.QtWidgets import QGridLayout, QWidget
from PyQt5 import uic

class Needs(QWidget):

	def __init__(self, socket):
		super(Needs, self).__init__()
		self.socket = socket
		uic.loadUi("./ui/needs.ui", self)

		self.setStyleSheet(open("./ui/buttonFocus.css").read())
		self.needsGroup = self.findChild(QGridLayout, "gridLayout")
		self.focusUtil = FocusUtil(self.needsGroup)
		self.show()

	def keyPressEvent(self, event):
		if (event.key() == 87):
			self.focusUtil.moveFocusUpdate(Direction.UP)
		elif (event.key() == 65):
			self.focusUtil.moveFocusUpdate(Direction.LEFT)
		elif (event.key() == 83):
			self.focusUtil.moveFocusUpdate(Direction.DOWN)
		elif (event.key() == 68):
			self.focusUtil.moveFocusUpdate(Direction.RIGHT)