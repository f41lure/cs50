{"filter":false,"title":"helpers.py","tooltip":"/similarities/helpers.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":18,"column":13},"action":"remove","lines":["def lines(a, b):","    \"\"\"Return lines in both a and b\"\"\"","","    # TODO","    return []","","","def sentences(a, b):","    \"\"\"Return sentences in both a and b\"\"\"","","    # TODO","    return []","","","def substrings(a, b, n):","    \"\"\"Return substrings of length n in both a and b\"\"\"","","    # TODO","    return []"],"id":2},{"start":{"row":0,"column":0},"end":{"row":57,"column":0},"action":"insert","lines":["from nltk.tokenize import sent_tokenize","def lines(a, b):","    \"\"\"Return lines in both a and b\"\"\"","","    # TODO","    x = a.splitlines()","    y = b.splitlines()","##    print(x)","##    print(y)","    list1 = []","    for i in range(0, len(x)):","        if x[i] in y:","            list1.append(x[i])","            continue","##    print(list1)","    return list(list1)","","def sentences(a, b):","    \"\"\"Return sentences in both a and b\"\"\"","","    # break strings into sentences lists and delete the same sentence","    a_sent = set(sent_tokenize(a))","    b_sent = set(sent_tokenize(b))","","    a_sent &= b_sent","","    return list(a_sent)","","","##for i in range(no of substrs):","##    list.append[n:n+letter size gap]","##","","def substrings(a, b, n):","    \"\"\"Return substrings of length n in both a and b\"\"\"","","    # TODO","    list_a = []","    list_b = []","","    for i in range(len(a) - n + 1):","        list_a.append(a[i:i + n])","##    print(list_a)","","    for i in range(len(b) - n + 1):","        list_b.append(b[i:i + n])","##    print(list_b)","    list_all = []","","    for i in range(0, len(list_a)):","        if list_a[i] in list_b:","            list_all.append(list_a[i])","##    print(list_all)","","    return list(list_all)","","##substrings(\"yale\", \"alakabam\", 3)",""]}]]},"ace":{"folds":[],"scrolltop":877,"scrollleft":0,"selection":{"start":{"row":57,"column":0},"end":{"row":57,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1521487865238,"hash":"34d48ae396df2c403af063010a77f5f1e74db3a0"}