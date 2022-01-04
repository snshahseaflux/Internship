import random, math

class Training:

	def dice_roll(self):
		arr = range(1,7)
		while True:
			switch = input('\nPress 1 to roll the dice | Press 0 to exit\n')
			if switch=='0':

				return 

			elif switch=='1':
				print(random.choice(arr))


	# This is basically a competition against binary search
	# binary search takes log base2 (n) steps to reach the outcome
	# We set the difficulty manually, Hence number of steps given
	# to the user are log base2 (n) + 2
	def guess_number(self):

		start = int(input('\nPlease enter start of the range:\n'))
		end = int(input('\nPlease enter end of the range:\n')) + 1
		arr = [k for k in range(start,end)]
		num = random.choice(arr)

		max_steps = math.ceil(math.log(len(arr),2)) + 2 # Easy/Medium Difficulty for shorter ranges

		while max_steps:
			print()
			print(f'You have {max_steps} guesses left. Choose wisely')
			print('-------------------------------------------------------------')
			print()
			guess = int(input('\nGuess the number selected randomly:\n'))
			if guess>num:
				print('\nYour guess was larger than the selected number. Try again !\n')
			elif guess<num:
				print('\nYour guess was smaller than the selected number. Try again !\n')

			elif guess==num:
				print(f'Bingo! You won. The guess is correct. The selected number was {num}')
				return

			max_steps-=1
		print('You lost the game. Better luck next time!')


	def bmi_calculator(self):
		name = input('\nEnter name:\n')
		weight = float(input('\nEnter weight in kilograms:\n'))
		height = float(input('\nEnter height in meters:\n'))
		bmi = weight / height**2
		category = ""
		if bmi<18.5:
			category = 'Underweight'
		elif bmi>=18.5 and bmi<25:
			category = 'Normal'
		elif bmi>=25 and bmi<30:
			category = 'Overweight'
		elif bmi>=30:
			category = 'Obesity'
		
		f = open("bmi_log.txt", mode='a', encoding='utf-8')
		f.write(f'{"name".ljust(15)}: {name}\n')
		f.write(f'{"height".ljust(16)}: {height} meters\n')
		f.write(f'{"weight".ljust(15)}: {weight} kilos\n')
		f.write(f'{"bmi".ljust(17)}: {bmi:.{4}}\n')
		f.write(f'{"category".ljust(14)}: {category}\n\n')
		f.close()


	def rpc(self):
		count = 10
		arr = ['r', 'p', 's']
		print('Rock -----> r')
		print('Paper ----> p')
		print('Scissor---> s')
		f = open("rps_log.txt", mode='a', encoding='utf-8')
		while(count):
			print()
			print()
			print(f'--------------------------------MATCH {11-count}---------------------------------------')
			print()
			user = input("Enter a sign:\n").strip()
			if user not in arr:
				print('\nPlease enter a valid input. Rematch!\n')
				continue
			computer = random.choice(arr)
			if user==computer:
				log = f"Match {11-count} Results ----> Draw | Both opted {computer} \n"

			else:
				if user=='r' and computer=='p':
					log = f"Match {11-count} Results ----> computer won | computer chose paper againt user's rock.\n"
				if user=='r' and computer=='s':
					log = f"Match {11-count} Results ----> user won | user chose rock againt computer's scissors.\n"
				if user=='p' and computer=='r':
					log = f"Match {11-count} Results ----> user won | user chose paper againt computer's rock.\n"
				if user=='p' and computer=='s':
					log = f"Match {11-count} Results ----> computer won | computer chose scissors againt user's paper.\n"
				if user=='s' and computer=='r':
					log = f"Match {11-count} Results ----> computer won | computer chose rock againt user's scissors.\n"
				if user=='s' and computer=='p':
					log = f"Match {11-count} Results ----> user won | user chose scissors againt computer's paper.\n"
			
			f.write(log)
			count-=1
		f.close()



if __name__ == '__main__':
	t1 = Training()
	while True:
		print()
		print()
		print()
		print('----------------------  ----SELECT ONE OF THE FOLLOWING-----------------------------')
		print('1. Dice Roll')
		print('2. Guess Number')
		print('3. BMI Calculator')
		print('4. Rock-Paper-Scissor')
		print('5. Exit')
		print()
		choice = int(input())
		if choice==1:
			t1.dice_roll()
		elif choice==2:
			t1.guess_number()
		elif choice==3:
			t1.bmi_calculator()
		elif choice==4:
			t1.rpc()
		elif choice==5:
			break
		else:
			print('\nChoose one of the 5 choices\n')






