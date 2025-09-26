# 提示用户输入年份
year_input = input("请输入一个年份：")

try:
    # 将输入转换为整数
    year = int(year_input)
    # 判断闰年的条件
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")
except ValueError:
    # 处理输入不是数字的情况
    print("请输入有效的数字年份！")
