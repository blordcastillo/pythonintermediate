def get_zipcode(zipcode):
    zipcode = str(zipcode)[:9]
    if len(zipcode) < 6:
        return zipcode
    zipcode = '{:0<9}'.format(zipcode)
    zipcode = zipcode[:5] + '-' + zipcode[5:]
    return zipcode
