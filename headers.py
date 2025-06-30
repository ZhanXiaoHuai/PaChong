# headers

import re

hearders_str='''
priority:u=0, i
sec-ch-ua:"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"
sec-ch-ua-mobile:?0
sec-ch-ua-platform:"Windows"
sec-fetch-dest:document
sec-fetch-mode:navigate
sec-fetch-site:none
sec-fetch-user:?1
upgrade-insecure-requests:1
'''

pattern='^(.*?):(.*)$'

for line in hearders_str.splitlines():
    print(re.sub(pattern,'\'\\1\':\'\\2\',',line).replace(' ',''))


