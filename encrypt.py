# usr/bin/python2
'''
Tools  : encryptor base64 untuk python
Pungsi : untuk mengamankan script python agar tidak di curi oleh orang lain/di recode
--------------------------------------------------------------------------------------
Autor  : M.Luqman.Arief
Team   : X-Garuda_Red
Github : github :https://github.com/ARIEF-16
facebook : https://www.facebook.com/profile.php?id=100055134992811

'''

# color
A = "\033[1;31m"
B = "\033[1;32m"
C = "\033[1;33m"
D = "\033[1;34m"
E = "\033[1;35m"
F = "\033[1;35m"
G = "\033[1;36m"
import os,base64
os.system("clear")
logo = """
\033[1;32m
             _
            | |
         _  | |  __   __   _  _  _    _
|  |  |_|/  |/  /    /  \_/ |/ |/ |  |/
 \/ \/  |__/|__/\___/\__/   |  |  |_/|__/\033[1;33m
_________________________________________
          Autor: M.Luqman.Arif
          Team : X-Garuda_Red
-----------------------------------------
"""




print logo
print "%sEX:\n%s/path/yourfile.py" % (A,C)
print
file_name = raw_input("\033[1;33m[\033[0;36mfile\033[1;33m ] >> ")
try:
	file = open("%s" % (file_name))
	encrypt = base64.b64encode(file.read())
	file = open("hasil.py","w")
	file.write("#code by : M.Luqman.Arief\n")
	file.write("#github :https://github.com/ARIEF-16\n")
	file.write("#faceebook: https://www.facebook.com/profile.php?id=100055134992811\n")
	file.write("import base64\n")
	ash = "'"
	file.write("result = %s %s %s \n"% (ash,encrypt,ash))
	file.write("eval(compile(base64.b64decode(result),'<string>','exec'))\n")
	file.close()
	print "%s[+] %sfile saved %s'hasil.py...'" % (A,B,B)




except IOError,e:
	print "%s[CRITICAL] %sError:%s" % (A,B,e)





