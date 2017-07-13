# 

for item in account.inbox.filter(subject='Test', is_read=True):
    print item.subject
    print item.body
