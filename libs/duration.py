class Duration:
	def __init__(self, hours = 0, minutes = 0, seconds = 0):
		self.seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

	def totalSeconds(self):
		return self.seconds

	def getHours(self):
		return self.totalSeconds() // 3600

	def getMinutes(self):
		return (self.totalSeconds() % 3600) // 60

	def getSeconds(self):
		return self.totalSeconds() % 60

	def toHHMMSS(self):
		return "{0}:{1:02d}:{2:02d}".format(self.getHours(), self.getMinutes(), self.getSeconds())

	def toMMSS(self):
		minutes = self.getHours() * 60 + self.getMinutes()
		seconds = self.getSeconds()
		return "{0}:{1:02d}".format(minutes, seconds)

if __name__ == "__main__":
	dur = Duration(hours = 3, minutes = 45, seconds = 0)
	print(dur.toHHMMSS())
	print(dur.toMMSS())
	print(dur.totalSeconds())