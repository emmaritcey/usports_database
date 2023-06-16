#%%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/player_stats_info.csv')
df
# %%
df[df['NAME']=='Emma Thompson2']
# %%
df.loc[[2613,3233,3907],'NAME'] = 'Emma Thompson'
df[df['NAME']=='Emma Thompson']
# %%
df[df['NAME']=='Emma Johnson']
# %%
df.loc[[5197,5868,6536],'NAME'] = 'Emma Johnson2'
df[df['NAME']=='Emma Johnson']
# %%
df[df['NAME']=='Emma Johnson2']
#%%
df.loc[6815, 'NAME'] = 'Amelie Bouchard'
# %%
df.to_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/player_stats_info2.csv', index=False)
# %%
df.loc[6815]
# %%
