"""
Title : HTML 파싱
Link : https://www.acmicpc.net/problem/22859
"""

html = input().strip()

ans = []
# p태그가 시작되었는지
is_p = False
# 아무 태그 안인지
is_tag = False
# 태그 안
tag = ''
# p태그 사이
paragraph = ''
for s in html:
    if s == '<':
        is_tag = True
    elif s == '>':
        is_tag = False
        if tag == 'p':
            is_p = True
        # p태그 닫힐 때
        elif tag == '/p':
            is_p = False
            tmp = ''
            for p in paragraph:
                if p == ' ':
                    if not tmp or tmp[-1] == ' ':
                        continue
                tmp += p
            tmp = tmp.strip()
            ans.append(tmp)
            paragraph = ''
        # 제목
        elif tag.count('"') == 2:
            title = tag.split('"')
            ans.append('title : ' + title[1])
        tag = ''
    # 태그 내부일때
    elif is_tag:
        tag += s
    # p태그 사이 일 때
    elif not is_tag and is_p:
        paragraph += s

# 출력
print(*ans, sep='\n')


'''
# WA
# div, p태그로 split
html = input().strip().split('<div')
lines = []
for h in html:
    lines.extend(h.split('<p>'))

ans = []
for line in lines[1:]:
    # div 속성으로 반드시 title이 존재
    if 'title="' in line:
        title = line.split('"')
        # ans.append('title : ' + title[1])
        print('title : ' + title[1])
    else:
        tmp = ' '
        # 태그 내부인지 아닌지
        is_in_tag = False
        for s in line:
            if s == '<':
                is_in_tag = True
            elif s == '>':
                is_in_tag = False
            elif not is_in_tag:
                # 연속된 공백 없도록
                if s == ' ' and tmp[-1] == ' ':
                    continue
                tmp += s
        # 앞/뒤 공백 없게
        tmp = tmp.strip()
        if tmp:
            print(tmp)
'''

'''
# index error
html = input().strip()
ans = []

div = False
tag = False
tmp = ' '
for i in range(len(html) - 7):
    s = html[i]
    if s == '<':
        tag = True
        # div 태그인지 확인
        if html[i + 1:i + 4] == 'div':
            div = True
        # 닫는 p태그인지 확인
        elif html[i + 1:i + 3] == '/p':
            ans.append(tmp.strip())
            tmp = ' '
    elif s == '>':
        tag = False
        # 태그가 끝날 때 div였으면 title로 추가
        if div:
            title = tmp.split('"')
            ans.append('title : ' + title[1])
            tmp = ' '
            div = False
    # div이면 내용 추가
    elif div:
        tmp += s
    # div가 아니고 다른 tag속이 아닐 때
    elif not div and not tag:
        # 빈칸이 연속되거나, 가장 앞, 뒤가 아니게
        if s == ' ' or tmp[-1] == ' ':
            continue
        tmp += s

print(*ans, sep='\n')
'''


'''
html = input().strip().split('<div')

lines = []
for i in range(1, len(html)):
    lines.append(html[i].split('<p>'))

ans = []
for div in lines:
    if 'title="'in div[0]:
        title = div[0].split('"')
        ans.append('title : ' + title[1])
        st = 1
    else:
        st = 0
    
    for i in range(st, len(div)):
        paragraph = div[i]
        tmp = ''
        tag = False
        for s in paragraph:
            if s == '<':
                tag = True
            elif s == '>':
                tag = False
            elif tag:
                continue
            else:
                if s == ' ':
                    if len(tmp) == 0 or tmp[-1] == ' ':
                        continue
                tmp += s
        if tmp:
            ans.append(tmp)

print(*ans, sep='\n')
'''

'''
# index error?
html = input().strip().split('<div')
ans = []

for context in html[1:]:
    if not context:
        continue
    tmp = context.split('<p>')
    # 제목은 따로 추가
    title = tmp[0].split('"')
    ans.append('title : ' + title[1])
    if len(context) == 1:
        continue
    # 각 줄 추가
    for paragraph in tmp[1:]:
        para = ''
        tag = False
        for i in range(len(paragraph)):
            if paragraph[i] == '>':
                tag = False
            elif paragraph[i] == '<' or tag:
                tag = True
                continue
            else:
                c = paragraph[i]
                if c == ' ':
                    if not para or para[-1] == ' ':
                        continue
                para += c
        para.strip()
        if para:
            ans.append(para)

print(*ans, sep='\n')
'''

'''
# index error
html = list(input().strip().split('<'))

ans = []
for i in range(2, len(html) - 1):
    tmp = html[i].split('>')
    # div라면 title로 추가
    if len(tmp[0]) > 3 and tmp[0][:3] == 'div':
        title = tmp[0].split('"')
        ans.append('title : ' + title[1])
    elif tmp[1] == ' ' * len(tmp[1]):
        continue
    elif tmp[0] == 'p':
        ans.append(tmp[1].strip())
    else:
        ans[-1] += ' ' + tmp[1].strip()

print(*ans, sep='\n')
'''

'''
<main><div title="title"></div></main>
<main><div title="title"></div><p>para</p></main>
<main><p>para1</p><div title="tit  le"><p>para2</p></div><p>  pa<i>dod  odo </i> ra3</p></main>

<main><div title="title"></div><p>  p  p  </p></main>

'''