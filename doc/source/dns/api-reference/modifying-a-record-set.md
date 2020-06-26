# Modifying a Record Set<a name="EN-US_TOPIC_0077449085"></a>

## Function<a name="section49332166"></a>

Modify a record set.

## URI<a name="section41336317"></a>

-   URI format

    PUT  /v2/zones/\{zone\_id\}/recordsets/\{recordset\_id\}

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table52104579"></a><table><thead align="left"><tr id="row50570707"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p2586631"><a name="p2586631"></a><a name="p2586631"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.24222422242224%" id="mcps1.2.4.1.2"><p id="p8190559"><a name="p8190559"></a><a name="p8190559"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.42444244424442%" id="mcps1.2.4.1.3"><p id="p59455556"><a name="p59455556"></a><a name="p59455556"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51170717"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p51187411"><a name="p51187411"></a><a name="p51187411"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.24222422242224%" headers="mcps1.2.4.1.2 "><p id="p52539597"><a name="p52539597"></a><a name="p52539597"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.42444244424442%" headers="mcps1.2.4.1.3 "><p id="p27848947"><a name="p27848947"></a><a name="p27848947"></a>Zone ID</p>
    </td>
    </tr>
    <tr id="row49313939"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p35006119"><a name="p35006119"></a><a name="p35006119"></a>recordset_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.24222422242224%" headers="mcps1.2.4.1.2 "><p id="p16923420"><a name="p16923420"></a><a name="p16923420"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.42444244424442%" headers="mcps1.2.4.1.3 "><p id="p28619802"><a name="p28619802"></a><a name="p28619802"></a>ID of the record set to be modified</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36482533"></a>

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="table9470531173211"></a><table><thead align="left"><tr id="row60397351173211"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.5.1.1"><p id="p65819295173211"><a name="p65819295173211"></a><a name="p65819295173211"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.29%" id="mcps1.2.5.1.2"><p id="p42278174173211"><a name="p42278174173211"></a><a name="p42278174173211"></a><strong id="b593421527191713_1"><a name="b593421527191713_1"></a><a name="b593421527191713_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.45%" id="mcps1.2.5.1.3"><p id="p26309572173211"><a name="p26309572173211"></a><a name="p26309572173211"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.81%" id="mcps1.2.5.1.4"><p id="p67071922173211"><a name="p67071922173211"></a><a name="p67071922173211"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34337486173211"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p33154613173211"><a name="p33154613173211"></a><a name="p33154613173211"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.5.1.2 "><p id="p28540882173211"><a name="p28540882173211"></a><a name="p28540882173211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.3 "><p id="p37402311173211"><a name="p37402311173211"></a><a name="p37402311173211"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.81%" headers="mcps1.2.5.1.4 "><p id="p43441715173211"><a name="p43441715173211"></a><a name="p43441715173211"></a>(Optional) Description for the domain name</p>
    <p id="p9966775173211"><a name="p9966775173211"></a><a name="p9966775173211"></a>The value cannot exceed 255 characters.</p>
    </td>
    </tr>
    <tr id="row44235645173211"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p56753577173211"><a name="p56753577173211"></a><a name="p56753577173211"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.5.1.2 "><p id="p44923213173211"><a name="p44923213173211"></a><a name="p44923213173211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.3 "><p id="p45055368173211"><a name="p45055368173211"></a><a name="p45055368173211"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.81%" headers="mcps1.2.5.1.4 "><p id="p41610046141952"><a name="p41610046141952"></a><a name="p41610046141952"></a>Caching period of the record set (in seconds)</p>
    <p id="p54818170173211"><a name="p54818170173211"></a><a name="p54818170173211"></a>The default value is <strong id="b84235270615612"><a name="b84235270615612"></a><a name="b84235270615612"></a>300s</strong>.</p>
    <p id="p20437753173211"><a name="p20437753173211"></a><a name="p20437753173211"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    <tr id="row59750658173211"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p62596825173211"><a name="p62596825173211"></a><a name="p62596825173211"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.5.1.2 "><p id="p32296167173211"><a name="p32296167173211"></a><a name="p32296167173211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.45%" headers="mcps1.2.5.1.3 "><p id="p5792332173211"><a name="p5792332173211"></a><a name="p5792332173211"></a>List&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.81%" headers="mcps1.2.5.1.4 "><p id="p8321575173211"><a name="p8321575173211"></a><a name="p8321575173211"></a>Record set value, which varies depending on the record set type.</p>
    <p id="p813988173211"><a name="p813988173211"></a><a name="p813988173211"></a>For example, the value of an AAAA record set is the IPv6 address list mapped to the domain name.</p>
    <p id="p59053902173211"><a name="p59053902173211"></a><a name="p59053902173211"></a>For details, see section <strong id="b84235270610515"><a name="b84235270610515"></a><a name="b84235270610515"></a>Management</strong> &gt; <strong id="b842352706105111"><a name="b842352706105111"></a><a name="b842352706105111"></a>Managing Record Sets</strong> &gt; <strong id="b842352706105146"><a name="b842352706105146"></a><a name="b842352706105146"></a>Adding a Record Set</strong> in the <em id="i842352697105158"><a name="i842352697105158"></a><a name="i842352697105158"></a>Domain Name Service User Guide</em>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request
    -   A type

        ```
        {
            "description": "This is an example record set.",
            "ttl": 3600,
            "records": [
                "192.168.10.1",
                "192.168.10.2"
            ]
        }
        ```

    -   AAAA type

        ```
        {
            "description": "This is an example record set.",
            "ttl": 3600,
            "records": [
                "fe80:0:0:0:202:b3ff:fe1e:8329",
                "ff03:0db8:85a3:0:0:8a2e:0370:7334"
            ]
        }
        ```

    -   MX type

        ```
        {
            "description": "This is an example record set.",
            "ttl": 3600,
            "records": [
                "1 mail.example.com"
            ]
        }
        ```

    -   CNAME type

        ```
        {
            "description": "This is an example record set.",
            "ttl": 3600,
            "records": [
                "server1.example.com"
            ]
        }
        ```

    -   TXT type

        ```
        {
            "description": "This is an example record set.",
            "ttl": 300,
            "records": [
                "\"This host is used for sale.\""
            ]
        }
        ```

    -   NS type

        ```
        {
            "description": "This is an example record set.",
            "ttl": 300,
            "records": [
                "node1.example.com.",
                "node2.example.com."
            ]
        }
        ```

    -   SRV type

        ```
        {
            "description": "This is an example record set.",
            "ttl": 3600,
            "records": [
                "3 60 2176 sipserver.example.com.",
                "10 100 2176 sipserver.example.com."
            ]
        }
        ```

    -   PTR type

        ```
        {
            "description": "This is an example record set.",
            "ttl": 3600,
            "records": [
                "host.example.com."
        
            ]
        }
        
        ```

    -   CAA type

        ```
        {
            "name": "www.example.com.",
            "description": "This is an example record set.",
            "type": "CAA",
            "ttl": 300,
            "records": [
                "0 issue \"example.com\"",
                "0 issuewild \"www.certinomis.com\"",
                "0 iodef \"mailto:xx@example.org\"",
                "0 iodef \"http://iodef.example.com\""
            ]
        }
        ```



## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  3**  Parameters in the response

    <a name="table44131970191032"></a><table><thead align="left"><tr id="en-us_topic_0037134404_row52466955175323"><th class="cellrowborder" valign="top" width="27.889999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0037134404_p2769858175323"><a name="en-us_topic_0037134404_p2769858175323"></a><a name="en-us_topic_0037134404_p2769858175323"></a><strong id="en-us_topic_0037134404_b162774213314533"><a name="en-us_topic_0037134404_b162774213314533"></a><a name="en-us_topic_0037134404_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.55%" id="mcps1.2.4.1.2"><p id="en-us_topic_0037134404_p46296309175323"><a name="en-us_topic_0037134404_p46296309175323"></a><a name="en-us_topic_0037134404_p46296309175323"></a><strong id="en-us_topic_0037134404_b84235270619112"><a name="en-us_topic_0037134404_b84235270619112"></a><a name="en-us_topic_0037134404_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.56%" id="mcps1.2.4.1.3"><p id="en-us_topic_0037134404_p62697904175323"><a name="en-us_topic_0037134404_p62697904175323"></a><a name="en-us_topic_0037134404_p62697904175323"></a><strong id="en-us_topic_0037134404_b842352706112423"><a name="en-us_topic_0037134404_b842352706112423"></a><a name="en-us_topic_0037134404_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0037134404_row47909891175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p64112397175323"><a name="en-us_topic_0037134404_p64112397175323"></a><a name="en-us_topic_0037134404_p64112397175323"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p1660870175323"><a name="en-us_topic_0037134404_p1660870175323"></a><a name="en-us_topic_0037134404_p1660870175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p1249204175323"><a name="en-us_topic_0037134404_p1249204175323"></a><a name="en-us_topic_0037134404_p1249204175323"></a>Record set ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row6942422175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p64097412175323"><a name="en-us_topic_0037134404_p64097412175323"></a><a name="en-us_topic_0037134404_p64097412175323"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p44990515175323"><a name="en-us_topic_0037134404_p44990515175323"></a><a name="en-us_topic_0037134404_p44990515175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p32019574175323"><a name="en-us_topic_0037134404_p32019574175323"></a><a name="en-us_topic_0037134404_p32019574175323"></a>Record set name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row61442071175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p51194416175323"><a name="en-us_topic_0037134404_p51194416175323"></a><a name="en-us_topic_0037134404_p51194416175323"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p63301991175323"><a name="en-us_topic_0037134404_p63301991175323"></a><a name="en-us_topic_0037134404_p63301991175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p43966660175323"><a name="en-us_topic_0037134404_p43966660175323"></a><a name="en-us_topic_0037134404_p43966660175323"></a>Record set description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row2176746175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p11805366175323"><a name="en-us_topic_0037134404_p11805366175323"></a><a name="en-us_topic_0037134404_p11805366175323"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p1051908175323"><a name="en-us_topic_0037134404_p1051908175323"></a><a name="en-us_topic_0037134404_p1051908175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p10043845175323"><a name="en-us_topic_0037134404_p10043845175323"></a><a name="en-us_topic_0037134404_p10043845175323"></a>Zone ID of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row61212722175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p8318586175323"><a name="en-us_topic_0037134404_p8318586175323"></a><a name="en-us_topic_0037134404_p8318586175323"></a>zone_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p31287919175323"><a name="en-us_topic_0037134404_p31287919175323"></a><a name="en-us_topic_0037134404_p31287919175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p16372315175323"><a name="en-us_topic_0037134404_p16372315175323"></a><a name="en-us_topic_0037134404_p16372315175323"></a>Zone name of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row38132372175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p37461920175323"><a name="en-us_topic_0037134404_p37461920175323"></a><a name="en-us_topic_0037134404_p37461920175323"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p27536075175323"><a name="en-us_topic_0037134404_p27536075175323"></a><a name="en-us_topic_0037134404_p27536075175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p24813356175323"><a name="en-us_topic_0037134404_p24813356175323"></a><a name="en-us_topic_0037134404_p24813356175323"></a>Record set type</p>
    <p id="en-us_topic_0037134404_p173531225174112"><a name="en-us_topic_0037134404_p173531225174112"></a><a name="en-us_topic_0037134404_p173531225174112"></a>The value can be <strong id="en-us_topic_0037134404_b84235270693731"><a name="en-us_topic_0037134404_b84235270693731"></a><a name="en-us_topic_0037134404_b84235270693731"></a>A</strong>, <strong id="en-us_topic_0037134404_b84235270693735"><a name="en-us_topic_0037134404_b84235270693735"></a><a name="en-us_topic_0037134404_b84235270693735"></a>AAAA</strong>, <strong id="en-us_topic_0037134404_b84235270693738"><a name="en-us_topic_0037134404_b84235270693738"></a><a name="en-us_topic_0037134404_b84235270693738"></a>MX</strong>, <strong id="en-us_topic_0037134404_b84235270693741"><a name="en-us_topic_0037134404_b84235270693741"></a><a name="en-us_topic_0037134404_b84235270693741"></a>CNAME</strong>, <strong id="en-us_topic_0037134404_b84235270693746"><a name="en-us_topic_0037134404_b84235270693746"></a><a name="en-us_topic_0037134404_b84235270693746"></a>TXT</strong>, <strong id="en-us_topic_0037134404_b84235270693755"><a name="en-us_topic_0037134404_b84235270693755"></a><a name="en-us_topic_0037134404_b84235270693755"></a>NS</strong> (only in public zones), <strong id="en-us_topic_0037134404_b8423527069382"><a name="en-us_topic_0037134404_b8423527069382"></a><a name="en-us_topic_0037134404_b8423527069382"></a>SRV</strong>, <strong id="en-us_topic_0037134404_b8423527069385"><a name="en-us_topic_0037134404_b8423527069385"></a><a name="en-us_topic_0037134404_b8423527069385"></a>PTR</strong> (only in private zones), and <strong id="en-us_topic_0037134404_b84235270693810"><a name="en-us_topic_0037134404_b84235270693810"></a><a name="en-us_topic_0037134404_b84235270693810"></a>CAA</strong> (only in public zones).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row20796819175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p4811553175323"><a name="en-us_topic_0037134404_p4811553175323"></a><a name="en-us_topic_0037134404_p4811553175323"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p47559731175323"><a name="en-us_topic_0037134404_p47559731175323"></a><a name="en-us_topic_0037134404_p47559731175323"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p35349847185925"><a name="en-us_topic_0037134404_p35349847185925"></a><a name="en-us_topic_0037134404_p35349847185925"></a>Caching period of a domain name (in seconds)</p>
    <p id="en-us_topic_0037134404_p2275826812726"><a name="en-us_topic_0037134404_p2275826812726"></a><a name="en-us_topic_0037134404_p2275826812726"></a>A longer caching period makes a change on the authoritative DNS server take longer time to be synchronized to other DNS servers.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row13978060175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p43388342175323"><a name="en-us_topic_0037134404_p43388342175323"></a><a name="en-us_topic_0037134404_p43388342175323"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p29596719175323"><a name="en-us_topic_0037134404_p29596719175323"></a><a name="en-us_topic_0037134404_p29596719175323"></a>List&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p30492925175323"><a name="en-us_topic_0037134404_p30492925175323"></a><a name="en-us_topic_0037134404_p30492925175323"></a>Domain name resolution result</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row23148559175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p36524189175323"><a name="en-us_topic_0037134404_p36524189175323"></a><a name="en-us_topic_0037134404_p36524189175323"></a>create_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p47080972175323"><a name="en-us_topic_0037134404_p47080972175323"></a><a name="en-us_topic_0037134404_p47080972175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p15737135175323"><a name="en-us_topic_0037134404_p15737135175323"></a><a name="en-us_topic_0037134404_p15737135175323"></a>Time when the record set was created</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row33465792175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p42570937175323"><a name="en-us_topic_0037134404_p42570937175323"></a><a name="en-us_topic_0037134404_p42570937175323"></a>update_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p27449776175323"><a name="en-us_topic_0037134404_p27449776175323"></a><a name="en-us_topic_0037134404_p27449776175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p63703533175323"><a name="en-us_topic_0037134404_p63703533175323"></a><a name="en-us_topic_0037134404_p63703533175323"></a>Time when the record set was updated</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row17850883175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p36228271175323"><a name="en-us_topic_0037134404_p36228271175323"></a><a name="en-us_topic_0037134404_p36228271175323"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p6480061175323"><a name="en-us_topic_0037134404_p6480061175323"></a><a name="en-us_topic_0037134404_p6480061175323"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p28721670185925"><a name="en-us_topic_0037134404_p28721670185925"></a><a name="en-us_topic_0037134404_p28721670185925"></a>Resource status, which can be <strong id="en-us_topic_0037134404_b842352706121016"><a name="en-us_topic_0037134404_b842352706121016"></a><a name="en-us_topic_0037134404_b842352706121016"></a>PENDING_CREATE</strong>, <strong id="en-us_topic_0037134404_b842352706121023"><a name="en-us_topic_0037134404_b842352706121023"></a><a name="en-us_topic_0037134404_b842352706121023"></a>ACTIVE</strong>, <strong id="en-us_topic_0037134404_b842352706112413"><a name="en-us_topic_0037134404_b842352706112413"></a><a name="en-us_topic_0037134404_b842352706112413"></a>PENDING_DELETE</strong>, <strong id="en-us_topic_0037134404_b842352706104310"><a name="en-us_topic_0037134404_b842352706104310"></a><a name="en-us_topic_0037134404_b842352706104310"></a>PENDING_UPDATE</strong>, or <strong id="en-us_topic_0037134404_b84235270691843"><a name="en-us_topic_0037134404_b84235270691843"></a><a name="en-us_topic_0037134404_b84235270691843"></a>ERROR</strong></p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row61184424175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p49633411175323"><a name="en-us_topic_0037134404_p49633411175323"></a><a name="en-us_topic_0037134404_p49633411175323"></a>default</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p56048766175323"><a name="en-us_topic_0037134404_p56048766175323"></a><a name="en-us_topic_0037134404_p56048766175323"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p52627220185925"><a name="en-us_topic_0037134404_p52627220185925"></a><a name="en-us_topic_0037134404_p52627220185925"></a>Whether the record set is created by default</p>
    <p id="en-us_topic_0037134404_p46587348115949"><a name="en-us_topic_0037134404_p46587348115949"></a><a name="en-us_topic_0037134404_p46587348115949"></a>A default record set cannot be deleted or modified.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row15199048201026"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p23163408201026"><a name="en-us_topic_0037134404_p23163408201026"></a><a name="en-us_topic_0037134404_p23163408201026"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p40653752201026"><a name="en-us_topic_0037134404_p40653752201026"></a><a name="en-us_topic_0037134404_p40653752201026"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p4619625201026"><a name="en-us_topic_0037134404_p4619625201026"></a><a name="en-us_topic_0037134404_p4619625201026"></a>Project ID of the record set</p>
    </td>
    </tr>
    <tr id="en-us_topic_0037134404_row3965248419366"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037134404_p2132803819366"><a name="en-us_topic_0037134404_p2132803819366"></a><a name="en-us_topic_0037134404_p2132803819366"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037134404_p1127763319366"><a name="en-us_topic_0037134404_p1127763319366"></a><a name="en-us_topic_0037134404_p1127763319366"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037134404_p1368584110253"><a name="en-us_topic_0037134404_p1368584110253"></a><a name="en-us_topic_0037134404_p1368584110253"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0037134404_p4371306185925"><a name="en-us_topic_0037134404_p4371306185925"></a><a name="en-us_topic_0037134404_p4371306185925"></a>When a response is broken into pages, a <strong id="en-us_topic_0037134404_b38947790110750"><a name="en-us_topic_0037134404_b38947790110750"></a><a name="en-us_topic_0037134404_b38947790110750"></a>next</strong> link is provided to retrieve all results.</p>
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
        "ttl": 3600,
        "records": [
            "192.168.10.1",
            "192.168.10.2"
        ],
        "status": "PENDING_UPDATE",
        "links": {
            "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149/recordsets/2c9eb155587228570158722b6ac30007"
        },
        "zone_id": "2c9eb155587194ec01587224c9f90149",
        "zone_name": "example.com.",
        "create_at": "2016-11-17T12:03:17.827",
        "update_at": "2016-11-17T12:56:03.827",
        "default": false,
        "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c"
    }
    ```


## **Returned Value**<a name="section42637797161043"></a>

See  [General Request Return Code](general-request-return-code.md).

