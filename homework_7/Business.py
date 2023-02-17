# Ստեղծել contacts.txt ֆայլ, ավելացնել հետևյալ (First_Name Last_Name, Title, Extension, Email)
# տեքստը՝ օգտագվելով Python-ի ֆայլային ֆունկցիոնալից։ Ստորև ուղարկում եմ pdf ֆայլ 
# (Business_Proposal.pdf), որի պարունակությունը կարդալով պետք է դուրս բերել 
# AUTHORS: դաշտը իր ենթատողերով և ավելացնել contacts.txt ֆայլում։
import PyPDF2

my_file = open('contacts.txt', 'a')
text = 'First_Name Last_Name, Title, Extension, Email\n'
my_file.write(text)
pdf_file = open('Business_Proposal.pdf', 'rb')
my_file.write(PyPDF2.PdfReader(pdf_file).pages[1].extract_text())
my_file.close()
pdf_file.close()
print('well done')