from riotwatcher import LolWatcher, ApiError

#Must enter Riot API to run
lol_watcher = LolWatcher('XXX-XXX-XXX-XXX')
na = 'na1'
me = lol_watcher.summoner.by_name(na,'openbackpack')

matches= lol_watcher.match.matchlist_by_puuid('americas',me['puuid'],None,10,None,'ranked',None,None)

lastmatch= lol_watcher.match.by_id('americas',matches[0])

puuid1=(lastmatch['metadata']['participants'][3])
player1=(lol_watcher.summoner.by_puuid(na,puuid1)['name'])
p1data=lastmatch['info']['participants'][0]['championName']
sumid1=lastmatch['info']['participants'][0]['summonerId']
champid1=lastmatch['info']['participants'][0]['championId']
puuidtosum=lol_watcher.champion_mastery.by_summoner_by_champion(na,sumid1,champid1)
points=puuidtosum['championPoints']
if points >= 21600:
    result="Level 5+ - Master"
elif points >=12600:
    result="Level 4 - Decent"
elif points >=6000:
    result="Level 3 - Mediocre"
elif points >1800:
    result="Level 2 - Getting there"
else:
    result="Level 1 - Noob"

print(player1+" is "+result+" at "+p1data)
