s, i, j, c , p ,counter = list(input()), 0, 0, 0 ,[],0
for u in range(len(s)):
    if s[u] == '(':
        p.append(u)
while c < len(s) - 1:
    if s[c] == '(':
        i += 1
        counter+=1
    else: i -= 1
    if i < 0 and s[c]==')':
        s[p[counter]],s[c] ,j,i,c =s[c],s[p[counter]], j + p[counter] - c,i+1,c+1
        counter+=1
    c += 1
print(j)
