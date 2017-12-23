import random

def generateDoor():
	doors = ["goat", "goat", "car"]
	random.shuffle(doors)
	first_choice = random.choice(range(len(doors)))
	return doors, first_choice

def revealGoat(first_choice, doors_original):
	doors = doors_original[::]
	if doors[first_choice] == "goat":
		doors[first_choice] = "taken"
		goats_indices = [doors.index("goat")]
	else:
		goats_indices = [i for i, x in enumerate(doors) if x == "goat"]
	return goats_indices

if __name__ == "__main__":
	trial_size = 1000000
	sample_size = 0
	swap_success = 0
	stay_success = 0

	while(sample_size < trial_size):

		reveal = ["?????","?????","?????"]
#		print("================================")
#		print("Sample #", sample_size+1)
		doors, first_choice = generateDoor()

		# Declare First Choice
#		print("\nFirst Choice", first_choice)
		reveal[first_choice] = "Choice"
#		print("Door0\tDoor1\tDoor2")
#		print("%s\t%s\t%s" % tuple(reveal))
#		print("\t"*first_choice, " ^")

		# Reveal Goat
		goat_locations = revealGoat(first_choice, doors)
		second_choice = random.choice(goat_locations)
		goat_locations.remove(second_choice)
		
		for option in enumerate(doors):
			if option[0] != first_choice and option[0] != second_choice:
				third_choice = option[0]
		
		reveal[second_choice] = "Goat!"
#		print("\nGoat is Definitely in Door", second_choice)
#		print("Door0\tDoor1\tDoor2")
#		print("%s\t%s\t%s" % tuple(reveal))
#		print("\t"*second_choice, " ^")

#		print("Do you choose to stay or swap?")
#		print("??????????????????????????")
		if doors[first_choice] == "car":
#			print("\tStay Wins!")
			stay_success += 1
		if doors[third_choice] == "car":
#			print("\tSwap Wins!")
			swap_success += 1
#		print("??????????????????????????")

		sample_size += 1

	print("********************************************")
	print("Final Statistics (Out of", sample_size, "trials)")
	print("Stay Success (Percentage):", round(100*(stay_success/sample_size),4),"%")
	print("Swap Success (Percentage):", round(100*(swap_success/sample_size),4),"%")
	print("********************************************")



	