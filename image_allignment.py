import os , subprocess , time
#installing fpdf if the user hasn't installed it
subprocess.run(['pip3 install fpdf' , 'pip3 install colorama'] , shell = True)
from fpdf import FPDF
from colorama import Fore
#project initialization
print(Fore.GREEN + f'image to pdf v1.0')
username = input('enter the username in your filesystem: ')
printer = input('enter the name of you printer: ')
pdf = FPDF()
pdf.add_page()
current = os.getcwd()
turn = 0
if os.path.exists(f'/home/{username}/Downloads/pics_to_pdf') == False:
	print('Fore.RED' + f'the path /home/{username}/Downloads/pics_to_pdf does not exist.Creation of the path has completed.Please put your images there and come back')
	os.mkdir(f'/home/{username}/Downloads/pics_to_pdf')
	time.sleep(8)
	quit()
os.chdir(f'/home/{username}/Downloads/pics_to_pdf')
x = 00
y = 00
for file in os.listdir():
	print(f'completed reading {file}')
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
print(f'PDF created.saving in {current}')
os.chdir(current)
pdf.output('image_outpt.pdf')
print('PDF saved!')
ask_to_print = input('do you want to print the output file?(y/n): ')
if ask_to_print == 'y' or ask_to_print == 'Y':
	a = subprocess.run(f'lp image_outpt.pdf -d {printer}' , shell = True , capture_output = True , text = True)
	print(a)
print('Wrapping up....')
time.sleep(5)
quit()
