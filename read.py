data = []
count = 0#每讀1000筆印一次
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:#每讀1000筆印出來
			print(len(data))
print(len(data))
#print(data)
print(data[0])
print('---------')
print(data[1])