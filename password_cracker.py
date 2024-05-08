import hashlib

def crack_sha1_hash(hash, use_salts = False):
    bFound = False
    returnVal = ""

    with open('top-10000-passwords.txt', 'r') as f: 
        for pwd_line in f.readlines():
            h=hashlib.sha1()    
            
            #strip out new line characters
            pwd = pwd_line.strip()

            if (use_salts == True):
                with open('known-salts.txt', 'r') as fsalts: 
                    for salt_line in fsalts.readlines():
                         #strip out new line characters
                        salt = salt_line.strip()

                        #prepend salt to password
                        pwd_salt_prepend = salt + pwd 
                        #append salt to password
                        pwd_salt_append = pwd + salt
                        
                        hashed_salt_prepend = hashlib.sha1(pwd_salt_prepend.encode()).hexdigest()
                        hashed_salt_append = hashlib.sha1(pwd_salt_append.encode()).hexdigest()

                        if ((hash==hashed_salt_prepend) or (hash==hashed_salt_append)):
                            return pwd
            else:  
                hashed_pwd = hashlib.sha1(pwd.encode()).hexdigest()

                if (hash==hashed_pwd):
                    return pwd
        
    #return 
    return "PASSWORD NOT IN DATABASE"