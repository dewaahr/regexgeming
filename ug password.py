import re
def cek_password(password):
    indikator=0
    pola=r"(?=.*?[A-Z])"
    besar=re.match(pola,password)
    if besar!=None:
        pola=r'(?=.*?[a-z])'
        kecil=re.match(pola,password)
        indikator=indikator+1
        if kecil!=None:
            pola=r'(?=.*?[0-9])'
            angka=re.match(pola,password)
            indikator=indikator+1
            if angka!=None:
                pola=r"(?=.*?[#?!@$%^&*-])"
                simbol=re.match(pola,password)
                if simbol!=None:
                    indikator=indikator+1

    spasi=r'(?=.*?[\s])'
    if re.match(spasi,password)!=None:
        print("Password tidak valid")
    elif len(password)>6:
        if len(password)>20:
            print("Password tidak valid")
        else:
            if indikator>2:
                print('Password kuat')
            else:
                print('Password lemah')
    else:
        print("Password tidak valid")
