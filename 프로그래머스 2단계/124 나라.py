def solution(n): #3진법     31
    answer = ''
    while n !=0:
        if n%3==0:
            answer="4"+answer
        else:
            answer=str(n%3)+answer
        if n%3==0:
            n=n//3-1
        else:
            n=n//3
    
    print(answer)
    return answer
'''
1->1
2->2
3->3
4->11
5->12
6->13
7->21
8->22
9->23
10->31
11->32
12->33
13->111
14->112
15->113
16->121
17->122
18->123
19->131
20->132
21->133
22->211
23->212
24->213
25->221
26->222
27->223
28->231
29->232
30->233
31->311
32->312
33->313
34->321
35->322
36->323
37->331
38->332
39->333
40->1111
