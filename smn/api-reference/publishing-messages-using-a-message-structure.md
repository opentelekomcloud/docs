# Publishing Messages Using a Message Structure<a name="smn_api_54002"></a>

## Description<a name="section2529770119494"></a>

-   API name

    Publish


-   Function

    Use the message structure to publish a message to the topic. After the message ID is returned, the message has been saved and is to be pushed to the subscribers of the topic. This API allows you to send different message content to different types of subscribers.


## URI<a name="section5419540819494"></a>

-   URI format

    POST /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}/publish


-   Parameter description

    <a name="table5857211319494"></a>
    <table><thead align="left"><tr id="row2704976919494"><th class="cellrowborder" valign="top" width="20.48%" id="mcps1.1.5.1.1"><p id="p4354764619494"><a name="p4354764619494"></a><a name="p4354764619494"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.28%" id="mcps1.1.5.1.2"><p id="p3769841519494"><a name="p3769841519494"></a><a name="p3769841519494"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.69%" id="mcps1.1.5.1.3"><p id="p3367280619494"><a name="p3367280619494"></a><a name="p3367280619494"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.550000000000004%" id="mcps1.1.5.1.4"><p id="p4314272819494"><a name="p4314272819494"></a><a name="p4314272819494"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6136344319494"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.5.1.1 "><p id="p438298719494"><a name="p438298719494"></a><a name="p438298719494"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.28%" headers="mcps1.1.5.1.2 "><p id="p1947768019494"><a name="p1947768019494"></a><a name="p1947768019494"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.5.1.3 "><p id="p3418823319494"><a name="p3418823319494"></a><a name="p3418823319494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.5.1.4 "><p id="p26342752155347"><a name="p26342752155347"></a><a name="p26342752155347"></a>Project ID</p>
    <p id="p1778348719494"><a name="p1778348719494"></a><a name="p1778348719494"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row1215136319494"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.1.5.1.1 "><p id="p4473635119494"><a name="p4473635119494"></a><a name="p4473635119494"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.28%" headers="mcps1.1.5.1.2 "><p id="p6687467519494"><a name="p6687467519494"></a><a name="p6687467519494"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.69%" headers="mcps1.1.5.1.3 "><p id="p4813962419494"><a name="p4813962419494"></a><a name="p4813962419494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.5.1.4 "><p id="p699549419494"><a name="p699549419494"></a><a name="p699549419494"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section6208316219494"></a>

-   Parameter description

    <a name="table4393345619494"></a>
    <table><thead align="left"><tr id="row5198822719494"><th class="cellrowborder" valign="top" width="19.18808119188081%" id="mcps1.1.5.1.1"><p id="p5029685319494"><a name="p5029685319494"></a><a name="p5029685319494"></a><strong id="b937669179"><a name="b937669179"></a><a name="b937669179"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.64813518648135%" id="mcps1.1.5.1.2"><p id="p4751327919494"><a name="p4751327919494"></a><a name="p4751327919494"></a><strong id="b6259598993519"><a name="b6259598993519"></a><a name="b6259598993519"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.40785921407859%" id="mcps1.1.5.1.3"><p id="p2337041019494"><a name="p2337041019494"></a><a name="p2337041019494"></a><strong id="b511149455"><a name="b511149455"></a><a name="b511149455"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.75592440755925%" id="mcps1.1.5.1.4"><p id="p1395507019494"><a name="p1395507019494"></a><a name="p1395507019494"></a><strong id="b1076734232"><a name="b1076734232"></a><a name="b1076734232"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2272409419494"><td class="cellrowborder" valign="top" width="19.18808119188081%" headers="mcps1.1.5.1.1 "><p id="p2871231519494"><a name="p2871231519494"></a><a name="p2871231519494"></a>subject</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.64813518648135%" headers="mcps1.1.5.1.2 "><p id="p4399616019494"><a name="p4399616019494"></a><a name="p4399616019494"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.40785921407859%" headers="mcps1.1.5.1.3 "><p id="p691922219494"><a name="p691922219494"></a><a name="p691922219494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.75592440755925%" headers="mcps1.1.5.1.4 "><p id="p2358611619494"><a name="p2358611619494"></a><a name="p2358611619494"></a>Message subject, which is presented as the email subject when SMN sends massages to email subscribers</p>
    <p id="p950615309415"><a name="p950615309415"></a><a name="p950615309415"></a>The message subject cannot exceed 512 bytes.</p>
    </td>
    </tr>
    <tr id="row1441009919494"><td class="cellrowborder" valign="top" width="19.18808119188081%" headers="mcps1.1.5.1.1 "><p id="p2636733319494"><a name="p2636733319494"></a><a name="p2636733319494"></a>message_structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.64813518648135%" headers="mcps1.1.5.1.2 "><p id="p5537924419494"><a name="p5537924419494"></a><a name="p5537924419494"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.40785921407859%" headers="mcps1.1.5.1.3 "><p id="p5653380819494"><a name="p5653380819494"></a><a name="p5653380819494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.75592440755925%" headers="mcps1.1.5.1.4 "><p id="p1956614103219"><a name="p1956614103219"></a><a name="p1956614103219"></a>Message structure, which contains JSON character strings. Specify protocols in the structure, which can be <strong id="b84235270693845"><a name="b84235270693845"></a><a name="b84235270693845"></a>http</strong>, <strong id="b137855045115"><a name="b137855045115"></a><a name="b137855045115"></a>https</strong>, <strong id="b84235270692756"><a name="b84235270692756"></a><a name="b84235270692756"></a>email</strong>, <strong id="b84235270692858"><a name="b84235270692858"></a><a name="b84235270692858"></a>dms</strong>, and <strong id="b179071953195310"><a name="b179071953195310"></a><a name="b179071953195310"></a>sms</strong>. </p>
    <p id="p1583573619494"><a name="p1583573619494"></a><a name="p1583573619494"></a>The <strong id="b84235270693914"><a name="b84235270693914"></a><a name="b84235270693914"></a>default</strong> protocol is mandatory. If the system fails to match any other protocols, the default message is sent.</p>
    <div class="note" id="note1920913487410"><a name="note1920913487410"></a><a name="note1920913487410"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p2142739193425"><a name="p2142739193425"></a><a name="p2142739193425"></a>Three message formats are supported:</p>
    <a name="ul39581890193437"></a><a name="ul39581890193437"></a><ul id="ul39581890193437"><li>message</li><li>message_structure</li><li>message_template_name</li></ul>
    <p id="p38575679193513"><a name="p38575679193513"></a><a name="p38575679193513"></a>If the three formats are specified at the same time, they take effect in the following sequence: <strong id="b842352706142832"><a name="b842352706142832"></a><a name="b842352706142832"></a>message_structure</strong> &gt; <strong id="b842352706142838"><a name="b842352706142838"></a><a name="b842352706142838"></a>message_template_name</strong> &gt; <strong id="b842352706142846"><a name="b842352706142846"></a><a name="b842352706142846"></a>message</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row6307720141310"><td class="cellrowborder" valign="top" width="19.18808119188081%" headers="mcps1.1.5.1.1 "><p id="p23681125515"><a name="p23681125515"></a><a name="p23681125515"></a>time_to_live</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.64813518648135%" headers="mcps1.1.5.1.2 "><p id="p23681626518"><a name="p23681626518"></a><a name="p23681626518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.40785921407859%" headers="mcps1.1.5.1.3 "><p id="p18075392520"><a name="p18075392520"></a><a name="p18075392520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.75592440755925%" headers="mcps1.1.5.1.4 "><p id="p66191571978"><a name="p66191571978"></a><a name="p66191571978"></a>TTL of a message, specifically, the maximum time period for retaining the message in the system</p>
    <p id="p73858218511"><a name="p73858218511"></a><a name="p73858218511"></a>If the period expires, the system will discard the message. The time period is measured in seconds, and the default TTL is <strong id="b84235270617311"><a name="b84235270617311"></a><a name="b84235270617311"></a>3600s</strong> (one hour).</p>
    <p id="p185211212174217"><a name="p185211212174217"></a><a name="p185211212174217"></a>The value must be a positive integer less than or equal to 604,800 (3600 x 24 x 7).</p>
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
        "time_to_live":"3600",
        "message_structure": "{"default":"test v2 default", "email":"abc"}"
    }
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For example, a topic has two types of subscriptions, SMS and email. After the API is called to publish messages, the email subscriber will receive message "abc", and the SMS subscriber will receive the default message "test v2 default".   


## Response<a name="section6514890019494"></a>

-   Parameter description

    <a name="table2558106919494"></a>
    <table><thead align="left"><tr id="row4596945119494"><th class="cellrowborder" valign="top" width="31.756824317568245%" id="mcps1.1.4.1.1"><p id="p3253804119494"><a name="p3253804119494"></a><a name="p3253804119494"></a><strong id="b1026020138"><a name="b1026020138"></a><a name="b1026020138"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.736726327367265%" id="mcps1.1.4.1.2"><p id="p1833566819494"><a name="p1833566819494"></a><a name="p1833566819494"></a><strong id="b1140952734"><a name="b1140952734"></a><a name="b1140952734"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.5064493550645%" id="mcps1.1.4.1.3"><p id="p879411519494"><a name="p879411519494"></a><a name="p879411519494"></a><strong id="b425172387"><a name="b425172387"></a><a name="b425172387"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5167660719494"><td class="cellrowborder" valign="top" width="31.756824317568245%" headers="mcps1.1.4.1.1 "><p id="p2505561119494"><a name="p2505561119494"></a><a name="p2505561119494"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.1.4.1.2 "><p id="p1623863619494"><a name="p1623863619494"></a><a name="p1623863619494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.5064493550645%" headers="mcps1.1.4.1.3 "><p id="p4026117819494"><a name="p4026117819494"></a><a name="p4026117819494"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row2382565119494"><td class="cellrowborder" valign="top" width="31.756824317568245%" headers="mcps1.1.4.1.1 "><p id="p5082954219494"><a name="p5082954219494"></a><a name="p5082954219494"></a>message_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.736726327367265%" headers="mcps1.1.4.1.2 "><p id="p2355227519494"><a name="p2355227519494"></a><a name="p2355227519494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.5064493550645%" headers="mcps1.1.4.1.3 "><p id="p2868611219494"><a name="p2868611219494"></a><a name="p2868611219494"></a>Message ID, which is unique</p>
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


## Returned Value<a name="section585587219494"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

