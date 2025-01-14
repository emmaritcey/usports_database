import pandas as pd
import numpy as np
import os

#duplciate names and indices found manually in another notebook
#if updates to data is made, must check that these indices haven't changed


def fix_first_names(df1):
       #fix names where only first initial is recorded
    df1.loc[df1['NAME'] == 'R Atkinson', 'NAME'] = 'Rashida Atkinson'
    df1.loc[df1['NAME'] == 'J Stratton', 'NAME'] = 'Jill Stratton'
    df1.loc[df1['NAME'] == 'J. Stratton', 'NAME'] = 'Jill Stratton'
    df1.loc[df1['NAME'] == 'J Longauer', 'NAME'] = 'Julie Longauer'
    df1.loc[df1['NAME'] == 'J. Longauer', 'NAME'] = 'Julie Longauer'
    df1.loc[df1['NAME'] == 'D Dewards', 'NAME'] = 'Diedre Edwards'
    df1.loc[df1['NAME'] == 'V Wallace', 'NAME'] = 'Vanessa Wallace'
    df1.loc[df1['NAME'] == 'M Baker', 'NAME'] = 'Maddy Baker'
    df1.loc[df1['NAME'] == 'A Addo', 'NAME'] = 'Abena Addo'
    df1.loc[df1['NAME'] == 'L Bailey', 'NAME'] = 'Liane Bailey'
    df1.loc[df1['NAME'] == 'L. Bailey', 'NAME'] = 'Liane Bailey'
    df1.loc[df1['NAME'] == 'J Gaunt', 'NAME'] = 'Jay Gaunt'
    df1.loc[df1['NAME'] == 'E Piccini', 'NAME'] = 'Emily Piccini'
    df1.loc[df1['NAME'] == 'A Garner', 'NAME'] = 'Alanna Garner'
    df1.loc[df1['NAME'] == 'S Acolatse', 'NAME'] = 'Selali Acolatse'
    df1.loc[df1['NAME'] == 'A Van Kampen', 'NAME'] = 'Alicia Van Kampen'
    df1.loc[df1['NAME'] == 'R Sider', 'NAME'] = 'Rachel Sider'
    df1.loc[df1['NAME'] == 'K Chute', 'NAME'] = 'Kristy Chute'
    df1.loc[df1['NAME'] == 'V Brathwaite', 'NAME'] = 'Vanessa Brathwaite'
    df1.loc[df1['NAME'] == 'C. Quinlan', 'NAME'] = 'Collen Quinlan'
    df1.loc[df1['NAME'] == 'E. Tilley', 'NAME'] = 'Erin Tilley'
    df1.loc[df1['NAME'] == 'L. Bossers', 'NAME'] = 'Laura Bossers'
    df1.loc[df1['NAME'] == 'S. Brathwaite', 'NAME'] = 'Sabrina Brathwaite'
    df1.loc[df1['NAME'] == 'S. Hickey', 'NAME'] = 'Saraya Hickey'
    df1.loc[df1['NAME'] == 'T. Lee', 'NAME'] = 'Tori Lee'
    df1.loc[df1['NAME'] == 'J. Medri', 'NAME'] = 'Joanna Medri'
    df1.loc[df1['NAME'] == 'E. McNeely', 'NAME'] = 'Erin McNeely'
    df1.loc[df1['NAME'] == 'M. Stoncius', 'NAME'] = 'Megan Stoncius'
    df1.loc[df1['NAME'] == 'K. Menton', 'NAME'] = 'Kristina Menton'
    df1.loc[df1['NAME'] == 'A. Van kampen', 'NAME'] = 'Alicia Van Kampen'
    df1.loc[df1['NAME'] == 'Alicia Van kampen', 'NAME'] = 'Alicia Van Kampen'
    df1.loc[df1['NAME'] == 'R. Sider', 'NAME'] = 'Rachael Sider'
    df1.loc[df1['NAME'] == 'A. Lauzon', 'NAME'] = 'Amanda Lauzon'
    df1.loc[df1['NAME'] == 'K. McConnell', 'NAME'] = 'Katelyn'
    df1.loc[df1['NAME'] == 'N. Schutz', 'NAME'] = 'Nicki Schutz'
    df1.loc[df1['NAME'] == 'S. Pierce', 'NAME'] = 'Sherri Piere'
    df1.loc[df1['NAME'] == 'L Boag', 'NAME'] = 'Liz Boag'
    df1.loc[df1['NAME'] == 'P Robinson', 'NAME'] = 'Paige Robinson'
    df1.loc[df1['NAME'] == 'R Urosevic', 'NAME'] = 'Rachael Urosevic'
    df1.loc[df1['NAME'] == 'B Moore', 'NAME'] = 'Brittany Moore'
    df1.loc[df1['NAME'] == 'L Minutillo', 'NAME'] = 'Lisa Minutillo'
    df1.loc[df1['NAME'] == 'G Bullard', 'NAME'] = 'Gemma Bullard'
    df1.loc[df1['NAME'] == 'L Bailey', 'NAME'] = 'Liane Bailey'
    df1.loc[df1['NAME'] == 'M MacDougall', 'NAME'] = 'Meaghan MacDougall'
    df1.loc[df1['NAME'] == 'L Bailey', 'NAME'] = 'Liane Bailey'
    df1.loc[df1['NAME'] == 'C Wallace', 'NAME'] = 'Christine Wallace'
    df1.loc[df1['NAME'] == 'S Kernahan', 'NAME'] = 'Sydney Kernahan'
    df1.loc[df1['NAME'] == 'J Tomas', 'NAME'] = 'Jordan Tomas'
    df1.loc[df1['NAME'] == 'H Koposhynska', 'NAME'] = 'Hanna Koposhynska'
    df1.loc[df1['NAME'] == 'J Wheat', 'NAME'] = 'Jill Wheat'
    df1.loc[df1['NAME'] == 'R Beddoe', 'NAME'] = 'Ryley Beddoe'
    df1.loc[df1['NAME'] == 'M. Ferland', 'NAME'] = 'Marjorie Ferland'
    df1.loc[df1['NAME'] == 'E. Jobin', 'NAME'] = 'Elyse Jobin'
    df1.loc[df1['NAME'] == 'M-L F-Laberge', 'NAME'] = 'Marie-L F.-Laberge'
    df1.loc[df1['NAME'] == 'M-M Genois', 'NAME'] = 'Marie-Mich. Genois'
    df1.loc[df1['NAME'] == 'S. Ducruc', 'NAME'] = 'Sandrine Ducruc'
    df1.loc[df1['NAME'] == 'M. L-Dion', 'NAME'] = 'Melodie Laniel-Dion'
    df1.loc[df1['NAME'] == 'Melodie Laniel dion', 'NAME'] = 'Melodie Laniel-Dion'
    df1.loc[df1['NAME'] == 'C. St-Amour', 'NAME'] = 'Chanelle St-Amour'
    df1.loc[df1['NAME'] == 'M-P Nadeau', 'NAME'] = 'Marie-Pascale Nadeau'
    
    return df1
    
    

def run():
    df1 = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/player_stats_info.csv')
    df2 = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/player_stats_ball_control.csv')
    df3 = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/player_stats_shooting.csv')

    #df1[df1['NAME']=='Emma Thompson']
    idx_list1 = [3984,4643,5310,5975,6645]
    df1.loc[idx_list1,'NAME'] = 'Emma Thompson2'
    df2.loc[idx_list1,'NAME'] = 'Emma Thompson2'
    df3.loc[idx_list1,'NAME'] = 'Emma Thompson2'

    #df2[df2['NAME']=='Emma Johnson']
    idx_list2 = [5192,5862,6527]
    df1.loc[idx_list2,'NAME'] = 'Emma Johnson2'
    df2.loc[idx_list2,'NAME'] = 'Emma Johnson2'
    df3.loc[idx_list2,'NAME'] = 'Emma Johnson2'

    #df2[df2['NAME']=='Mackenzie Robinson']
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
    
    #fix names where first name is just first initial
    df1 = fix_first_names(df1)
    df2 = fix_first_names(df2)
    df3 = fix_first_names(df3)
    
    #Toronto 2015, 2014: Ducharme, Lewin, Laurin
    save_path = '/Users/emmaritcey/Documents/basketball_research/usports_database/data/duplicates_removed'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
        
    df1.to_csv(save_path + '/player_stats_info.csv', index=False)
    df2.to_csv(save_path + '/player_stats_ball_control.csv', index=False)
    df3.to_csv(save_path + '/player_stats_shooting.csv', index=False)

run()
