import json
import sys
with open("./Article.json", 'r', encoding='utf-8') as f:
    fs = json.load(f)
    print(len(fs))
    i=0
    li_s = []

    for key in fs[0]:
        print(key)

    sys.exit(1)
    for company in fs:
        li = []
        if (len(company) == 19):
            for key in company:
            # print(len(company))

                if key != "title":
                    li.append(company[key])
                # i += 1
            li_s.append(li)

    with open("./data.csv",'w',encoding="utf-8-sig") as output:
        for i in range(len(li_s)):
            for j in range(len(li_s[i])):
                output.write(str(li_s[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
                output.write(',')  # 相当于Tab一下，换一个单元格
            output.write('\n')

    # print(i)