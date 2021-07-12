# coding=gbk
import tabula
import pandas as pd
import re
import os


def dealPDF(path, filename):
    dfs = tabula.read_pdf(path + "\\" + filename, pages='all')

    print("begin to write: " + filename)

    f = open(path + "\\" + filename[:-4] + ".txt", "w")

    i = -1
    for df in dfs:
        i = i+1
        if df.shape[1] <= 3 or df.shape[0] <= 2:
            continue

        if "中文简称" not in df.columns:
            df.columns = df.iloc[0]
            df = df.drop(index=0).drop(index=1)
            if "中文简称" not in df.columns:
                print("index: " + str(i))
                continue
        col_Cname = df["中文简称"]
        col_pinyin = df.iloc[:, df.columns.get_loc("中文简称") - 2]

        for word, prefix in zip(col_Cname, col_pinyin):
            if isinstance(word, str) and not "中文简称" in word:
                word = re.sub(r"\s", '', word)
                if isinstance(prefix, str):
                    # print(prefix)
                    f.write(", " + word)
                else:
                    f.write(word)

    f.close()

path = "F:\资料\教育行标"
files = os.listdir(path)
for file in files:
    if not os.path.isdir(file):  # if file is not a director
        if not file.endswith('pdf'):
            pass
        else:
            dealPDF(path, file)

# dealPDF(r"F:\资料\教育行标", "教育管理信息 中职学校管理信息.pdf")

