# 1 : datascience-examen van Johan Van Erum
    de code base bevat 3 notebooks in de map /notebooks
    -   examen-deel1-oplossing, het eerste deel, gedaan op 4 juni 2024 vanaf 18:45 's avonds
    -   examen-deel1-oplossing-afgewerkt, het eerste deel, gedaan op 4 juni 2024, vervolledigd buiten tijd
    -   examen-deel1-original, de opgave van het examen
    -   examen-deel2-oplossing, het tweede deel, gedaan op 11 juni 2024 vanaf 18:45 's avonds
    -   examen-deel2-original, de opgave van het examen

    deze notebooks vormen de oplossing van de student Johan Van Erum voor het examen  
    
# 2 : wat is dit ?
    Dit betreft het examen data science, Syntra, 1ste jaar, gegeven door Tim Hellemans  
    en gaat organisatorisch door in 2 delen, van thuis uit gedaan,  
    met Tim Hellemans als online proctor voor de studenten  

    De opgave wordt even voor starttijd bekend gemaakt  
    - in de vorm van een notebook in /notebooks  
    - de opgave zelf is terug te vinden in /notebooks/examen-deel(?)-original  
    - de bijbehorende gegevens zijn terug te vinden in /data/geboortes

# 3 : detail betreffende de opdracht zelf
    - deel 1: 4/6/2024  
    geen specifieke opmerkingen

    - deel 2: 11/6/2024  
    opmerkingen nog toe te voegen tijdens examen
    
# 4. uitvoeren : hoe weet ik snel wat het allemaal doet ?  
    doe een run all, nadat je de omgeving hebt opgezet  
        
    - tip  
        - gebruik de outline functie van VS code om snel naar het deel te gaan van je interesse  
        - voor data analyse voor beide opdrachten werd de Microsoft Data Wrangler extension gebruikt  

# 5. omgeving : opzetten van de omgeving  
    opgezet als .venv in VS code Python 3.12.3, zie enviroment file /requirements.txt  

# 6. eigen modules in /scripts 
    - /scripts/my_constants_standards.py as mymc
        - functie : mycs.my_colors_setup()  
          bevat constanten die mogelijk hebruikbaar zijn  
          zoals bv. kleuren  
        
    - /scripts/my_matplotlib_standards.py as myms
        - functie : myms.my_matplotlib_pyplot_setup()  
          default setting voor pyplot grafieken  