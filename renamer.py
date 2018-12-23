import os
import requests


print("What show do you want to watch?")
x = input()
print("What season are you changing?")
y = input()

# gets the data for the season of the show you are watching
website = requests.get('https://en.wikipedia.org/wiki/' + x.replace(' ','_') + '_(season_' + y + ')').text
from bs4 import BeautifulSoup
#puts information into parse tree
soup = BeautifulSoup(website,'lxml')
#getting only data that one wants
my_table = soup.find('table',{'class':'wikitable plainrowheaders wikiepisodetable'})
links = my_table.findAll('td',{'class':'summary'})

titles = []
replace = ['/','[',']','|','<','>','+',';','=','.','?',':']

#outer for loop that goes through all the titles in wikipedia table
#inner for loop gets rid of any characters that are unaccpetable in file names
for link in links:
    text = link.text.replace('"','')
    for i in replace:
        text = text.replace(i,'')
    titles.append(text)
print(titles)

def main():
  i = 1
  #setting the memory address of file locations
  Var = 'E:/Television/' + x + '/Season ' + str(y) + '/'
  for filename in os.listdir(Var):
     z = i
     z -= 1
     name = 'S0' + str(y) + 'E' + str(i) + ' '+ titles[z] + ".mp4"
     pic = Var + filename
     name = Var + name
     os.rename(pic,name)
     print(filename)
     i += 1

if __name__ == '__main__':
  main()
