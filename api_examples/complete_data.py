from riotwatcher import LolWatcher, ApiError

#Must enter Riot API to run
lol_watcher = LolWatcher('XXX-XXX-XXX-XXX')
na = 'na1'
me = lol_watcher.summoner.by_name(na,'openbackpack')

matches= lol_watcher.match.matchlist_by_puuid('americas',me['puuid'],None,10,None,'ranked',None,None)
lastmatch= lol_watcher.match.by_id('americas',matches[2])

#calls for summoner 1
puuid1=(lastmatch['metadata']['participants'][0])
sumid1=lastmatch['info']['participants'][0]['summonerId']
stats1=lol_watcher.league.by_summoner(na,sumid1)
player1=(lol_watcher.summoner.by_puuid(na,puuid1)['name'])
champ1=lastmatch['info']['participants'][0]['championName']
champid1=lastmatch['info']['participants'][0]['championId']
winrate1=(stats1[0]['wins']/(stats1[0]['wins']+stats1[0]['losses']))*100
mastery1=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid1,champid1)
points1=mastery1['championPoints']
if points1 >= 21600:
    result1="Level 5+ - Master"
elif points1 >=12600:
    result1="Level 4 - Decent"
elif points1 >=6000:
    result1="Level 3 - Mediocre"
elif points1 >1800:
    result1="Level 2 - Getting there"
else:
    result1="Level 1 - Noob"

puuid2=(lastmatch['metadata']['participants'][1])
sumid2=lastmatch['info']['participants'][1]['summonerId']
stats2=lol_watcher.league.by_summoner(na,sumid2)
player2=(lol_watcher.summoner.by_puuid(na,puuid2)['name'])
champ2=lastmatch['info']['participants'][1]['championName']
champid2=lastmatch['info']['participants'][1]['championId']
winrate2=(stats2[0]['wins']/(stats2[0]['wins']+stats2[0]['losses']))*100
mastery2=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid2,champid2)
points2=mastery2['championPoints']
if points2 >= 21600:
    result2="Level 5+ - Master"
elif points2 >=12600:
    result2="Level 4 - Decent"
elif points2 >=6000:
    result2="Level 3 - Mediocre"
elif points2 >1800:
    result2="Level 2 - Getting there"
else:
    result2="Level 1 - Noob"

puuid3=(lastmatch['metadata']['participants'][2])
sumid3=lastmatch['info']['participants'][2]['summonerId']
stats3=lol_watcher.league.by_summoner(na,sumid3)
player3=(lol_watcher.summoner.by_puuid(na,puuid3)['name'])
champ3=lastmatch['info']['participants'][2]['championName']
champid3=lastmatch['info']['participants'][2]['championId']
winrate3=(stats3[0]['wins']/(stats3[0]['wins']+stats3[0]['losses']))*100
mastery3=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid3,champid3)
points3=mastery3['championPoints']
if points3 >= 21600:
    result3="Level 5+ - Master"
elif points3 >=12600:
    result3="Level 4 - Decent"
elif points3 >=6000:
    result3="Level 3 - Mediocre"
elif points3 >1800:
    result3="Level 2 - Getting there"
else:
    result3="Level 1 - Noob"

puuid4=(lastmatch['metadata']['participants'][3])
sumid4=lastmatch['info']['participants'][3]['summonerId']
stats4=lol_watcher.league.by_summoner(na,sumid4)
player4=(lol_watcher.summoner.by_puuid(na,puuid4)['name'])
champ4=lastmatch['info']['participants'][3]['championName']
champid4=lastmatch['info']['participants'][3]['championId']
winrate4=(stats4[0]['wins']/(stats4[0]['wins']+stats4[0]['losses']))*100
mastery4=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid4,champid4)
points4=mastery4['championPoints']
if points4 >= 21600:
    result4="Level 5+ - Master"
elif points4 >=12600:
    result4="Level 4 - Decent"
elif points4 >=6000:
    result4="Level 3 - Mediocre"
elif points4 >1800:
    result4="Level 2 - Getting there"
else:
    result4="Level 1 - Noob"    

puuid5=(lastmatch['metadata']['participants'][4])
sumid5=lastmatch['info']['participants'][4]['summonerId']
stats5=lol_watcher.league.by_summoner(na,sumid5)
player5=(lol_watcher.summoner.by_puuid(na,puuid5)['name'])
champ5=lastmatch['info']['participants'][4]['championName']
champid5=lastmatch['info']['participants'][4]['championId']
winrate5=(stats5[0]['wins']/(stats5[0]['wins']+stats5[0]['losses']))*100
mastery5=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid5,champid5)
points5=mastery5['championPoints']
if points5 >= 21600:
    result5="Level 5+ - Master"
elif points5 >=12600:
    result5="Level 4 - Decent"
elif points5 >=6000:
    result5="Level 3 - Mediocre"
elif points5 >1800:
    result5="Level 2 - Getting there"
else:
    result5="Level 1 - Noob"   

puuid6=(lastmatch['metadata']['participants'][5])
sumid6=lastmatch['info']['participants'][5]['summonerId']
stats6=lol_watcher.league.by_summoner(na,sumid6)
player6=(lol_watcher.summoner.by_puuid(na,puuid6)['name'])
champ6=lastmatch['info']['participants'][5]['championName']
champid6=lastmatch['info']['participants'][5]['championId']
winrate6=(stats6[0]['wins']/(stats6[0]['wins']+stats6[0]['losses']))*100
mastery6=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid6,champid6)
points6=mastery6['championPoints']
if points6 >= 21600:
    result6="Level 5+ - Master"
elif points6 >=12600:
    result6="Level 4 - Decent"
elif points6 >=6000:
    result6="Level 3 - Mediocre"
elif points6 >1800:
    result6="Level 2 - Getting there"
else:
    result6="Level 1 - Noob"

puuid7=(lastmatch['metadata']['participants'][6])
sumid7=lastmatch['info']['participants'][6]['summonerId']
stats7=lol_watcher.league.by_summoner(na,sumid7)
player7=(lol_watcher.summoner.by_puuid(na,puuid7)['name'])
champ7=lastmatch['info']['participants'][6]['championName']
champid7=lastmatch['info']['participants'][6]['championId']
winrate7=(stats7[0]['wins']/(stats7[0]['wins']+stats7[0]['losses']))*100
mastery7=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid7,champid7)
points7=mastery7['championPoints']
if points7 >= 21600:
    result7="Level 5+ - Master"
elif points7 >=12600:
    result7="Level 4 - Decent"
elif points7 >=6000:
    result7="Level 3 - Mediocre"
elif points7 >1800:
    result7="Level 2 - Getting there"
else:
    result7="Level 1 - Noob"

puuid8=(lastmatch['metadata']['participants'][7])
sumid8=lastmatch['info']['participants'][7]['summonerId']
stats8=lol_watcher.league.by_summoner(na,sumid8)
player8=(lol_watcher.summoner.by_puuid(na,puuid8)['name'])
champ8=lastmatch['info']['participants'][7]['championName']
champid8=lastmatch['info']['participants'][7]['championId']
winrate8=(stats8[0]['wins']/(stats8[0]['wins']+stats8[0]['losses']))*100
mastery8=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid8,champid8)
points8=mastery8['championPoints']
if points8 >= 21600:
    result8="Level 5+ - Master"
elif points8 >=12600:
    result8="Level 4 - Decent"
elif points8 >=6000:
    result8="Level 3 - Mediocre"
elif points8 >1800:
    result8="Level 2 - Getting there"
else:
    result8="Level 1 - Noob"

puuid9=(lastmatch['metadata']['participants'][8])
sumid9=lastmatch['info']['participants'][8]['summonerId']
stats9=lol_watcher.league.by_summoner(na,sumid9)
player9=(lol_watcher.summoner.by_puuid(na,puuid9)['name'])
champ9=lastmatch['info']['participants'][8]['championName']
champid9=lastmatch['info']['participants'][8]['championId']
winrate9=(stats9[0]['wins']/(stats9[0]['wins']+stats9[0]['losses']))*100
mastery9=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid9,champid9)
points9=mastery4['championPoints']
if points9 >= 21600:
    result9="Level 5+ - Master"
elif points9 >=12600:
    result9="Level 4 - Decent"
elif points9 >=6000:
    result9="Level 3 - Mediocre"
elif points9 >1800:
    result9="Level 2 - Getting there"
else:
    result9="Level 1 - Noob"    

puuid10=(lastmatch['metadata']['participants'][9])
sumid10=lastmatch['info']['participants'][9]['summonerId']
stats10=lol_watcher.league.by_summoner(na,sumid10)
player10=(lol_watcher.summoner.by_puuid(na,puuid10)['name'])
champ10=lastmatch['info']['participants'][9]['championName']
champid10=lastmatch['info']['participants'][9]['championId']
winrate10=(stats10[0]['wins']/(stats10[0]['wins']+stats10[0]['losses']))*100
mastery10=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid10,champid10)
points10=mastery10['championPoints']
if points10 >= 21600:
    result10="Level 5+ - Master"
elif points10 >=12600:
    result10="Level 4 - Decent"
elif points10 >=6000:
    result10="Level 3 - Mediocre"
elif points10 >1800:
    result10="Level 2 - Getting there"
else:
    result10="Level 1 - Noob"  

if lastmatch['info']['teams'][0]['win'] == True:
    winner="Red Team"
else:
    winner="Blue Team"


print("------------ Match 1 -------------")
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
