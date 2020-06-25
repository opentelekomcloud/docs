# Querying Alarm Configuration<a name="antiddos_02_0029"></a>

## Functions<a name="section55096476"></a>

This API allows you to query alarm configuration, such as whether a certain type of alarms will be received, and whether alarms are received through SMS messages or emails.

## URI<a name="section26106237"></a>

-   URI format

    GET /v2/\{project\_id\}/warnalert/alertconfig/query

-   Parameter description

    <a name="table51410791"></a>
    <table><thead align="left"><tr id="row16041741"><th class="cellrowborder" valign="top" width="24.347565243475646%" id="mcps1.1.5.1.1"><p id="p24312641"><a name="p24312641"></a><a name="p24312641"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.10758924107589%" id="mcps1.1.5.1.2"><p id="p23166934"><a name="p23166934"></a><a name="p23166934"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.617938206179375%" id="mcps1.1.5.1.3"><p id="p64582388"><a name="p64582388"></a><a name="p64582388"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.92690730926907%" id="mcps1.1.5.1.4"><p id="p63790914"><a name="p63790914"></a><a name="p63790914"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66790376"><td class="cellrowborder" valign="top" width="24.347565243475646%" headers="mcps1.1.5.1.1 "><p id="p41311375"><a name="p41311375"></a><a name="p41311375"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.10758924107589%" headers="mcps1.1.5.1.2 "><p id="p57887070"><a name="p57887070"></a><a name="p57887070"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.617938206179375%" headers="mcps1.1.5.1.3 "><p id="p58341118"><a name="p58341118"></a><a name="p58341118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.4 "><p id="p28010135"><a name="p28010135"></a><a name="p28010135"></a>A user's ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section33629549"></a>

-   Request example

    ```
    GET /v2/67641fe6886f43fcb78edbbf0ad0b99f/warnalert/alertconfig/query
    ```


## Response<a name="section34230492"></a>

-   Element description

    <a name="table48692557"></a>
    <table><thead align="left"><tr id="row57013647"><th class="cellrowborder" valign="top" width="23.090000000000003%" id="mcps1.1.5.1.1"><p id="p54702703"><a name="p54702703"></a><a name="p54702703"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.85%" id="mcps1.1.5.1.2"><p id="p1733939"><a name="p1733939"></a><a name="p1733939"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.530000000000005%" id="mcps1.1.5.1.3"><p id="p6231364"><a name="p6231364"></a><a name="p6231364"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.530000000000005%" id="mcps1.1.5.1.4"><p id="p34978441"><a name="p34978441"></a><a name="p34978441"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14681450"><td class="cellrowborder" valign="top" width="23.090000000000003%" headers="mcps1.1.5.1.1 "><p id="p48346833"><a name="p48346833"></a><a name="p48346833"></a>warn_config</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.85%" headers="mcps1.1.5.1.2 "><p id="p23779363"><a name="p23779363"></a><a name="p23779363"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.1.5.1.3 "><p id="p47080266"><a name="p47080266"></a><a name="p47080266"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.1.5.1.4 "><p id="p28885026"><a name="p28885026"></a><a name="p28885026"></a>Alarm configuration</p>
    </td>
    </tr>
    <tr id="row58638646"><td class="cellrowborder" valign="top" width="23.090000000000003%" headers="mcps1.1.5.1.1 "><p id="p52109899"><a name="p52109899"></a><a name="p52109899"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.85%" headers="mcps1.1.5.1.2 "><p id="p60152276"><a name="p60152276"></a><a name="p60152276"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.1.5.1.3 "><p id="p40496186"><a name="p40496186"></a><a name="p40496186"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.1.5.1.4 "><p id="p58965604"><a name="p58965604"></a><a name="p58965604"></a>ID of an alarm group</p>
    </td>
    </tr>
    <tr id="row60928390"><td class="cellrowborder" valign="top" width="23.090000000000003%" headers="mcps1.1.5.1.1 "><p id="p36252562"><a name="p36252562"></a><a name="p36252562"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.85%" headers="mcps1.1.5.1.2 "><p id="p50776406"><a name="p50776406"></a><a name="p50776406"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.1.5.1.3 "><p id="p19248251"><a name="p19248251"></a><a name="p19248251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.530000000000005%" headers="mcps1.1.5.1.4 "><p id="p15604521"><a name="p15604521"></a><a name="p15604521"></a>Description of an alarm group</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Data structure description of  **warn\_config**

    <a name="table56006663"></a>
    <table><thead align="left"><tr id="row16420978"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.1.5.1.1"><p id="p55030817"><a name="p55030817"></a><a name="p55030817"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.958004199580042%" id="mcps1.1.5.1.2"><p id="p28311181"><a name="p28311181"></a><a name="p28311181"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.66853314668533%" id="mcps1.1.5.1.3"><p id="p11504285"><a name="p11504285"></a><a name="p11504285"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.94560543945605%" id="mcps1.1.5.1.4"><p id="p59431865"><a name="p59431865"></a><a name="p59431865"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49251786"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.1 "><p id="p29971768"><a name="p29971768"></a><a name="p29971768"></a>antiDDoS</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.2 "><p id="p11794154"><a name="p11794154"></a><a name="p11794154"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.66853314668533%" headers="mcps1.1.5.1.3 "><p id="p15802441"><a name="p15802441"></a><a name="p15802441"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94560543945605%" headers="mcps1.1.5.1.4 "><p id="p4929340"><a name="p4929340"></a><a name="p4929340"></a>DDoS attacks</p>
    </td>
    </tr>
    <tr id="row44364065"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.1 "><p id="p36719502"><a name="p36719502"></a><a name="p36719502"></a>bruce_force</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.2 "><p id="p21489667"><a name="p21489667"></a><a name="p21489667"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.66853314668533%" headers="mcps1.1.5.1.3 "><p id="p62941481"><a name="p62941481"></a><a name="p62941481"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94560543945605%" headers="mcps1.1.5.1.4 "><p id="p65095207"><a name="p65095207"></a><a name="p65095207"></a>Brute force cracking (system logins, FTP, and DB)</p>
    </td>
    </tr>
    <tr id="row48985959"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.1 "><p id="p8439774"><a name="p8439774"></a><a name="p8439774"></a>remote_login</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.2 "><p id="p12533056"><a name="p12533056"></a><a name="p12533056"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.66853314668533%" headers="mcps1.1.5.1.3 "><p id="p8544631"><a name="p8544631"></a><a name="p8544631"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94560543945605%" headers="mcps1.1.5.1.4 "><p id="p21026539"><a name="p21026539"></a><a name="p21026539"></a>Alarms about remote logins</p>
    </td>
    </tr>
    <tr id="row55021127"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.1 "><p id="p27526304"><a name="p27526304"></a><a name="p27526304"></a>weak_password</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.2 "><p id="p15038186"><a name="p15038186"></a><a name="p15038186"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.66853314668533%" headers="mcps1.1.5.1.3 "><p id="p10133581"><a name="p10133581"></a><a name="p10133581"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94560543945605%" headers="mcps1.1.5.1.4 "><p id="p15513712"><a name="p15513712"></a><a name="p15513712"></a>Weak passwords (system and database)</p>
    </td>
    </tr>
    <tr id="row5405681"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.1 "><p id="p35206999"><a name="p35206999"></a><a name="p35206999"></a>high_privilege</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.2 "><p id="p33194707"><a name="p33194707"></a><a name="p33194707"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.66853314668533%" headers="mcps1.1.5.1.3 "><p id="p4416714"><a name="p4416714"></a><a name="p4416714"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94560543945605%" headers="mcps1.1.5.1.4 "><p id="p22209574"><a name="p22209574"></a><a name="p22209574"></a>Overly high rights of a database process</p>
    </td>
    </tr>
    <tr id="row65668446"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.1 "><p id="p17543884"><a name="p17543884"></a><a name="p17543884"></a>back_doors</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.2 "><p id="p11768466"><a name="p11768466"></a><a name="p11768466"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.66853314668533%" headers="mcps1.1.5.1.3 "><p id="p13721689"><a name="p13721689"></a><a name="p13721689"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94560543945605%" headers="mcps1.1.5.1.4 "><p id="p37715016"><a name="p37715016"></a><a name="p37715016"></a>Webshells</p>
    </td>
    </tr>
    <tr id="row3890831"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.1 "><p id="p46721870"><a name="p46721870"></a><a name="p46721870"></a>waf</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.2 "><p id="p26375114"><a name="p26375114"></a><a name="p26375114"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.66853314668533%" headers="mcps1.1.5.1.3 "><p id="p56009450"><a name="p56009450"></a><a name="p56009450"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94560543945605%" headers="mcps1.1.5.1.4 "><p id="p40471574"><a name="p40471574"></a><a name="p40471574"></a>Reserved</p>
    </td>
    </tr>
    <tr id="row49427073194532"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.1 "><p id="p63319096194541"><a name="p63319096194541"></a><a name="p63319096194541"></a>send_frequency</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.2 "><p id="p28573150194541"><a name="p28573150194541"></a><a name="p28573150194541"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.66853314668533%" headers="mcps1.1.5.1.3 "><p id="p1789380615303"><a name="p1789380615303"></a><a name="p1789380615303"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.94560543945605%" headers="mcps1.1.5.1.4 "><p id="p33380830194541"><a name="p33380830194541"></a><a name="p33380830194541"></a>Possible values:</p>
    <a name="ul31992022194541"></a><a name="ul31992022194541"></a><ul id="ul31992022194541"><li><span class="parmvalue" id="parmvalue555125744153957_3"><a name="parmvalue555125744153957_3"></a><a name="parmvalue555125744153957_3"></a><b>0</b></span>: indicates that alarms are sent once a day.</li><li><span class="parmvalue" id="parmvalue42786548315404_3"><a name="parmvalue42786548315404_3"></a><a name="parmvalue42786548315404_3"></a><b>1</b></span>: indicates that alarms are sent once every half hour.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
       "warn_config":    {
          "antiDDoS": true,
          "bruce_force": false,
          "remote_login": false,
          "weak_password": false,
          "high_privilege": false,
          "back_doors": false,
          "waf": false
       },
       "topic_urn": "urn:smn:eu-de:67641fe6886f43fcb78edbbf0ad0b99f:test_soft",
       "display_name": "group_1"
    }
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >SFTP is more secure than FTP. To secure data transmission, use SFTP to transfer files.  


## Returned Value<a name="section39638980"></a>

See  [Status Code](status-code.md).

