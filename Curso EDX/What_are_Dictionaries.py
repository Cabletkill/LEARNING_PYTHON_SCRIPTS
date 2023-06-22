# Create a List

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)
print()

print (release_year_dict['Thriller'])
print(release_year_dict['The Bodyguard'])
print(release_year_dict.values())
print (release_year_dict.keys())

release_year_dict['Graduation']= "2007"
print(release_year_dict)

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])


'The Bodyguard' in release_year_dict
print(release_year_dict)







