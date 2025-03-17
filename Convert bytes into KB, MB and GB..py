# Convert bytes to KB, MB, and GB
bytes = float(input("Enter size in bytes: "))
KB = 1024          
MB = KB * 1024     
GB = MB * 1024     
kilobytes = bytes / KB
megabytes = bytes / MB
gigabytes = bytes / GB
print(bytes,'bytes is equal to:')
print(kilobytes,'KB')
print(megabytes,'MB')
print(gigabytes,'GB')
'''
output=
Enter size in bytes: 54254405397
54254405397.0 bytes is equal to:
52982817.77050781 KB
51741.032979011536 MB
50.52835251856595 GB
'''
