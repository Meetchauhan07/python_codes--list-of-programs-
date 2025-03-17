#Calculating net salary
gs=float(input("Enter the gross salary="))
allowance=gs/10
deduction=gs*(3/100)
ns=gs+allowance-deduction
print('net salary is',ns)
'''
output
Enter the gross salary=5643.59
net salary is 6038.6413

'''
#Calculating net sales
gs=float(input("Enter the gross sales="))
discount=gs/10
ns=gs-discount
print('net sales is ',ns)

'''
output=
Enter the gross sales=500
net sales is  450.0
'''
