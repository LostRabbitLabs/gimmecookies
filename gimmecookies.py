#!/usr/bin/python3
import subprocess
import requests
import sys
import socket

cookie_lib = []

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
}

try:
    domain = sys.argv[1]
except:
    print ("\nGimme Cookies Error!! Use the format below:\n./gimmecookies.py example.com\n\n")
    sys.exit()

print("\n                .';::::::;,'.                    ")
print("            .,cloO00Okkkxkkkxdc'.                ")
print("          .cxkl..:OOxxdooddxkOOOd:.              ")
print("        .lkOOx'   :xxddddddxxxxkOOk;             ")
print("       ,xK0OOd.    'oxxxxxo:;;:oxkO0o.           ")
print("      ,kKKK0Ol.     ,xkkd;.     'cxk0d.          ")
print("     .xKKK0OOl.     .o0k,         ,ok0l.         ")
print("     :KKK0Okkx;      .,.      .    .,ox,         ")
print("    .dK00Okkxkx:             c0ko;...;kc         ")
print("    .xK00Okxxkx;             'kXXXK0OKXl         ")
print("    .dK00kxkkd'   G I M M E   ,OKKKKKKKc         ")
print("     cKK0Okkkc                .xXKK00KO,         ")
print("     .kKK0kkd'  C O O K I E S  kKKK00Ko.         ")
print("      ;OKK0O:                  cKK0KKx.          ")
print("       ;OKK0l |_ostRabbit|_abs cKKKKd.           ")
print("        .d0KOc.               ,kKKOc.            ")
print("          ,o00xc,.         .'l0KOl.              ")
print("            .:oO0kl;,'..':dOOko;.                ")
print("               ..;:cllccccc,..                   \n\n")
print("    Can I Haz Cookies from " + domain + "?\n")

hostfile = domain + "-hosts.txt"
sublister_command = "python Sublist3r/sublist3r.py -d " + domain + " -o " + domain + "-hosts.txt"

process = subprocess.Popen(sublister_command,
    shell=True,
    stdout=subprocess.PIPE,
    )

process.wait()

inputfile = open(hostfile, "r")
all_hosts = inputfile.readlines()
inputfile.close()

all_hosts = set(all_hosts)

def get_cookies(hosts,ip):
    session = requests.Session()
    try:
        response = session.get(hosts, verify=False, headers=headers, timeout=5)
        all_cookies = session.cookies.get_dict()
        all_headers = response.headers
        responsecode = response.status_code
        responsecode = str(responsecode)
    except:
        pass
        all_cookies = ""
        all_headers = ""
    for mycookies in all_cookies:
        cookievalue = all_cookies[mycookies]
        output = hosts + ";" + ip + ";" + responsecode + ";" + mycookies + ";" + cookievalue + "\n"
        filename1 = domain + "-output-cookies.csv"
        with open (filename1, "a") as outputfile:
            outputfile.write(output)
    for myheaders in all_headers:
        headersvalue = all_headers[myheaders]
        filename2 = domain + "-output-headers.csv"
        output = hosts + ";" + ip + ";"  + responsecode + ";" + myheaders + ";" + headersvalue + "\n"
        with open (filename2, "a") as outputfile:
            outputfile.write(output)


for hosts in all_hosts:
    hosts = hosts.strip("\n")
    print (hosts) 
    try:
        ip = socket.gethostbyname(hosts)
        hosts1 = "http://" + hosts
        get_cookies(hosts1,ip)
    except:
        pass
        print ("Host does not resolve. Moving on...\n")
    try:
        ip2 = socket.gethostbyname(hosts)
        hosts2 = "https://" + hosts
        get_cookies(hosts2,ip2)
    except:
        pass
        print ("Host does not resolve. Moving on...\n")


print( "\nAll done! Check for output files!\n")
sys.exit()

