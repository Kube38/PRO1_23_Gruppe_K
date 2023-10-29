def berechne_note(wetter, betriebssystem, note):
    #Wetterbedingungen als Einfluss
    if wetter == "sonnig":
        note =- 0.3
    if wetter == "regnerisch":
        note =+ 0.3
    if wetter == "stürmisch":
        note =+ 0.6

    #Betriebssystem als Einfluss
    if betriebssystem == "Linux":
        note =- 1.0
    if betriebssystem == "Windows":
        note =+ 0.3
    if betriebssystem == "Mac":
        note =+ 1.0

    return note
