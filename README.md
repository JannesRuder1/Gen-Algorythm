# Checkliste fÃ¼r die Anwendungsklasse 1 (Markdown-Template)

## Nutzungshinweise
Diese Checkliste liefert Empfehlungen zur Software-Entwicklung. PrimÃ¤r richten sich diese an Software-Entwickler zur SelbsteinschÃ¤tzung entwickelter Software und als Ideengeber fÃ¼r die weitere Entwicklung. Die Checkliste liefert keine neuen, revolutionÃ¤ren AnsÃ¤tze zur Software-Entwicklung. Sie hilft aber notwendige, wesentliche Schritte der Software-Entwicklung nicht zu vergessen. Zudem kÃ¶nnen die Empfehlungen als Argumentationshilfe dienen.

Die Empfehlungen sind mit Fokus auf Wissenserhalt und gute Software-Engineering-Praxis erstellt. Sie unterstÃ¼tzen dabei, die Nachvollziehbarkeit und Nachhaltigkeit entwickelter Software zu erhalten. Die Empfehlungen motivieren den Einsatz von Tools, die Erstellung von Dokumentation, die Etablierung von Prozessen oder die Einhaltung von Prinzipien. Bei der Bewertung einer Empfehlung empfiehlt es sich daher zu Ã¼berlegen, inwieweit der genannte Aspekt umgesetzt ist und ob Verbesserungsbedarf besteht. Dies kann man beispielsweise wie folgt umsetzen:

* Gibt es derzeit keinen Verbesserungsbedarf und die Empfehlung ist prinzipiell passend adressiert? Status: **ok**
* Gibt es Verbesserungspotential, welches in nÃ¤chster Zeit umgesetzt werden kann bzw. sollte? Status: **todo**, Verbesserungsbedarf unter Bemerkungen festhalten
* Ist die Empfehlung derzeit noch nicht relevant, kÃ¶nnte aber in einer spÃ¤teren Entwicklungsphase hilfreich sein? Status: **future**
* Ist die Empfehlung im Entwicklungskontext nicht sinnvoll umsetzbar? Status: **n.a.** (not applicable, nicht zutreffend), Grund unter Bemerkungen erlÃ¤utern

> Den Status zwischen `**[]**` vermerken. Die Bemerkungen unterhalb der Empfehlung als Liste (z.B. `* Repository einrichten`) erfassen.

## Zusammenfassung der Ergebnisse
Die Software erreicht Anwendungsklasse [1, 2 oder 3].

Der Schwerpunkt zukÃ¼nftiger Verbesserungen liegt auf:

## Inhaltsverzeichnis
[[Qualifizierung](#qualifizierung)] [[Anforderungsmanagement](#anforderungsmanagement)] [[Software-Architektur](#software-architektur)] [[Ã„nderungsmanagement](#aenderungsmanagement)] [[Design und Implementierung](#design-implementierung)] [[Software-Test](#software-test)] [[Release-Management](#release-management)] [[Automatisierung und AbhÃ¤ngigkeitsmanagement](#automatisierung-abhaengigkeiten)] 

## Qualifizierung <a name="qualifizierung"></a>
**[]** Der Software-Verantwortliche kennt die verschiedenen Anwendungsklassen und weiÃŸ, welche fÃ¼r seine Software anzustreben ist. *(EQA.1, ab Anwendungsklasse 1)*

**[]** Der Software-Verantwortliche weiÃŸ, wie er gezielt UnterstÃ¼tzung zu Beginn und im Verlauf der Entwicklung anfordern und sich mit anderen Kollegen zum Thema Software-Entwicklung austauschen kann. *(EQA.2, ab Anwendungsklasse 1)*

**[]** Die an der Entwicklung Beteiligten ermitteln den Qualifikationsbedarf in Bezug auf ihre Rolle  und die angestrebte Anwendungsklasse. Sie kommunizieren diesen Bedarf an den Vorgesetzten. *(EQA.3, ab Anwendungsklasse 1)*

**[]** Den an der Entwicklung Beteiligten stehen die fÃ¼r ihre Aufgaben benÃ¶tigten Werkzeuge zur VerfÃ¼gung und sie sind geschult in deren Benutzung. *(EQA.4, ab Anwendungsklasse 1)*

## Anforderungsmanagement <a name="anforderungsmanagement"></a>
**[]** Die Aufgabenstellung ist mit allen Beteiligten abgestimmt und dokumentiert. Sie beschreibt in knapper, verstÃ¤ndlicher Form die Ziele, den Zweck der Software, die wesentlichen Anforderungen und die angestrebte Anwendungsklasse. *(EAM.1, ab Anwendungsklasse 1)*

**[]** Die Randbedingungen sind erfasst. *(EAM.3, ab Anwendungsklasse 1)*

## Software-Architektur <a name="software-architektur"></a>
**[]** Wesentliche Architekturkonzepte und damit zusammenhÃ¤ngende Entscheidungen sind zumindest in knapper Form dokumentiert. *(ESA.2, ab Anwendungsklasse 1)*

## Ã„nderungsmanagement <a name="aenderungsmanagement"></a>
**[]** Die wichtigsten Informationen, um zur Entwicklung beitragen zu kÃ¶nnen, sind an einer zentralen Stelle abgelegt. *(EÃ„M.2, ab Anwendungsklasse 1)*

**[]** Bekannte Fehler, wichtige ausstehende Aufgaben und Ideen sind zumindest stichpunktartig in einer Liste festgehalten und zentral abgelegt. *(EÃ„M.5, ab Anwendungsklasse 1)*

**[]** Ein Repository ist in einem Versionskontrollsystem eingerichtet. Das Repository ist angemessen strukturiert und enthÃ¤lt mÃ¶glichst alle Artefakte, die zum Erstellen einer nutzbaren Version der Software und deren Test erforderlich sind. *(EÃ„M.7, ab Anwendungsklasse 1)*

**[]** Jede Ã„nderung des Repository dient mÃ¶glichst einem spezifischen Zweck, enthÃ¤lt eine verstÃ¤ndliche Beschreibung und hinterlÃ¤sst die Software mÃ¶glichst in einem konsistenten, funktionierenden Zustand. *(EÃ„M.8, ab Anwendungsklasse 1)*

## Design und Implementierung <a name="design-implementierung"></a>
**[]** Es werden die Ã¼blichen Konstrukte und LÃ¶sungsansÃ¤tze der gewÃ¤hlten Programmiersprache eingesetzt sowie ein Regelsatz hinsichtlich des Programmierstils konsequent angewendet. Der Regelsatz bezieht sich zumindest auf die Formatierung und Kommentierung. *(EDI.1, ab Anwendungsklasse 1)*

**[]** Die Software ist mÃ¶glichst modular strukturiert. Die Module sind lose gekoppelt, d.h., ein einzelnes Modul hÃ¤ngt mÃ¶glichst gering von anderen Modulen ab. *(EDI.2, ab Anwendungsklasse 1)*

**[]** Im Quelltext und in den Kommentaren sind mÃ¶glichst wenig duplizierte Informationen enthalten. (â€žDon`t repeat yourself.â€œ) *(EDI.9, ab Anwendungsklasse 1)*

**[]** Es werden einfache, verstÃ¤ndliche LÃ¶sungen bevorzugt eingesetzt.  (â€žKeep it simple and stupid.â€œ). *(EDI.10, ab Anwendungsklasse 1)*

## Software-Test <a name="software-test"></a>
**[]** Die grundlegenden Funktionen und Eigenschaften der Software werden in einer mÃ¶glichst betriebsnahen Umgebung getestet. *(EST.4, ab Anwendungsklasse 1)*

**[]** Das Repository enthÃ¤lt mÃ¶glichst alle fÃ¼r den Test der Software erforderlichen Artefakte. *(EST.10, ab Anwendungsklasse 1)*

## Release-Management <a name="release-management"></a>
**[]** Jedes Release besitzt eine eindeutige Release-Nummer. Anhand der Release-Nummer lÃ¤sst sich der zugrunde liegende Softwarestand im Repository ermitteln. *(ERM.1, ab Anwendungsklasse 1)*

**[]** Das Release-Paket enthÃ¤lt oder verweist auf die Nutzer-Dokumentation. Sie besteht zumindest aus Installations-, Nutzungs- und Kontaktinformationen sowie den Release Notes. Im Fall der Weitergabe des Release-Pakets an Dritte auÃŸerhalb des DLR, sind die Lizenzbedingungen unbedingt beizulegen. *(ERM.2, ab Anwendungsklasse 1)*

**[]** WÃ¤hrend der Release-DurchfÃ¼hrung werden alle vorgesehenen TestaktivitÃ¤ten ausgefÃ¼hrt. *(ERM.6, ab Anwendungsklasse 1)*

**[]** Vor der Weitergabe des Release-Pakets an Dritte auÃŸerhalb des DLR ist sicherzustellen, dass eine Lizenz festgelegt ist, die Lizenzbestimmungen verwendeter Fremdsoftware eingehalten werden und alle erforderlichen Lizenzinformationen dem Release-Paket beigelegt sind. *(ERM.9, ab Anwendungsklasse 1)*

**[]** Vor der Weitergabe des Release-Pakets an Dritte auÃŸerhalb des DLR ist sicherzustellen, dass die Regelungen zur Exportkontrolle eingehalten werden. *(ERM.10, ab Anwendungsklasse 1)*

## Automatisierung und AbhÃ¤ngigkeitsmanagement <a name="automatisierung-abhaengigkeiten"></a>
**[]** Der einfache Build-Prozess lÃ¤uft grundlegend automatisiert ab und notwendige manuelle Schritte sind beschrieben. Zudem sind ausreichend Informationen zur Betriebs- und Entwicklungsumgebung vorhanden. *(EAA.1, ab Anwendungsklasse 1)*

**[]** Die AbhÃ¤ngigkeiten zum Erstellen der Software sind zumindest mit dem Namen, der Versionsnummer, dem Zweck, den Lizenzbestimmungen und der Bezugsquelle beschrieben. *(EAA.2, ab Anwendungsklasse 1)*

**[]** Das Repository enthÃ¤lt mÃ¶glichst alle Bestandteile, um den Build-Prozess durchfÃ¼hren zu kÃ¶nnen. *(EAA.10, ab Anwendungsklasse 1)*