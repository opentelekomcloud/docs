# Querying Whitelists<a name="EN-US_TOPIC_0143878052"></a>

## Function<a name="section54348282"></a>

This API is used to query the whitelists. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

## URI<a name="section19372497"></a>

GET /v2.0/lbaas/whitelists

## Constraints<a name="section1642041515445"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="section40134753"></a>

**Table  1**  Request parameters

<a name="table57586824"></a>
<table><thead align="left"><tr id="row30755174"><th class="cellrowborder" valign="top" width="24.717528247175284%" id="mcps1.2.5.1.1"><p id="p8141195"><a name="p8141195"></a><a name="p8141195"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.478352164783523%" id="mcps1.2.5.1.2"><p id="p62838551"><a name="p62838551"></a><a name="p62838551"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.108689131086889%" id="mcps1.2.5.1.3"><p id="p55457081"><a name="p55457081"></a><a name="p55457081"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.695430456954305%" id="mcps1.2.5.1.4"><p id="p2035876173816"><a name="p2035876173816"></a><a name="p2035876173816"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33982084"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p1085411"><a name="p1085411"></a><a name="p1085411"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p7847228"><a name="p7847228"></a><a name="p7847228"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="p127181511386"><a name="p127181511386"></a><a name="p127181511386"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.695430456954305%" headers="mcps1.2.5.1.4 "><p id="p4235152211344"><a name="p4235152211344"></a><a name="p4235152211344"></a>Specifies the ID of the whitelist from which pagination query starts, that is, the ID of the last whitelist on the previous page.</p>
<p id="p06221826143418"><a name="p06221826143418"></a><a name="p06221826143418"></a>This parameter must be used together with <strong id="b1135115312501"><a name="b1135115312501"></a><a name="b1135115312501"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row51375689"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p681306"><a name="p681306"></a><a name="p681306"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p40870010"><a name="p40870010"></a><a name="p40870010"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="p55185864"><a name="p55185864"></a><a name="p55185864"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.695430456954305%" headers="mcps1.2.5.1.4 "><p id="p163282306342"><a name="p163282306342"></a><a name="p163282306342"></a>Specifies the number of whitelists on each page.</p>
<p id="p8300236113416"><a name="p8300236113416"></a><a name="p8300236113416"></a>The value ranges from <strong id="b103431150115018"><a name="b103431150115018"></a><a name="b103431150115018"></a>0</strong> to <strong id="b153455503502"><a name="b153455503502"></a><a name="b153455503502"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row48229068"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p14240444"><a name="p14240444"></a><a name="p14240444"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p16016049"><a name="p16016049"></a><a name="p16016049"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="p12625296"><a name="p12625296"></a><a name="p12625296"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.695430456954305%" headers="mcps1.2.5.1.4 "><p id="p15227113913341"><a name="p15227113913341"></a><a name="p15227113913341"></a>Specifies the page direction. The value can be <strong id="b390065817354"><a name="b390065817354"></a><a name="b390065817354"></a>true</strong> or <strong id="b1290075819353"><a name="b1290075819353"></a><a name="b1290075819353"></a>false</strong>, and the default value is <strong id="b15901155813351"><a name="b15901155813351"></a><a name="b15901155813351"></a>false</strong>. The last page in the list requested with <strong id="b5902135812359"><a name="b5902135812359"></a><a name="b5902135812359"></a>page_reverse</strong> set to <strong id="b17902858113520"><a name="b17902858113520"></a><a name="b17902858113520"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b190375818355"><a name="b190375818355"></a><a name="b190375818355"></a>page_reverse</strong> set to <strong id="b99031858183513"><a name="b99031858183513"></a><a name="b99031858183513"></a>true</strong> will not contain the "previous" link.</p>
<p id="p5244104243413"><a name="p5244104243413"></a><a name="p5244104243413"></a>This parameter must be used together with <strong id="b77778512509"><a name="b77778512509"></a><a name="b77778512509"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row33569718"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p34792670"><a name="p34792670"></a><a name="p34792670"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p37463366"><a name="p37463366"></a><a name="p37463366"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="p15526337193815"><a name="p15526337193815"></a><a name="p15526337193815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.695430456954305%" headers="mcps1.2.5.1.4 "><p id="p14633815"><a name="p14633815"></a><a name="p14633815"></a>Specifies the whitelist ID.</p>
</td>
</tr>
<tr id="row64595475"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p64851000"><a name="p64851000"></a><a name="p64851000"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p17215303"><a name="p17215303"></a><a name="p17215303"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="p18439633"><a name="p18439633"></a><a name="p18439633"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.695430456954305%" headers="mcps1.2.5.1.4 "><p id="p40275672"><a name="p40275672"></a><a name="p40275672"></a>Specifies the ID of the project where the whitelist is used.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row598411"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p48471335"><a name="p48471335"></a><a name="p48471335"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p58634288"><a name="p58634288"></a><a name="p58634288"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="p6640940193810"><a name="p6640940193810"></a><a name="p6640940193810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.695430456954305%" headers="mcps1.2.5.1.4 "><p id="p24747384"><a name="p24747384"></a><a name="p24747384"></a>Specifies the ID of the listener to which the whitelist is added.</p>
</td>
</tr>
<tr id="row63159007"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p15605948"><a name="p15605948"></a><a name="p15605948"></a>enable_whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p49611956"><a name="p49611956"></a><a name="p49611956"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="p56122294"><a name="p56122294"></a><a name="p56122294"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="45.695430456954305%" headers="mcps1.2.5.1.4 "><p id="p31687177"><a name="p31687177"></a><a name="p31687177"></a>Specifies whether to enable access control.</p>
<p id="p07333135114"><a name="p07333135114"></a><a name="p07333135114"></a><strong id="b111775845010"><a name="b111775845010"></a><a name="b111775845010"></a>true</strong>: Access control is enabled.</p>
<p id="p57393175115"><a name="p57393175115"></a><a name="p57393175115"></a><strong id="b864165905011"><a name="b864165905011"></a><a name="b864165905011"></a>false</strong>: Access control is disabled.</p>
</td>
</tr>
<tr id="row62547480"><td class="cellrowborder" valign="top" width="24.717528247175284%" headers="mcps1.2.5.1.1 "><p id="p33181137"><a name="p33181137"></a><a name="p33181137"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="16.478352164783523%" headers="mcps1.2.5.1.2 "><p id="p285771"><a name="p285771"></a><a name="p285771"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="p3317546"><a name="p3317546"></a><a name="p3317546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.695430456954305%" headers="mcps1.2.5.1.4 "><p id="p61076600"><a name="p61076600"></a><a name="p61076600"></a>Specifies the IP addresses in the whitelist.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section25668457"></a>

**Table  2**  Response parameters

<a name="table51071350"></a>
<table><thead align="left"><tr id="row44858696"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p9675774"><a name="p9675774"></a><a name="p9675774"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p45540236"><a name="p45540236"></a><a name="p45540236"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p64880539"><a name="p64880539"></a><a name="p64880539"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20832339"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p9697883"><a name="p9697883"></a><a name="p9697883"></a>whitelists</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p892419588196"><a name="p892419588196"></a><a name="p892419588196"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p8608636"><a name="p8608636"></a><a name="p8608636"></a>Lists the whitelists. For details, see <a href="#table10368864">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **whitelist**  parameter description

<a name="table10368864"></a>
<table><thead align="left"><tr id="row37967333"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p55455104"><a name="p55455104"></a><a name="p55455104"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p62678444"><a name="p62678444"></a><a name="p62678444"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p43789200"><a name="p43789200"></a><a name="p43789200"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row57264341"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p7900067"><a name="p7900067"></a><a name="p7900067"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p133511948124317"><a name="p133511948124317"></a><a name="p133511948124317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p62933377"><a name="p62933377"></a><a name="p62933377"></a>Specifies the whitelist ID.</p>
</td>
</tr>
<tr id="row17352883"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p63406273"><a name="p63406273"></a><a name="p63406273"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p35634492"><a name="p35634492"></a><a name="p35634492"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1927617501235"><a name="p1927617501235"></a><a name="p1927617501235"></a>Specifies the ID of the project where the whitelist is used.</p>
<p id="p630013400352"><a name="p630013400352"></a><a name="p630013400352"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row6414438"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p49807439"><a name="p49807439"></a><a name="p49807439"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p7870720"><a name="p7870720"></a><a name="p7870720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1627615010317"><a name="p1627615010317"></a><a name="p1627615010317"></a>Specifies the ID of the listener to which the whitelist is added.</p>
</td>
</tr>
<tr id="row33501748"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p29287106"><a name="p29287106"></a><a name="p29287106"></a>enable_whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p23445396"><a name="p23445396"></a><a name="p23445396"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p72761950830"><a name="p72761950830"></a><a name="p72761950830"></a>Specifies whether to enable access control.</p>
<p id="p202761501737"><a name="p202761501737"></a><a name="p202761501737"></a><strong id="b1819373155120"><a name="b1819373155120"></a><a name="b1819373155120"></a>true</strong>: Access control is enabled.</p>
<p id="p92762509318"><a name="p92762509318"></a><a name="p92762509318"></a><strong id="b1814373216517"><a name="b1814373216517"></a><a name="b1814373216517"></a>false</strong>: Access control is disabled.</p>
</td>
</tr>
<tr id="row46042798"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p38479195"><a name="p38479195"></a><a name="p38479195"></a>whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p29807080"><a name="p29807080"></a><a name="p29807080"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1627714507313"><a name="p1627714507313"></a><a name="p1627714507313"></a>Specifies the IP addresses in the whitelist.</p>
</td>
</tr>
<tr id="row53198443"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1932512294547"><a name="p1932512294547"></a><a name="p1932512294547"></a>whitelists_links</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p11698122122015"><a name="p11698122122015"></a><a name="p11698122122015"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p5542991616"><a name="p5542991616"></a><a name="p5542991616"></a>Provides links to the previous or next page during pagination query, respectively.</p>
<p id="p165764116119"><a name="p165764116119"></a><a name="p165764116119"></a>This parameter exists only in the response body of pagination query.</p>
<p id="p53635145114"><a name="p53635145114"></a><a name="p53635145114"></a>For details, see <a href="#table24944072">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **whitelists\_links**  parameter description

<a name="table24944072"></a>
<table><thead align="left"><tr id="row49248941"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p29741298"><a name="p29741298"></a><a name="p29741298"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p60234923"><a name="p60234923"></a><a name="p60234923"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p47190593"><a name="p47190593"></a><a name="p47190593"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64341659"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p44291873"><a name="p44291873"></a><a name="p44291873"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p156227148448"><a name="p156227148448"></a><a name="p156227148448"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p1653852193312"><a name="en-us_topic_0096561531_p1653852193312"></a><a name="en-us_topic_0096561531_p1653852193312"></a>Provides links to the previous or next page during pagination query, respectively.</p>
</td>
</tr>
<tr id="row24216442"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p15374808"><a name="p15374808"></a><a name="p15374808"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p37399910"><a name="p37399910"></a><a name="p37399910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1772113411218"><a name="p1772113411218"></a><a name="p1772113411218"></a>Specifies the prompt of the previous or next page.</p>
<p id="p422510443113"><a name="p422510443113"></a><a name="p422510443113"></a>The value can be <strong id="b10782114918516"><a name="b10782114918516"></a><a name="b10782114918516"></a>next</strong> or <strong id="b57831049185110"><a name="b57831049185110"></a><a name="b57831049185110"></a>previous</strong>. The value <strong id="b137025114515"><a name="b137025114515"></a><a name="b137025114515"></a>next</strong> indicates the href containing the URL of the next page, and <strong id="b1571175145112"><a name="b1571175145112"></a><a name="b1571175145112"></a>previous</strong> indicates the href containing the URL of the previous page.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section96772101512"></a>

-   Example request 1: Querying all whitelists

    ```
    GET https://{Endpoint}/v2.0/lbaas/whitelists
    ```

-   Example response 1

    ```
    { 
        "whitelists": [ 
            { 
                "id": "eabfefa3fd1740a88a47ad98e132d238",  
                "listener_id": "eabfefa3fd1740a88a47ad98e132d238",  
                "tenant_id": "eabfefa3fd1740a88a47ad98e132d238",  
                "enable_whitelist": true,  
                "whitelist": "192.168.11.1,192.168.0.1/24,192.168.201.18/8,100.164.0.1/24" 
            },  
            { 
                "id": "eabfefa3fd1740a88a47ad98e132d326",  
                "listener_id": "eabfefa3fd1740a88a47ad98e132d327",  
                "tenant_id": "eabfefa3fd1740a88a47ad98e132d436",  
                "enable_whitelist": true,  
                "whiltelist": "192.168.12.1,192.168.1.1/24,192.168.203.18/8,100.164.5.1/24" 
            } 
        ] 
    }
    ```

-   Example request 2: Filtering the whitelists added to listener eabfefa3fd1740a88a47ad98e132d230

    ```
    GET https://{Endpoint}/v2.0/lbaas/whitelists?listener_id=eabfefa3fd1740a88a47ad98e132d230
    ```

-   Example response 2

    ```
    { 
        "whitelists": [ 
            { 
                "id": "eabfefa3fd1740a88a47ad98e132d238",  
                "listener_id": "eabfefa3fd1740a88a47ad98e132d230",  
                "tenant_id": "eabfefa3fd1740a88a47ad98e132d239",  
                "enable_whitelist": true,  
                "whitelist": "192.168.11.1,192.168.0.1/24,192.168.201.18/8,100.164.0.1/24" 
            },  
            { 
                "id": "eabfefa3fd1740a88a47ad98e132d326",  
                "listener_id": "eabfefa3fd1740a88a47ad98e132d327",  
                "tenant_id": "eabfefa3fd1740a88a47ad98e132d439",  
                "enable_whitelist": true,  
                "whiltelist": "192.168.12.1,192.168.1.1/24,192.168.203.18/8,100.164.5.1/24" 
            } 
        ] 
    }
    ```


## Status Code<a name="section1998814713716"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

