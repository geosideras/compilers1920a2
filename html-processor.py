import re

def repl(m):                         ##Συναρτηση που αναλογα με το τι ειναι το group(1) της μεταβλητης m επιστρεφει το καταλληλο χαρακτηρα 
	if m.group(1)=="amp" :
		return '&'
	if m.group(1)=="gt" :
		return '>'
	if m.group(1)=="lt" :
		return '<'
	if m.group(1)=="nbsp" :
		return ' '

titlos= re.compile(r'(<title>)(.+?)</title>')  ##εκφραση που παιρνει οτι εχει αναμεσα στα tags title
sxolia= re.compile(r'<!--(.+?)-->',re.DOTALL)  ##εκφραση που παιρνει τα σχολια , δηλαδη οτι υπαρχει αναμεσα σε <!-- και --> 
other_tags= re.compile(r'<(script)|(style)>(.+?)</(script)|(style)>')  ##εκφραση που παιρνει οτι εχει αναμεσα στα tags script και style
href= re.compile(r'<a(.+?)(href="(.+?)")(.+?)>(.+?)</a>')  ##εκφραση που παιρνει οτι εχει αναμεσα στα tags a 
tags= re.compile(r'<(.+?)>',re.DOTALL)  ##εκφραση που παιρνει οτι εχει αναμεσα σε ολα tags title
cntitics= re.compile(r'&(.+?);',re.DOTALL)  ##εκφραση που παιρνει οτι εχει αναμεσα στους χαρακτηρες & και ;
many_spaces= re.compile(r'\s+')  ##εκφραση που παιρνει οποιοδηποτε σημειο του κειμενου που εχει δυο η περισσοτερες φορες το κενο χαρακτηρα

with open("testpage.txt","r") as fp:  ##ανοιγουμε το αρχειο εισοδου
	text = fp.read()

	f= open("output.txt","w+")  ##ανοιγουμε ενα νεο αρχειο εξοδου
	
	for m in titlos.finditer(text): ##παιρνουμε οτι εχει αναμεσα στα title tags
		print(m.group(2), file=f)  ##και τα τυπωνουμε στο αρχειο f

	text = sxolia.sub(' ',text) 	##γραφουμε στην μεταβλητη text οτι ειχε , αντικαταστωντας εκφραση sxolia με ενα κενο χαρακτηρα 
	text = other_tags.sub(' ',text) ##γραφουμε στην μεταβλητη text οτι ειχε , αντικαταστωντας εκφραση other_tags με ενα κενο χαρακτηρα
	for m in href.finditer(text):  	##περνουμε οτι εχει μεσα στο href="" του a tag και οτι εχει αναμεσα στο <a> και </a> 
		print(m.group(3),m.group(5), file=f)  ##και τα τυπωνουμε στο αρχειο f
	text = tags.sub(' ',text)  		##γραφουμε στην μεταβλητη text οτι ειχε , αντικαταστωντας εκφραση tags με ενα κενο χαρακτηρα
	text = cntitics.sub(repl,text)	 ##γραφουμε στην μεταβλητη text οτι ειχε , αντικαταστωντας εκφραση cntitics με ενα κενο χαρακτηρα
	text = many_spaces.sub(' ',text)  ##γραφουμε στην μεταβλητη text οτι ειχε , αντικαταστωντας εκφραση many_spaces με ενα κενο χαρακτηρα

	print(text, file=f)  ##εκτυπωνουμε στο αρχειο f την μεταβλητη text
	
	
	
