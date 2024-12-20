### Password/Username/Port Generation
import random
import os
import shutil
from ipaddress import ip_address
letters = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['+','-','_','=','!']
more = ['#','@','$','&','*','(',')','<','>','.','%','?','^']

### Backtrack after failed process
def clean_up():
	shutil.rmtree('__pycache__')
	exit()

### Daemon User (`firo`) Password Gen
def usr_passwd_gen(num):
	passwd = []
	charlist = letters+numbers+symbols+more
	for i in range(num):
		randomchar = random.choice(charlist)
		passwd.append(randomchar)
	usrpwd = "".join(passwd)
	return usrpwd

### RPC Username ###
def username_gen(num):
	u = []
	charlist = letters
	for i in range(num):
		randomchar = random.choice(charlist)
		u.append(randomchar)
	rpcname = "".join(u)
	return rpcname

### RPC Password Generator
def rpc_passwd_gen(num):
	passwd = []
	charlist = letters+numbers+symbols
	for i in range(num):
		randomchar = random.choice(charlist)
		passwd.append(randomchar)
	rpcpwd = "".join(passwd)
	return rpcpwd

### Random port generator ###

def port_gen():
	p = []
	firstchar = random.choice("12345")
	p.append(firstchar)
	for i in range(4):
		randomchar = random.choice(numbers)
		p.append(randomchar)
	randport = "".join(p)
	return randport

## sanatize

def rpc_pass(v):
	for i in v:
		if i == "#":
			print(f"Error: Rpc password can not contain the '#' character it will comment out <#ANTHING FROM THAT POINT ON>: {v}\nPlease consider leaving this field blank and letting the script generate a password for you")
			clean_up()

#check that its not an internal ip && ip is valid && ip is not reserved
def ext(v):
	try:
		ip_address(v)
	except ValueError:
		print(f"{v} is not a valid IPAddress")
		clean_up()
	if ip_address(v).is_reserved:
		print(f"{v} is a reserved IP Address.\n please ensure you have entered in the correct information and try again.")
		clean_up()
	elif ip_address(v).is_private:
		print(f"{v} is a private IP Address.\nThis script is not interned for LAN node set up.\nPlease enter the External IP address of your server.")
		clean_up()


def port(v):
	for i in v:
		if i not in numbers:
			print(f"Error: Port can contain numbers only: {v}\nPlease consider leaving this field blank and letting the script generate a port for you")
			clean_up()
	if v <= 10000 and v != 22:
		print(f"Please consider using a port above 10000.")
		while True:
			x = input("Are you sure {v} is not in use? [y/n]")
			if x.lower() == "y" or "yes":
				False
			elif x.lower() == "n" or "no":
				clean_up()
			else:
				print("Please input yes or no")
				continue
def usr(v):
	for i in v:
		if i not in letters:
			print(f"Error: Usernames should consist of letters only: {v}\nPlease consider leaving this field blank and letting the script generate a username for you")
			clean_up()

## Check if key exists 
def key_check(a):
	dir = a
	num = 0
	file = 'ed25519_firo_0'
	cond = True
	
	for root, dirs, files in os.walk(dir):
		while cond:
			if num == 100:
				print("Too many keys have been generated by this script, please check you are using all 99 of your keys!")
			elif file in files and num > 9 and num < 100:
				num+=1
				file = file[:-2]
				file = file+str(num)
			elif file in files and file[-1] == str(num):
				num+=1
				file = file[:-1]
				file = file+str(num)
			elif file in files and file+'_'+str(num) in files:
				num+=1
				file = file+'_'+str(num)
			else:
				cond = False
				return file

### Random cronjob start time and day for updater			
day = random.randrange(7)
hour = random.randrange(11)
minute = random.randrange(60)