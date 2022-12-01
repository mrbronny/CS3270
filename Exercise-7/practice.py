import requests as req
import pprint as p
import re

#populate self.index with self.index[word] = [URL1, URL2, ...]
#populate self.graph with self.graph[pURL] = [cURL, cURL, ...]
index = {}
graph = {}
rank = {}
depth = 2

def main():
  headers = {'User-Agent': "XY"}
  urls = [('http://roversgame.net/cs3270/page1.html', 1)]
  while urls:
    if urls[0][0] not in graph and urls[0][1] <= depth:
      x = req.get(urls[0][0], headers = headers).text
      #print(x)
      innerhtml = re.split('<.*>', x)
      for line in innerhtml:
        line = line.replace("\n", " ")
        if line != '':
          line = line.split(' ')
          for word in line:
            if not re.search("\d", word):
              word = re.sub("\W", "", word)
              if word:
                word = word.lower()
                if word in index:
                  index[word] += [urls[0][0]]
                else:
                  index[word] = [urls[0][0]]
      links = re.findall('http://.*?"', x)
      graph[urls[0][0]] = []
      for link in links:
        if link[:-1] not in graph[urls[0][0]]:
          graph[urls[0][0]] += [link[:-1]]
          urls += [(link[:-1], urls[0][1]+1)]
      urls.pop(0)
    else:
      urls.pop(0)
  p.pprint(graph) 
  p.pprint(co)
  

if __name__ == "__main__":
  main()