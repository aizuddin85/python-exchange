ITEM_FIELDS = {
    'item_id': ('ItemId', string_type),
    'changekey': ('ChangeKey', string_type),
    'mime_content': ('MimeContent', MimeContent),
    'sensitivity': ('Sensitivity', Choice),
    'importance': ('Importance', Choice),
    'is_draft': ('IsDraft', bool),
    'subject': ('Subject', string_type),
    'headers': ('InternetMessageHeaders', [MessageHeader]),
    'body': ('Body', Body),  # Or HTMLBody, which is a subclass of Body
    'attachments': ('Attachments', [Attachment]),  # ItemAttachment or FileAttachment
    'reminder_is_set': ('ReminderIsSet', bool),
    'categories': ('Categories', [string_type]),
    'extern_id': (ExternId, ExternId),
    'datetime_created': ('DateTimeCreated', EWSDateTime),
    'datetime_sent': ('DateTimeSent', EWSDateTime),
    'datetime_received': ('DateTimeReceived', EWSDateTime),
    'last_modified_name': ('LastModifiedName', string_type),
    'last_modified_time': ('LastModifiedTime', EWSDateTime),
}
