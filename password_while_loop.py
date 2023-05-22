#Password
password = "a123456"
z = 3
while True:
    pwd = input("請輸入密碼")
    if pwd == password:
    	print("登入成功!")
    	break
    else:
    	z = z - 1
    	print("密碼錯誤!還有",z,"次機會")
    	if z == 0:
    		print("連續輸入三次錯誤密碼，密碼已上鎖，請通知後台人員解鎖")
    		break
