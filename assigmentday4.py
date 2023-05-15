if __name__ == '__main__':
    def caesarcipher(kalimat, kata):
        encryiption = ''
        word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for text in kalimat.upper():
            if text.isalpha():
                encryiption += word[word.index(text)-26+kata]
            else:
                encryiption += text
        return encryiption
    
    kalimat = 'Meet me by the rose bushes tonight.'
    kata = 4
    encryiption = caesarcipher(kalimat, kata)
    print(encryiption)


