from dotenv import load_dotenv
from shareplum import Site
from shareplum import Office365

load_dotenv()
user = os.getenv("GVI_USER")
passwd = os.getenv("GVI_PASSWD")
url = 'https://cseserviceproj.sharepoint.com'


def initSite(user, passwd, url):
    authcookie = Office365(url, username=user, password=passwd).GetCookies()
    site = Site(url, authcookie=authcookie)
    return site

def getList(site, listname):
    new_list = site.List(listname)
    return new_list

def UpdateItemField(sp_list, name, field, val):
    sp_data = sp_list.GetListItems()
    for item in sp_data:
        if (item['Title'] == name):
            item[field] = val
            break
    sp_list.UpdateListItems(data=sp_data, kind='Update')

def DeleteItem(sp_list, name):
    sp_data = sp_list.GetListItems()
    #for item in sp_data:
        #if(item['Title'] == name):
           
def AddItem(sp_list, contact_info):
    sp_list.UpdateListItems(data=contact_info, kind='New')
   
