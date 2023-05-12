text = input("masukkan kata: ")
oldText = input("masukkan kata yang ingin diganti: ")
newText = input("masukkan kata pengganti: ")

if oldText in text:
    replacedText = text.replace(oldText, newText)
    print(replacedText)