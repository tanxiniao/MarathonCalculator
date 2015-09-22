from libs.duration import Duration
from libs.runningPredictor import RunningPredictor
from libs.trainningPace import TrainingPaceGenerator

def createRunningPredictor():
	oldDist = float(input("请输入您近期完成的某个比赛的距离（km）："))
	oldTime = input("请输入您完成该比赛所用的时间（时:分:秒）：")
	h, m, s = oldTime.split(":")
	return RunningPredictor(oldDist, Duration(h, m, s))

def predictRunningDuration(predictor):
	print("\n比赛成绩预测：")
	print("-" * 80)
	items = [("5km", 5), ("10km", 10), ("Half Marathon (21.0975km)", 21.0975), ("Full Marathon (42.195km)", 42.195)]
	for item in items:
		itemName = item[0]
		itemDist = item[1]
		duration, pace = predictor.predict(itemDist)
		print("{0:30s} {1:20s} {2:20s}".format(itemName, duration.toHHMMSS(), pace.toMMSS() + "（分:秒/km）"))	

def generateTrainingPace(predictor):
	print("\n全马训练的参考配速：")
	print("-" * 80)
	marathonDuration, marathonPace = predictor.predict(42.195)
	paceGenerator = TrainingPaceGenerator(marathonDuration, marathonPace)
	showEasyPace(paceGenerator)
	showMarathonPace(paceGenerator)
	showTempoPace(paceGenerator)
	showYasso800Pace(paceGenerator)
	showYasso1000Pace(paceGenerator)

def showEasyPace(paceGenerator):
	fasterEasyPace, slowerEasyPace = paceGenerator.getEasyPaceRange()
	print("{0:30s} {1:20s}".format("Easy Run", fasterEasyPace.toMMSS() + "～" + slowerEasyPace.toMMSS() + "（分:秒/km）"))

def showMarathonPace(paceGenerator):
	marathonPace = paceGenerator.getMarathonPace()
	print("{0:30s} {1:20s}".format("Marathon Pace", marathonPace.toMMSS() + "（分:秒/km）"))

def showTempoPace(paceGenerator):
	tempoPace = paceGenerator.getTempoPace()
	print("{0:30s} {1:20s}".format("Tempo Run", tempoPace.toMMSS() + "（分:秒/km）"))

def showYasso800Pace(paceGenerator):
	pace = paceGenerator.getYasso800Pace()
	print("{0:30s} {1:20s}".format("Yasso 800", pace.toMMSS() + "（分:秒/800m）"))

def showYasso1000Pace(paceGenerator):
	pace = paceGenerator.getYasso1000Pace()
	print("{0:30s} {1:20s}".format("Yasso 1000", pace.toMMSS() + "（分:秒/km）"))

if __name__ == "__main__":
	predictor = createRunningPredictor()
	predictRunningDuration(predictor)
	generateTrainingPace(predictor)