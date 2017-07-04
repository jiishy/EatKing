#from django.shortcuts import render
#from .models import *
#Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import re, math

gdict = { "" : "不限", "g110" : "火锅", "g132" : "咖啡厅", "g508" : "烧烤", "g117" : "面包甜点",
         "g113" : "日本菜", "g112" : "小吃快餐", "g111" : "自助餐", "g116" : "西餐", "g311" : "北京菜", "g114" : "韩国料理", "g101" : "江浙菜", "g103" : "粤菜", "g102" : "川菜", "g104" : "湘菜", "g108" : "清真菜", "g109" : "素菜", "g3243" : "新疆菜", "g26481" : "西北菜", "g115" : "东南亚菜", "g1783" : "家常菜", "g248" : "云南菜", "g105" : "贵州菜", "g26483" : "鲁菜", "g246" : "湖北菜", "g106" : "东北菜", "g1845" : "俄罗斯菜", "g118" : "其他", "g251" : "海鲜", "g219" : "小龙虾", "g1817" : "粉面馆", "g1338" : "私房菜", "g250" : "创意菜", "g26482" : "徽菜", "g107" : "台湾菜" }

rdict1 = {"r2580" : "三里屯", "r1471" : "望京", "r2578" : "国贸", "r1466" : "朝外大街", "r1470" : "亚运村","r1469" : "亮马桥/三元桥", "r2078" : "大望路", "r1489" : "五道口", "r1488" : "中关村", "r2579" : "双井","r2871" : "十里堡", "r1475" : "王府井/东单", "r1467" : "朝阳公园/团结湖", "r1481" : "西单", "r1465" : "建外大街", "r2583" : "酒仙桥"}

rdict2 = {"r14" : "朝阳区", "r17" : "海淀区", "r15" : "东城区", "r16" : "西城区", "r20" : "丰台区","r5952" : "大兴区", "r5950" : "昌平区", "r5951" : "通州区", "r328" : "石景山区", "r9158" : "顺义区","r27615" : "怀柔区", "r9157" : "房山区", "r27614" : "门头沟区", "r27616" : "平谷区", "c434" : "密云区","c435" : "延庆区" }

rdict3 = {"r2179" : "1号线", "r2180" : "2号线", "r3057" : "4号线", "r2181" : "5号线", "r8095" : "6号线","r66748" : "7号线", "r7643" : "8号线", "r7644" : "9号线", "r2507" : "10号线", "r2182" : "13号线","r8687" : "14号线", "r6962" : "15号线", "r6961" : "昌平线", "r6964" : "大兴线", "r6965" : "亦庄线","r6963" : "房山线", "r8195" : "八通线", "r8196" : "机场线" }

sdict = { "" : "默认", "s1" : "口味", "s2" : "环境", "s3" : "服务", "s4" : "人均", "s5" : "评论", "s6" : "星级" }

# Create your views here.
def index(request):
	#posts = Post.objects.order_by('-created_at')
	return render(request, 'index.html')#, {'posts': posts})

def search(request):
    if request.method == 'POST':
        content = request.POST.get('search')
    else:
        content = ''
    return redirect('search_submit', '', '', '', '', content)

def search_submit(request, g, r, p, s, content):
    if g:
        g_pattern = g + '#'
    else:
        g_pattern = '.*'
    if r:
        r_pattern = r + '#'
    else:
        r_pattern = '.*'
    if content == '':
        datas = Shop.objects.filter(area_id__regex = r_pattern).filter(type_id__regex = g_pattern)[:750]
    else:
        str = u'[\w\W]*' + content + u'[\w\W]*'
        datas = Shop.objects.filter(area_id__regex = r_pattern).filter(type_id__regex = g_pattern).filter(name__regex = str)[:750]

    if s == 's11':
        datas = sorted(datas, reverse=True, key=lambda data: data.taste_score)
    elif s == 's12':
        datas = sorted(datas, key=lambda data: data.taste_score)
    elif s == 's21':
        datas = sorted(datas, reverse=True, key=lambda data: data.env_score)
    elif s == 's22':
        datas = sorted(datas, key=lambda data: data.env_score)
    elif s == 's31':
        datas = sorted(datas, reverse=True, key=lambda data: data.serv_score)
    elif s == 's32':
        datas = sorted(datas, key=lambda data: data.serv_score)
    elif s == 's41':
        datas = sorted(datas, reverse=True, key=lambda data: data.price)
    elif s == 's42':
        datas = sorted(datas, key=lambda data: data.price)
    elif s == 's51':
        datas = sorted(datas, reverse=True, key=lambda data: data.comment_num)
    elif s == 's52':
        datas = sorted(datas, key=lambda data: data.comment_num)
    elif s == 's61':
        datas = sorted(datas, reverse=True, key=lambda data: data.rate)
    elif s == 's62':
        datas = sorted(datas, key=lambda data: data.rate)
    else:
        s = ''

    num_per_page = 15
    paginator = Paginator(datas, num_per_page)
    try:
        shops = paginator.page(p[1:])
    except PageNotAnInteger:
        shops = paginator.page(1)
    except EmptyPage:
        shops = paginator.page(paginator.num_pages)

    d = 4
    start = shops.number - d
    if start < 1:
        start = 1
    end = start + d * 2
    if end > paginator.num_pages:
        end = paginator.num_pages
        start = end - d * 2
        if start < 1:
            start = 1
    show = range(start, end + 1)
    dict = { 'content' : content, 'shops' : shops,
           'gdict' : gdict, 'rdict1' : rdict1,
           'rdict2' : rdict2, 'rdict3' : rdict3, 'sdict' : sdict,
          'g' : g, 'r' : r, 'p' : p, 's' : s, 'show' : show }

    return render(request, 'search.html', dict)

def filter(request):
    return render(request,'search.html')

def sort(request):
    return render(request,'search.html')

def enter_shop(request, shop_id, p):
    shop = Shop.objects.filter(id=shop_id)[0]
    datas = shop.Shop_Comments.all().order_by('-create_at')
    num_per_page = 15
    paginator = Paginator(datas, num_per_page)
    try:
        comments = paginator.page(p[1:])
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    d = 4
    start = comments.number - d
    if start < 1:
        start = 1
    end = start + d * 2
    if end > paginator.num_pages:
        end = paginator.num_pages
        start = end - d * 2
        if start < 1:
            start = 1
    show = range(start, end + 1)
    return render(request,'shop.html', { 'shop' : shop, 'comments' : comments, 'show' : show, 'p' : p,'comment_form':comment_form() })

@login_required
@require_POST
def comment(request, shop_id):
    content = request.POST.get('comment')
    if not content:
        return redirect("enter_shop", shop_id, '')
    else:
        comment = Comment.objects.create(content = content,user_id_id = request.user.id, shop_id_id = shop_id ,taste_score = 5, env_score = 5, serv_score = 5, like_num = 0, create_at = timezone.now())
        comment.save
        comments = Comment.objects.filter(content=content)
        return redirect("enter_shop", shop_id, '')

def comment_submit(request, shop_id):
    form = comment_form(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user_id_id = request.user.id
        comment.shop_id_id = shop_id
        comment.save()
        messages.info(request, '评论成功')
    else:
        messages.warning(request, ' 评论失败')

    return redirect('enter_shop', shop_id, '')

def like_comment(request):
    return render(request,'shop.html')

def unlike_comment(request):
    return render(request,'shop.html')

def like_shop(request):
    return render(request,'shop.html')

def unlike_shop(request):
    return render(request,'shop.html')

def new_shop(request):
    return render(request, 'new_shop.html',
                  { 'new_shop_form' : New_shopForm() })

def new_shop_submit(request):
    form = New_shopForm(request.POST)
    if form.is_valid():
        new_shop = form.save(commit=False)
        new_shop.save()
        messages.info(request, ' 申请添加店铺成功')
    else:
        messages.warning(request, ' 申请添加店铺失败')

    return redirect('new_shop')

def accuse_shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'accuse.html', { 'shop' : shop, 'accuse_shop_form' : Accuse_shopForm() })

def accuse_shop_submit(request, shop_id):
    form = Accuse_shopForm(request.POST)
    if form.is_valid():
        accuse_shop = form.save(commit=False)
        accuse_shop.accuser_id = shop_id
        accuse_shop.defendant_id = request.user.id
        accuse_shop.save()
        messages.info(request, ' 举报店铺成功')
    else:
        messages.warning(request, ' 举报店铺失败')
    
    return redirect('accuse_shop', shop_id)