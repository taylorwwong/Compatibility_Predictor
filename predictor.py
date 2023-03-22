import json
import numpy as np

# load file
data = json.load(open('input.json'))

# setup lists
team_total = []
app_total = []
app_names = []
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
    app_names.append(i['name'])

# find mean for team
avg_team = np.mean(team_total)

# find compatibility and add to dict
for i in app_total:
    temp = avg_team - i
    comp = (10 - abs(temp))/10
    result.append(comp)

# output data
output = {
    "scoredApplicants":[
        {
            "name": f'{app_names[0]}',
            "score": f'{result[0]}'
        },
        {
            "name": f'{app_names[1]}',
            "score": f'{result[1]}'
        },
        {
            "name": f'{app_names[2]}',
            "score": f'{result[2]}'
        }
    ]
}

# write to json
with open('output.json', 'w') as out:
    json.dump(output, out)
