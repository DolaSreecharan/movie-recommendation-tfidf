import csv
import numpy as np
import re

database =[]
movie = []
all_movies_words = []
appeared = {}
with open('../movie_data.csv', newline='') as f:
    data = csv.DictReader(f)
    data = list(data)
    no_of_movies = len(data)
    index = 0
    appeared_in_totalf = 1
    for indi,i in enumerate(data): # one one movie at a time
        file = f'file{indi}'
        each_movie = []
        for key,val in i.items(): #taking from one movie(format:dict)
            if key == 'name':
                movie.append([val])
            each_movie = each_movie+val.split()
        for j in each_movie:
            j = j.lower()
            if j in appeared:
                appeared[j][1]+=1
                if appeared[j][3] != file:
                    appeared[j][2]+=1
                    appeared[j][3] = file
            else:
                all_movies_words.append(j)
                appeared[j] = [index,1,1,file]
                index+=1
        no_of_word = len(each_movie)

        calc_set = [0]*len(all_movies_words)
        for j in each_movie:
            j = j.lower()
            calc_set[appeared[j][0]] = (appeared[j][1]/no_of_word)*np.log(no_of_movies/appeared[j][2]).tolist()
        database.append(calc_set)
        for j in each_movie:
            j = j.lower()
            appeared[j][1] = 0
#up to now appeared has [index,no.of times repeated in each file,no.of files word appeared,file last stopped]
#now i changed index 3 to IDF by dividing it with total no of movies
for i in appeared:
    appeared[i][2] = np.log(no_of_movies/appeared[i][2]).tolist()

all_movies_words_len = len(all_movies_words)
for i,v in enumerate(database):
    database[i] = v+[0]*(all_movies_words_len-len(v))

query = input('Enter Description: ')
length = len(query.split())
sample = [0]*len(database[0])
appeared2 = {}
for i in query.split():
    i = i.lower()
    if i in appeared2:
        appeared2[i]+=1
    else:
        appeared2[i] = 1
for i in query.split():
    i = i.lower()
    if i in appeared:
        sample[appeared[i][0]] = (appeared2[i]/length)*appeared[i][2]
result = []
for i,v in enumerate(database):
    if np.linalg.norm(sample)*np.linalg.norm(v)==0:
        continue
    theta = np.arccos((np.dot(v,sample))/(np.linalg.norm(sample)*np.linalg.norm(v)))
    result.append((theta,movie[i]))
result.sort(key = lambda x:x[0])
print('--TOP 5 MOVIES RECOMMENDATION BASED ON YOUR REQUEST--')

for i,v in enumerate(result[:5]):
    print(i+1,'.',v[1][0])
