class Cipher:
    """
        Cipher class is for the encipherment of data flow.
        One octet is in the range 0 ~ 255 (2 ^ 8).
        To do encryption, it just maps one byte to another one.
        Example:
            encodePassword
            | index | 0x00 | 0x01 | 0x02 | 0x03 | ... | 0xff | || 0x02ff0a04
            | ----- | ---- | ---- | ---- | ---- | --- | ---- | ||
            | value | 0x01 | 0x02 | 0x03 | 0x04 | ... | 0x00 | \/ 0x03000b05
            decodePassword
            | index | 0x00 | 0x01 | 0x02 | 0x03 | 0x04 | ... | || 0x03000b05
            | ----- | ---- | ---- | ---- | ---- | ---- | --- | ||
            | value | 0xff | 0x00 | 0x01 | 0x02 | 0x03 | ... | \/ 0x02ff0a04
        It just shifts one step to make a simply encryption, encode and decode.
    """

    def __init__(self, encodePassword: bytearray,
                 decodePassword: bytearray) -> None:
        self.encodePassword = encodePassword.copy()
        self.decodePassword = decodePassword.copy()

    def info(self):
        return self.encodePassword, self.decodePassword

    def encode(self, bs: bytearray):
        for i, v in enumerate(bs):
            bs[i] = self.encodePassword[v]

    def info_encode(self, bs: bytearray):
        for i, v in enumerate(bs):
            bs[i] = self.encodePassword[v]
        return bs

    def decode(self, bs: bytearray):
        for i, v in enumerate(bs):
            bs[i] = self.decodePassword[v]

    def info_decode(self, bs: bytearray):
        for i, v in enumerate(bs):
            bs[i] = self.encodePassword[v]
        return bs

    # @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
    # @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
    # @staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
    # @classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。

    @classmethod
    def NewCipher(cls, encodePassword: bytearray):
        decodePassword = encodePassword.copy()
        for i, v in enumerate(encodePassword):
            decodePassword[v] = i
        return cls(encodePassword, decodePassword)
