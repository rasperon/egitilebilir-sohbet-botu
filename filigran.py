# filigran.py
import os

def yazdir_logo():
    # CMD ekranını temizle
    os.system("cls" if os.name == "nt" else "clear")

    logo = """

██████████████████████████████████████████████████
█▄─▄▄▀██▀▄─██─▄▄▄▄█▄─▄▄─█▄─▄▄─█▄─▄▄▀█─▄▄─█▄─▀█▄─▄█
██─▄─▄██─▀─██▄▄▄▄─██─▄▄▄██─▄█▀██─▄─▄█─██─██─█▄▀─██
▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀
    """
    print(logo)

# filigran dosyası içindeki ASCII logosunu yazdırıyoruz
if __name__ == "__main__":
    yazdir_logo()
