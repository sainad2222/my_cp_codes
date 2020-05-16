s = input().strip('{').strip(",").strip('}').split(', ')
for i in s:
    if(i==''):
        s.remove(i)
sx = set(s)
count=0
for i in sx:
    count+=1
print(count)