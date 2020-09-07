def get_input_num():
    input_str = input("请输入想发布章节数目(阿拉伯数字)：")
    try:
        return int(input_str)
    except ValueError:
        print("输入有误，请输入阿拉伯数字")
        return get_input_num()