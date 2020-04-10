# Modifying a Message Template <a name="smn_api_53002"></a>

## Description<a name="section28165387"></a>

-   API name

    UpdateMessageTemplate


-   Function

    Modify the message template content.


## URI<a name="section52161898"></a>

-   URI format

    PUT /v2/\{project\_id\}/notifications/message\_template/\{message\_template\_id\}


-   Parameter description

    <a name="table54302323"></a>
    <table><thead align="left"><tr id="row60235282"><th class="cellrowborder" valign="top" width="25.5%" id="mcps1.1.5.1.1"><p id="p47219689"><a name="p47219689"></a><a name="p47219689"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.11%" id="mcps1.1.5.1.2"><p id="p66698493"><a name="p66698493"></a><a name="p66698493"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.27%" id="mcps1.1.5.1.3"><p id="p33868853"><a name="p33868853"></a><a name="p33868853"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.12%" id="mcps1.1.5.1.4"><p id="p59022586"><a name="p59022586"></a><a name="p59022586"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29043529"><td class="cellrowborder" valign="top" width="25.5%" headers="mcps1.1.5.1.1 "><p id="p3715619"><a name="p3715619"></a><a name="p3715619"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.1.5.1.2 "><p id="p32529705"><a name="p32529705"></a><a name="p32529705"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.3 "><p id="p17660485"><a name="p17660485"></a><a name="p17660485"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.12%" headers="mcps1.1.5.1.4 "><p id="p52904931155237"><a name="p52904931155237"></a><a name="p52904931155237"></a>Project ID</p>
    <p id="p21213148"><a name="p21213148"></a><a name="p21213148"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row29346720"><td class="cellrowborder" valign="top" width="25.5%" headers="mcps1.1.5.1.1 "><p id="p28274094"><a name="p28274094"></a><a name="p28274094"></a>message_template_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.1.5.1.2 "><p id="p8500244"><a name="p8500244"></a><a name="p8500244"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.3 "><p id="p17431163"><a name="p17431163"></a><a name="p17431163"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.12%" headers="mcps1.1.5.1.4 "><p id="p2638090"><a name="p2638090"></a><a name="p2638090"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-message-templates.md">Querying Message Templates</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section66803900"></a>

-   Parameter description

    <a name="table30791836"></a>
    <table><thead align="left"><tr id="row6221225"><th class="cellrowborder" valign="top" width="23.22%" id="mcps1.1.5.1.1"><p id="p34157240"><a name="p34157240"></a><a name="p34157240"></a><strong id="b1462225432"><a name="b1462225432"></a><a name="b1462225432"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.55%" id="mcps1.1.5.1.2"><p id="p15273051"><a name="p15273051"></a><a name="p15273051"></a><strong id="b1726867193357"><a name="b1726867193357"></a><a name="b1726867193357"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.650000000000002%" id="mcps1.1.5.1.3"><p id="p29157627"><a name="p29157627"></a><a name="p29157627"></a><strong id="b2011936958"><a name="b2011936958"></a><a name="b2011936958"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.580000000000002%" id="mcps1.1.5.1.4"><p id="p12957567"><a name="p12957567"></a><a name="p12957567"></a><strong id="b1375619600"><a name="b1375619600"></a><a name="b1375619600"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54777941"><td class="cellrowborder" valign="top" width="23.22%" headers="mcps1.1.5.1.1 "><p id="p7828214"><a name="p7828214"></a><a name="p7828214"></a>content</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.55%" headers="mcps1.1.5.1.2 "><p id="p30105629"><a name="p30105629"></a><a name="p30105629"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.1.5.1.3 "><p id="p22636847"><a name="p22636847"></a><a name="p22636847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.1.5.1.4 "><p id="p21645334"><a name="p21645334"></a><a name="p21645334"></a>Template content, which currently supports plain text only</p>
    <p id="p115842109384"><a name="p115842109384"></a><a name="p115842109384"></a>The template content cannot be left blank or larger than 256 KB.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    PUT https://{SMN_Endpoint}/v2/{project_id}/notifications/message_template/b3ffa2cdda574168826316f0628f774f
    ```

    ```
    {
        "content": "(1/22)You are invited to subscribe to topic({topic_id_id1}). Click the following URL to confirm subscription:(If you do not want to subscribe to this topic, ignore this message.)"
    }
    ```


## Response<a name="section64364196"></a>

-   Parameter description

    <a name="table19559856"></a>
    <table><thead align="left"><tr id="row645991"><th class="cellrowborder" valign="top" width="30.79%" id="mcps1.1.4.1.1"><p id="p52325333"><a name="p52325333"></a><a name="p52325333"></a><strong id="b1087091850"><a name="b1087091850"></a><a name="b1087091850"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.79%" id="mcps1.1.4.1.2"><p id="p10493555"><a name="p10493555"></a><a name="p10493555"></a><strong id="b1607979099"><a name="b1607979099"></a><a name="b1607979099"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.42%" id="mcps1.1.4.1.3"><p id="p44671593"><a name="p44671593"></a><a name="p44671593"></a><strong id="b339191833"><a name="b339191833"></a><a name="b339191833"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25915775"><td class="cellrowborder" valign="top" width="30.79%" headers="mcps1.1.4.1.1 "><p id="p18803055"><a name="p18803055"></a><a name="p18803055"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.79%" headers="mcps1.1.4.1.2 "><p id="p46652504"><a name="p46652504"></a><a name="p46652504"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.42%" headers="mcps1.1.4.1.3 "><p id="p20756449"><a name="p20756449"></a><a name="p20756449"></a>Request ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "request_id": "5fcba32bd2814ea39431829c22bda94b"
    }
    ```


## Returned Value<a name="section42406858"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

