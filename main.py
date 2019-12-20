import bs4
import requests

opggUrl = 'https://na.op.gg/statistics/champion/'


def getWinRate(opggUrl):
    res = requests.get(opggUrl)
    res.raise_for_status()

    soupRate = bs4.BeautifulSoup(res.content, 'html.parser')
    elemRate = soupRate.find_all('#ChampionStatsTable > table > tbody > tr:nth-child(1) > td:nth-child(4) > span')
    return elemRate


def getChamp(opggUrl):
    resTop = requests.get(opggUrl)
    resTop.raise_for_status()
    soupChamp = bs4.BeautifulSoup(resTop.content, 'html.parser')
    elemChamp = soupChamp.find_all('#ChampionStatsTable > table > tbody > tr:nth-child(1) > td.Cell.ChampionName > a')
    return elemChamp


topChamp = getChamp(opggUrl)
rate = getWinRate('https://na.op.gg/champion/statistics')

print(getWinRate(opggUrl))
print(getChamp(opggUrl))
