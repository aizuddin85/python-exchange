'''
Mark unread item as read.
'''

for item in account.inbox.filter(is_read=False):
    item.is_read = True
    item.save()
