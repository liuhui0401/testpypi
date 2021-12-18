import lunarcalendar
import  stringcolor
from lunarcalendar.festival import festivals
import sys
import os
from datetime import datetime
import pdb

def make_color(code):
    def color_func(s):
        tpl = '\x1b[{}m{}\x1b[0m'
        return tpl.format(code, s)
    return color_func

red = make_color(31)
green = make_color(32)
yellow = make_color(33)
blue = make_color(34)
magenta = make_color(35)
cyan = make_color(36)

holiday = {}
holiday_list = []
favorite = []
chinese_list = ["New Year's Day", "Ching Ming Festival", "LaBa Festival", "New Year's Eve",
                "XiaoNian", "Chinese New Year", "PoWu Festival", "Lantern Festival", 
                "Dragon Head Festival", "Dragon Boat Festival", "Qixi Festival", "Ghost Festival", 
                "Mid-Autumn Festival", "Double Ninth Festival", "HanYi Festival", "Dong Festival"]
foreign_list = ["Valentine's Day", "Halloween", "Thanksgiving Day", "Christmas Eve", "Christmas Day", "Easter"]
new_list = ["Women's Day", "Arbor Day", "Youth Day in China", "International Nurses Day",
            "Father's Day", "Mother's Day", "Children's Day", "Teacher's Day",
            "National Day of the People's Republic of China"]
    

def init(input): # input: year(int)
    global holiday
    global holiday_list
    holiday.clear()
    holiday_list.clear()
    for fest in festivals:
        holiday[fest] = fest(input)
    holiday_list = sorted(holiday.items(), key=lambda x: x[1]) # list


def Set_Favorite_Festival(input): # input: festival(str)
    for fest in festivals:
        if input == fest.get_lang('en'):
            favorite.append(fest)
            break
        for zhname in fest.get_lang_list('zh'):
            if zhname == input:
                favorite.append(fest)
                break


def Get_Favorite_Festival(input): # input: year(int)
    init(input)
    if len(favorite) == 0:
        print("None")
    else:
        for fav in favorite:
            print('{} on {}: {}'.format(fav.get_lang('zh'), input, holiday[fav]))


def Cancel_Favorite_Festival(input): #input: festival(str)
    flag = 0
    for fest in festivals:
        if input == fest.get_lang('en'):
            favorite.remove(fest)
            flag = 1
            break
        for zhname in fest.get_lang_list('zh'):
            if zhname == input:
                favorite.remove(fest)
                flag = 1
                break
    if flag == 0:
        print("{} isn't in favorite".format(input))


def Year_Festivals(input): # input: year(int)
    init(input)
    for fest in holiday:
        if fest in favorite:
            print('{} on {}: {}'.format(cyan(fest.get_lang('zh')), input, fest(input)))
        elif fest.get_lang('en') in chinese_list:
            print('{} on {}: {}'.format(red(fest.get_lang('zh')), input, fest(input)))
        elif fest.get_lang('en') in foreign_list:
            print('{} on {}: {}'.format(blue(fest.get_lang('zh')), input, fest(input)))
        else:
            print('{} on {}: {}'.format(fest.get_lang('zh'), input, fest(input)))


def Next_Festivals(input): # input: year(special)
    date = datetime.strptime(input, '%Y-%m-%d').date()
    year = date.year
    cnt = 0
    init(year)
    for fest in holiday.keys():
        if cnt == 10:
            break
        if date < holiday[fest]:
            if fest.get_lang('en') in favorite:
                print('{} on {}: {}'.format(cyan(fest.get_lang('zh')), year, fest(year)))
            elif fest.get_lang('en') in chinese_list:
                print('{} on {}: {}'.format(red(fest.get_lang('zh')), year, fest(year)))
            elif fest.get_lang('en') in foreign_list:
                print('{} on {}: {}'.format(blue(fest.get_lang('zh')), year, fest(year)))
            else:
                print('{} on {}: {}'.format(fest.get_lang('zh'), year, fest(year)))
            cnt += 1