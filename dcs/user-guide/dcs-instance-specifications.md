# DCS Instance Specifications<a name="EN-US_TOPIC_0237964758"></a>

For each single-node DCS Redis instance, the available memory is less than the total memory because some memory is reserved for system overhead.

For each master/standby DCS Redis instance, the available memory is less than the total memory because some memory is reserved for data persistence. If DCS Redis instances are deployed in master/standby mode, only the master cache node contributes to the available memory.

**Table  1**  Specifications of single-node and master/standby DCS Redis instances

<a name="table2822601515717"></a>
<table><tbody><tr id="row45170224"><td class="cellrowborder" colspan="3" valign="top"><p id="p34909498"><a name="p34909498"></a><a name="p34909498"></a><strong id="b45750028"><a name="b45750028"></a><a name="b45750028"></a>Memory (GB)</strong></p>
</td>
<td class="cellrowborder" rowspan="2" valign="top"><p id="p14764792"><a name="p14764792"></a><a name="p14764792"></a><strong id="b65774268"><a name="b65774268"></a><a name="b65774268"></a>Maximum Number of Connections Allowed</strong></p>
</td>
<td class="cellrowborder" rowspan="2" valign="top"><p id="p26115459"><a name="p26115459"></a><a name="p26115459"></a><strong id="b33712545"><a name="b33712545"></a><a name="b33712545"></a>Maximum Intranet Bandwidth (Mbit/s)</strong></p>
</td>
</tr>
<tr id="row34977455"><td class="cellrowborder" valign="top"><p id="p14601640"><a name="p14601640"></a><a name="p14601640"></a><strong id="b64305901"><a name="b64305901"></a><a name="b64305901"></a>Total</strong></p>
</td>
<td class="cellrowborder" valign="top"><p id="p41395459"><a name="p41395459"></a><a name="p41395459"></a><strong id="b37014815"><a name="b37014815"></a><a name="b37014815"></a>Available (Single Node)</strong></p>
</td>
<td class="cellrowborder" valign="top"><p id="p45410029"><a name="p45410029"></a><a name="p45410029"></a><strong id="b6037081"><a name="b6037081"></a><a name="b6037081"></a>Available (Master/Standby)</strong></p>
</td>
</tr>
<tr id="row54333736"><td class="cellrowborder" valign="top" width="9.47617794156357%"><p id="p38956471"><a name="p38956471"></a><a name="p38956471"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="20.49662191804861%"><p id="p1357571"><a name="p1357571"></a><a name="p1357571"></a>1.5</p>
</td>
<td class="cellrowborder" valign="top" width="28.007370360621213%"><p id="p42854387"><a name="p42854387"></a><a name="p42854387"></a>1.5</p>
</td>
<td class="cellrowborder" valign="top" width="20.18074931999649%"><p id="p48653295"><a name="p48653295"></a><a name="p48653295"></a>10,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.839080459770116%"><p id="p48602848"><a name="p48602848"></a><a name="p48602848"></a>128</p>
</td>
</tr>
<tr id="row34772456"><td class="cellrowborder" valign="top" width="9.47617794156357%"><p id="p65105571"><a name="p65105571"></a><a name="p65105571"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="20.49662191804861%"><p id="p39059911"><a name="p39059911"></a><a name="p39059911"></a>3.2</p>
</td>
<td class="cellrowborder" valign="top" width="28.007370360621213%"><p id="p9736186"><a name="p9736186"></a><a name="p9736186"></a>3.2</p>
</td>
<td class="cellrowborder" valign="top" width="20.18074931999649%"><p id="p50433639"><a name="p50433639"></a><a name="p50433639"></a>10,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.839080459770116%"><p id="p58592948"><a name="p58592948"></a><a name="p58592948"></a>192</p>
</td>
</tr>
<tr id="row57574486"><td class="cellrowborder" valign="top" width="9.47617794156357%"><p id="p33021783"><a name="p33021783"></a><a name="p33021783"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="20.49662191804861%"><p id="p57518732"><a name="p57518732"></a><a name="p57518732"></a>6.8</p>
</td>
<td class="cellrowborder" valign="top" width="28.007370360621213%"><p id="p28505693"><a name="p28505693"></a><a name="p28505693"></a>6.4</p>
</td>
<td class="cellrowborder" valign="top" width="20.18074931999649%"><p id="p27259828"><a name="p27259828"></a><a name="p27259828"></a>10,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.839080459770116%"><p id="p60562422"><a name="p60562422"></a><a name="p60562422"></a>192</p>
</td>
</tr>
<tr id="row8190892"><td class="cellrowborder" valign="top" width="9.47617794156357%"><p id="p59482492"><a name="p59482492"></a><a name="p59482492"></a>16</p>
</td>
<td class="cellrowborder" valign="top" width="20.49662191804861%"><p id="p53352557"><a name="p53352557"></a><a name="p53352557"></a>13.6</p>
</td>
<td class="cellrowborder" valign="top" width="28.007370360621213%"><p id="p26589862"><a name="p26589862"></a><a name="p26589862"></a>12.8</p>
</td>
<td class="cellrowborder" valign="top" width="20.18074931999649%"><p id="p6295248"><a name="p6295248"></a><a name="p6295248"></a>10,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.839080459770116%"><p id="p40153107"><a name="p40153107"></a><a name="p40153107"></a>256</p>
</td>
</tr>
<tr id="row25833645"><td class="cellrowborder" valign="top" width="9.47617794156357%"><p id="p12150471"><a name="p12150471"></a><a name="p12150471"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="20.49662191804861%"><p id="p44664077"><a name="p44664077"></a><a name="p44664077"></a>27.2</p>
</td>
<td class="cellrowborder" valign="top" width="28.007370360621213%"><p id="p61020521"><a name="p61020521"></a><a name="p61020521"></a>25.6</p>
</td>
<td class="cellrowborder" valign="top" width="20.18074931999649%"><p id="p43715136"><a name="p43715136"></a><a name="p43715136"></a>10,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.839080459770116%"><p id="p51265148"><a name="p51265148"></a><a name="p51265148"></a>256</p>
</td>
</tr>
<tr id="row58733156"><td class="cellrowborder" valign="top" width="9.47617794156357%"><p id="p59765170"><a name="p59765170"></a><a name="p59765170"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="20.49662191804861%"><p id="p9140568"><a name="p9140568"></a><a name="p9140568"></a>58.2</p>
</td>
<td class="cellrowborder" valign="top" width="28.007370360621213%"><p id="p2188543"><a name="p2188543"></a><a name="p2188543"></a>51.2</p>
</td>
<td class="cellrowborder" valign="top" width="20.18074931999649%"><p id="p43054286"><a name="p43054286"></a><a name="p43054286"></a>12,000</p>
</td>
<td class="cellrowborder" valign="top" width="21.839080459770116%"><p id="p64845166"><a name="p64845166"></a><a name="p64845166"></a>384</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Specifications of cluster DCS Redis instances

<a name="table45620191"></a>
<table><thead align="left"><tr id="row8999603"><th class="cellrowborder" valign="top" width="23.232323232323232%" id="mcps1.2.5.1.1"><p id="p57879229"><a name="p57879229"></a><a name="p57879229"></a><strong id="b123611619183513"><a name="b123611619183513"></a><a name="b123611619183513"></a>Total Memory (GB)</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.2"><p id="p57705992"><a name="p57705992"></a><a name="p57705992"></a><strong id="b83708199358"><a name="b83708199358"></a><a name="b83708199358"></a>Available Memory (GB)</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323232%" id="mcps1.2.5.1.3"><p id="p43673788"><a name="p43673788"></a><a name="p43673788"></a><strong id="b1937215191357"><a name="b1937215191357"></a><a name="b1937215191357"></a>Maximum Number of Connections Allowed</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.28282828282828%" id="mcps1.2.5.1.4"><p id="p47915903"><a name="p47915903"></a><a name="p47915903"></a><strong id="b337415197357"><a name="b337415197357"></a><a name="b337415197357"></a>Maximum Intranet Bandwidth (Mbit/s)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row55982972"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.1 "><p id="p38326873"><a name="p38326873"></a><a name="p38326873"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.2 "><p id="p17468990"><a name="p17468990"></a><a name="p17468990"></a>64</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.3 "><p id="p5702100"><a name="p5702100"></a><a name="p5702100"></a>20,000</p>
</td>
<td class="cellrowborder" valign="top" width="28.28282828282828%" headers="mcps1.2.5.1.4 "><p id="p59216962"><a name="p59216962"></a><a name="p59216962"></a>2000</p>
</td>
</tr>
<tr id="row63190618"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.1 "><p id="p18166465"><a name="p18166465"></a><a name="p18166465"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.2 "><p id="p62197523"><a name="p62197523"></a><a name="p62197523"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.3 "><p id="p4834618"><a name="p4834618"></a><a name="p4834618"></a>20,000</p>
</td>
<td class="cellrowborder" valign="top" width="28.28282828282828%" headers="mcps1.2.5.1.4 "><p id="p56059806"><a name="p56059806"></a><a name="p56059806"></a>2000</p>
</td>
</tr>
<tr id="row34776210"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.1 "><p id="p65409627"><a name="p65409627"></a><a name="p65409627"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.2 "><p id="p63688469"><a name="p63688469"></a><a name="p63688469"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.3 "><p id="p58492392"><a name="p58492392"></a><a name="p58492392"></a>20,000</p>
</td>
<td class="cellrowborder" valign="top" width="28.28282828282828%" headers="mcps1.2.5.1.4 "><p id="p40263291"><a name="p40263291"></a><a name="p40263291"></a>2000</p>
</td>
</tr>
<tr id="row26825300"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.1 "><p id="p25365674"><a name="p25365674"></a><a name="p25365674"></a>512</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.2 "><p id="p41353750"><a name="p41353750"></a><a name="p41353750"></a>512</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.5.1.3 "><p id="p61319421"><a name="p61319421"></a><a name="p61319421"></a>20,000</p>
</td>
<td class="cellrowborder" valign="top" width="28.28282828282828%" headers="mcps1.2.5.1.4 "><p id="p817225"><a name="p817225"></a><a name="p817225"></a>2000</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The maximum intranet bandwidth is the sum of maximum inbound and outbound intranet bandwidths. Usually, DCS instances are read more frequently than they are written. Therefore, it is recommended that the maximum inbound intranet bandwidth be one third of the maximum intranet bandwidth and the maximum outbound intranet bandwidth be two thirds of the maximum intranet bandwidth.  

