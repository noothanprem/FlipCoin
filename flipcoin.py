import random
class FlipCoin:
	
	def flip_coin(self):

		toss=random.randint(0,1)
		if toss == 0:
			print("Heads")
		else:
			print("Tails")

if __name__ == "__main__":

	flipcoin_object = FlipCoin()
	flipcoin_object.flip_coin()

