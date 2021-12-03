def kdv(fiyat):
    ''' fiyat değişkeninin %18'ini verir. '''
    return fiyat * 0.18

def aracOtv(fiyat,kategori,mh):
    '''
    fiyat,
    kategori = ticari veya lüks
    mh = motor hacmi
    '''
    if(kategori == "ticari"):
        return fiyat * 0.6
    elif(kategori == "lüks"):
        if(mh < 2000 ):
            return fiyat * 0.8
        else :
            return fiyat * 1.6
    else:
        return fiyat * 0.4

def sonFiyat (fiyat,kategori,mh):
    return aracOtv(fiyat,kategori,mh) + kdv(fiyat) +  fiyat

