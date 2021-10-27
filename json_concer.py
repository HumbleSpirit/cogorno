#import pandas as pd
#df = pd.read_json ('Backswing-Mechanics.json')
#print(df)
#df.to_csv ('Backswing-Mechanics.csv', index = None)
import json
from pandas.io.json import json_normalize
with open ('Backswing-Mechanics.json') as json_data:
    data = json.load(json_data)
print(data)
df=pd.DataFrame(contents[''])
print(df[contentable])