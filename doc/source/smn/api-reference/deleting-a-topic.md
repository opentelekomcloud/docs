# Deleting a Topic<a name="smn_api_51003"></a>

## Description<a name="en-us_topic_0025373766"></a>

-   API name

    DeleteTopic


-   Function

    Delete a topic and its subscribers. If a topic is deleted, a pending message will fail to deliver to the topic subscribers.


## URI<a name="section6556909"></a>

-   URI format

    DELETE /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}


-   Parameter description

    <a name="table36893359"></a>
    <table><thead align="left"><tr id="row46277382"><th class="cellrowborder" valign="top" width="21.862186218621858%" id="mcps1.1.5.1.1"><p id="p57480441"><a name="p57480441"></a><a name="p57480441"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.122212221222124%" id="mcps1.1.5.1.2"><p id="p25404116"><a name="p25404116"></a><a name="p25404116"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.122212221222124%" id="mcps1.1.5.1.3"><p id="p44467520"><a name="p44467520"></a><a name="p44467520"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.89338933893389%" id="mcps1.1.5.1.4"><p id="p45099364"><a name="p45099364"></a><a name="p45099364"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13951479"><td class="cellrowborder" valign="top" width="21.862186218621858%" headers="mcps1.1.5.1.1 "><p id="p56327989"><a name="p56327989"></a><a name="p56327989"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.122212221222124%" headers="mcps1.1.5.1.2 "><p id="p66273227"><a name="p66273227"></a><a name="p66273227"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.122212221222124%" headers="mcps1.1.5.1.3 "><p id="p66531170"><a name="p66531170"></a><a name="p66531170"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.89338933893389%" headers="mcps1.1.5.1.4 "><p id="p12084664154931"><a name="p12084664154931"></a><a name="p12084664154931"></a>Project ID</p>
    <p id="p20315681"><a name="p20315681"></a><a name="p20315681"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row46181951"><td class="cellrowborder" valign="top" width="21.862186218621858%" headers="mcps1.1.5.1.1 "><p id="p49750539"><a name="p49750539"></a><a name="p49750539"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.122212221222124%" headers="mcps1.1.5.1.2 "><p id="p3261819"><a name="p3261819"></a><a name="p3261819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.122212221222124%" headers="mcps1.1.5.1.3 "><p id="p62880759"><a name="p62880759"></a><a name="p62880759"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.89338933893389%" headers="mcps1.1.5.1.4 "><p id="p60176744"><a name="p60176744"></a><a name="p60176744"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section59012183"></a>

Request example

```
DELETE https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2
```

## Response<a name="section61347601"></a>

-   Parameter description

    <a name="table9967070"></a>
    <table><thead align="left"><tr id="row65063572"><th class="cellrowborder" valign="top" width="31.443144314431443%" id="mcps1.1.4.1.1"><p id="p35658012"><a name="p35658012"></a><a name="p35658012"></a><strong id="b1954561229"><a name="b1954561229"></a><a name="b1954561229"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.443144314431443%" id="mcps1.1.4.1.2"><p id="p2617844"><a name="p2617844"></a><a name="p2617844"></a><strong id="b996406409"><a name="b996406409"></a><a name="b996406409"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.11371137113711%" id="mcps1.1.4.1.3"><p id="p10718788"><a name="p10718788"></a><a name="p10718788"></a><strong id="b1242165385"><a name="b1242165385"></a><a name="b1242165385"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62991470"><td class="cellrowborder" valign="top" width="31.443144314431443%" headers="mcps1.1.4.1.1 "><p id="p2035480"><a name="p2035480"></a><a name="p2035480"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.443144314431443%" headers="mcps1.1.4.1.2 "><p id="p30656219"><a name="p30656219"></a><a name="p30656219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.11371137113711%" headers="mcps1.1.4.1.3 "><p id="p125790"><a name="p125790"></a><a name="p125790"></a>Request ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    { 
         "request_id": " 5fcba32bd2814ea39431829c22bda94b", 
    }
    ```


## Returned Value<a name="section15257500"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

