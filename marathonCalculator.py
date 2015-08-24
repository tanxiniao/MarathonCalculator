def timeToSeconds(time):
	h, m, s = time.split(":")
	return int(h) * 3600 + int(m) * 60 + int(s)

def kmToMile(km):
	return km / 1.609344

def predictTime(oldDist, oldTime, newDist):
	# use Dave Cameron's formula
	oldDist = kmToMile(oldDist)
	newDist = kmToMile(newDist)
	a = 13.49681 - 0.048865 * oldDist + 2.438936 / (oldDist ** 0.7905)
	b = 13.49681 - 0.048865 * newDist + 2.438936 / (newDist ** 0.7905)
	return int(oldTime * (a / b) * (newDist / oldDist))

def secondsToTime(seconds):
	h = int(seconds / 3600)
	m = int(seconds % 3600 / 60)
	s = int(seconds % 60)
	return "%d:%02d:%02d" %(h, m, s)

def showPredictions(oldDist, oldTime):
	print("\n比赛成绩预测：")
	print("-" * 80)
	distances = [5, 10, 21.0975, 42.195]
	items = ["5km", "10km", "半程马拉松", "全程马拉松"]
	for index in range(len(distances)):
		time = predictTime(oldDist, oldTime, distances[index])
		print(items[index] + " : " + secondsToTime(time))

def secondsToPace(seconds):
	m = int(seconds / 60)
	s = int(seconds % 60)
	return "%d:%02d" %(m, s)

def showEasyRunPace(marathonPace):
	easyPaceRange = [marathonPace + 38, marathonPace + 56]
	print("轻松跑：" + secondsToPace(easyPaceRange[0]) + " ~ " + secondsToPace(easyPaceRange[1]) + "（分:秒/km）")

def showMarathonPace(marathonPace):
	print("配速跑：" + secondsToPace(marathonPace) + "（分:秒/km）")

def showTempoRunPace(marathonPace):
	tempoPace = marathonPace - 22
	print("节奏跑：" + secondsToPace(tempoPace) + "（分:秒/km）")

def showYasso800Pace(marathonTime):
	h = int(marathonTime / 3600)
	m = int(marathonTime % 3600 / 60)
	secondsPer800m = h * 60 + m
	print("亚索800：" + secondsToPace(secondsPer800m) + "（分:秒/800m）")

def showYasso1000Pace(marathonTime):
	h = int(marathonTime / 3600)
	m = int(marathonTime % 3600 / 60)
	secondsPerKm = int((h * 60 + m) / 800.0 * 1000)
	print("亚索1000：" + secondsToPace(secondsPerKm) + "（分:秒/km）")

def showTrainningPaces(oldDist, oldTime):
	print("\n马拉松训练的参考配速：")
	print("-" * 80)
	marathonDist = 42.195
	marathonTime = predictTime(oldDist, oldTime, marathonDist)
	marathonPace = int(marathonTime / marathonDist)
	showEasyRunPace(marathonPace)
	showMarathonPace(marathonPace)
	showTempoRunPace(marathonPace)
	showYasso800Pace(marathonTime)
	showYasso1000Pace(marathonTime)

if __name__ == "__main__":
	dist = float(input("请输入您近期完成的某个比赛的距离（km）："))
	time = timeToSeconds(input("请输入您完成该比赛所用的时间（时:分:秒）："))
	showPredictions(dist, time)
	showTrainningPaces(dist, time)
