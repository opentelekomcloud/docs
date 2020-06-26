# Querying Topic Details<a name="smn_api_51005"></a>

## Description<a name="section64935954"></a>

-   API name

    QueryTopicDetail


-   Function

    Query the detailed information about a topic.


## URI<a name="section47552675"></a>

-   URI format

    GET /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}


-   Parameter description

    <a name="table60453091"></a>
    <table><thead align="left"><tr id="row31471768"><th class="cellrowborder" valign="top" width="23.82238223822382%" id="mcps1.1.5.1.1"><p id="p66185246"><a name="p66185246"></a><a name="p66185246"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.942194219421943%" id="mcps1.1.5.1.2"><p id="p59404709"><a name="p59404709"></a><a name="p59404709"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.012101210121013%" id="mcps1.1.5.1.3"><p id="p47052116"><a name="p47052116"></a><a name="p47052116"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.223322332233224%" id="mcps1.1.5.1.4"><p id="p53125076"><a name="p53125076"></a><a name="p53125076"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57297510"><td class="cellrowborder" valign="top" width="23.82238223822382%" headers="mcps1.1.5.1.1 "><p id="p10586695"><a name="p10586695"></a><a name="p10586695"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.942194219421943%" headers="mcps1.1.5.1.2 "><p id="p52215961"><a name="p52215961"></a><a name="p52215961"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.012101210121013%" headers="mcps1.1.5.1.3 "><p id="p1634435"><a name="p1634435"></a><a name="p1634435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.223322332233224%" headers="mcps1.1.5.1.4 "><p id="p61977638154952"><a name="p61977638154952"></a><a name="p61977638154952"></a>Project ID</p>
    <p id="p65280430"><a name="p65280430"></a><a name="p65280430"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row9249362"><td class="cellrowborder" valign="top" width="23.82238223822382%" headers="mcps1.1.5.1.1 "><p id="p11000853"><a name="p11000853"></a><a name="p11000853"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.942194219421943%" headers="mcps1.1.5.1.2 "><p id="p18653909"><a name="p18653909"></a><a name="p18653909"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.012101210121013%" headers="mcps1.1.5.1.3 "><p id="p34571641"><a name="p34571641"></a><a name="p34571641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.223322332233224%" headers="mcps1.1.5.1.4 "><p id="p48839530"><a name="p48839530"></a><a name="p48839530"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section25320898"></a>

Request example

```
GET https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/urn:smn:regionId:8bad8a40e0f7462f8c1676e3f93a8183:test_create_topic_v2
```

## Response<a name="section26561495"></a>

-   Parameter description

    <a name="table38552084"></a>
    <table><thead align="left"><tr id="row10058158"><th class="cellrowborder" valign="top" width="25.81%" id="mcps1.1.4.1.1"><p id="p9404449"><a name="p9404449"></a><a name="p9404449"></a><strong id="b1009826988"><a name="b1009826988"></a><a name="b1009826988"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.07%" id="mcps1.1.4.1.2"><p id="p23562876"><a name="p23562876"></a><a name="p23562876"></a><strong id="b1080124458"><a name="b1080124458"></a><a name="b1080124458"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.12%" id="mcps1.1.4.1.3"><p id="p29544808"><a name="p29544808"></a><a name="p29544808"></a><strong id="b1535763238"><a name="b1535763238"></a><a name="b1535763238"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33089041"><td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.1.4.1.1 "><p id="p62966687"><a name="p62966687"></a><a name="p62966687"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.07%" headers="mcps1.1.4.1.2 "><p id="p27997"><a name="p27997"></a><a name="p27997"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.12%" headers="mcps1.1.4.1.3 "><p id="p2267763"><a name="p2267763"></a><a name="p2267763"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row42586845"><td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.1.4.1.1 "><p id="p26982424"><a name="p26982424"></a><a name="p26982424"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.07%" headers="mcps1.1.4.1.2 "><p id="p38092711"><a name="p38092711"></a><a name="p38092711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.12%" headers="mcps1.1.4.1.3 "><p id="p65610739"><a name="p65610739"></a><a name="p65610739"></a>Name of the topic</p>
    </td>
    </tr>
    <tr id="row48717564"><td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.1.4.1.1 "><p id="p53808606"><a name="p53808606"></a><a name="p53808606"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.07%" headers="mcps1.1.4.1.2 "><p id="p63529816"><a name="p63529816"></a><a name="p63529816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.12%" headers="mcps1.1.4.1.3 "><p id="p45641491"><a name="p45641491"></a><a name="p45641491"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    <tr id="row53759727"><td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.1.4.1.1 "><p id="p59570626"><a name="p59570626"></a><a name="p59570626"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.07%" headers="mcps1.1.4.1.2 "><p id="p60491410"><a name="p60491410"></a><a name="p60491410"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.12%" headers="mcps1.1.4.1.3 "><p id="p57656838184157"><a name="p57656838184157"></a><a name="p57656838184157"></a>Topic display name, which is presented as the name of the email sender in email messages</p>
    </td>
    </tr>
    <tr id="row20888703"><td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.1.4.1.1 "><p id="p14263389"><a name="p14263389"></a><a name="p14263389"></a>push_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.07%" headers="mcps1.1.4.1.2 "><p id="p14483900"><a name="p14483900"></a><a name="p14483900"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.12%" headers="mcps1.1.4.1.3 "><p id="p32345284"><a name="p32345284"></a><a name="p32345284"></a>Message pushing policy</p>
    <p id="p10916523273"><a name="p10916523273"></a><a name="p10916523273"></a><strong id="b842352706928"><a name="b842352706928"></a><a name="b842352706928"></a>0</strong> indicates that the message sending fails and the message is cached in the queue. <strong id="b8423527069213"><a name="b8423527069213"></a><a name="b8423527069213"></a>1</strong> indicates that the failed message is discarded.</p>
    </td>
    </tr>
    <tr id="row24500989"><td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.1.4.1.1 "><p id="p38423121"><a name="p38423121"></a><a name="p38423121"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.07%" headers="mcps1.1.4.1.2 "><p id="p25265097"><a name="p25265097"></a><a name="p25265097"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.12%" headers="mcps1.1.4.1.3 "><p id="p33206990"><a name="p33206990"></a><a name="p33206990"></a>Time when the topic was created</p>
    <p id="p12947570279"><a name="p12947570279"></a><a name="p12947570279"></a>The UTC time is in <em id="i3709181953211"><a name="i3709181953211"></a><a name="i3709181953211"></a>YYYY-MM-DDTHH:MM:SSZ</em> format.</p>
    </td>
    </tr>
    <tr id="row48704899"><td class="cellrowborder" valign="top" width="25.81%" headers="mcps1.1.4.1.1 "><p id="p52782726"><a name="p52782726"></a><a name="p52782726"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.07%" headers="mcps1.1.4.1.2 "><p id="p47542385"><a name="p47542385"></a><a name="p47542385"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.12%" headers="mcps1.1.4.1.3 "><p id="p25727981"><a name="p25727981"></a><a name="p25727981"></a>Time when the topic was updated</p>
    <p id="p15544215281"><a name="p15544215281"></a><a name="p15544215281"></a>The UTC time is in <em id="i4623338325"><a name="i4623338325"></a><a name="i4623338325"></a>YYYY-MM-DDTHH:MM:SSZ</em> format.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "update_time":"2016-08-01T02:16:38Z",
        "push_policy":0,
        "create_time":"2016-08-01T02:16:38Z",
        "name":"test_create_topic_v2",
        "topic_urn":"urn:smn:regionId:8bad8a40e0f7462f8c1676e3f93a8183:test_create_topic_v2",
        "display_name":"test create topic v2",
        "request_id":"6837531fd3f54550927b930180a706bf"
    }
    ```


## Returned Value<a name="section37726867"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

