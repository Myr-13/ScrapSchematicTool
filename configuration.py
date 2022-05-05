import json
import os

class Config:
	def __init__(self):
		self.file_name = "settings.json"
		self.settings = {
			"window": {
				"width": 1200,
				"height": 720,
				"fps": 60
			}
		}
		if os.name == "nt":
			self.appdata = os.getenv("APPDATA")
		else:
			self.appdata = "/home/" + os.getlogin()

	def save(self):
		# Check save path %APPDATA%/MyroDev/ScrapSchematicTool
		if not os.path.exists(self.appdata + "/MyroDev"):
			os.chdir(self.appdata)
			os.mkdir("MyroDev")
		if not os.path.exists(self.appdata + "/MyroDev/ScrapSchematicTool"):
			os.chdir(self.appdata + "/MyroDev")
			os.mkdir("ScrapSchematicTool")

		# Save
		os.chdir(self.appdata + "/MyroDev/ScrapSchematicTool")
		json.dump(self.settings, open(self.file_name, "w"))

		print("Config saved")

	def load(self):
		if os.path.exists(self.appdata + "/MyroDev/ScrapSchematicTool/" + self.file_name):
			os.chdir(self.appdata + "/MyroDev/ScrapSchematicTool")
			self.settings = json.load(open(self.file_name, "r"))

			print("Config loaded")
