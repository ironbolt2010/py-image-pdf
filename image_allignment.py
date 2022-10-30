import os , subprocess , platform
from configparser import ConfigParser
#installing fpdf if the user hasn't installed it
#subprocess.run(['pip3 install fpdf' , 'pip3 install colorama' , 'pip freeze'] , shell = True)
from fpdf import FPDF
from colorama import Fore
#project initialization
print(Fore.GREEN + f'image to pdf v1.1')
used = False
print('locating info.ini in current directory...')
if 'info.ini' in os.listdir():
	pref = input("info.ini file located.You can load it's contents to the current session if you want(y/n)?: ")
	if pref == 'y' or pref == 'Y':
		used = True
		configuration = ConfigParser()
		configuration.read('info.ini')
		username = configuration['INFORMATION']
		username = username['username']
		printer = configuration['INFORMATION']
		printer = printer['printer name']
		print('information loaded.')
	else:
		username = input('enter the username in your filesystem: ')
		printer = input('enter the name of you printer: ')
pdf = FPDF()
pdf.add_page()
current = os.getcwd()
turn = 0
if platform.system() == 'Windows':
	if os.path.exists(f'C:/Users/{username}/Downloads/pics_to_pdf') == False:
		print(Fore.RED + f'the path /home/{username}/Downloads/pics_to_pdf does not exist.Creation of the path has completed.Please put your images there and come back')
		os.mkdir(f'C:/users/{username}/Downloads/pics_to_pdf')
		quit()
	os.chdir('C:/Users/{username}/Downloads/pics_to_pdf')
if os.path.exists(f'/home/{username}/Downloads/pics_to_pdf') == False and platform.System() != 'Windows':
	print(Fore.RED + f'the path /home/{username}/Downloads/pics_to_pdf does not exist.Creation of the path has completed.Please put your images there and come back')
	os.mkdir(f'/home/{username}/Downloads/pics_to_pdf')
	quit()
if platform.system() == 'Windows':
	os.chdir(f'C:/Users/{username}/Downloads/pics_to_pdf')
else:
	os.chdir(f'/home/{username}/Downloads/pics_to_pdf')
x = 00
y = 00
for file in os.listdir():
	print(f'completed reading {file}')
	try:
		pdf.image(file , w=100 , x = x , y=y , h = 50)
		x += 100

		if turn == 11:
	        	pdf.add_page()
	        	turn = 0
	        	y = 00
	        	x = 00
		if x>=200:
	        	y+= 50
	        	x = 00
		turn += 1
	except:
		print(f'{Fore.RED} an error occurd.Failed to read {file} {Fore.GREEN}')
print(f'PDF created.saving in {current}')
os.chdir(current)
pdf.output('image_output.pdf')
print('PDF saved!')
if used == False:
	ask_to_print = input('do you want to print the output file?(y/n)(you can type "SAVE ALL INFO" to save all the info you just typed): ')
else:
	ask_to_print = input('do you want to print the output file?(y/n): ')
if ask_to_print == 'y' or ask_to_print == 'Y':
	if platform.system() != 'Windows':
		a = subprocess.run(f'lp image_outpt.pdf -d {printer}' , shell = True , capture_output = True , text = True)
		print(a)
	else:
		a = os.startfile('image_output.pdf' , 'Print')
if ask_to_print == 'SAVE ALL INFO':
	print('writing information to file...')
	config = ConfigParser()
	config['INFORMATION'] = {'USERNAME':username,
				'PRINTER NAME':printer}
	with open('info.ini' , 'wt') as f:
		config.write(f)
		f.close()
	print('information writing completed!')
if platform.system() != 'Windows':
	os.system('open image_output.pdf')
else:
	os.system('start image_output.pdf')
quit()
