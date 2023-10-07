# IT-forensik
Handledning: 
Hur man använder deepscan.py för att djupskanna en USB-enhet

Introduktion:
Detta script kan du använda för att djupskanna en USB-enhet för att identifiera potentiella filer raderade filer.
Med hjälp av filsignaturer kan vi detektera och potentiellt återskapa raderade filer. (:


1- Säkerställ att du har Python installerat på din dator.
2- Klona filen eller kopiera koden till en fil med namnet deepscan.py.
 
python deepscan.py /dev/sdb1

Byt ut /dev/sdb1 med sökvägen till din USB-enhet.

Tolka resultatet.
Scriptet kommer att skanna enheten och rapportera potentiella filsignaturer den hittar. 
Om en signatur identifieras, betyder det att det kan finnas en raderad fil av den typen på enheten.

Varning, tänk på följande sak!!!
Var mycket försiktig när du arbetar med rätt enhetsvägar. 
Se till att du läser från rätt enhet.
Detta verktyg identifierar bara potentiella filsignaturer. Det garanterar inte fullständig eller korrekt återställning av filen.
Försök inte skriva till enheten medan du skannar den.
Slutsats:
deepscan.py är ett enkelt men kraftfullt verktyg för att identifiera raderade filer på en USB-enhet. 
Genom att förstå och använda detta verktyg kan du ta ett steg mot att bli mer skicklig inom dataåterställning!

