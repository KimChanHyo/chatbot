
from bs4 import BeautifulSoup
from Src import src 
from TimeManager import tm # tm == TimeManager
import time
import urllib.request


class Menu :
    def __init__(self) :
        # 식단 정보
        self.__meal = dict()

        # parsing url
        self.__url = 'https://coop.koreatech.ac.kr:45578/dining/menu.php' + \
                     '?sday=' + str(tm.mainTime.sec)
        self.__parsing()

    # 아침 or 점심 or 저녁을 인자로 넘기면 해당하는 메뉴 반환
    def getMeal(self, content) :
        return '[' + content + '] - ' +	\
               str(tm.mainTime.st[1]) + '.' + str(tm.mainTime.st[2]) + '\n' + \
               self.__meal[content]

    # 메뉴 파싱
    def __parsing(self) :
        with urllib.request.urlopen(self.__url) as fs :
            soup = BeautifulSoup(fs.read()
                                 .decode('euc-kr')
                                 .replace('timeo', 'time')
                                 .replace('listo', 'list')
                                 .replace('\r', '')
                                 .replace('\t', '')
                                 .replace('kcal', 'kcal\n')
                                 , 'html.parser')
            items = soup.find_all('td', {'class' : 'menu-list'})

        # 아침 점심 저녁
        for i in range(3) :
            tmpData = ''
            # 한식, 일품, 특식, 양식, 능수관
            for j in range(5) :
                txt = items[i * 8 + j].get_text()
                if txt == '\n\xa0\n' : continue
                tmpData += ('# ' + src.mealType[j] + txt + '─' * 12 + '\n')
            self.__meal[src.mealTime[i]] = tmpData[:-2]


menu = Menu()
