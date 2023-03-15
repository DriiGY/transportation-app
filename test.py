# from email_validator import validate_email, EmailNotValidError

# def check_email(em):
#     try:
        
#         if validate_email(em):
#             return True
#     except:
#         return False

# print(check_email("ola@hotmail.com"))
# print(check_email("ola@hotmailcom"))



quest = ['What is TransportYoiu ?', 'What are my preferences ?', 'Options available:']
matching = [ for i in range(0,len(quest)) if "available" in quest[i]]
print(matching)