#!/usr/bin/python

import ConfigParser
from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, NTLM, Configuration

CONF_FILE = '/etc/automata.conf'
conflist = {}

try:
    Config = ConfigParser.ConfigParser()
    Config.read(CONF_FILE)
except IOError as e:
    print "Unable to open config file {}.".format(CONF_FILE)
    raise e
options = Config.options('email')
for option in options:
    try:
        conflist[option] = Config.get('email', option)
        if conflist[option] == -1:
            print('Skip: {}'.format(option))
    except AttributeError:
        print('Exception occured on {}'.format(option))
        conflist = None
        raise AttributeError

user = conflist['user']
secret = conflist['secret']
mailaddress = conflist['mailaddress']
exchange = conflist['exchange']

credentials = Credentials(
    username=user,
    password=secret
)

config = Configuration(server=exchange, credentials=credentials, verify_ssl=False)
account = Account(
    primary_smtp_address=mailaddress,
    config=config,
    autodiscover=False,
    access_type=DELEGATE
)

for item in account.inbox.filter(is_read=True):
    print item.subject
    print item.body
