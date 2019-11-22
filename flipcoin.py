import random
import operator
class FlipCoin:
	
	singlet_dict = {'H':0,'T':0}
	doublet_dict = {'HH':0,'HT':0,'TH':0,'TT':0}
	triplet_dict = {'HHH':0,'HHT':0,'HTH':0,'THH':0,'TTT':0,'TTH':0,'THT':0,'HTT':0}
	def singlet(self,number):

		for flip_count in range(number):
			toss=random.randint(0,1)
			if toss == 0:
				print("Tails")
				self.singlet_dict['T'] += 1
			else:
				print("Heads")
				self.singlet_dict['H'] += 1
		print(self.singlet_dict)		
		heads_percentage = (self.singlet_dict['H'] / number) * 100
		tails_percentage = 100 - heads_percentage
		print("Heads Percentage : ",heads_percentage)
		print("Tails Percentage : ",tails_percentage)
		
		return self.singlet_dict

	def doublet(self,number):

		for flip_count in range(number):
			first_toss = random.randint(0,1)
			second_toss = random.randint(0,1)
			if first_toss == 0 and second_toss == 0:
				print("TT")
				self.doublet_dict['TT'] += 1
			elif first_toss == 0 and second_toss == 1:
				print("TH")
				self.doublet_dict['TH'] += 1
			elif first_toss == 1 and second_toss == 0:
				print("HT")
				self.doublet_dict['HT'] += 1
			else:
				print("HH")
				self.doublet_dict['HH'] += 1
		
		print(self.doublet_dict)
		sorted_doublet_dict = sorted(self.doublet_dict.items(), key=lambda kv:kv[1])
		tt_percentage = (self.doublet_dict['TT'] / number) * 100
		th_percentage = (self.doublet_dict['TH'] / number) * 100
		ht_percentage = (self.doublet_dict['HT'] / number) * 100
		hh_percentage = (self.doublet_dict['HH'] / number) * 100
		
		print("TT Percentage : ",tt_percentage) 
		print("TH Percentage : ",th_percentage)
		print("HT Percentage : ",ht_percentage)
		print("HH Percentage : ",hh_percentage)
		
		return self.doublet_dict
	
	def triplet(self,number):
		
		for flip_count in range(number):

			first_toss = random.randint(0,1)
			second_toss = random.randint(0,1)
			third_toss = random.randint(0,1)

			if first_toss == 0 and second_toss == 0 and third_toss == 0:
				print("TTT")
				self.triplet_dict['TTT'] += 1
			elif first_toss == 0 and second_toss == 0 and third_toss == 1:
				print("TTH")
				self.triplet_dict['TTH'] += 1
			elif first_toss == 0 and second_toss == 1 and third_toss == 0:
				print("THT")
				self.triplet_dict['THT'] += 1
			elif first_toss == 1 and second_toss == 0 and third_toss == 0:
				print("HTT")
				self.triplet_dict['HTT'] += 1
			elif first_toss == 1 and second_toss == 1 and third_toss == 1:
				print("HHH")
				self.triplet_dict['HHH'] += 1
			elif first_toss == 1 and second_toss == 1 and third_toss == 0:
				print("HHT")
				self.triplet_dict['HHT'] += 1
			elif first_toss == 1 and second_toss == 0 and third_toss == 1:
				print("HTH")
				self.triplet_dict['HTH'] += 1
			else:
				print("THH")
				self.triplet_dict['THH'] += 1

		print(self.triplet_dict)
		
		triplet_percentage_dict = {'HHH':0,'HHT':0,'HTH':0,'THH':0,'TTT':0,'TTH':0,'THT':0,'HTT':0}
		
		triplet_percentage_dict['HHH'] = ((self.triplet_dict['HHH'] / number) * 100)
		triplet_percentage_dict['HHT'] = ((self.triplet_dict['HHT'] / number) * 100)
		triplet_percentage_dict['HTH'] = ((self.triplet_dict['HTH'] / number) * 100)
		triplet_percentage_dict['THH'] = ((self.triplet_dict['THH'] / number) * 100)
		triplet_percentage_dict['TTT'] = ((self.triplet_dict['TTT'] / number) * 100)
		triplet_percentage_dict['TTH'] = ((self.triplet_dict['TTH'] / number) * 100)
		triplet_percentage_dict['THT'] = ((self.triplet_dict['THT'] / number) * 100)
		triplet_percentage_dict['HTT'] = ((self.triplet_dict['HTT'] / number) * 100)

		print(triplet_percentage_dict)

		
		return self.triplet_dict

if __name__ == "__main__":

	flipcoin_object = FlipCoin()
	number = int(input("How many times you want to flip the coin ? :"))
	
	singlet_dict = flipcoin_object.singlet(number)
	sorted_singlet_dict = sorted(singlet_dict.items(), key=lambda k : (k[1],k[0]))
	print("Sorted singlet Pairs : ",sorted_singlet_dict)
	
	doublet_dict = flipcoin_object.doublet(number)
	sorted_doublet_dict = sorted(doublet_dict.items(),key = lambda k : (k[1],k[0]))
	print("Sorted doublet Pairs : ",sorted_doublet_dict)

	triplet_dict = flipcoin_object.triplet(number)
	sorted_triplet_dict = sorted(triplet_dict.items(),key=lambda k : (k[1],k[0]))
	print("Sorted triplet Pairs : ",sorted_triplet_dict)

	singlet_max_element = sorted_singlet_dict[len(sorted_singlet_dict)-1]

	doublet_max_element = sorted_doublet_dict[len(sorted_doublet_dict)-1]

	triplet_max_element = sorted_triplet_dict[len(sorted_triplet_dict)-1]
	
	for each_pair in sorted_singlet_dict:
		if singlet_max_element[1] == each_pair[1]:
			print("Winning combination of Singlet : ",each_pair)
	for each_pair in sorted_doublet_dict:
		if doublet_max_element[1] == each_pair[1]:
			print("Winning combination of Doublet : ",each_pair)
	for each_pair in sorted_triplet_dict:
		if triplet_max_element[1] == each_pair[1]:
			print("Winning combination of triplet : ",each_pair) 	



