from app import MainApp
from models import create_dictionary
import secrets

def main():
    dct = create_dictionary()
    keyslist = list(dct.keys())
    secrets.SystemRandom().shuffle(keyslist)
    app = MainApp(keyslist,dct)
    app.mainloop()

if __name__ == "__main__":
    main()
