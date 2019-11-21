import random
class FlipCoin:
	
	singlet_dict = {'H':0,'T':0}

	def flip_coin(self,number):

		for flip_count in range(number):
			toss=random.randint(0,1)
			if toss == 0:
				print("Heads")
				self.singlet_dict['H'] += 1
			else:
				print("Tails")
				self.singlet_dict['T'] += 1
		
		heads_percentage = (self.singlet_dict['H'] / number) * 100
		tails_percentage = (self.singlet_dict['T'] / number) * 100
		print("Heads Percentage : ",heads_percentage)
		print("Tails Percentage : ",tails_percentage)

if __name__ == "__main__":

	flipcoin_object = FlipCoin()
	number = int(input("How many times you want to flip the coin ? :"))
	flipcoin_object.flip_coin(number)

