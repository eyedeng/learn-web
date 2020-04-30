import sys


def main(argv):
    """
    中文Unicode编码，凯撒加密，简单保护私人文件
    """
    if len(argv) > 0:
        file_name, key, is_enc = argv[0], int(argv[1]), True
        if len(argv) == 3 and argv[2][0] == 'd':
            is_enc = False
    else:
        file_name = input("File name: ")
        key = int(input("Secret key number: "))
        enc_or_dec = input("Encode or Decode File(e/d): ")
        is_enc = False
        if enc_or_dec[0] == 'e':
            is_enc = True
    zh_sta, zh_end = 0x4e00, 0x9fa5 + key
    code = ""

    no_code_part = False  # 非加密部分 标志
    no_code_s, no_code_e = 8594, 8592

    with open(file_name, "r", encoding="utf-8") as f:
        for c in f.read():
            if not no_code_part and zh_sta <= ord(c) <= zh_end:
                code += chr(ord(c) + key) if is_enc else chr(ord(c) - key)
            elif ord(c) == no_code_s or ord(c) == no_code_e:
                no_code_part = True if ord(c) == no_code_s else False
                code += c
            else:
                code += c

    pre = "en-" if is_enc else "de-"
    with open(pre + file_name, "w", encoding="utf-8") as f:
        f.write(code)


if __name__ == "__main__":
    main(sys.argv[1:])
