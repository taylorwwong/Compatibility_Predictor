import json
import numpy as np

# load file
data = json.load(open('input.json'))

# setup lists
team_total = []
app_total = []
result = []

# loop through json
for i in data['team']:
    intel = (i['attributes']['intelligence'])
    spicy = (i['attributes']['spicyFoodTolerance'])
    combined = int(intel) + int(spicy)
    team_total.append(int(combined))

for i in data['applicants']:
    intel = (i['attributes']['intelligence'])
    spicy = (i['attributes']['spicyFoodTolerance'])
    combined = int(intel) + int(spicy)
    app_total.append(int(combined))

# find mean for team
avg_team = np.mean(team_total)

# find compatibility
for i in app_total:
    temp = avg_team - i
    comp = (10 - abs(temp))/10
    result.append(comp)




# write to json
with open('output.json', 'w') as out:
    out.write(obj)

print(team_total)
print(avg_team)
print(app_total)
print(result)