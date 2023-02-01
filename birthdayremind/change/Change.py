from tkinter.constants import ALL, END
import numpy as np
import tkinter as tk
import tkinter.messagebox
from hashlib import md5


def Load(file):  # Load
    data = np.load(file, allow_pickle=True).item()
    return data


def Save(data, file):  # Save
    dictionary = data
    np.save(file, dictionary)


# print(Load("data.npy"))


Data = Load("../datas/data.npy")

window = tk.Tk()  # init
window.title('My Window')  # window name

window.geometry('600x350')  # window dize 这里的乘是小x

l = tk.Label(window, text='编辑/添加', bg='green', font=('Arial', 12), width=30, height=2)
# l.pack()

imp = tk.Frame(window)  # 输入框主容器
imp.pack()
on = tk.Frame(imp)
un = tk.Frame(imp)
on.pack(side='left')
un.pack(side='right')

tk.Label(on, text='月份/month', font=('Arial', 12), width=30, height=2).pack()
month_i = tk.Entry(on, show=None, font=('Arial', 14))
month_i.pack()
tk.Label(un, text='日期/day', font=('Arial', 12), width=30, height=2).pack()
day_i = tk.Entry(un, show=None, font=('Arial', 14))
day_i.pack()

CH = tk.Frame(window)  # 更改框主容器
CH.pack()
co = tk.Frame()
cu = tk.Frame(CH)
co.pack(side='top')
cu.pack(side='bottom')

tk.Label(window, text='数据/data', font=('Arial', 12), width=30, height=2).place(x=50, y=120, width=200, heigh=50,
                                                                               anchor='w')
turn = tk.Entry(window, show=None, font=('Arial', 14))
turn.place(x=50, y=170, width=270, heigh=60, anchor='w')


def getEntry(code):
    string = str(code.get())  # 获取Entry的内容
    # print(string)
    return string


month = 0
day = 0


def Hash(data):
    re = md5(data.encode())
    return re.digest()


def getToday():
    month = getEntry(month_i)
    day = getEntry(day_i)
    print(month, day)
    if month and day:
        old_data = Data[int(month)][int(day)]
        turn.delete(0, 'end')
        turn.insert("insert", old_data)
        # sig = Hash(old_data)
    else:
        if month:
            if month is not int:
                tk.messagebox.showwarning(title='Error', message='必须输入整数')
                # print('请输入整数')
            tk.messagebox.showwarning(title='Error', message='请输入天数')
            # print("请输入day")
        elif day:
            tk.messagebox.showwarning(title='Error', message='请输入月份')
            # print("请输入month")
            if day is not int:
                tk.messagebox.showwarning(title='Error', message='必须输入整数')
                # print('请输入整数')
        else:
            tk.messagebox.showwarning(title='Error', message='请输入数据')
            # print('请输入month and day')


button = tk.Button(window, text='查找', font=('微软雅黑', 12), command=getToday)
button.pack()

list1 = []


def showAll():
    output = open('../datas/all.txt', 'w')
    for i in Data:
        m = Data[i]
        for j in m:
            h = m[j]
            if h and h[0]:
                output.write(str(h) + "\t" + str(i) + "\t" + str(j) + "\n")

    output.close()
    import os
    os.system("../datas/all.txt")


button = tk.Button(window, text='全部/ALL', font=('微软雅黑', 12), command=showAll)
button.pack(side='bottom')


def Add():
    string = turn.get()
    tname = string.split(',')
    month = getEntry(month_i)
    day = getEntry(day_i)
    # print('name=',tname,'type=',type(tname))
    try:
        Data[int(month)][int(day)] = tname
        tk.messagebox.showinfo(title='OK', message='添加成功')
        Save(Data, "../datas/data.npy")
    except BaseException:
        tk.messagebox.showerror(title='Error', message='添加失败')


button1 = tk.Button(window, text='添加/Add', font=('微软雅黑', 12), command=Add)
button1.place(x=380, y=150)

# 测试：
# def Show():
#    string = turn.get('1.0','end')
#    print('name=',string)
#    print('type=',type(string))
#    tname = string.split(',')
#    return string


# button_text = tk.Button(window,text='测试',font=('微软雅黑', 12),command=Show)
# button_text.pack()


window.mainloop()

# Data = Load("data.npy")

# for key in dat:
#	lis = dat[key]
#	month = lis[0]
#	day = lis[1]
#	Data[month][day].append(key)

# Save(Data,"data.npy")
