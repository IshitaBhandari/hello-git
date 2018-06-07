Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = [100,'Ishita',True,'Urvee',500,['Aakshi','Nemo']]
>>> x.append(['google','apple','facebook','microsoft','tesla'])
>>> x
[100, 'Ishita', True, 'Urvee', 500, ['Aakshi', 'Nemo'], ['google', 'apple', 'facebook', 'microsoft', 'tesla']]
>>> x.count('Ishita')
1
>>> x.count(100)
1
>>> nums=[8,4,10,3,8,2,7]
>>> nums.sort()
>>> nums
[2, 3, 4, 7, 8, 8, 10]
>>> A = [9,5,12,66,8]
>>> B = [10,0,3,7]
>>> C = A + B
>>> C
[9, 5, 12, 66, 8, 10, 0, 3, 7]
>>> C.sort()
>>> C
[0, 3, 5, 7, 8, 9, 10, 12, 66]
>>> stack = ['Ishita','Urvee','Aakshi','Medhavini']
>>> stack.append('Himadri')
>>> stack
['Ishita', 'Urvee', 'Aakshi', 'Medhavini', 'Himadri']
>>> stack.append('jack')
>>> stack
['Ishita', 'Urvee', 'Aakshi', 'Medhavini', 'Himadri', 'jack']
>>> stack.pop()
'jack'
>>> stack.pop()
'Himadri'
>>> 
KeyboardInterrupt
>>> temp = len(C)
>>> even = 0
>>> odd = 0
>>> while temp == 0:
	if C[temp]%2 == 0:
		even=even+1
		temp = temp-1
	else:
		odd = odd+1
		temp=temp-1
	print('even->%d  odd->%d',even ,odd)

	
>>> 
