#程序文件Pz1_9.py
a=["张三", "男", 23, "江苏", "硕士", "已婚", ["身高172", "体重70"]]
print(a[0])      #显示第一个元素：张三
print(a[-1])     #显示最后一个元素：['身高172', '体重70']
print(a[-1][1])  #显示最后一个元素中的第二个元素：体重70
print(a[-3:])    #显示后三个元素
print(a[:3])     #显示前三个元素
print(a[::2])    #显示奇数位置的元素
print(a[0:-1])   #显示第一个元素到倒数第二个元素
