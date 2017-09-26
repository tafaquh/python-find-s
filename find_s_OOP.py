# Created by M Tafaquh Fiddin Al Islami
# 2110151035 | 3 D4 IT B 2017
# Politeknik Elektronika Negeri Surabaya

class Data(object):
    def __init__(self, sky, airtemp, humidity, wind, water, forecast, enjoy):
        self.__sky = sky
        self.__airtemp = airtemp
        self.__humidity = humidity
        self.__wind = wind
        self.__water = water
        self.__forecast = forecast
        self.__enjoy = enjoy
    
    def __init__(self, sky=0, airtemp=0, humidity=0, wind=0, \
                 water=0, forecast=0, enjoy=0):
        self.__sky = sky
        self.__airtemp = airtemp
        self.__humidity = humidity
        self.__wind = wind
        self.__water = water
        self.__forecast = forecast
        self.__enjoy = enjoy

    def printValue(self):
        print("Sky \tAirTempt \tHumidity \tWind \tWater \tForeCast \tEnjoy")
        print("%s \t%s \t\t%s \t\t%s \t%s \t%s \t\t%s" % \
              (self.getSky(), self.getAirTemp(), self.getHumidity(),\
               self.getWind(), self.getWater(), self.getForeCast(), self.getEnjoy()))
        
    def setSky(self, sky):
        self.__sky = sky
    def getSky(self):
        return self.__sky
    
    def setAirTemp(self, airtemp):
        self.__airtemp = airtemp
    def getAirTemp(self):
        return self.__airtemp

    def setHumidity(self, humidity):
        self.__humidity = humidity
    def getHumidity(self):
        return self.__humidity

    def setWind(self, wind):
        self.__wind = wind
    def getWind(self):
        return self.__wind

    def setWater(self, water):
        self.__water = water
    def getWater(self):
        return self.__water

    def setForeCast(self, forecast):
        self.__forecast = forecast
    def getForeCast(self):
        return self.__forecast

    def setEnjoy(self, enjoy):
        self.__enjoy = enjoy
    def getEnjoy(self):
        return self.__enjoy
    
def main():
    data1 = Data("Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes")
    data2 = Data("Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes")
    data3 = Data("Rainy", "Cold", "High", "Strong", "Warm", "Change", "No")
    data4 = Data("Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes")

    testing1 = Data("Sunny", "Warm", "High", "Strong", "Cool", "Change", "")
    testing2 = Data("Sunny", "Warm", "Normal", "Weak", "Warm", "Same", "")
    testing3 = Data("Rainy", "Cold", "Normal", "Weak", "Warm", "Same", "")
    testing4 = Data("Rainy", "Warm", "Normal", "Weak", "Warm", "Same", "")
    
    s = Data()
    
    list_data = [data1, data2, data3, data4]
    list_testing = [testing1, testing2, testing3, testing4]

    countEnjoy = int(0)
    check = input("Which hypotheses do you prefer <'+'/ '-'>? ")
    
    if check != "+" and check != "-":
        while check != "+" and check != "-":
            print("Please press '+' or '-' without single quotation mark")
            check = input("Which hypotheses do you prefer <'+'/ '-'>? ")
            
    else:
        if check == "+" : check = "Yes"
        else : check = "No"
        #Training Goes Here
        for i in range(0, len(list_data)):
            if check == list_data[i].getEnjoy():
                countEnjoy += 1
                if countEnjoy == 1:
                    s.__dict__ = list_data[i].__dict__.copy()
                else:
                    if list_data[i].getSky() == s.getSky():
                        s.setSky(list_data[i].getSky())
                    else:
                        s.setSky("?")
                    if list_data[i].getAirTemp() == s.getAirTemp():
                        s.setAirTemp(list_data[i].getAirTemp())
                    else:
                        s.setAirTemp("?")
                    if list_data[i].getHumidity() == s.getHumidity():
                        s.setHumidity(list_data[i].getHumidity())
                    else:
                        s.setHumidity("?")
                    if list_data[i].getWind() == s.getWind():
                        s.setWind(list_data[i].getWind())
                    else:
                        s.setWind("?")
                    if list_data[i].getWater() == s.getWater():
                        s.setWater(list_data[i].getWater())
                    else:
                        s.setWater("?")
                    if list_data[i].getForeCast() == s.getForeCast():
                        s.setForeCast(list_data[i].getForeCast())
                    else:
                        s.setForeCast("?")
        s.setEnjoy(check)
    print("Final Hypothesis")
    print(s.printValue())
    
    #Testing Goes Here
    
    for i in range(0, len(list_testing)):
        temp = int(0)
        count_q = int(0)
        if bool(list_testing[i].getSky() == s.getSky()) != bool(s.getSky() == "?"):
            temp += 1
        else: count_q += 1
        if bool(list_testing[i].getAirTemp() == s.getAirTemp()) != bool(s.getAirTemp() == "?"):
            temp += 1
        else: count_q += 1
        if bool(list_testing[i].getHumidity() == s.getHumidity()) != bool(s.getHumidity() == "?"):
            temp += 1
        else: count_q += 1
        if bool(list_testing[i].getWind() == s.getWind()) != bool(s.getWind() == "?"):
            temp += 1
        else: count_q += 1
        if bool(list_testing[i].getWater() == s.getWater()) != bool(s.getWater() == "?"):
            temp += 1
        else: count_q += 1
        if bool(list_testing[i].getForeCast() == s.getForeCast()) != bool(s.getForeCast() == "?"):
            temp += 1
        else: count_q += 1
        
        if temp == count_q:
            list_testing[i].setEnjoy("No")
        elif temp == 6:
            list_testing[i].setEnjoy("Yes")
        else:
            list_testing[i].setEnjoy("Unknown")

        
        print("\nResult from Testing-%d"% (i+1))
        print(list_testing[i].printValue())
        
if __name__ == '__main__':
    main()
