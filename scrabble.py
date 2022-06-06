letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Dict comprehension that has the elements of letters as the keys and the elements of points as the values.
letter_to_points = {key:value for key, value in zip(letters, points)}
# print(letter_to_point)

#Adding a blank tile and point to the Dict
letter_to_points[" "] = 0

#A function that will take in a word and return how many points that word is worth.
def score_word(word):
  point_total = 0
  #For loop that goes through the letters in word and adds the point value of each letter to point_total.
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points[letter]
    else:
      point_total += 0
  return point_total

#TESTING score_word function --> Should return 15 pts
brownie_points = score_word("BROWNIE")
# print(brownie_points)

#A dictionary that maps players to a list of the words they have played.
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH","EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

#An empty dictionary to contain the mapping of players to how many points they’ve scored.
player_to_points = {}

#Iterating through the items in player_to_words to calculate each players points
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)
