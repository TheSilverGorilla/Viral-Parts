import zipfile
import tqdm
from time import sleep

def zip_cracker(word_file, zip_file):
    passwd = []
    length_list = len(list(open(word_file, 'rb')))
    with open(word_file, 'rb') as file:
        for i in file:
            for element in i.split():
                try:
                    zip_file.extractall(pwd=element.strip())
                    passwd.append(element.decode())
                except:
                    pass
        for t in tqdm.tqdm(range(0, length_list), desc = "Completing bruteforce..."):
            sleep(0.0001)
    if len(passwd)!=0:
        print("Password is " + passwd[0])
    else:
        print("Choose a different word list to bruteforce from.")

def main():
    txt_file_input = input("Choose a file to bruteforce the zipfile: ")
    zip_file_input = input("Choose a zip file to attack: ")
    zip_file = zipfile.ZipFile(zip_file_input)
    zip_cracker(txt_file_input, zip_file)

if __name__ == '__main__':
    main()
