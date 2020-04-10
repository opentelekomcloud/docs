# Deleting a Specified Topic Attribute<a name="smn_api_51008"></a>

## Description<a name="section64935954"></a>

-   API name

    DeleteTopicAttributeByName


-   Function

    Delete a specified topic attribute.


## URI<a name="section47552675"></a>

-   URI format

    DELETE /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}/attributes/\{name\}


-   Parameter description

    <a name="table60453091"></a>
    <table><thead align="left"><tr id="row31471768"><th class="cellrowborder" valign="top" width="21.46%" id="mcps1.1.5.1.1"><p id="p66185246"><a name="p66185246"></a><a name="p66185246"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.7%" id="mcps1.1.5.1.2"><p id="p59404709"><a name="p59404709"></a><a name="p59404709"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.310000000000002%" id="mcps1.1.5.1.3"><p id="p47052116"><a name="p47052116"></a><a name="p47052116"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.53%" id="mcps1.1.5.1.4"><p id="p53125076"><a name="p53125076"></a><a name="p53125076"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57297510"><td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.1.5.1.1 "><p id="p10586695"><a name="p10586695"></a><a name="p10586695"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.1.5.1.2 "><p id="p52215961"><a name="p52215961"></a><a name="p52215961"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.310000000000002%" headers="mcps1.1.5.1.3 "><p id="p1634435"><a name="p1634435"></a><a name="p1634435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.53%" headers="mcps1.1.5.1.4 "><p id="p35765041155042"><a name="p35765041155042"></a><a name="p35765041155042"></a>Project ID</p>
    <p id="p65280430"><a name="p65280430"></a><a name="p65280430"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row9249362"><td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.1.5.1.1 "><p id="p11000853"><a name="p11000853"></a><a name="p11000853"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.1.5.1.2 "><p id="p18653909"><a name="p18653909"></a><a name="p18653909"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.310000000000002%" headers="mcps1.1.5.1.3 "><p id="p34571641"><a name="p34571641"></a><a name="p34571641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.53%" headers="mcps1.1.5.1.4 "><p id="p48839530"><a name="p48839530"></a><a name="p48839530"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    <tr id="row5965394515386"><td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.1.5.1.1 "><p id="p14783623153811"><a name="p14783623153811"></a><a name="p14783623153811"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.7%" headers="mcps1.1.5.1.2 "><p id="p56622849153811"><a name="p56622849153811"></a><a name="p56622849153811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.310000000000002%" headers="mcps1.1.5.1.3 "><p id="p23048084153811"><a name="p23048084153811"></a><a name="p23048084153811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.53%" headers="mcps1.1.5.1.4 "><p id="p54955495153811"><a name="p54955495153811"></a><a name="p54955495153811"></a>Attribute name</p>
    <p id="p2749131513324"><a name="p2749131513324"></a><a name="p2749131513324"></a>Only specified attribute names are supported. For details, see section <a href="topic-attribute-list.md">Topic Attribute List</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section25320898"></a>

Example request

```
DELETE https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/{topic_urn}/attributes/access_policy
```

## Response<a name="section26561495"></a>

-   Parameter description

    <a name="table38552084"></a>
    <table><thead align="left"><tr id="row10058158"><th class="cellrowborder" valign="top" width="32.12678732126787%" id="mcps1.1.4.1.1"><p id="p9404449"><a name="p9404449"></a><a name="p9404449"></a><strong id="b1554253775"><a name="b1554253775"></a><a name="b1554253775"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.12678732126787%" id="mcps1.1.4.1.2"><p id="p23562876"><a name="p23562876"></a><a name="p23562876"></a><strong id="b1090510174"><a name="b1090510174"></a><a name="b1090510174"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.746425357464254%" id="mcps1.1.4.1.3"><p id="p29544808"><a name="p29544808"></a><a name="p29544808"></a><strong id="b271585961"><a name="b271585961"></a><a name="b271585961"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33089041"><td class="cellrowborder" valign="top" width="32.12678732126787%" headers="mcps1.1.4.1.1 "><p id="p62966687"><a name="p62966687"></a><a name="p62966687"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.12678732126787%" headers="mcps1.1.4.1.2 "><p id="p27997"><a name="p27997"></a><a name="p27997"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.746425357464254%" headers="mcps1.1.4.1.3 "><p id="p2267763"><a name="p2267763"></a><a name="p2267763"></a>Request ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "request_id":"6837531fd3f54550927b930180a706bf"
    }
    ```


## Returned Value<a name="section37726867"></a>

See  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See  [Error Code](error-code.md).

