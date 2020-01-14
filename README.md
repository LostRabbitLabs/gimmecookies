# gimmecookies
Python3 script to generate CSV output files from domain-wide crawl for digital assets (like cookies!).

     Language: Python 3
     Libraries: sys, socket, subprocess, requests
     Additional Packages Needed: Sublist3r
     Purpose: Penetration Testing / Digital Asset Management


# Install
Follow the steps below to install 'gimmecookies'.

     git clone https://github.com/lostrabbitlabs/gimmecookies
     cd gimmecookies
     chmod 655 gimmecookies.py


This script also requires 'Sublist3r' in your 'gimmecookies' directory:

     git clone https://github.com/aboul3la/Sublist3r
     cd Sublist3r
     pip install -r requirements.txt
     

# Usage
Simply provide a domain name and run the script.

     ./gimmecookies.py example.com


# Output
When completed will create up to three (3) output files:

     example.com-hosts.txt
     example.com-output-headers.csv
     example.com-output-cookies.csv
