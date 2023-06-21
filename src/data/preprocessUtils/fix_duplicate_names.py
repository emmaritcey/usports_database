import pandas as pd
import numpy as np

#duplciate names and indices found manually in another notebook
#if updates to data is made, must check that these indices haven't changed

def run():
    df1 = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/player_stats_info.csv')
    df2 = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/player_stats_ball_control.csv')
    df3 = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/player_stats_shooting.csv')

    df1[df1['NAME']=='Emma Thompson']
    idx_list1 = [3984,4643,5310,5975,6645]
    df1.loc[idx_list1,'NAME'] = 'Emma Thompson2'
    df2.loc[idx_list1,'NAME'] = 'Emma Thompson2'
    df3.loc[idx_list1,'NAME'] = 'Emma Thompson2'

    df2[df2['NAME']=='Emma Johnson']
    idx_list2 = [5192,5862,6527]
    df1.loc[idx_list2,'NAME'] = 'Emma Johnson2'
    df2.loc[idx_list2,'NAME'] = 'Emma Johnson2'
    df3.loc[idx_list2,'NAME'] = 'Emma Johnson2'

    df2[df2['NAME']=='Mackenzie Robinson']
    idx_list3 = [3642]
    df1.loc[idx_list3, 'NAME'] = 'Mackenzie Robinson2'
    df2.loc[idx_list3, 'NAME'] = 'Mackenzie Robinson2'
    df3.loc[idx_list3, 'NAME'] = 'Mackenzie Robinson2'

    idx_list4 = [6806, 7534]
    df1.loc[idx_list4, 'NAME'] = 'Amelie Bouchard'
    df2.loc[idx_list4, 'NAME'] = 'Amelie Bouchard'
    df3.loc[idx_list4, 'NAME'] = 'Amelie Bouchard'

    idx_list5 = [6257]
    df1.loc[idx_list5, 'NAME'] = 'Maeva Courla'
    df2.loc[idx_list5, 'NAME'] = 'Maeva Courla'
    df3.loc[idx_list5, 'NAME'] = 'Maeva Courla'
    
    idx_list6 = [5433]
    df1.loc[idx_list6, 'NAME'] = 'Megan Stewart2'
    df2.loc[idx_list6, 'NAME'] = 'Megan Stewart2'
    df3.loc[idx_list6, 'NAME'] = 'Megan Stewart2'
    
    #maria Lambropoulos is listed on two teams usports rosters but not on concordia website
    idx_list7 = [6941]
    df1 = df1.drop(idx_list7)
    df2 = df2.drop(idx_list7)
    df3 = df3.drop(idx_list7)

    df1.to_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/duplicates_removed/player_stats_info.csv', index=False)
    df2.to_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/duplicates_removed/player_stats_ball_control.csv', index=False)
    df3.to_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/duplicates_removed/player_stats_shooting.csv', index=False)

run()
