import requests
import re
import json
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
}
list1 = []
list2 = []
list3 = []
list4 = []
list_all = []
i = 1614066736711
j = 0
url = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(j)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_="+str(i)
html = requests.get(url,headers=headers).content.decode()
list1 = re.findall('"content":"(.*?)"',html,re.S)
#print(list1)
j = re.findall('"last":"(.*?)"',html,re.S)
i = i+3
url = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(j[0])+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_="+str(i)
html = requests.get(url,headers=headers).content.decode()
list2 = re.findall('"content":"(.*?)"',html,re.S)
#print(list2)
for k in range(1,1168,1):
    i += 1
    j = re.findall('"last":"(.*?)"',html,re.S)
    url = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(j[0])+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_="+str(i)
    html = requests.get(url,headers=headers).content.decode()
    list3 = re.findall('"content":"(.*?)"',html,re.S)
    list4 += list3
    #print(list4)
list_all = list1 + list2 + list4
print(list_all)
