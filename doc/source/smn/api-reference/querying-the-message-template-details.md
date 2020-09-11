# Querying the Message Template Details<a name="smn_api_53005"></a>

## Description<a name="section17649112"></a>

-   API name

    QueryMessageTemplateDetail


-   Function

    Query the template details, including the template content.


## URI<a name="section24624288"></a>

-   URI format

    GET /v2/\{project\_id\}/notifications/message\_template/\{message\_template\_id\}


-   Parameter description

    <a name="table48031108"></a>
    <table><thead align="left"><tr id="row27859461"><th class="cellrowborder" valign="top" width="25.040000000000003%" id="mcps1.1.5.1.1"><p id="p42023897"><a name="p42023897"></a><a name="p42023897"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.119999999999997%" id="mcps1.1.5.1.2"><p id="p48492497"><a name="p48492497"></a><a name="p48492497"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.51%" id="mcps1.1.5.1.3"><p id="p35578198"><a name="p35578198"></a><a name="p35578198"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.33%" id="mcps1.1.5.1.4"><p id="p63261775"><a name="p63261775"></a><a name="p63261775"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59293887"><td class="cellrowborder" valign="top" width="25.040000000000003%" headers="mcps1.1.5.1.1 "><p id="p38075525"><a name="p38075525"></a><a name="p38075525"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.1.5.1.2 "><p id="p64218721"><a name="p64218721"></a><a name="p64218721"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.51%" headers="mcps1.1.5.1.3 "><p id="p34333880"><a name="p34333880"></a><a name="p34333880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.33%" headers="mcps1.1.5.1.4 "><p id="p16674844155319"><a name="p16674844155319"></a><a name="p16674844155319"></a>Project ID</p>
    <p id="p29580916"><a name="p29580916"></a><a name="p29580916"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row22543082"><td class="cellrowborder" valign="top" width="25.040000000000003%" headers="mcps1.1.5.1.1 "><p id="p14050320"><a name="p14050320"></a><a name="p14050320"></a>message_template_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.119999999999997%" headers="mcps1.1.5.1.2 "><p id="p64334135"><a name="p64334135"></a><a name="p64334135"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.51%" headers="mcps1.1.5.1.3 "><p id="p43682438"><a name="p43682438"></a><a name="p43682438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.33%" headers="mcps1.1.5.1.4 "><p id="p48616614"><a name="p48616614"></a><a name="p48616614"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-message-templates.md">Querying Message Templates</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section20292006"></a>

Example request

```
GET https://{SMN_Endpoint}/v2/{project_id}/notifications/message_template/57ba8dcecda844878c5dd5815b65d10f
```

## Response<a name="section48410331"></a>

-   Parameter description

    <a name="table60555637"></a>
    <table><thead align="left"><tr id="row55059575"><th class="cellrowborder" valign="top" width="29.020000000000003%" id="mcps1.1.4.1.1"><p id="p30640599"><a name="p30640599"></a><a name="p30640599"></a><strong id="b842352706191030_1"><a name="b842352706191030_1"></a><a name="b842352706191030_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.69%" id="mcps1.1.4.1.2"><p id="p65969435"><a name="p65969435"></a><a name="p65969435"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.29%" id="mcps1.1.4.1.3"><p id="p41924012"><a name="p41924012"></a><a name="p41924012"></a><strong id="b84235270619115_1"><a name="b84235270619115_1"></a><a name="b84235270619115_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51318482"><td class="cellrowborder" valign="top" width="29.020000000000003%" headers="mcps1.1.4.1.1 "><p id="p63156409"><a name="p63156409"></a><a name="p63156409"></a>message_template_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.1.4.1.2 "><p id="p15395467"><a name="p15395467"></a><a name="p15395467"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.1.4.1.3 "><p id="p39073330"><a name="p39073330"></a><a name="p39073330"></a>Template ID</p>
    </td>
    </tr>
    <tr id="row30299850"><td class="cellrowborder" valign="top" width="29.020000000000003%" headers="mcps1.1.4.1.1 "><p id="p38368787"><a name="p38368787"></a><a name="p38368787"></a>message_template_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.1.4.1.2 "><p id="p20864077"><a name="p20864077"></a><a name="p20864077"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.1.4.1.3 "><p id="p12268704"><a name="p12268704"></a><a name="p12268704"></a>Template name</p>
    </td>
    </tr>
    <tr id="row139520593919"><td class="cellrowborder" valign="top" width="29.020000000000003%" headers="mcps1.1.4.1.1 "><p id="p33048293"><a name="p33048293"></a><a name="p33048293"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.1.4.1.2 "><p id="p18228205714104"><a name="p18228205714104"></a><a name="p18228205714104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.1.4.1.3 "><p id="p1114082"><a name="p1114082"></a><a name="p1114082"></a>Protocol supported by the template</p>
    <p id="p13331422755"><a name="p13331422755"></a><a name="p13331422755"></a>Currently, the following protocols are supported:</p>
    <a name="ul88352301953"></a><a name="ul88352301953"></a><ul id="ul88352301953"><li><strong id="smn_api_53001_b122581017374"><a name="smn_api_53001_b122581017374"></a><a name="smn_api_53001_b122581017374"></a>email</strong></li><li><strong id="smn_api_53001_b1938219133716"><a name="smn_api_53001_b1938219133716"></a><a name="smn_api_53001_b1938219133716"></a>default</strong></li><li><strong id="smn_api_53001_b23671526885"><a name="smn_api_53001_b23671526885"></a><a name="smn_api_53001_b23671526885"></a>sms</strong></li><li><strong id="smn_api_53001_b49701126897"><a name="smn_api_53001_b49701126897"></a><a name="smn_api_53001_b49701126897"></a>dms</strong></li><li><strong id="smn_api_53001_b185159332910"><a name="smn_api_53001_b185159332910"></a><a name="smn_api_53001_b185159332910"></a>http</strong> and <strong id="smn_api_53001_b25282033899"><a name="smn_api_53001_b25282033899"></a><a name="smn_api_53001_b25282033899"></a>https</strong></li></ul>
    </td>
    </tr>
    <tr id="row48741777"><td class="cellrowborder" valign="top" width="29.020000000000003%" headers="mcps1.1.4.1.1 "><p id="p55769855"><a name="p55769855"></a><a name="p55769855"></a>tag_names</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.1.4.1.2 "><p id="p21064410"><a name="p21064410"></a><a name="p21064410"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.1.4.1.3 "><p id="p1311575516403"><a name="p1311575516403"></a><a name="p1311575516403"></a>Variable list</p>
    <p id="p28495625"><a name="p28495625"></a><a name="p28495625"></a>The variable name will be quoted in braces ({}) in the template. When you use a template to send messages, you can replace the variable with any content.</p>
    </td>
    </tr>
    <tr id="row36671901"><td class="cellrowborder" valign="top" width="29.020000000000003%" headers="mcps1.1.4.1.1 "><p id="p17633966"><a name="p17633966"></a><a name="p17633966"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.1.4.1.2 "><p id="p19065136"><a name="p19065136"></a><a name="p19065136"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.1.4.1.3 "><p id="p772170"><a name="p772170"></a><a name="p772170"></a>Time when the template was created</p>
    <p id="p17515094173556"><a name="p17515094173556"></a><a name="p17515094173556"></a>The UTC time is in <em id="i2155151513511"><a name="i2155151513511"></a><a name="i2155151513511"></a>YYYY-MM-DDTHH:MM:SSZ</em> format.</p>
    </td>
    </tr>
    <tr id="row26041554"><td class="cellrowborder" valign="top" width="29.020000000000003%" headers="mcps1.1.4.1.1 "><p id="p28991153"><a name="p28991153"></a><a name="p28991153"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.1.4.1.2 "><p id="p66582052"><a name="p66582052"></a><a name="p66582052"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.1.4.1.3 "><p id="p24437140"><a name="p24437140"></a><a name="p24437140"></a>Last time when the template was updated</p>
    <p id="p3896935217360"><a name="p3896935217360"></a><a name="p3896935217360"></a>The UTC time is in <em id="i1557451817351"><a name="i1557451817351"></a><a name="i1557451817351"></a>YYYY-MM-DDTHH:MM:SSZ</em> format.</p>
    </td>
    </tr>
    <tr id="row30826283"><td class="cellrowborder" valign="top" width="29.020000000000003%" headers="mcps1.1.4.1.1 "><p id="p13901009"><a name="p13901009"></a><a name="p13901009"></a>content</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.1.4.1.2 "><p id="p52239951"><a name="p52239951"></a><a name="p52239951"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.1.4.1.3 "><p id="p3577678"><a name="p3577678"></a><a name="p3577678"></a>Template content</p>
    </td>
    </tr>
    <tr id="row17748175775810"><td class="cellrowborder" valign="top" width="29.020000000000003%" headers="mcps1.1.4.1.1 "><p id="p55439693194741"><a name="p55439693194741"></a><a name="p55439693194741"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.1.4.1.2 "><p id="p61430126194741"><a name="p61430126194741"></a><a name="p61430126194741"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.29%" headers="mcps1.1.4.1.3 "><p id="p9784341194741"><a name="p9784341194741"></a><a name="p9784341194741"></a>Request ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "message_template_name": "confirm_message",
        "protocol": "https",
        "update_time": "2016-08-02T08:22:25Z",
        "create_time": "2016-08-02T08:22:20Z",
        "request_id":"ba79ca8f794f4f50985ce7b98a401b47",
        "tag_names": [
            "topic_id_id4"
        ],
        "content": "(1/24)You are invited to subscribe to topic({topic_id_id4}). Click the following URL to confirm subscription:(If you do not want to subscribe to this topic, ignore this message.)",
        "message_template_id": "57ba8dcecda844878c5dd5815b65d10f"
    }
    ```


## Returned Value<a name="section33039800"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

