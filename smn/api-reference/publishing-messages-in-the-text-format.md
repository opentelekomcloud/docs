# Publishing Messages in the Text Format<a name="smn_api_54001"></a>

## Description<a name="section34083598194741"></a>

-   API name

    Publish


-   Function

    Publish messages in the text format to a topic. After the message ID is returned, the message has been saved and is to be pushed to the subscribers of the topic.


## URI<a name="section16663308194741"></a>

-   URI format

    POST /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}/publish


-   Parameter description

    <a name="table59928756194741"></a>
    <table><thead align="left"><tr id="row4278206194741"><th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.1"><p id="p10990404194741"><a name="p10990404194741"></a><a name="p10990404194741"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.04809519048095%" id="mcps1.1.5.1.2"><p id="p17807502194741"><a name="p17807502194741"></a><a name="p17807502194741"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.1.5.1.3"><p id="p33121540194741"><a name="p33121540194741"></a><a name="p33121540194741"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.42535746425357%" id="mcps1.1.5.1.4"><p id="p65599120194741"><a name="p65599120194741"></a><a name="p65599120194741"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26682115194741"><td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.1 "><p id="p13767740194741"><a name="p13767740194741"></a><a name="p13767740194741"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.2 "><p id="p41445161194741"><a name="p41445161194741"></a><a name="p41445161194741"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="p1614899194741"><a name="p1614899194741"></a><a name="p1614899194741"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="p55689039155337"><a name="p55689039155337"></a><a name="p55689039155337"></a>Project ID</p>
    <p id="p63697985194741"><a name="p63697985194741"></a><a name="p63697985194741"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row63606429194741"><td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.1 "><p id="p51847142194741"><a name="p51847142194741"></a><a name="p51847142194741"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.2 "><p id="p38868943194741"><a name="p38868943194741"></a><a name="p38868943194741"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="p61376640194741"><a name="p61376640194741"></a><a name="p61376640194741"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.42535746425357%" headers="mcps1.1.5.1.4 "><p id="p5451938194741"><a name="p5451938194741"></a><a name="p5451938194741"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1142871194741"></a>

-   Parameter description

    <a name="table49296942194741"></a>
    <table><thead align="left"><tr id="row13744451194741"><th class="cellrowborder" valign="top" width="17.52%" id="mcps1.1.5.1.1"><p id="p39558753194741"><a name="p39558753194741"></a><a name="p39558753194741"></a><strong id="b57274411"><a name="b57274411"></a><a name="b57274411"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.48%" id="mcps1.1.5.1.2"><p id="p50142464194741"><a name="p50142464194741"></a><a name="p50142464194741"></a><strong id="b287768269352"><a name="b287768269352"></a><a name="b287768269352"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.21%" id="mcps1.1.5.1.3"><p id="p35007816194741"><a name="p35007816194741"></a><a name="p35007816194741"></a><strong id="b453632946"><a name="b453632946"></a><a name="b453632946"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.79%" id="mcps1.1.5.1.4"><p id="p17060832194741"><a name="p17060832194741"></a><a name="p17060832194741"></a><strong id="b1841617943"><a name="b1841617943"></a><a name="b1841617943"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65643809194741"><td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.1 "><p id="p15548314194741"><a name="p15548314194741"></a><a name="p15548314194741"></a>subject</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.48%" headers="mcps1.1.5.1.2 "><p id="p51453956194741"><a name="p51453956194741"></a><a name="p51453956194741"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.21%" headers="mcps1.1.5.1.3 "><p id="p7020935194741"><a name="p7020935194741"></a><a name="p7020935194741"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.79%" headers="mcps1.1.5.1.4 "><p id="p31824842194741"><a name="p31824842194741"></a><a name="p31824842194741"></a>Message subject, which is used as the email subject when you publish email messages. The value cannot exceed 512 characters.</p>
    </td>
    </tr>
    <tr id="row47751841194741"><td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.1 "><p id="p42693949194741"><a name="p42693949194741"></a><a name="p42693949194741"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.48%" headers="mcps1.1.5.1.2 "><p id="p35657812194741"><a name="p35657812194741"></a><a name="p35657812194741"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.21%" headers="mcps1.1.5.1.3 "><p id="p2601680194741"><a name="p2601680194741"></a><a name="p2601680194741"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.79%" headers="mcps1.1.5.1.4 "><p id="p9409561194741"><a name="p9409561194741"></a><a name="p9409561194741"></a>Message content</p>
    <p id="p23976982194741"><a name="p23976982194741"></a><a name="p23976982194741"></a>The message content is a UTF-8-coded character string of no more than 256 KB. For SMS subscribers, if the content exceeds 256 bytes, the system will divide it into multiple messages and send only the first two.</p>
    <a name="ul956721115202"></a><a name="ul956721115202"></a>
    </td>
    </tr>
    <tr id="row103682214520"><td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.1 "><p id="p23681125515"><a name="p23681125515"></a><a name="p23681125515"></a>time_to_live</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.48%" headers="mcps1.1.5.1.2 "><p id="p23681626518"><a name="p23681626518"></a><a name="p23681626518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.21%" headers="mcps1.1.5.1.3 "><p id="p18075392520"><a name="p18075392520"></a><a name="p18075392520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.79%" headers="mcps1.1.5.1.4 "><p id="p66191571978"><a name="p66191571978"></a><a name="p66191571978"></a>Time-to-live (TTL) of a message, specifically, the maximum time period for retaining the message in the system</p>
    <p id="p73858218511"><a name="p73858218511"></a><a name="p73858218511"></a>If the period expires, the system will discard the message. The time period is measured in seconds, and the default TTL is <strong id="b84235270617311"><a name="b84235270617311"></a><a name="b84235270617311"></a>3600s</strong> (one hour).</p>
    <p id="p163851021156"><a name="p163851021156"></a><a name="p163851021156"></a>The value must be a positive integer less than or equal to 604,800 (3600 x 24 x 7).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/urn:smn:regionId: f96188c7ccaf4ffba0c9aa149ab2bd57:test_create_topic_v2/publish
    ```

    ```
    {
        "subject": "test message v2",
        "message": "Message test message v2",
        "time_to_live":"3600"
    }
    ```


## Response<a name="section43693179194741"></a>

-   Parameter description

    <a name="table48990005194741"></a>
    <table><thead align="left"><tr id="row32165281194741"><th class="cellrowborder" valign="top" width="30.006999300069992%" id="mcps1.1.4.1.1"><p id="p55250992194741"><a name="p55250992194741"></a><a name="p55250992194741"></a><strong id="b142806169"><a name="b142806169"></a><a name="b142806169"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.807319268073194%" id="mcps1.1.4.1.2"><p id="p46145363194741"><a name="p46145363194741"></a><a name="p46145363194741"></a><strong id="b913296798"><a name="b913296798"></a><a name="b913296798"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.185681431856814%" id="mcps1.1.4.1.3"><p id="p46786931194741"><a name="p46786931194741"></a><a name="p46786931194741"></a><strong id="b1375747178"><a name="b1375747178"></a><a name="b1375747178"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13112008194741"><td class="cellrowborder" valign="top" width="30.006999300069992%" headers="mcps1.1.4.1.1 "><p id="p55439693194741"><a name="p55439693194741"></a><a name="p55439693194741"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.807319268073194%" headers="mcps1.1.4.1.2 "><p id="p61430126194741"><a name="p61430126194741"></a><a name="p61430126194741"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.185681431856814%" headers="mcps1.1.4.1.3 "><p id="p9784341194741"><a name="p9784341194741"></a><a name="p9784341194741"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row19245029194741"><td class="cellrowborder" valign="top" width="30.006999300069992%" headers="mcps1.1.4.1.1 "><p id="p15343493194741"><a name="p15343493194741"></a><a name="p15343493194741"></a>message_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.807319268073194%" headers="mcps1.1.4.1.2 "><p id="p34863430194741"><a name="p34863430194741"></a><a name="p34863430194741"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.185681431856814%" headers="mcps1.1.4.1.3 "><p id="p5365583194741"><a name="p5365583194741"></a><a name="p5365583194741"></a>Message ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "message_id": "bf94b63a5dfb475994d3ac34664e24f2",
        "request_id": "9974c07f6d554a6d827956acbeb4be5f"
    }
    ```


## Returned Value<a name="section56116278194741"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

