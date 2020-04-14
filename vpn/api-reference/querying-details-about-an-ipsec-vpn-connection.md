# Querying Details About an IPsec VPN Connection<a name="en_topic_0093011493"></a>

## **Function**<a name="section62260885"></a>

This interface is used to query details about an IPsec VPN connection.

## URI<a name="section23477058"></a>

GET /v2.0/vpn/ipsec-site-connections/\{connection\_id\}

**Table  1**  Parameter description

<a name="table975465201311"></a>
<table><thead align="left"><tr id="row576295251316"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p9762252151315"><a name="p9762252151315"></a><a name="p9762252151315"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p14769952101319"><a name="p14769952101319"></a><a name="p14769952101319"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p17769152151313"><a name="p17769152151313"></a><a name="p17769152151313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p14769852121311"><a name="p14769852121311"></a><a name="p14769852121311"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1176955271315"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p77775524139"><a name="p77775524139"></a><a name="p77775524139"></a>connection_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1277795291312"><a name="p1277795291312"></a><a name="p1277795291312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p87779521134"><a name="p87779521134"></a><a name="p87779521134"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p277775214138"><a name="p277775214138"></a><a name="p277775214138"></a>Specifies the IPsec VPN connection ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section22593558"></a>

None

## Response Message<a name="section2015430"></a>

[Table 2](#table21749220)  describes the response parameters.

**Table  2**  Response parameters

<a name="table21749220"></a>
<table><thead align="left"><tr id="row63149496"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p60827539"><a name="p60827539"></a><a name="p60827539"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42890904"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p51611184"><a name="p51611184"></a><a name="p51611184"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19756352"><a name="p19756352"></a><a name="p19756352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34213098"><a name="p34213098"></a><a name="p34213098"></a>Specifies the endpoint group ID (VPC subnets).</p>
</td>
</tr>
<tr id="row39482434"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43960571"><a name="p43960571"></a><a name="p43960571"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p4036497"><a name="p4036497"></a><a name="p4036497"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42565233"><a name="p42565233"></a><a name="p42565233"></a>Specifies the IPsec VPN connection status. The value can be <strong id="b842352706164927"><a name="b842352706164927"></a><a name="b842352706164927"></a>ACTIVE</strong>,&nbsp;<strong id="b842352706164931"><a name="b842352706164931"></a><a name="b842352706164931"></a>DOWN</strong>,&nbsp;<strong id="b842352706164935"><a name="b842352706164935"></a><a name="b842352706164935"></a>BUILD</strong>,&nbsp;<strong id="b842352706164939"><a name="b842352706164939"></a><a name="b842352706164939"></a>ERROR</strong>,&nbsp;<strong id="b842352706164943"><a name="b842352706164943"></a><a name="b842352706164943"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b842352706164948"><a name="b842352706164948"></a><a name="b842352706164948"></a>PENDING_UPDATE</strong>, or&nbsp;<strong id="b84235270616508"><a name="b84235270616508"></a><a name="b84235270616508"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row47542785"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25760373"><a name="p25760373"></a><a name="p25760373"></a>psk</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p6215498"><a name="p6215498"></a><a name="p6215498"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p44806966"><a name="p44806966"></a><a name="p44806966"></a>Specifies the pre-shared key.</p>
</td>
</tr>
<tr id="row609510"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p49370368"><a name="p49370368"></a><a name="p49370368"></a>initiator</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p39576862"><a name="p39576862"></a><a name="p39576862"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p19600264"><a name="p19600264"></a><a name="p19600264"></a>Specifies whether this VPN can only respond to connections or both respond to and initiate connections.</p>
</td>
</tr>
<tr id="row42184651"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p61513540"><a name="p61513540"></a><a name="p61513540"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16540805"><a name="p16540805"></a><a name="p16540805"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9191297"><a name="p9191297"></a><a name="p9191297"></a>Specifies the IPsec VPN connection name.</p>
</td>
</tr>
<tr id="row15612815"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p56678513"><a name="p56678513"></a><a name="p56678513"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27556864"><a name="p27556864"></a><a name="p27556864"></a>Boo</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9307971"><a name="p9307971"></a><a name="p9307971"></a>Specifies the administrative status. The value can be <strong id="b842352706221557"><a name="b842352706221557"></a><a name="b842352706221557"></a>true</strong>&nbsp;or&nbsp;<strong id="b84235270622160"><a name="b84235270622160"></a><a name="b84235270622160"></a>false</strong>.</p>
</td>
</tr>
<tr id="row16662877"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p7515778"><a name="p7515778"></a><a name="p7515778"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p4798296"><a name="p4798296"></a><a name="p4798296"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p7566645"><a name="p7566645"></a><a name="p7566645"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row990949"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p13158007"><a name="p13158007"></a><a name="p13158007"></a>ipsecpolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p59165662"><a name="p59165662"></a><a name="p59165662"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28244554"><a name="p28244554"></a><a name="p28244554"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
<tr id="row52874399"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p54967961"><a name="p54967961"></a><a name="p54967961"></a>auth_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p23219884"><a name="p23219884"></a><a name="p23219884"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8539194"><a name="p8539194"></a><a name="p8539194"></a>Specifies the authentication mode. The default value is <strong id="b84235270616111"><a name="b84235270616111"></a><a name="b84235270616111"></a>psk</strong>.</p>
</td>
</tr>
<tr id="row9743886"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p51057338"><a name="p51057338"></a><a name="p51057338"></a>peer_cidrs</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24856892"><a name="p24856892"></a><a name="p24856892"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37160390"><a name="p37160390"></a><a name="p37160390"></a>(Deprecated) Specifies the tenant's CIDR blocks. The value is in the form of <em id="i842352697222235"><a name="i842352697222235"></a><a name="i842352697222235"></a>&lt;net_address &gt; / &lt; prefix &gt;</em>.</p>
</td>
</tr>
<tr id="row66008059"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45052529"><a name="p45052529"></a><a name="p45052529"></a>mtu</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25376232"><a name="p25376232"></a><a name="p25376232"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p63478007"><a name="p63478007"></a><a name="p63478007"></a>Specifies the maximum transmission unit to address fragmentation.</p>
</td>
</tr>
<tr id="row34431157"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p37460321"><a name="p37460321"></a><a name="p37460321"></a>ikepolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14387121"><a name="p14387121"></a><a name="p14387121"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p38839134"><a name="p38839134"></a><a name="p38839134"></a>Specifies the IKE policy ID.</p>
</td>
</tr>
<tr id="row14007894"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p60897649"><a name="p60897649"></a><a name="p60897649"></a>peer_address</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p33762549"><a name="p33762549"></a><a name="p33762549"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p56833109"><a name="p56833109"></a><a name="p56833109"></a>Specifies the remote gateway address.</p>
</td>
</tr>
<tr id="row41735936"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25167636"><a name="p25167636"></a><a name="p25167636"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25312629"><a name="p25312629"></a><a name="p25312629"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p48829755"><a name="p48829755"></a><a name="p48829755"></a>Specifies the IPsec VPN connection ID.</p>
</td>
</tr>
<tr id="row36814618"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p29194114"><a name="p29194114"></a><a name="p29194114"></a>ipsec_site_connection</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p15913018"><a name="p15913018"></a><a name="p15913018"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p51028923"><a name="p51028923"></a><a name="p51028923"></a>Specifies the IPsec VPN connection object.</p>
</td>
</tr>
<tr id="row56607127"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21774588"><a name="p21774588"></a><a name="p21774588"></a>route_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18911189"><a name="p18911189"></a><a name="p18911189"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59133445"><a name="p59133445"></a><a name="p59133445"></a>Specifies the route advertising mode. The default value is <strong id="b409160175141644"><a name="b409160175141644"></a><a name="b409160175141644"></a>static</strong>.</p>
</td>
</tr>
<tr id="row62438959"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24390923"><a name="p24390923"></a><a name="p24390923"></a>peer_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p29507743"><a name="p29507743"></a><a name="p29507743"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p58343698"><a name="p58343698"></a><a name="p58343698"></a>Specifies the remote gateway ID.</p>
</td>
</tr>
<tr id="row55331235"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52645056"><a name="p52645056"></a><a name="p52645056"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p36391162"><a name="p36391162"></a><a name="p36391162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p56187107"><a name="p56187107"></a><a name="p56187107"></a>Provides supplementary information about the IPsec VPN connection.</p>
</td>
</tr>
<tr id="row35921916"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23994101"><a name="p23994101"></a><a name="p23994101"></a>interval</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64473998"><a name="p64473998"></a><a name="p64473998"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p26731201"><a name="p26731201"></a><a name="p26731201"></a>Specifies the DPD interval in seconds. The default value is <strong id="b460615530142328"><a name="b460615530142328"></a><a name="b460615530142328"></a>30</strong>.</p>
</td>
</tr>
<tr id="row39254219"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25475209"><a name="p25475209"></a><a name="p25475209"></a>peer_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50226059"><a name="p50226059"></a><a name="p50226059"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p28655997"><a name="p28655997"></a><a name="p28655997"></a>Specifies the endpoint group ID (tenant CIDR blocks).</p>
</td>
</tr>
<tr id="row56577386"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p19365543"><a name="p19365543"></a><a name="p19365543"></a>dpd</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25105132"><a name="p25105132"></a><a name="p25105132"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p29623216"><a name="p29623216"></a><a name="p29623216"></a>Specifies the DPD protocol control.</p>
</td>
</tr>
<tr id="row65282360"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p53379839"><a name="p53379839"></a><a name="p53379839"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28799665"><a name="p28799665"></a><a name="p28799665"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p43154428"><a name="p43154428"></a><a name="p43154428"></a>Specifies the DPD timeout. The default value is 120 seconds.</p>
</td>
</tr>
<tr id="row52845536"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52630025"><a name="p52630025"></a><a name="p52630025"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p35173667"><a name="p35173667"></a><a name="p35173667"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p54160201"><a name="p54160201"></a><a name="p54160201"></a>Specifies the DPD action. The value can be <strong id="b842352706165431"><a name="b842352706165431"></a><a name="b842352706165431"></a>clear</strong>,&nbsp;<strong id="b842352706165434"><a name="b842352706165434"></a><a name="b842352706165434"></a>hold</strong>,&nbsp;<strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>restart</strong>,&nbsp;<strong id="b842352706165443"><a name="b842352706165443"></a><a name="b842352706165443"></a>disabled</strong>, or&nbsp;<strong id="b842352706165447"><a name="b842352706165447"></a><a name="b842352706165447"></a>restart-by-peer</strong>. The default value is&nbsp;<strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>hold</strong>.</p>
</td>
</tr>
<tr id="row41760071"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p27122565"><a name="p27122565"></a><a name="p27122565"></a>vpnservice_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p49444123"><a name="p49444123"></a><a name="p49444123"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p65754481"><a name="p65754481"></a><a name="p65754481"></a>Specifies the VPN service ID.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section18138873"></a>

-   Example Request

    ```
    GET /v2.0/vpn/ipsec-site-connections/{connection_id}
    ```


-   Example Response

    ```
    {
      "ipsec_site_connection" : {
        "status" : "DOWN",
        "psk" : "secret",
        "initiator" : "bi-directional",
        "name" : "vpnconnection1",
        "admin_state_up" : true,
        "project_id" : "10039663455a446d8ba2cbb058b0f578",
        "tenant_id" : "10039663455a446d8ba2cbb058b0f578",
        "auth_mode" : "psk",
        "peer_cidrs" : [ ],
        "mtu" : 1500,
        "peer_ep_group_id" : "9ad5a7e0-6dac-41b4-b20d-a7b8645fddf1",
        "ikepolicy_id" : "9b00d6b0-6c93-4ca5-9747-b8ade7bb514f",
        "vpnservice_id" : "5c561d9d-eaea-45f6-ae3e-08d1a7080828",
        "dpd" : {
          "action" : "hold",
          "interval" : 30,
          "timeout" : 120
        },
        "route_mode" : "static",
        "ipsecpolicy_id" : "e6e23d0c-9519-4d52-8ea4-5b1f96d857b1",
        "local_ep_group_id" : "3e1815dd-e212-43d0-8f13-b494fa553e68",
        "peer_address" : "172.24.4.226",
        "peer_id" : "172.24.4.226",
        "id" : "851f280f-5639-4ea3-81aa-e298525ab74b",
        "description" : ""
      }
    }
    ```


## Returned Values<a name="section26431778"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

