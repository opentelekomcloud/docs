# Logging Overview<a name="obs_03_0431"></a>

You can enable logging to facilitate analysis or audit as required. Access logs enable a bucket owner to analyze the property, type, or trend of requests to the bucket in depth. When the logging function of a bucket is enabled, OBS will log access requests for the bucket automatically, and write the generated log files to the specified bucket \(target bucket\).

The logging function itself is offered for free, only the space occupied by log files is charged.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>After logging is enabled, the log delivery user will be automatically granted the permission to read the bucket ACL and write the bucket where logs are saved. If you manually disable such permissions, bucket logging fails.  

OBS can record bucket access requests in logs for request analysis and log audit.

Logs occupy some OBS storage space rented by users, causing extra fees. For this reason, OBS does not collect bucket access logs by default.

Approximately fifteen minutes after log management is successfully configured, you can view the operation logs in the target bucket that stores the logs.

The following shows an example access log of the target bucket:

```
787f2f92b20943998a4fe2ab75eb09b8 bucket [13/Aug/2015:01:43:42 +0000] xx.xx.xx.xx 
787f2f92b20943998a4fe2ab75eb09b8 281599BACAD9376ECE141B842B94535B  REST.GET.BUCKET.LOCATION 
- "GET /bucket?location HTTP/1.1" 200 - 211 - 6 6 "-"  "HttpClient" - -
```

The access log of each bucket contains the following information.

**Table  1**  Bucket log format

<a name="en-us_topic_0045853553_table131214386116"></a>
<table><thead align="left"><tr id="en-us_topic_0045853553_row91211438610"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.1"><p id="en-us_topic_0045853553_p171215388116"><a name="en-us_topic_0045853553_p171215388116"></a><a name="en-us_topic_0045853553_p171215388116"></a><strong id="en-us_topic_0045853553_b5199335294"><a name="en-us_topic_0045853553_b5199335294"></a><a name="en-us_topic_0045853553_b5199335294"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.2"><p id="en-us_topic_0045853553_p41212381016"><a name="en-us_topic_0045853553_p41212381016"></a><a name="en-us_topic_0045853553_p41212381016"></a><strong id="en-us_topic_0045853553_b1026099112911"><a name="en-us_topic_0045853553_b1026099112911"></a><a name="en-us_topic_0045853553_b1026099112911"></a>Value Example</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.3"><p id="en-us_topic_0045853553_p812114386117"><a name="en-us_topic_0045853553_p812114386117"></a><a name="en-us_topic_0045853553_p812114386117"></a><strong id="en-us_topic_0045853553_b5762121572918"><a name="en-us_topic_0045853553_b5762121572918"></a><a name="en-us_topic_0045853553_b5762121572918"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0045853553_row1812118381315"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p317119161311"><a name="en-us_topic_0045853553_p317119161311"></a><a name="en-us_topic_0045853553_p317119161311"></a>BucketOwner</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p11713161731"><a name="en-us_topic_0045853553_p11713161731"></a><a name="en-us_topic_0045853553_p11713161731"></a>787f2f92b20943998a4fe2ab75eb09b8</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p1317111168312"><a name="en-us_topic_0045853553_p1317111168312"></a><a name="en-us_topic_0045853553_p1317111168312"></a>Account ID of the bucket owner</p>
<p id="en-us_topic_0045853553_p16250135004910"><a name="en-us_topic_0045853553_p16250135004910"></a><a name="en-us_topic_0045853553_p16250135004910"></a><strong id="en-us_topic_0045853553_b575518588313"><a name="en-us_topic_0045853553_b575518588313"></a><a name="en-us_topic_0045853553_b575518588313"></a>Account ID</strong> corresponds to <strong id="en-us_topic_0045853553_b41318815412"><a name="en-us_topic_0045853553_b41318815412"></a><a name="en-us_topic_0045853553_b41318815412"></a>Domain ID</strong> on the <strong id="en-us_topic_0045853553_b1397315101441"><a name="en-us_topic_0045853553_b1397315101441"></a><a name="en-us_topic_0045853553_b1397315101441"></a>My Credential</strong> page.</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row512113386112"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p1717113165312"><a name="en-us_topic_0045853553_p1717113165312"></a><a name="en-us_topic_0045853553_p1717113165312"></a>Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p3171216839"><a name="en-us_topic_0045853553_p3171216839"></a><a name="en-us_topic_0045853553_p3171216839"></a>bucket</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p21714168313"><a name="en-us_topic_0045853553_p21714168313"></a><a name="en-us_topic_0045853553_p21714168313"></a>Name of the bucket</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row161211438717"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p141718161331"><a name="en-us_topic_0045853553_p141718161331"></a><a name="en-us_topic_0045853553_p141718161331"></a>Time</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p1217121611311"><a name="en-us_topic_0045853553_p1217121611311"></a><a name="en-us_topic_0045853553_p1217121611311"></a>[13/Aug/2015:01:43:42 +0000]</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p7171316031"><a name="en-us_topic_0045853553_p7171316031"></a><a name="en-us_topic_0045853553_p7171316031"></a>Timestamp of the request (UTC)</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row71212387114"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p517112168319"><a name="en-us_topic_0045853553_p517112168319"></a><a name="en-us_topic_0045853553_p517112168319"></a>Remote IP</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p11171121618320"><a name="en-us_topic_0045853553_p11171121618320"></a><a name="en-us_topic_0045853553_p11171121618320"></a>xx.xx.xx.xx</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p317121610316"><a name="en-us_topic_0045853553_p317121610316"></a><a name="en-us_topic_0045853553_p317121610316"></a>IP address from where the request is initiated</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row412120385118"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p1617116161139"><a name="en-us_topic_0045853553_p1617116161139"></a><a name="en-us_topic_0045853553_p1617116161139"></a>Requester</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p4171141618312"><a name="en-us_topic_0045853553_p4171141618312"></a><a name="en-us_topic_0045853553_p4171141618312"></a>787f2f92b20943998a4fe2ab75eb09b8</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p121711816833"><a name="en-us_topic_0045853553_p121711816833"></a><a name="en-us_topic_0045853553_p121711816833"></a>Requester ID</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row1012119381212"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p17171181616312"><a name="en-us_topic_0045853553_p17171181616312"></a><a name="en-us_topic_0045853553_p17171181616312"></a>RequestID</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p91713161734"><a name="en-us_topic_0045853553_p91713161734"></a><a name="en-us_topic_0045853553_p91713161734"></a>281599BACAD9376ECE141B842B94535B</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p8171121615316"><a name="en-us_topic_0045853553_p8171121615316"></a><a name="en-us_topic_0045853553_p8171121615316"></a>Request ID</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row0121538319"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p15171316734"><a name="en-us_topic_0045853553_p15171316734"></a><a name="en-us_topic_0045853553_p15171316734"></a>Operation</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p217121618311"><a name="en-us_topic_0045853553_p217121618311"></a><a name="en-us_topic_0045853553_p217121618311"></a>REST.GET.BUCKET.LOCATION</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p917112161834"><a name="en-us_topic_0045853553_p917112161834"></a><a name="en-us_topic_0045853553_p917112161834"></a>Name of the Operation</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row0997173031516"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p159971730131518"><a name="en-us_topic_0045853553_p159971730131518"></a><a name="en-us_topic_0045853553_p159971730131518"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p4997430191515"><a name="en-us_topic_0045853553_p4997430191515"></a><a name="en-us_topic_0045853553_p4997430191515"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p1428011903918"><a name="en-us_topic_0045853553_p1428011903918"></a><a name="en-us_topic_0045853553_p1428011903918"></a>Object name</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row218717133312"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p181712167318"><a name="en-us_topic_0045853553_p181712167318"></a><a name="en-us_topic_0045853553_p181712167318"></a>Request-URI</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p151711616837"><a name="en-us_topic_0045853553_p151711616837"></a><a name="en-us_topic_0045853553_p151711616837"></a>GET /bucket?location HTTP/1.1</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p1517181618315"><a name="en-us_topic_0045853553_p1517181618315"></a><a name="en-us_topic_0045853553_p1517181618315"></a>URI of the request</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row965413106316"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p131710168310"><a name="en-us_topic_0045853553_p131710168310"></a><a name="en-us_topic_0045853553_p131710168310"></a>HTTPStatus</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p9171316238"><a name="en-us_topic_0045853553_p9171316238"></a><a name="en-us_topic_0045853553_p9171316238"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p18171171616313"><a name="en-us_topic_0045853553_p18171171616313"></a><a name="en-us_topic_0045853553_p18171171616313"></a>Return code</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row15399651112010"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p103991051162012"><a name="en-us_topic_0045853553_p103991051162012"></a><a name="en-us_topic_0045853553_p103991051162012"></a>ErrorCode</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p4399185111206"><a name="en-us_topic_0045853553_p4399185111206"></a><a name="en-us_topic_0045853553_p4399185111206"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p193991851112014"><a name="en-us_topic_0045853553_p193991851112014"></a><a name="en-us_topic_0045853553_p193991851112014"></a>Error code</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row18264188238"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p117117161836"><a name="en-us_topic_0045853553_p117117161836"></a><a name="en-us_topic_0045853553_p117117161836"></a>BytesSent</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p61717167319"><a name="en-us_topic_0045853553_p61717167319"></a><a name="en-us_topic_0045853553_p61717167319"></a>211</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p161711016435"><a name="en-us_topic_0045853553_p161711016435"></a><a name="en-us_topic_0045853553_p161711016435"></a>Size of the HTTP response, expressed in bytes</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row4789642132118"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p8789114282111"><a name="en-us_topic_0045853553_p8789114282111"></a><a name="en-us_topic_0045853553_p8789114282111"></a>ObjectSize</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p15789144252119"><a name="en-us_topic_0045853553_p15789144252119"></a><a name="en-us_topic_0045853553_p15789144252119"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p878954214212"><a name="en-us_topic_0045853553_p878954214212"></a><a name="en-us_topic_0045853553_p878954214212"></a>Object size (bytes)</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row7983195831"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p14171516134"><a name="en-us_topic_0045853553_p14171516134"></a><a name="en-us_topic_0045853553_p14171516134"></a>TotalTime</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p1417115160310"><a name="en-us_topic_0045853553_p1417115160310"></a><a name="en-us_topic_0045853553_p1417115160310"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p2017114161831"><a name="en-us_topic_0045853553_p2017114161831"></a><a name="en-us_topic_0045853553_p2017114161831"></a>Processing time on the server (ms)</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row16811143633"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p617110167315"><a name="en-us_topic_0045853553_p617110167315"></a><a name="en-us_topic_0045853553_p617110167315"></a>Turn-AroundTime</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p4171616233"><a name="en-us_topic_0045853553_p4171616233"></a><a name="en-us_topic_0045853553_p4171616233"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p161711716536"><a name="en-us_topic_0045853553_p161711716536"></a><a name="en-us_topic_0045853553_p161711716536"></a>Total time for processing the request (ms)</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row9951955723"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p0951655520"><a name="en-us_topic_0045853553_p0951655520"></a><a name="en-us_topic_0045853553_p0951655520"></a>Referer</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p199511855725"><a name="en-us_topic_0045853553_p199511855725"></a><a name="en-us_topic_0045853553_p199511855725"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p1195113551720"><a name="en-us_topic_0045853553_p1195113551720"></a><a name="en-us_topic_0045853553_p1195113551720"></a>Header field <strong id="en-us_topic_0045853553_b728161215314"><a name="en-us_topic_0045853553_b728161215314"></a><a name="en-us_topic_0045853553_b728161215314"></a>Referer</strong> of the request</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row144987116315"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p154981012317"><a name="en-us_topic_0045853553_p154981012317"></a><a name="en-us_topic_0045853553_p154981012317"></a>User-Agent</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p15498310315"><a name="en-us_topic_0045853553_p15498310315"></a><a name="en-us_topic_0045853553_p15498310315"></a>HttpClient</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p549815114320"><a name="en-us_topic_0045853553_p549815114320"></a><a name="en-us_topic_0045853553_p549815114320"></a>User-Agent header of the request</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row1320275918214"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p72021159823"><a name="en-us_topic_0045853553_p72021159823"></a><a name="en-us_topic_0045853553_p72021159823"></a>VersionID</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p1820219591624"><a name="en-us_topic_0045853553_p1820219591624"></a><a name="en-us_topic_0045853553_p1820219591624"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p2020218592212"><a name="en-us_topic_0045853553_p2020218592212"></a><a name="en-us_topic_0045853553_p2020218592212"></a>Version ID carried in the request</p>
</td>
</tr>
<tr id="en-us_topic_0045853553_row5594115117310"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0045853553_p1559445111318"><a name="en-us_topic_0045853553_p1559445111318"></a><a name="en-us_topic_0045853553_p1559445111318"></a>STSLogUrn</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0045853553_p125943511133"><a name="en-us_topic_0045853553_p125943511133"></a><a name="en-us_topic_0045853553_p125943511133"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0045853553_p65941151832"><a name="en-us_topic_0045853553_p65941151832"></a><a name="en-us_topic_0045853553_p65941151832"></a>Federated authentication and agency information</p>
</td>
</tr>
</tbody>
</table>

