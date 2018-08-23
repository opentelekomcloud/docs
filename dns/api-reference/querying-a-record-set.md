# Querying a Record Set<a name="EN-US_TOPIC_0037129968"></a>

## Function<a name="section18389930"></a>

Query a record set.

## URI<a name="section31291646"></a>

-   URI format

    GET /v2/zones/\{zone\_id\}/recordsets/\{recordset\_id\}

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table21421675"></a><table><thead align="left"><tr id="row9119245"><th class="cellrowborder" valign="top" width="25.629999999999995%" id="mcps1.2.4.1.1"><p id="p461342"><a name="p461342"></a><a name="p461342"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.81%" id="mcps1.2.4.1.2"><p id="p37368736"><a name="p37368736"></a><a name="p37368736"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.559999999999995%" id="mcps1.2.4.1.3"><p id="p6968762"><a name="p6968762"></a><a name="p6968762"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27598869"><td class="cellrowborder" valign="top" width="25.629999999999995%" headers="mcps1.2.4.1.1 "><p id="p20915929"><a name="p20915929"></a><a name="p20915929"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.2.4.1.2 "><p id="p16468652"><a name="p16468652"></a><a name="p16468652"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p58892473"><a name="p58892473"></a><a name="p58892473"></a>Zone ID</p>
    </td>
    </tr>
    <tr id="row60270212"><td class="cellrowborder" valign="top" width="25.629999999999995%" headers="mcps1.2.4.1.1 "><p id="p50048984"><a name="p50048984"></a><a name="p50048984"></a>recordset_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.2.4.1.2 "><p id="p27435897"><a name="p27435897"></a><a name="p27435897"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p7715150"><a name="p7715150"></a><a name="p7715150"></a>Record set ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13189358"></a>

None

## Response<a name="section51595365"></a>

-   Parameter description

    **Table  2**  Parameters in the response

    <a name="table28278595"></a><table><thead align="left"><tr id="en-us_topic_0037134404_row52466955175323"><th class="cellrowborder" valign="top" width="27.889999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037134404_p2769858175323"><a name="en-us_topic_0037134404_p2769858175323"></a><a name="en-us_topic_0037134404_p2769858175323"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0037134404_p46296309175323"><a name="en-us_topic_0037134404_p46296309175323"></a><a name="en-us_topic_0037134404_p46296309175323"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.3%" id="mcps1.2.4.1.3"><p id="en-us_topic_0037134404_p62697904175323"><a name="en-us_topic_0037134404_p62697904175323"></a><a name="en-us_topic_0037134404_p62697904175323"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0037134404_row47909891175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p64112397175323"><a name="en-us_topic_0037134404_p64112397175323"></a><a name="en-us_topic_0037134404_p64112397175323"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p1660870175323"><a name="en-us_topic_0037134404_p1660870175323"></a><a name="en-us_topic_0037134404_p1660870175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p1249204175323"><a name="en-us_topic_0037134404_p1249204175323"></a><a name="en-us_topic_0037134404_p1249204175323"></a>Record set ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row6942422175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p64097412175323"><a name="en-us_topic_0037134404_p64097412175323"></a><a name="en-us_topic_0037134404_p64097412175323"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p44990515175323"><a name="en-us_topic_0037134404_p44990515175323"></a><a name="en-us_topic_0037134404_p44990515175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p32019574175323"><a name="en-us_topic_0037134404_p32019574175323"></a><a name="en-us_topic_0037134404_p32019574175323"></a>Record set name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row61442071175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p51194416175323"><a name="en-us_topic_0037134404_p51194416175323"></a><a name="en-us_topic_0037134404_p51194416175323"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p63301991175323"><a name="en-us_topic_0037134404_p63301991175323"></a><a name="en-us_topic_0037134404_p63301991175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p43966660175323"><a name="en-us_topic_0037134404_p43966660175323"></a><a name="en-us_topic_0037134404_p43966660175323"></a>Record set description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row2176746175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p11805366175323"><a name="en-us_topic_0037134404_p11805366175323"></a><a name="en-us_topic_0037134404_p11805366175323"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p1051908175323"><a name="en-us_topic_0037134404_p1051908175323"></a><a name="en-us_topic_0037134404_p1051908175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p10043845175323"><a name="en-us_topic_0037134404_p10043845175323"></a><a name="en-us_topic_0037134404_p10043845175323"></a>Zone ID of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row61212722175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p8318586175323"><a name="en-us_topic_0037134404_p8318586175323"></a><a name="en-us_topic_0037134404_p8318586175323"></a>zone_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p31287919175323"><a name="en-us_topic_0037134404_p31287919175323"></a><a name="en-us_topic_0037134404_p31287919175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p16372315175323"><a name="en-us_topic_0037134404_p16372315175323"></a><a name="en-us_topic_0037134404_p16372315175323"></a>Zone name of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row38132372175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p37461920175323"><a name="en-us_topic_0037134404_p37461920175323"></a><a name="en-us_topic_0037134404_p37461920175323"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p27536075175323"><a name="en-us_topic_0037134404_p27536075175323"></a><a name="en-us_topic_0037134404_p27536075175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p24813356175323"><a name="en-us_topic_0037134404_p24813356175323"></a><a name="en-us_topic_0037134404_p24813356175323"></a>Record set type</p>
    <p id="p6203146164115"><a name="p6203146164115"></a><a name="p6203146164115"></a>The value can be <strong id="b84235270693731"><a name="b84235270693731"></a><a name="b84235270693731"></a>A</strong>,&nbsp;<strong id="b84235270693735"><a name="b84235270693735"></a><a name="b84235270693735"></a>AAAA</strong>,&nbsp;<strong id="b84235270693738"><a name="b84235270693738"></a><a name="b84235270693738"></a>MX</strong>,&nbsp;<strong id="b84235270693741"><a name="b84235270693741"></a><a name="b84235270693741"></a>CNAME</strong>,&nbsp;<strong id="b84235270693746"><a name="b84235270693746"></a><a name="b84235270693746"></a>TXT</strong>,&nbsp;<strong id="b84235270693755"><a name="b84235270693755"></a><a name="b84235270693755"></a>NS</strong>&nbsp;(only in public zones),&nbsp;<strong id="b8423527069403"><a name="b8423527069403"></a><a name="b8423527069403"></a>SOA</strong>,&nbsp;<strong id="b8423527069382"><a name="b8423527069382"></a><a name="b8423527069382"></a>SRV</strong>,&nbsp;<strong id="b8423527069385"><a name="b8423527069385"></a><a name="b8423527069385"></a>PTR</strong>&nbsp;(only in private zones), and&nbsp;<strong id="b84235270693810"><a name="b84235270693810"></a><a name="b84235270693810"></a>CAA</strong> (only in public zones).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row20796819175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p4811553175323"><a name="en-us_topic_0037134404_p4811553175323"></a><a name="en-us_topic_0037134404_p4811553175323"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p47559731175323"><a name="en-us_topic_0037134404_p47559731175323"></a><a name="en-us_topic_0037134404_p47559731175323"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="p19063127173959"><a name="p19063127173959"></a><a name="p19063127173959"></a>Caching period of a domain name (in seconds)</p>
    <p id="en-us_topic_0037134404_p22097398175323"><a name="en-us_topic_0037134404_p22097398175323"></a><a name="en-us_topic_0037134404_p22097398175323"></a>A longer caching period makes a change on the authoritative DNS server take longer time to be synchronized to other DNS servers.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row13978060175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p43388342175323"><a name="en-us_topic_0037134404_p43388342175323"></a><a name="en-us_topic_0037134404_p43388342175323"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p29596719175323"><a name="en-us_topic_0037134404_p29596719175323"></a><a name="en-us_topic_0037134404_p29596719175323"></a>List&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p30492925175323"><a name="en-us_topic_0037134404_p30492925175323"></a><a name="en-us_topic_0037134404_p30492925175323"></a>Domain name resolution result</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row23148559175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p36524189175323"><a name="en-us_topic_0037134404_p36524189175323"></a><a name="en-us_topic_0037134404_p36524189175323"></a>create_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p47080972175323"><a name="en-us_topic_0037134404_p47080972175323"></a><a name="en-us_topic_0037134404_p47080972175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p15737135175323"><a name="en-us_topic_0037134404_p15737135175323"></a><a name="en-us_topic_0037134404_p15737135175323"></a>Time when the record set was created</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row33465792175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p42570937175323"><a name="en-us_topic_0037134404_p42570937175323"></a><a name="en-us_topic_0037134404_p42570937175323"></a>update_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p27449776175323"><a name="en-us_topic_0037134404_p27449776175323"></a><a name="en-us_topic_0037134404_p27449776175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p63703533175323"><a name="en-us_topic_0037134404_p63703533175323"></a><a name="en-us_topic_0037134404_p63703533175323"></a>Time when the record set was updated</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row17850883175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p36228271175323"><a name="en-us_topic_0037134404_p36228271175323"></a><a name="en-us_topic_0037134404_p36228271175323"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p6480061175323"><a name="en-us_topic_0037134404_p6480061175323"></a><a name="en-us_topic_0037134404_p6480061175323"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p65781854175323"><a name="en-us_topic_0037134404_p65781854175323"></a><a name="en-us_topic_0037134404_p65781854175323"></a>Resource status</p>
    <p id="en-us_topic_0037134404_p51374523175323"><a name="en-us_topic_0037134404_p51374523175323"></a><a name="en-us_topic_0037134404_p51374523175323"></a>The value can be <strong id="b84235270695628"><a name="b84235270695628"></a><a name="b84235270695628"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>,&nbsp;<strong id="b84235270683910"><a name="b84235270683910"></a><a name="b84235270683910"></a>PENDING_UPDATE</strong>,&nbsp;<strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_DELETE</strong>, or&nbsp;<strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row61184424175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p49633411175323"><a name="en-us_topic_0037134404_p49633411175323"></a><a name="en-us_topic_0037134404_p49633411175323"></a>default</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p56048766175323"><a name="en-us_topic_0037134404_p56048766175323"></a><a name="en-us_topic_0037134404_p56048766175323"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="p64010884174034"><a name="p64010884174034"></a><a name="p64010884174034"></a>Whether the record set is created by default</p>
    <p id="p39227046174034"><a name="p39227046174034"></a><a name="p39227046174034"></a>A default record set cannot be deleted or modified.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row15199048201026"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p23163408201026"><a name="en-us_topic_0037134404_p23163408201026"></a><a name="en-us_topic_0037134404_p23163408201026"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p40653752201026"><a name="en-us_topic_0037134404_p40653752201026"></a><a name="en-us_topic_0037134404_p40653752201026"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p4619625201026"><a name="en-us_topic_0037134404_p4619625201026"></a><a name="en-us_topic_0037134404_p4619625201026"></a>Project ID of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row3965248419366"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p2132803819366"><a name="en-us_topic_0037134404_p2132803819366"></a><a name="en-us_topic_0037134404_p2132803819366"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p1127763319366"><a name="en-us_topic_0037134404_p1127763319366"></a><a name="en-us_topic_0037134404_p1127763319366"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.3%" headers="mcps1.2.4.1.3 "><p id="p4006161419514"><a name="p4006161419514"></a><a name="p4006161419514"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0037134404_p4107308719366"><a name="en-us_topic_0037134404_p4107308719366"></a><a name="en-us_topic_0037134404_p4107308719366"></a>When a response is broken into pages, a <strong id="b84235270695245"><a name="b84235270695245"></a><a name="b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "id": "2c9eb155587228570158722b6ac30007",
        "name": "www.example.com.",
        "description": "This is an example record set.",
        "type": "A",
        "ttl": 300,
        "records": [
            "192.168.10.2",
            "192.168.10.1"
        ],
        "status": "PENDING_CREATE",
        "links": {
            "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149/recordsets/2c9eb155587228570158722b6ac30007"
        },
        "zone_id": "2c9eb155587194ec01587224c9f90149",
        "zone_name": "example.com.",
        "create_at": "2016-11-17T12:03:17.827",
        "update_at": "2016-11-17T12:03:18.827",
        "default": false,
        "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c"
    }
    
    ```


## Returned Value<a name="section61705107"></a>

See  [General Request Return Code](general-request-return-code.md).

