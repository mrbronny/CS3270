import requests as req
import pprint
import re

class HayStack():

  def __init__(self, url, depth = 3):
    self.url = url
    self.depth = depth
    self.index = {}
    self.graph = {}
    self.ranks = {}
    #populate self.index with self.index[word] = [URL1, URL2, ...]
    #populate self.graph with self.graph[pURL] = [cURL, cURL, ...]
    headers = {'User-Agent': "XY"}
    urls = [(self.url, 1)]
    while urls:
      if urls[0][0] not in self.graph and urls[0][1] <= self.depth:
        x = req.get(urls[0][0], headers = headers).text
        print(x)
        innerhtml = re.split('<.*>', x)
        input(innerhtml)
        for line in innerhtml:
          line = line.replace("\n", " ")
          if line != '':
            line = line.split(' ')
            for word in line:
              if not re.search("\d", word):
                word = re.sub("\W", "", word)
                if word:
                  word = word.lower()
                  if word in self.index:
                    if urls[0][0] not in self.index[word]:
                      self.index[word] += [urls[0][0]]
                  else:
                    self.index[word] = [urls[0][0]]
        links = re.findall('http://.*?"', x)
        self.graph[urls[0][0]] = []
        for link in links:
          if link[:-1] not in self.graph[urls[0][0]]:
            self.graph[urls[0][0]] += [link[:-1]]
            urls += [(link[:-1], urls[0][1]+1)]
        urls.pop(0)
      else:
        urls.pop(0)
    self.compute_ranks(self.graph)
    

  def compute_ranks(self, graph): 
    d = 0.85     # probability that surfer will bail 
    numloops = 10 
    ranks = {}
    npages = len(graph) 
    for page in graph: 
      ranks[page] = 1.0 / npages 
    for _ in range(0, numloops):
      newranks = {} 
      for page in graph:
        newrank = (1 - d) / npages 
        for url in graph:    
          if page in graph[url]:  # this url links to page 
            newrank += d*ranks[url]/len(graph[url]) 
        newranks[page] = newrank 
      ranks = newranks 
    self.ranks = ranks

  def lookup(self, word):
    #takes word and returns webpages with word in rank order, highest to lowest
    urls = self.index[word.lower()]
    urls.sort(reverse = True, key = lambda x:self.ranks[x])
    return urls

if __name__ == '__main__': 
  engine = HayStack('http://roversgame.net/cs3270/page1.html',4)
  for w in ['pages','links','you','have','I']: 
    print(w) 
    pprint.pprint(engine.lookup(w)) 
  print()
  print('index:') 
  pprint.pprint(engine.index) 
  print() 
  print('graph:') 
  pprint.pprint(engine.graph) 
  print() 
  print('ranks:') 
  pprint.pprint({page:round(rank,4) for page,rank in engine.ranks.items()}) 