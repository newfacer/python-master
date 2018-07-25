# coding=utf-8
import sys
import urllib3
import requests
import os
import zipfile
import tushare as ts
import zipfile
import os
# url = "http://www.cninfo.com.cn/cninfo-new/data/download"

# payload = {('market', 'sz'), ('type', 'lrb'),('code','000100'),('orgid','gssz0000100'),('minYear','2004'),('maxYear','2018')}
# res = requests.post(url, files=payload)
# print (res.request.body)
# print (res.request.headers)

# print (res.status_code)
# 404 error cause error boundary

#with open("gssz0000100_2004_2018.zip", "wb") as code:
#    code.write(res)

# res = http.request(
#     'POST',
#     'http://www.cninfo.com.cn/cninfo-new/data/download',
#     headers = {'Content-Type':"multipart/form-data;%s"%boundary},
#     multipart_boundary = boundary,
#     fields={
#          'market':('None','sz','None'), 
#          'type':('None','lrb','None'),
#          'code': ('None','000100','None'),
#          'orgid':('None','gssz0000100','None') ,
#          'minYear':('None','2004','None'),
#          'maxYear':('None','2018','None')
#          })
def mkdir(path): 
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
 
    if not isExists:
        os.makedirs(path)
        print path+' 创建成功'
        return True
    else:
        print path+' 目录已存在'
        return False



rootPath = 'D:\\python\\python-finance-master\\python-master\\data'
csvPath = rootPath + '\\csv'
mkdir(rootPath)
mkdir(csvPath)

def unzipFile(path): 
    #file_list = os.listdir(r'.')
    file_list = os.listdir(path)
    for file_name in file_list:
        if os.path.splitext(file_name)[1] == '.zip':
            print file_name

            targetFile = os.path.join(path,file_name)
            file_zip = zipfile.ZipFile(targetFile, 'r')
            for file in file_zip.namelist():
                file_zip.extract(file,path+'\\csv')
            file_zip.close()  


urllib3.disable_warnings()
http = urllib3.PoolManager()

boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
dat = ts.get_stock_basics()
index = {}
index = dat.index._data
payload = {}
queryload = {}
csvType = ['fzb','llb','lrb']

for j in range(0,len(csvType)):
    for i in range(0,len(index)):
        queryload['keyWord'] = index[i]
        queryload['maxNum'] = 10
        queryload['hq_or_cw'] = 2
        queryRes = requests.post('http://www.cninfo.com.cn/cninfo-new/data/query', data=queryload)
        queryDict = eval(queryRes.content)[0]
        payload['market'] = queryDict['market'];
        payload['type'] = csvType[j];
        payload['orgid'] = queryDict['orgId'];
        payload['minYear'] = queryDict['startTime'];
        payload['maxYear'] = 2018;
        payload['code'] = index[i]
        cPath='D:\\python\\python-finance-master\\python-master\\data\\'+payload['market']+'_'+payload['type']+'_'+payload['code']+'_'+str(payload['minYear'])+'_'+str(payload['maxYear'])+'.zip'
        cPath=cPath.strip()
        cPath=cPath.rstrip("\\")
        isExists=os.path.exists(cPath)
        if not isExists:
            res = requests.post('http://www.cninfo.com.cn/cninfo-new/data/checkDownloadFileIsExit', data=payload)
            if res.content == 'true':
                res = http.request(
                    'POST',
                    'http://www.cninfo.com.cn/cninfo-new/data/download',
                    headers = {},
                    multipart_boundary = boundary,
                    fields=payload);
                with open('D:\\python\\python-finance-master\\python-master\\data\\'+payload['market']+'_'+payload['type']+'_'+payload['code']+'_'+str(payload['minYear'])+'_'+str(payload['maxYear'])+'.zip', "wb") as code:
                    code.write(res.data)
            else:
                print ('file ' +payload['market']+'_'+payload['type']+'_'+payload['code']+'_'+str(payload['minYear'])+'_'+str(payload['maxYear'])+'.zip' + 'not Found!')


unzipFile(rootPath)
