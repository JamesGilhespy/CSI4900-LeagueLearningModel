from riotwatcher import LolWatcher, ApiError
import csv

#Must enter Riot API to run
lol_watcher = LolWatcher('RGAPI-9007adac-643b-40be-985a-cd8de200e315')
na = 'na1'
me = lol_watcher.summoner.by_name(na,'Victør')

matches= lol_watcher.match.matchlist_by_puuid('americas',me['puuid'],None,3,None,'ranked',None,None)
dataset = open('C:/Users/ofbac/OneDrive/Desktop/League Machine Learning Model/test1.csv', 'a', encoding='UTF8', newline='')
writer = csv.writer(dataset)
header=['Red_Top_WR','Red_Top_Champion_XP','Red_Top_ChampWR','Red_JG_WR','Red_JG_ChampXP','Red_JG_ChampWR','Red_Mid_WR',	'Red_Mid_ChampXP',	'Red_Mid_ChampWR',	'Red_ADC_WR',	'Red_ADC_ChampXP',	'Red_ADC_ChampWR',	'Red_SUP_WR',	'Red_SUP_ChampXP',	'Red_SUP_ChampWR',	'Blue_TOP_WR',	'Blue_TOP_ChampXP',	'Blue_TOP_ChampWR',	'Blue_JG_WR',	'Blue_JG_ChampXP',	'Blue_JG_ChampWR',	'Blue_Mid_WR',	'Blue_Mid_ChampXP',	'Blue_Mid_ChampWR',	'Blue_ADC_WR',	'Blue_ADC_ChampXP',	'Blue_ADC_ChampWR',	'Blue_SUP_WR',	'Blue_SUP_ChampXP',	'Blue_SUP_ChampWR',	'Winning_Team']

#calls for summoner 1
for i in range(len(matches)):
    lastmatch= lol_watcher.match.by_id('americas',matches[i])
    puuid1=(lastmatch['metadata']['participants'][0])
    sumid1=lastmatch['info']['participants'][0]['summonerId']
    stats1=lol_watcher.league.by_summoner(na,sumid1)
    player1=(lol_watcher.summoner.by_puuid(na,puuid1)['name'])
    champ1=lastmatch['info']['participants'][0]['championName']
    champid1=lastmatch['info']['participants'][0]['championId']
    winrate1=(stats1[0]['wins']/(stats1[0]['wins']+stats1[0]['losses']))*100
    mastery1=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid1,champid1)
    points1=mastery1['championPoints']

    if points1 >= 125000:
        result1="8"
    elif points1 >=90000:
        result1="7"
    elif points1 >=75000:
        result1="6"
    elif points1 >=60000:
        result1="5"
    elif points1 >=45000:
        result1="4"
    elif points1 >=30000:
        result1="3"
    elif points1 >15000:
        result1="2"
    else:
        result1="1"

    puuid2=(lastmatch['metadata']['participants'][1])
    sumid2=lastmatch['info']['participants'][1]['summonerId']
    stats2=lol_watcher.league.by_summoner(na,sumid2)
    player2=(lol_watcher.summoner.by_puuid(na,puuid2)['name'])
    champ2=lastmatch['info']['participants'][1]['championName']
    champid2=lastmatch['info']['participants'][1]['championId']
    winrate2=(stats2[0]['wins']/(stats2[0]['wins']+stats2[0]['losses']))*100
    mastery2=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid2,champid2)
    points2=mastery2['championPoints']
    if points2 >= 125000:
        result2="8"
    elif points2 >=90000:
        result2="7"
    elif points2 >=75000:
        result2="6"
    elif points2 >=60000:
        result2="5"
    elif points2 >=45000:
        result2="4"
    elif points2 >=30000:
        result2="3"
    elif points2 >15000:
        result2="2"
    else:
        result2="1"

    puuid3=(lastmatch['metadata']['participants'][2])
    sumid3=lastmatch['info']['participants'][2]['summonerId']
    stats3=lol_watcher.league.by_summoner(na,sumid3)
    player3=(lol_watcher.summoner.by_puuid(na,puuid3)['name'])
    champ3=lastmatch['info']['participants'][2]['championName']
    champid3=lastmatch['info']['participants'][2]['championId']
    winrate3=(stats3[0]['wins']/(stats3[0]['wins']+stats3[0]['losses']))*100
    mastery3=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid3,champid3)
    points3=mastery3['championPoints']
    if points3 >= 125000:
        result3="8"
    elif points3 >=90000:
        result3="7"
    elif points3 >=75000:
        result3="6"
    elif points3 >=60000:
        result3="5"
    elif points3 >=45000:
        result3="4"
    elif points3 >=30000:
        result3="3"
    elif points3 >15000:
        result3="2"
    else:
        result3="1" 

    puuid4=(lastmatch['metadata']['participants'][3])
    sumid4=lastmatch['info']['participants'][3]['summonerId']
    stats4=lol_watcher.league.by_summoner(na,sumid4)
    player4=(lol_watcher.summoner.by_puuid(na,puuid4)['name'])
    champ4=lastmatch['info']['participants'][3]['championName']
    champid4=lastmatch['info']['participants'][3]['championId']
    winrate4=(stats4[0]['wins']/(stats4[0]['wins']+stats4[0]['losses']))*100
    mastery4=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid4,champid4)
    points4=mastery4['championPoints']
    if points4 >= 125000:
        result4="8"
    elif points4 >=90000:
        result4="7"
    elif points4 >=75000:
        result4="6"
    elif points4 >=60000:
        result4="5"
    elif points4 >=45000:
        result4="4"
    elif points4 >=30000:
        result4="3"
    elif points4 >15000:
        result4="2"
    else:
        result4="1" 

    puuid5=(lastmatch['metadata']['participants'][4])
    sumid5=lastmatch['info']['participants'][4]['summonerId']
    stats5=lol_watcher.league.by_summoner(na,sumid5)
    player5=(lol_watcher.summoner.by_puuid(na,puuid5)['name'])
    champ5=lastmatch['info']['participants'][4]['championName']
    champid5=lastmatch['info']['participants'][4]['championId']
    winrate5=(stats5[0]['wins']/(stats5[0]['wins']+stats5[0]['losses']))*100
    mastery5=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid5,champid5)
    points5=mastery5['championPoints']
    if points5 >= 125000:
        result5="8"
    elif points5 >=90000:
        result5="7"
    elif points5 >=75000:
        result5="6"
    elif points5 >=60000:
        result5="5"
    elif points5 >=45000:
        result5="4"
    elif points5 >=30000:
        result5="3"
    elif points5 >15000:
        result5="2"
    else:
        result5="1" 

    puuid6=(lastmatch['metadata']['participants'][5])
    sumid6=lastmatch['info']['participants'][5]['summonerId']
    stats6=lol_watcher.league.by_summoner(na,sumid6)
    player6=(lol_watcher.summoner.by_puuid(na,puuid6)['name'])
    champ6=lastmatch['info']['participants'][5]['championName']
    champid6=lastmatch['info']['participants'][5]['championId']
    winrate6=(stats6[0]['wins']/(stats6[0]['wins']+stats6[0]['losses']))*100
    mastery6=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid6,champid6)
    points6=mastery6['championPoints']
    if points6 >= 125000:
        result6="8"
    elif points6 >=90000:
        result6="7"
    elif points6 >=75000:
        result6="6"
    elif points6 >=60000:
        result6="5"
    elif points6 >=45000:
        result6="4"
    elif points6 >=30000:
        result6="3"
    elif points6 >15000:
        result6="2"
    else:
        result6="1" 

    puuid7=(lastmatch['metadata']['participants'][6])
    sumid7=lastmatch['info']['participants'][6]['summonerId']
    stats7=lol_watcher.league.by_summoner(na,sumid7)
    player7=(lol_watcher.summoner.by_puuid(na,puuid7)['name'])
    champ7=lastmatch['info']['participants'][6]['championName']
    champid7=lastmatch['info']['participants'][6]['championId']
    winrate7=(stats7[0]['wins']/(stats7[0]['wins']+stats7[0]['losses']))*100
    mastery7=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid7,champid7)
    points7=mastery7['championPoints']
    if points7 >= 125000:
        result7="8"
    elif points7 >=90000:
        result7="7"
    elif points7 >=75000:
        result7="6"
    elif points7 >=60000:
        result7="5"
    elif points7 >=45000:
        result7="4"
    elif points7 >=30000:
        result7="3"
    elif points7 >15000:
        result7="2"
    else:
        result7="1"   

    puuid8=(lastmatch['metadata']['participants'][7])
    sumid8=lastmatch['info']['participants'][7]['summonerId']
    stats8=lol_watcher.league.by_summoner(na,sumid8)
    player8=(lol_watcher.summoner.by_puuid(na,puuid8)['name'])
    champ8=lastmatch['info']['participants'][7]['championName']
    champid8=lastmatch['info']['participants'][7]['championId']
    winrate8=(stats8[0]['wins']/(stats8[0]['wins']+stats8[0]['losses']))*100
    mastery8=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid8,champid8)
    points8=mastery8['championPoints']
    if points8 >= 125000:
        result8="8"
    elif points8 >=90000:
        result8="7"
    elif points8 >=75000:
        result8="6"
    elif points8 >=60000:
        result8="5"
    elif points8 >=45000:
        result8="4"
    elif points8 >=30000:
        result8="3"
    elif points8 >15000:
        result8="2"
    else:
        result8="1"   

    puuid9=(lastmatch['metadata']['participants'][8])
    sumid9=lastmatch['info']['participants'][8]['summonerId']
    stats9=lol_watcher.league.by_summoner(na,sumid9)
    player9=(lol_watcher.summoner.by_puuid(na,puuid9)['name'])
    champ9=lastmatch['info']['participants'][8]['championName']
    champid9=lastmatch['info']['participants'][8]['championId']
    winrate9=(stats9[0]['wins']/(stats9[0]['wins']+stats9[0]['losses']))*100
    mastery9=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid9,champid9)
    points9=mastery4['championPoints']
    if points9 >= 125000:
        result9="8"
    elif points9 >=90000:
        result9="7"
    elif points9 >=75000:
        result9="6"
    elif points9 >=60000:
        result9="5"
    elif points9 >=45000:
        result9="4"
    elif points9 >=30000:
        result9="3"
    elif points9 >15000:
        result9="2"
    else:
        result9="1"     

    puuid10=(lastmatch['metadata']['participants'][9])
    sumid10=lastmatch['info']['participants'][9]['summonerId']
    stats10=lol_watcher.league.by_summoner(na,sumid10)
    player10=(lol_watcher.summoner.by_puuid(na,puuid10)['name'])
    champ10=lastmatch['info']['participants'][9]['championName']
    champid10=lastmatch['info']['participants'][9]['championId']
    winrate10=(stats10[0]['wins']/(stats10[0]['wins']+stats10[0]['losses']))*100
    mastery10=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid10,champid10)
    points10=mastery10['championPoints']

    if points10 >= 125000:
        result10="8"
    elif points10 >=90000:
        result10="7"
    elif points10 >=75000:
        result10="6"
    elif points10 >=60000:
        result10="5"
    elif points10 >=45000:
        result10="4"
    elif points10 >=30000:
        result10="3"
    elif points10 >15000:
        result10="2"
    else:
        result10="1"  

    if lastmatch['info']['teams'][0]['win'] == True:
        winner="Red"
    else:
        winner="Blue"


    print("------------ Match"+str(i+1)+" -------------")
    print("Red Team:\n Player 1: "+player1+" playing "+champ1+", summoner win rate: "+str(round(winrate1,2))+", Champion experience: "+result1+", Champion Winrate: "+str(51))
    print(" Player 2: "+player2+" playing "+champ2+", summoner win rate: "+str(round(winrate2,2))+", Champion experience: "+result2+", Champion Winrate: "+str(51))
    print(" Player 3: "+player3+" playing "+champ3+", summoner win rate: "+str(round(winrate3,2))+", Champion experience: "+result3+", Champion Winrate: "+str(51))
    print(" Player 4: "+player4+" playing "+champ4+", summoner win rate: "+str(round(winrate4,2))+", Champion experience: "+result4+", Champion Winrate: "+str(51))
    print(" Player 5: "+player5+" playing "+champ5+", summoner win rate: "+str(round(winrate5,2))+", Champion experience: "+result5+", Champion Winrate: "+str(51))
    print("Blue Team:\n Player 1: "+player6+" playing "+champ6+", summoner win rate: "+str(round(winrate6,2))+", Champion experience: "+result6+", Champion Winrate: "+str(51))
    print(" Player 2: "+player7+" playing "+champ7+", summoner win rate: "+str(round(winrate7,2))+", Champion experience: "+result7+", Champion Winrate: "+str(51))
    print(" Player 3: "+player8+" playing "+champ8+", summoner win rate: "+str(round(winrate8,2))+", Champion experience: "+result8+", Champion Winrate: "+str(51))
    print(" Player 4: "+player9+" playing "+champ9+", summoner win rate: "+str(round(winrate9,2))+", Champion experience: "+result9+", Champion Winrate: "+str(51))
    print(" Player 5: "+player10+" playing "+champ10+", summoner win rate: "+str(round(winrate10,2))+", Champion experience: "+result10+", Champion Winrate: "+str(51)+"\n")
    print("Winning Team: "+winner+"\n")

    data=[str(round(winrate1,2)),result1,champ1,str(round(winrate2,2)),result2,champ2,str(round(winrate3,2)),result3,champ3,str(round(winrate4,2)),result4,champ4,str(round(winrate5,2)),result5,champ5,str(round(winrate6,2)),result6,champ6,str(round(winrate7,2)),result7,champ7,str(round(winrate8,2)),result8,champ8,str(round(winrate9,2)),result9,champ9,str(round(winrate10,2)),result10,champ10,winner]

    writer.writerow(data)