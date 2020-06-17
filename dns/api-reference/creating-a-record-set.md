# Creating a Record Set<a name="EN-US_TOPIC_0037134404"></a>

## Function<a name="section2763065016101"></a>

Create a record set.

## URI<a name="section53701671161015"></a>

-   URI format

    POST /v2/zones/\{zone\_id\}/recordsets

-   Parameter description

    **Table  1**  Parameter in the URI

    <a name="table30807893173129"></a><table><thead align="left"><tr id="row38661368173129"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.1"><p id="p14212988173129"><a name="p14212988173129"></a><a name="p14212988173129"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.069999999999997%" id="mcps1.2.4.1.2"><p id="p23287688173129"><a name="p23287688173129"></a><a name="p23287688173129"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.6%" id="mcps1.2.4.1.3"><p id="p1114682173129"><a name="p1114682173129"></a><a name="p1114682173129"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6301875173129"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p5124116173129"><a name="p5124116173129"></a><a name="p5124116173129"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.069999999999997%" headers="mcps1.2.4.1.2 "><p id="p65804667173129"><a name="p65804667173129"></a><a name="p65804667173129"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6%" headers="mcps1.2.4.1.3 "><p id="p56820233173129"><a name="p56820233173129"></a><a name="p56820233173129"></a>Zone ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44958995161021"></a>

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="table9470531173211"></a><table><thead align="left"><tr id="row60397351173211"><th class="cellrowborder" valign="top" width="19.25%" id="mcps1.2.5.1.1"><p id="p65819295173211"><a name="p65819295173211"></a><a name="p65819295173211"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.54%" id="mcps1.2.5.1.2"><p id="p42278174173211"><a name="p42278174173211"></a><a name="p42278174173211"></a><strong id="b11039231112234"><a name="b11039231112234"></a><a name="b11039231112234"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.809999999999999%" id="mcps1.2.5.1.3"><p id="p26309572173211"><a name="p26309572173211"></a><a name="p26309572173211"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.4%" id="mcps1.2.5.1.4"><p id="p67071922173211"><a name="p67071922173211"></a><a name="p67071922173211"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65160710173211"><td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.5.1.1 "><p id="p21415905173211"><a name="p21415905173211"></a><a name="p21415905173211"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54%" headers="mcps1.2.5.1.2 "><p id="p58188388173211"><a name="p58188388173211"></a><a name="p58188388173211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.809999999999999%" headers="mcps1.2.5.1.3 "><p id="p45293229173211"><a name="p45293229173211"></a><a name="p45293229173211"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.4%" headers="mcps1.2.5.1.4 "><p id="p5054941173211"><a name="p5054941173211"></a><a name="p5054941173211"></a>Fully qualified domain name (FQDN) suffixed with a zone name, which is a complete host name ended with a dot</p>
    <p id="p27471407151355"><a name="p27471407151355"></a><a name="p27471407151355"></a>A domain name is case insensitive. Uppercase letters will also be converted into lowercase letters.</p>
    </td>
    </tr>
    <tr id="row34337486173211"><td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.5.1.1 "><p id="p33154613173211"><a name="p33154613173211"></a><a name="p33154613173211"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54%" headers="mcps1.2.5.1.2 "><p id="p28540882173211"><a name="p28540882173211"></a><a name="p28540882173211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.809999999999999%" headers="mcps1.2.5.1.3 "><p id="p37402311173211"><a name="p37402311173211"></a><a name="p37402311173211"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.4%" headers="mcps1.2.5.1.4 "><p id="p11980181185925"><a name="p11980181185925"></a><a name="p11980181185925"></a>(Optional) Description of the domain name, which must not exceed 255 characters</p>
    </td>
    </tr>
    <tr id="row52503862173211"><td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.5.1.1 "><p id="p4265712173211"><a name="p4265712173211"></a><a name="p4265712173211"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54%" headers="mcps1.2.5.1.2 "><p id="p43588224173211"><a name="p43588224173211"></a><a name="p43588224173211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.809999999999999%" headers="mcps1.2.5.1.3 "><p id="p44233480173211"><a name="p44233480173211"></a><a name="p44233480173211"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.4%" headers="mcps1.2.5.1.4 "><p id="p29114279173211"><a name="p29114279173211"></a><a name="p29114279173211"></a>Record set type</p>
    <p id="p160041663916"><a name="p160041663916"></a><a name="p160041663916"></a>The value can be <strong id="b84235270693731"><a name="b84235270693731"></a><a name="b84235270693731"></a>A</strong>, <strong id="b84235270693735"><a name="b84235270693735"></a><a name="b84235270693735"></a>AAAA</strong>, <strong id="b84235270693738"><a name="b84235270693738"></a><a name="b84235270693738"></a>MX</strong>, <strong id="b84235270693741"><a name="b84235270693741"></a><a name="b84235270693741"></a>CNAME</strong>, <strong id="b84235270693746"><a name="b84235270693746"></a><a name="b84235270693746"></a>TXT</strong>, <strong id="b84235270693755"><a name="b84235270693755"></a><a name="b84235270693755"></a>NS</strong> (only in public zones), <strong id="b8423527069382"><a name="b8423527069382"></a><a name="b8423527069382"></a>SRV</strong>, <strong id="b8423527069385"><a name="b8423527069385"></a><a name="b8423527069385"></a>PTR</strong> (only in private zones), and <strong id="b84235270693810"><a name="b84235270693810"></a><a name="b84235270693810"></a>CAA</strong> (only in public zones).</p>
    </td>
    </tr>
    <tr id="row44235645173211"><td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.5.1.1 "><p id="p56753577173211"><a name="p56753577173211"></a><a name="p56753577173211"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54%" headers="mcps1.2.5.1.2 "><p id="p44923213173211"><a name="p44923213173211"></a><a name="p44923213173211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.809999999999999%" headers="mcps1.2.5.1.3 "><p id="p15148058212620"><a name="p15148058212620"></a><a name="p15148058212620"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.4%" headers="mcps1.2.5.1.4 "><p id="p41610046141952"><a name="p41610046141952"></a><a name="p41610046141952"></a>Caching period of the record set (in seconds)</p>
    <p id="p54818170173211"><a name="p54818170173211"></a><a name="p54818170173211"></a>The default value is <strong id="b84235270615612"><a name="b84235270615612"></a><a name="b84235270615612"></a>300s</strong>.</p>
    <p id="p66468204185925"><a name="p66468204185925"></a><a name="p66468204185925"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    <tr id="row59750658173211"><td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.5.1.1 "><p id="p62596825173211"><a name="p62596825173211"></a><a name="p62596825173211"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54%" headers="mcps1.2.5.1.2 "><p id="p32296167173211"><a name="p32296167173211"></a><a name="p32296167173211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.809999999999999%" headers="mcps1.2.5.1.3 "><p id="p5792332173211"><a name="p5792332173211"></a><a name="p5792332173211"></a>List&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.4%" headers="mcps1.2.5.1.4 "><p id="p8321575173211"><a name="p8321575173211"></a><a name="p8321575173211"></a>Record set value, which varies depending on the record set type.</p>
    <p id="p54934263185925"><a name="p54934263185925"></a><a name="p54934263185925"></a>For example, the value of an AAAA record set is the IPv6 address list mapped to the domain name.</p>
    <p id="p59053902173211"><a name="p59053902173211"></a><a name="p59053902173211"></a>For details, see section "Managing Record Sets" in the <em id="i842352697143148"><a name="i842352697143148"></a><a name="i842352697143148"></a>Domain Name Service User Guide</em>.</p>
    </td>
    </tr>
    <tr id="row11879661194927"><td class="cellrowborder" valign="top" width="19.25%" headers="mcps1.2.5.1.1 "><p id="p24376203194927"><a name="p24376203194927"></a><a name="p24376203194927"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54%" headers="mcps1.2.5.1.2 "><p id="p28315431194927"><a name="p28315431194927"></a><a name="p28315431194927"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.809999999999999%" headers="mcps1.2.5.1.3 "><p id="p11848571194927"><a name="p11848571194927"></a><a name="p11848571194927"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.4%" headers="mcps1.2.5.1.4 "><p id="p20210224194927"><a name="p20210224194927"></a><a name="p20210224194927"></a>Resource tag. For details, see <a href="#EN-US_TOPIC_0037134404__table19530794112436">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the tag list

    <a name="table19530794112436"></a><table><thead align="left"><tr id="en-us_topic_0057310891_row15361836112436"><th class="cellrowborder" valign="top" width="17.28%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057310891_p58707511112436"><a name="en-us_topic_0057310891_p58707511112436"></a><a name="en-us_topic_0057310891_p58707511112436"></a><strong id="en-us_topic_0057310891_b162774213314533"><a name="en-us_topic_0057310891_b162774213314533"></a><a name="en-us_topic_0057310891_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057310891_p57687928112436"><a name="en-us_topic_0057310891_p57687928112436"></a><a name="en-us_topic_0057310891_p57687928112436"></a><strong id="en-us_topic_0057310891_b593421527191713"><a name="en-us_topic_0057310891_b593421527191713"></a><a name="en-us_topic_0057310891_b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.77%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057310891_p42210623112436"><a name="en-us_topic_0057310891_p42210623112436"></a><a name="en-us_topic_0057310891_p42210623112436"></a><strong id="en-us_topic_0057310891_b84235270619112"><a name="en-us_topic_0057310891_b84235270619112"></a><a name="en-us_topic_0057310891_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.8%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057310891_p63617265112436"><a name="en-us_topic_0057310891_p63617265112436"></a><a name="en-us_topic_0057310891_p63617265112436"></a><strong id="en-us_topic_0057310891_b842352706112423"><a name="en-us_topic_0057310891_b842352706112423"></a><a name="en-us_topic_0057310891_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057310891_row35684479112436"><td class="cellrowborder" valign="top" width="17.28%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057310891_p13313439112530"><a name="en-us_topic_0057310891_p13313439112530"></a><a name="en-us_topic_0057310891_p13313439112530"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057310891_p50150432112436"><a name="en-us_topic_0057310891_p50150432112436"></a><a name="en-us_topic_0057310891_p50150432112436"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057310891_p35653193112436"><a name="en-us_topic_0057310891_p35653193112436"></a><a name="en-us_topic_0057310891_p35653193112436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.8%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057310891_p48921437201850"><a name="en-us_topic_0057310891_p48921437201850"></a><a name="en-us_topic_0057310891_p48921437201850"></a>Tag key. The key contains 36 Unicode characters at most and cannot be blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row20048002112436"><td class="cellrowborder" valign="top" width="17.28%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057310891_p66095544112533"><a name="en-us_topic_0057310891_p66095544112533"></a><a name="en-us_topic_0057310891_p66095544112533"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057310891_p1570770112436"><a name="en-us_topic_0057310891_p1570770112436"></a><a name="en-us_topic_0057310891_p1570770112436"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057310891_p60123528112436"><a name="en-us_topic_0057310891_p60123528112436"></a><a name="en-us_topic_0057310891_p60123528112436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.8%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057310891_p61714725112922"><a name="en-us_topic_0057310891_p61714725112922"></a><a name="en-us_topic_0057310891_p61714725112922"></a>Tag value. Each value contains 43 Unicode characters at most and can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request
    -   A type

        ```
        {
            "name": "www.example.com.",
            "description": "This is an example record set.",
            "type": "A",
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
            "name": "www.example.com.",
            "description": "This is an example record set.",
            "type": "AAAA",
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
            "name": "www.example.com.",
            "description": "This is an example record set.",
            "type": "MX",
            "ttl": 3600,
            "records": [
                "1 mail.example.com"
            ]
        }
        ```

    -   CNAME type

        ```
        {
            "name": "sale.example.com.",
            "description": "This is an example record set.",
            "type": "CNAME",
            "ttl": 3600,
            "records": [
                "server1.example.com"
            ]
        }
        ```

    -   TXT type

        ```
        {
            "name": "server1.example.com.",
            "description": "This is an example record set.",
            "type": "TXT",
            "ttl": 300,
            "records": [
                "\"This host is used for sale.\""
            ]
        }
        ```

    -   NS type

        ```
        {
            "name": "server1.example.com.",
            "description": "This is an example record set.",
            "type": "NS",
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
            "name": "_sip._tcp.example.com.",
            "description": "This is an example record set.",
            "type": "SRV",
            "ttl": 300,
            "records": [
                "3 60 2176 sipserver.example.com.",
                "10 100 2176 sipserver.example.com."
            ]
        }
        ```

    -   PTR type

        ```
        {
            "name": "1.1.168.192.in-addr.arpa.",
            "description": "This is an example record set.",
            "type": "PTR",
            "ttl": 300,
            "records": [
                "webserver.example.com."
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

    **Table  4**  Parameters in the response

    <a name="table7669703175323"></a><table><thead align="left"><tr id="row52466955175323"><th class="cellrowborder" valign="top" width="27.889999999999997%" id="mcps1.2.4.1.1"><p id="p2769858175323"><a name="p2769858175323"></a><a name="p2769858175323"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.55%" id="mcps1.2.4.1.2"><p id="p46296309175323"><a name="p46296309175323"></a><a name="p46296309175323"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.56%" id="mcps1.2.4.1.3"><p id="p62697904175323"><a name="p62697904175323"></a><a name="p62697904175323"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47909891175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p64112397175323"><a name="p64112397175323"></a><a name="p64112397175323"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p1660870175323"><a name="p1660870175323"></a><a name="p1660870175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p1249204175323"><a name="p1249204175323"></a><a name="p1249204175323"></a>Record set ID</p>
    </td>
    </tr>
    <tr id="row6942422175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p64097412175323"><a name="p64097412175323"></a><a name="p64097412175323"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p44990515175323"><a name="p44990515175323"></a><a name="p44990515175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p32019574175323"><a name="p32019574175323"></a><a name="p32019574175323"></a>Record set name</p>
    </td>
    </tr>
    <tr id="row61442071175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p51194416175323"><a name="p51194416175323"></a><a name="p51194416175323"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p63301991175323"><a name="p63301991175323"></a><a name="p63301991175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p43966660175323"><a name="p43966660175323"></a><a name="p43966660175323"></a>Record set description</p>
    </td>
    </tr>
    <tr id="row2176746175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p11805366175323"><a name="p11805366175323"></a><a name="p11805366175323"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p1051908175323"><a name="p1051908175323"></a><a name="p1051908175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p10043845175323"><a name="p10043845175323"></a><a name="p10043845175323"></a>Zone ID of the record set</p>
    </td>
    </tr>
    <tr id="row61212722175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p8318586175323"><a name="p8318586175323"></a><a name="p8318586175323"></a>zone_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p31287919175323"><a name="p31287919175323"></a><a name="p31287919175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p16372315175323"><a name="p16372315175323"></a><a name="p16372315175323"></a>Zone name of the record set</p>
    </td>
    </tr>
    <tr id="row38132372175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p37461920175323"><a name="p37461920175323"></a><a name="p37461920175323"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p27536075175323"><a name="p27536075175323"></a><a name="p27536075175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p24813356175323"><a name="p24813356175323"></a><a name="p24813356175323"></a>Record set type</p>
    <p id="p173531225174112"><a name="p173531225174112"></a><a name="p173531225174112"></a>The value can be <strong id="b84235270693731_1"><a name="b84235270693731_1"></a><a name="b84235270693731_1"></a>A</strong>, <strong id="b84235270693735_1"><a name="b84235270693735_1"></a><a name="b84235270693735_1"></a>AAAA</strong>, <strong id="b84235270693738_1"><a name="b84235270693738_1"></a><a name="b84235270693738_1"></a>MX</strong>, <strong id="b84235270693741_1"><a name="b84235270693741_1"></a><a name="b84235270693741_1"></a>CNAME</strong>, <strong id="b84235270693746_1"><a name="b84235270693746_1"></a><a name="b84235270693746_1"></a>TXT</strong>, <strong id="b84235270693755_1"><a name="b84235270693755_1"></a><a name="b84235270693755_1"></a>NS</strong> (only in public zones), <strong id="b8423527069382_1"><a name="b8423527069382_1"></a><a name="b8423527069382_1"></a>SRV</strong>, <strong id="b8423527069385_1"><a name="b8423527069385_1"></a><a name="b8423527069385_1"></a>PTR</strong> (only in private zones), and <strong id="b84235270693810_1"><a name="b84235270693810_1"></a><a name="b84235270693810_1"></a>CAA</strong> (only in public zones).</p>
    </td>
    </tr>
    <tr id="row20796819175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p4811553175323"><a name="p4811553175323"></a><a name="p4811553175323"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p47559731175323"><a name="p47559731175323"></a><a name="p47559731175323"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p35349847185925"><a name="p35349847185925"></a><a name="p35349847185925"></a>Caching period of a domain name (in seconds)</p>
    <p id="p2275826812726"><a name="p2275826812726"></a><a name="p2275826812726"></a>A longer caching period makes a change on the authoritative DNS server take longer time to be synchronized to other DNS servers.</p>
    </td>
    </tr>
    <tr id="row13978060175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p43388342175323"><a name="p43388342175323"></a><a name="p43388342175323"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p29596719175323"><a name="p29596719175323"></a><a name="p29596719175323"></a>List&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p30492925175323"><a name="p30492925175323"></a><a name="p30492925175323"></a>Domain name resolution result</p>
    </td>
    </tr>
    <tr id="row23148559175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p36524189175323"><a name="p36524189175323"></a><a name="p36524189175323"></a>create_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p47080972175323"><a name="p47080972175323"></a><a name="p47080972175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p15737135175323"><a name="p15737135175323"></a><a name="p15737135175323"></a>Time when the record set was created</p>
    </td>
    </tr>
    <tr id="row33465792175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p42570937175323"><a name="p42570937175323"></a><a name="p42570937175323"></a>update_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p27449776175323"><a name="p27449776175323"></a><a name="p27449776175323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p63703533175323"><a name="p63703533175323"></a><a name="p63703533175323"></a>Time when the record set was updated</p>
    </td>
    </tr>
    <tr id="row17850883175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p36228271175323"><a name="p36228271175323"></a><a name="p36228271175323"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p6480061175323"><a name="p6480061175323"></a><a name="p6480061175323"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p28721670185925"><a name="p28721670185925"></a><a name="p28721670185925"></a>Resource status, which can be <strong id="b842352706121016"><a name="b842352706121016"></a><a name="b842352706121016"></a>PENDING_CREATE</strong>, <strong id="b842352706121023"><a name="b842352706121023"></a><a name="b842352706121023"></a>ACTIVE</strong>, <strong id="b842352706112413"><a name="b842352706112413"></a><a name="b842352706112413"></a>PENDING_DELETE</strong>, <strong id="b842352706104310"><a name="b842352706104310"></a><a name="b842352706104310"></a>PENDING_UPDATE</strong>, or <strong id="b84235270691843"><a name="b84235270691843"></a><a name="b84235270691843"></a>ERROR</strong></p>
    </td>
    </tr>
    <tr id="row61184424175323"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p49633411175323"><a name="p49633411175323"></a><a name="p49633411175323"></a>default</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p56048766175323"><a name="p56048766175323"></a><a name="p56048766175323"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p52627220185925"><a name="p52627220185925"></a><a name="p52627220185925"></a>Whether the record set is created by default</p>
    <p id="p46587348115949"><a name="p46587348115949"></a><a name="p46587348115949"></a>A default record set cannot be deleted or modified.</p>
    </td>
    </tr>
    <tr id="row15199048201026"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p23163408201026"><a name="p23163408201026"></a><a name="p23163408201026"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p40653752201026"><a name="p40653752201026"></a><a name="p40653752201026"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p4619625201026"><a name="p4619625201026"></a><a name="p4619625201026"></a>Project ID of the record set</p>
    </td>
    </tr>
    <tr id="row3965248419366"><td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.1 "><p id="p2132803819366"><a name="p2132803819366"></a><a name="p2132803819366"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.2.4.1.2 "><p id="p1127763319366"><a name="p1127763319366"></a><a name="p1127763319366"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.56%" headers="mcps1.2.4.1.3 "><p id="p1368584110253"><a name="p1368584110253"></a><a name="p1368584110253"></a>Link of the current resource or other related resources</p>
    <p id="p4371306185925"><a name="p4371306185925"></a><a name="p4371306185925"></a>When a response is broken into pages, a <strong id="b38947790110750"><a name="b38947790110750"></a><a name="b38947790110750"></a>next</strong> link is provided to retrieve all results.</p>
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
            "192.168.10.1",
            "192.168.10.2"
        ],
        "status": "PENDING_CREATE",
        "links": {
            "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149/recordsets/2c9eb155587228570158722b6ac30007"
        },
        "zone_id": "2c9eb155587194ec01587224c9f90149",
        "zone_name": "example.com.",
        "create_at": "2016-11-17T12:03:17.827",
        "update_at": null,
        "default": false,
        "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c"
    }
    
    ```


## Returned Value<a name="section42637797161043"></a>

See  [General Request Return Code](general-request-return-code.md).
