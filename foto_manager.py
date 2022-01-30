import os

# prende la data dal nome del file e la restituisce
def get_date(filename, prefix):
    name = os.path.basename(filename)
    name = name.removeprefix(prefix)
    anno = ""
    mese = ""
    for i in range(4):
        anno = anno + name[i]
    mese = mese + name[4] + name[5]
    # print("anno = "+anno)
    # print("mese = "+mese)
    return anno, mese

def ask_prefix():
    print("\nI nomi delle foto solitamente contengono la data della creazione, il formato potrebbe essere:"
          "\n\tIMG-20200130-WA00.jpg\t\tPrefisso = IMG-"
          "\nSono presenti informazioni diverse tra fotocamera, whatsapp etc.. quindi devi specificare il prefisso "
          "altrimenti non verranno riconosciute.\nSe non e' presente basta premere invio.")
    print("\nPrefisso > ")
    return input()


""" modifica la stringa per spostare i files, poi li sposta."""
def replace_foto(file, source, destination):
    os.replace(source+"\\"+file, destination+"\\"+file)

def get_mese(mese):
    m = int(mese)
    if m == 1:
        return "gennaio"
    if m == 2:
        return "febbraio"
    if m == 3:
        return "marzo"
    if m == 4:
        return "aprile"
    if m == 5:
        return "maggio"
    if m == 6:
        return "giugno"
    if m == 7:
        return "luglio"
    if m == 8:
        return "agosto"
    if m == 9:
        return "settembre"
    if m == 10:
        return "ottobre"
    if m == 11:
        return "novembre"
    if m == 12:
        return "dicembre"


def is_valid_foto(filename, prefix):
    return True if prefix in filename else False


""" Gestisce cartelle e files dividendo tra anni e mesi, dentro la cartella data. Per ogni file crea (se non c'e') una
cartella anno, e al suo interno delle cartelle mese (se non ci sono) in base alla data della foto, e divide le foto
presenti nella cartella root, all'interno di queste cartelle anno e mese."""
def choose_dir(directory, filename, prefix):
    if is_valid_foto(filename, prefix):

        anno, mese = get_date(filename, prefix)

        if int(mese) < 1:
            print("\n\nErrore >> Mese = 0 wtf ?")
            exit(0)

        # print("dir = "+directory)
        # print("file = "+filename)
        target_dir_anno = directory+"\\anno "+str(anno)
        # print("target anno = "+target_dir_anno)
        target_dir_mese = target_dir_anno+"\\"+get_mese(mese)+" "+str(anno)
        # print("target mese = "+target_dir_mese)

        try:
            os.mkdir(target_dir_anno)
        except:
            pass

        try:
            os.mkdir(target_dir_mese)
        except:
            pass

        replace_foto(filename, directory, target_dir_mese)
        # controlla esistenza cartella anno
        # la crea se necessario
        # controlla esistenza cartella mese
        # la crea se necessario
        return 0
    else:
        return 1


def main():
    banner()
    print("\nI file non riconosciuti verranno lasciati nella cartella di partenza.")
    print("\nPercorso Cartella da sistemare > ")
    directory = input()

    prefix = ask_prefix()
    unknown = 0
    # per ogni foto che trova ( controlla i formati)
    for filename in os.listdir(directory):
        unknown += choose_dir(directory, filename, prefix)

    print("\n\t >> Operazione completa -")
    print("\n\t >> File non riconosciuti : "+str(unknown)+" -"+"\t\t\t\t\t- FlowerBot-00")

def banner():
    print("----------------------")
    print("#\tFoto Manager")
    print("----------------------")

def test():
    return "r", "s"

main()