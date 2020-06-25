# Querying Subscriptions of a Specified Topic<a name="smn_api_52002"></a>

## Description<a name="en-us_topic_0025373770"></a>

-   API name

    ListSubscriptionsByTopic


-   Function

    Query the list of subscriptions of a specified topic by page. The list is sorted by the subscription adding time in ascending order. If no subscription has been added to the topic, an empty list is returned.


## URI<a name="section37356392"></a>

-   URI format

    GET /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}/subscriptions?offset=\{offset\}&limit=\{limit\}


-   Parameter description

    <a name="table10143581"></a>
    <table><thead align="left"><tr id="row8289053"><th class="cellrowborder" valign="top" width="24.709999999999997%" id="mcps1.1.5.1.1"><p id="p324668"><a name="p324668"></a><a name="p324668"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.06%" id="mcps1.1.5.1.2"><p id="p26298136"><a name="p26298136"></a><a name="p26298136"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.61%" id="mcps1.1.5.1.3"><p id="p49774232"><a name="p49774232"></a><a name="p49774232"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.620000000000005%" id="mcps1.1.5.1.4"><p id="p5180964"><a name="p5180964"></a><a name="p5180964"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35224963"><td class="cellrowborder" valign="top" width="24.709999999999997%" headers="mcps1.1.5.1.1 "><p id="p34649765"><a name="p34649765"></a><a name="p34649765"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.1.5.1.2 "><p id="p55167604"><a name="p55167604"></a><a name="p55167604"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.1.5.1.3 "><p id="p39390935"><a name="p39390935"></a><a name="p39390935"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.620000000000005%" headers="mcps1.1.5.1.4 "><p id="p7542769155117"><a name="p7542769155117"></a><a name="p7542769155117"></a>Project ID</p>
    <p id="p36549175"><a name="p36549175"></a><a name="p36549175"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row2129750"><td class="cellrowborder" valign="top" width="24.709999999999997%" headers="mcps1.1.5.1.1 "><p id="p38292076"><a name="p38292076"></a><a name="p38292076"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.1.5.1.2 "><p id="p14650458"><a name="p14650458"></a><a name="p14650458"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.1.5.1.3 "><p id="p45836489"><a name="p45836489"></a><a name="p45836489"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.620000000000005%" headers="mcps1.1.5.1.4 "><p id="p21768161"><a name="p21768161"></a><a name="p21768161"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    <tr id="row31297682"><td class="cellrowborder" valign="top" width="24.709999999999997%" headers="mcps1.1.5.1.1 "><p id="p52084342"><a name="p52084342"></a><a name="p52084342"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.1.5.1.2 "><p id="p37545213172528"><a name="p37545213172528"></a><a name="p37545213172528"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.1.5.1.3 "><p id="p7035667"><a name="p7035667"></a><a name="p7035667"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.620000000000005%" headers="mcps1.1.5.1.4 "><p id="p146581828102110"><a name="p146581828102110"></a><a name="p146581828102110"></a>Offset</p>
    <p id="p21821344207"><a name="p21821344207"></a><a name="p21821344207"></a>If the value is an integer greater than 0 but less than the number of resources, all resources after this offset will be queried. The default value is <strong id="b11811133314711"><a name="b11811133314711"></a><a name="b11811133314711"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row45251091"><td class="cellrowborder" valign="top" width="24.709999999999997%" headers="mcps1.1.5.1.1 "><p id="p41459726"><a name="p41459726"></a><a name="p41459726"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.1.5.1.2 "><p id="p6679585172531"><a name="p6679585172531"></a><a name="p6679585172531"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.1.5.1.3 "><p id="p25040094"><a name="p25040094"></a><a name="p25040094"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.620000000000005%" headers="mcps1.1.5.1.4 "><a name="ul38160342182720"></a><a name="ul38160342182720"></a><ul id="ul38160342182720"><li>Number of resources returned on each page</li><li>Value range: 1–100<p id="p3980022182720"><a name="p3980022182720"></a><a name="p3980022182720"></a>Commonly used values are <strong id="b1988313383187"><a name="b1988313383187"></a><a name="b1988313383187"></a>10</strong>, <strong id="b13884138181811"><a name="b13884138181811"></a><a name="b13884138181811"></a>20</strong>, and <strong id="b28859388189"><a name="b28859388189"></a><a name="b28859388189"></a>50</strong>.</p>
    <p id="p1134873382116"><a name="p1134873382116"></a><a name="p1134873382116"></a>The default value is <strong id="b82991142181817"><a name="b82991142181817"></a><a name="b82991142181817"></a>100</strong>.</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section663215"></a>

Example request

```
GET https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_topic_v1/subscriptions?offset=0&limit=100 
```

## Response<a name="section5968939"></a>

-   Parameter description

    <a name="table30212363"></a>
    <table><thead align="left"><tr id="row20364417"><th class="cellrowborder" valign="top" width="27.53724627537246%" id="mcps1.1.4.1.1"><p id="p38905106"><a name="p38905106"></a><a name="p38905106"></a><strong id="b842352706191030_1"><a name="b842352706191030_1"></a><a name="b842352706191030_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.50614938506149%" id="mcps1.1.4.1.2"><p id="p64305920"><a name="p64305920"></a><a name="p64305920"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.95660433956604%" id="mcps1.1.4.1.3"><p id="p41397042"><a name="p41397042"></a><a name="p41397042"></a><strong id="b84235270619115_1"><a name="b84235270619115_1"></a><a name="b84235270619115_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16425092"><td class="cellrowborder" valign="top" width="27.53724627537246%" headers="mcps1.1.4.1.1 "><p id="p55364084"><a name="p55364084"></a><a name="p55364084"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.50614938506149%" headers="mcps1.1.4.1.2 "><p id="p55305800"><a name="p55305800"></a><a name="p55305800"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.95660433956604%" headers="mcps1.1.4.1.3 "><p id="p50584809"><a name="p50584809"></a><a name="p50584809"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row33559471"><td class="cellrowborder" valign="top" width="27.53724627537246%" headers="mcps1.1.4.1.1 "><p id="p33962670"><a name="p33962670"></a><a name="p33962670"></a>subscription_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.50614938506149%" headers="mcps1.1.4.1.2 "><p id="p66621782"><a name="p66621782"></a><a name="p66621782"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.95660433956604%" headers="mcps1.1.4.1.3 "><p id="p27655246"><a name="p27655246"></a><a name="p27655246"></a>Number of subscriptions</p>
    </td>
    </tr>
    <tr id="row28015283"><td class="cellrowborder" valign="top" width="27.53724627537246%" headers="mcps1.1.4.1.1 "><p id="p54645451"><a name="p54645451"></a><a name="p54645451"></a>subscriptions</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.50614938506149%" headers="mcps1.1.4.1.2 "><p id="p64205424"><a name="p64205424"></a><a name="p64205424"></a>Subscription structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.95660433956604%" headers="mcps1.1.4.1.3 "><p id="p33256841"><a name="p33256841"></a><a name="p33256841"></a>For details, see <a href="#table62621618105717">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Subscription structure

    <a name="table62621618105717"></a>
    <table><thead align="left"><tr id="smn_api_52001_row57429145195712"><th class="cellrowborder" valign="top" width="28.6971302869713%" id="mcps1.2.4.1.1"><p id="smn_api_52001_p21249193195712"><a name="smn_api_52001_p21249193195712"></a><a name="smn_api_52001_p21249193195712"></a><strong id="smn_api_52001_b18916324810"><a name="smn_api_52001_b18916324810"></a><a name="smn_api_52001_b18916324810"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.786821317868213%" id="mcps1.2.4.1.2"><p id="smn_api_52001_p43463090195712"><a name="smn_api_52001_p43463090195712"></a><a name="smn_api_52001_p43463090195712"></a><strong id="smn_api_52001_b84235270619112"><a name="smn_api_52001_b84235270619112"></a><a name="smn_api_52001_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.51604839516049%" id="mcps1.2.4.1.3"><p id="smn_api_52001_p30849371195712"><a name="smn_api_52001_p30849371195712"></a><a name="smn_api_52001_p30849371195712"></a><strong id="smn_api_52001_b11761269480"><a name="smn_api_52001_b11761269480"></a><a name="smn_api_52001_b11761269480"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="smn_api_52001_row2389422195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="smn_api_52001_p59325480195712"><a name="smn_api_52001_p59325480195712"></a><a name="smn_api_52001_p59325480195712"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="smn_api_52001_p40634595195712"><a name="smn_api_52001_p40634595195712"></a><a name="smn_api_52001_p40634595195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="smn_api_52001_p3067911195712"><a name="smn_api_52001_p3067911195712"></a><a name="smn_api_52001_p3067911195712"></a>Resource identifier of a topic, which is unique</p>
    </td>
    </tr>
    <tr id="smn_api_52001_row21914642195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="smn_api_52001_p30255586195712"><a name="smn_api_52001_p30255586195712"></a><a name="smn_api_52001_p30255586195712"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="smn_api_52001_p34783382195712"><a name="smn_api_52001_p34783382195712"></a><a name="smn_api_52001_p34783382195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="smn_api_52001_p65990551195712"><a name="smn_api_52001_p65990551195712"></a><a name="smn_api_52001_p65990551195712"></a>Subscription protocol (Different protocols indicate different types of endpoints to receive messages.)</p>
    <p id="smn_api_52001_p15571735514"><a name="smn_api_52001_p15571735514"></a><a name="smn_api_52001_p15571735514"></a>Currently, the following protocols are supported:</p>
    <a name="smn_api_52001_ul1715273514576"></a><a name="smn_api_52001_ul1715273514576"></a><ul id="smn_api_52001_ul1715273514576"><li><strong id="smn_api_52001_b65901133114410"><a name="smn_api_52001_b65901133114410"></a><a name="smn_api_52001_b65901133114410"></a>email</strong>: The endpoints are email address.</li><li><strong id="smn_api_52001_b99571741008"><a name="smn_api_52001_b99571741008"></a><a name="smn_api_52001_b99571741008"></a>sms</strong>: The endpoints are phone numbers.</li><li><strong id="smn_api_52001_b1099011287223"><a name="smn_api_52001_b1099011287223"></a><a name="smn_api_52001_b1099011287223"></a>http</strong> and <strong id="smn_api_52001_b577715331224"><a name="smn_api_52001_b577715331224"></a><a name="smn_api_52001_b577715331224"></a>https</strong>: The endpoints are URLs.</li></ul>
    </td>
    </tr>
    <tr id="smn_api_52001_row57165101195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="smn_api_52001_p66970508195712"><a name="smn_api_52001_p66970508195712"></a><a name="smn_api_52001_p66970508195712"></a>subscription_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="smn_api_52001_p55902100195712"><a name="smn_api_52001_p55902100195712"></a><a name="smn_api_52001_p55902100195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="smn_api_52001_p31776236195712"><a name="smn_api_52001_p31776236195712"></a><a name="smn_api_52001_p31776236195712"></a>Resource identifier of a subscription, which is unique</p>
    </td>
    </tr>
    <tr id="smn_api_52001_row12318113195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="smn_api_52001_p58243097195712"><a name="smn_api_52001_p58243097195712"></a><a name="smn_api_52001_p58243097195712"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="smn_api_52001_p20070430195712"><a name="smn_api_52001_p20070430195712"></a><a name="smn_api_52001_p20070430195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="smn_api_52001_p15092119195712"><a name="smn_api_52001_p15092119195712"></a><a name="smn_api_52001_p15092119195712"></a>Project ID of the topic creator</p>
    </td>
    </tr>
    <tr id="smn_api_52001_row63410262195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="smn_api_52001_p35957569195712"><a name="smn_api_52001_p35957569195712"></a><a name="smn_api_52001_p35957569195712"></a>endpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="smn_api_52001_p26881981195712"><a name="smn_api_52001_p26881981195712"></a><a name="smn_api_52001_p26881981195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="smn_api_52001_p29956849195712"><a name="smn_api_52001_p29956849195712"></a><a name="smn_api_52001_p29956849195712"></a>Message receiving endpoint</p>
    </td>
    </tr>
    <tr id="smn_api_52001_row28162748195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="smn_api_52001_p66590149195712"><a name="smn_api_52001_p66590149195712"></a><a name="smn_api_52001_p66590149195712"></a>remark</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="smn_api_52001_p25092994195712"><a name="smn_api_52001_p25092994195712"></a><a name="smn_api_52001_p25092994195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="smn_api_52001_p19266652195712"><a name="smn_api_52001_p19266652195712"></a><a name="smn_api_52001_p19266652195712"></a>Remarks</p>
    </td>
    </tr>
    <tr id="smn_api_52001_row19637006195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="smn_api_52001_p47093678195712"><a name="smn_api_52001_p47093678195712"></a><a name="smn_api_52001_p47093678195712"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="smn_api_52001_p56491591195712"><a name="smn_api_52001_p56491591195712"></a><a name="smn_api_52001_p56491591195712"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="smn_api_52001_p12416128195712"><a name="smn_api_52001_p12416128195712"></a><a name="smn_api_52001_p12416128195712"></a>Subscription status</p>
    <a name="smn_api_52001_ul1357151620117"></a><a name="smn_api_52001_ul1357151620117"></a><ul id="smn_api_52001_ul1357151620117"><li><strong id="smn_api_52001_b1964943612113"><a name="smn_api_52001_b1964943612113"></a><a name="smn_api_52001_b1964943612113"></a>0</strong>: unconfirmed</li><li><strong id="smn_api_52001_b1944317489116"><a name="smn_api_52001_b1944317489116"></a><a name="smn_api_52001_b1944317489116"></a>1</strong>: confirmed</li><li><strong id="smn_api_52001_b15634230216"><a name="smn_api_52001_b15634230216"></a><a name="smn_api_52001_b15634230216"></a>3</strong>: canceled</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "request_id": "4650b14bf221492fb819c231d167e6fe", 
        "subscription_count": 2, 
        "subscriptions": [
            {
                "topic_urn": "urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_topic_v1", 
                "protocol": "sms", 
                "subscription_urn": "urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_topic_v1:2e778e84408e44058e6cbc6d3c377837", 
                "owner": "762bdb3251034f268af0e395c53ea09b", 
                "endpoint": "xxxxxxxxxx", 
                "remark": "", 
                "status": 0
            }, 
            {
                "topic_urn": "urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_topic_v1", 
                "protocol": "email", 
                "subscription_urn": "urn:smn:regionId:762bdb3251034f268af0e395c53ea09b:test_topic_v1:a2d52a9f5c3b47f48c3fafb177a58796", 
                "owner": "762bdb3251034f268af0e395c53ea09b", 
                "endpoint": "xx@xx.com", 
                "remark": "", 
                "status": 0
            }
    ] 
    }
    ```


## Returned Value<a name="section53720453"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

