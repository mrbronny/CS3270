from collections import namedtuple
animals = set()
Animal = namedtuple('Animal', ['name', 'kind', 'size'])
animals.add(Animal("Scooby", "dog", "big"))
animals.add(Animal("Fluffy", "cat", "medium"))
animals.add(Animal("Marvin", "mouse", "small"))
animals.add(Animal("Hedwig", "bird", "medium"))
animals.add(Animal("Tweety", "bird", "small"))
animals.add(Animal("Scabbers", "rat", "small"))
animals.add(Animal("Jumbo", "elephant", "huge"))
people = set()
Person = namedtuple('Person', ['name', 'age'])
people.add(Person("Agatha", "old"))
people.add(Person("Harry", "young"))
people.add(Person("Shaggy", "middle-aged"))
people.add(Person("Daphne", "middle-aged"))
people.add(Person("Sylvia", "young"))
people.add(Person("Ron", "old"))
pets = set()
Pet = namedtuple('Pet', ['owner', 'animal'])
pets.add(Pet("Shaggy", "Scooby"))
pets.add(Pet("Harry", "Hedwig"))
pets.add(Pet("Sylvia", "Jumbo"))
pets.add(Pet("Agatha", "Fluffy"))
pets.add(Pet("Agatha", "Tweety"))
pets.add(Pet("Ron", "Scabbers"))
pets.add(Pet("Sylvia", "Marvin"))
pets.add(Pet("Daphne", "Muffin"))

def main():
  sylvia_kinds = {animal.kind for animal in animals if animal.name in {pet.animal for pet in pets if pet.owner == "Sylvia"}}
  print(sylvia_kinds)
  #outputs {'mouse', 'elephant'}
  small_pet_owner_ages = {person.age for person in people if person.name in {pet.owner for pet in pets if pet.animal in {animal.name for animal in animals if animal.size == "small"}}}
  print(small_pet_owner_ages)
  #outputs {'young', 'old'}

if __name__ == "__main__":
  main()