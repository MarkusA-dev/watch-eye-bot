import json

#GuildId -> ChannelId -> list of watched users
jsonstr = {"guildId": { "channelId": [ 203491, 12830120933, 12938719827, 29937661987 ]}}


data = json.dumps(jsonstr, indent=4)


#list of watched users
print(jsonstr["guildId"]["channelId"])