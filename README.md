# 1 : datascience-examen van Johan Van Erum
    de code base bevat 2 notebooks in de map /notebooks
    -   examen-deel1-dataload, het eerste deel, gedaan op 4 juni 2024 vanaf 18:45 's avonds
    -   examen-deel2-analyse, het tweede deel, gedaan op 11 juni 2024 vanaf 18:45 's avonds
    deze notebooks vormen de oplossing van de student Johan Van Erum (ikke) voor het examen  
    
# 2 : wat is dit ?
    het examen data science, Syntra, 1ste jaar, gegeven door Tim Hellemans  
    gaat organisatorisch door in 2 delen, van thuis uit gedaan,  
    met Tim Hellemans als online proctor voor de studenten  

    de opgave wordt even voor starttijd bekend gemaakt  
    in de vorm van een notebook .... 
    en is terug te vinden in /documentation  

    De input gegevens zijn terug te vinden in /data/raw

# 3 : detail betreffende de opdracht zelf
    - deel 1: 4/6/2024  

    blablabla
    blablabla

    - deel 2: 11/6/2024  

    blablabla
    blablabla

# 4. uitvoeren : hoe weet ik snel wat het allemaal doet ?  
    doe een run all, nadat je de omgeving hebt opgezet  

    - voor notebook 'examen-deel1-dataload.ipynb'  
        - ga na uitvoering 'run all'

        direct naar sectie "G : uitvoeren van de simulatie (oplossing)"  
        en voer de cell uit met de functie mdls.simulatie(..) 
        als je de verschillende waarden voor de fabrieken BRU en STO 
        wil testen 
        - secties A t.e.m. E laden en manipuleren de data
        - sectie F analyseert de productie gegevens en onderzoekt de simulatie
        - in sectie G : zet de 2 lijnen met 'BRU','STO','ALL' actief of in commentaar voor resultaten relatief aan de fabriek  
        en voer de cel opnieuw uit, pas variabele 'use_random_seed' aan voor variabiliteit in de simulatie
        - outline opdracht 'examen-deel1-dataload.ipynb'  


    - voor notebook 'examen-deel2-analyse.ipynb'  
        - ga na uitvoering 'run all'  

        direct naar sectie "F : vragen en antwoorden "
        - secie F bevat telkens een paragraaf met de (herhaalde) vraag 
        en het bijbehorende antwoord (in kleur Cadetblue) in een aparte cell          
        - per vraag zie je onder het antwoord ook een aparte paragraaf 'Onderzoek' met de  
        (onderzoeks)code geschreven om het antwoord te kunnen formuleren  
        - sectie A t.e.m E bevat het laden en manipuleren de data
        - outline opdracht 'autoproductie.ipynb'  
    

    - tip  
        - gebruik de outline functie van VS code om snel naar het deel te gaan van je interesse  
        - voor data analyse voor beide opdrachten werd de Microsoft Data Wrangler extension gebruikt  

# 5. omgeving : opzetten van de omgeving  
    opgezet als .venv in VS code Python 3.12.3, zie enviroment file /requirements.txt  

# 6. eigen modules in /scripts 
    - /scripts/come_in_handy as cih
        - cih.show_info_about_column(..)  
        = in één keer de nodige gegevens zien van één enkele kolom  

    - scripts/my_constants.py 
        - bevat constanten die mogelijk hebruikbaar zijn, zoals bv. kleuren  
        opgezet na tip van Tim tijdens de les, wordt voorlopig nog niet gebruikt  

    - /scripts/my_matplotlib_standards.py as mypltstd  
        - mypltstd.my_matplotlib_pyplot_standards_setup(..)
        *opgezet na tip van Tim tijdens de les  
        voor grafische plot constanten en default setting  
