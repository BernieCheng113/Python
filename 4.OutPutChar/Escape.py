EscapeStr =''

#Bell
EscapeStr='Bell:'
print(EscapeStr + "\a")

#vertical tab
txt = 'Hello\vWorld'
EscapeStr = 'vertical tab:' 
print(EscapeStr + txt)

#back
txt = 'Hello\bWorld'
EscapeStr = 'back:' 
print(EscapeStr + txt)

#Backslash
txt = 'Hello\\World'
EscapeStr = 'Backslash:' 
print(EscapeStr + txt)

#Form Feed
txt = 'Hello\fWorld'
EscapeStr = 'Form Feed:' 
print(EscapeStr + txt)

#tab
txt = 'Hello\tWorld'
EscapeStr = 'teb:' 
print(EscapeStr + txt)

#Newline
txt = 'Hello\nWorld'
EscapeStr = 'Newline:' 
print(EscapeStr + txt)

#Single Quote
txt = 'Hello\'World'
EscapeStr = 'Single Quote:' 
print(EscapeStr + txt)

#SCarriage Return
txt = 'Hello\rWorld'
EscapeStr = 'Carriage Return:' 
print(EscapeStr + txt)

#Double Quote
txt = 'Hello\"World'
EscapeStr = 'double Quote:' 
print(EscapeStr + txt)
