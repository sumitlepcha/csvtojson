# Creating a nested JSON from the sample file.

Highlights:

- First Columns is the header
- Nested JSON starts after a certain row and the identifier for that row can be changed based on the requirement
- As of now program need you to input the value of the last row of the header
- Program can read the number of columns and reiterate through the columns.
- There are few more thing printed even before the JSON, which can be changed/ ignored

Output:
{"eventtype":"nft","eventsubtype":"ibaccountLockout","event-name":"nft_ibaccountlockout","source":"ib",'eventid':'123',"eventts":"27-07-2015 12:24:51.151","msgBody":"{'HostId':'F','succ-fail-flg':'S','sys_time':'27-07-2015 12:24:51.151','lockoutts':'27-07-2015 12:24:51.151','event-id':'','error-code':'NA','error-desc':'NA','cust-id':'1890212','mdm-id':'1-49YIEO','user-id':'1001890212','addr-network':'10.1.138.167','IP-Country':'','IP-City':'','nb-type':'','time-slot':'S2','source-cntry':'AE','addentity1':'','addentity2':'','addentity3':'','addentity4':'','addentity5':'','addentity6':'','addentity7':'','addentity8':'','addentity9':'','addentity10':''}"}
