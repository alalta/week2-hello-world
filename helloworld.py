# Anadia Lalta
language = 'english'
Spanish = 'Hola a todos'
Italian = 'Ciao a tutti'
Portuguese = 'Ola a todos'

print('Hello everyone!')
print(' Choose a language and I will greet you in that language!')  #ask for the language they want me to greet them in 
print(str(1)+ '.Spanish')   
print(str(2)+ '.Italian')    
print(str(3) + '.Portuguese')
language= input()
if language == str(1) :      #translates "Hello everyone" to Spanish
    print('Hola a todos')
elif language == str(2) :         #translates "Hello everyone" to Italian
    print('Ciao a tutti')
elif language == str(3) :       #translates "Hello everyone to Portuguese
     print('Ola a todos')
