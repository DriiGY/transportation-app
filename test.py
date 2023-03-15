# from email_validator import validate_email, EmailNotValidError

# def check_email(em):
#     try:
        
#         if validate_email(em):
#             return True
#     except:
#         return False

# print(check_email("ola@hotmail.com"))
# print(check_email("ola@hotmailcom"))



# assign list
l = [1, 2.0, 'have', 'a', 'geeky', 'day']
# assign string
s = 'geeky'
nl=list(map(str,l))
print(nl)
x=" ".join(nl)
print(x)
# check if string is present in the list
if x.find(s)!=-1:
    print(f'{s} is present in the list')
else:
    print(f'{s} is not present in the list')
