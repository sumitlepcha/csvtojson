# Creating a nested JSON from the sample file.

Highlights:

- First Columns is the header
- Nested JSON starts after a certain row and the identifier for that row can be changed based on the requirement
- As of now program need you to input the value of the last row of the header
- Program can read the number of columns and reiterate through the columns.
- There are few more thing printed even before the JSON, which can be changed/ ignored

Sample Output:
{"eventtype":"nft","eventsubtype":"ibaccountLockout","event-name":"nft_ibaccountlockout","source":"ib",'eventid':'123',"eventts":"27-07-2015 12:24:51.151","msgBody":"{'HoId':'F','su-flg':'S','sys_time':'27-07-2015 12:24:51.151','lots':'27-07-2015 12:24:51.151','event-id':'','er-ce':'NA','er-desc':'NA','cu-id':'1890212','dm-id':'1-49YIEO','usr-id':'1001890212','addr-net':'10.1.138.167','IP-Cont':'','IP-Cty':'','nb-tpe':'','tme-slt':'S2','src-cntry':'AE','addentity10':''}"}
