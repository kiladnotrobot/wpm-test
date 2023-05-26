alph = 'йцукенгшщзхъфывапролджэячсмитьбю'

result = open(r'C:\Users\alex-\Desktop\курсач\assets/english.txt', "w+")


with open(r'C:\Users\alex-\Desktop\курсач\assets/RUS.txt','r') as file:
    for line in file.readlines():
        if line[0] not in alph:
            #print(line)
            result.write(line)

result.close()