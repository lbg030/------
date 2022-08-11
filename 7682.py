def check(lst):
	xflag,oflag = False, False
	
	for i in range(3):
		if lst[(i*3)+0] == lst[(i*3)+1] == lst[(i*3)+2]:
			if lst[(i*3)+0] == 'X':
				xflag = True
			elif lst[(i*3)+0] == 'O':
				oflag = True
	
	for i in range(3):
		if lst[i] == lst[i +3] == lst[i + 6]:
			if lst[i] == 'X':
				xflag = True
			elif lst[i] == 'O':
				oflag = True

	if lst[0] == lst[4] == lst[8]:
		if lst[0] == 'X':
			xflag = True
		elif lst[0] == 'O':
			oflag = True
	if lst[2] == lst[4] == lst[6]:
		if lst[2] == 'X':
			xflag = True
		elif lst[2] == 'O':
			oflag = True
	
	return xflag,oflag

while True:
	lst = list(input())
	xcnt = lst.count('X')
	ocnt = lst.count('O')
	
	result = False
	fullflag = (True if lst.count(".") == 0 else False)
	if len(lst) == 3:
		break
	
	else:
		xflag, oflag = check(lst)
		
		# 어떠한 경우에도 둘다 트루면 결과는 거짓
		if xflag == True and oflag == True:
			result = False
   
		#.이 없는 경우
		elif fullflag:
			if xcnt - ocnt == 1:
				if oflag == False:
					result = True

		#.이 존재
		else:
			if (xflag == True) and (xcnt - ocnt == 1):
				result = True

			elif (oflag == True) and (xcnt - ocnt == 0):
				result = True
	
	
	if result:
		print("valid")
	
	else:
		print('invalid')