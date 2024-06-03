import pandas as pd
from datetime import datetime
import os

df = pd.read_csv('mapping/disciplines.csv')
df = df[df['worldathletics_ranking'].notnull()]

for index, row in df.iterrows():
    discipline = row['worldathletics_ranking']
    type = row['worldathletics_ranking_type']
    year = datetime.now().year

    sex = ["men", "women"]
    ageGroup = ["u20", "senior"]
    if(discipline == "4x400-metres-relay"):
        sex.append("mixed")
    
    for a in ageGroup:
        for s in sex:
            print(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType world --output tmp/leads/world/{a}/{s}-{a}-{discipline}.csv")
            os.system(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType world --output tmp/leads/world/{a}/{s}-{a}-{discipline}.csv")
            os.system(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType area --region europe --output tmp/leads/area/europe/{a}/{s}-{a}-{discipline}.csv")
            os.system(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType area --region africa --output tmp/leads/area/africa/{a}/{s}-{a}-{discipline}.csv")
            os.system(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType area --region asia --output tmp/leads/area/asia/{a}/{s}-{a}-{discipline}.csv")
            os.system(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType area --region \"north and central america\" --output tmp/leads/area/naca/{a}/{s}-{a}-{discipline}.csv")
            os.system(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType area --region oceania --output tmp/leads/area/oceania/{a}/{s}-{a}-{discipline}.csv")
            os.system(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType area --region \"south america\" --output tmp/leads/area/sa/{a}/{s}-{a}-{discipline}.csv")
            os.system(f"python worldranking.py --type {type} --discipline {discipline} --sex {s} --ageCategory {a} --year {year} --regionType countries --region ger --output tmp/leads/country/ger/{a}/{s}-{a}-{discipline}.csv") 