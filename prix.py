#!/usr/bin/python3

import sys
import getopt
import os
import PyPDF2

def main(argv):
	nom = argv[2]

	# Ouvrir le PDF et compter le nombre des pages:
	pdfFileObject = open(nom, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
	pages = pdfReader.numPages
	
	# Calculer le prix de la traduction:
	# Traduction simple:
	if sys.argv[1] == '1':
		prix = round(pages * 8, 2)
		type = 'Simple'
		
	# Traduction assermentee:
	else:
		prix = round(pages * 12, 2) + 20
		type = 'Assermentee'
	
	# Afficher les informations:
	print("Numero de pages:", pages)
	print("Prix: CAD$", prix)
	print("Type:", type)
	
	# Deplacer le PDF vers le dossier approprié en changeant son nom:
	cmd = 'mv ' + nom + ' ' + type + '/' + os.path.splitext(nom)[0] + '.pdf'
	#print(cmd)
	os.popen(cmd)
	
	
	# Ajouter le prix dans l'archive "revenue_du_jour.txt"
	cmd = 'echo ' + str(prix) + ' >> /home/ubuntu/Dropbox/Traductions/Soutien/revenu_jour.txt'
	#print(cmd)
	os.popen(cmd)
	
	# Fermer le PDF:
	pdfFileObject.close()
    

if __name__ == "__main__":
    main(sys.argv)
