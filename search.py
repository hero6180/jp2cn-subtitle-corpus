#!/usr/bin/python3
# coding:utf-8

import sys
import time

try:
  keyword = sys.argv[1]
  keyword = keyword.strip()
except Exception as e:
  print("----")
  print("使用方法：")
  print("    python3 search.py keyword")
  print("使用实例：")
  print("    python3 search.py 美女")
  print("    python3 search.py 結婚")
  print("    python3 search.py うれしい")
  print("    python3 search.py メチャメチャ")
  print("查询记录：")
  print("    python3 search.py history")
  print("----")
  sys.exit()

if keyword == "history":
  last = []
  with open("history.txt","r",encoding="utf-8") as f:
    l = 1
    while l:
      l = f.readline()
      info = l.split("\n")[0]
      if info != "":
        last.append(info)
  if len(last) <= 10:
    print("----")
    print("最近查询记录：")
    for i in range(1,len(last)+1):
      print(i,last[-i])
    print("----")
    sys.exit()
  elif len(last) > 10 :
    print("----")
    print("最近查询记录：")
    for i in range(1,11):
      print(i,last[-i])
    print("----")
    sys.exit()
elif keyword in ["","-","--","<",">","·","anki.apkg"]:
  print("----")
  print("没有查询到例句。")
  print("----")
  sys.exit()

li = []

with open("anki.apkg","r",encoding="utf-8") as f:
  l = 1
  while l:
    l = f.readline()
    info = l.split("\n")[0]
    if info != "":
      if keyword in info:
        li.append(info)

count = len(li)

with open("history.txt","a",encoding="utf-8") as f:
  f.write(keyword + "\n")

def printNext(li):
  print("----")
  comm = input("当前查询还有{}条结果未显示，是否继续查看下{}条？A(all)/Y(yes)/N(no)".format(len(li),10 if len(li) >= 10 else len(li),len(li)))
  comm = comm.strip()
  if comm in ["n","no","N","No","NO"]:
    print("----")
    sys.exit()
  elif comm in ["a","all","A","All","ALL"]:
    print("----")
    for i in range(0,len(li)):
      print(li[i])
    print("----")
  elif comm in ["y","yes","Y","Yes","YES",""]:
    if len(li) <= 10:
      print("----")
      for i in li:
        print(i)
      print("----")
    elif len(li) > 10:
      print("----")
      for i in range(0,10):
        print(li[i])
      li = li[10:]
      printNext(li)
  else:
    print("命令输入有误，请重新输入！")
    time.sleep(1)
    printNext(li)

if count == 0:
  print("----")
  print("没有查询到例句。")
  print("----")
elif count <= 10:
  print("----")
  for i in li:
    print(i)
  print("----")
elif count > 10:
  print("----")
  for i in range(0,10):
    print(li[i])
  li = li[10:]
  printNext(li)


