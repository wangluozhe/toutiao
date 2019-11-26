# 前言
任何爬虫工程师在爬取网站数据之前都会对网站进行分析，并且进行==逆向(js)破解(加密)==，所以我们在爬取今日头条的文章和视频数据之前，我们也需要先分析一下今日头条的反爬虫机制以及进行==逆向(js)破解(加密)==。

# 分析今日头条
今日头条某用户的链接：==https://www.toutiao.com/c/user/3410443345/#mid=3413306633==
![今日头条某用户链接](https://img-blog.csdnimg.cn/20191101152616547.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
我们将对今日头条链接进行详细的分析，以下为==分析步骤：==
### 1.分析网站信息是否是静态数据
按==F12==弹出开发者界面，选择==Network区域==，你会发现有很多的请求链接，鼠标划到最上面，然后看到有一个跟==网站URL==一样的链接，点击进去。
![演示图](https://img-blog.csdnimg.cn/20191101153216191.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
![演示图](https://img-blog.csdnimg.cn/20191101153510110.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
从这里得出今日头条网站的数据并不是静态数据，所以我们要进行下一步分析。
### 2.分析网站信息是否为AJAX请求的
AJAX请求是网站通过js脚本发起的请求连接，目的就是为了在不刷新网页的情况下就能实时的更新网页内容，从而在感觉上你是觉得他和网页源码拼接在一起。

我们再从众多的链接中进行筛选，由于AJAX的类型是XHR的，所以在开发者模式里面我们选择XHR，就能看到只剩下几个链接了，然后从这几个链接里面找出与网站内容极其相符的链接就可以了。
![演示图](https://img-blog.csdnimg.cn/20191101154655910.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
这样分析出来了网站的内容主要靠AJAX请求的数据来显示的。
### 3.分析请求链接
我们知道这个链接后就会要去请求这个链接，从而在里面获取到自己想要的数据，这样我们就获得了数据。

我们来看一下==开发者工具==中的==Network区域==的==Headers区域==，经过两次刷新网页会发现两次请求中的参数是有变化的，以及Request Headers的参数也是有变化的，看图。
第一次请求：
![第一次请求](https://img-blog.csdnimg.cn/20191101160014877.png)
![第一次请求](https://img-blog.csdnimg.cn/20191101160035641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
第二次请求：
![第二次请求](https://img-blog.csdnimg.cn/20191101160056345.png)
![第二次请求](https://img-blog.csdnimg.cn/20191101160109613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
赖加载请求：

解释(百度百科)：在Web应用程序中，系统的瓶颈常在于系统的响应速度。如果系统响应速度过慢，用户就会出现埋怨情绪，系统的价值也因此会大打折扣。因此，提高系统响应速度，是非常重要的。
Web应用程序做的最多就是和后台数据库交互，而查询数据库是种非常耗时的过程。当数据库里记录过多时，查询优化更显得尤为重要。为了解决这种问题，有人提出了缓存的概念。缓存就是将用户频繁使用的数据放在内存中以便快速访问。在用户执行一次查询操作后，查询的记录会放在缓存中。当用户再次查询时，系统会首先从缓存中读取，如果缓存中没有，再查询数据库。缓存技术在一定程度上提升了系统性能，但是当数据量过大时，缓存就不太合适了。因为内存容量有限，把过多的数据放在内存中，会影响电脑性能。而另一种技术，懒加载可以解决这种问题。
![赖加载请求](https://img-blog.csdnimg.cn/20191101163941394.png)
![赖加载请求](https://img-blog.csdnimg.cn/20191101164001232.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
从上面图片来看，我们就能发现链接的参数和请求的headers的参数是有变化的。
变化参数的作用：
|参数|作用|加密|
|--|--|--|
|page_type|获取数据的类型为文章还是视频，==视频为0==，==文章为1==|否|
|user_id|获取那个用户的数据，在用户链接中获取user_id：https://www.toutiao.com/c/user/==3410443345==/#mid=3413306633|否|
|max_behot_time|连续获取用户的数据，用于赖加载上，第一次值默认为0，后续的值为上一次返回数据中的max_behot_time的值|否|
|count|单次返回最大的数据量，默认值为20|否|
|as|每一次请求的链接是否是最近的时间|是|
|cp|与上同理|是|
|_signature|用于判断user_id和max_behot_time的值跟链接和headers的参数的值是否相等|是|

需要注意的Request Headers中cookie的参数(解决方法：手动获取这些参数的值)：
|参数|作用|变化|加密|
|--|--|--|--|
|tt_webid|未知|根据我的观察是一天变化一次|是|
|WEATHER_CITY|标记城市|不变化|是(urlencode)|
|tt_webid|未知|同上tt_webid一样|是|
|csrftoken|用于csrf|同上|是|
这样就分析完整个网站了，下面开始实战。
# 爬取今日头条
知道这些加密参数后就开始对加密参数进行破解
### 1.破解as和cp
首先我们已经知道了每次的访问参数都在变化，所以我们要先找出这些参数的加密代码，也就是js代码。

搜索js文件中带有`as`或`cp`或`_signature`字符的文件，然后再分析代码是怎么构成的。

搜索方法：
![搜索方法](https://img-blog.csdnimg.cn/20191101170258637.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
进入后再按Ctrl+F再次搜索`_signature`，就可以看到参数的加密方法了。
![搜索](https://img-blog.csdnimg.cn/20191101170441760.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
这样就能找到这串加密代码了。
```javascript
function n() {
    var e, i = ascp.getHoney(), t = "";
    return window.TAC && (t = TAC.sign(userInfo.id + "" + d.params.max_behot_time)),
    e = _.extend({}, d.params, {
        as: i.as,
        cp: i.cp,
        _signature: t
    })
}
```
其中==i.as==和==i.cp==分别对应==as==和==cp==，而==i==是由`ascp.getHoney()`这代码返回的，所以我们继续找`ascp.getHoney`,继续搜索`getHoney`函数。
![搜索](https://img-blog.csdnimg.cn/20191101171111280.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
```javascript
i.getHoney = function() {
    var e = Math.floor((new Date).getTime() / 1e3)
      , i = e.toString(16).toUpperCase()
      , t = md5(e).toString().toUpperCase();
    if (8 != i.length)
        return {
            as: "479BB4B7254C150",
            cp: "7E0AC8874BB0985"
        };
    for (var o = t.slice(0, 5), n = t.slice(-5), a = "", s = 0; 5 > s; s++)
        a += o[s] + i[s];
    for (var r = "", l = 0; 5 > l; l++)
        r += i[l + 3] + n[l];
    return {
        as: "A1" + a + i.slice(-3),
        cp: i.slice(0, 3) + r + "E1"
    }
}
```
根据这串JS代码将他转换为Python代码就可以得出`as`和`cp`的值了，下面给出Python代码：
```python
import math,time,hashlib

def getHoney():
    e = math.floor(int(str(time.time() * 1000).split('.')[0]) / 1e3)	#获取13位毫秒数然后除于1e3再向下取整
    i = str('%X' % e)	#转换e为16进制
    m5 = hashlib.md5()
    m5.update(str(e).encode('utf-8'))
    t = str(m5.hexdigest()).upper()	#进行md5加密
    if 8 != len(i):
        return {'as':'479BB4B7254C150','cp':'7E0AC8874BB0985'}
    o = t[0:5]
    n = t[-5:]
    a = ""
    r = ""
    for x in range(5):	#交换字符串
        a += o[x] + i[x]
        r += i[x + 3] + n[x]
    return {'as':"A1" + a + i[-3:],'cp':i[0:3] + r + "E1"}

if __name__ == '__main__':
	print(getHoney())
```
![输出结果](https://img-blog.csdnimg.cn/20191101173413781.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
### 2.破解_signature
根据上面破解==as==和==cp==时候的截图，我们可以看见生成`_signature`的值是==t==，而生成t的方法是`TAC.sign(userInfo.id + "" + d.params.max_behot_time)`，所以我们要搜索`TAC.sign()`方法。
![搜索](https://img-blog.csdnimg.cn/20191101170441760.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
搜索完成之后发现是很大一串混淆加密后的方法实现的TAC，想要破解需要花很多时间去看代码，所以为了方便，我就用execjs直接执行这串代码就可以了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191101174311270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
js源代码：
```javascript
Function(function(e) {
    return 'e(e,a,r){(b[e]||(b[e]=t("x,y","x "+e+" y")(r,a)}a(e,a,r){(k[r]||(k[r]=t("x,y","new x[y]("+Array(r+1).join(",x[y]")(1)+")")(e,a)}r(e,a,r){n,t,s={},b=s.d=r?r.d+1:0;for(s["$"+b]=s,t=0;t<b;t)s[n="$"+t]=r[n];for(t=0,b=s=a;t<b;t)s[t]=a[t];c(e,0,s)}c(t,b,k){u(e){v[x]=e}f{g=,ting(bg)}l{try{y=c(t,b,k)}catch(e){h=e,y=l}}for(h,y,d,g,v=[],x=0;;)switch(g=){case 1:u(!)4:f5:u((e){a=0,r=e;{c=a<r;c&&u(e[a]),c}}(6:y=,u((y8:if(g=,lg,g=,y===c)b+=g;else if(y!==l)y9:c10:u(s(11:y=,u(+y)12:for(y=f,d=[],g=0;g<y;g)d[g]=y.charCodeAt(g)^g+y;u(String.fromCharCode.apply(null,d13:y=,h=delete [y]14:59:u((g=)?(y=x,v.slice(x-=g,y:[])61:u([])62:g=,k[0]=65599*k[0]+k[1].charCodeAt(g)>>>065:h=,y=,[y]=h66:u(e(t[b],,67:y=,d=,u((g=).x===c?r(g.y,y,k):g.apply(d,y68:u(e((g=t[b])<"<"?(b--,f):g+g,,70:u(!1)71:n72:+f73:u(parseInt(f,3675:if(){bcase 74:g=<<16>>16g76:u(k[])77:y=,u([y])78:g=,u(a(v,x-=g+1,g79:g=,u(k["$"+g])81:h=,[f]=h82:u([f])83:h=,k[]=h84:!085:void 086:u(v[x-1])88:h=,y=,h,y89:u({e{r(e.y,arguments,k)}e.y=f,e.x=c,e})90:null91:h93:h=0:;default:u((g<<16>>16)-16)}}n=this,t=n.Function,s=Object.keys||(e){a={},r=0;for(c in e)a[r]=c;a=r,a},b={},k={};r'.replace(/[-]/g, function(i) {
        return e[15 & i.charCodeAt(0)]
    })
}("v[x++]=v[--x]t.charCodeAt(b++)-32function return ))++.substrvar .length(),b+=;break;case ;break}".split("")))()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [TAC = {}]);
```
由于python没有浏览器的userAgent，所以我们得对代码进行一点改变，让他来适应我们python代码。
```javascript
function tac(userid){
    Function(function(e) {
        global.navigator={};	//声明一个浏览器得navigator
        global.navigator.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36";	//给navigator添加一个userAgent，让下面混淆能够正常读取userAgent信息，此userAgent必须和python代码中的headers里的userAgent一模一样。
        return 'e(e,a,r){(b[e]||(b[e]=t("x,y","x "+e+" y")(r,a)}a(e,a,r){(k[r]||(k[r]=t("x,y","new x[y]("+Array(r+1).join(",x[y]")(1)+")")(e,a)}r(e,a,r){n,t,s={},b=s.d=r?r.d+1:0;for(s["$"+b]=s,t=0;t<b;t)s[n="$"+t]=r[n];for(t=0,b=s=a;t<b;t)s[t]=a[t];c(e,0,s)}c(t,b,k){u(e){v[x]=e}f{g=,ting(bg)}l{try{y=c(t,b,k)}catch(e){h=e,y=l}}for(h,y,d,g,v=[],x=0;;)switch(g=){case 1:u(!)4:f5:u((e){a=0,r=e;{c=a<r;c&&u(e[a]),c}}(6:y=,u((y8:if(g=,lg,g=,y===c)b+=g;else if(y!==l)y9:c10:u(s(11:y=,u(+y)12:for(y=f,d=[],g=0;g<y;g)d[g]=y.charCodeAt(g)^g+y;u(String.fromCharCode.apply(null,d13:y=,h=delete [y]14:59:u((g=)?(y=x,v.slice(x-=g,y:[])61:u([])62:g=,k[0]=65599*k[0]+k[1].charCodeAt(g)>>>065:h=,y=,[y]=h66:u(e(t[b],,67:y=,d=,u((g=).x===c?r(g.y,y,k):g.apply(d,y68:u(e((g=t[b])<"<"?(b--,f):g+g,,70:u(!1)71:n72:+f73:u(parseInt(f,3675:if(){bcase 74:g=<<16>>16g76:u(k[])77:y=,u([y])78:g=,u(a(v,x-=g+1,g79:g=,u(k["$"+g])81:h=,[f]=h82:u([f])83:h=,k[]=h84:!085:void 086:u(v[x-1])88:h=,y=,h,y89:u({e{r(e.y,arguments,k)}e.y=f,e.x=c,e})90:null91:h93:h=0:;default:u((g<<16>>16)-16)}}n=this,t=n.Function,s=Object.keys||(e){a={},r=0;for(c in e)a[r]=c;a=r,a},b={},k={};r'.replace(/[-]/g, function(i) {
            return e[15 & i.charCodeAt(0)]
        })
    }("v[x++]=v[--x]t.charCodeAt(b++)-32function return ))++.substrvar .length(),b+=;break;case ;break}".split("")))()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [TAC = {}]);
    var signs = TAC.sign(userid);
    return signs
}
```
在执行上面这串js代码前请先更换一个`js环境`，默认`execjs`使用的是windows系统的`JScript`，这个`js环境`不适合这串代码，所以安装一个`nodejs环境`，然后重启一下`pycharm`就可以了。
把这串js代码保存为js文件，然后用python来进行执行，下面转换为python代码。
```python
import execjs

def get_signature(user_id,max_behot_time):
    with open('newsign.js') as f:
        jsData = f.read()
    execjs.get()
    ctx = execjs.compile(jsData).call('tac',str(user_id) + str(max_behot_time))  #复原TAC.sign(userInfo.id + "" + i.param.max_behot_time)
    return ctx

if __name__ == '__main__':
	user_id = 'https://www.toutiao.com/c/user/3410443345/#mid=3413306633'.split('/')[-2]	#获取user_id
	print(get_signature(user_id,0))
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191101175214195.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
这三个加密参数破解完了，那么就大功告成了。
### 3.获取数据
上面已经介绍完了所有的过程，所以这里就不多说废话了，直接上代码了。
```python
import requests,math,time,hashlib,execjs,json

#获取_signature参数
def get_signature(user_id,max_behot_time):
    with open('newsign.js') as f:
        jsData = f.read()
    execjs.get()
    ctx = execjs.compile(jsData).call('tac',str(user_id) + str(max_behot_time))  #复原TAC.sign(userInfo.id + "" + i.param.max_behot_time)
    return ctx

#获取as和cp参数
def getHoney():
    e = math.floor(int(str(time.time() * 1000).split('.')[0]) / 1e3)
    i = str('%X' % e)
    m1 = hashlib.md5()
    m1.update(str(e).encode('utf-8'))
    t = str(m1.hexdigest()).upper()
    if 8 != len(i):
        return {
            'as':'479BB4B7254C150',
            'cp':'7E0AC8874BB0985'
        }
    o = t[0:5]
    n = t[-5:]
    a = ""
    r = ""
    for x in range(5):
        a += o[x] + i[x]
        r += i[x + 3] + n[x]
    return {'as':"A1" + a + i[-3:],'cp':i[0:3] + r + "E1"}

#获取网站api的json数据
def get_json(user_id,max_behot_time,as_cp,signature,page_type):
    #page_type为0是爬取视频内容，为1是爬取文章内容
    headers = {
        'authority': 'www.toutiao.com',
        'method': 'GET',
        'path': '/c/user/article/?page_type={page_type}&user_id={user_id}&max_behot_time={max_behot_time}&count=20&as={as}&cp={cp}&_signature={signature}'.format(page_type=page_type,user_id=user_id,max_behot_time=max_behot_time,signature=signature, **as_cp),
        'scheme': 'https',
        'accept': 'application/json, text/javascript',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'tt_webid=6753859293584737805; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6753859293584737805; csrftoken=60ed6e0a8271872b7d0ab6b864bd6611; __tasessionId=eqzqwzzav1572574450156',
        'referer': 'https://www.toutiao.com/c/user/3410443345/',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    url = 'https://www.toutiao.com/c/user/article/?page_type={page_type}&user_id={user_id}&max_behot_time={max_behot_time}&count=20&as={as}&cp={cp}&_signature={signature}'.format(page_type=page_type,user_id=user_id,max_behot_time=max_behot_time,signature=signature, **as_cp)
    response = requests.get(url, headers=headers)
    resp_json = json.loads(response.text)
    return resp_json

if __name__ == '__main__':
    url = 'https://www.toutiao.com/c/user/3410443345/#mid=3413306633'  # url为用户文章和视频的源
    user_id = url.split('/')[-2]  # 获取用户user_id，等同于js中的userInfo.id
    max_behot_time = 0  # _signature参数生成需要，并且赖加载时也需要此参数
    page_type = 1   #0为文章，1为视频
    as_cp = getHoney()  #获取as和cp值
    signature = get_signature(user_id,max_behot_time) #获取_signature值
    toutiao_json = get_json(user_id,max_behot_time,as_cp,signature,page_type)   #获取今日头条文章数据
    print(json.dumps(toutiao_json,ensure_ascii=False,indent=4,sort_keys=True))
```
![演示图](https://img-blog.csdnimg.cn/20191101181706930.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
### 4.获取赖加载数据(完整版)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191101182201451.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
上图就是获取到空数据，所以为了解决这个问题加了try来进行控制。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191101183332541.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjc5MDc3,size_16,color_FFFFFF,t_70)
完整代码：
```python
import requests,math,time,hashlib,execjs,json

#获取_signature参数
def get_signature(user_id,max_behot_time):
    with open('newsign.js') as f:
        jsData = f.read()
    execjs.get()
    ctx = execjs.compile(jsData).call('tac',str(user_id) + str(max_behot_time))  #复原TAC.sign(userInfo.id + "" + i.param.max_behot_time)
    return ctx

#获取as和cp参数
def getHoney():
    e = math.floor(int(str(time.time() * 1000).split('.')[0]) / 1e3)
    i = str('%X' % e)
    m1 = hashlib.md5()
    m1.update(str(e).encode('utf-8'))
    t = str(m1.hexdigest()).upper()
    if 8 != len(i):
        return {
            'as':'479BB4B7254C150',
            'cp':'7E0AC8874BB0985'
        }
    o = t[0:5]
    n = t[-5:]
    a = ""
    r = ""
    for x in range(5):
        a += o[x] + i[x]
        r += i[x + 3] + n[x]
    return {'as':"A1" + a + i[-3:],'cp':i[0:3] + r + "E1"}

#获取网站api的json数据
def get_json(user_id,max_behot_time,as_cp,signature,page_type):
    #page_type为0是爬取视频内容，为1是爬取文章内容
    headers = {
        'authority': 'www.toutiao.com',
        'method': 'GET',
        'path': '/c/user/article/?page_type={page_type}&user_id={user_id}&max_behot_time={max_behot_time}&count=20&as={as}&cp={cp}&_signature={signature}'.format(page_type=page_type,user_id=user_id,max_behot_time=max_behot_time,signature=signature, **as_cp),
        'scheme': 'https',
        'accept': 'application/json, text/javascript',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'tt_webid=6753859293584737805; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6753859293584737805; csrftoken=60ed6e0a8271872b7d0ab6b864bd6611; __tasessionId=eqzqwzzav1572574450156',
        'referer': 'https://www.toutiao.com/c/user/3410443345/',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    url = 'https://www.toutiao.com/c/user/article/?page_type={page_type}&user_id={user_id}&max_behot_time={max_behot_time}&count=20&as={as}&cp={cp}&_signature={signature}'.format(page_type=page_type,user_id=user_id,max_behot_time=max_behot_time,signature=signature, **as_cp)
    response = requests.get(url, headers=headers)
    resp_json = json.loads(response.text)
    return resp_json

if __name__ == '__main__':
    url = 'https://www.toutiao.com/c/user/3410443345/#mid=3413306633'  # url为用户文章和视频的源
    user_id = url.split('/')[-2]  # 获取用户user_id，等同于js中的userInfo.id
    max_behot_time = 0  # _signature参数生成需要，并且赖加载时也需要此参数
    isDown = True  # 一直获取数据
    page_type = 1   #0为视频，1为文章
    while isDown:	#解决赖加载问题
        as_cp = getHoney()
        signature = get_signature(user_id, max_behot_time)
        toutiao_json = get_json(user_id, max_behot_time, as_cp, signature,page_type)
        # 由于今日头条的反爬虫机制，有时会获取到空的数据，所以需要用try来控制，一般比例是3：1所以是访问3次有一次获得数据
        if page_type:
            try:
                max_behot_time = toutiao_json['next']['max_behot_time']     #数据为空就没有这个选项从而引发try
                print('文章数据：%s' % str(toutiao_json))
                has_more = toutiao_json['has_more'] #获取是否还有下一页数据
                if not has_more:    #用来判断是否没有下一页了
                    isDown = False
                    break
            except Exception as e:
                continue
        else:
            try:
                max_behot_time = toutiao_json['next']['max_behot_time']  # 数据为空就没有这个选项从而引发try
                print('视频数据：%s' % str(toutiao_json))
                has_more = toutiao_json['has_more'] #获取是否还有下一页数据
                if not has_more:    #用来判断是否没有下一页了
                    isDown = False
                    break
            except Exception as e:
                continue
```
# 声明：本文仅供学习交流使用，请勿用于商业用途，违者后果自负。