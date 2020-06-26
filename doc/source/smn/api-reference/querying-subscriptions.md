# Querying Subscriptions<a name="smn_api_52001"></a>

## Description<a name="section61847473"></a>

-   API name

    ListSubscriptions


-   Function

    Query the list of all subscriptions by page. The list is sorted by the subscription adding time in ascending order. If no subscription has been added, an empty list is returned.


## URI<a name="section19756352"></a>

-   URI format

    GET /v2/\{project\_id\}/notifications/subscriptions?offset=\{offset\}&limit=\{limit\}

-   Parameter description

    <a name="table47542785"></a>
    <table><thead align="left"><tr id="row44806966"><th class="cellrowborder" valign="top" width="21.002100210021002%" id="mcps1.1.5.1.1"><p id="p5485596"><a name="p5485596"></a><a name="p5485596"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.022002200220022%" id="mcps1.1.5.1.2"><p id="p41680131"><a name="p41680131"></a><a name="p41680131"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.002100210021002%" id="mcps1.1.5.1.3"><p id="p20647442"><a name="p20647442"></a><a name="p20647442"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.973797379737974%" id="mcps1.1.5.1.4"><p id="p61830130"><a name="p61830130"></a><a name="p61830130"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61513540"><td class="cellrowborder" valign="top" width="21.002100210021002%" headers="mcps1.1.5.1.1 "><p id="p16540805"><a name="p16540805"></a><a name="p16540805"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.022002200220022%" headers="mcps1.1.5.1.2 "><p id="p64736823"><a name="p64736823"></a><a name="p64736823"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.002100210021002%" headers="mcps1.1.5.1.3 "><p id="p9191297"><a name="p9191297"></a><a name="p9191297"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.973797379737974%" headers="mcps1.1.5.1.4 "><p id="p5734644015513"><a name="p5734644015513"></a><a name="p5734644015513"></a>Project ID</p>
    <p id="p6297612"><a name="p6297612"></a><a name="p6297612"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row27556864"><td class="cellrowborder" valign="top" width="21.002100210021002%" headers="mcps1.1.5.1.1 "><p id="p17513507"><a name="p17513507"></a><a name="p17513507"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.022002200220022%" headers="mcps1.1.5.1.2 "><p id="p4777719172219"><a name="p4777719172219"></a><a name="p4777719172219"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.002100210021002%" headers="mcps1.1.5.1.3 "><p id="p15748167"><a name="p15748167"></a><a name="p15748167"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.973797379737974%" headers="mcps1.1.5.1.4 "><p id="p146581828102110"><a name="p146581828102110"></a><a name="p146581828102110"></a>Offset</p>
    <p id="p21821344207"><a name="p21821344207"></a><a name="p21821344207"></a>If the value is an integer greater than 0 but less than the number of resources, all resources after this offset will be queried. The default value is <strong id="b152461342124410"><a name="b152461342124410"></a><a name="b152461342124410"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row53117702"><td class="cellrowborder" valign="top" width="21.002100210021002%" headers="mcps1.1.5.1.1 "><p id="p7566645"><a name="p7566645"></a><a name="p7566645"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.022002200220022%" headers="mcps1.1.5.1.2 "><p id="p12416120172223"><a name="p12416120172223"></a><a name="p12416120172223"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.002100210021002%" headers="mcps1.1.5.1.3 "><p id="p51313205"><a name="p51313205"></a><a name="p51313205"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.973797379737974%" headers="mcps1.1.5.1.4 "><a name="ul38160342182720"></a><a name="ul38160342182720"></a><ul id="ul38160342182720"><li>Value range: 1–100<p id="p3980022182720"><a name="p3980022182720"></a><a name="p3980022182720"></a>Commonly used values are <strong id="b17124217134617"><a name="b17124217134617"></a><a name="b17124217134617"></a>10</strong>, <strong id="b169771314154610"><a name="b169771314154610"></a><a name="b169771314154610"></a>20</strong>, and <strong id="b78111511194612"><a name="b78111511194612"></a><a name="b78111511194612"></a>50</strong>.</p>
    </li><li>Number of resources returned on each page</li></ul>
    <p id="p5184153012911"><a name="p5184153012911"></a><a name="p5184153012911"></a>The default value is <strong id="b109171820114612"><a name="b109171820114612"></a><a name="b109171820114612"></a>100</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section43589445"></a>

Example request

```
GET https://{SMN_Endpoint}/v2/{project_id}/notifications/subscriptions?offset=0&limit=2
```

## Response<a name="section56760689"></a>

-   Parameter description

    <a name="table8539194"></a>
    <table><thead align="left"><tr id="row46855021"><th class="cellrowborder" valign="top" width="29.95299529952995%" id="mcps1.1.4.1.1"><p id="p37160390"><a name="p37160390"></a><a name="p37160390"></a><strong id="b842352706191030_1"><a name="b842352706191030_1"></a><a name="b842352706191030_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.95299529952995%" id="mcps1.1.4.1.2"><p id="p57201619"><a name="p57201619"></a><a name="p57201619"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.09400940094009%" id="mcps1.1.4.1.3"><p id="p2819581"><a name="p2819581"></a><a name="p2819581"></a><strong id="b84235270619115_1"><a name="b84235270619115_1"></a><a name="b84235270619115_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44335814"><td class="cellrowborder" valign="top" width="29.95299529952995%" headers="mcps1.1.4.1.1 "><p id="p34431157"><a name="p34431157"></a><a name="p34431157"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.95299529952995%" headers="mcps1.1.4.1.2 "><p id="p37460321"><a name="p37460321"></a><a name="p37460321"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.09400940094009%" headers="mcps1.1.4.1.3 "><p id="p14387121"><a name="p14387121"></a><a name="p14387121"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row19228540"><td class="cellrowborder" valign="top" width="29.95299529952995%" headers="mcps1.1.4.1.1 "><p id="p14007894"><a name="p14007894"></a><a name="p14007894"></a>subscription_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.95299529952995%" headers="mcps1.1.4.1.2 "><p id="p60897649"><a name="p60897649"></a><a name="p60897649"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.09400940094009%" headers="mcps1.1.4.1.3 "><p id="p33762549"><a name="p33762549"></a><a name="p33762549"></a>Number of subscriptions</p>
    </td>
    </tr>
    <tr id="row51054032"><td class="cellrowborder" valign="top" width="29.95299529952995%" headers="mcps1.1.4.1.1 "><p id="p41735936"><a name="p41735936"></a><a name="p41735936"></a>subscriptions</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.95299529952995%" headers="mcps1.1.4.1.2 "><p id="p898341316566"><a name="p898341316566"></a><a name="p898341316566"></a>Subscription structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.09400940094009%" headers="mcps1.1.4.1.3 "><p id="p25312629"><a name="p25312629"></a><a name="p25312629"></a>See <a href="#table43425256195712">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Subscription structure

    <a name="table43425256195712"></a>
    <table><thead align="left"><tr id="row57429145195712"><th class="cellrowborder" valign="top" width="28.6971302869713%" id="mcps1.2.4.1.1"><p id="p21249193195712"><a name="p21249193195712"></a><a name="p21249193195712"></a><strong id="b18916324810"><a name="b18916324810"></a><a name="b18916324810"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.786821317868213%" id="mcps1.2.4.1.2"><p id="p43463090195712"><a name="p43463090195712"></a><a name="p43463090195712"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.51604839516049%" id="mcps1.2.4.1.3"><p id="p30849371195712"><a name="p30849371195712"></a><a name="p30849371195712"></a><strong id="b11761269480"><a name="b11761269480"></a><a name="b11761269480"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2389422195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="p59325480195712"><a name="p59325480195712"></a><a name="p59325480195712"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="p40634595195712"><a name="p40634595195712"></a><a name="p40634595195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="p3067911195712"><a name="p3067911195712"></a><a name="p3067911195712"></a>Resource identifier of a topic, which is unique</p>
    </td>
    </tr>
    <tr id="row21914642195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="p30255586195712"><a name="p30255586195712"></a><a name="p30255586195712"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="p34783382195712"><a name="p34783382195712"></a><a name="p34783382195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="p65990551195712"><a name="p65990551195712"></a><a name="p65990551195712"></a>Subscription protocol (Different protocols indicate different types of endpoints to receive messages.)</p>
    <p id="p15571735514"><a name="p15571735514"></a><a name="p15571735514"></a>Currently, the following protocols are supported:</p>
    <a name="ul1715273514576"></a><a name="ul1715273514576"></a><ul id="ul1715273514576"><li><strong id="b65901133114410"><a name="b65901133114410"></a><a name="b65901133114410"></a>email</strong>: The endpoints are email address.</li><li><strong id="b99571741008"><a name="b99571741008"></a><a name="b99571741008"></a>sms</strong>: The endpoints are phone numbers.</li><li><strong id="b1099011287223"><a name="b1099011287223"></a><a name="b1099011287223"></a>http</strong> and <strong id="b577715331224"><a name="b577715331224"></a><a name="b577715331224"></a>https</strong>: The endpoints are URLs.</li></ul>
    </td>
    </tr>
    <tr id="row57165101195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="p66970508195712"><a name="p66970508195712"></a><a name="p66970508195712"></a>subscription_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="p55902100195712"><a name="p55902100195712"></a><a name="p55902100195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="p31776236195712"><a name="p31776236195712"></a><a name="p31776236195712"></a>Resource identifier of a subscription, which is unique</p>
    </td>
    </tr>
    <tr id="row12318113195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="p58243097195712"><a name="p58243097195712"></a><a name="p58243097195712"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="p20070430195712"><a name="p20070430195712"></a><a name="p20070430195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="p15092119195712"><a name="p15092119195712"></a><a name="p15092119195712"></a>Project ID of the topic creator</p>
    </td>
    </tr>
    <tr id="row63410262195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="p35957569195712"><a name="p35957569195712"></a><a name="p35957569195712"></a>endpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="p26881981195712"><a name="p26881981195712"></a><a name="p26881981195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="p29956849195712"><a name="p29956849195712"></a><a name="p29956849195712"></a>Message receiving endpoint</p>
    </td>
    </tr>
    <tr id="row28162748195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="p66590149195712"><a name="p66590149195712"></a><a name="p66590149195712"></a>remark</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="p25092994195712"><a name="p25092994195712"></a><a name="p25092994195712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="p19266652195712"><a name="p19266652195712"></a><a name="p19266652195712"></a>Remarks</p>
    </td>
    </tr>
    <tr id="row19637006195712"><td class="cellrowborder" valign="top" width="28.6971302869713%" headers="mcps1.2.4.1.1 "><p id="p47093678195712"><a name="p47093678195712"></a><a name="p47093678195712"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.786821317868213%" headers="mcps1.2.4.1.2 "><p id="p56491591195712"><a name="p56491591195712"></a><a name="p56491591195712"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.51604839516049%" headers="mcps1.2.4.1.3 "><p id="p12416128195712"><a name="p12416128195712"></a><a name="p12416128195712"></a>Subscription status</p>
    <a name="ul1357151620117"></a><a name="ul1357151620117"></a><ul id="ul1357151620117"><li><strong id="b1964943612113"><a name="b1964943612113"></a><a name="b1964943612113"></a>0</strong>: unconfirmed</li><li><strong id="b1944317489116"><a name="b1944317489116"></a><a name="b1944317489116"></a>1</strong>: confirmed</li><li><strong id="b15634230216"><a name="b15634230216"></a><a name="b15634230216"></a>3</strong>: canceled</li></ul>
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
                "endpoint": "xxxxxxxxxxx", 
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


## Returned Value<a name="section41084157"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

