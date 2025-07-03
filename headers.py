# headers

import re

hearders_str='''
        __VIEWSTATE:/ wEPDwUKLTU5OTg0MDIwNw8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBZGQGi0FCmPHMP + KelvQVsoBoqE2Axg ==
        __VIEWSTATEGENERATOR:C93BE1AE
        from
        email:402755838@qq.com
        pwd:zhang2925385
        code:DCZF
        denglu:登录
'''

pattern='^(.*?):(.*)$'

for line in hearders_str.splitlines():
    print(re.sub(pattern,'\'\\1\':\'\\2\',',line).replace(' ',''))


