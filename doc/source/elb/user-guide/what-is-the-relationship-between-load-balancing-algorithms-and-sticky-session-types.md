# What Is the Relationship Between Load Balancing Algorithms and Sticky Session Types?<a name="EN-US_TOPIC_0091131372"></a>

The sticky session feature ensures that requests from the same client are routed to the same backend server. Three types of sticky sessions are available.  [Table 1](#table44808652142126)  lists the relationships between load balancing algorithms and sticky session types of enhanced load balancers.  [Table 2](#table1612018518726)  lists the relationships between load balancing algorithms and sticky session types of classic load balancers.

**Table  1**  Session stickiness of enhanced load balancers

<a name="table44808652142126"></a>
<table><thead align="left"><tr id="row57750719142126"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p56688074142142"><a name="p56688074142142"></a><a name="p56688074142142"></a><strong id="b84235270610234"><a name="b84235270610234"></a><a name="b84235270610234"></a>Load Balancing Algorithm</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.95%" id="mcps1.2.5.1.2"><p id="p52415961142126"><a name="p52415961142126"></a><a name="p52415961142126"></a><strong id="b842352706102318"><a name="b842352706102318"></a><a name="b842352706102318"></a>Sticky Session Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.68%" id="mcps1.2.5.1.3"><p id="p4883497514222"><a name="p4883497514222"></a><a name="p4883497514222"></a><strong id="b842352706144352"><a name="b842352706144352"></a><a name="b842352706144352"></a>Layer 4 (TCP/UDP)</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.37%" id="mcps1.2.5.1.4"><p id="p35305098142126"><a name="p35305098142126"></a><a name="p35305098142126"></a><strong id="b842352706123424"><a name="b842352706123424"></a><a name="b842352706123424"></a>Layer 7 (HTTP/HTTPS)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row49310429142126"><td class="cellrowborder" rowspan="3" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p36596594142258"><a name="p36596594142258"></a><a name="p36596594142258"></a>Weighted round robin</p>
</td>
<td class="cellrowborder" valign="top" width="31.95%" headers="mcps1.2.5.1.2 "><p id="p3955310142336"><a name="p3955310142336"></a><a name="p3955310142336"></a>Source IP address</p>
</td>
<td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.5.1.3 "><p id="p2738028614244"><a name="p2738028614244"></a><a name="p2738028614244"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.2.5.1.4 "><p id="p321066114244"><a name="p321066114244"></a><a name="p321066114244"></a>Not supported</p>
</td>
</tr>
<tr id="row33466439142126"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p64848874142336"><a name="p64848874142336"></a><a name="p64848874142336"></a>Load balancer cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p5887104114244"><a name="p5887104114244"></a><a name="p5887104114244"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p382499114244"><a name="p382499114244"></a><a name="p382499114244"></a>Supported</p>
</td>
</tr>
<tr id="row57140943142126"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p30189096142336"><a name="p30189096142336"></a><a name="p30189096142336"></a>Application cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p3695507314244"><a name="p3695507314244"></a><a name="p3695507314244"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p4057092714244"><a name="p4057092714244"></a><a name="p4057092714244"></a>Supported</p>
</td>
</tr>
<tr id="row34797656142126"><td class="cellrowborder" rowspan="3" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4320234142249"><a name="p4320234142249"></a><a name="p4320234142249"></a>Weighted least connections</p>
</td>
<td class="cellrowborder" valign="top" width="31.95%" headers="mcps1.2.5.1.2 "><p id="p63252787142336"><a name="p63252787142336"></a><a name="p63252787142336"></a>Source IP address</p>
</td>
<td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.5.1.3 "><p id="p4830601114244"><a name="p4830601114244"></a><a name="p4830601114244"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.2.5.1.4 "><p id="p2047283614244"><a name="p2047283614244"></a><a name="p2047283614244"></a>Not supported</p>
</td>
</tr>
<tr id="row15279881142126"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p7492703142336"><a name="p7492703142336"></a><a name="p7492703142336"></a>Load balancer cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p2652971714244"><a name="p2652971714244"></a><a name="p2652971714244"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p142344114244"><a name="p142344114244"></a><a name="p142344114244"></a>Not supported</p>
</td>
</tr>
<tr id="row9181406142131"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p26362629142336"><a name="p26362629142336"></a><a name="p26362629142336"></a>Application cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p3105612214244"><a name="p3105612214244"></a><a name="p3105612214244"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p3251797314244"><a name="p3251797314244"></a><a name="p3251797314244"></a>Not supported</p>
</td>
</tr>
<tr id="row20434471142131"><td class="cellrowborder" rowspan="3" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p17428470142251"><a name="p17428470142251"></a><a name="p17428470142251"></a>Source IP hash</p>
</td>
<td class="cellrowborder" valign="top" width="31.95%" headers="mcps1.2.5.1.2 "><p id="p25221962142336"><a name="p25221962142336"></a><a name="p25221962142336"></a>Source IP address</p>
</td>
<td class="cellrowborder" valign="top" width="20.68%" headers="mcps1.2.5.1.3 "><p id="p1617379314244"><a name="p1617379314244"></a><a name="p1617379314244"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.2.5.1.4 "><p id="p3500885214244"><a name="p3500885214244"></a><a name="p3500885214244"></a>Supported</p>
</td>
</tr>
<tr id="row2150805142126"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p66090712142336"><a name="p66090712142336"></a><a name="p66090712142336"></a>Load balancer cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p2008522214244"><a name="p2008522214244"></a><a name="p2008522214244"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1629026714244"><a name="p1629026714244"></a><a name="p1629026714244"></a>Not supported</p>
</td>
</tr>
<tr id="row63191412142126"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p63073698142336"><a name="p63073698142336"></a><a name="p63073698142336"></a>Application cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p6444507014244"><a name="p6444507014244"></a><a name="p6444507014244"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p5266815914244"><a name="p5266815914244"></a><a name="p5266815914244"></a>Not supported</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Session stickiness of classic load balancers

<a name="table1612018518726"></a>
<table><thead align="left"><tr id="row4031731118726"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p3759409618838"><a name="p3759409618838"></a><a name="p3759409618838"></a><strong id="b280255018838"><a name="b280255018838"></a><a name="b280255018838"></a>Load Balancing Algorithm</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p2568002018838"><a name="p2568002018838"></a><a name="p2568002018838"></a><strong id="b2979358918838"><a name="b2979358918838"></a><a name="b2979358918838"></a>Sticky Session Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p6447051418838"><a name="p6447051418838"></a><a name="p6447051418838"></a><strong id="b411700554"><a name="b411700554"></a><a name="b411700554"></a>Layer 4 (TCP/UDP)</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p2280043118838"><a name="p2280043118838"></a><a name="p2280043118838"></a><strong id="b742721118"><a name="b742721118"></a><a name="b742721118"></a>Layer 7 (HTTP/HTTPS)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2886765918726"><td class="cellrowborder" rowspan="3" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p464373218838"><a name="p464373218838"></a><a name="p464373218838"></a>Round robin</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p4059800018838"><a name="p4059800018838"></a><a name="p4059800018838"></a>Source IP address</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p10366418838"><a name="p10366418838"></a><a name="p10366418838"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p839679618838"><a name="p839679618838"></a><a name="p839679618838"></a>Not supported</p>
</td>
</tr>
<tr id="row3177055518726"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1435825318838"><a name="p1435825318838"></a><a name="p1435825318838"></a>Load balancer cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p2216786418838"><a name="p2216786418838"></a><a name="p2216786418838"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p5076657218838"><a name="p5076657218838"></a><a name="p5076657218838"></a>Supported</p>
</td>
</tr>
<tr id="row5977167318726"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p3184695918838"><a name="p3184695918838"></a><a name="p3184695918838"></a>Application cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p2946689518838"><a name="p2946689518838"></a><a name="p2946689518838"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p62808486181718"><a name="p62808486181718"></a><a name="p62808486181718"></a>Not supported</p>
</td>
</tr>
<tr id="row227775918726"><td class="cellrowborder" rowspan="3" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5918080418838"><a name="p5918080418838"></a><a name="p5918080418838"></a>Least connections</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2891582618838"><a name="p2891582618838"></a><a name="p2891582618838"></a>Source IP address</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p6048060918838"><a name="p6048060918838"></a><a name="p6048060918838"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p6709119318838"><a name="p6709119318838"></a><a name="p6709119318838"></a>Not supported</p>
</td>
</tr>
<tr id="row1472471318813"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p5422692218838"><a name="p5422692218838"></a><a name="p5422692218838"></a>Load balancer cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p3030459018838"><a name="p3030459018838"></a><a name="p3030459018838"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p3875272618838"><a name="p3875272618838"></a><a name="p3875272618838"></a>Not supported</p>
</td>
</tr>
<tr id="row1477401918813"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p6501485318838"><a name="p6501485318838"></a><a name="p6501485318838"></a>Application cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p3171176818838"><a name="p3171176818838"></a><a name="p3171176818838"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p44220119181726"><a name="p44220119181726"></a><a name="p44220119181726"></a>Not supported</p>
</td>
</tr>
<tr id="row190362518813"><td class="cellrowborder" rowspan="3" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p957039418838"><a name="p957039418838"></a><a name="p957039418838"></a>Source IP hash</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p3700448618838"><a name="p3700448618838"></a><a name="p3700448618838"></a>Source IP address</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p4457335718838"><a name="p4457335718838"></a><a name="p4457335718838"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p5367218518838"><a name="p5367218518838"></a><a name="p5367218518838"></a>Supported</p>
</td>
</tr>
<tr id="row1219487518813"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p255581518838"><a name="p255581518838"></a><a name="p255581518838"></a>Load balancer cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p569442918838"><a name="p569442918838"></a><a name="p569442918838"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p5859560418838"><a name="p5859560418838"></a><a name="p5859560418838"></a>Not supported</p>
</td>
</tr>
<tr id="row2628835018835"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p3495809818838"><a name="p3495809818838"></a><a name="p3495809818838"></a>Application cookie</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1303366518838"><a name="p1303366518838"></a><a name="p1303366518838"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p34236357181722"><a name="p34236357181722"></a><a name="p34236357181722"></a>Not supported</p>
</td>
</tr>
</tbody>
</table>

Generally, the round robin algorithm is recommended. Layer-4 sticky sessions use source IP addresses, and Layer-7 sticky sessions use load balancer cookies.

