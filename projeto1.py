import PyPDF2
import os
#mesclador
merger = PyPDF2.PdfMerger()

#listar os pdfs

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

#agora juntar todos os pdfs

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}")

#criar pdf final

merger.write("PDF final.pdf")
