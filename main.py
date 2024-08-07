
import os
import time
from termcolor import colored

def banner():
	os.system("clear")
	print("\n\n")
	ban_1 = "           █▀█ ▄▀█ █▄░█ █▀▄ █▀█ █▀█ ▄▀█\n".center(50," ")
	ban_2 = " █▀▀ █▀█ █░▀█ █▄▀ █▄█ █▀▄ █▀█\n".center(50," ")
	ban_3 = "Beta Edition - Magarevedant\n".center(40," ")
	
	print(colored(ban_1 + ban_2,"cyan"),colored(ban_3,"white"))
	app()






#basic functions to esay the script
def write(txt):
        print(colored(txt,'cyan'))
        
def warn(txt):
		print(colored(txt,"yellow"))

def boot():
		print("[*] Booting up Pandora...( please wait)")
		try:
			print("checking file tree.....")
			tools = os.path.exists("tools/")
			sys = os.path.exists("sys_config/")
			sys_usr = os.path.exists("sys_config/usr.ini")
			sys_req = os.path.exists("sys_config/requirement.ini")
			help = os.path.exists("sys_config/help.txt")
			print("tools directory found~")
			print(tools)
			print("sys directory found~")
			print(sys)
			print("user config found~")
			print(sys_usr)
			print("requirement config found~")
			print(sys_req)
			print("help file found~")
			print(help)
			os.system("pip install termcolor")
			
			
			time.sleep(0.5)
		
			
		except:
			warn("[!] Something went wrong")
			warn("Aborting...")
			os.system("exit")
		banner()
	
	
def op_tool(tool,cmd):
	path = "tools/"+tool+"/"
	if cmd == "open":
		try:
			file = path+tool+".py"
			file = open(file,"r")
			code = file.read()
			file.close()
			return exec(code)
		except:
			warn("something went wrong while opening "+tool)
	elif cmd == "help":
		file = path+"help.txt"
		file = open(file,"r")
		help = file.read()
		file.close()
		return help
	elif cmd == "setup":
		file = path+"req.txt"
		file = open(file,"r")
		req = file.read()
		file.close()
		os.system("pip install -r "+req)
	else:
		pass
		
def list_tools():
	return os.listdir("tools/")
	

# Main script loop
def app():
        print('\n')
        print(colored("┌──( Pandora )~[" + str(os.getcwd()) + "]","cyan"))
        cmd = input(colored("└─[*] command-$ ","cyan"))
        if cmd == "exit":
                write("[*] Exiting Pandora...")
                exit()
        elif cmd == "cls" or cmd == "clear":
        		banner()
        elif cmd == "help":
        	help = open("sys_config/help.txt","r")
        	print(help.read())
        	help.close()
        elif cmd == "app -list":
        	write(list_tools())
        elif "app -setup " in cmd:
        	tool = cmd.replace("app -setup ","")
        	print(tool)
        	if os.path.exists("tools/"+tool):
        		warn("setting up "+tool)
        		op_tool(tool,"setup")
        	else:
        		warn("No such app found!")
        elif "app -help " in cmd:
        	tool = cmd.replace("app -help ","")
        	if os.path.exists("tools/"+tool):
        		warn("help for "+tool)
        		print(op_tool(tool,"help"))
        	else:
        		warn("No such app found!")
        elif "app" in cmd:
        	tool = cmd.replace("app ","")
        	if os.path.exists("tools/"+tool):
        		warn("opening "+tool)
        		op_tool(tool,"open")
        	else:
        		warn("No such app found!")
        
        else:
        	try:
        		os.system(cmd)
        	except:
        		pass
        app()
        	
        	
if __name__ == "__main__":
	boot()
