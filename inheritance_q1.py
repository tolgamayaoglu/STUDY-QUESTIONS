# Inheritance Q1

def read_file():
  # TODO: extract name, ID, and the score from the file
  with open('input.txt', 'r') as f:

    lines = f.readlines()
    name = lines[0].rstrip("\n")
    ID = lines[1].rstrip("\n")
    scores = (lines[2].rstrip("\n")).split(' ')
    scores = [int(s) for s in scores]

  r_dict = {'name' : name, 'ID': ID, 'scores' : scores}

  return r_dict


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):

		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Player(Person):
  '''
  The __init__ method
    firstName - A string denoting the Person's first name.
    lastName - A string denoting the Person's last name.
    id - An integer denoting the Person's ID number.
    scores - An array of integers denoting the Person's test scores.
  '''
  def __init__(self, firstName, lastName, idNumber, scores):
    Person.__init__(self, firstName, lastName, idNumber)
    self.scores = scores

  '''
  The calculate method
    Returns one of the characters A, B, C, D 
    denoting the grade of the player.
  '''
  def calculate(self):
    total = 0

    for score in self.scores:
      total += score

    avg = total / len(self.scores)

    if 20 <= avg:
      return 'A'
    if 15 <= avg < 20:
      return 'B'
    if 5 <= avg < 15:
      return 'C'
    if avg < 5:
      return 'D'

  '''
  The total_matches method
    Returns how many matches are played by the player.
  '''
  def total_matches(self):
    return len(self.scores)


player_dict = read_file()

# TODO: create the Player instance, print it
name_list = player_dict['name'].split(' ')
firstName, lastName = name_list[0], name_list[1]
p = Player(firstName, lastName, player_dict['ID'] , player_dict['scores'])
p.printPerson()

# TODO: compute the grade of the player and print it
print("Grade: ", p.calculate())
print("Total Matches: ", p.total_matches())
