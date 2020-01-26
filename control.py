def openTab():
    '''Opens tab when whole hand visible'''
    import webbrowser
    import speech
    
    print('Open')
    website = speech.listen().strip().split(' ')
    url = ''
    if(('Google' in website[0] or 'google' in website[0]) and len(website)>1):
        url += 'https://www.google.com/search?q='
        for words in range(1,len(website)):
            url += website[words]
            url += ' '
    elif(len(website)>1): 
        for words in website:
            url += website
    else:
        url += 'https://www.' + website[0] + '.com'
    print('link is:',url)
    webbrowser.open_new_tab(url)

def closeTab():
    '''Closes tab when fist made'''
    import os
    
    print('Close')
    os.system('cd ~')
    os.system('killall firefox')
    os.system('cd Documents/Projects/TAMUHack')
    
    