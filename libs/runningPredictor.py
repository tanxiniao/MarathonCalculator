from .duration import Duration

class RunningPredictor:
	def __init__(self, oldDistance, oldDuration):
		self.oldDistance = float(oldDistance)
		self.oldDuration = oldDuration

	def predict(self, newDistance):
		# use Dave Cameron's formula
		newDistance = float(newDistance)
		oldDistInMiles = self.oldDistance / 1.609344
		newDistInMiles = newDistance / 1.609344
		oldSeconds = self.oldDuration.totalSeconds()
		a = 13.49681 - 0.048865 * oldDistInMiles + 2.438936 / (oldDistInMiles ** 0.7905)
		b = 13.49681 - 0.048865 * newDistInMiles + 2.438936 / (newDistInMiles ** 0.7905)
		newSeconds = int(oldSeconds * (a / b) * (newDistInMiles / oldDistInMiles))

		# revise total duration
		secondsPerKM = int(newSeconds / newDistance)
		totalSeconds = int(secondsPerKM * newDistance)
		return (Duration(seconds = totalSeconds), Duration(seconds = secondsPerKM))

if __name__ == "__main__":
	predictor = RunningPredictor(42.195, Duration(hours = 4))
	dur, pace = predictor.predict(42.195)
	print(dur.toHHMMSS())
	print(pace.toMMSS())