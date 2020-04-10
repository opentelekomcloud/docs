# Modifying a Topic<a name="smn_api_51002"></a>

## Description<a name="section37714282185146"></a>

-   API name

    UpdateTopic


-   Function

    Update the topic display name.


## URI<a name="section46186214185146"></a>

-   URI format

    PUT /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}


-   Parameter description

    <a name="table20000134185146"></a>
    <table><thead align="left"><tr id="row37235592185146"><th class="cellrowborder" valign="top" width="22.887711228877112%" id="mcps1.1.5.1.1"><p id="p63292990185146"><a name="p63292990185146"></a><a name="p63292990185146"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.047595240475953%" id="mcps1.1.5.1.2"><p id="p26458572185146"><a name="p26458572185146"></a><a name="p26458572185146"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.957304269573047%" id="mcps1.1.5.1.3"><p id="p62769627185146"><a name="p62769627185146"></a><a name="p62769627185146"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.107389261073894%" id="mcps1.1.5.1.4"><p id="p51175059185146"><a name="p51175059185146"></a><a name="p51175059185146"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13917467185146"><td class="cellrowborder" valign="top" width="22.887711228877112%" headers="mcps1.1.5.1.1 "><p id="p53573052185146"><a name="p53573052185146"></a><a name="p53573052185146"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.047595240475953%" headers="mcps1.1.5.1.2 "><p id="p44449957185146"><a name="p44449957185146"></a><a name="p44449957185146"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.957304269573047%" headers="mcps1.1.5.1.3 "><p id="p43676799185146"><a name="p43676799185146"></a><a name="p43676799185146"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.107389261073894%" headers="mcps1.1.5.1.4 "><p id="p60845278154921"><a name="p60845278154921"></a><a name="p60845278154921"></a>Project ID</p>
    <p id="p48159858185146"><a name="p48159858185146"></a><a name="p48159858185146"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row10600782185146"><td class="cellrowborder" valign="top" width="22.887711228877112%" headers="mcps1.1.5.1.1 "><p id="p53356996185146"><a name="p53356996185146"></a><a name="p53356996185146"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.047595240475953%" headers="mcps1.1.5.1.2 "><p id="p26949456185146"><a name="p26949456185146"></a><a name="p26949456185146"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.957304269573047%" headers="mcps1.1.5.1.3 "><p id="p35422295185146"><a name="p35422295185146"></a><a name="p35422295185146"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.107389261073894%" headers="mcps1.1.5.1.4 "><p id="p50633667185146"><a name="p50633667185146"></a><a name="p50633667185146"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section18618345185146"></a>

-   Parameter description

    <a name="table16833793185146"></a>
    <table><thead align="left"><tr id="row46280455185146"><th class="cellrowborder" valign="top" width="24.55754424557544%" id="mcps1.1.5.1.1"><p id="p57729347185146"><a name="p57729347185146"></a><a name="p57729347185146"></a><strong id="b1356528961"><a name="b1356528961"></a><a name="b1356528961"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.537946205379455%" id="mcps1.1.5.1.2"><p id="p45565556185146"><a name="p45565556185146"></a><a name="p45565556185146"></a><strong id="b1876350995538"><a name="b1876350995538"></a><a name="b1876350995538"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.15788421157884%" id="mcps1.1.5.1.3"><p id="p66931458185146"><a name="p66931458185146"></a><a name="p66931458185146"></a><strong id="b784388616"><a name="b784388616"></a><a name="b784388616"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.74662533746625%" id="mcps1.1.5.1.4"><p id="p52739028185146"><a name="p52739028185146"></a><a name="p52739028185146"></a><strong id="b1905563813"><a name="b1905563813"></a><a name="b1905563813"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7465062185146"><td class="cellrowborder" valign="top" width="24.55754424557544%" headers="mcps1.1.5.1.1 "><p id="p690294185146"><a name="p690294185146"></a><a name="p690294185146"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.537946205379455%" headers="mcps1.1.5.1.2 "><p id="p55913834185146"><a name="p55913834185146"></a><a name="p55913834185146"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.15788421157884%" headers="mcps1.1.5.1.3 "><p id="p32726699185146"><a name="p32726699185146"></a><a name="p32726699185146"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.74662533746625%" headers="mcps1.1.5.1.4 "><p id="p17720185311254"><a name="p17720185311254"></a><a name="p17720185311254"></a>Topic display name, which is presented as the name of the email sender in email messages</p>
    <p id="p57656838184157"><a name="p57656838184157"></a><a name="p57656838184157"></a>The display name cannot exceed 192 bytes.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    PUT https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2
    { 
        "display_name":"testtest222"
    }
    ```


## Response<a name="section11007541185146"></a>

-   Parameter description

    <a name="table11342130185146"></a>
    <table><thead align="left"><tr id="row63969717185146"><th class="cellrowborder" valign="top" width="26.16%" id="mcps1.1.4.1.1"><p id="p14164593185146"><a name="p14164593185146"></a><a name="p14164593185146"></a><strong id="b1721293395"><a name="b1721293395"></a><a name="b1721293395"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.080000000000002%" id="mcps1.1.4.1.2"><p id="p6481381185146"><a name="p6481381185146"></a><a name="p6481381185146"></a><strong id="b1338891928"><a name="b1338891928"></a><a name="b1338891928"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.760000000000005%" id="mcps1.1.4.1.3"><p id="p55229882185146"><a name="p55229882185146"></a><a name="p55229882185146"></a><strong id="b946130502"><a name="b946130502"></a><a name="b946130502"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42504102185146"><td class="cellrowborder" valign="top" width="26.16%" headers="mcps1.1.4.1.1 "><p id="p20280204185146"><a name="p20280204185146"></a><a name="p20280204185146"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.080000000000002%" headers="mcps1.1.4.1.2 "><p id="p32083827185146"><a name="p32083827185146"></a><a name="p32083827185146"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.760000000000005%" headers="mcps1.1.4.1.3 "><p id="p48653186185146"><a name="p48653186185146"></a><a name="p48653186185146"></a>Request ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "request_id": "6a63a18b8bab40ffb71ebd9cb80d0085"
    }
    ```


## Returned Value<a name="section26976275185146"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

