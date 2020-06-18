# Error Codes<a name="EN-US_TOPIC_0107541808"></a>

## Context<a name="section2270842516290"></a>

-   An error code returned by an API does not correspond to one error message. The following table lists only common error messages.
-   Most BMS APIs are asynchronous. Some error codes are displayed in the returned messages for task viewing requests. HTTP status codes may not be accurate.
-   The BMS service is strongly dependent on other services, such as network and storage. When error messages are provided for the BMS-depended services, contact technical support for troubleshooting.

## Error Code Description<a name="section59060991162916"></a>

<a name="table36210876112050"></a>
<table><thead align="left"><tr id="row60537118112050"><th class="cellrowborder" valign="top" width="9.900990099009901%" id="mcps1.1.6.1.1"><p id="p36247510141740"><a name="p36247510141740"></a><a name="p36247510141740"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.1.6.1.2"><p id="p4559511112050"><a name="p4559511112050"></a><a name="p4559511112050"></a>Returned Value</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.6.1.3"><p id="p33776109112050"><a name="p33776109112050"></a><a name="p33776109112050"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="28.71287128712871%" id="mcps1.1.6.1.4"><p id="p1010742314195"><a name="p1010742314195"></a><a name="p1010742314195"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="31.683168316831683%" id="mcps1.1.6.1.5"><p id="p28762041141941"><a name="p28762041141941"></a><a name="p28762041141941"></a>Handling Measure</p>
</th>
</tr>
</thead>
<tbody><tr id="row46722832155116"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p47395611142232"><a name="p47395611142232"></a><a name="p47395611142232"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p20402961155119"><a name="p20402961155119"></a><a name="p20402961155119"></a>BMS.0001</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p42027136155119"><a name="p42027136155119"></a><a name="p42027136155119"></a>Request error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p96751453181710"><a name="p96751453181710"></a><a name="p96751453181710"></a>Fail to parse request, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p48023993141941"><a name="p48023993141941"></a><a name="p48023993141941"></a>Check the request body according to the returned error message.</p>
</td>
</tr>
<tr id="row61981312164"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p319131314169"><a name="p319131314169"></a><a name="p319131314169"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1119813151610"><a name="p1119813151610"></a><a name="p1119813151610"></a>BMS.0002</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p15091917292"><a name="p15091917292"></a><a name="p15091917292"></a><span id="text154602050191117"><a name="text154602050191117"></a><a name="text154602050191117"></a>BMS</span><span id="text82535523113"><a name="text82535523113"></a><a name="text82535523113"></a></span> has not been launched.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p191915139169"><a name="p191915139169"></a><a name="p191915139169"></a>The BMS service is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1719161361618"><a name="p1719161361618"></a><a name="p1719161361618"></a>Select a region where the BMS service is available.</p>
</td>
</tr>
<tr id="row230915415181"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1730919415182"><a name="p1730919415182"></a><a name="p1730919415182"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p230915415188"><a name="p230915415188"></a><a name="p230915415188"></a>BMS.0003</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1230984116183"><a name="p1230984116183"></a><a name="p1230984116183"></a>Request error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p7309154111185"><a name="p7309154111185"></a><a name="p7309154111185"></a>Create BareMetal Server error, request is null.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p23092418188"><a name="p23092418188"></a><a name="p23092418188"></a>Check the request body according to the returned error message.</p>
</td>
</tr>
<tr id="row10706171532016"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p207069158203"><a name="p207069158203"></a><a name="p207069158203"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p632712556203"><a name="p632712556203"></a><a name="p632712556203"></a>BMS.0004</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p10706215162011"><a name="p10706215162011"></a><a name="p10706215162011"></a>Insufficient permission.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1389194941019"><a name="p1389194941019"></a><a name="p1389194941019"></a>Role check fail, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p470641511206"><a name="p470641511206"></a><a name="p470641511206"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row9328111419124"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p93281514191219"><a name="p93281514191219"></a><a name="p93281514191219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p63281214161211"><a name="p63281214161211"></a><a name="p63281214161211"></a>BMS.0005</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p13316191841511"><a name="p13316191841511"></a><a name="p13316191841511"></a>Insufficient permission.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p14136205464318"><a name="p14136205464318"></a><a name="p14136205464318"></a>Role check fail, reason: You do not have permission or your balance is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p0328181416122"><a name="p0328181416122"></a><a name="p0328181416122"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row11136111414310"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1513631415312"><a name="p1513631415312"></a><a name="p1513631415312"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p2013651412317"><a name="p2013651412317"></a><a name="p2013651412317"></a>BMS.0008</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p51368141313"><a name="p51368141313"></a><a name="p51368141313"></a>Failed to query a flavor.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p12136151411311"><a name="p12136151411311"></a><a name="p12136151411311"></a>Fail to query flavor [%s], reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1413601433120"><a name="p1413601433120"></a><a name="p1413601433120"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row45871655172710"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p558745532714"><a name="p558745532714"></a><a name="p558745532714"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p195871055152716"><a name="p195871055152716"></a><a name="p195871055152716"></a>BMS.0006</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p858745552715"><a name="p858745552715"></a><a name="p858745552715"></a>Failed to create the task.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p175877558273"><a name="p175877558273"></a><a name="p175877558273"></a>Fail to operate baremetal server.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p666217560299"><a name="p666217560299"></a><a name="p666217560299"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row16549131763113"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p195494178311"><a name="p195494178311"></a><a name="p195494178311"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p11549171723112"><a name="p11549171723112"></a><a name="p11549171723112"></a>BMS.0009</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p105491217113115"><a name="p105491217113115"></a><a name="p105491217113115"></a>Failed to query flavor attributes.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p6549217183115"><a name="p6549217183115"></a><a name="p6549217183115"></a>Fail to query flavor extra specs[%s], reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p19550417123112"><a name="p19550417123112"></a><a name="p19550417123112"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1453772110314"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p353822163118"><a name="p353822163118"></a><a name="p353822163118"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p185381221113111"><a name="p185381221113111"></a><a name="p185381221113111"></a>BMS.0010</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p0926155514019"><a name="p0926155514019"></a><a name="p0926155514019"></a>Failed to query an image.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p115381219316"><a name="p115381219316"></a><a name="p115381219316"></a>Fail to query image [%s], reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1853810211315"><a name="p1853810211315"></a><a name="p1853810211315"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1425510257310"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1025522514313"><a name="p1025522514313"></a><a name="p1025522514313"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p16255132553119"><a name="p16255132553119"></a><a name="p16255132553119"></a>BMS.0011</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p92559255317"><a name="p92559255317"></a><a name="p92559255317"></a>The images do not support <span id="text853412315122"><a name="text853412315122"></a><a name="text853412315122"></a>BMS</span><span id="text1653418361214"><a name="text1653418361214"></a><a name="text1653418361214"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p3255825173120"><a name="p3255825173120"></a><a name="p3255825173120"></a>The selected images cannot be used to apply for BMSs, %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p6255425183115"><a name="p6255425183115"></a><a name="p6255425183115"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row8184164615425"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p19184124617425"><a name="p19184124617425"></a><a name="p19184124617425"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1510053732411"><a name="p1510053732411"></a><a name="p1510053732411"></a>BMS.0012</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1184134619421"><a name="p1184134619421"></a><a name="p1184134619421"></a>Insufficient IP addresses in the selected subnet.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p15188144644216"><a name="p15188144644216"></a><a name="p15188144644216"></a>The number of IP addresses in the selected subnet[%s] is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p10188146154220"><a name="p10188146154220"></a><a name="p10188146154220"></a>Check whether the IP addresses of the subnet are used up.</p>
</td>
</tr>
<tr id="row240019166262"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p134001816112617"><a name="p134001816112617"></a><a name="p134001816112617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1940112165262"><a name="p1940112165262"></a><a name="p1940112165262"></a>BMS.0013</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p114011116192617"><a name="p114011116192617"></a><a name="p114011116192617"></a>Failed to query the port.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p94011916162619"><a name="p94011916162619"></a><a name="p94011916162619"></a>Fail to query ports by subnet [%s], reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1140161617260"><a name="p1140161617260"></a><a name="p1140161617260"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row95761222102614"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p15761222172619"><a name="p15761222172619"></a><a name="p15761222172619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p15577132262610"><a name="p15577132262610"></a><a name="p15577132262610"></a>BMS.0014</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p357742216265"><a name="p357742216265"></a><a name="p357742216265"></a>IP address conflict.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p155771622132617"><a name="p155771622132617"></a><a name="p155771622132617"></a>The specified IP address conflicts with an existing IP address in subnet[%s].</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p10577152212614"><a name="p10577152212614"></a><a name="p10577152212614"></a>Modify the NIC IP address.</p>
</td>
</tr>
<tr id="row12808260265"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p38111260268"><a name="p38111260268"></a><a name="p38111260268"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p18811226202612"><a name="p18811226202612"></a><a name="p18811226202612"></a>BMS.0015</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p981152616267"><a name="p981152616267"></a><a name="p981152616267"></a>Failed to query the NIC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1281142612261"><a name="p1281142612261"></a><a name="p1281142612261"></a>Fail to query subnet, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p82134619117"><a name="p82134619117"></a><a name="p82134619117"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1733391919264"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1333317194265"><a name="p1333317194265"></a><a name="p1333317194265"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p16333101911268"><a name="p16333101911268"></a><a name="p16333101911268"></a>BMS.0017</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p14333111913267"><a name="p14333111913267"></a><a name="p14333111913267"></a>The EIP quota is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p33331119102620"><a name="p33331119102620"></a><a name="p33331119102620"></a>The number[%d] of EIPs has reached the maximum[%d] allowed. Apply for a higher quota and try again.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p9333161912614"><a name="p9333161912614"></a><a name="p9333161912614"></a>Apply for a higher EIP quota.</p>
</td>
</tr>
<tr id="row17872872610"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p128710862613"><a name="p128710862613"></a><a name="p128710862613"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p58717813267"><a name="p58717813267"></a><a name="p58717813267"></a>BMS.0218</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p198716832610"><a name="p198716832610"></a><a name="p198716832610"></a>Failed to create the order.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p88712820262"><a name="p88712820262"></a><a name="p88712820262"></a>Fail to create order, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p88719872612"><a name="p88719872612"></a><a name="p88719872612"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1079015020266"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1379016012614"><a name="p1379016012614"></a><a name="p1379016012614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1679017012262"><a name="p1679017012262"></a><a name="p1679017012262"></a>BMS.0018</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p6790130112614"><a name="p6790130112614"></a><a name="p6790130112614"></a>Invalid request parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p19791135925112"><a name="p19791135925112"></a><a name="p19791135925112"></a>Request parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p18507553132613"><a name="p18507553132613"></a><a name="p18507553132613"></a>Modify the request parameters based on the returned error message.</p>
</td>
</tr>
<tr id="row1381514115262"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p148150111261"><a name="p148150111261"></a><a name="p148150111261"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1681591111268"><a name="p1681591111268"></a><a name="p1681591111268"></a>BMS.0019</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1070113415215"><a name="p1070113415215"></a><a name="p1070113415215"></a>Invalid NIC parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p19815411112615"><a name="p19815411112615"></a><a name="p19815411112615"></a>publicIp parameter is illegal, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p17815161118261"><a name="p17815161118261"></a><a name="p17815161118261"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row68671232261"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p286717316269"><a name="p286717316269"></a><a name="p286717316269"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p0867133122620"><a name="p0867133122620"></a><a name="p0867133122620"></a>BMS.0021</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p20867203102618"><a name="p20867203102618"></a><a name="p20867203102618"></a>The flavor is invalid for creating the <span id="text151741414161216"><a name="text151741414161216"></a><a name="text151741414161216"></a>BMS</span><span id="text14174101411212"><a name="text14174101411212"></a><a name="text14174101411212"></a></span>. Select another flavor.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p88678332618"><a name="p88678332618"></a><a name="p88678332618"></a>Flavor parameter is illegal, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1786743132616"><a name="p1786743132616"></a><a name="p1786743132616"></a>Select a valid flavor.</p>
</td>
</tr>
<tr id="row15660195810503"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p7718189499"><a name="p7718189499"></a><a name="p7718189499"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p3718158194910"><a name="p3718158194910"></a><a name="p3718158194910"></a>BMS.0022</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p124421525104915"><a name="p124421525104915"></a><a name="p124421525104915"></a>Invalid request parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p389416145214"><a name="p389416145214"></a><a name="p389416145214"></a>Request parameter is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1544252515499"><a name="p1544252515499"></a><a name="p1544252515499"></a>Modify the request parameters based on the returned error message.</p>
</td>
</tr>
<tr id="row1969210596259"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p14692059152518"><a name="p14692059152518"></a><a name="p14692059152518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p126921459112511"><a name="p126921459112511"></a><a name="p126921459112511"></a>BMS.0023</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p10692659192513"><a name="p10692659192513"></a><a name="p10692659192513"></a>Failed to query the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1669225952517"><a name="p1669225952517"></a><a name="p1669225952517"></a>Fail to query limits, reason: %s</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1769217593258"><a name="p1769217593258"></a><a name="p1769217593258"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row7753183055311"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p147531530185313"><a name="p147531530185313"></a><a name="p147531530185313"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1575403085310"><a name="p1575403085310"></a><a name="p1575403085310"></a>BMS.0025</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p9754173025311"><a name="p9754173025311"></a><a name="p9754173025311"></a>The number of <span id="text15998619151215"><a name="text15998619151215"></a><a name="text15998619151215"></a>BMS</span><span id="text1399881971219"><a name="text1399881971219"></a><a name="text1399881971219"></a></span>s exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p3754143045314"><a name="p3754143045314"></a><a name="p3754143045314"></a>The number of cloud servers has reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p775453095310"><a name="p775453095310"></a><a name="p775453095310"></a>Apply for a higher quota.</p>
</td>
</tr>
<tr id="row27431934145314"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1743203417539"><a name="p1743203417539"></a><a name="p1743203417539"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p4743193414533"><a name="p4743193414533"></a><a name="p4743193414533"></a>BMS.0026</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p43175139415"><a name="p43175139415"></a><a name="p43175139415"></a>The number of <span id="text10777521181211"><a name="text10777521181211"></a><a name="text10777521181211"></a>BMS</span><span id="text5777192151217"><a name="text5777192151217"></a><a name="text5777192151217"></a></span> CPUs exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p574315344531"><a name="p574315344531"></a><a name="p574315344531"></a>The number of CPU cores used by all cloud servers has reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p9537310171914"><a name="p9537310171914"></a><a name="p9537310171914"></a>Apply for a higher quota.</p>
</td>
</tr>
<tr id="row1611512273539"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p181151927165313"><a name="p181151927165313"></a><a name="p181151927165313"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p81158273536"><a name="p81158273536"></a><a name="p81158273536"></a>BMS.0027</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p48381113646"><a name="p48381113646"></a><a name="p48381113646"></a>The <span id="text1573752314121"><a name="text1573752314121"></a><a name="text1573752314121"></a>BMS</span><span id="text1673762316128"><a name="text1673762316128"></a><a name="text1673762316128"></a></span> memory exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1711518272530"><a name="p1711518272530"></a><a name="p1711518272530"></a>The memory space used by all cloud servers has reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p16122201101917"><a name="p16122201101917"></a><a name="p16122201101917"></a>Apply for a higher quota.</p>
</td>
</tr>
<tr id="row1270532365315"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p270542385319"><a name="p270542385319"></a><a name="p270542385319"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p10705523165319"><a name="p10705523165319"></a><a name="p10705523165319"></a>BMS.0028</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1839194310185"><a name="p1839194310185"></a><a name="p1839194310185"></a>The number of <span id="text1082119250127"><a name="text1082119250127"></a><a name="text1082119250127"></a>BMS</span><span id="text15821625151211"><a name="text15821625151211"></a><a name="text15821625151211"></a></span>s and that of CPUs exceed the quotas.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p15705102385316"><a name="p15705102385316"></a><a name="p15705102385316"></a>The number of CPU cores used by all cloud servers and that of cloud servers have reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1814161116199"><a name="p1814161116199"></a><a name="p1814161116199"></a>Apply for a higher quota.</p>
</td>
</tr>
<tr id="row0207165534"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p620161616537"><a name="p620161616537"></a><a name="p620161616537"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p420191612534"><a name="p420191612534"></a><a name="p420191612534"></a>BMS.0029</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p31364341342"><a name="p31364341342"></a><a name="p31364341342"></a>The number of <span id="text671112715122"><a name="text671112715122"></a><a name="text671112715122"></a>BMS</span><span id="text87111327181210"><a name="text87111327181210"></a><a name="text87111327181210"></a></span>s and the memory exceed the quotas.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p162071655311"><a name="p162071655311"></a><a name="p162071655311"></a>The memory space used by all cloud servers and the number of cloud servers have reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p14011912151913"><a name="p14011912151913"></a><a name="p14011912151913"></a>Apply for a higher quota.</p>
</td>
</tr>
<tr id="row35211619205314"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p19521151917538"><a name="p19521151917538"></a><a name="p19521151917538"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1852121913536"><a name="p1852121913536"></a><a name="p1852121913536"></a>BMS.0030</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1357153419414"><a name="p1357153419414"></a><a name="p1357153419414"></a>The <span id="text1297513019122"><a name="text1297513019122"></a><a name="text1297513019122"></a>BMS</span><span id="text0975193081219"><a name="text0975193081219"></a><a name="text0975193081219"></a></span> memory and the number of CPUs exceed the quotas.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p16521419125318"><a name="p16521419125318"></a><a name="p16521419125318"></a>The memory space and number of CPU cores used by all cloud servers have reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p106851713181913"><a name="p106851713181913"></a><a name="p106851713181913"></a>Apply for a higher quota.</p>
</td>
</tr>
<tr id="row1263617765312"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1063637125314"><a name="p1063637125314"></a><a name="p1063637125314"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p5636571532"><a name="p5636571532"></a><a name="p5636571532"></a>BMS.0031</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p4433453161818"><a name="p4433453161818"></a><a name="p4433453161818"></a>The number of <span id="text795510326126"><a name="text795510326126"></a><a name="text795510326126"></a>BMS</span><span id="text109551632161219"><a name="text109551632161219"></a><a name="text109551632161219"></a></span>s, the number of CPUs, and the memory exceed the quotas.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p56361274531"><a name="p56361274531"></a><a name="p56361274531"></a>The number of cloud servers, the memory space used by all cloud servers, and the number of CPU cores used by all cloud servers have reached the maximum allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p11396141471918"><a name="p11396141471918"></a><a name="p11396141471918"></a>Apply for a higher quota.</p>
</td>
</tr>
<tr id="row1379862145310"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1679819216537"><a name="p1679819216537"></a><a name="p1679819216537"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p2798821530"><a name="p2798821530"></a><a name="p2798821530"></a>BMS.0032</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1697717362268"><a name="p1697717362268"></a><a name="p1697717362268"></a>Contact the administrator to apply for a <span id="text7418373127"><a name="text7418373127"></a><a name="text7418373127"></a>BMS</span><span id="text1541537111214"><a name="text1541537111214"></a><a name="text1541537111214"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1979816285310"><a name="p1979816285310"></a><a name="p1979816285310"></a>Token check fail.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1879811217535"><a name="p1879811217535"></a><a name="p1879811217535"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row7640191169"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p36421991614"><a name="p36421991614"></a><a name="p36421991614"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1564289765"><a name="p1564289765"></a><a name="p1564289765"></a>BMS.0033</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1489914715288"><a name="p1489914715288"></a><a name="p1489914715288"></a>You do not have operation rights. Contact the administrator.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1864215912611"><a name="p1864215912611"></a><a name="p1864215912611"></a>Fail to check roles, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p13642797611"><a name="p13642797611"></a><a name="p13642797611"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row424519278113"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p12456278111"><a name="p12456278111"></a><a name="p12456278111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p17245827141117"><a name="p17245827141117"></a><a name="p17245827141117"></a>BMS.0034</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p16245132711114"><a name="p16245132711114"></a><a name="p16245132711114"></a>Currently, <span id="text14474134013125"><a name="text14474134013125"></a><a name="text14474134013125"></a>BMS</span><span id="text04741340171213"><a name="text04741340171213"></a><a name="text04741340171213"></a></span>s cannot be automatically provisioned.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p112454275114"><a name="p112454275114"></a><a name="p112454275114"></a>Not support create Bare Metal Server.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p11245227131112"><a name="p11245227131112"></a><a name="p11245227131112"></a>This operation is not supported.</p>
</td>
</tr>
<tr id="row16319160610"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1269013614152"><a name="p1269013614152"></a><a name="p1269013614152"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p156311716567"><a name="p156311716567"></a><a name="p156311716567"></a>BMS.0047</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p16631201610610"><a name="p16631201610610"></a><a name="p16631201610610"></a>Invalid system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1563112163618"><a name="p1563112163618"></a><a name="p1563112163618"></a>Root volume is illegal, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p729832813394"><a name="p729832813394"></a><a name="p729832813394"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1030914518615"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1020797151513"><a name="p1020797151513"></a><a name="p1020797151513"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p130916514619"><a name="p130916514619"></a><a name="p130916514619"></a>BMS.0049</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1030917514620"><a name="p1030917514620"></a><a name="p1030917514620"></a>Failed to query <strong id="b842352706165036"><a name="b842352706165036"></a><a name="b842352706165036"></a>key_name</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p33091751610"><a name="p33091751610"></a><a name="p33091751610"></a>Query keypair fail, reason is: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p103093511615"><a name="p103093511615"></a><a name="p103093511615"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1374319614494"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p57431762493"><a name="p57431762493"></a><a name="p57431762493"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p147438634920"><a name="p147438634920"></a><a name="p147438634920"></a>BMS.0102</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p12743065499"><a name="p12743065499"></a><a name="p12743065499"></a>This image does not support volume attaching.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1774311654912"><a name="p1774311654912"></a><a name="p1774311654912"></a>The image not support attach volume.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p07431668498"><a name="p07431668498"></a><a name="p07431668498"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row78666919551"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p11866399559"><a name="p11866399559"></a><a name="p11866399559"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1686614912552"><a name="p1686614912552"></a><a name="p1686614912552"></a>BMS.0103</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1986616915554"><a name="p1986616915554"></a><a name="p1986616915554"></a>The disk does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p8866399553"><a name="p8866399553"></a><a name="p8866399553"></a>Attach volume %s fail, volume info is null.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p10866799552"><a name="p10866799552"></a><a name="p10866799552"></a>Check whether the disk information is correct.</p>
</td>
</tr>
<tr id="row884617172161"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p138461717201619"><a name="p138461717201619"></a><a name="p138461717201619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p12846111751614"><a name="p12846111751614"></a><a name="p12846111751614"></a>BMS.0104</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p188461117151615"><a name="p188461117151615"></a><a name="p188461117151615"></a>The data volume cannot be attached to the mount point of the system volume.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1884661720167"><a name="p1884661720167"></a><a name="p1884661720167"></a>Attach volume %s fail, data volume can not attach in root volume device.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p784618171169"><a name="p784618171169"></a><a name="p784618171169"></a>Select another mount point.</p>
</td>
</tr>
<tr id="row491112222614"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p20911152172615"><a name="p20911152172615"></a><a name="p20911152172615"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1911192182615"><a name="p1911192182615"></a><a name="p1911192182615"></a>BMS.0105</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1191192112613"><a name="p1191192112613"></a><a name="p1191192112613"></a>The mount point is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p391112215261"><a name="p391112215261"></a><a name="p391112215261"></a>Attach volume %s fail, device is illegal.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p115102432714"><a name="p115102432714"></a><a name="p115102432714"></a>Check whether the mount point is valid.</p>
</td>
</tr>
<tr id="row45681259161816"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p656817597188"><a name="p656817597188"></a><a name="p656817597188"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p4568145914184"><a name="p4568145914184"></a><a name="p4568145914184"></a>BMS.0106</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p8568115913185"><a name="p8568115913185"></a><a name="p8568115913185"></a>The AZ of data disks is different from that of the <span id="text8908145161212"><a name="text8908145161212"></a><a name="text8908145161212"></a>BMS</span><span id="text1490817456121"><a name="text1490817456121"></a><a name="text1490817456121"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1856875991816"><a name="p1856875991816"></a><a name="p1856875991816"></a>Attach volume %s fail, volume's az is not equal with server's az.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p4568459171819"><a name="p4568459171819"></a><a name="p4568459171819"></a>Ensure that the AZ of data disks is the same as that of the <span id="text17449748161219"><a name="text17449748161219"></a><a name="text17449748161219"></a>BMS</span><span id="text1844984861218"><a name="text1844984861218"></a><a name="text1844984861218"></a></span>.</p>
</td>
</tr>
<tr id="row20310194131116"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p11310141101117"><a name="p11310141101117"></a><a name="p11310141101117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p53101541121111"><a name="p53101541121111"></a><a name="p53101541121111"></a>BMS.0108</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p19310134161111"><a name="p19310134161111"></a><a name="p19310134161111"></a>The system disk does not match the <span id="text12779195519122"><a name="text12779195519122"></a><a name="text12779195519122"></a>BMS</span><span id="text2779125517126"><a name="text2779125517126"></a><a name="text2779125517126"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p20310241131115"><a name="p20310241131115"></a><a name="p20310241131115"></a>Attach volume %s fail, root volume is not match with vm, do not change image.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p2310184115119"><a name="p2310184115119"></a><a name="p2310184115119"></a>Attach a matching system disk to the <span id="text11233553181211"><a name="text11233553181211"></a><a name="text11233553181211"></a>BMS</span><span id="text202337533125"><a name="text202337533125"></a><a name="text202337533125"></a></span>.</p>
</td>
</tr>
<tr id="row118411343113414"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p168421643173412"><a name="p168421643173412"></a><a name="p168421643173412"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1842114363414"><a name="p1842114363414"></a><a name="p1842114363414"></a>BMS.0111</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1684244323411"><a name="p1684244323411"></a><a name="p1684244323411"></a>Failed to verify the password injection method.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p10842124319347"><a name="p10842124319347"></a><a name="p10842124319347"></a>Password injection method verification failed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p10843543113417"><a name="p10843543113417"></a><a name="p10843543113417"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row39942029104516"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1499482911450"><a name="p1499482911450"></a><a name="p1499482911450"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1999422994518"><a name="p1999422994518"></a><a name="p1999422994518"></a>BMS.1001</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1899482910453"><a name="p1899482910453"></a><a name="p1899482910453"></a>This operation can be performed only when the <span id="text9364105901214"><a name="text9364105901214"></a><a name="text9364105901214"></a>BMS</span><span id="text20364115941219"><a name="text20364115941219"></a><a name="text20364115941219"></a></span> is in running or stopped.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p8994929154513"><a name="p8994929154513"></a><a name="p8994929154513"></a>Volume can only be attached when sever %s stopped or active.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p117764919465"><a name="p117764919465"></a><a name="p117764919465"></a>Try again later or contact technical support.</p>
</td>
</tr>
<tr id="row42112310515"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p132110316511"><a name="p132110316511"></a><a name="p132110316511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p19218319515"><a name="p19218319515"></a><a name="p19218319515"></a>BMS.1002</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p4216365117"><a name="p4216365117"></a><a name="p4216365117"></a>The number of data disks that can be attached to the <span id="text461616201319"><a name="text461616201319"></a><a name="text461616201319"></a>BMS</span><span id="text26161227134"><a name="text26161227134"></a><a name="text26161227134"></a></span> exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p4211738517"><a name="p4211738517"></a><a name="p4211738517"></a>Attach volume fail, server %s attchment num over limit.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p6217395119"><a name="p6217395119"></a><a name="p6217395119"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row4207174810566"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p132081348105616"><a name="p132081348105616"></a><a name="p132081348105616"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p192091348155617"><a name="p192091348155617"></a><a name="p192091348155617"></a>BMS.1003</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p3209144815615"><a name="p3209144815615"></a><a name="p3209144815615"></a>The disk status is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1120964865616"><a name="p1120964865616"></a><a name="p1120964865616"></a>Attach shareable volume %s fail, volume status is %s, not available or inuse.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p720994819565"><a name="p720994819565"></a><a name="p720994819565"></a>Check whether the disk is in attached or other unavailable status.</p>
</td>
</tr>
<tr id="row37139275"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p37594715"><a name="p37594715"></a><a name="p37594715"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1971591176"><a name="p1971591176"></a><a name="p1971591176"></a>BMS.1004</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p2076910714"><a name="p2076910714"></a><a name="p2076910714"></a>The number of shared data disks that can be attached to the <span id="text187723781316"><a name="text187723781316"></a><a name="text187723781316"></a>BMS</span><span id="text1277257161316"><a name="text1277257161316"></a><a name="text1277257161316"></a></span> exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p375965012712"><a name="p375965012712"></a><a name="p375965012712"></a>Attach shareable volume %s fail, volume status is %s, not available or inuse.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1871691074"><a name="p1871691074"></a><a name="p1871691074"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row108246354425"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p4824143519427"><a name="p4824143519427"></a><a name="p4824143519427"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p11824635124215"><a name="p11824635124215"></a><a name="p11824635124215"></a>BMS.1006</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p782414353423"><a name="p782414353423"></a><a name="p782414353423"></a>The running status of the <span id="text103401210121320"><a name="text103401210121320"></a><a name="text103401210121320"></a>BMS</span><span id="text18340310121313"><a name="text18340310121313"></a><a name="text18340310121313"></a></span> cannot be obtained.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p382413355426"><a name="p382413355426"></a><a name="p382413355426"></a>Server %s info is null or its status or its metadata is null.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p128241235144211"><a name="p128241235144211"></a><a name="p128241235144211"></a>Try again later or contact technical support.</p>
</td>
</tr>
<tr id="row1978810156534"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p197881815205314"><a name="p197881815205314"></a><a name="p197881815205314"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p19788151565311"><a name="p19788151565311"></a><a name="p19788151565311"></a>BMS.1007</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p13788111595319"><a name="p13788111595319"></a><a name="p13788111595319"></a>Failed to call the API.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p4788201525318"><a name="p4788201525318"></a><a name="p4788201525318"></a>Calling interface failed</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p678812159539"><a name="p678812159539"></a><a name="p678812159539"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row82811248214"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p122818472115"><a name="p122818472115"></a><a name="p122818472115"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1228118412115"><a name="p1228118412115"></a><a name="p1228118412115"></a>BMS.1008</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p38821246182718"><a name="p38821246182718"></a><a name="p38821246182718"></a>The disk type does not match the BMS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p728114442111"><a name="p728114442111"></a><a name="p728114442111"></a>The server[%s] is not HANA server, volume[%s] is not match with server.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1228111482112"><a name="p1228111482112"></a><a name="p1228111482112"></a>Check whether the disk type matches the BMS or contact the technical support.</p>
</td>
</tr>
<tr id="row38512166015"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p88513162002"><a name="p88513162002"></a><a name="p88513162002"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1485131613016"><a name="p1485131613016"></a><a name="p1485131613016"></a>BMS.1009</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p208519161602"><a name="p208519161602"></a><a name="p208519161602"></a>The data disk has been attached to the <span id="text6857141414137"><a name="text6857141414137"></a><a name="text6857141414137"></a>BMS</span><span id="text68570144132"><a name="text68570144132"></a><a name="text68570144132"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p138517161015"><a name="p138517161015"></a><a name="p138517161015"></a>Attach shareable volume %s fail, volume status is %s, the volume has been attached to the server.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p188515161507"><a name="p188515161507"></a><a name="p188515161507"></a>Select another data disk.</p>
</td>
</tr>
<tr id="row42771143125810"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p8277243105814"><a name="p8277243105814"></a><a name="p8277243105814"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p15277104310583"><a name="p15277104310583"></a><a name="p15277104310583"></a>BMS.1011</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p627718439580"><a name="p627718439580"></a><a name="p627718439580"></a>The data disk is being attached.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p11277164315583"><a name="p11277164315583"></a><a name="p11277164315583"></a>Attach shareable volume %s fail, volume status is %s, not available or inuse.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p7248204425911"><a name="p7248204425911"></a><a name="p7248204425911"></a>Do not repeatedly attach the data disk.</p>
</td>
</tr>
<tr id="row139381418181520"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p79386183150"><a name="p79386183150"></a><a name="p79386183150"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1593881851516"><a name="p1593881851516"></a><a name="p1593881851516"></a>BMS.3001</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p19381218141512"><a name="p19381218141512"></a><a name="p19381218141512"></a>Failed to query the security group or subnet.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p13938161871518"><a name="p13938161871518"></a><a name="p13938161871518"></a>Query security group failed: %s.</p>
<p id="p18197275374"><a name="p18197275374"></a><a name="p18197275374"></a>or</p>
<p id="p162492811371"><a name="p162492811371"></a><a name="p162492811371"></a>Query vpcId for subnet failed: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p2939518111513"><a name="p2939518111513"></a><a name="p2939518111513"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row521995351910"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p621945312194"><a name="p621945312194"></a><a name="p621945312194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p142198534196"><a name="p142198534196"></a><a name="p142198534196"></a>BMS.3011</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p9219253121913"><a name="p9219253121913"></a><a name="p9219253121913"></a>System error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p13219253101915"><a name="p13219253101915"></a><a name="p13219253101915"></a>Decoded token is null.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p0219753171915"><a name="p0219753171915"></a><a name="p0219753171915"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row2579165111155"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p185791951151513"><a name="p185791951151513"></a><a name="p185791951151513"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p6579851171514"><a name="p6579851171514"></a><a name="p6579851171514"></a>BMS.3025</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p4579551151511"><a name="p4579551151511"></a><a name="p4579551151511"></a>The EVS disk type is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p3579165191518"><a name="p3579165191518"></a><a name="p3579165191518"></a>Not support create shareable data volumes.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p557915191519"><a name="p557915191519"></a><a name="p557915191519"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row2091234820210"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p119121485210"><a name="p119121485210"></a><a name="p119121485210"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p17912194815218"><a name="p17912194815218"></a><a name="p17912194815218"></a>BMS.3035</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1491214486212"><a name="p1491214486212"></a><a name="p1491214486212"></a>No matching disk is found for the <span id="text1046192061317"><a name="text1046192061317"></a><a name="text1046192061317"></a>BMS</span><span id="text17465201131"><a name="text17465201131"></a><a name="text17465201131"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p591213481217"><a name="p591213481217"></a><a name="p591213481217"></a>Attach volume fail: the bmsid [%s] in volume metadata is not the same with bmsid [%s] in url.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p209121548229"><a name="p209121548229"></a><a name="p209121548229"></a>Ensure that the disk matches the <span id="text78131322111314"><a name="text78131322111314"></a><a name="text78131322111314"></a>BMS</span><span id="text28131622111320"><a name="text28131622111320"></a><a name="text28131622111320"></a></span> or contact technical support.</p>
</td>
</tr>
<tr id="row73291247111516"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1432916473157"><a name="p1432916473157"></a><a name="p1432916473157"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p732913474156"><a name="p732913474156"></a><a name="p732913474156"></a>BMS.3039</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p63290472155"><a name="p63290472155"></a><a name="p63290472155"></a>Failed to verify password complexity.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p143291247181516"><a name="p143291247181516"></a><a name="p143291247181516"></a>The password is illegal, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p103296479151"><a name="p103296479151"></a><a name="p103296479151"></a>See the password rules.</p>
</td>
</tr>
<tr id="row161401442131518"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p214034211154"><a name="p214034211154"></a><a name="p214034211154"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p7140124218159"><a name="p7140124218159"></a><a name="p7140124218159"></a>BMS.3040</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p171405422150"><a name="p171405422150"></a><a name="p171405422150"></a>Failed to query the VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p5140242191517"><a name="p5140242191517"></a><a name="p5140242191517"></a>The vpcId[%s] is invalid or not-existing.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p131876663613"><a name="p131876663613"></a><a name="p131876663613"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row5241143418150"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p18241123471519"><a name="p18241123471519"></a><a name="p18241123471519"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p9241634181516"><a name="p9241634181516"></a><a name="p9241634181516"></a>BMS.0201</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p11212184625318"><a name="p11212184625318"></a><a name="p11212184625318"></a>The parameters for creating the <span id="text77508264137"><a name="text77508264137"></a><a name="text77508264137"></a>BMS</span><span id="text20750122691313"><a name="text20750122691313"></a><a name="text20750122691313"></a></span> are incorrectly configured.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1024163411519"><a name="p1024163411519"></a><a name="p1024163411519"></a>Fail to check the baremetal server params, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p167253416413"><a name="p167253416413"></a><a name="p167253416413"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row10759163671710"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p17759193611174"><a name="p17759193611174"></a><a name="p17759193611174"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p127591136191717"><a name="p127591136191717"></a><a name="p127591136191717"></a>BMS.0202</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p8325133124212"><a name="p8325133124212"></a><a name="p8325133124212"></a>The data disk type is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p575918368174"><a name="p575918368174"></a><a name="p575918368174"></a>All volumes must be in same type.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p4759036161710"><a name="p4759036161710"></a><a name="p4759036161710"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1856463013155"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p4564133031512"><a name="p4564133031512"></a><a name="p4564133031512"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p9564123021519"><a name="p9564123021519"></a><a name="p9564123021519"></a>BMS.0203</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p2564730111520"><a name="p2564730111520"></a><a name="p2564730111520"></a>Parameter <strong id="b1151582424210"><a name="b1151582424210"></a><a name="b1151582424210"></a>Volume</strong> is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1056413011520"><a name="p1056413011520"></a><a name="p1056413011520"></a>Volume is illegal, %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p56941827104319"><a name="p56941827104319"></a><a name="p56941827104319"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1696293215180"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p7962173231818"><a name="p7962173231818"></a><a name="p7962173231818"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1796253211818"><a name="p1796253211818"></a><a name="p1796253211818"></a>BMS.0204</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p296273211820"><a name="p296273211820"></a><a name="p296273211820"></a>The number of data disks exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p896293211186"><a name="p896293211186"></a><a name="p896293211186"></a>The num of datavolume is illegal, the num is %d, max num allow is %d.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p39621632171816"><a name="p39621632171816"></a><a name="p39621632171816"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row129941737121815"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p16994133713184"><a name="p16994133713184"></a><a name="p16994133713184"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1994113717182"><a name="p1994113717182"></a><a name="p1994113717182"></a>BMS.0205</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p899463718184"><a name="p899463718184"></a><a name="p899463718184"></a>The <span id="text177363012138"><a name="text177363012138"></a><a name="text177363012138"></a>BMS</span><span id="text4731730111311"><a name="text4731730111311"></a><a name="text4731730111311"></a></span> quantity is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p399473751810"><a name="p399473751810"></a><a name="p399473751810"></a>The number of baremetal server is out of range for one quest.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p13994143716189"><a name="p13994143716189"></a><a name="p13994143716189"></a>Change the <span id="text14492332111315"><a name="text14492332111315"></a><a name="text14492332111315"></a>BMS</span><span id="text1649210320134"><a name="text1649210320134"></a><a name="text1649210320134"></a></span> quantity.</p>
</td>
</tr>
<tr id="row13283139161920"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p42830396198"><a name="p42830396198"></a><a name="p42830396198"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p152836391195"><a name="p152836391195"></a><a name="p152836391195"></a>BMS.0206</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1828320397197"><a name="p1828320397197"></a><a name="p1828320397197"></a>Invalid name.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p8283639201919"><a name="p8283639201919"></a><a name="p8283639201919"></a>The length of baremetal server name[%s] is %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p102831539131911"><a name="p102831539131911"></a><a name="p102831539131911"></a>Change the name as required.</p>
</td>
</tr>
<tr id="row107543456197"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p375610457194"><a name="p375610457194"></a><a name="p375610457194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p67561845181914"><a name="p67561845181914"></a><a name="p67561845181914"></a>BMS.0207</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p76758314472"><a name="p76758314472"></a><a name="p76758314472"></a>No IP address can be specified when <span id="text67101734151314"><a name="text67101734151314"></a><a name="text67101734151314"></a>BMS</span><span id="text1710183413131"><a name="text1710183413131"></a><a name="text1710183413131"></a></span>s are created in a batch.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1775644516191"><a name="p1775644516191"></a><a name="p1775644516191"></a>VPC is illegal, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p12756174519196"><a name="p12756174519196"></a><a name="p12756174519196"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row194284254153"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p5428112531518"><a name="p5428112531518"></a><a name="p5428112531518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1642819253155"><a name="p1642819253155"></a><a name="p1642819253155"></a>BMS.0208</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1136963718484"><a name="p1136963718484"></a><a name="p1136963718484"></a>Failed to query the AZ.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p721492691711"><a name="p721492691711"></a><a name="p721492691711"></a>Fail to get RegionInfo by tenant [%s], reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p14223041184919"><a name="p14223041184919"></a><a name="p14223041184919"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row11521629191910"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1652192912194"><a name="p1652192912194"></a><a name="p1652192912194"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p7522297193"><a name="p7522297193"></a><a name="p7522297193"></a>BMS.0210</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1230162404918"><a name="p1230162404918"></a><a name="p1230162404918"></a>The length of the injected data exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p85222918199"><a name="p85222918199"></a><a name="p85222918199"></a>The size of userdata [%d] is over quota limits [%d].</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1521329181914"><a name="p1521329181914"></a><a name="p1521329181914"></a>Modify the injected data.</p>
</td>
</tr>
<tr id="row14416133151715"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p124165332177"><a name="p124165332177"></a><a name="p124165332177"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p10416103311713"><a name="p10416103311713"></a><a name="p10416103311713"></a>BMS.0211</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1441617339171"><a name="p1441617339171"></a><a name="p1441617339171"></a>Invalid key.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p16416193316178"><a name="p16416193316178"></a><a name="p16416193316178"></a>The image platfrom is [%s], support publicKey, resion: the publicKey is illegal, null is not allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p8416153381719"><a name="p8416153381719"></a><a name="p8416153381719"></a>Select a valid key.</p>
</td>
</tr>
<tr id="row957763411408"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p10577113419401"><a name="p10577113419401"></a><a name="p10577113419401"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p19577234184015"><a name="p19577234184015"></a><a name="p19577234184015"></a>BMS.0114</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1257753410409"><a name="p1257753410409"></a><a name="p1257753410409"></a>The disk to be detached is not in the disk list of the <span id="text11659103961313"><a name="text11659103961313"></a><a name="text11659103961313"></a>BMS</span><span id="text17659153910137"><a name="text17659153910137"></a><a name="text17659153910137"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p11577434194015"><a name="p11577434194015"></a><a name="p11577434194015"></a>Volume %s is not in server %s attach volume list.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p157773410405"><a name="p157773410405"></a><a name="p157773410405"></a>Check whether the disk exists.</p>
</td>
</tr>
<tr id="row787602171713"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p208761521101714"><a name="p208761521101714"></a><a name="p208761521101714"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p924222917177"><a name="p924222917177"></a><a name="p924222917177"></a>BMS.0212</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p5521251112012"><a name="p5521251112012"></a><a name="p5521251112012"></a>The system is overloaded.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p6876132114174"><a name="p6876132114174"></a><a name="p6876132114174"></a>System is overloaded, please try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p11876221151716"><a name="p11876221151716"></a><a name="p11876221151716"></a>Try again later.</p>
</td>
</tr>
<tr id="row119141251711"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p10915127175"><a name="p10915127175"></a><a name="p10915127175"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p139111219175"><a name="p139111219175"></a><a name="p139111219175"></a>BMS.0213</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p091812101714"><a name="p091812101714"></a><a name="p091812101714"></a>Insufficient permission.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p3911212181718"><a name="p3911212181718"></a><a name="p3911212181718"></a>OBTAZ role verify fail: not allowed role.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p20910121173"><a name="p20910121173"></a><a name="p20910121173"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row3854121631711"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p158541316151713"><a name="p158541316151713"></a><a name="p158541316151713"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p7854111618171"><a name="p7854111618171"></a><a name="p7854111618171"></a>BMS.0214</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p785431661719"><a name="p785431661719"></a><a name="p785431661719"></a>Failed to query the NIC.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p12854141618178"><a name="p12854141618178"></a><a name="p12854141618178"></a>Query subnet[%s] failed: response is null.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p589015617537"><a name="p589015617537"></a><a name="p589015617537"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row17604122617188"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p106046268182"><a name="p106046268182"></a><a name="p106046268182"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p166041626121813"><a name="p166041626121813"></a><a name="p166041626121813"></a>BMS.0215</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p260413265181"><a name="p260413265181"></a><a name="p260413265181"></a>Failed to create the order.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p186042261180"><a name="p186042261180"></a><a name="p186042261180"></a>The response of inquiry order info is null or invalide.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p96049261186"><a name="p96049261186"></a><a name="p96049261186"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row12369112215188"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p136902210180"><a name="p136902210180"></a><a name="p136902210180"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1836912213187"><a name="p1836912213187"></a><a name="p1836912213187"></a>BMS.0216</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p3369122211819"><a name="p3369122211819"></a><a name="p3369122211819"></a>Failed to submit the order.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p103691222171813"><a name="p103691222171813"></a><a name="p103691222171813"></a>Submit order[%s] failed: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1136942261812"><a name="p1136942261812"></a><a name="p1136942261812"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row5229624122418"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p72297248249"><a name="p72297248249"></a><a name="p72297248249"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p62291924142410"><a name="p62291924142410"></a><a name="p62291924142410"></a>BMS.0217</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1322982416242"><a name="p1322982416242"></a><a name="p1322982416242"></a>Failed to verify metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p12612722145518"><a name="p12612722145518"></a><a name="p12612722145518"></a>Create server fail, reason: metaData is illegal.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p522917244249"><a name="p522917244249"></a><a name="p522917244249"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row43241952111014"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p183241352111018"><a name="p183241352111018"></a><a name="p183241352111018"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p2032535291012"><a name="p2032535291012"></a><a name="p2032535291012"></a>BMS.0222</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p14325165210108"><a name="p14325165210108"></a><a name="p14325165210108"></a>The primary NIC cannot be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p163259529108"><a name="p163259529108"></a><a name="p163259529108"></a>primary port can not be deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p9325852111019"><a name="p9325852111019"></a><a name="p9325852111019"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row7165154113536"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p016516414532"><a name="p016516414532"></a><a name="p016516414532"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p131656410534"><a name="p131656410534"></a><a name="p131656410534"></a>BMS.0223</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p20167541135316"><a name="p20167541135316"></a><a name="p20167541135316"></a>Currently, only SCSI disks are supported.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p716710411537"><a name="p716710411537"></a><a name="p716710411537"></a>Only SCSI disks are supported.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p2167341115317"><a name="p2167341115317"></a><a name="p2167341115317"></a>Select the SCSI disk type.</p>
</td>
</tr>
<tr id="row990502035017"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p129061120205018"><a name="p129061120205018"></a><a name="p129061120205018"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p19906102065010"><a name="p19906102065010"></a><a name="p19906102065010"></a>BMS.0039</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p890682015014"><a name="p890682015014"></a><a name="p890682015014"></a>The <span id="text1435554416134"><a name="text1435554416134"></a><a name="text1435554416134"></a>BMS</span><span id="text73552044181313"><a name="text73552044181313"></a><a name="text73552044181313"></a></span> has been shut down.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1190692045017"><a name="p1190692045017"></a><a name="p1190692045017"></a>Server is stopped, not allow to stop.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p2906220115020"><a name="p2906220115020"></a><a name="p2906220115020"></a>Do not stop the BMS again.</p>
</td>
</tr>
<tr id="row186178394509"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p9617193917505"><a name="p9617193917505"></a><a name="p9617193917505"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p15617939115016"><a name="p15617939115016"></a><a name="p15617939115016"></a>BMS.0040</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p176172039185020"><a name="p176172039185020"></a><a name="p176172039185020"></a>The <span id="text17872114521314"><a name="text17872114521314"></a><a name="text17872114521314"></a>BMS</span><span id="text1387254521313"><a name="text1387254521313"></a><a name="text1387254521313"></a></span> does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1361710393508"><a name="p1361710393508"></a><a name="p1361710393508"></a>The server is not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p961723955017"><a name="p961723955017"></a><a name="p961723955017"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row20600123116508"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1760153125013"><a name="p1760153125013"></a><a name="p1760153125013"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p16601931145010"><a name="p16601931145010"></a><a name="p16601931145010"></a>BMS.0035</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p46011731165012"><a name="p46011731165012"></a><a name="p46011731165012"></a>The <span id="text1163074714132"><a name="text1163074714132"></a><a name="text1163074714132"></a>BMS</span><span id="text9631204751313"><a name="text9631204751313"></a><a name="text9631204751313"></a></span> is being powered on and no other operations are allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p96011931145013"><a name="p96011931145013"></a><a name="p96011931145013"></a>Server is powering on, not allow to %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p4601103111502"><a name="p4601103111502"></a><a name="p4601103111502"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1437252914503"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p437262919503"><a name="p437262919503"></a><a name="p437262919503"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1837216297504"><a name="p1837216297504"></a><a name="p1837216297504"></a>BMS.0036</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1889010147015"><a name="p1889010147015"></a><a name="p1889010147015"></a>The <span id="text17584163582017"><a name="text17584163582017"></a><a name="text17584163582017"></a>BMS</span><span id="text25855357204"><a name="text25855357204"></a><a name="text25855357204"></a></span> is being powered off and no other operations are allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p637292955011"><a name="p637292955011"></a><a name="p637292955011"></a>Server is powering off, not allow to %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1737232975017"><a name="p1737232975017"></a><a name="p1737232975017"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row201701124155014"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p17170182495010"><a name="p17170182495010"></a><a name="p17170182495010"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p171708248509"><a name="p171708248509"></a><a name="p171708248509"></a>BMS.0038</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p81709243507"><a name="p81709243507"></a><a name="p81709243507"></a>The <span id="text758917523137"><a name="text758917523137"></a><a name="text758917523137"></a>BMS</span><span id="text1558985221319"><a name="text1558985221319"></a><a name="text1558985221319"></a></span> is running and cannot be started.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p71701424185015"><a name="p71701424185015"></a><a name="p71701424185015"></a>Server is running, not allow to start.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p917016243502"><a name="p917016243502"></a><a name="p917016243502"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1160114446522"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p16601144115217"><a name="p16601144115217"></a><a name="p16601144115217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p196013443520"><a name="p196013443520"></a><a name="p196013443520"></a>BMS.0037</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p983152813219"><a name="p983152813219"></a><a name="p983152813219"></a>The <span id="text8447165671314"><a name="text8447165671314"></a><a name="text8447165671314"></a>BMS</span><span id="text644718569136"><a name="text644718569136"></a><a name="text644718569136"></a></span> is being restarted and no other operations are allowed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p0601194425217"><a name="p0601194425217"></a><a name="p0601194425217"></a>Server is rebooting, not allow to %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p6601104417529"><a name="p6601104417529"></a><a name="p6601104417529"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row166414268501"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1066422675018"><a name="p1066422675018"></a><a name="p1066422675018"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p10664102610500"><a name="p10664102610500"></a><a name="p10664102610500"></a>BMS.0288</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p126642266506"><a name="p126642266506"></a><a name="p126642266506"></a>You do not have permissions to perform this operation.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p9664102612509"><a name="p9664102612509"></a><a name="p9664102612509"></a>Policy doesn't allow %s to be performed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p06641526175012"><a name="p06641526175012"></a><a name="p06641526175012"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1429882014811"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p6298420280"><a name="p6298420280"></a><a name="p6298420280"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1629832010811"><a name="p1629832010811"></a><a name="p1629832010811"></a>BMS.0290</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p162981820689"><a name="p162981820689"></a><a name="p162981820689"></a>The disk is not a shared disk and cannot be attached to multiple BMSs.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p142982201687"><a name="p142982201687"></a><a name="p142982201687"></a>Batch attach volume type must be sharable.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p629815206817"><a name="p629815206817"></a><a name="p629815206817"></a>Select a shared disk.</p>
</td>
</tr>
<tr id="row9102167719"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p91021766715"><a name="p91021766715"></a><a name="p91021766715"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p20102661073"><a name="p20102661073"></a><a name="p20102661073"></a>BMS.0071</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p15102126775"><a name="p15102126775"></a><a name="p15102126775"></a>If an EIP has been specified for creating the <span id="text04063221417"><a name="text04063221417"></a><a name="text04063221417"></a>BMS</span><span id="text6406627145"><a name="text6406627145"></a><a name="text6406627145"></a></span>, no other EIP can be created for the <span id="text14561718122313"><a name="text14561718122313"></a><a name="text14561718122313"></a>BMS</span><span id="text1563121816230"><a name="text1563121816230"></a><a name="text1563121816230"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p71021761876"><a name="p71021761876"></a><a name="p71021761876"></a>Using a existing eip and creating a new eip can't be used at the same time.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1310226671"><a name="p1310226671"></a><a name="p1310226671"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1773415468618"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p19734846369"><a name="p19734846369"></a><a name="p19734846369"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p67345461461"><a name="p67345461461"></a><a name="p67345461461"></a>BMS.0072</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p147341461061"><a name="p147341461061"></a><a name="p147341461061"></a>An EIP cannot be used to create multiple <span id="text1992294141412"><a name="text1992294141412"></a><a name="text1992294141412"></a>BMS</span><span id="text119229413146"><a name="text119229413146"></a><a name="text119229413146"></a></span>s.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p373416461265"><a name="p373416461265"></a><a name="p373416461265"></a>An existing EIP cannot be assigned to the ECSs created in batches.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1473415463620"><a name="p1473415463620"></a><a name="p1473415463620"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row243118441862"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p143154419610"><a name="p143154419610"></a><a name="p143154419610"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p343116443611"><a name="p343116443611"></a><a name="p343116443611"></a>BMS.0073</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1943154416611"><a name="p1943154416611"></a><a name="p1943154416611"></a>The bandwidth parameter is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p043112441964"><a name="p043112441964"></a><a name="p043112441964"></a>Bandwidth info in eip is null.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1843119441464"><a name="p1843119441464"></a><a name="p1843119441464"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1713813502068"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1113810501363"><a name="p1113810501363"></a><a name="p1113810501363"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p11138150868"><a name="p11138150868"></a><a name="p11138150868"></a>BMS.0074</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1913815020611"><a name="p1913815020611"></a><a name="p1913815020611"></a>The EIP extension parameter is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p413818501761"><a name="p413818501761"></a><a name="p413818501761"></a>Parameter exetendparam or chargingMode is null.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p61381350961"><a name="p61381350961"></a><a name="p61381350961"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row75961551364"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p7596955266"><a name="p7596955266"></a><a name="p7596955266"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p165966554617"><a name="p165966554617"></a><a name="p165966554617"></a>BMS.0075</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p12596125517617"><a name="p12596125517617"></a><a name="p12596125517617"></a>The bandwidth ID is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p14596135511610"><a name="p14596135511610"></a><a name="p14596135511610"></a>Bandwidth info in eip is null.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1116891710221"><a name="p1116891710221"></a><a name="p1116891710221"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row117491201372"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p47491301578"><a name="p47491301578"></a><a name="p47491301578"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1074914013713"><a name="p1074914013713"></a><a name="p1074914013713"></a>BMS.0077</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p19749701676"><a name="p19749701676"></a><a name="p19749701676"></a>Invalid bandwidth size.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1674930373"><a name="p1674930373"></a><a name="p1674930373"></a>PublicIp parameter is illegal, reason: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p774950078"><a name="p774950078"></a><a name="p774950078"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row261219531582"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p76126531085"><a name="p76126531085"></a><a name="p76126531085"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p061275313815"><a name="p061275313815"></a><a name="p061275313815"></a>BMS.0078</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p13612153983"><a name="p13612153983"></a><a name="p13612153983"></a>EIP quota is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p26129135012"><a name="p26129135012"></a><a name="p26129135012"></a>Shared bandwidth has been bound to %d EIPs, quota is %d.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p86121453685"><a name="p86121453685"></a><a name="p86121453685"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row135121951387"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p145121511089"><a name="p145121511089"></a><a name="p145121511089"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p151214516819"><a name="p151214516819"></a><a name="p151214516819"></a>BMS.0079</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p12513851981"><a name="p12513851981"></a><a name="p12513851981"></a>The EIP bandwidth type is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p18463109165210"><a name="p18463109165210"></a><a name="p18463109165210"></a>Specifies the bandwidth of the shared type and the id cannot be empty.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p82640425234"><a name="p82640425234"></a><a name="p82640425234"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row119061048982"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p290724820816"><a name="p290724820816"></a><a name="p290724820816"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p17907154816816"><a name="p17907154816816"></a><a name="p17907154816816"></a>BMS.0080</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p2090714489812"><a name="p2090714489812"></a><a name="p2090714489812"></a>The subnet status is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p254615915533"><a name="p254615915533"></a><a name="p254615915533"></a>Check subnet status failed.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1290717480812"><a name="p1290717480812"></a><a name="p1290717480812"></a>Check whether the subnet exists or whether it is in <strong id="b1933854619429"><a name="b1933854619429"></a><a name="b1933854619429"></a>ACTIVE</strong> state.</p>
</td>
</tr>
<tr id="row185081133165715"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1747743319571"><a name="p1747743319571"></a><a name="p1747743319571"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p14771233155710"><a name="p14771233155710"></a><a name="p14771233155710"></a>BMS.0297</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p94911933155711"><a name="p94911933155711"></a><a name="p94911933155711"></a>The submitted EVS disk order has not been paid. The EVS disk cannot be attached to or detached from the BMS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1287619231113"><a name="p1287619231113"></a><a name="p1287619231113"></a>Fail to attach volume[%s]: volume is locked.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p2491163312579"><a name="p2491163312579"></a><a name="p2491163312579"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row1740820213514"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p9408221852"><a name="p9408221852"></a><a name="p9408221852"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1940942115517"><a name="p1940942115517"></a><a name="p1940942115517"></a>BMS.0054</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p194091021252"><a name="p194091021252"></a><a name="p194091021252"></a>Failed to verify the capacity.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p164091921350"><a name="p164091921350"></a><a name="p164091921350"></a>Check capacity fail, the number of capacity is: [%d], and req num is: [%d].</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p34093211253"><a name="p34093211253"></a><a name="p34093211253"></a>The capacity is insufficient. Contact technical support.</p>
</td>
</tr>
<tr id="row18750113019127"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p10752530101219"><a name="p10752530101219"></a><a name="p10752530101219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1875293031213"><a name="p1875293031213"></a><a name="p1875293031213"></a>BMS.0055</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p8752130141212"><a name="p8752130141212"></a><a name="p8752130141212"></a>Failed to query the quota.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1575243041219"><a name="p1575243041219"></a><a name="p1575243041219"></a>Query capacity fail, Flavor id is [%s], reason: [%s].</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p20752103015128"><a name="p20752103015128"></a><a name="p20752103015128"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row203061910528"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p153141032105214"><a name="p153141032105214"></a><a name="p153141032105214"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p43071918529"><a name="p43071918529"></a><a name="p43071918529"></a>BMS.3037</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p330718965213"><a name="p330718965213"></a><a name="p330718965213"></a>Insufficient resources or failed to start the BMS.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p203076916525"><a name="p203076916525"></a><a name="p203076916525"></a>Insufficient resources or failed to start the BMS.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p676514231124"><a name="p676514231124"></a><a name="p676514231124"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row138391734155212"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1283918347525"><a name="p1283918347525"></a><a name="p1283918347525"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p9840183416521"><a name="p9840183416521"></a><a name="p9840183416521"></a>BMS.3004</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p88401134125218"><a name="p88401134125218"></a><a name="p88401134125218"></a>Failed to create the BMS due to an internal system error.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p78401134185210"><a name="p78401134185210"></a><a name="p78401134185210"></a>Failed to create the BMS due to an internal system error.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p38401234165211"><a name="p38401234165211"></a><a name="p38401234165211"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row163221015771"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p16271911496"><a name="p16271911496"></a><a name="p16271911496"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p432416159712"><a name="p432416159712"></a><a name="p432416159712"></a>BMS.3005</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p83241715471"><a name="p83241715471"></a><a name="p83241715471"></a>Failed to create the port.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p16324181514719"><a name="p16324181514719"></a><a name="p16324181514719"></a>Failed to create the port.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p16324161513714"><a name="p16324161513714"></a><a name="p16324161513714"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row8806121714719"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p192449122918"><a name="p192449122918"></a><a name="p192449122918"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p148074172077"><a name="p148074172077"></a><a name="p148074172077"></a>BMS.3033</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p16807151712710"><a name="p16807151712710"></a><a name="p16807151712710"></a>Failed to create the system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p6807101713720"><a name="p6807101713720"></a><a name="p6807101713720"></a>Failed to create the system disk.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p12807141715715"><a name="p12807141715715"></a><a name="p12807141715715"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1815918712"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p198285123911"><a name="p198285123911"></a><a name="p198285123911"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1782593713"><a name="p1782593713"></a><a name="p1782593713"></a>BMS.3029</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p19865915711"><a name="p19865915711"></a><a name="p19865915711"></a>Failed to create the system disk. The disk status is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1875919712"><a name="p1875919712"></a><a name="p1875919712"></a>Failed to create the system disk. The disk status is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p18805920713"><a name="p18805920713"></a><a name="p18805920713"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row45602073815"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1082517131798"><a name="p1082517131798"></a><a name="p1082517131798"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p75605719819"><a name="p75605719819"></a><a name="p75605719819"></a>BMS.3006</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p165601673815"><a name="p165601673815"></a><a name="p165601673815"></a>Failed to assign the EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p1456011710811"><a name="p1456011710811"></a><a name="p1456011710811"></a>Failed to assign the floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p11560137881"><a name="p11560137881"></a><a name="p11560137881"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row164601314817"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p1134115141390"><a name="p1134115141390"></a><a name="p1134115141390"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p194601733812"><a name="p194601733812"></a><a name="p194601733812"></a>BMS.3021</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p34604317816"><a name="p34604317816"></a><a name="p34604317816"></a>Failed to create the data disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p94601031487"><a name="p94601031487"></a><a name="p94601031487"></a>Failed to create the data disk.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p204601319820"><a name="p204601319820"></a><a name="p204601319820"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row35973513815"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p4892181411915"><a name="p4892181411915"></a><a name="p4892181411915"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p135971251981"><a name="p135971251981"></a><a name="p135971251981"></a>BMS.3019</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p659765687"><a name="p659765687"></a><a name="p659765687"></a>Failed to attach the data disk.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p2597151785"><a name="p2597151785"></a><a name="p2597151785"></a>Failed to attach the data disk.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p259755285"><a name="p259755285"></a><a name="p259755285"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row163461919810"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p740515151291"><a name="p740515151291"></a><a name="p740515151291"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p11346171289"><a name="p11346171289"></a><a name="p11346171289"></a>BMS.3038</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p14346312818"><a name="p14346312818"></a><a name="p14346312818"></a>Failed to assign an EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p734613114812"><a name="p734613114812"></a><a name="p734613114812"></a>Failed to assign the EIP.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p153468112819"><a name="p153468112819"></a><a name="p153468112819"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row12594173318311"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p0595143316318"><a name="p0595143316318"></a><a name="p0595143316318"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p75951433939"><a name="p75951433939"></a><a name="p75951433939"></a>BMS.0315</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p15954331438"><a name="p15954331438"></a><a name="p15954331438"></a>Disks cannot be attached to a BMS using this flavor.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p45951133535"><a name="p45951133535"></a><a name="p45951133535"></a>Disks cannot be attached to a BMS using this flavor[%s].</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p8958158841"><a name="p8958158841"></a><a name="p8958158841"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row16705181313814"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p670514131781"><a name="p670514131781"></a><a name="p670514131781"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p11705161315817"><a name="p11705161315817"></a><a name="p11705161315817"></a>BMS.0400</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p57057131887"><a name="p57057131887"></a><a name="p57057131887"></a>The image does not support IPv6.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p07051135820"><a name="p07051135820"></a><a name="p07051135820"></a>the image[%s] is not support ipv6.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p67051513385"><a name="p67051513385"></a><a name="p67051513385"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row101831346141913"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p818424671919"><a name="p818424671919"></a><a name="p818424671919"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p1918454615194"><a name="p1918454615194"></a><a name="p1918454615194"></a>BMS.0360</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p718484618196"><a name="p718484618196"></a><a name="p718484618196"></a>The disk has been frozen and cannot be operated for the <span id="text96786237145"><a name="text96786237145"></a><a name="text96786237145"></a>BMS</span><span id="text1067812230141"><a name="text1067812230141"></a><a name="text1067812230141"></a></span>.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p76965402115"><a name="p76965402115"></a><a name="p76965402115"></a>This operation cannot be performed because EVS Disk %s is frozen.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p1918414671919"><a name="p1918414671919"></a><a name="p1918414671919"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row17541856104216"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p6543195610427"><a name="p6543195610427"></a><a name="p6543195610427"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p2543155684218"><a name="p2543155684218"></a><a name="p2543155684218"></a>BMS.3026</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p14543175674218"><a name="p14543175674218"></a><a name="p14543175674218"></a>The password does not meet requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p165439561420"><a name="p165439561420"></a><a name="p165439561420"></a>Password does not meet the requirements of the rule.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p754314565420"><a name="p754314565420"></a><a name="p754314565420"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row377345812429"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p77742058194212"><a name="p77742058194212"></a><a name="p77742058194212"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p137741158174213"><a name="p137741158174213"></a><a name="p137741158174213"></a>BMS.3027</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p11774125814211"><a name="p11774125814211"></a><a name="p11774125814211"></a>Invalid VPC parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p157757582424"><a name="p157757582424"></a><a name="p157757582424"></a>VPC parameter is illegal.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p5775165874212"><a name="p5775165874212"></a><a name="p5775165874212"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row459281154318"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p359212112434"><a name="p359212112434"></a><a name="p359212112434"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p165928118432"><a name="p165928118432"></a><a name="p165928118432"></a>BMS.3028</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1959261154318"><a name="p1959261154318"></a><a name="p1959261154318"></a>Disk quota is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p10592191154311"><a name="p10592191154311"></a><a name="p10592191154311"></a>cinder quota check fail.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p859216124319"><a name="p859216124319"></a><a name="p859216124319"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
<tr id="row18645111782320"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p189434824411"><a name="p189434824411"></a><a name="p189434824411"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p139431894417"><a name="p139431894417"></a><a name="p139431894417"></a>Common.0018</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p69439884417"><a name="p69439884417"></a><a name="p69439884417"></a>tenant_id in the token is different from that in the URL.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p164235218234"><a name="p164235218234"></a><a name="p164235218234"></a>tenantId in token is not the same with in URL.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p794318810447"><a name="p794318810447"></a><a name="p794318810447"></a>Check whether the tenant token is correct.</p>
</td>
</tr>
<tr id="row6354133152016"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p73551135202"><a name="p73551135202"></a><a name="p73551135202"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p193551335201"><a name="p193551335201"></a><a name="p193551335201"></a>BMS.0111</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p1635610316202"><a name="p1635610316202"></a><a name="p1635610316202"></a>Password or key pair is not specified, or both specified.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p835610317208"><a name="p835610317208"></a><a name="p835610317208"></a>none or multi password specify, please specify one.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p33561632202"><a name="p33561632202"></a><a name="p33561632202"></a>The password and key pair cannot be specified at the same time. Select one of them based on the login mode.</p>
</td>
</tr>
<tr id="row195441754118"><td class="cellrowborder" valign="top" width="9.900990099009901%" headers="mcps1.1.6.1.1 "><p id="p209551017144116"><a name="p209551017144116"></a><a name="p209551017144116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.6.1.2 "><p id="p5955517184114"><a name="p5955517184114"></a><a name="p5955517184114"></a>BMS.0395</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.6.1.3 "><p id="p2095651744115"><a name="p2095651744115"></a><a name="p2095651744115"></a>Windows <span id="text203641828161415"><a name="text203641828161415"></a><a name="text203641828161415"></a>BMS</span><span id="text1436402817145"><a name="text1436402817145"></a><a name="text1436402817145"></a></span>s do not support remote login.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.1.6.1.4 "><p id="p12956017174114"><a name="p12956017174114"></a><a name="p12956017174114"></a>The server[%s] is windows system and can not support remote login.</p>
</td>
<td class="cellrowborder" valign="top" width="31.683168316831683%" headers="mcps1.1.6.1.5 "><p id="p16956317134114"><a name="p16956317134114"></a><a name="p16956317134114"></a>See the returned error message or contact technical support.</p>
</td>
</tr>
</tbody>
</table>

