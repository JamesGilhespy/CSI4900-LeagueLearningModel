from riotwatcher import LolWatcher, ApiError

#Must enter Riot API to run
lol_watcher = LolWatcher('RGAPI-xxxxx-xxxxxx-xxxxx-xxxx')
na = 'na1'
me = lol_watcher.summoner.by_name(na,'openbackpack')

matches= lol_watcher.match.matchlist_by_puuid('americas',me['puuid'],None,10,None,'ranked',None,None)
#
for i in range(len(matches)):
    lastmatch= lol_watcher.match.by_id('americas',matches[i])

    puuid1=(lastmatch['metadata']['participants'][0])
    puuid2=(lastmatch['metadata']['participants'][1])
    puuid3=(lastmatch['metadata']['participants'][2])
    puuid4=(lastmatch['metadata']['participants'][3])
    puuid5=(lastmatch['metadata']['participants'][4])
    puuid6=(lastmatch['metadata']['participants'][5])
    puuid7=(lastmatch['metadata']['participants'][6])
    puuid8=(lastmatch['metadata']['participants'][7])
    puuid9=(lastmatch['metadata']['participants'][8])
    puuid10=(lastmatch['metadata']['participants'][9])

    player1=(lol_watcher.summoner.by_puuid(na,puuid1)['name'])
    player2=(lol_watcher.summoner.by_puuid(na,puuid2)['name'])
    player3=(lol_watcher.summoner.by_puuid(na,puuid3)['name'])
    player4=(lol_watcher.summoner.by_puuid(na,puuid4)['name'])
    player5=(lol_watcher.summoner.by_puuid(na,puuid5)['name'])
    player6=(lol_watcher.summoner.by_puuid(na,puuid6)['name'])
    player7=(lol_watcher.summoner.by_puuid(na,puuid7)['name'])
    player8=(lol_watcher.summoner.by_puuid(na,puuid8)['name'])
    player9=(lol_watcher.summoner.by_puuid(na,puuid9)['name'])
    player10=(lol_watcher.summoner.by_puuid(na,puuid10)['name'])

    p1data=lastmatch['info']['participants'][0]['championName']
    p2data=lastmatch['info']['participants'][1]['championName']
    p3data=lastmatch['info']['participants'][2]['championName']
    p4data=lastmatch['info']['participants'][3]['championName']
    p5data=lastmatch['info']['participants'][4]['championName']
    p6data=lastmatch['info']['participants'][5]['championName']
    p7data=lastmatch['info']['participants'][6]['championName']
    p8data=lastmatch['info']['participants'][7]['championName']
    p9data=lastmatch['info']['participants'][8]['championName']
    p10data=lastmatch['info']['participants'][9]['championName']
    if lastmatch['info']['teams'][0]['win'] == True:
        winner="Blue Team"
    else:
        winner="Red Team"
    print("----------- MATCH "+str(i+1)+"-----------")
    print("Blue Team:\n Top: "+player1+" playing "+p1data+"\n Jungle: "+player2+" playing "+p2data+"\n Middle: "+player3+" playing "+p3data+"\n ADC: "+player4+" playing "+p4data+"\n Support: "+player5+" playing "+p5data+"\nRed Team:\n Top: "+player6+" playing "+p6data+"\n Jungle: "+player7+" playing "+p7data+"\n Middle: "+player8+" playing "+p8data+"\n ADC: "+player9+" playing "+p9data+"\n Support: "+player10+" playing "+p10data+"\n")
    print("Winning Team:"+winner+"\n")
    
