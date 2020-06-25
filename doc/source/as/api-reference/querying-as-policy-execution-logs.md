# Querying AS Policy Execution Logs<a name="EN-US_TOPIC_0102994869"></a>

## Function<a name="section1299912553252"></a>

This interface is used to query the historical records of AS policy execution based on search criteria. The results are displayed by page.

-   Search criteria can be the log ID, AS resource type, AS resource ID, policy execution type, start time, end time, start line number, and number of records.
-   If no search criteria are specified, a maximum of 20 AS policy execution logs can be queried by default.

## URI<a name="section755023613117"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_policy\_execute\_log/\{scaling\_policy\_id\}

>![](/images/icon-note.gif) **NOTE:**   
>You can type the question mark \(?\) and ampersand \(&\) at the end of the URI to define multiple search criteria. AS policy execution logs can be searched by all optional parameters in the following table. For details, see the example request.  

**Table  1**  Parameter description

<a name="table7553153610318"></a>
<table><thead align="left"><tr id="row866418363312"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.5.1.1"><p id="p20664336153114"><a name="p20664336153114"></a><a name="p20664336153114"></a><strong id="b182893275010"><a name="b182893275010"></a><a name="b182893275010"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p8664153633113"><a name="p8664153633113"></a><a name="p8664153633113"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p9664103623115"><a name="p9664103623115"></a><a name="p9664103623115"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.2.5.1.4"><p id="p116641436133115"><a name="p116641436133115"></a><a name="p116641436133115"></a><strong id="b143561318012"><a name="b143561318012"></a><a name="b143561318012"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row266493643114"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p1366413611319"><a name="p1366413611319"></a><a name="p1366413611319"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p196641736163116"><a name="p196641736163116"></a><a name="p196641736163116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p13664173616316"><a name="p13664173616316"></a><a name="p13664173616316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row166645368310"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p16641636163114"><a name="p16641636163114"></a><a name="p16641636163114"></a>scaling_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p7664203618312"><a name="p7664203618312"></a><a name="p7664203618312"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p5664173615319"><a name="p5664173615319"></a><a name="p5664173615319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p15664183616316"><a name="p15664183616316"></a><a name="p15664183616316"></a>Specifies the AS policy ID.</p>
</td>
</tr>
<tr id="row1666410363316"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p12665036163112"><a name="p12665036163112"></a><a name="p12665036163112"></a>log_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p866519364319"><a name="p866519364319"></a><a name="p866519364319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p12665103613316"><a name="p12665103613316"></a><a name="p12665103613316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p350525033414"><a name="p350525033414"></a><a name="p350525033414"></a>Specifies the ID of an AS policy execution log.</p>
</td>
</tr>
<tr id="row5665183610317"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p1666593693112"><a name="p1666593693112"></a><a name="p1666593693112"></a>scaling_resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p1366503617312"><a name="p1366503617312"></a><a name="p1366503617312"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1665103653115"><a name="p1665103653115"></a><a name="p1665103653115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p266553610317"><a name="p266553610317"></a><a name="p266553610317"></a>Specifies the scaling resource type.</p>
<a name="ul466523683115"></a><a name="ul466523683115"></a><ul id="ul466523683115"><li>AS group: <strong id="b84235270691950"><a name="b84235270691950"></a><a name="b84235270691950"></a>SCALING_GROUP</strong></li><li>Bandwidth: <strong id="b8423527069204"><a name="b8423527069204"></a><a name="b8423527069204"></a>BANDWIDTH</strong></li></ul>
</td>
</tr>
<tr id="row666512363314"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p1366520366311"><a name="p1366520366311"></a><a name="p1366520366311"></a>scaling_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p2066583633114"><a name="p2066583633114"></a><a name="p2066583633114"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1366543633116"><a name="p1366543633116"></a><a name="p1366543633116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p3665336143114"><a name="p3665336143114"></a><a name="p3665336143114"></a>Specifies the scaling resource ID.</p>
</td>
</tr>
<tr id="row46654368314"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p1066517362316"><a name="p1066517362316"></a><a name="p1066517362316"></a>execute_type</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p266513612316"><a name="p266513612316"></a><a name="p266513612316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p12665113620315"><a name="p12665113620315"></a><a name="p12665113620315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p266583643115"><a name="p266583643115"></a><a name="p266583643115"></a>Specifies the AS policy execution type.</p>
<a name="ul7315151314"></a><a name="ul7315151314"></a><ul id="ul7315151314"><li><strong id="b842352706101310"><a name="b842352706101310"></a><a name="b842352706101310"></a>SCHEDULED</strong>: automatically triggered at a specified time point</li><li><strong id="b84235270610179"><a name="b84235270610179"></a><a name="b84235270610179"></a>RECURRENCE</strong>: automatically triggered at a specified time period</li><li><strong id="b842352706101739"><a name="b842352706101739"></a><a name="b842352706101739"></a>ALARM</strong>: alarm-triggered</li><li><strong id="b842352706101755"><a name="b842352706101755"></a><a name="b842352706101755"></a>MANUAL</strong>: manually triggered</li></ul>
</td>
</tr>
<tr id="row10665836153111"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p1466515364318"><a name="p1466515364318"></a><a name="p1466515364318"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p14665193683119"><a name="p14665193683119"></a><a name="p14665193683119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1766513366311"><a name="p1766513366311"></a><a name="p1766513366311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p73497191114"><a name="p73497191114"></a><a name="p73497191114"></a>Specifies the start time that complies with UTC for querying AS policy execution logs. The format of the start time is <strong id="b14044178162939"><a name="b14044178162939"></a><a name="b14044178162939"></a>yyyy-MM-ddThh:mm:ssZ</strong>.</p>
</td>
</tr>
<tr id="row9665133610311"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p1366518369311"><a name="p1366518369311"></a><a name="p1366518369311"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p7665163616312"><a name="p7665163616312"></a><a name="p7665163616312"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1866516361317"><a name="p1866516361317"></a><a name="p1866516361317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p45451238816"><a name="p45451238816"></a><a name="p45451238816"></a>Specifies the end time that complies with UTC for querying AS policy execution logs. The format of the end time is <strong id="b14801105416014"><a name="b14801105416014"></a><a name="b14801105416014"></a>yyyy-MM-ddThh:mm:ssZ</strong>.</p>
</td>
</tr>
<tr id="row1066553620316"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p266516361310"><a name="p266516361310"></a><a name="p266516361310"></a>start_number</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p4665436143115"><a name="p4665436143115"></a><a name="p4665436143115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1665193653118"><a name="p1665193653118"></a><a name="p1665193653118"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p59373825"><a name="p59373825"></a><a name="p59373825"></a>Specifies the start line number. The default value is <strong id="b1714415211599"><a name="b1714415211599"></a><a name="b1714415211599"></a>0</strong>. The minimum parameter value is <strong id="b18744142621611"><a name="b18744142621611"></a><a name="b18744142621611"></a>0</strong>.</p>
</td>
</tr>
<tr id="row1665636103116"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.5.1.1 "><p id="p17666163673114"><a name="p17666163673114"></a><a name="p17666163673114"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p13666193613315"><a name="p13666193613315"></a><a name="p13666193613315"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p11666193614313"><a name="p11666193614313"></a><a name="p11666193614313"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p21968676"><a name="p21968676"></a><a name="p21968676"></a>Specifies the number of query records. The default value is <strong id="b168447885495335"><a name="b168447885495335"></a><a name="b168447885495335"></a>20</strong>. The value range is 0 to 100.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section1613001415326"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query the AS policy execution log with ID  **05545d3d-ccf9-4bca-ae4f-1e5e73ca0bf6**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/edcb94a885a84ed3a3fdf8ea4d2741da/scaling_policy_execute_log/05545d3d-ccf9-4bca-ae4f-1e5e73ca0bf6
    ```


## Response Message<a name="section05201533193214"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table1652713383212"></a>
    <table><thead align="left"><tr id="row971213315322"><th class="cellrowborder" valign="top" width="20.362036203620363%" id="mcps1.2.4.1.1"><p id="p07122339327"><a name="p07122339327"></a><a name="p07122339327"></a><strong id="b43871432006"><a name="b43871432006"></a><a name="b43871432006"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.851585158515851%" id="mcps1.2.4.1.2"><p id="p6712133183219"><a name="p6712133183219"></a><a name="p6712133183219"></a><strong id="b84235270693914"><a name="b84235270693914"></a><a name="b84235270693914"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="63.78637863786379%" id="mcps1.2.4.1.3"><p id="p1771223312328"><a name="p1771223312328"></a><a name="p1771223312328"></a><strong id="b886518333010"><a name="b886518333010"></a><a name="b886518333010"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1671233373212"><td class="cellrowborder" valign="top" width="20.362036203620363%" headers="mcps1.2.4.1.1 "><p id="p77121633193218"><a name="p77121633193218"></a><a name="p77121633193218"></a>total_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.851585158515851%" headers="mcps1.2.4.1.2 "><p id="p87121133193218"><a name="p87121133193218"></a><a name="p87121133193218"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.78637863786379%" headers="mcps1.2.4.1.3 "><p id="p1771233312321"><a name="p1771233312321"></a><a name="p1771233312321"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    <tr id="row77124334323"><td class="cellrowborder" valign="top" width="20.362036203620363%" headers="mcps1.2.4.1.1 "><p id="p14712433173212"><a name="p14712433173212"></a><a name="p14712433173212"></a>start_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.851585158515851%" headers="mcps1.2.4.1.2 "><p id="p0712113310329"><a name="p0712113310329"></a><a name="p0712113310329"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.78637863786379%" headers="mcps1.2.4.1.3 "><p id="p3712183383213"><a name="p3712183383213"></a><a name="p3712183383213"></a>Specifies the start line number.</p>
    </td>
    </tr>
    <tr id="row1671212337326"><td class="cellrowborder" valign="top" width="20.362036203620363%" headers="mcps1.2.4.1.1 "><p id="p1071253373216"><a name="p1071253373216"></a><a name="p1071253373216"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.851585158515851%" headers="mcps1.2.4.1.2 "><p id="p571213383210"><a name="p571213383210"></a><a name="p571213383210"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.78637863786379%" headers="mcps1.2.4.1.3 "><p id="p12712733143216"><a name="p12712733143216"></a><a name="p12712733143216"></a>Specifies the maximum number of resources to be queried.</p>
    </td>
    </tr>
    <tr id="row127121933183220"><td class="cellrowborder" valign="top" width="20.362036203620363%" headers="mcps1.2.4.1.1 "><p id="p7712143333219"><a name="p7712143333219"></a><a name="p7712143333219"></a>scaling_policy_execute_log</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.851585158515851%" headers="mcps1.2.4.1.2 "><p id="p199611453164414"><a name="p199611453164414"></a><a name="p199611453164414"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.78637863786379%" headers="mcps1.2.4.1.3 "><p id="p67123332326"><a name="p67123332326"></a><a name="p67123332326"></a>Specifies the AS policy execution logs. For details, see <a href="#table253953315328">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_policy\_execute\_log**  field description

    <a name="table253953315328"></a>
    <table><thead align="left"><tr id="row4713123316326"><th class="cellrowborder" valign="top" width="20.197980201979803%" id="mcps1.2.4.1.1"><p id="p16713103343210"><a name="p16713103343210"></a><a name="p16713103343210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.13838616138386%" id="mcps1.2.4.1.2"><p id="p167131933173217"><a name="p167131933173217"></a><a name="p167131933173217"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.66363363663634%" id="mcps1.2.4.1.3"><p id="p871373383215"><a name="p871373383215"></a><a name="p871373383215"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1671311338321"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p171317336327"><a name="p171317336327"></a><a name="p171317336327"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p1771318337329"><a name="p1771318337329"></a><a name="p1771318337329"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p4713163343210"><a name="p4713163343210"></a><a name="p4713163343210"></a>Specifies the AS policy execution status.</p>
    <a name="ul1882220491106"></a><a name="ul1882220491106"></a><ul id="ul1882220491106"><li><strong id="b1144461815207"><a name="b1144461815207"></a><a name="b1144461815207"></a>SUCCESS</strong>: The AS policy has been executed.</li><li><strong id="b1917291182018"><a name="b1917291182018"></a><a name="b1917291182018"></a>FAIL</strong>: Executing the AS policy failed.</li><li><strong id="b842352706171746"><a name="b842352706171746"></a><a name="b842352706171746"></a>EXECUTING</strong>: The AS policy is being executed.</li></ul>
    </td>
    </tr>
    <tr id="row107131033173216"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p371383383216"><a name="p371383383216"></a><a name="p371383383216"></a>failed_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p47131533153215"><a name="p47131533153215"></a><a name="p47131533153215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p071373373210"><a name="p071373373210"></a><a name="p071373373210"></a>Specifies the AS policy execution failure.</p>
    </td>
    </tr>
    <tr id="row4713133143214"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p137135339328"><a name="p137135339328"></a><a name="p137135339328"></a>execute_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p3713113333216"><a name="p3713113333216"></a><a name="p3713113333216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p671323313215"><a name="p671323313215"></a><a name="p671323313215"></a>Specifies the AS policy execution type.</p>
    <a name="ul164154538016"></a><a name="ul164154538016"></a><ul id="ul164154538016"><li><strong id="b413791495"><a name="b413791495"></a><a name="b413791495"></a>SCHEDULED</strong>: automatically triggered at a specified time point</li><li><strong id="b1868842213"><a name="b1868842213"></a><a name="b1868842213"></a>RECURRENCE</strong>: automatically triggered at a specified time period</li><li><strong id="b656572101"><a name="b656572101"></a><a name="b656572101"></a>ALARM</strong>: alarm-triggered</li><li><strong id="b1363359787"><a name="b1363359787"></a><a name="b1363359787"></a>MANUAL</strong>: manually triggered</li></ul>
    </td>
    </tr>
    <tr id="row471373310326"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p20713183373210"><a name="p20713183373210"></a><a name="p20713183373210"></a>execute_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p14713163313216"><a name="p14713163313216"></a><a name="p14713163313216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p1971383353218"><a name="p1971383353218"></a><a name="p1971383353218"></a>Specifies the time when an AS policy was executed. The time format complies with UTC.</p>
    </td>
    </tr>
    <tr id="row20713153313329"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p11713933113214"><a name="p11713933113214"></a><a name="p11713933113214"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p5713133317327"><a name="p5713133317327"></a><a name="p5713133317327"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p371323353212"><a name="p371323353212"></a><a name="p371323353212"></a>Specifies the ID of an AS policy execution log.</p>
    </td>
    </tr>
    <tr id="row6713103373214"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p8391182132116"><a name="p8391182132116"></a><a name="p8391182132116"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p671315331327"><a name="p671315331327"></a><a name="p671315331327"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p9115104123715"><a name="p9115104123715"></a><a name="p9115104123715"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row11714183333213"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p1771433393216"><a name="p1771433393216"></a><a name="p1771433393216"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p137148339329"><a name="p137148339329"></a><a name="p137148339329"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p1471413373217"><a name="p1471413373217"></a><a name="p1471413373217"></a>Specifies the AS policy ID.</p>
    </td>
    </tr>
    <tr id="row9714183383213"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p6714103310329"><a name="p6714103310329"></a><a name="p6714103310329"></a>scaling_resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p27141433173219"><a name="p27141433173219"></a><a name="p27141433173219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p11714143310326"><a name="p11714143310326"></a><a name="p11714143310326"></a>Specifies the scaling resource type.</p>
    <a name="ul197143338327"></a><a name="ul197143338327"></a><ul id="ul197143338327"><li>AS group: <strong id="b1098778374"><a name="b1098778374"></a><a name="b1098778374"></a>SCALING_GROUP</strong></li><li>Bandwidth: <strong id="b1723268034"><a name="b1723268034"></a><a name="b1723268034"></a>BANDWIDTH</strong></li></ul>
    </td>
    </tr>
    <tr id="row17714183315324"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p371473319323"><a name="p371473319323"></a><a name="p371473319323"></a>scaling_resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p13714733143216"><a name="p13714733143216"></a><a name="p13714733143216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p10715133343219"><a name="p10715133343219"></a><a name="p10715133343219"></a>Specifies the scaling resource ID.</p>
    </td>
    </tr>
    <tr id="row4715203353214"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p571563383214"><a name="p571563383214"></a><a name="p571563383214"></a>old_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p071573317320"><a name="p071573317320"></a><a name="p071573317320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p197151336327"><a name="p197151336327"></a><a name="p197151336327"></a>Specifies the source value.</p>
    </td>
    </tr>
    <tr id="row1771533343217"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p1271563343219"><a name="p1271563343219"></a><a name="p1271563343219"></a>desire_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p1371573313217"><a name="p1371573313217"></a><a name="p1371573313217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p1671513331323"><a name="p1671513331323"></a><a name="p1671513331323"></a>Specifies the target value.</p>
    </td>
    </tr>
    <tr id="row1450019713399"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p12501107113910"><a name="p12501107113910"></a><a name="p12501107113910"></a>limit_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p385004711497"><a name="p385004711497"></a><a name="p385004711497"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p11850647164919"><a name="p11850647164919"></a><a name="p11850647164919"></a>Specifies the operation restrictions.</p>
    <p id="p53866212428"><a name="p53866212428"></a><a name="p53866212428"></a>If <strong id="b15609115411378"><a name="b15609115411378"></a><a name="b15609115411378"></a>scaling_resource_type</strong> is set to <strong id="b16101154153712"><a name="b16101154153712"></a><a name="b16101154153712"></a>BANDWIDTH</strong> and <strong id="b2610105493710"><a name="b2610105493710"></a><a name="b2610105493710"></a>operation</strong> is not <strong id="b561145493714"><a name="b561145493714"></a><a name="b561145493714"></a>SET</strong>, this parameter takes effect and the unit is Mbit/s.</p>
    <p id="p38504475497"><a name="p38504475497"></a><a name="p38504475497"></a>In this case:</p>
    <a name="ul1659020543422"></a><a name="ul1659020543422"></a><ul id="ul1659020543422"><li>If <strong id="b84235270694030"><a name="b84235270694030"></a><a name="b84235270694030"></a>operation</strong> is set to <strong id="b84235270694036"><a name="b84235270694036"></a><a name="b84235270694036"></a>ADD</strong>, this parameter indicates the maximum bandwidth allowed.</li><li>If <strong id="b894390753"><a name="b894390753"></a><a name="b894390753"></a>operation</strong> is set to <strong id="b1847141865"><a name="b1847141865"></a><a name="b1847141865"></a>REDUCE</strong>, this parameter indicates the minimum bandwidth allowed.</li></ul>
    </td>
    </tr>
    <tr id="row12715143363213"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p97151033113212"><a name="p97151033113212"></a><a name="p97151033113212"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p57151833143219"><a name="p57151833143219"></a><a name="p57151833143219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p1871512337329"><a name="p1871512337329"></a><a name="p1871512337329"></a>Specifies the AS policy execution type.</p>
    <a name="ul198202035000"></a><a name="ul198202035000"></a><ul id="ul198202035000"><li><strong id="b1629814121180"><a name="b1629814121180"></a><a name="b1629814121180"></a>ADD</strong>: indicates adding instances.</li><li><strong id="b84235270692351"><a name="b84235270692351"></a><a name="b84235270692351"></a>REMOVE</strong>: indicates reducing instances.</li><li><strong id="b84235270692418"><a name="b84235270692418"></a><a name="b84235270692418"></a>SET</strong>: indicates setting the number of instances to a specified value.</li></ul>
    </td>
    </tr>
    <tr id="row10715163318322"><td class="cellrowborder" valign="top" width="20.197980201979803%" headers="mcps1.2.4.1.1 "><p id="p471523393216"><a name="p471523393216"></a><a name="p471523393216"></a>job_records</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.13838616138386%" headers="mcps1.2.4.1.2 "><p id="p14715123343218"><a name="p14715123343218"></a><a name="p14715123343218"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.66363363663634%" headers="mcps1.2.4.1.3 "><p id="p57159333323"><a name="p57159333323"></a><a name="p57159333323"></a>Specifies the tasks contained in a scaling action based on an AS policy. For details, see <a href="#table10573113383219">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **job\_records**  field description

    <a name="table10573113383219"></a>
    <table><thead align="left"><tr id="row107161833143219"><th class="cellrowborder" valign="top" width="20.06%" id="mcps1.2.4.1.1"><p id="p117164335324"><a name="p117164335324"></a><a name="p117164335324"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.3%" id="mcps1.2.4.1.2"><p id="p87161433103215"><a name="p87161433103215"></a><a name="p87161433103215"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.63999999999999%" id="mcps1.2.4.1.3"><p id="p671613338324"><a name="p671613338324"></a><a name="p671613338324"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37164337321"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p7716143314329"><a name="p7716143314329"></a><a name="p7716143314329"></a>job_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p371610335328"><a name="p371610335328"></a><a name="p371610335328"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p3716173303214"><a name="p3716173303214"></a><a name="p3716173303214"></a>Specifies the task name.</p>
    </td>
    </tr>
    <tr id="row27169338321"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p11716123314328"><a name="p11716123314328"></a><a name="p11716123314328"></a>record_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p6716103333215"><a name="p6716103333215"></a><a name="p6716103333215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p271653323210"><a name="p271653323210"></a><a name="p271653323210"></a>Specifies the record type.</p>
    <a name="ul184948276018"></a><a name="ul184948276018"></a><ul id="ul184948276018"><li><strong id="b84235270610279"><a name="b84235270610279"></a><a name="b84235270610279"></a>API</strong>: API calling type</li><li><strong id="b842352706102725"><a name="b842352706102725"></a><a name="b842352706102725"></a>MEG</strong>: message type</li></ul>
    </td>
    </tr>
    <tr id="row15716133319323"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p171713339324"><a name="p171713339324"></a><a name="p171713339324"></a>record_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p1171743315328"><a name="p1171743315328"></a><a name="p1171743315328"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p1471713353210"><a name="p1471713353210"></a><a name="p1471713353210"></a>Specifies the record time.</p>
    </td>
    </tr>
    <tr id="row15717633203218"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p14717183323215"><a name="p14717183323215"></a><a name="p14717183323215"></a>request</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p187179337324"><a name="p187179337324"></a><a name="p187179337324"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p4717143310323"><a name="p4717143310323"></a><a name="p4717143310323"></a>Specifies the request body. This parameter is valid only if <strong id="b842352706102823"><a name="b842352706102823"></a><a name="b842352706102823"></a>record_type</strong> is set to <strong id="b842352706102826"><a name="b842352706102826"></a><a name="b842352706102826"></a>API</strong>.</p>
    </td>
    </tr>
    <tr id="row1271717339321"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p127172331324"><a name="p127172331324"></a><a name="p127172331324"></a>response</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p17717183314323"><a name="p17717183314323"></a><a name="p17717183314323"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p0717183393214"><a name="p0717183393214"></a><a name="p0717183393214"></a>Specifies the response body. This parameter is valid only if <strong id="b842352706102858"><a name="b842352706102858"></a><a name="b842352706102858"></a>record_type</strong> is set to <strong id="b84235270610293"><a name="b84235270610293"></a><a name="b84235270610293"></a>API</strong>.</p>
    </td>
    </tr>
    <tr id="row1271733317326"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p171753333220"><a name="p171753333220"></a><a name="p171753333220"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p151632143413"><a name="p151632143413"></a><a name="p151632143413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p57171833143217"><a name="p57171833143217"></a><a name="p57171833143217"></a>Specifies the returned code. This parameter is valid only if <strong id="b583265226"><a name="b583265226"></a><a name="b583265226"></a>record_type</strong> is set to <strong id="b1741887214"><a name="b1741887214"></a><a name="b1741887214"></a>API</strong>.</p>
    </td>
    </tr>
    <tr id="row3717203319323"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p127171330326"><a name="p127171330326"></a><a name="p127171330326"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p187171133113214"><a name="p187171133113214"></a><a name="p187171133113214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p57179331328"><a name="p57179331328"></a><a name="p57179331328"></a>Specifies the message. This parameter is valid only if <strong id="b1660858168"><a name="b1660858168"></a><a name="b1660858168"></a>record_type</strong> is set to <strong id="b30167069"><a name="b30167069"></a><a name="b30167069"></a>MEG</strong>.</p>
    </td>
    </tr>
    <tr id="row1471753353215"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p11717123317323"><a name="p11717123317323"></a><a name="p11717123317323"></a>job_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p671773373217"><a name="p671773373217"></a><a name="p671773373217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p371733383211"><a name="p371733383211"></a><a name="p371733383211"></a>Specifies the execution status of the task.</p>
    <a name="ul187911822909"></a><a name="ul187911822909"></a><ul id="ul187911822909"><li><strong>SUCCESS</strong>: The task is successfully executed.</li><li><strong>FAIL</strong>: The task failed to be executed.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **meta\_data**  field description

    <a name="table3261054618219"></a>
    <table><thead align="left"><tr id="row5267718118219"><th class="cellrowborder" valign="top" width="20.06%" id="mcps1.2.4.1.1"><p id="p3899327918219"><a name="p3899327918219"></a><a name="p3899327918219"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.11%" id="mcps1.2.4.1.2"><p id="p433905418219"><a name="p433905418219"></a><a name="p433905418219"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.83%" id="mcps1.2.4.1.3"><p id="p1591908918219"><a name="p1591908918219"></a><a name="p1591908918219"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1437784118219"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.4.1.1 "><p id="p2375445318219"><a name="p2375445318219"></a><a name="p2375445318219"></a>User-defined key-value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p4506253418219"><a name="p4506253418219"></a><a name="p4506253418219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.83%" headers="mcps1.2.4.1.3 "><p id="p2618660318219"><a name="p2618660318219"></a><a name="p2618660318219"></a>Specifies the key and value of the metadata.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "limit": 20,
      "scaling_policy_execute_log": [
        {
          "id": "b86e4175-30cb-4b1e-a332-83f9ee472c58",
          "status": "SUCCESS",
          "type": "REMOVE",
          "tenant_id": "0428982a1b8039f42f01c005edde7c0d",
          "scaling_resource_type": "SCALING_GROUP",
          "scaling_resource_id": "1f2d3e73-7ef6-40b3-a8fa-514b68eccaa7",
          "scaling_policy_id": "05545d3d-ccf9-4bca-ae4f-1e5e73ca0bf6",
          "old_value": "1",
          "desire_value": "0",
          "limit_value": "0",
          "execute_time": "2019-03-18T16:00:00Z",
          "execute_type": "RECURRENCE",
          "job_records": [
            {
              "message": "modify desire number of scaling group",
              "job_name": "ADJUST_VM_NUMBERS",
              "record_type": "MEG",
              "record_time": "2019-03-18T16:00:00Z",
              "job_status": "SUCCESS"
            }
          ]
        }
      ],
      "total_number": 1,
      "start_number": 0
    }
    ```


## Returned Values<a name="section13597651197"></a>

-   Normal

    200

-   Abnormal

    <a name="table842286995"></a>
    <table><thead align="left"><tr id="row144201061797"><th class="cellrowborder" valign="top" width="43.62%" id="mcps1.1.3.1.1"><p id="p124201269917"><a name="p124201269917"></a><a name="p124201269917"></a>Returned Values</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.379999999999995%" id="mcps1.1.3.1.2"><p id="p134201163918"><a name="p134201163918"></a><a name="p134201163918"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1442066992"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p0420263920"><a name="p0420263920"></a><a name="p0420263920"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p194200610910"><a name="p194200610910"></a><a name="p194200610910"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row6420261891"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p124209614911"><a name="p124209614911"></a><a name="p124209614911"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p1242056892"><a name="p1242056892"></a><a name="p1242056892"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1242015611915"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p74206613913"><a name="p74206613913"></a><a name="p74206613913"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p14420661799"><a name="p14420661799"></a><a name="p14420661799"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row542119612912"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p542056596"><a name="p542056596"></a><a name="p542056596"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p1542056699"><a name="p1542056699"></a><a name="p1542056699"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row842146897"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p44211761498"><a name="p44211761498"></a><a name="p44211761498"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p164211062911"><a name="p164211062911"></a><a name="p164211062911"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row0421156998"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p114211565914"><a name="p114211565914"></a><a name="p114211565914"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p5421161094"><a name="p5421161094"></a><a name="p5421161094"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row44211464914"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p7421161499"><a name="p7421161499"></a><a name="p7421161499"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p12421766914"><a name="p12421766914"></a><a name="p12421766914"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row12421166494"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p5421961793"><a name="p5421961793"></a><a name="p5421961793"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p19421668913"><a name="p19421668913"></a><a name="p19421668913"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row11421146194"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p1642186693"><a name="p1642186693"></a><a name="p1642186693"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p194211161492"><a name="p194211161492"></a><a name="p194211161492"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row242215619914"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p842214611918"><a name="p842214611918"></a><a name="p842214611918"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p7422166292"><a name="p7422166292"></a><a name="p7422166292"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row142214613918"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p74221261295"><a name="p74221261295"></a><a name="p74221261295"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p12422106198"><a name="p12422106198"></a><a name="p12422106198"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row1942217618910"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p44221861693"><a name="p44221861693"></a><a name="p44221861693"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p74221464917"><a name="p74221464917"></a><a name="p74221464917"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row1542216613916"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p19422261915"><a name="p19422261915"></a><a name="p19422261915"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p042218620915"><a name="p042218620915"></a><a name="p042218620915"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row164221561394"><td class="cellrowborder" valign="top" width="43.62%" headers="mcps1.1.3.1.1 "><p id="p1142286898"><a name="p1142286898"></a><a name="p1142286898"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.379999999999995%" headers="mcps1.1.3.1.2 "><p id="p84221661591"><a name="p84221661591"></a><a name="p84221661591"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

