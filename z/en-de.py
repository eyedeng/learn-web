
def main():
    """
    中文Unicode编码，凯撒加密，简单保护私人文件
    """
    file_name = input("File name: ")
    enc_or_dec = input("Encode or Decode File(e/d): ")
    is_enc = False
    if enc_or_dec[0] == 'e':
        is_enc = True
    key = int(input("Secret key number: "))
    zh_sta, zh_end = 0x4e00, 0x9fa5 + key
    code = ""

    with open(file_name, "r", encoding="utf-8") as f:
        for c in f.read():
            if zh_sta <= ord(c) <= zh_end:
                code += chr(ord(c) + key) if is_enc else chr(ord(c) - key)
            else:
                code += c

    pre = "en-" if is_enc else "de-"
    with open(pre + file_name, "w", encoding="utf-8") as f:
        f.write(code)


if __name__ == "__main__":
    main()
