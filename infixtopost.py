def priority1(c):
  if c=='^':
    return 1
  elif c=='+' or c=='-':
    return 2
  elif c=='*' or c=='/':
    return 3
  else:
    return 0
#infix=[]
postfix=''
stackarr=[]
print("Enter infix expression")
infix=input()
print("infix expression is",infix)
for i in infix:
  if i.isalnum():
    postfix+=i
    print("post fix expression is",postfix)
  elif i=='(':
      stackarr.append(i)
  elif i==')':
      while stackarr and stackarr[-1]!='(':
        postfix+=stackarr.pop()
      stackarr.pop()

  else:
      while stackarr and stackarr[-1]!='(' and priority1(i)<=priority1(stackarr[-1]):
        postfix+=stackarr.pop()
      stackarr.append(i)
while stackarr:
  postfix+=stackarr.pop()

print("postfix expression is",postfix)
