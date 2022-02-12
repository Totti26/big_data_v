import csv
import matplotlib.pyplot as plot

stations = []

class stationInfo():
    def __init__(self, name):
        self.name = name
        self.averageMax, self.averageMin, self.maxTemp, self.minTemp = 0, 0, 0, 0
        self.info = {
            "Max" : [],
            "Min" : [],
            }
        
    def firstData(self, value, limits):
        if value > limits[1] or value < limits[0]:
            return False
        else:
            return True

    def addData(self, infoName, data, limits):
        if self.firstData(data, limits):
            self.info[infoName].append(data)
        else:
            self.info[infoName].append("")

    def calcMax(self, infoName):
        Max = 0 
        for data in self.info[infoName]:
            if data != "":
                if Max == 0 or data > Max:
                    Max = data
        return Max
    
    def calcMin(self, infoName):
        Min = 0
        for data in self.info[infoName]:
            if data != "":
                if Min == 0 or data < Min:
                    Min = data
        return Min

    def Average(self, infoName):
        dataAmmount = 0
        average = 0
        for data in self.info[infoName]:
            if data != "":
                average += data
                dataAmmount += 1
        average /= dataAmmount
        return average

    def plotInfo(self, list):
        plot.plot(range(len(list)), list, label = station.name)

    def cleanInfo(self, infoName):
        newList = []
        for i in range(len(self.info[infoName])):
            if self.info[infoName][i] == "":
                forwardStep = 1
                while self.info[infoName][i + forwardStep] == "":
                    forwardStep += 1
                if i == 0:
                    info = self.info[infoName][i + forwardStep]
                elif i == len(self.info[infoName]) - 1:
                    info = newList[i - 1]
                else:
                    info = ((self.info[infoName][i + forwardStep] - info) / forwardStep + 1) + info
            else:
                info = self.info[infoName][i]
            newList.append(info)
        return newList

    def printInfo(self):
        print(f"{self.name}'s highest temp was {round(self.maxTemp, 2)}. ")
        print(f"{self.name}'s lowest temp was {round(self.minTemp, 2)}. ")
        print(f"{self.name}'s avg highest temp was {round(self.averageMax, 2)}. ")
        print(f"{self.name}'s avg highest temp was {round(self.averageMin, 2)}. ")
        print("")

with open('BigData2016 (1).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        max = float(row["TMAX"])
        min = float(row["TMIN"])
        
        currentStation = row["STID"]
        i = 0
        if len(stations) == 0:
            stations.append(stationInfo(currentStation))
        for station in stations:
            i += 1
            if station.name == currentStation:
                break
            else:
                if i >= len(stations):
                    stations.append(stationInfo(currentStation))
        for station in stations:
            if station.name == currentStation:
                station.addData("Max", max, (-80, 120))
                station.addData("Min", min, (-80, 120))

for station in stations:
    station.averageMax = station.Average("Max")
    station.averageMin = station.Average("Min")
    station.maxTemp = station.Average("Max")
    station.minTemp = station.Average("Min")
    station.printInfo()
    dataList = station.cleanInfo("Max")
    station.plotInfo(dataList)
                
plot.legend()    
plot.show()
