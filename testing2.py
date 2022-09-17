import json
annot_file_path = '1.json'

with open(annot_file_path, 'r') as f:
		data = json.load(f)
# print(data)
member = data['shapes'][0]
print(member)
label = [member['label']]
grid = member['points']

print(label, grid[0])
 
 # 폴더 구조
#  classification = data['classificationdata -> train[hz, bz 폴더 밑 데이터], '] // OD [data -> train[img,label]] 6 2 2
