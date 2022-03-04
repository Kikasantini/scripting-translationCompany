#!/usr/bin/python3

import os
import datetime
import pytz

TZ = 'US/Eastern'

def main():
	# Date et heure courantes:
	date_heure = datetime.datetime.now()
	date_heure = (date_heure.astimezone(pytz.timezone(TZ)))
	date_heure = date_heure.strftime("%Y-%m-%d")
	
	# Ouvrir le TXT dans le mode de lecture:
	f = open("/home/ubuntu/Dropbox/Traductions/Soutien/revenu_jour.txt", 'r')
	s = f.readlines()
	p = str(s)
	
	# Faire la somme des revenus du jour:
	total = 0
	for line in s:
		try:
			total += float(line)
		except ValueError:
			print("Invalid")
		
	# Ajouter la somme dans le fichier "somme_revenu.txt":
	cmd = 'echo ' + str(date_heure) + ' CAD$ ' + str(total) + ' >> /home/ubuntu/Dropbox/Traductions/Soutien/revenu_total.txt'
	#print(cmd)
	os.popen(cmd)
	
	f.close()
	
	# Ouvrir le fichier "revenu_jour.txt" dans le mode écriture (pour l'éffacer):
	f = open("/home/ubuntu/Dropbox/Traductions/Soutien/revenu_jour.txt", 'w')
	f.close()

if __name__ == "__main__":
	main()
    
