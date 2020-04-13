# Creating an SNAT Rule<a name="nat_api_0006"></a>

## Function<a name="section45647471"></a>

This API is used to create an SNAT rule.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can create an SNAT rule only when  **status**  of the NAT gateway is set to  **ACTIVE**  and  **admin\_state\_up**  of the NAT gateway administrator to  **True**.  

## URI<a name="section8174056"></a>

POST /v2.0/snat\_rules

## Request<a name="section58118839"></a>

[Table 1](#table10267194320114)  describes the request parameters.

**Table  1**  Request parameter

<a name="table10267194320114"></a>
<table><thead align="left"><tr id="row6376174317113"><th class="cellrowborder" valign="top" width="23.72%" id="mcps1.2.5.1.1"><p id="p83761431417"><a name="p83761431417"></a><a name="p83761431417"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.219999999999999%" id="mcps1.2.5.1.2"><p id="p19376144311113"><a name="p19376144311113"></a><a name="p19376144311113"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.56%" id="mcps1.2.5.1.3"><p id="p1237644310118"><a name="p1237644310118"></a><a name="p1237644310118"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.5%" id="mcps1.2.5.1.4"><p id="p19376243814"><a name="p19376243814"></a><a name="p19376243814"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row113769431511"><td class="cellrowborder" valign="top" width="23.72%" headers="mcps1.2.5.1.1 "><p id="p143761543316"><a name="p143761543316"></a><a name="p143761543316"></a>snat_rule</p>
</td>
<td class="cellrowborder" valign="top" width="8.219999999999999%" headers="mcps1.2.5.1.2 "><p id="p143761543914"><a name="p143761543914"></a><a name="p143761543914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p3376143212"><a name="p3376143212"></a><a name="p3376143212"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.5%" headers="mcps1.2.5.1.4 "><p id="p63766431210"><a name="p63766431210"></a><a name="p63766431210"></a>Specifies the SNAT rule object. For details, see <a href="#table628219431019">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Description of the  **snat\_rule**  field

<a name="table628219431019"></a>
<table><thead align="left"><tr id="row5376743718"><th class="cellrowborder" valign="top" width="22.57%" id="mcps1.2.5.1.1"><p id="p4376134314114"><a name="p4376134314114"></a><a name="p4376134314114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.649999999999999%" id="mcps1.2.5.1.2"><p id="p43767431317"><a name="p43767431317"></a><a name="p43767431317"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.9%" id="mcps1.2.5.1.3"><p id="p3376643415"><a name="p3376643415"></a><a name="p3376643415"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.879999999999995%" id="mcps1.2.5.1.4"><p id="p5376154315117"><a name="p5376154315117"></a><a name="p5376154315117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9376643318"><td class="cellrowborder" valign="top" width="22.57%" headers="mcps1.2.5.1.1 "><p id="p33764431917"><a name="p33764431917"></a><a name="p33764431917"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p143761343014"><a name="p143761343014"></a><a name="p143761343014"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.9%" headers="mcps1.2.5.1.3 "><p id="p143761143518"><a name="p143761143518"></a><a name="p143761143518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.879999999999995%" headers="mcps1.2.5.1.4 "><p id="p15376243712"><a name="p15376243712"></a><a name="p15376243712"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row73761743512"><td class="cellrowborder" valign="top" width="22.57%" headers="mcps1.2.5.1.1 "><p id="p18522143016410"><a name="p18522143016410"></a><a name="p18522143016410"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p115225301847"><a name="p115225301847"></a><a name="p115225301847"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.9%" headers="mcps1.2.5.1.3 "><p id="p9522830441"><a name="p9522830441"></a><a name="p9522830441"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.879999999999995%" headers="mcps1.2.5.1.4 "><p id="p115223302049"><a name="p115223302049"></a><a name="p115223302049"></a>Specifies the network ID used by the SNAT rule. This parameter and <strong id="b106891520164317"><a name="b106891520164317"></a><a name="b106891520164317"></a>cidr</strong> are alternative.</p>
</td>
</tr>
<tr id="row237617432112"><td class="cellrowborder" valign="top" width="22.57%" headers="mcps1.2.5.1.1 "><p id="p56167320519"><a name="p56167320519"></a><a name="p56167320519"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="8.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p11616163653"><a name="p11616163653"></a><a name="p11616163653"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.9%" headers="mcps1.2.5.1.3 "><p id="p7616132519"><a name="p7616132519"></a><a name="p7616132519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.879999999999995%" headers="mcps1.2.5.1.4 "><p id="p96161631513"><a name="p96161631513"></a><a name="p96161631513"></a>Specifies CIDR, which can be in the format of a network segment or a host IP address. This parameter and <strong id="b7582204212211"><a name="b7582204212211"></a><a name="b7582204212211"></a>network_id</strong> are alternative.</p>
<p id="p1861612320514"><a name="p1861612320514"></a><a name="p1861612320514"></a>If the value of <strong id="b26831022102418"><a name="b26831022102418"></a><a name="b26831022102418"></a>Source_type</strong> is <strong id="b1378414485243"><a name="b1378414485243"></a><a name="b1378414485243"></a>0</strong>, the CIDR block must be a subset of the VPC subnet CIDR block.</p>
<p id="p20616431753"><a name="p20616431753"></a><a name="p20616431753"></a>If the value of <strong id="b1623745462716"><a name="b1623745462716"></a><a name="b1623745462716"></a>Source_type</strong> is <strong id="b12237354122713"><a name="b12237354122713"></a><a name="b12237354122713"></a>1</strong>, <strong id="b1217945310323"><a name="b1217945310323"></a><a name="b1217945310323"></a>cidr</strong> must be a CIDR block of Direct Connect connection.</p>
</td>
</tr>
<tr id="row1637684317119"><td class="cellrowborder" valign="top" width="22.57%" headers="mcps1.2.5.1.1 "><p id="p1437611434114"><a name="p1437611434114"></a><a name="p1437611434114"></a>source_type</p>
</td>
<td class="cellrowborder" valign="top" width="8.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p1537617431518"><a name="p1537617431518"></a><a name="p1537617431518"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.9%" headers="mcps1.2.5.1.3 "><p id="p537624314120"><a name="p537624314120"></a><a name="p537624314120"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.879999999999995%" headers="mcps1.2.5.1.4 "><p id="p037614433118"><a name="p037614433118"></a><a name="p037614433118"></a><strong id="b667415014212"><a name="b667415014212"></a><a name="b667415014212"></a>0</strong>: Either <strong id="b116749506215"><a name="b116749506215"></a><a name="b116749506215"></a>network_id</strong> or <strong id="b1767575012212"><a name="b1767575012212"></a><a name="b1767575012212"></a>cidr</strong> can be specified in a VPC.</p>
<p id="p1937614436114"><a name="p1937614436114"></a><a name="p1937614436114"></a><strong id="b216113591626"><a name="b216113591626"></a><a name="b216113591626"></a>1</strong>: Only <strong id="b141612591429"><a name="b141612591429"></a><a name="b141612591429"></a>cidr</strong> can be specified over a Direct Connect connection.</p>
<p id="p1137616431711"><a name="p1137616431711"></a><a name="p1137616431711"></a>If no value is entered, the default value <strong id="b14717415339"><a name="b14717415339"></a><a name="b14717415339"></a>0</strong> (VPC) is used.</p>
</td>
</tr>
<tr id="row19376114318117"><td class="cellrowborder" valign="top" width="22.57%" headers="mcps1.2.5.1.1 "><p id="p63761431119"><a name="p63761431119"></a><a name="p63761431119"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p183763431012"><a name="p183763431012"></a><a name="p183763431012"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.9%" headers="mcps1.2.5.1.3 "><p id="p173763431417"><a name="p173763431417"></a><a name="p173763431417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.879999999999995%" headers="mcps1.2.5.1.4 "><p id="p03765431213"><a name="p03765431213"></a><a name="p03765431213"></a>Specifies the EIP ID. Multiple EIPs are separated using commas (,).</p>
<p id="p123761343915"><a name="p123761343915"></a><a name="p123761343915"></a>The maximum length of the ID is 4096 bytes.</p>
<p id="p103761343515"><a name="p103761343515"></a><a name="p103761343515"></a>The number of EIP IDs cannot exceed 20.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section53307511"></a>

[Table 3](#table64245911)  lists response parameters.

**Table  3**  Response parameters

<a name="table64245911"></a>
<table><thead align="left"><tr id="row15388566"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p38514356"><a name="p38514356"></a><a name="p38514356"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p32655106"><a name="p32655106"></a><a name="p32655106"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.4.1.3"><p id="p38657103"><a name="p38657103"></a><a name="p38657103"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row44217630"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p24858302"><a name="p24858302"></a><a name="p24858302"></a>snat_rule</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p256599"><a name="p256599"></a><a name="p256599"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.3 "><p id="p5825169"><a name="p5825169"></a><a name="p5825169"></a>Specifies the SNAT rule object. For details, see <a href="#table161525103">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Description of the  **snat\_rule**  field

<a name="table161525103"></a>
<table><thead align="left"><tr id="row1725172181011"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p1725119218105"><a name="p1725119218105"></a><a name="p1725119218105"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.2"><p id="p162517218107"><a name="p162517218107"></a><a name="p162517218107"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.4.1.3"><p id="p525182161010"><a name="p525182161010"></a><a name="p525182161010"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row112519221010"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p42513251017"><a name="p42513251017"></a><a name="p42513251017"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1225113212107"><a name="p1225113212107"></a><a name="p1225113212107"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p102511291019"><a name="p102511291019"></a><a name="p102511291019"></a>Specifies the SNAT rule ID.</p>
</td>
</tr>
<tr id="row125152161012"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p625113241017"><a name="p625113241017"></a><a name="p625113241017"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p152512024103"><a name="p152512024103"></a><a name="p152512024103"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p152510211012"><a name="p152510211012"></a><a name="p152510211012"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row13251172191013"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p172667221018"><a name="p172667221018"></a><a name="p172667221018"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p82666214109"><a name="p82666214109"></a><a name="p82666214109"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p1726611251011"><a name="p1726611251011"></a><a name="p1726611251011"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row226622101019"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p162661929108"><a name="p162661929108"></a><a name="p162661929108"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p02661226100"><a name="p02661226100"></a><a name="p02661226100"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p42669211108"><a name="p42669211108"></a><a name="p42669211108"></a>Specifies the network ID used by the SNAT rule.</p>
</td>
</tr>
<tr id="row1266724105"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1266132131018"><a name="p1266132131018"></a><a name="p1266132131018"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p5266122121017"><a name="p5266122121017"></a><a name="p5266122121017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p10266122191010"><a name="p10266122191010"></a><a name="p10266122191010"></a>Specifies a subset of the VPC subnet CIDR block or a CIDR block of Direct Connect connection.</p>
</td>
</tr>
<tr id="row16266192191014"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p182661326103"><a name="p182661326103"></a><a name="p182661326103"></a>source_type</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p62661213102"><a name="p62661213102"></a><a name="p62661213102"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p172664291014"><a name="p172664291014"></a><a name="p172664291014"></a><strong id="b676212732"><a name="b676212732"></a><a name="b676212732"></a>0</strong>: Either <strong id="b1783763818"><a name="b1783763818"></a><a name="b1783763818"></a>network_id</strong> or <strong id="b346895545"><a name="b346895545"></a><a name="b346895545"></a>cidr</strong> can be specified in a VPC.</p>
<p id="p192667291014"><a name="p192667291014"></a><a name="p192667291014"></a><strong id="b1191167696"><a name="b1191167696"></a><a name="b1191167696"></a>1</strong>: Only <strong id="b1040270195"><a name="b1040270195"></a><a name="b1040270195"></a>cidr</strong> can be specified over a Direct Connect connection.</p>
<p id="p1026615271011"><a name="p1026615271011"></a><a name="p1026615271011"></a>If no value is entered, the default value <strong id="b434407976"><a name="b434407976"></a><a name="b434407976"></a>0</strong> (VPC) is used.</p>
</td>
</tr>
<tr id="row1526617211109"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p82661421103"><a name="p82661421103"></a><a name="p82661421103"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p8266142121011"><a name="p8266142121011"></a><a name="p8266142121011"></a>String(4096)</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><a name="ul1926613271020"></a><a name="ul1926613271020"></a><ul id="ul1926613271020"><li>Specifies the EIP ID. Multiple EIPs are separated using commas (,).</li><li>The maximum length of the ID is 4096 bytes.</li></ul>
</td>
</tr>
<tr id="row1326617261012"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p5266123104"><a name="p5266123104"></a><a name="p5266123104"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p19266427107"><a name="p19266427107"></a><a name="p19266427107"></a>String(1024)</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><a name="ul026610212101"></a><a name="ul026610212101"></a><ul id="ul026610212101"><li>Specifies the EIP. Multiple EIPs are separated using commas (,).</li><li>The maximum length is 1024 bytes.</li></ul>
</td>
</tr>
<tr id="row20266627104"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1426682131019"><a name="p1426682131019"></a><a name="p1426682131019"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p7266202101010"><a name="p7266202101010"></a><a name="p7266202101010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><a name="ul132663212108"></a><a name="ul132663212108"></a><ul id="ul132663212108"><li>Specifies the status of the SNAT rule.</li><li>For details about all its values, see <a href="resource-status-description.md#table1390614366107">Table 1</a>.</li></ul>
</td>
</tr>
<tr id="row826616212109"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p226611211104"><a name="p226611211104"></a><a name="p226611211104"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p1764614265487"><a name="p1764614265487"></a><a name="p1764614265487"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><a name="ul71858556358"></a><a name="ul71858556358"></a><ul id="ul71858556358"><li>Specifies whether the SNAT rule is enabled or disabled.</li><li>The value can be:<a name="ul16205638124410"></a><a name="ul16205638124410"></a><ul id="ul16205638124410"><li><strong id="b76592042145713"><a name="b76592042145713"></a><a name="b76592042145713"></a>true</strong>: The SNAT rule is enabled.</li><li><strong id="b42002045125519"><a name="b42002045125519"></a><a name="b42002045125519"></a>false</strong>: The SNAT rule is disabled.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row626642101011"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p18266122141014"><a name="p18266122141014"></a><a name="p18266122141014"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p32669214104"><a name="p32669214104"></a><a name="p32669214104"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.4.1.3 "><p id="p776395025914"><a name="p776395025914"></a><a name="p776395025914"></a>Specifies when the SNAT rule is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section10005551"></a>

-   Example request
    1.  Configure parameter  **network\_id**  in a VPC.

        ```
        POST https://{Endpoint}/v2.0/snat_rules 
        {
            "snat_rule": {
                "nat_gateway_id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8",
                "network_id": "eaad9cd6-2372-4be1-9535-9bd37210ae7b",
                "source_type":0,
                "floating_ip_id": "bdc10a4c-d81a-41ec-adf7-de857f7c812a"
            }
        }
        ```

    1.  Configure parameter  **cider**  in a VPC.

        ```
        POST https://{Endpoint}/v2.0/snat_rules
        {      
           "snat_rule": {
                 "nat_gateway_id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8",
                 "cidr": "192.168.1.10/32",
                 "source_type":0,
                 "floating_ip_id": "bdc10a4c-d81a-41ec-adf7-de857f7c812a"
              }
          }
        ```

    1.  Configure parameter  **cider**  over a Direct Connect connection.

        ```
        POST https://{Endpoint}/v2.0/snat_rules 
         {
              "snat_rule": { 
                 "nat_gateway_id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8",
                 "cidr": "172.30.0.0/24",
                 "source_type":1,
                 "floating_ip_id": "bdc10a4c-d81a-41ec-adf7-de857f7c812a"
              }
          }
        ```



-   Example response
    1.  Response to the request for specifying the  **network\_id**  for a VPC

        ```
        { 
             "snat_rule": { 
                 "floating_ip_id": "bdc10a4c-d81a-41ec-adf7-de857f7c812a", 
                 "status": "PENDING_CREATE", 
                 "nat_gateway_id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8", 
                 "admin_state_up": true, 
                 "network_id": "eaad9cd6-2372-4be1-9535-9bd37210ae7b", 
                 "cidr": null, 
                 "source_type":0, 
                 "tenant_id": "27e25061336f4af590faeabeb7fcd9a3", 
                 "created_at": "2017-11-18 07:54:21.665430", 
                 "id": "5b95c675-69c2-4656-ba06-58ff72e1d338", 
                 "floating_ip_address": "5.21.11.226"
             } 
         }
        ```

    2.  Response to the request for specifying the CIDR block in a VPC

        ```
        { 
             "snat_rule": { 
                 "floating_ip_id": "bdc10a4c-d81a-41ec-adf7-de857f7c812a", 
                 "status": "PENDING_CREATE", 
                 "nat_gateway_id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8", 
                 "admin_state_up": true, 
                 "cidr": "192.168.1.10/32", 
                 "source_type":0, 
                 "tenant_id": "27e25061336f4af590faeabeb7fcd9a3", 
                 "created_at": "2017-11-18 07:54:21.665430", 
                 "id": "5b95c675-69c2-4656-ba06-58ff72e1d338", 
                 "floating_ip_address": "5.21.11.226"
             } 
         }
        ```

    3.  Response to the request for specifying the CIDR block in a VPC

        ```
        { 
             "snat_rule": { 
                 "floating_ip_id": "bdc10a4c-d81a-41ec-adf7-de857f7c812a", 
                 "status": "PENDING_CREATE", 
                 "nat_gateway_id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8", 
                 "admin_state_up": true, 
                 "cidr": "172.30.0.0/24", 
                 "source_type":1, 
                 "tenant_id": "27e25061336f4af590faeabeb7fcd9a3", 
                 "created_at": "2017-11-18 07:54:21.665430", 
                 "id": "5b95c675-69c2-4656-ba06-58ff72e1d338", 
                 "floating_ip_address": "5.21.11.226"
             } 
         }
        ```



## Status Code<a name="section5143287"></a>

See  [Status Codes](status-codes.md).

