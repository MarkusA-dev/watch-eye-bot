import json


#GuildId -> ChannelId -> list of watched users
jsonstr = {"guildId": { "channelId": [ 203491, 12830120933, 12938719827, 29937661987 ]}}


#list of watched users
print(jsonstr["guildId"]["channelId"])

def writejson(newdata, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["servers"].update(newdata)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def addserver(server, channel, users=None, data=jsonstr):
    if users == None:
        apdStr = {server: {channel: []}}
    else:
        apdStr = {server: {channel: [users]}}
    writejson(apdStr)

    

addserver("test22", "test32")

with open('data.json') as read:
    obj = json.load(read)
    print(json.dumps(obj, indent=4))
