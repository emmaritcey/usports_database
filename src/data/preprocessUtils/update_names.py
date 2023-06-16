import pandas as pd

def run():
    df = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/raw/all_stars.csv')
    
    
    #remove all capitals and spaces from shool names
    df['School'] = df['School'].str.lower()
    df['School'] = df['School'].str.replace(" ", "")
    df = df[df['Name']!='Robyn Buna']
    
    df.to_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/all_stars.csv',
              index=False)
    
    df = pd.read_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/players.csv')
    
    df.loc[ df['NAME'] == 'Justine Colley', 'NAME'] = 'Justine Colley-Leger'
    df.loc[ df['NAME'] == 'Lia St. pierre', 'NAME'] = 'Lia St. Pierre'
    df.loc[ df['NAME'] == 'Susanne Canvin', 'NAME'] = 'Susanne Canvin Morrison'
    df.loc[ df['NAME'] == 'Karla Yepez', 'NAME'] = 'Karla Yepez Villamorin'
    df.loc[ df['NAME'] == 'Lyndsay DeGroot', 'NAME'] = 'Lyndsay DeGroot Sutherland'
    df.loc[ df['NAME'] == 'Kim Tulloch', 'NAME'] = 'Kimberley Tulloch'
    df.loc[ df['NAME'] == 'Saskia Van ginhoven', 'NAME'] = 'Saskia Van Ginhoven'
    df.loc[ df['NAME'] == 'Tessa Ratzlaff', 'NAME'] = 'Tessa Ratzlaff Allison'
    df.loc[ df['NAME'] == 'Harlem Sidhu', 'NAME'] = 'Harlem Sidhu Dulay'
    df.loc[ df['NAME'] == 'Jess Brown', 'NAME'] = 'Jessica Brown'
    df.loc[ df['NAME'] == 'Mackenzie Farmer', 'NAME'] = 'MacKenzie Farmer'
    df.loc[ df['NAME'] == 'Lisa Furchner', 'NAME'] = 'Lisa Furchner Carruthers'
    df.loc[ df['NAME'] == 'Sasha Polishchuk', 'NAME'] = 'Alexandra (Sasha) Polishchuk'
    df.loc[ df['NAME'] == 'Maddy Horst', 'NAME'] = 'Madison Horst'
    df.loc[ df['NAME'] == 'Hailey Milligan', 'NAME'] = 'Hailey Milligan-Jones'
    df.loc[ df['NAME'] == 'Bojana Kovacevic', 'NAME'] = 'Bojana Kovacevic Glisic'
    df.loc[ df['NAME'] == 'M-M Genois', 'NAME'] = 'Marie-Michelle Genois'
    df.loc[ df['NAME'] == 'Michelle A-Bellemare', 'NAME'] = 'Michelle Auger-Bellemare'
    df.loc[ df['NAME'] == 'Alex Kiss-Rusk', 'NAME'] = 'Alexandia Kiss-Rusk'
    df.loc[ df['NAME'] == 'Khaleann C.-Goudreau', 'NAME'] = 'Khaleann Caron-Goudreau'
    
    df.to_csv('/Users/emmaritcey/Documents/basketball_research/usports_database/data/processed/players.csv', 
              index=False)
    