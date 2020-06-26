# Creating a Topic<a name="smn_api_51001"></a>

## Description<a name="section9931723184157"></a>

-   API name

    CreateTopic


-   Function

    Create a topic. Each user can create 3000 topics at most. In the high-concurrent scenario, a user may create a few topics more than 3000.

    The API is idempotent. It resturns a successful result after creating a topic. If a topic of the same name already exists, the status code is 200. Otherwise, the status code is 201.


## URI<a name="section59578064184157"></a>

-   URI format

    POST /v2/\{project\_id\}/notifications/topics


-   Parameter description

    <a name="table29213141184157"></a>
    <table><thead align="left"><tr id="row19251397184157"><th class="cellrowborder" valign="top" width="25.25747425257474%" id="mcps1.1.5.1.1"><p id="p15859347184157"><a name="p15859347184157"></a><a name="p15859347184157"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.33756624337566%" id="mcps1.1.5.1.2"><p id="p9538705184157"><a name="p9538705184157"></a><a name="p9538705184157"></a><strong id="b842352706191051"><a name="b842352706191051"></a><a name="b842352706191051"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.13768623137686%" id="mcps1.1.5.1.3"><p id="p34437607184157"><a name="p34437607184157"></a><a name="p34437607184157"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.267273272672732%" id="mcps1.1.5.1.4"><p id="p37982782184157"><a name="p37982782184157"></a><a name="p37982782184157"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29823245184157"><td class="cellrowborder" valign="top" width="25.25747425257474%" headers="mcps1.1.5.1.1 "><p id="p66872662184157"><a name="p66872662184157"></a><a name="p66872662184157"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.33756624337566%" headers="mcps1.1.5.1.2 "><p id="p47976511184157"><a name="p47976511184157"></a><a name="p47976511184157"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.13768623137686%" headers="mcps1.1.5.1.3 "><p id="p60892144184157"><a name="p60892144184157"></a><a name="p60892144184157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.267273272672732%" headers="mcps1.1.5.1.4 "><p id="p59334239154910"><a name="p59334239154910"></a><a name="p59334239154910"></a>Project ID</p>
    <p id="p33316626184157"><a name="p33316626184157"></a><a name="p33316626184157"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section16815303184157"></a>

-   Parameter description

    <a name="table65343646184157"></a>
    <table><thead align="left"><tr id="row24199091184157"><th class="cellrowborder" valign="top" width="21.10788921107889%" id="mcps1.1.5.1.1"><p id="p13969361184157"><a name="p13969361184157"></a><a name="p13969361184157"></a><strong id="b842352706191030_1"><a name="b842352706191030_1"></a><a name="b842352706191030_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.897610238976103%" id="mcps1.1.5.1.2"><p id="p57776496184157"><a name="p57776496184157"></a><a name="p57776496184157"></a><strong id="b6239563592942"><a name="b6239563592942"></a><a name="b6239563592942"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.377762223777623%" id="mcps1.1.5.1.3"><p id="p49384632184157"><a name="p49384632184157"></a><a name="p49384632184157"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.61673832616738%" id="mcps1.1.5.1.4"><p id="p40732240184157"><a name="p40732240184157"></a><a name="p40732240184157"></a><strong id="b84235270619115_1"><a name="b84235270619115_1"></a><a name="b84235270619115_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16731537184157"><td class="cellrowborder" valign="top" width="21.10788921107889%" headers="mcps1.1.5.1.1 "><p id="p13077258184157"><a name="p13077258184157"></a><a name="p13077258184157"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.897610238976103%" headers="mcps1.1.5.1.2 "><p id="p52625012184157"><a name="p52625012184157"></a><a name="p52625012184157"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.377762223777623%" headers="mcps1.1.5.1.3 "><p id="p44473009184157"><a name="p44473009184157"></a><a name="p44473009184157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.61673832616738%" headers="mcps1.1.5.1.4 "><p id="p45543947184157"><a name="p45543947184157"></a><a name="p45543947184157"></a>Name of the topic to be created</p>
    <p id="p979550192113"><a name="p979550192113"></a><a name="p979550192113"></a>The topic name is a string of 1 to 255 characters. It must contain letters, digits, hyphens (-), and underscores (_), and must start with a letter or digit.</p>
    </td>
    </tr>
    <tr id="row49758753184157"><td class="cellrowborder" valign="top" width="21.10788921107889%" headers="mcps1.1.5.1.1 "><p id="p3927189184157"><a name="p3927189184157"></a><a name="p3927189184157"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.897610238976103%" headers="mcps1.1.5.1.2 "><p id="p49666922184157"><a name="p49666922184157"></a><a name="p49666922184157"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.377762223777623%" headers="mcps1.1.5.1.3 "><p id="p35509001184157"><a name="p35509001184157"></a><a name="p35509001184157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.61673832616738%" headers="mcps1.1.5.1.4 "><p id="p6330530816482"><a name="p6330530816482"></a><a name="p6330530816482"></a>Topic display name, which is presented as the name of the email sender in email messages</p>
    <p id="p11282828192211"><a name="p11282828192211"></a><a name="p11282828192211"></a>The display name cannot exceed 192 bytes.</p>
    <p id="p7371996273"><a name="p7371996273"></a><a name="p7371996273"></a>The value is left blank by default.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    POST https://{SMN_Endpoint}/v2/{project_id}/notifications/topics
    ```

    ```
    {
        "name": "test_topic_v2",
        "display_name": "testtest"
    }
    ```


## Response<a name="section26706597184157"></a>

-   Parameter description

    <a name="table741793184157"></a>
    <table><thead align="left"><tr id="row65023299184157"><th class="cellrowborder" valign="top" width="21.13%" id="mcps1.1.4.1.1"><p id="p32395875184157"><a name="p32395875184157"></a><a name="p32395875184157"></a><strong id="b842352706191030_2"><a name="b842352706191030_2"></a><a name="b842352706191030_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.6%" id="mcps1.1.4.1.2"><p id="p6820199184157"><a name="p6820199184157"></a><a name="p6820199184157"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.269999999999996%" id="mcps1.1.4.1.3"><p id="p15565240184157"><a name="p15565240184157"></a><a name="p15565240184157"></a><strong id="b84235270619115_2"><a name="b84235270619115_2"></a><a name="b84235270619115_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50957918184157"><td class="cellrowborder" valign="top" width="21.13%" headers="mcps1.1.4.1.1 "><p id="p33950725184157"><a name="p33950725184157"></a><a name="p33950725184157"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.1.4.1.2 "><p id="p65654167184157"><a name="p65654167184157"></a><a name="p65654167184157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.269999999999996%" headers="mcps1.1.4.1.3 "><p id="p16387326184157"><a name="p16387326184157"></a><a name="p16387326184157"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row983478184157"><td class="cellrowborder" valign="top" width="21.13%" headers="mcps1.1.4.1.1 "><p id="p12552895184157"><a name="p12552895184157"></a><a name="p12552895184157"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.6%" headers="mcps1.1.4.1.2 "><p id="p10151609184157"><a name="p10151609184157"></a><a name="p10151609184157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.269999999999996%" headers="mcps1.1.4.1.3 "><p id="p16974028184157"><a name="p16974028184157"></a><a name="p16974028184157"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "request_id": "6a63a18b8bab40ffb71ebd9cb80d0085",
        "topic_urn": "urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2"
    }
    ```


## Returned Value<a name="section15080701184157"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

