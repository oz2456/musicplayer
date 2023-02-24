#Project Music Player
input("Only One Singer Available ?")
f = input("Which album : AH , KISSLAND , DAWN , MDM , STARBOY")
if f == "AH":
    print('ENJOY')
    from os import startfile
    startfile(r'H:\Downloads\Weeknd\AH.mp3')
elif f == "KISSLAND":
    print('ENJOY')
    from os import startfile
    startfile(r'H:\Downloads\Weeknd\KISSLAND.mp3')
elif f == "DAWN":
    print('ENJOY')
    from os import startfile
    startfile(r'H:\Downloads\Weeknd\DAWN.mp3')
elif f == "STARBOY":
    print('ENJOY')
    from os import startfile
    startfile(r'H:\Downloads\Weeknd\STARBOY.mp3')
elif f == "MDM":
    print('ENJOY')
    from os import startfile
    startfile(r'H:\Downloads\Weeknd\MDM.mp3')
else:
    ("This is my first project it only plays music"
     "Error 401 -Only music to be played")

