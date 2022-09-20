from collections import namedtuple

def main():

  parts = set()
  Part = namedtuple('Part', ['pno','pname','color','weight','city'])
  projects = set()
  Project = namedtuple('Project', ['jno','jname','city'])
  suppliers = set()
  Supplier = namedtuple('Supplier', ['sno','sname','status','city'])
  spjset = set()
  Spj = namedtuple('Spj', ['sno','pno','jno','qty'])

  with open("parts.txt", "r") as file:
    file = file.readlines()
    for line in file[2:]:
      line = line.strip()
      line = line.split(",")
      parts.add(Part(line[0],line[1],line[2],line[3],line[4]))

  with open("projects.txt", "r") as file:
    file = file.readlines()
    for line in file[2:]:
      line = line.strip()
      line = line.split(",")
      projects.add(Project(line[0],line[1],line[2]))

  with open("suppliers.txt", "r") as file:
    file = file.readlines()
    for line in file[2:]:
      line = line.strip()
      line = line.split(",")
      suppliers.add(Supplier(line[0],line[1],line[2],line[3]))

  with open("spj.txt", "r") as file:
    file = file.readlines()
    for line in file[2:]:
      line = line.strip()
      line = line.split(",")
      spjset.add(Spj(line[0],line[1],line[2],line[3]))

  #all suppliers that supply bolts
  print({supplier.sname for supplier in suppliers if supplier.sno in {spj.sno for spj in spjset if spj.pno in {part.pno for part in parts if part.pname == "Bolt"}}})
  #all suppliers that supply blue parts
  print({supplier.sname for supplier in suppliers if supplier.sno in {spj.sno for spj in spjset if spj.pno in {part.pno for part in parts if part.color == "Blue"}}})
  #all suppliers not used in Athens project
  print({supplier.sname for supplier in suppliers if supplier.sno not in {spj.sno for spj in spjset if spj.jno in {project.jno for project in projects if project.city == "Athens"}}})
  #names and colors of all parts not used in Oslo
  print({(part.pname,part.color) for part in parts if part.pno not in {spj.pno for spj in spjset if spj.jno in {project.jno for project in projects if project.city == "Oslo"}}})
  #pairs of names of suppliers located in the same city
  print({(supplier1.sname,supplier2.sname) for supplier1 in suppliers for supplier2 in suppliers if supplier1.city == supplier2.city if supplier1.sname < supplier2.sname})
  #all suppliers by city (use dictionary)
  citydict = {"Paris":"","Athens":"","London":""}
  citydict["Paris"] = {supplier.sname for supplier in suppliers if supplier.city == "Paris"}
  citydict["Athens"] = {supplier.sname for supplier in suppliers if supplier.city == "Athens"}
  citydict["London"] = {supplier.sname for supplier in suppliers if supplier.city == "London"}
  print(citydict)
  
if __name__ == "__main__":
  main()