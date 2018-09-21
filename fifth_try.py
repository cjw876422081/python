#写程序将温度从华氏温度转换为摄氏温度。转换公式为C=5/9*(F-32)
def PtoC( degree ):
    return float((degree - 32 ) * 5 / 9)
print( PtoC(eval(input())))
#另一种写法
# def PtoC2( degree ):
#     return (degree - 32 ) * 5 / 9
# print( PtoC2(100))

