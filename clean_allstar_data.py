import pandas as pd

def main():
    df = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/all_stars.csv', 
                     columns=['Season', 'Name', 'School',  'Conference', 'allstar_team'])
    
    
    #remove all capitals and spaces from shool names
    df['School'] = df['School'].str.lower()
    df['School'] = df['School'].str.replace(" ", "")
    
    
    df.loc[ df['Name'] == 'Justine Colley-Leger', 'Name'] = 'Justine Colley'
    
    
    
    
    
    
    
main()