# Everything will be same except for the last cell in the colab notebook

# Continue predicting until a full-stop appears to mark a meaningful end of the sentence

t = input("Enter the text: ")
t_, j = custom(n-1, v, t, r)

if j==1:
  print("The complete output is:\n")
  print(t, end='')
  
  while True:
    pred = model.predict(t_)
    y = list(v.keys())
    z = list(v.values())
    m = list(pred[0]).index(max(pred[0]))
    val = y[z.index(m)]
    print(val, end='')
    if val=='.':
      break
    t_[0].pop(0)
    t_[0].append(m)
    

# Continue predicting to give multiple words (only for next char predictor)

t = input("Enter the text: ")
t_, j = custom(n-1, v, t, r)

if j==1:
  x = int(input("Enter the number of complete words to be predicted: "))
  c = 1
  print("The complete output is:\n")
  print(t, end='')
  
  while True:
    pred = model.predict(t_)
    y = list(v.keys())
    z = list(v.values())
    m = list(pred[0]).index(max(pred[0]))
    val = y[z.index(m)]
    
    if val==' ':
      if c==x:
        break
      c = c+1
    print(val, end='')
    t_[0].pop(0)
    t_[0].append(m)
