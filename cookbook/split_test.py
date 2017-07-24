line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print('uname:',uname)
print('*fields:',*fields)
print('homedir:',homedir)
print('sh:',sh)