def string():
    all_char={} #for stroting the all characters count 
    name=str(raw_input('enter the string'))
    spec_char=str(raw_input('enter the specific character:'))
    print 'length of the string',len(name)
    print '-------------------------'
    print 'count of all letters is'
    for i in name:
        all_char[i]=name.count(i)
    print all_char
    print '-------------------------'
    if (len(spec_char)==1):
        print 'count of ',spec_char,' in string is:',name.count(spec_char)
    else:
        print 'enter only one letter'
    