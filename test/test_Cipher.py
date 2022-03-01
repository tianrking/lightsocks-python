import sys
sys.path.append("./") # 相对于使用者而言的项目路径
from lightsocks.core.cipher import Cipher

a = bytearray(1)
b = bytearray(2)
c = bytearray('c',encoding='UTF-8')
d = bytearray('d',encoding='UTF-8')
# print(a,b,c,d)

GG = Cipher(a,b)

_a,_b = GG.info()
print('bytearray:\n',_a,_b)

_encode_data = GG.info_encode(a)
print("encode:\n",_encode_data)

_decode_data = GG.info_decode(a)
print("decode:\n",_encode_data)

# @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
# @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
# @staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
# @classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。

_NewCipher_data = GG.NewCipher(a)
print(_NewCipher_data)