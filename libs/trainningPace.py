from .duration import Duration

class TrainingPaceGenerator:
	def __init__(self, marathonDuration, marathonPace):
		self.marathonDuration = marathonDuration
		self.marathonPace = marathonPace

	def getEasyPaceRange(self):
		fasterEasyPace = Duration(seconds = self.marathonPace.totalSeconds() + 38)
		slowerEasyPace = Duration(seconds = self.marathonPace.totalSeconds() + 56)
		return (fasterEasyPace, slowerEasyPace)

	def getMarathonPace(self):
		return self.marathonPace

	def getTempoPace(self):
		return Duration(seconds = self.marathonPace.totalSeconds() - 22)

	def getYasso800Pace(self):
		h = self.marathonDuration.getHours()
		m = self.marathonDuration.getMinutes()
		return Duration(minutes = h, seconds = m)

	def getYasso1000Pace(self):
		yasso800Pace = self.getYasso800Pace()
		return Duration(seconds = yasso800Pace.totalSeconds() / 800.0 * 1000)