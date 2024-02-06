import pandas as pd
# read data Json
df_participant = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqthon-participants.csv')

# create Postal code
df_participant['postal_code'] = df_participant['address'].str.extract(r'(\d+)$')
# Diasumsikan kota merupakan sekumpulan karakter yang terdapat setelah nomor jalan diikuti dengan \n (newline character) atau dalam bahasa lainnya yaitu enter.
df_participant['city'] = df_participant['address'].str.extract(r'(?<=\n)(\w.+)(?=,)') 
#profil github mereka merupakan gabungan dari first_name dan last_name yang sudah di-lowercase. 
df_participant['github_profile'] = 'https://github.com/' + df_participant['first_name'].str.lower() + df_participant['last_name'].str.lower()

df_participant['cleaned_phone_number'] = df_participant['phone_number'].str.replace(r'^(\+62|62)', '0', regex=True)
df_participant['cleaned_phone_number'] = df_participant['cleaned_phone_number'].str.replace(r'[()-]', '', regex=True)
df_participant['cleaned_phone_number'] = df_participant['cleaned_phone_number'].str.replace(r'\s+', '', regex=True)

# team name

def func(col):
    abbrev_name = "%s%s"%(col['first_name'][0],col['last_name'][0])
    country = col['country']
    abbrev_institute = '%s'%(''.join(list(map(lambda word: word[0], col['institute'].split()))))
    return "%s-%s-%s"%(abbrev_name,country,abbrev_institute)
df_participant['team_name'] = df_participant.apply(func, axis=1)

def func(col):
    first_name_lower = col['first_name'].lower()
    last_name_lower = col['last_name'].lower()
    institute = ''.join(list(map(lambda word: word[0], col['institute'].lower().split())))
    
    if 'Universitas' in col['institute']:
        if len(col['country'].split()) > 1:
            country = ''.join(list(map(lambda word: word[0], col['country'].lower().split())))
        else:
            country = col['country'][:3].lower()
        return "%s%s@%s.ac.%s"%(first_name_lower,last_name_lower,institute,country)
        
    return "%s%s@%s.com"%(first_name_lower,last_name_lower,institute)
    
df_participant['email'] = df_participant.apply(func, axis=1)

#df_participant['birth_date'] = pd.to_datetime(df_participant['birth_date'], format='%d %b %Y')
df_participant['birth_date'] = pd.to_datetime(df_participant['birth_date'], format='%d %b %Y')
df_participant['birth_date'] = df_participant['birth_date'].dt.strftime('%Y-%m-%d')

print(df_participant)