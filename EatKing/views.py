#from django.shortcuts import render
#from .models import *
#Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import *

gdict = {"g110" : "火锅", "g132" : "咖啡厅", "g508" : "烧烤", "g117" : "面包甜点", "g113" : "日本菜",
 "g112" : "小吃快餐", "g111" : "自助餐", "g116" : "西餐", "g311" : "北京菜", "g114" : "韩国料理",
 "g101" : "江浙菜", "g103" : "粤菜", "g102" : "川菜", "g104" : "湘菜", "g108" : "清真菜",
 "g109" : "素菜", "g3243" : "新疆菜", "g26481" : "西北菜", "g115" : "东南亚菜", "g1783" : "家常菜",
 "g248" : "云南菜", "g105" : "贵州菜", "g26483" : "鲁菜", "g246" : "湖北菜", "g106" : "东北菜",
 "g1845" : "俄罗斯菜", "g118" : "其他", "g251" : "海鲜", "g219" : "小龙虾", "g1817" : "粉面馆",
 "g1338" : "私房菜", "g250" : "创意菜", "g26482" : "徽菜", "g107" : "台湾菜" }

rdict1 = {"r2580" : "三里屯", "r1471" : "望京", "r2578" : "国贸", "r1466" : "朝外大街", "r1470" : "亚运村",
"r1469" : "亮马桥/三元桥", "r2078" : "大望路", "r1489" : "五道口", "r1488" : "中关村", "r2579" : "双井",
"r2871" : "十里堡", "r1475" : "王府井/东单", "r1467" : "朝阳公园/团结湖", "r1481" : "西单", 
"r1465" : "建外大街", "r2583" : "酒仙桥"}

rdict2 = {"r14" : "朝阳区", "r17" : "海淀区", "r15" : "东城区", "r16" : "西城区", "r20" : "丰台区",
"r5952" : "大兴区", "r5950" : "昌平区", "r5951" : "通州区", "r328" : "石景山区", "r9158" : "顺义区",
"r27615" : "怀柔区", "r9157" : "房山区", "r27614" : "门头沟区", "r27616" : "平谷区", "c434" : "密云区",
"c435" : "延庆区" }

rdict3 = {"r2179" : "1号线", "r2180" : "2号线", "r3057" : "4号线", "r2181" : "5号线", "r8095" : "6号线",
"r66748" : "7号线", "r7643" : "8号线", "r7644" : "9号线", "r2507" : "10号线", "r2182" : "13号线",
"r8687" : "14号线", "r6962" : "15号线", "r6961" : "昌平线", "r6964" : "大兴线", "r6965" : "亦庄线",
"r6963" : "房山线", "r8195" : "八通线", "r8196" : "机场线" }


# Create your views here.
def index(request):
	#posts = Post.objects.order_by('-created_at')
	return render(request, 'index.html')#, {'posts': posts})

def search(request, content=''):
    if request.method == 'POST':
        content = request.POST.get('search')
    if not content:
        content = ''
    return redirect('search_submit', content)

def search_submit(request, content):
    if content == '':
        shops = Shop.objects.filter(id__lt = 100)
    else:
        str = u'[\w\W]*' + content + u'[\w\W]*'
        shops = Shop.objects.filter(name__regex = str)[:100]
    #shops = Shop.objects.filter(image = '')[:100]
    dict = { 'content' : content, 'shops' : shops,
           'gdict' : gdict, 'rdict1' : rdict1, 'rdict2' : rdict2, 'rdict3' : rdict3 }
    return render(request, 'search.html', dict)

def filter(request):
	return render(request,'search.html')

def sort(request):
	return render(request,'search.html')

def enter_shop(request):
	return render(request,'shop.html')

def comment(request):
	return render(request,'shop.html')

def like_comment(request):
	return render(request,'shop.html')

def unlike_comment(request):
	return render(request,'shop.html')

def like_shop(request):
	return render(request,'shop.html')

def unlike_shop(request):
	return render(request,'shop.html')
