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