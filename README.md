# Skripte-za-preimenovanje

UVOD

Povremeno radim u jednoj tvrtki koja se bavi održavanjem web stranica u Joomli. Većina posla se svodi na objavu raznih pravnih dokumenata (javni pozivi, javne nabave, savjetovanja s javnošću, itd.). Moj problem je bio što je svaki od tih dokumenata trebao prije objave biti preimenovan. Trebalo je zamijeit č, ć, š, ž, đ za c, c, s, z, d, trebalo je sve razmake zamijeniti za donje crte, ukloniti duple razmake, ukloniti točke, zareze, upitnike, uskličnike i sve slične znakove. Također je trebalo dokumente pretvarati u u .pdf ili u .docx formate.

Druga stvar su slike. S obzirom da sve slike koje se objavljuju na stranicama moraju biti smanjene na odrđenu veličinu da zauzimaju manje prostora i moraju biti preimenovane na način da se prva slika zove "1", sljedeća "2", sljedeća "3", itd.

Moj šef je to sve ručno radio vjerojatno 10-ak godina, ali meni se to činilo malo besmisleno pa sam napravio ovih nekoliko skripta u Pythonu čisto da sebi i njemu olakšam malo život i razbijem dosadu.

1. "Preimenovanje i resizanje slika.py"

Ova skripta preimenuju sve slike koje se nalaze u "Download"/"Preuzimanja" mapi i smanjuje ih na veličinu na način da veća dimenzija bude 1000 px. 

Npr.
Ako je slika dimezija 2000X1200, bit će smanjena na 1000X600. Ako je slika dimezija 1200X2000, bit će smanjena na 600X1000.

2. "Preimenovanje, pretvaranje u PDF i brisanjem.py"

Ova skripta preimenuje datoteke na način napisan u uvodu i pretvara ih u .pdf, ukoliko su datoteke u nekom od formata koje podržava Microsoft Word program. Nakon pretvaranja, skripta briše orginalnu datoteku u Word formatu.

3. "Preimenovanje, pretvaranje u PDF bez brisanja.py"

Ova skripta preimenuje datoteke na način napisan u uvodu i pretvara ih u .pdf, ukoliko su datoteke u nekom od formata koje podržava Microsoft Word program. Nakon pretvaranja, skripta briše zadržava pretvorenu i orginalnu datoteku.

4. "Preimenovanje i pretvaranje u WORD.py"
Ova skripta preimenuje datoteke na način napisan u uvodu i pretvara ih u .docx, ukoliko su datoteke u .pdf formatu.

5. "Samo preimenovanje.py"
Ova skripta samo preimenuje sve datoteke koje imaju ekstenziju .xlsx, .xls, .docx, .doc, .dotd, .pdf, .zip, na prethodno spomenuti način.
