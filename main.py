#!/usr/bin/env python
# coding: utf-8

# In[6]:



import requests
import threading
import time
import json


def worker(tid, n):
    url = "https://clarksonmsda.org/api/get_product.php?pid="
    url = url + str(n)
    req = requests.get(url)
    data = json.loads(req.text)
    if data['data'] is not None:
        
        dict1 = {
            "prod_id":      data['data']['prod_id'],
            "prod_sku":     data['data']['prod_sku'],
            "prod_cat":     data['data']['prod_cat'],
            "prod_name":    data['data']['prod_name']
        }
        outfilename = "./output/pid_" + str(n).rjust(4, '0') + ".json"
        
        with open(outfilename, "w") as outfile:
            json.dump(dict1, outfile)


n = 0
tid = 0
tidlst = []  
start = time.time()
while tid < 200:
    w = threading.Thread(name='tid_'+str(tid),target=worker, args=(tid, n,))
    w.start()
    tidlst.append(w)
    tid += 1
    n += 1
for t in tidlst:
    t.join()
print(tidlst)
print(time.time() - start)


# In[ ]:




