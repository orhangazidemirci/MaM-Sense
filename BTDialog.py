from BasicUI import BasicUI
from BTThread import BTThread
from PyQt5.QtWidgets import QListWidget, QStatusBar, QWidget
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
import bluetooth


class BTDialog(BasicUI):

	def __init__(self, parent, dataCallback, connectedCallback, errorCallback):
		super(BTDialog, self).__init__("./ui/bluetooth.ui", parent, None, None)
		
		self.connectedCallback = connectedCallback
		self.dataCallback = dataCallback
		self.errorCallback = errorCallback

		self.btDevices = self.findChild(QListWidget, "btList")
		self.btDevices.clicked.connect(self.deviceSelected)
		self.scanDevices()

	def scanDevices(self):
		self.devices = bluetooth.discover_devices(lookup_names = True)
		self.devicesFound()

	def devicesFound(self):
		for device in self.devices:
			address, name = device
			self.btDevices.insertItem(0, name)
		self.devices = self.devices[::-1]

	def initBluetooth(self):
		self.bluetoothThread = BTThread(self.address, self.dataCallback, self.connectedCallback, self.errorCallback)
		self.bluetoothThread.init()
		

	@pyqtSlot()
	def deviceSelected(self):
		self.address, name = self.devices[self.btDevices.currentRow()]
		self.initBluetooth()




