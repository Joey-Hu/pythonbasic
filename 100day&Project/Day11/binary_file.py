# @author: huhao
# @file: binary_file.py
# @time: 2019/7/18 15:23
# @Document：https://www.python.org/doc/
# @desc:


def main():
    try:
        with open("lena.jpg", "rb") as img:     # rb, wb 以二进制格式操作文件
            data = img.read()
            print(type(data))
        with open("lena_w.jpg", "wb") as img2:
            img2.write(data)
    except FileNotFoundError:
        print(" 文件无法打开！")
    except IOError:
        print("文件读写错误")
    print("DONE!")


if __name__ == '__main__':
    main()