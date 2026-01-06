nums = []
for i in range(100):
    try:
       div = i - 50
       nums += [100 / div]
    except Exception as e:
       print(e)
       print(i, div)