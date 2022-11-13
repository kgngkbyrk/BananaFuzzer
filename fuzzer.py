import requests
import climage


output = climage.convert('banana.jpg', is_8color=True, 
                         palette='tango', is_256color=False)
print(output)
url=input("target url: ")
ext=input("ext: ")
wlist=input("path of wordlist: ")

print("BananaFuzzer started fuzzing...")

wlistlines=open(wlist, "r").readlines()

for i in range(0, len(wlistlines)):
    enum=wlistlines[i].replace("\n","")
    r=requests.get(url+"/"+enum+ext)

    if r.status_code != 404:
        print(url+"/"+enum+ext+" - "+str(r.status_code))

print("Done!\nExiting...")