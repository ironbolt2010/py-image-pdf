# py-image-pdf
This project is only available for Linux.Basically it will get the images in a folder in your downloads folder and save it in the current directory where the file is.
For this file to actually operate,First,you will need to have a directory in your downloads folder called 'pics_to_pdf'.Type the name exactly as given.  
After that,Just paste some pictures in the filder that you created earlier.  
Then,Run the python file in a terminal and the expected inputs are as fillows(all the inputs are case sensitive):  
     **I:'enter the username in your filesystem: ' this asks for your system username ex:-/home/THIS_IS_YOUR_USERNAME/Desktop.......  
    II:"enter the name of your printer: " for this goto your printer settings in linux and find the name of your printer of preference and type the printer         name in(remember!:The name that you enter is indeed case sensitive.).  
    III:"do you want to print the output file?(y/n): " this takes only 2 valid arguments 'y' and 'n'(remeber that these is case sensitive.).entering 'y'           will print your output file.Anything else won't.**  
    other inputs triggered on special conditions:  
        **I)do you want to print the output file?(y/n)(you can type SAVE ALL INFO to save all the info you just typed: ):if you type SAVE ALL INFO to this input,then that will trigger the program to make a info.ini file with the username and the printer name you entered previously to the current directory so you can use them again.**  
        II)info.ini file loacated.you can load it's contents if you want(y/n):**This means that the program found a info.ini file in your current directory.Typing 'y' will automatically fill in the username and printer name for you.**    
