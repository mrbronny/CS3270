#show what generators are and do

def ourgenerator(name):
  greeting = "Hi "
  yield greeting
  sent_name = yield name
  greeting += sent_name
  yield greeting
  greeting += ", it was nice meeting you."
  yield greeting

gen = ourgenerator("")
print(next(gen))
#Hi
next(gen) #skip the yield that will be sent a value
print(gen.send("George"))
#Hi George
print(next(gen))
#Hi George, it was nice meeting you.