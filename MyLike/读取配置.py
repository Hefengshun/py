import json
with open('config.json', 'r', encoding='utf8')as fp:
    allJson =  json.load(fp)
    idsList = allJson['idsList']
print(allJson,idsList)
for i,item in enumerate(idsList):
    print(i,item,idsList[i])
# all= cfg.get()
# print(all)
