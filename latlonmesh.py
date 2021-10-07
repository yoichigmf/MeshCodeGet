# -*- coding: utf-8 -*-
#   https://www.gis-py.com/entry/py-latlon2mesh    こちらのコードを参照  4次メッシュ部分を追加
#
#     2021.10.7  Y.Kayama
#

def getmeshID(lat, lon):
    #1次メッシュ
    quotient_lat, remainder_lat = divmod(lat * 60, 40)
    first2digits = str(quotient_lat)[0:2]

    #1次メッシュ下2けた
    last2digits = str(lon - 100)[0:2]
    remainder_lon = lon - int(last2digits) - 100

    #1次メッシュ
    first_mesh = first2digits + last2digits
    
    #if level == 1:
   #     return meshid_1

    #2次メッシュ上1けた
    first1digits, remainder_lat = divmod(remainder_lat, 5)

    #2次メッシュ下1けた
    last1digits, remainder_lon = divmod(remainder_lon * 60, 7.5)

    #2次メッシュ
    second_mesh = first_mesh + str(first1digits)[0:1] + str(last1digits)[0:1]

    #3次メッシュ上1けた
    first1digits, remainder_lat = divmod(remainder_lat * 60, 30)

    #3次メッシュ下1けた
    last1digits, remainder_lon = divmod(remainder_lon * 60, 45)

    #3次メッシュ
    third_mesh = second_mesh + str(first1digits)[0:1] + str(last1digits)[0:1]
    
    
    
    
        #4次メッシュ y けた
    first1digit, remainder_lat = divmod(remainder_lat , 15)

    print("first1 " + str(first1digit) + " remainder_lat " + str(remainder_lat) )
    
    #4次メッシュ x けた
    last1digit, remainder_lon = divmod(remainder_lon , 22.5)
    
    print("last1 " + str(last1digit) + " remainder_lon " + str(remainder_lon) )
    
    if first1digit > 0:
           if last1digit > 0:
                digit = "4"
           else:
                digit = "3"
    else:
           if last1digit > 0:
                digit = "2"
           else:
                digit = "1"
                
                 
    
    forth_mesh = third_mesh + digit
    
    
    

    print("1次メッシュ:" + first_mesh)
    print("2次メッシュ:" + second_mesh)
    print("3次メッシュ:" + third_mesh)
    
    print("4次メッシュ:" + forth_mesh)
    
    return forth_mesh

if __name__ == '__main__':
#129.988013,32.342565
    getmeshID(32.343503, 129.987654)
    #    getmeshID(35.7007777, 139.71475)