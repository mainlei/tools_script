#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *  
import ttk

root = Tk()
root.height = 640
root.width = 960
root.title('UI资源命名工具')
root.geometry("600x200+120+100")
# 1.文件拖入窗口 2.设置输出路径，如果不设置模式为输入路径 3.设置配置表 
# 读取配置表
scene = ['sys','login','load','main','shop']
ui = ['null','Lable','Button','ProgressBar']
color = ['null','透明','white','black','red','yellow','blue']
state =['null','selected','normal','disable']
is_9scale = ['no','yes']



def createCombobox(root,list):
    name = StringVar()
    m_combobox = ttk.Combobox(root, textvariable=name,width=8)
    m_combobox['values'] = list
    # 在函数内设计无用 垃圾设计
    # m_combobox.current(0)
    m_combobox["state"] = "readonly"
    def _callback(*args):
        print(m_combobox.get()) #打印选中的值
        pass
    m_combobox.bind("<<ComboboxSelected>>",_callback)
    m_combobox.pack()
    return m_combobox
    pass

label1 = Label(root, text='场景名')
label2 = Label(root, text='UI控件名')
label3 = Label(root, text='具体功能')
label4 = Label(root, text='颜色')
label5 = Label(root, text="状态")
label6 = Label(root, text="是否是九宫格图")

tip = Label(root, text="自动生成资源名")
filename = Label(root, text="")



# 设置下拉框
sceneCombobox = createCombobox(root,scene)
sceneCombobox.current(0)

uiCombobox = createCombobox(root,ui)
uiCombobox.current(0)

editbox = Entry(root, bd =5,width=8)
editbox.pack(side = RIGHT)

colorCombobox = createCombobox(root,color)
colorCombobox.current(0)

stateCombobox = createCombobox(root,state)
stateCombobox.current(0)

is_9scaleCombobox = createCombobox(root,is_9scale)
is_9scaleCombobox.current(0)

def getStrByCombobox(combobox):
    str = combobox.get()
    if str == 'null' or str == 'no' or str == NONE:
        return NONE
        pass
    return str
    pass

def btnCallback():
    filenameStr = ''
    sceneName = getStrByCombobox(sceneCombobox)
    uiName = getStrByCombobox(uiCombobox)
    customName = getStrByCombobox(editbox)
    colorName = getStrByCombobox(colorCombobox)
    stateName = getStrByCombobox(stateCombobox)
    is_9scaleName = getStrByCombobox(is_9scaleCombobox)
    if sceneName :
        filenameStr = filenameStr+sceneName
        pass
    if uiName :
        filenameStr = filenameStr+'_'+uiName
        pass
    if customName:
        filenameStr = filenameStr+customName
        pass
    if colorName :
        filenameStr = filenameStr+'_'+colorName
        pass
    if stateName :
        filenameStr = filenameStr+'_'+stateName
        pass
    if is_9scaleName :
        filenameStr = filenameStr+'_'+is_9scaleName
        pass
    filename['text'] = filenameStr
    pass

# 按钮
btn = Button(root,text="生成文件名",command=btnCallback)
btn.pack()
btn.grid(row=2,column=0)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
label4.grid(row=0, column=3)
label5.grid(row=0, column=4)
label6.grid(row=0, column=5)
tip.grid(row=2,column=1)
filename.grid(row=3,column=1)



# 设置布局位置
sceneCombobox.grid(row=1, column=0)
uiCombobox.grid(row=1, column=1)
editbox.grid(row=1, column=2)
colorCombobox.grid(row=1, column=3)
stateCombobox.grid(row=1, column=4)
is_9scaleCombobox.grid(row=1, column=5)


root.mainloop()