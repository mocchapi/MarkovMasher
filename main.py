import markovify
from time import sleep

if __name__ == '__main__':
	lasagna = ''
	print('[1] from file\n[2] mash now')
	choice = input(':')
	if choice == '1':
		print('a good file should have a single buttonmash per line (see example.txt)')
		filename = input('filename: ')
		with open(filename,'r') as f:
			text = f.read()
			text = text.replace(' ','')
			for item in text.split('\n'):
				newitem = ' '.join(item)
				print(newitem)
				lasagna = f'{lasagna}\n{newitem}'

	elif choice == '2':
		textedput = ''
		print('buttonmash & press enter\nkeep doing this until you are satisfied. type "stop" to start generating.')
		while textedput != 'stop':
			lasagna = f'{lasagna}\n{" ".join(textedput)}'
			print(lasagna)
			print(len(lasagna.split('\n')))
			textedput = input('>')
		newline = "\n"
		newfilename = f'{lasagna.split(newline)[1]}.txt'
		with open(newfilename,'w') as f:
			f.write(lasagna)
			print(f'saved as {newfilename}')
	else:
		exit()
	print(lasagna)
	model = markovify.NewlineText(lasagna)
	while True:
		print(model.make_short_sentence(120).replace(' ',''))
		sleep(0.05)
