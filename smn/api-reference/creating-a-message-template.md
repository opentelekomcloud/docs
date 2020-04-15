# Creating a Message Template<a name="smn_api_53001"></a>

## Description<a name="section8297742193738"></a>

-   API name

    CreateMessageTemplate


-   Function

    Create a message template for quick message sending to reduce the request data volume.

    By default, a user can create a maximum of 100 message templates. However, in a high-concurrency scenario, which is rare, extra templates may be successfully created.


## URI<a name="section9256466193738"></a>

-   URI format

    POST /v2/\{project\_id\}/notifications/message\_template


-   Parameter description

    <a name="table66376860193738"></a>
    <table><thead align="left"><tr id="row32265521193738"><th class="cellrowborder" valign="top" width="19.54%" id="mcps1.1.5.1.1"><p id="p63370415193738"><a name="p63370415193738"></a><a name="p63370415193738"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.490000000000002%" id="mcps1.1.5.1.2"><p id="p32730030193738"><a name="p32730030193738"></a><a name="p32730030193738"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.09%" id="mcps1.1.5.1.3"><p id="p33886806193738"><a name="p33886806193738"></a><a name="p33886806193738"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.88%" id="mcps1.1.5.1.4"><p id="p60476750193738"><a name="p60476750193738"></a><a name="p60476750193738"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40354127193738"><td class="cellrowborder" valign="top" width="19.54%" headers="mcps1.1.5.1.1 "><p id="p47458856193738"><a name="p47458856193738"></a><a name="p47458856193738"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.1.5.1.2 "><p id="p18962162193738"><a name="p18962162193738"></a><a name="p18962162193738"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.09%" headers="mcps1.1.5.1.3 "><p id="p59540181193738"><a name="p59540181193738"></a><a name="p59540181193738"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.88%" headers="mcps1.1.5.1.4 "><p id="p204280715521"><a name="p204280715521"></a><a name="p204280715521"></a>Project ID</p>
    <p id="p58025336193738"><a name="p58025336193738"></a><a name="p58025336193738"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section62753823193738"></a>

-   Parameter description

    <a name="table14955048193738"></a>
    <table><thead align="left"><tr id="row8946017193738"><th class="cellrowborder" valign="top" width="25.629999999999995%" id="mcps1.1.5.1.1"><p id="p53538768193738"><a name="p53538768193738"></a><a name="p53538768193738"></a><strong id="b842352706191030_1"><a name="b842352706191030_1"></a><a name="b842352706191030_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.41%" id="mcps1.1.5.1.2"><p id="p41672976193738"><a name="p41672976193738"></a><a name="p41672976193738"></a><strong id="b181195193337"><a name="b181195193337"></a><a name="b181195193337"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.560000000000002%" id="mcps1.1.5.1.3"><p id="p20067913193738"><a name="p20067913193738"></a><a name="p20067913193738"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.4%" id="mcps1.1.5.1.4"><p id="p14888226193738"><a name="p14888226193738"></a><a name="p14888226193738"></a><strong id="b84235270619115_1"><a name="b84235270619115_1"></a><a name="b84235270619115_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38253781193738"><td class="cellrowborder" valign="top" width="25.629999999999995%" headers="mcps1.1.5.1.1 "><p id="p11548543193738"><a name="p11548543193738"></a><a name="p11548543193738"></a>message_template_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.41%" headers="mcps1.1.5.1.2 "><p id="p63016810193738"><a name="p63016810193738"></a><a name="p63016810193738"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.560000000000002%" headers="mcps1.1.5.1.3 "><p id="p4087998193738"><a name="p4087998193738"></a><a name="p4087998193738"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.4%" headers="mcps1.1.5.1.4 "><p id="p62692385193738"><a name="p62692385193738"></a><a name="p62692385193738"></a>Template name</p>
    <p id="p487820285367"><a name="p487820285367"></a><a name="p487820285367"></a>The template name is a string of 1 to 64 characters. It must contain upper- or lower-case letters, digits, hyphens (-), and underscores (_), and must start with a letter or digit.</p>
    </td>
    </tr>
    <tr id="row1612977193738"><td class="cellrowborder" valign="top" width="25.629999999999995%" headers="mcps1.1.5.1.1 "><p id="p63542293193738"><a name="p63542293193738"></a><a name="p63542293193738"></a>content</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.41%" headers="mcps1.1.5.1.2 "><p id="p46652102193738"><a name="p46652102193738"></a><a name="p46652102193738"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.560000000000002%" headers="mcps1.1.5.1.3 "><p id="p20723883193738"><a name="p20723883193738"></a><a name="p20723883193738"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.4%" headers="mcps1.1.5.1.4 "><p id="p912940193738"><a name="p912940193738"></a><a name="p912940193738"></a>Template content, which currently supports plain text only</p>
    <p id="p73931234163613"><a name="p73931234163613"></a><a name="p73931234163613"></a>The template content cannot be left blank or larger than 256 KB.</p>
    </td>
    </tr>
    <tr id="row61554123193738"><td class="cellrowborder" valign="top" width="25.629999999999995%" headers="mcps1.1.5.1.1 "><p id="p19828051193738"><a name="p19828051193738"></a><a name="p19828051193738"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.41%" headers="mcps1.1.5.1.2 "><p id="p62568275193738"><a name="p62568275193738"></a><a name="p62568275193738"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.560000000000002%" headers="mcps1.1.5.1.3 "><p id="p34865524193738"><a name="p34865524193738"></a><a name="p34865524193738"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.4%" headers="mcps1.1.5.1.4 "><p id="p23131803"><a name="p23131803"></a><a name="p23131803"></a>Protocol supported by the template</p>
    <p id="p15571735514"><a name="p15571735514"></a><a name="p15571735514"></a>Currently, the following protocols are supported:</p>
    <a name="ul1715273514576"></a><a name="ul1715273514576"></a><ul id="ul1715273514576"><li><strong id="b122581017374"><a name="b122581017374"></a><a name="b122581017374"></a>email</strong></li><li><strong id="b1938219133716"><a name="b1938219133716"></a><a name="b1938219133716"></a>default</strong></li><li><strong id="b23671526885"><a name="b23671526885"></a><a name="b23671526885"></a>sms</strong></li><li><strong id="b49701126897"><a name="b49701126897"></a><a name="b49701126897"></a>dms</strong></li><li><strong id="b185159332910"><a name="b185159332910"></a><a name="b185159332910"></a>http</strong> and <strong id="b25282033899"><a name="b25282033899"></a><a name="b25282033899"></a>https</strong></li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{SMN_Endpoint}/v2/{project_id}/notifications/message_template
    ```

    ```
    {
        "message_template_name": "confirm_message",
        "protocol": "https",
        "content": "(1/2)You are invited to subscribe to topic({topic_id}). Click the following URL to confirm subscription:(If you do not want to subscribe to this topic, ignore this message.)"
    }
    ```


## Response<a name="section2535551193738"></a>

-   Parameter description

    <a name="table59861740193738"></a>
    <table><thead align="left"><tr id="row37209510193738"><th class="cellrowborder" valign="top" width="34.09340934093409%" id="mcps1.1.4.1.1"><p id="p61180371193738"><a name="p61180371193738"></a><a name="p61180371193738"></a><strong id="b842352706191030_2"><a name="b842352706191030_2"></a><a name="b842352706191030_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.56295629562956%" id="mcps1.1.4.1.2"><p id="p56663008193738"><a name="p56663008193738"></a><a name="p56663008193738"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.343634363436344%" id="mcps1.1.4.1.3"><p id="p26300917193738"><a name="p26300917193738"></a><a name="p26300917193738"></a><strong id="b84235270619115_2"><a name="b84235270619115_2"></a><a name="b84235270619115_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23431513193738"><td class="cellrowborder" valign="top" width="34.09340934093409%" headers="mcps1.1.4.1.1 "><p id="p18904440193738"><a name="p18904440193738"></a><a name="p18904440193738"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.56295629562956%" headers="mcps1.1.4.1.2 "><p id="p54864704193738"><a name="p54864704193738"></a><a name="p54864704193738"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.1.4.1.3 "><p id="p14856024193738"><a name="p14856024193738"></a><a name="p14856024193738"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row25514541193738"><td class="cellrowborder" valign="top" width="34.09340934093409%" headers="mcps1.1.4.1.1 "><p id="p53411941193738"><a name="p53411941193738"></a><a name="p53411941193738"></a>message_template_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.56295629562956%" headers="mcps1.1.4.1.2 "><p id="p31399978193738"><a name="p31399978193738"></a><a name="p31399978193738"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.343634363436344%" headers="mcps1.1.4.1.3 "><p id="p60370275193738"><a name="p60370275193738"></a><a name="p60370275193738"></a>Resource identifier of the template, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
        "request_id":"ca03efa691624d8eb2dfeba01a1bcf6e",
        "message_template_id":"57ba8dcecda844878c5dd5815b65d10f"
    }
    ```


## Returned Value<a name="section49451272193738"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

