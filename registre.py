#!/usr/bin/python3

import sys
import getopt
import os
import datetime
import pytz
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import blue

TZ = 'US/Eastern'

# Fonction Put_Watermark:
def put_watermark(laDate, input_pdf, output_pdf, watermark, registry):
	watermark_instance = PdfFileReader(watermark)
	watermark_page = watermark_instance.getPage(0)
	pdf_reader = PdfFileReader(input_pdf)
	pdf_writer = PdfFileWriter()
	
	registry_instance = PdfFileReader(registry)
	registry_page = registry_instance.getPage(0)


	# Creer nouveau PDF (ligne bleu):
	canvas = Canvas("extra.pdf", pagesize=(8.3*72,11.7*72))
	canvas.setFillColor(blue)
	canvas.drawString(120, 50, laDate)
	canvas.save()
	
	canvas_instance = PdfFileReader("extra.pdf")
	canvas_page = canvas_instance.getPage(0)
	
	
	# Ajouter la marque de page:
	for page in range(pdf_reader.getNumPages()):
		page = pdf_reader.getPage(page)
		page.mergePage(watermark_page)
		page.mergePage(canvas_page)
		pdf_writer.addPage(page)
	
	
	# Effacer pdf avec la ligne bleu:
	cmd = 'rm extra.pdf'
	#print(cmd)
	os.popen(cmd)
	
	# Ajouter la dernier page:
	pdf_writer.addPage(registry_page)

	with open(output_pdf, 'wb') as out:
		pdf_writer.write(out)

	# Enlever traduction sans registre:
	cmd = 'rm ' + input_pdf
	#print(cmd)
	os.popen(cmd)

	# Deplacer fichier vers le dossier "Tr.Registrees":
	cmd = 'mv ' + output_pdf + ' Tr.Registrees/' + os.path.splitext(output_pdf)[0] + '.pdf'
	#print(cmd)
	os.popen(cmd)


# Fonction principale:
def main():

	# Date et heure corantes:
	date_heure = datetime.datetime.now()
	date_heure = (date_heure.astimezone(pytz.timezone(TZ)))
	date_heure = date_heure.strftime("%Y%m%d-%Hh%Mm%S")
	
	directory = '/home/ubuntu/Dropbox/Traductions/Assermentee/'
	
	# Boucle pour chercher tous les fichiers PDF dans le dossier courant:
	for file in os.listdir(directory):
		if not file.endswith(".pdf"):
			continue
		nom_fichier_final = os.path.splitext(file)[0] + '-' + date_heure + '-Traduction_Assermentee.pdf'
		laDate = date_heure + ' BFNascimento#182ESLima#511 @RGTraduction'
		
		
		# Appele de la fonction Put_Watermark:
		put_watermark(
		laDate,
    		input_pdf=file,
    		output_pdf=nom_fichier_final,
    		watermark='/home/ubuntu/Dropbox/Traductions/Soutien/marqueur.pdf',
    		registry='/home/ubuntu/Dropbox/Traductions/Soutien/signature.pdf'
		)

    	

if __name__ == "__main__":
	main()
    
