# Error Code Description v2.0<a name="nat_api_0040"></a>

## Background Information<a name="section130614503315"></a>

-   An error code returned by an API does not correspond to one error message. The following table lists only common error messages.
-   Most NAT Gateway APIs are asynchronous. Some error codes are displayed in the returned messages for task viewing requests. HTTP status codes may not be accurate.
-   The NAT Gateway service is strongly dependent on other services, such as network and storage. When error messages are provided for the NAT Gateway-depended services, contact technical support for troubleshooting.

## Error Codes<a name="section932110513314"></a>

<a name="table19989164922114"></a>
<table><thead align="left"><tr id="row1350515102119"><th class="cellrowborder" valign="top" width="7.140714071407141%" id="mcps1.1.7.1.1"><p id="p175051951202114"><a name="p175051951202114"></a><a name="p175051951202114"></a><strong>Module</strong></p>
</th>
<th class="cellrowborder" valign="top" width="8.54085408540854%" id="mcps1.1.7.1.2"><p id="p1150535132111"><a name="p1150535132111"></a><a name="p1150535132111"></a><strong>HTTP Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.511351135113511%" id="mcps1.1.7.1.3"><p id="p1505105119211"><a name="p1505105119211"></a><a name="p1505105119211"></a><strong>Error Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.701570157015702%" id="mcps1.1.7.1.4"><p id="p55052513212"><a name="p55052513212"></a><a name="p55052513212"></a><strong>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.552755275527556%" id="mcps1.1.7.1.5"><p id="p19505115112215"><a name="p19505115112215"></a><a name="p19505115112215"></a><strong id="b842352706193758"><a name="b842352706193758"></a><a name="b842352706193758"></a>Error Message</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.552755275527556%" id="mcps1.1.7.1.6"><p id="p195052518210"><a name="p195052518210"></a><a name="p195052518210"></a><strong>Handling Measure</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row9505451142116"><td class="cellrowborder" rowspan="22" valign="top" width="7.140714071407141%" headers="mcps1.1.7.1.1 "><p id="p1150595122111"><a name="p1150595122111"></a><a name="p1150595122111"></a>Public</p>
</td>
<td class="cellrowborder" valign="top" width="8.54085408540854%" headers="mcps1.1.7.1.2 "><p id="p950535172112"><a name="p950535172112"></a><a name="p950535172112"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="13.511351135113511%" headers="mcps1.1.7.1.3 "><p id="p550585182119"><a name="p550585182119"></a><a name="p550585182119"></a>VPC.0002</p>
</td>
<td class="cellrowborder" valign="top" width="15.701570157015702%" headers="mcps1.1.7.1.4 "><p id="p13505195115214"><a name="p13505195115214"></a><a name="p13505195115214"></a>The AZ is left blank.</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.5 "><p id="p85053517214"><a name="p85053517214"></a><a name="p85053517214"></a>Available zone Name is null.</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.6 "><p id="p75051251172117"><a name="p75051251172117"></a><a name="p75051251172117"></a>Verify whether the <strong id="b842352706201122"><a name="b842352706201122"></a><a name="b842352706201122"></a>availability_zone</strong> field in the request body for creating a subnet is empty.</p>
</td>
</tr>
<tr id="row8505251142115"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p5505451152111"><a name="p5505451152111"></a><a name="p5505451152111"></a>404</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p95055513214"><a name="p95055513214"></a><a name="p95055513214"></a>VPC.0003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p25051851162111"><a name="p25051851162111"></a><a name="p25051851162111"></a>The VPC does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p2050555115216"><a name="p2050555115216"></a><a name="p2050555115216"></a>VPC does not exit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p45051851152119"><a name="p45051851152119"></a><a name="p45051851152119"></a>Check whether the VPC ID is correct or whether the VPC exists under the tenant.</p>
</td>
</tr>
<tr id="row18505165113217"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p11505105112114"><a name="p11505105112114"></a><a name="p11505105112114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p7505651162110"><a name="p7505651162110"></a><a name="p7505651162110"></a>VPC.0004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p75051351132111"><a name="p75051351132111"></a><a name="p75051351132111"></a>The status of the VPC is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p145050511217"><a name="p145050511217"></a><a name="p145050511217"></a>VPC is not active, please try later.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p550555110216"><a name="p550555110216"></a><a name="p550555110216"></a>Try again later or contact technical support.</p>
</td>
</tr>
<tr id="row1750514516213"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p750511516211"><a name="p750511516211"></a><a name="p750511516211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p650515116219"><a name="p650515116219"></a><a name="p650515116219"></a>VPC.0007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p135058514219"><a name="p135058514219"></a><a name="p135058514219"></a>Inconsistent tenant IDs.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p18505551172117"><a name="p18505551172117"></a><a name="p18505551172117"></a>urlTenantId is not equal tokenTenantId</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1250520518219"><a name="p1250520518219"></a><a name="p1250520518219"></a>The tenant ID in the URL is different from that parsed in the token.</p>
</td>
</tr>
<tr id="row250525172114"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p7505185114215"><a name="p7505185114215"></a><a name="p7505185114215"></a>401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p250513513219"><a name="p250513513219"></a><a name="p250513513219"></a>VPC.0008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1050513511215"><a name="p1050513511215"></a><a name="p1050513511215"></a>Invalid token.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p450513511212"><a name="p450513511212"></a><a name="p450513511212"></a>Invalid token in the header.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p150515182111"><a name="p150515182111"></a><a name="p150515182111"></a>Check whether the token in the request header is valid.</p>
</td>
</tr>
<tr id="row850585172116"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p16505151132110"><a name="p16505151132110"></a><a name="p16505151132110"></a>401</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p12505951182120"><a name="p12505951182120"></a><a name="p12505951182120"></a>VPC.0009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p13505251112111"><a name="p13505251112111"></a><a name="p13505251112111"></a>Real-name authentication fails.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p7505651192119"><a name="p7505651192119"></a><a name="p7505651192119"></a>real-name authentication fail.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p8505051122110"><a name="p8505051122110"></a><a name="p8505051122110"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row10505175112118"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1850555115212"><a name="p1850555115212"></a><a name="p1850555115212"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p250515511217"><a name="p250515511217"></a><a name="p250515511217"></a>VPC.2701</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p19505175172112"><a name="p19505175172112"></a><a name="p19505175172112"></a>You do not have permission to perform this operation, or your account balance is insufficient.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1505175112211"><a name="p1505175112211"></a><a name="p1505175112211"></a>Token not allowed to do this action.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p2050515120210"><a name="p2050515120210"></a><a name="p2050515120210"></a>Check whether the account balance is insufficient or whether your account has been frozen.</p>
</td>
</tr>
<tr id="row12505105111215"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p125055511215"><a name="p125055511215"></a><a name="p125055511215"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p25051151142118"><a name="p25051151142118"></a><a name="p25051151142118"></a>VPC.0010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1050595142111"><a name="p1050595142111"></a><a name="p1050595142111"></a>Insufficient permissions to make calls to the underlying system.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p105051251182112"><a name="p105051251182112"></a><a name="p105051251182112"></a>Rules on xx by ** disallowed by policy</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p6505145192118"><a name="p6505145192118"></a><a name="p6505145192118"></a>Obtain the required permissions.</p>
</td>
</tr>
<tr id="row9505195118211"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p12505165122116"><a name="p12505165122116"></a><a name="p12505165122116"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p185052051162111"><a name="p185052051162111"></a><a name="p185052051162111"></a>VPC.2201</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1505151112113"><a name="p1505151112113"></a><a name="p1505151112113"></a>Insufficient fine-grained permissions.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p175054514217"><a name="p175054514217"></a><a name="p175054514217"></a>Policy doesn't allow &lt;x:x:x&gt; to be performed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p12505551202112"><a name="p12505551202112"></a><a name="p12505551202112"></a>Obtain the required permissions.</p>
</td>
</tr>
<tr id="row19505205118211"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p18505145152116"><a name="p18505145152116"></a><a name="p18505145152116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p10505751182114"><a name="p10505751182114"></a><a name="p10505751182114"></a>VPC.0014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1550505114211"><a name="p1550505114211"></a><a name="p1550505114211"></a>The enterprise project is unavailable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p6520145152111"><a name="p6520145152111"></a><a name="p6520145152111"></a>This enterpriseProject status is disable.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p5520195115216"><a name="p5520195115216"></a><a name="p5520195115216"></a>Use the ID of another available enterprise project.</p>
</td>
</tr>
<tr id="row125201151192111"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p25209518219"><a name="p25209518219"></a><a name="p25209518219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p852015112214"><a name="p852015112214"></a><a name="p852015112214"></a>VPC.0011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p652025112111"><a name="p652025112111"></a><a name="p652025112111"></a>Invalid enterprise project ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p3520351172118"><a name="p3520351172118"></a><a name="p3520351172118"></a>EnterpriseProjectId is invalid</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p135201151142119"><a name="p135201151142119"></a><a name="p135201151142119"></a>Enter a valid enterprise project ID.</p>
</td>
</tr>
<tr id="row2520115152110"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p13520155122120"><a name="p13520155122120"></a><a name="p13520155122120"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p145201251192110"><a name="p145201251192110"></a><a name="p145201251192110"></a>VPC.2048</p>
<p id="p1252015518216"><a name="p1252015518216"></a><a name="p1252015518216"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p552025119213"><a name="p552025119213"></a><a name="p552025119213"></a>Invalid timestamp.</p>
<p id="p352015112214"><a name="p352015112214"></a><a name="p352015112214"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p19520175142116"><a name="p19520175142116"></a><a name="p19520175142116"></a>Invalid value for created_at %(timestamp)s.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p15520115132114"><a name="p15520115132114"></a><a name="p15520115132114"></a>Enter the time in the correct format.</p>
<p id="p10520051142119"><a name="p10520051142119"></a><a name="p10520051142119"></a></p>
</td>
</tr>
<tr id="row1520175113214"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p2052016511216"><a name="p2052016511216"></a><a name="p2052016511216"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p10520951192111"><a name="p10520951192111"></a><a name="p10520951192111"></a>VPC.2002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p19520135142119"><a name="p19520135142119"></a><a name="p19520135142119"></a>Invalid request parameters.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p19520155119217"><a name="p19520155119217"></a><a name="p19520155119217"></a>Invalid parameters.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1452012514219"><a name="p1452012514219"></a><a name="p1452012514219"></a>Enter the correct parameter.</p>
</td>
</tr>
<tr id="row16520145116213"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p12520165114214"><a name="p12520165114214"></a><a name="p12520165114214"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p175209511212"><a name="p175209511212"></a><a name="p175209511212"></a>VPC.2010</p>
<p id="p452012511212"><a name="p452012511212"></a><a name="p452012511212"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p145201151162115"><a name="p145201151162115"></a><a name="p145201151162115"></a>The default route already exists.</p>
<p id="p17520115102119"><a name="p17520115102119"></a><a name="p17520115102119"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p152085132116"><a name="p152085132116"></a><a name="p152085132116"></a>The router %(router_id)s has default route.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p145201951172117"><a name="p145201951172117"></a><a name="p145201951172117"></a>The router has a default route. Delete the default route and then create a NAT gateway.</p>
<p id="p125201751132112"><a name="p125201751132112"></a><a name="p125201751132112"></a></p>
</td>
</tr>
<tr id="row05201051122112"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1452005110213"><a name="p1452005110213"></a><a name="p1452005110213"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p952055112214"><a name="p952055112214"></a><a name="p952055112214"></a>VPC.2011</p>
<p id="p165201051122114"><a name="p165201051122114"></a><a name="p165201051122114"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p35208514212"><a name="p35208514212"></a><a name="p35208514212"></a>The router does not exist.</p>
<p id="p45201351172114"><a name="p45201351172114"></a><a name="p45201351172114"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p18520155115216"><a name="p18520155115216"></a><a name="p18520155115216"></a>The router %(router_id)s does  not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p18520115114214"><a name="p18520115114214"></a><a name="p18520115114214"></a>Check whether the entered router ID is correct.</p>
<p id="p452065162116"><a name="p452065162116"></a><a name="p452065162116"></a></p>
</td>
</tr>
<tr id="row1952018511219"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p352025172113"><a name="p352025172113"></a><a name="p352025172113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p352085117212"><a name="p352085117212"></a><a name="p352085117212"></a>VPC.2009</p>
<p id="p15209516219"><a name="p15209516219"></a><a name="p15209516219"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p9520135120219"><a name="p9520135120219"></a><a name="p9520135120219"></a>The network does not exist.</p>
<p id="p152005112214"><a name="p152005112214"></a><a name="p152005112214"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1352095112217"><a name="p1352095112217"></a><a name="p1352095112217"></a>Network %(network_id)s does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p17520195102118"><a name="p17520195102118"></a><a name="p17520195102118"></a>Enter a valid network ID.</p>
<p id="p11520135110211"><a name="p11520135110211"></a><a name="p11520135110211"></a></p>
</td>
</tr>
<tr id="row10520145111211"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p185201751102118"><a name="p185201751102118"></a><a name="p185201751102118"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p652017518213"><a name="p652017518213"></a><a name="p652017518213"></a>VPC.2016</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p135201851192116"><a name="p135201851192116"></a><a name="p135201851192116"></a>The rule has not been deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p11520115117211"><a name="p11520115117211"></a><a name="p11520115117211"></a>Rule has not been deleted.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p20520145110218"><a name="p20520145110218"></a><a name="p20520145110218"></a>Contact technical support.</p>
<p id="p4520175115211"><a name="p4520175115211"></a><a name="p4520175115211"></a></p>
</td>
</tr>
<tr id="row1852095117219"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1852025162119"><a name="p1852025162119"></a><a name="p1852025162119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p205201151132112"><a name="p205201151132112"></a><a name="p205201151132112"></a>VPC.2049</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p952035119212"><a name="p952035119212"></a><a name="p952035119212"></a>The database is abnormal.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p15520251142119"><a name="p15520251142119"></a><a name="p15520251142119"></a>DB Error</p>
<p id="p13520195122112"><a name="p13520195122112"></a><a name="p13520195122112"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p13520951172117"><a name="p13520951172117"></a><a name="p13520951172117"></a>Contact technical support.</p>
<p id="p3520105111217"><a name="p3520105111217"></a><a name="p3520105111217"></a></p>
</td>
</tr>
<tr id="row1452015515211"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p55201519214"><a name="p55201519214"></a><a name="p55201519214"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p3520751162116"><a name="p3520751162116"></a><a name="p3520751162116"></a>VPC.2013</p>
<p id="p15520115172113"><a name="p15520115172113"></a><a name="p15520115172113"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p14520185132113"><a name="p14520185132113"></a><a name="p14520185132113"></a>The subnet is not connected to the virtual router.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p20520125120217"><a name="p20520125120217"></a><a name="p20520125120217"></a>Router %(router)s has no port for subnet %(subnet)s.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p145201351102113"><a name="p145201351102113"></a><a name="p145201351102113"></a>Add the subnet to the router port.</p>
<p id="p3520851132118"><a name="p3520851132118"></a><a name="p3520851132118"></a></p>
</td>
</tr>
<tr id="row852015152116"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p10520115118217"><a name="p10520115118217"></a><a name="p10520115118217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p18520165152113"><a name="p18520165152113"></a><a name="p18520165152113"></a>VPC.2019</p>
<p id="p3520851152115"><a name="p3520851152115"></a><a name="p3520851152115"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p135201351172118"><a name="p135201351172118"></a><a name="p135201351172118"></a>The resource is in use. </p>
<p id="p05203514219"><a name="p05203514219"></a><a name="p05203514219"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1052075120211"><a name="p1052075120211"></a><a name="p1052075120211"></a>Resource %(res_type)s %(res)s is used by %(user_type)s %(user)s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p105201651172119"><a name="p105201651172119"></a><a name="p105201651172119"></a>Contact technical support.</p>
<p id="p16520151162118"><a name="p16520151162118"></a><a name="p16520151162118"></a></p>
</td>
</tr>
<tr id="row14520125115214"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p195206513217"><a name="p195206513217"></a><a name="p195206513217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p135201751122113"><a name="p135201751122113"></a><a name="p135201751122113"></a>VPC.2008</p>
<p id="p552055122115"><a name="p552055122115"></a><a name="p552055122115"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1652045132118"><a name="p1652045132118"></a><a name="p1652045132118"></a>The network does not have any subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p852019519217"><a name="p852019519217"></a><a name="p852019519217"></a>Network %(network)s does not contain any IPv4 subnet</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p10520105182116"><a name="p10520105182116"></a><a name="p10520105182116"></a>Contact technical support.</p>
<p id="p18520135182112"><a name="p18520135182112"></a><a name="p18520135182112"></a></p>
</td>
</tr>
<tr id="row1520165116218"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1052035118212"><a name="p1052035118212"></a><a name="p1052035118212"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p12520155132115"><a name="p12520155132115"></a><a name="p12520155132115"></a>VPC.2012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p165209518219"><a name="p165209518219"></a><a name="p165209518219"></a>The VPC already has a NAT gateway.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1152015122112"><a name="p1152015122112"></a><a name="p1152015122112"></a>The router %(router_id)s already has nat gateway.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p55201651132119"><a name="p55201651132119"></a><a name="p55201651132119"></a>Select another VPC.</p>
</td>
</tr>
<tr id="row052035192116"><td class="cellrowborder" rowspan="15" valign="top" width="7.140714071407141%" headers="mcps1.1.7.1.1 "><p id="p252025172118"><a name="p252025172118"></a><a name="p252025172118"></a>NAT Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="8.54085408540854%" headers="mcps1.1.7.1.2 "><p id="p10520175111215"><a name="p10520175111215"></a><a name="p10520175111215"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="13.511351135113511%" headers="mcps1.1.7.1.3 "><p id="p125206517216"><a name="p125206517216"></a><a name="p125206517216"></a>VPC.2000</p>
</td>
<td class="cellrowborder" valign="top" width="15.701570157015702%" headers="mcps1.1.7.1.4 "><p id="p105201451182111"><a name="p105201451182111"></a><a name="p105201451182111"></a>NAT gateway request error.</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.5 "><p id="p15201751182117"><a name="p15201751182117"></a><a name="p15201751182117"></a>Lack of user authority.</p>
<p id="p85201651102118"><a name="p85201651102118"></a><a name="p85201651102118"></a>//request is null.</p>
<p id="p2052016519218"><a name="p2052016519218"></a><a name="p2052016519218"></a>//endpoint is empty.</p>
<p id="p1352018514216"><a name="p1352018514216"></a><a name="p1352018514216"></a>// resource type is invalid. //create natgateway requset is null. //update natgateway request is null</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.6 "><p id="p052015512216"><a name="p052015512216"></a><a name="p052015512216"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row052012516219"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p195201051142113"><a name="p195201051142113"></a><a name="p195201051142113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p7520251182118"><a name="p7520251182118"></a><a name="p7520251182118"></a>VPC.2030</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1520185120215"><a name="p1520185120215"></a><a name="p1520185120215"></a>The system is busy. Please try again later.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p25201451182112"><a name="p25201451182112"></a><a name="p25201451182112"></a>The system is busy. Please try again later.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p852019514214"><a name="p852019514214"></a><a name="p852019514214"></a>Try again later.</p>
</td>
</tr>
<tr id="row1152013511213"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p14520145142113"><a name="p14520145142113"></a><a name="p14520145142113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p17520195119213"><a name="p17520195119213"></a><a name="p17520195119213"></a>VPC.2001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p652045120214"><a name="p652045120214"></a><a name="p652045120214"></a>Incorrect NAT gateway parameter.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p9520185119212"><a name="p9520185119212"></a><a name="p9520185119212"></a>Request is invalid. //NatGateway id unvalid.</p>
<p id="p252017516217"><a name="p252017516217"></a><a name="p252017516217"></a>// the enterprise project id is unsupported.</p>
<p id="p652015515217"><a name="p652015515217"></a><a name="p652015515217"></a>// the enterprise project id in request is invalid. //parameter is null.</p>
<p id="p9520051152120"><a name="p9520051152120"></a><a name="p9520051152120"></a>// tags is invalid.</p>
<p id="p552011515215"><a name="p552011515215"></a><a name="p552011515215"></a>// get natgateways error limit is invalid.</p>
<p id="p8520165116211"><a name="p8520165116211"></a><a name="p8520165116211"></a>//get natgateways error marker is invalid.</p>
<p id="p3520551152111"><a name="p3520551152111"></a><a name="p3520551152111"></a>//Only admin user can do this action. //Parameters are invalid, check them and try.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p25201451102116"><a name="p25201451102116"></a><a name="p25201451102116"></a>Enter the correct parameter or contact technical support.</p>
</td>
</tr>
<tr id="row452065182117"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1520851182119"><a name="p1520851182119"></a><a name="p1520851182119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p15520551172113"><a name="p15520551172113"></a><a name="p15520551172113"></a>VPC.2004</p>
<p id="p10520851162117"><a name="p10520851162117"></a><a name="p10520851162117"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p165209517219"><a name="p165209517219"></a><a name="p165209517219"></a>The NAT gateway is not activated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1052015192118"><a name="p1052015192118"></a><a name="p1052015192118"></a>NatGateway %(nat_gateway_id)s is not ACTIVE.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1252013516214"><a name="p1252013516214"></a><a name="p1252013516214"></a>Check the gateway status. If the gateway is not in the running state for a long time, contact technical support.</p>
</td>
</tr>
<tr id="row125201251122116"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1452005112216"><a name="p1452005112216"></a><a name="p1452005112216"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p05201451112115"><a name="p05201451112115"></a><a name="p05201451112115"></a>VPC.2005</p>
<p id="p125209519216"><a name="p125209519216"></a><a name="p125209519216"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p18520145118219"><a name="p18520145118219"></a><a name="p18520145118219"></a>The NAT gateway is not in the UP state.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1252095113216"><a name="p1252095113216"></a><a name="p1252095113216"></a>NatGateway %(nat_gateway_id)s is not UP.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p552010511218"><a name="p552010511218"></a><a name="p552010511218"></a>The gateway may be frozen due to arrears.</p>
<p id="p15520195172111"><a name="p15520195172111"></a><a name="p15520195172111"></a></p>
</td>
</tr>
<tr id="row252016515215"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p2520205117211"><a name="p2520205117211"></a><a name="p2520205117211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p752095152112"><a name="p752095152112"></a><a name="p752095152112"></a>VPC.2006</p>
<p id="p7520135115219"><a name="p7520135115219"></a><a name="p7520135115219"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p175202516217"><a name="p175202516217"></a><a name="p175202516217"></a>The NAT gateway is frozen.</p>
<p id="p9520651192117"><a name="p9520651192117"></a><a name="p9520651192117"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p105201551182112"><a name="p105201551182112"></a><a name="p105201551182112"></a>NatGateway %(nat_gateway_id)s is frozen.can not update</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p9520451172110"><a name="p9520451172110"></a><a name="p9520451172110"></a>The gateway may be frozen due to arrears and cannot be updated.</p>
<p id="p95201551192119"><a name="p95201551192119"></a><a name="p95201551192119"></a></p>
</td>
</tr>
<tr id="row9520105162115"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p75201051142114"><a name="p75201051142114"></a><a name="p75201051142114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p152095132116"><a name="p152095132116"></a><a name="p152095132116"></a>VPC.2007</p>
<p id="p2520135119212"><a name="p2520135119212"></a><a name="p2520135119212"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p8520195119216"><a name="p8520195119216"></a><a name="p8520195119216"></a>The NAT gateway does not exist.</p>
<p id="p5520351192114"><a name="p5520351192114"></a><a name="p5520351192114"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p8520551102116"><a name="p8520551102116"></a><a name="p8520551102116"></a>NatGateway %(nat_gateway_id)s does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p152065116213"><a name="p152065116213"></a><a name="p152065116213"></a>The NAT gateway does not exist.</p>
<p id="p552015515216"><a name="p552015515216"></a><a name="p552015515216"></a></p>
</td>
</tr>
<tr id="row18520195115218"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p55201151142114"><a name="p55201151142114"></a><a name="p55201151142114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p155201151132116"><a name="p155201151132116"></a><a name="p155201151132116"></a>VPC.2050</p>
<p id="p195201951182110"><a name="p195201951182110"></a><a name="p195201951182110"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1520175117211"><a name="p1520175117211"></a><a name="p1520175117211"></a>Concurrent operation conflicts.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p13520115112110"><a name="p13520115112110"></a><a name="p13520115112110"></a>Concurrent conflict requests found</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p3520135119215"><a name="p3520135119215"></a><a name="p3520135119215"></a>Contact technical support.</p>
<p id="p052075162120"><a name="p052075162120"></a><a name="p052075162120"></a></p>
</td>
</tr>
<tr id="row8520115172114"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p165201151102110"><a name="p165201151102110"></a><a name="p165201151102110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p952085122120"><a name="p952085122120"></a><a name="p952085122120"></a>VPC.2051</p>
<p id="p6520051172110"><a name="p6520051172110"></a><a name="p6520051172110"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p165203513216"><a name="p165203513216"></a><a name="p165203513216"></a>Failed to create the internal port of the NAT gateway.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p175201951172114"><a name="p175201951172114"></a><a name="p175201951172114"></a>Create NG Port failed.</p>
<p id="p85205512218"><a name="p85205512218"></a><a name="p85205512218"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p18520551162110"><a name="p18520551162110"></a><a name="p18520551162110"></a>Internal error. Contact technical support.</p>
<p id="p13520951122118"><a name="p13520951122118"></a><a name="p13520951122118"></a></p>
</td>
</tr>
<tr id="row1152045182114"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p85209518210"><a name="p85209518210"></a><a name="p85209518210"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p5520251202110"><a name="p5520251202110"></a><a name="p5520251202110"></a>VPC.2052</p>
<p id="p19520155182110"><a name="p19520155182110"></a><a name="p19520155182110"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1352010517218"><a name="p1352010517218"></a><a name="p1352010517218"></a>Failed to bind the internal port to the NAT gateway.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1852075152113"><a name="p1852075152113"></a><a name="p1852075152113"></a>NG Port %(port)s is unbound.</p>
<p id="p155202517216"><a name="p155202517216"></a><a name="p155202517216"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p652035132111"><a name="p652035132111"></a><a name="p652035132111"></a>Internal error. Contact technical support.</p>
<p id="p45201851172119"><a name="p45201851172119"></a><a name="p45201851172119"></a></p>
</td>
</tr>
<tr id="row1752045132112"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p9520195182113"><a name="p9520195182113"></a><a name="p9520195182113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p952035142114"><a name="p952035142114"></a><a name="p952035142114"></a>VPC.2053</p>
<p id="p5520451142118"><a name="p5520451142118"></a><a name="p5520451142118"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1952025102115"><a name="p1952025102115"></a><a name="p1952025102115"></a>The NAT gateway does not support IPv6.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p3520125142117"><a name="p3520125142117"></a><a name="p3520125142117"></a>NatGateway does not support IPv6.</p>
<p id="p15520251172112"><a name="p15520251172112"></a><a name="p15520251172112"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p252055152119"><a name="p252055152119"></a><a name="p252055152119"></a>The NAT gateway cannot be bound to an IPv6 EIP.</p>
</td>
</tr>
<tr id="row5520135119216"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p18520851192114"><a name="p18520851192114"></a><a name="p18520851192114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p7520165102112"><a name="p7520165102112"></a><a name="p7520165102112"></a>VPC.2045</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1652045119212"><a name="p1652045119212"></a><a name="p1652045119212"></a>An error occurred when selecting the gateway node.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p12520251122110"><a name="p12520251122110"></a><a name="p12520251122110"></a>Get Nat gateway host failed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1452065162116"><a name="p1452065162116"></a><a name="p1452065162116"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row452010510219"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p35201351182110"><a name="p35201351182110"></a><a name="p35201351182110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p12520051192110"><a name="p12520051192110"></a><a name="p12520051192110"></a>VPC.2046</p>
<p id="p1552025118214"><a name="p1552025118214"></a><a name="p1552025118214"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p752016519213"><a name="p752016519213"></a><a name="p752016519213"></a>Failed to obtain the IP address of the gateway node.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1520135122115"><a name="p1520135122115"></a><a name="p1520135122115"></a>Get Nat gateway agent local_ip failed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p8520195162117"><a name="p8520195162117"></a><a name="p8520195162117"></a>Contact technical support.</p>
<p id="p9520145119214"><a name="p9520145119214"></a><a name="p9520145119214"></a></p>
</td>
</tr>
<tr id="row6520145112112"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1452018518219"><a name="p1452018518219"></a><a name="p1452018518219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p10520251162116"><a name="p10520251162116"></a><a name="p10520251162116"></a>VPC.2047</p>
<p id="p1552011517211"><a name="p1552011517211"></a><a name="p1552011517211"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1052005118215"><a name="p1052005118215"></a><a name="p1052005118215"></a>Failed to obtain the VPC route table.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p55203512216"><a name="p55203512216"></a><a name="p55203512216"></a>Get RouteTable %(router_id)s failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p052035112112"><a name="p052035112112"></a><a name="p052035112112"></a>Contact technical support.</p>
<p id="p1252075142120"><a name="p1252075142120"></a><a name="p1252075142120"></a></p>
</td>
</tr>
<tr id="row1852017510218"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p752005113213"><a name="p752005113213"></a><a name="p752005113213"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p155201651112113"><a name="p155201651112113"></a><a name="p155201651112113"></a>VPC.2012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p5520145110216"><a name="p5520145110216"></a><a name="p5520145110216"></a>The router already has a NAT gateway.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p4520651132120"><a name="p4520651132120"></a><a name="p4520651132120"></a>The router %(router_id)s already has nat gateway.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p19520451122112"><a name="p19520451122112"></a><a name="p19520451122112"></a>Select a router that has not been bound to a NAT gateway.</p>
<p id="p135201251112118"><a name="p135201251112118"></a><a name="p135201251112118"></a></p>
</td>
</tr>
<tr id="row7520155120214"><td class="cellrowborder" rowspan="12" valign="top" width="7.140714071407141%" headers="mcps1.1.7.1.1 "><p id="p1520165172110"><a name="p1520165172110"></a><a name="p1520165172110"></a>SNAT Rule</p>
<p id="p10520151132116"><a name="p10520151132116"></a><a name="p10520151132116"></a></p>
</td>
<td class="cellrowborder" valign="top" width="8.54085408540854%" headers="mcps1.1.7.1.2 "><p id="p1152095182111"><a name="p1152095182111"></a><a name="p1152095182111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="13.511351135113511%" headers="mcps1.1.7.1.3 "><p id="p25202518219"><a name="p25202518219"></a><a name="p25202518219"></a>VPC.2014</p>
</td>
<td class="cellrowborder" valign="top" width="15.701570157015702%" headers="mcps1.1.7.1.4 "><p id="p15201151162117"><a name="p15201151162117"></a><a name="p15201151162117"></a>Incorrect SNAT rule parameter.</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.5 "><p id="p952055122114"><a name="p952055122114"></a><a name="p952055122114"></a>Endpoint is null or empty. //Endpoint is Invalid.</p>
<p id="p852015132119"><a name="p852015132119"></a><a name="p852015132119"></a>//Request is null. //natGatewayId is invalid. //SnatRule id unvalid. //NatGatewayId is unvalid.</p>
<p id="p1852075118214"><a name="p1852075118214"></a><a name="p1852075118214"></a>//Invalid value for public ip id.</p>
<p id="p252005122116"><a name="p252005122116"></a><a name="p252005122116"></a>//Endpoint is null.</p>
<p id="p1452095172112"><a name="p1452095172112"></a><a name="p1452095172112"></a>//request is null.</p>
<p id="p12520125117214"><a name="p12520125117214"></a><a name="p12520125117214"></a>//Query SnatRules list error marker is invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.6 "><p id="p105205511214"><a name="p105205511214"></a><a name="p105205511214"></a>Enter the correct parameter or contact technical support.</p>
</td>
</tr>
<tr id="row14520251152116"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p185201251192115"><a name="p185201251192115"></a><a name="p185201251192115"></a>400</p>
<p id="p452016515213"><a name="p452016515213"></a><a name="p452016515213"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p19520351162120"><a name="p19520351162120"></a><a name="p19520351162120"></a>VPC.2031</p>
<p id="p252035182111"><a name="p252035182111"></a><a name="p252035182111"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p0520105110214"><a name="p0520105110214"></a><a name="p0520105110214"></a>The CIDR of the SNAT rule conflicts with the network.</p>
<p id="p1452035132116"><a name="p1452035132116"></a><a name="p1452035132116"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p13520195152110"><a name="p13520195152110"></a><a name="p13520195152110"></a>Either network_id or cidr must be specified.Both can not be specified at the same time</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p11520105115217"><a name="p11520105115217"></a><a name="p11520105115217"></a>Do not specify the <strong id="b228118556546"><a name="b228118556546"></a><a name="b228118556546"></a>Cidr</strong> and <strong id="b37991522557"><a name="b37991522557"></a><a name="b37991522557"></a>Network_id</strong> fields at the same time when configuring an SNAT rule.</p>
<p id="p65201519211"><a name="p65201519211"></a><a name="p65201519211"></a></p>
</td>
</tr>
<tr id="row1952065132120"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p16520651162113"><a name="p16520651162113"></a><a name="p16520651162113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p11520125142111"><a name="p11520125142111"></a><a name="p11520125142111"></a>VPC.2032</p>
<p id="p1752045112216"><a name="p1752045112216"></a><a name="p1752045112216"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p185201251132110"><a name="p185201251132110"></a><a name="p185201251132110"></a>Invalid CIDR block.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p652075117213"><a name="p652075117213"></a><a name="p652075117213"></a>cidr is invalid, make sure it's format is correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p17520205114211"><a name="p17520205114211"></a><a name="p17520205114211"></a>Enter a valid CIDR block, for example, 192.168.0.0/24.</p>
<p id="p20520205114213"><a name="p20520205114213"></a><a name="p20520205114213"></a></p>
</td>
</tr>
<tr id="row2052025132111"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1052016518212"><a name="p1052016518212"></a><a name="p1052016518212"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p18520351182112"><a name="p18520351182112"></a><a name="p18520351182112"></a>VPC.2033</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p25201551162113"><a name="p25201551162113"></a><a name="p25201551162113"></a>Invalid rule type.</p>
<p id="p125201951182110"><a name="p125201951182110"></a><a name="p125201951182110"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p19520165115213"><a name="p19520165115213"></a><a name="p19520165115213"></a>source_type and  network_id is incompatible.</p>
<p id="p1552055182115"><a name="p1552055182115"></a><a name="p1552055182115"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p852055192113"><a name="p852055192113"></a><a name="p852055192113"></a>If an SNAT rule is configured for a VPC, the parameter <strong id="b15707725165817"><a name="b15707725165817"></a><a name="b15707725165817"></a>Source_Type</strong> is optional or set its value to <strong id="b1793915118012"><a name="b1793915118012"></a><a name="b1793915118012"></a>0</strong>.</p>
<p id="p1052015113216"><a name="p1052015113216"></a><a name="p1052015113216"></a>If an SNAT rule is configured for a Direct Connect connection, <strong id="b18388639165717"><a name="b18388639165717"></a><a name="b18388639165717"></a>Source_type</strong> must be set to <strong id="b465516493578"><a name="b465516493578"></a><a name="b465516493578"></a>1</strong>.</p>
</td>
</tr>
<tr id="row152011518213"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p11520951182116"><a name="p11520951182116"></a><a name="p11520951182116"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p6520175162119"><a name="p6520175162119"></a><a name="p6520175162119"></a>VPC.2034</p>
<p id="p195201518212"><a name="p195201518212"></a><a name="p195201518212"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p452055132117"><a name="p452055132117"></a><a name="p452055132117"></a>The CIDR block must be a subset of the VPC subnet CIDR block.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1152018511216"><a name="p1152018511216"></a><a name="p1152018511216"></a>cidr must be a subset of subnet's cidr.</p>
<p id="p1552095102119"><a name="p1552095102119"></a><a name="p1552095102119"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p12520135111215"><a name="p12520135111215"></a><a name="p12520135111215"></a>If an SNAT rule is configured for a VPC, the CIDR block must be the VPC subnet CIDR block. For example, if the subnet is 192.168.0.0/24, the CIDR block can be 192.168.0.0/25.</p>
<p id="p052011513214"><a name="p052011513214"></a><a name="p052011513214"></a></p>
</td>
</tr>
<tr id="row1552055113216"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p9520115112110"><a name="p9520115112110"></a><a name="p9520115112110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p165201751162111"><a name="p165201751162111"></a><a name="p165201751162111"></a>VPC.2035</p>
<p id="p175201651162112"><a name="p175201651162112"></a><a name="p175201651162112"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p8520451142111"><a name="p8520451142111"></a><a name="p8520451142111"></a>The CIDR block conflicts with the subnet CIDR block.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p452018519211"><a name="p452018519211"></a><a name="p452018519211"></a>cidr conflicts with subnet's cidr.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p2520551202116"><a name="p2520551202116"></a><a name="p2520551202116"></a>If an SNAT rule is configured for a Direct Connect connection, the CIDR block cannot conflict with the VPC subnet CIDR block.</p>
</td>
</tr>
<tr id="row75201151152118"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p652085122111"><a name="p652085122111"></a><a name="p652085122111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p1452019514213"><a name="p1452019514213"></a><a name="p1452019514213"></a>VPC.2036</p>
<p id="p105201351192116"><a name="p105201351192116"></a><a name="p105201351192116"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p18520251122112"><a name="p18520251122112"></a><a name="p18520251122112"></a>The CIDR block conflicts with the existing one.</p>
<p id="p13520155116212"><a name="p13520155116212"></a><a name="p13520155116212"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p052010519219"><a name="p052010519219"></a><a name="p052010519219"></a>cidr in the request conflicts with cidrs of existing rules.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p2052035152111"><a name="p2052035152111"></a><a name="p2052035152111"></a>Enter a CIDR block that does not conflict with existing ones.</p>
<p id="p752095122118"><a name="p752095122118"></a><a name="p752095122118"></a></p>
</td>
</tr>
<tr id="row115202512213"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p2520105132111"><a name="p2520105132111"></a><a name="p2520105132111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p352075152112"><a name="p352075152112"></a><a name="p352075152112"></a>VPC.2018</p>
<p id="p1520145119214"><a name="p1520145119214"></a><a name="p1520145119214"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1520145122114"><a name="p1520145122114"></a><a name="p1520145122114"></a>The rule already exists.</p>
<p id="p13520851182111"><a name="p13520851182111"></a><a name="p13520851182111"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p15520151122111"><a name="p15520151122111"></a><a name="p15520151122111"></a>Snat rule for network %(network)s exists.</p>
<p id="p052017512216"><a name="p052017512216"></a><a name="p052017512216"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p05201451112113"><a name="p05201451112113"></a><a name="p05201451112113"></a>Select a subnet that is not configured with an SNAT rule.</p>
<p id="p125201951132113"><a name="p125201951132113"></a><a name="p125201951132113"></a></p>
</td>
</tr>
<tr id="row7520175115214"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p5520551172111"><a name="p5520551172111"></a><a name="p5520551172111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p252020512211"><a name="p252020512211"></a><a name="p252020512211"></a>VPC.2042</p>
<p id="p75201151102114"><a name="p75201151102114"></a><a name="p75201151102114"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p652010518219"><a name="p652010518219"></a><a name="p652010518219"></a>The EIP has been used by the SNAT rule.</p>
<p id="p10520155115213"><a name="p10520155115213"></a><a name="p10520155115213"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p6520125102110"><a name="p6520125102110"></a><a name="p6520125102110"></a>There is a duplicate EIP %(fips)s in SNAT rule.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p95204516217"><a name="p95204516217"></a><a name="p95204516217"></a>Select another EIP.</p>
<p id="p0520751132117"><a name="p0520751132117"></a><a name="p0520751132117"></a></p>
</td>
</tr>
<tr id="row1552045112217"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p13520751202113"><a name="p13520751202113"></a><a name="p13520751202113"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p65207511217"><a name="p65207511217"></a><a name="p65207511217"></a>VPC.2044</p>
<p id="p052045132111"><a name="p052045132111"></a><a name="p052045132111"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1152011514216"><a name="p1152011514216"></a><a name="p1152011514216"></a>The public IP address UUID of the SNAT rule is invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1952018512219"><a name="p1952018512219"></a><a name="p1952018512219"></a>Invalid input for floating_ip_id. Reason: \'%(fip)s\' is not a valid UUID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1520145142115"><a name="p1520145142115"></a><a name="p1520145142115"></a>Enter a valid UUID.</p>
<p id="p15201251182116"><a name="p15201251182116"></a><a name="p15201251182116"></a></p>
</td>
</tr>
<tr id="row152035113217"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1752045119219"><a name="p1752045119219"></a><a name="p1752045119219"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p1952015512218"><a name="p1952015512218"></a><a name="p1952015512218"></a>VPC.2040</p>
<p id="p1052075115219"><a name="p1052075115219"></a><a name="p1052075115219"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p752025111217"><a name="p752025111217"></a><a name="p752025111217"></a>The public IP address ID of an SNAT rule cannot be a null string.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1252013510212"><a name="p1252013510212"></a><a name="p1252013510212"></a>Invalid value for public ip id.</p>
<p id="p205209510210"><a name="p205209510210"></a><a name="p205209510210"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p11520165162111"><a name="p11520165162111"></a><a name="p11520165162111"></a>Enter a valid ID.</p>
<p id="p125201551112110"><a name="p125201551112110"></a><a name="p125201551112110"></a></p>
</td>
</tr>
<tr id="row5520155142117"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p4520175162119"><a name="p4520175162119"></a><a name="p4520175162119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p9520451152112"><a name="p9520451152112"></a><a name="p9520451152112"></a>VPC.2039</p>
<p id="p135201351122110"><a name="p135201351122110"></a><a name="p135201351122110"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p25201151182116"><a name="p25201151182116"></a><a name="p25201151182116"></a>The number of EIPs associated with the SNAT rule exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p5520155192114"><a name="p5520155192114"></a><a name="p5520155192114"></a>%(limit)s EIP has been associated to this SNAT rules's EIP pool, no more is allowed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p5520165162118"><a name="p5520165162118"></a><a name="p5520165162118"></a>The number of EIPs associated with the SNAT rule exceeds the upper limit. For details, see the <em id="i13570925162910"><a name="i13570925162910"></a><a name="i13570925162910"></a>NAT Gateway API Reference</em>.</p>
<p id="p65201651162113"><a name="p65201651162113"></a><a name="p65201651162113"></a></p>
</td>
</tr>
<tr id="row55201751152116"><td class="cellrowborder" rowspan="19" valign="top" width="7.140714071407141%" headers="mcps1.1.7.1.1 "><p id="p05204511215"><a name="p05204511215"></a><a name="p05204511215"></a>DNAT Rule</p>
<p id="p752014519215"><a name="p752014519215"></a><a name="p752014519215"></a></p>
</td>
<td class="cellrowborder" valign="top" width="8.54085408540854%" headers="mcps1.1.7.1.2 "><p id="p1952015117216"><a name="p1952015117216"></a><a name="p1952015117216"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="13.511351135113511%" headers="mcps1.1.7.1.3 "><p id="p135203519216"><a name="p135203519216"></a><a name="p135203519216"></a>VPC.2020</p>
</td>
<td class="cellrowborder" valign="top" width="15.701570157015702%" headers="mcps1.1.7.1.4 "><p id="p95203519210"><a name="p95203519210"></a><a name="p95203519210"></a>Incorrect DNAT rule parameter.</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.5 "><p id="p1952014513215"><a name="p1952014513215"></a><a name="p1952014513215"></a>get dnatRules error limit is invalid.</p>
<p id="p1852055192114"><a name="p1852055192114"></a><a name="p1852055192114"></a>//get dnatrules error marker is invalid.</p>
<p id="p152095152118"><a name="p152095152118"></a><a name="p152095152118"></a>//endpoint is empty.</p>
<p id="p5520135119215"><a name="p5520135119215"></a><a name="p5520135119215"></a>//DnatRule id unvalid.</p>
<p id="p552017512219"><a name="p552017512219"></a><a name="p552017512219"></a>//VPC ID is invalid.</p>
<p id="p115205512219"><a name="p115205512219"></a><a name="p115205512219"></a>//Request is null.</p>
<p id="p11520451142115"><a name="p11520451142115"></a><a name="p11520451142115"></a>//DnatRule id invalid.</p>
<p id="p752045112216"><a name="p752045112216"></a><a name="p752045112216"></a>//DnatRule natGatewayId id invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.6 "><p id="p10520135111219"><a name="p10520135111219"></a><a name="p10520135111219"></a>Enter the correct parameter or contact technical support.</p>
</td>
</tr>
<tr id="row13520151182110"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p155201651112114"><a name="p155201651112114"></a><a name="p155201651112114"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p155201851132118"><a name="p155201851132118"></a><a name="p155201851132118"></a>VPC.2054</p>
<p id="p1520105119213"><a name="p1520105119213"></a><a name="p1520105119213"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1452045182111"><a name="p1452045182111"></a><a name="p1452045182111"></a>Invalid DNAT rule protocol.</p>
<p id="p7520185132111"><a name="p7520185132111"></a><a name="p7520185132111"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p7520115132118"><a name="p7520115132118"></a><a name="p7520115132118"></a>Dnat rule protocol %(protocol)s not supported.Only protocol values %(values)s and integer representations [6, 17, 0] are supported.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p135201351152110"><a name="p135201351152110"></a><a name="p135201351152110"></a>Configure a valid protocol. The value range can be <strong id="b1398435272417"><a name="b1398435272417"></a><a name="b1398435272417"></a>6</strong>, <strong id="b18853747152419"><a name="b18853747152419"></a><a name="b18853747152419"></a>17</strong>, or <strong id="b15855641172418"><a name="b15855641172418"></a><a name="b15855641172418"></a>0</strong>, corresponding to protocols <strong id="b238952742514"><a name="b238952742514"></a><a name="b238952742514"></a>TCP</strong>, <strong id="b14893152515"><a name="b14893152515"></a><a name="b14893152515"></a>UDP</strong>, and <strong id="b482718398254"><a name="b482718398254"></a><a name="b482718398254"></a>ANY</strong>, respectively.</p>
<p id="p105201651192119"><a name="p105201651192119"></a><a name="p105201651192119"></a></p>
</td>
</tr>
<tr id="row9520051162110"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p15201451202112"><a name="p15201451202112"></a><a name="p15201451202112"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p352025115219"><a name="p352025115219"></a><a name="p352025115219"></a>VPC.2069</p>
<p id="p18520135172114"><a name="p18520135172114"></a><a name="p18520135172114"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p052020515218"><a name="p052020515218"></a><a name="p052020515218"></a>Invalid DNAT rule port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p952085162116"><a name="p952085162116"></a><a name="p952085162116"></a>Invalid value for port %(port)s</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p19520105113213"><a name="p19520105113213"></a><a name="p19520105113213"></a>Configure a valid internal port and external port. The value ranges from 0 to 65535.</p>
</td>
</tr>
<tr id="row952014517217"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p105202513212"><a name="p105202513212"></a><a name="p105202513212"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p18520351102113"><a name="p18520351102113"></a><a name="p18520351102113"></a>VPC.2023</p>
<p id="p13520145111215"><a name="p13520145111215"></a><a name="p13520145111215"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1552075112115"><a name="p1552075112115"></a><a name="p1552075112115"></a>The internal network information of the DNAT rule conflicts with the existing one.</p>
<p id="p175201051182119"><a name="p175201051182119"></a><a name="p175201051182119"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p17520185117210"><a name="p17520185117210"></a><a name="p17520185117210"></a>The port_id, private_ip, internal port and protocol spcified have been occupied.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p175201851172110"><a name="p175201851172110"></a><a name="p175201851172110"></a>Enter the VM port ID, private IP address, or internal port that does not conflict with the existing one.</p>
<p id="p1852035110210"><a name="p1852035110210"></a><a name="p1852035110210"></a></p>
</td>
</tr>
<tr id="row75201751112114"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p8520195110212"><a name="p8520195110212"></a><a name="p8520195110212"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p0520551102115"><a name="p0520551102115"></a><a name="p0520551102115"></a>VPC.2024</p>
<p id="p75203518216"><a name="p75203518216"></a><a name="p75203518216"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1152095120216"><a name="p1152095120216"></a><a name="p1152095120216"></a>The external network information of the DNAT rule conflicts with the existing one.</p>
<p id="p115201051112116"><a name="p115201051112116"></a><a name="p115201051112116"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p13520125112119"><a name="p13520125112119"></a><a name="p13520125112119"></a>The floating ip, external port and protocol specified have been occupied.</p>
<p id="p105202051142112"><a name="p105202051142112"></a><a name="p105202051142112"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p14520751102110"><a name="p14520751102110"></a><a name="p14520751102110"></a>Enter the floating IP address ID, external port, or protocol that does not conflict with the existing one.</p>
<p id="p0520125192119"><a name="p0520125192119"></a><a name="p0520125192119"></a></p>
</td>
</tr>
<tr id="row052085114214"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p4520751142115"><a name="p4520751142115"></a><a name="p4520751142115"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p1520551122112"><a name="p1520551122112"></a><a name="p1520551122112"></a>VPC.2070</p>
<p id="p16520185172113"><a name="p16520185172113"></a><a name="p16520185172113"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p10520251142112"><a name="p10520251142112"></a><a name="p10520251142112"></a>The request information of the DNAT rule is incorrect when <strong id="b192714141361"><a name="b192714141361"></a><a name="b192714141361"></a>Port Type</strong> is set to <strong id="b19272171403612"><a name="b19272171403612"></a><a name="b19272171403612"></a>All ports</strong>.</p>
<p id="p1052075119214"><a name="p1052075119214"></a><a name="p1052075119214"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1652035112211"><a name="p1652035112211"></a><a name="p1652035112211"></a>The external port equals 0 and internal port equls 0 and protocol equals any must satisfied at the same time.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p65201510213"><a name="p65201510213"></a><a name="p65201510213"></a>Set both the internal port and the external port to <strong id="b1296134143720"><a name="b1296134143720"></a><a name="b1296134143720"></a>0</strong> and the protocol is <strong id="b7900312173716"><a name="b7900312173716"></a><a name="b7900312173716"></a>ANY</strong>.</p>
<p id="p1552018518211"><a name="p1552018518211"></a><a name="p1552018518211"></a></p>
</td>
</tr>
<tr id="row1552045119217"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p135201651102117"><a name="p135201651102117"></a><a name="p135201651102117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p9520155112119"><a name="p9520155112119"></a><a name="p9520155112119"></a>VPC.2027</p>
<p id="p1052015112219"><a name="p1052015112219"></a><a name="p1052015112219"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1952075172116"><a name="p1952075172116"></a><a name="p1952075172116"></a>The port ID of the DNAT rule conflicts with that of an existing DNAT rule.</p>
<p id="p552065112114"><a name="p552065112114"></a><a name="p552065112114"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1852019518217"><a name="p1852019518217"></a><a name="p1852019518217"></a>The port_id already existing dnat allport rules or dnat_rules, can no longer create dnat rules or dnat allport rules.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p852014515213"><a name="p852014515213"></a><a name="p852014515213"></a>Change the VM port ID to create or modify the DNAT rule.</p>
</td>
</tr>
<tr id="row5520851152112"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p10520125112218"><a name="p10520125112218"></a><a name="p10520125112218"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p12520115118212"><a name="p12520115118212"></a><a name="p12520115118212"></a>VPC.2028</p>
<p id="p105201251172116"><a name="p105201251172116"></a><a name="p105201251172116"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p452019512218"><a name="p452019512218"></a><a name="p452019512218"></a>The private IP address of the DNAT rule conflicts with that of an existing DNAT rule.</p>
<p id="p12520185102110"><a name="p12520185102110"></a><a name="p12520185102110"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p95201651112117"><a name="p95201651112117"></a><a name="p95201651112117"></a>The private_ip already existing dnat allport rules or dnat rules, can no longer create dnat rules or dnat allport rules.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p6520155142119"><a name="p6520155142119"></a><a name="p6520155142119"></a>The private IP address conflicts with the existing DNAT rule. Change the private IP address or modify the DNAT rule.</p>
</td>
</tr>
<tr id="row165202515218"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p9520115182120"><a name="p9520115182120"></a><a name="p9520115182120"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p65201251122118"><a name="p65201251122118"></a><a name="p65201251122118"></a>VPC.2029</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p18520251172112"><a name="p18520251172112"></a><a name="p18520251172112"></a>The DNAT rule has been frozen and cannot be modified.</p>
<p id="p185201551122111"><a name="p185201551122111"></a><a name="p185201551122111"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p18520135182117"><a name="p18520135182117"></a><a name="p18520135182117"></a>DNAT rule is frozen, can no longer update.</p>
<p id="p11520195192111"><a name="p11520195192111"></a><a name="p11520195192111"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p15201951122112"><a name="p15201951122112"></a><a name="p15201951122112"></a>Check whether the floating IP address bound to the DNAT rule is in arrears or whether the user account is in arrears.</p>
</td>
</tr>
<tr id="row115208515210"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1520125192111"><a name="p1520125192111"></a><a name="p1520125192111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p12520135116216"><a name="p12520135116216"></a><a name="p12520135116216"></a>VPC.2038</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p252020517212"><a name="p252020517212"></a><a name="p252020517212"></a>The maximum number of DNAT rules allowed to be associated has been reached.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p152015513218"><a name="p152015513218"></a><a name="p152015513218"></a>%(limit)s DNAT rules has been associated to this NAT Gateway, no more is allowed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p25208511217"><a name="p25208511217"></a><a name="p25208511217"></a>The maximum number of DNAT rules allowed to be associated with the NAT gateway has been reached.</p>
</td>
</tr>
<tr id="row05201051122111"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p752055122117"><a name="p752055122117"></a><a name="p752055122117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p7520115115219"><a name="p7520115115219"></a><a name="p7520115115219"></a>VPC.2055</p>
<p id="p10520551102117"><a name="p10520551102117"></a><a name="p10520551102117"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1552035111211"><a name="p1552035111211"></a><a name="p1552035111211"></a>The DNAT rule contains mutually exclusive parameters.</p>
<p id="p18520185113217"><a name="p18520185113217"></a><a name="p18520185113217"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1252016514215"><a name="p1252016514215"></a><a name="p1252016514215"></a>The port_id and private_ip exist at the same time and value is not empty, but at least one value is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p2520135172112"><a name="p2520135172112"></a><a name="p2520135172112"></a>The VM port ID and private IP address cannot be configured at the same time.</p>
<p id="p45201851182115"><a name="p45201851182115"></a><a name="p45201851182115"></a></p>
</td>
</tr>
<tr id="row85201851162111"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p12520175110213"><a name="p12520175110213"></a><a name="p12520175110213"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p8520125192119"><a name="p8520125192119"></a><a name="p8520125192119"></a>VPC.2056</p>
<p id="p5520195152115"><a name="p5520195152115"></a><a name="p5520195152115"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p5520551182110"><a name="p5520551182110"></a><a name="p5520551182110"></a>The DNAT rule does not have some required parameters.</p>
<p id="p1752012516218"><a name="p1752012516218"></a><a name="p1752012516218"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p17520551162114"><a name="p17520551162114"></a><a name="p17520551162114"></a>The port_id and private_ip values are both empty, at least one value is not empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1852075114214"><a name="p1852075114214"></a><a name="p1852075114214"></a>Configure the VM port ID and private IP address.</p>
<p id="p185207512213"><a name="p185207512213"></a><a name="p185207512213"></a></p>
</td>
</tr>
<tr id="row7520205115218"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p8520105113211"><a name="p8520105113211"></a><a name="p8520105113211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p19520751192114"><a name="p19520751192114"></a><a name="p19520751192114"></a>VPC.2071</p>
<p id="p145201351132115"><a name="p145201351132115"></a><a name="p145201351132115"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p115208516213"><a name="p115208516213"></a><a name="p115208516213"></a>Invalid private IP address of the DNAT rule.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p9520851172111"><a name="p9520851172111"></a><a name="p9520851172111"></a>The private ip address is not legal.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p205201051132111"><a name="p205201051132111"></a><a name="p205201051132111"></a>Configure a valid private IP address.</p>
<p id="p15203518212"><a name="p15203518212"></a><a name="p15203518212"></a></p>
</td>
</tr>
<tr id="row7520951182114"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p1752010516211"><a name="p1752010516211"></a><a name="p1752010516211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p35204515211"><a name="p35204515211"></a><a name="p35204515211"></a>VPC.2037</p>
<p id="p11520051112115"><a name="p11520051112115"></a><a name="p11520051112115"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p85200515217"><a name="p85200515217"></a><a name="p85200515217"></a>This virtual IP address is not supported. </p>
<p id="p175203514212"><a name="p175203514212"></a><a name="p175203514212"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p16520135112119"><a name="p16520135112119"></a><a name="p16520135112119"></a>The virtual IP address is not supported.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p145201651152118"><a name="p145201651152118"></a><a name="p145201651152118"></a>Configure a valid private IP address.</p>
</td>
</tr>
<tr id="row1952018516212"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p135201651192119"><a name="p135201651192119"></a><a name="p135201651192119"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p452085132113"><a name="p452085132113"></a><a name="p452085132113"></a>VPC.2026</p>
<p id="p252018512212"><a name="p252018512212"></a><a name="p252018512212"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1352025132113"><a name="p1352025132113"></a><a name="p1352025132113"></a>The maximum number of DNAT rules allowed to be associated has been reached.</p>
<p id="p1152010517213"><a name="p1152010517213"></a><a name="p1152010517213"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1152015519217"><a name="p1152015519217"></a><a name="p1152015519217"></a>%(limit)s DNAT rules has been associated to this Floating IP, no more is allowed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p152015514216"><a name="p152015514216"></a><a name="p152015514216"></a>The maximum number of DNAT rules allowed to be associated with a floating IP address has been reached.</p>
<p id="p2520165113219"><a name="p2520165113219"></a><a name="p2520165113219"></a></p>
</td>
</tr>
<tr id="row175201351132117"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p3520551152110"><a name="p3520551152110"></a><a name="p3520551152110"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p152035118216"><a name="p152035118216"></a><a name="p152035118216"></a>VPC.2057</p>
<p id="p1520135117216"><a name="p1520135117216"></a><a name="p1520135117216"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p155201351172112"><a name="p155201351172112"></a><a name="p155201351172112"></a>The maximum number of DNAT rules allowed to be created in batches exceeds the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p3520125111213"><a name="p3520125111213"></a><a name="p3520125111213"></a>batch create dnat rules max limit: %(limit)s</p>
<p id="p1252015182110"><a name="p1252015182110"></a><a name="p1252015182110"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p252015510217"><a name="p252015510217"></a><a name="p252015510217"></a>The maximum number of DNAT rules allowed to be created in batches exceeds the upper limit.</p>
<p id="p952035172117"><a name="p952035172117"></a><a name="p952035172117"></a></p>
</td>
</tr>
<tr id="row115200512213"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p75205518214"><a name="p75205518214"></a><a name="p75205518214"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p552045152116"><a name="p552045152116"></a><a name="p552045152116"></a>VPC.2022</p>
<p id="p0520451102119"><a name="p0520451102119"></a><a name="p0520451102119"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p2520185162111"><a name="p2520185162111"></a><a name="p2520185162111"></a>Invalid VM port ID of the DNAT rule.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p352055182115"><a name="p352055182115"></a><a name="p352055182115"></a>Port %(port)s is not a valid port.</p>
<p id="p1352018519217"><a name="p1352018519217"></a><a name="p1352018519217"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p35201651142116"><a name="p35201651142116"></a><a name="p35201651142116"></a>Configure a valid VM port ID.</p>
<p id="p95201051172116"><a name="p95201051172116"></a><a name="p95201051172116"></a></p>
</td>
</tr>
<tr id="row11520135192112"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p3520195113211"><a name="p3520195113211"></a><a name="p3520195113211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p1452016514213"><a name="p1452016514213"></a><a name="p1452016514213"></a>VPC.2058</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p17520185182113"><a name="p17520185182113"></a><a name="p17520185182113"></a>The value of <strong id="b15851317191916"><a name="b15851317191916"></a><a name="b15851317191916"></a>VtepIp</strong> must be specified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p2520125172113"><a name="p2520125172113"></a><a name="p2520125172113"></a>Vtep_ip is Null.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p2520175142114"><a name="p2520175142114"></a><a name="p2520175142114"></a>Contact technical support.</p>
</td>
</tr>
<tr id="row1952075110212"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p8536151132112"><a name="p8536151132112"></a><a name="p8536151132112"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p6536135162110"><a name="p6536135162110"></a><a name="p6536135162110"></a>VPC.2075</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p125367511211"><a name="p125367511211"></a><a name="p125367511211"></a>The description contains more than 255 characters.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p653611512218"><a name="p653611512218"></a><a name="p653611512218"></a>Enter a maximum of 255 characters.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p16536135114216"><a name="p16536135114216"></a><a name="p16536135114216"></a>Enter a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row5536451132112"><td class="cellrowborder" rowspan="7" valign="top" width="7.140714071407141%" headers="mcps1.1.7.1.1 "><p id="p12536851102119"><a name="p12536851102119"></a><a name="p12536851102119"></a>EIP</p>
</td>
<td class="cellrowborder" valign="top" width="8.54085408540854%" headers="mcps1.1.7.1.2 "><p id="p653685116211"><a name="p653685116211"></a><a name="p653685116211"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="13.511351135113511%" headers="mcps1.1.7.1.3 "><p id="p353612512213"><a name="p353612512213"></a><a name="p353612512213"></a>VPC.2059</p>
<p id="p1053615510217"><a name="p1053615510217"></a><a name="p1053615510217"></a></p>
</td>
<td class="cellrowborder" valign="top" width="15.701570157015702%" headers="mcps1.1.7.1.4 "><p id="p115367515213"><a name="p115367515213"></a><a name="p115367515213"></a>The EIP is frozen.</p>
<p id="p1553655162110"><a name="p1553655162110"></a><a name="p1553655162110"></a></p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.5 "><p id="p8536185142113"><a name="p8536185142113"></a><a name="p8536185142113"></a>Floating Ip %(fip)s is freezed.</p>
</td>
<td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.1.7.1.6 "><p id="p125361514217"><a name="p125361514217"></a><a name="p125361514217"></a>Select an EIP that has not been frozen.</p>
<p id="p145361551182117"><a name="p145361551182117"></a><a name="p145361551182117"></a></p>
</td>
</tr>
<tr id="row35361951132113"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p853675111212"><a name="p853675111212"></a><a name="p853675111212"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p35369513214"><a name="p35369513214"></a><a name="p35369513214"></a>VPC.2060</p>
<p id="p35368517214"><a name="p35368517214"></a><a name="p35368517214"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1453613512211"><a name="p1453613512211"></a><a name="p1453613512211"></a>The EIP has been associated with a port.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p15361351132110"><a name="p15361351132110"></a><a name="p15361351132110"></a>Floating Ip %(fip)s has associated with port %(port)s.</p>
<p id="p15536751192112"><a name="p15536751192112"></a><a name="p15536751192112"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p12536155182116"><a name="p12536155182116"></a><a name="p12536155182116"></a>Select an EIP that has not been bound to any other object. For example, if an EIP has been bound to an ECS, it cannot be bound to a NAT gateway.</p>
</td>
</tr>
<tr id="row195361451182112"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p175361517213"><a name="p175361517213"></a><a name="p175361517213"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p1853613519210"><a name="p1853613519210"></a><a name="p1853613519210"></a>VPC.2061</p>
<p id="p175361051112113"><a name="p175361051112113"></a><a name="p175361051112113"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p195361651132115"><a name="p195361651132115"></a><a name="p195361651132115"></a>The EIP has been associated with a NAT gateway.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1053616513212"><a name="p1053616513212"></a><a name="p1053616513212"></a>Floating Ip %(fip)s has used by nat gateway %(nat_gateway)s.</p>
<p id="p85364513215"><a name="p85364513215"></a><a name="p85364513215"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p353645115216"><a name="p353645115216"></a><a name="p353645115216"></a>The EIP has been bound to a NAT gateway. Select another one.</p>
<p id="p1553685192117"><a name="p1553685192117"></a><a name="p1553685192117"></a></p>
</td>
</tr>
<tr id="row195361051172110"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p2053655118215"><a name="p2053655118215"></a><a name="p2053655118215"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p45361651112120"><a name="p45361651112120"></a><a name="p45361651112120"></a>VPC.2062</p>
<p id="p145361951202114"><a name="p145361951202114"></a><a name="p145361951202114"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p145361751152110"><a name="p145361751152110"></a><a name="p145361751152110"></a>The EIP is in use.</p>
<p id="p1853618512218"><a name="p1853618512218"></a><a name="p1853618512218"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p105361551172112"><a name="p105361551172112"></a><a name="p105361551172112"></a>Floating Ip %(fip)s has been occupied.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p125364514215"><a name="p125364514215"></a><a name="p125364514215"></a>The EIP has been bound to a NAT gateway. Select another one.</p>
</td>
</tr>
<tr id="row1253610517214"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p5536105162117"><a name="p5536105162117"></a><a name="p5536105162117"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p4536151142118"><a name="p4536151142118"></a><a name="p4536151142118"></a>VPC.2074</p>
<p id="p125362051122113"><a name="p125362051122113"></a><a name="p125362051122113"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p1453605132112"><a name="p1453605132112"></a><a name="p1453605132112"></a>An EIP cannot be associated with an SNAT rule and a DNAT rule with <strong id="b15610171514279"><a name="b15610171514279"></a><a name="b15610171514279"></a>Port Type</strong> set to <strong id="b64941105278"><a name="b64941105278"></a><a name="b64941105278"></a>All ports</strong> at the same time.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1853605116211"><a name="p1853605116211"></a><a name="p1853605116211"></a>Floating Ip %(fip)s can not be associated with both SNAT rule and DNAT all port rule.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p1536185112218"><a name="p1536185112218"></a><a name="p1536185112218"></a>Do not associate an EIP with an SNAT rule and a DNAT rule with <strong id="b1292273212276"><a name="b1292273212276"></a><a name="b1292273212276"></a>Port Type</strong> set to <strong id="b13922133212278"><a name="b13922133212278"></a><a name="b13922133212278"></a>All ports</strong> at the same time.</p>
</td>
</tr>
<tr id="row105361451112111"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p953617512216"><a name="p953617512216"></a><a name="p953617512216"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p1453618517213"><a name="p1453618517213"></a><a name="p1453618517213"></a>VPC.2073</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p12536185110212"><a name="p12536185110212"></a><a name="p12536185110212"></a>An EIP cannot be associated with a DNAT rule and a DNAT rule with <strong id="b81177144284"><a name="b81177144284"></a><a name="b81177144284"></a>Port Type</strong> set to <strong id="b1211901418287"><a name="b1211901418287"></a><a name="b1211901418287"></a>All ports</strong> at the same time.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p1653615519214"><a name="p1653615519214"></a><a name="p1653615519214"></a>Floating Ip %(fip)s can not be associated with both DNAT rule and DNAT all port rule.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p9536451132116"><a name="p9536451132116"></a><a name="p9536451132116"></a>Do not associate an EIP with a DNAT rule and a DNAT rule with <strong id="b14477929142814"><a name="b14477929142814"></a><a name="b14477929142814"></a>Port Type</strong> set to <strong id="b1747810291287"><a name="b1747810291287"></a><a name="b1747810291287"></a>All ports</strong> at the same time.</p>
</td>
</tr>
<tr id="row853619519218"><td class="cellrowborder" valign="top" headers="mcps1.1.7.1.1 "><p id="p25363517217"><a name="p25363517217"></a><a name="p25363517217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.2 "><p id="p7536351172117"><a name="p7536351172117"></a><a name="p7536351172117"></a>VPC.2043</p>
<p id="p145361351142119"><a name="p145361351142119"></a><a name="p145361351142119"></a></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.3 "><p id="p15536151202117"><a name="p15536151202117"></a><a name="p15536151202117"></a>The EIP has been associated with a rule.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.4 "><p id="p15536165172117"><a name="p15536165172117"></a><a name="p15536165172117"></a>Floating Ip %(fip)s is used by other rules</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.7.1.5 "><p id="p105364512211"><a name="p105364512211"></a><a name="p105364512211"></a>Select an EIP that is not in use.</p>
<p id="p19536175116211"><a name="p19536175116211"></a><a name="p19536175116211"></a></p>
</td>
</tr>
</tbody>
</table>

