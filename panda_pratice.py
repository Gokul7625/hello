import pandas as pd
data = {"name": ["gk", "mara","d","f","gg","dg"], "age": [20, 20,3,6,7,8]}
df = pd.DataFrame(data)
print(df.info())