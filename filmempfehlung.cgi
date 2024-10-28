#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import cgi

def filmempfehlung(genre, jahr, schauspieler, datenquelle):
    empfehlungen = []
    with open(datenquelle, 'r') as file:
        for line in file:
            film_info = line.strip().split(':')
            if len(film_info) == 4:
                if (genre.lower() == film_info[1].lower() or genre.lower() == 'alle') and                    (jahr == film_info[2] or jahr == '') and                    (schauspieler.lower() in film_info[3].lower() or schauspieler == ''):
                    empfehlungen.append(film_info[0])
    return empfehlungen

def main():
    print("Content-Type: text/html")    # Content-Type header setzen
    print()    # Leerzeile zwischen Header und Inhalt

    # Benutzereingaben aus dem Formular abrufen
    form = cgi.FieldStorage()
    genre = form.getvalue('genre', 'alle')
    jahr = form.getvalue('jahr', '')
    schauspieler = form.getvalue('schauspieler', '')

    # Filmdatenquelle
    datenquelle = 'film.txt'

    # Filmliste basierend auf Benutzereingaben abrufen
    empfehlungen = filmempfehlung(genre, jahr, schauspieler, datenquelle)

    # HTML-Ausgabe
    print("<!DOCTYPE html>")
    print("<html lang='de'>")
    print("<head>")
    print("<meta charset='utf-8'>")
    print("<title>Filmempfehlungen</title>")
    print("<link rel='stylesheet' href='m.css' type='text/css'>")
    print("</head>")
    print("<body>")
    print("<h1 class='textsty' style=' text-align:center; font-family:courier; color: rgb(232,139,136); font-size:200%;'>Filmempfehlungen:</h1>")
    print("<div style='margin-top:300px'>")
    if empfehlungen:
        print("<ul>")
        for film in empfehlungen:
            print("<li style='font-family:courier; color: rgb(232,139,136); font-size:150%;'>{}</li>".format(film))
        print("</ul>")
    else:
        print("<p>Keine Filme gefunden.</p>")
    print("</div>")
    print("</body>")
    print("</html>")

if __name__ == "__main__":
    main()
