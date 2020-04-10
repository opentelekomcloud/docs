# Querying Topics<a name="smn_api_51004"></a>

## Description<a name="en-us_topic_0025373767-chtext"></a>

-   API name

    ListTopics


-   Function

    Query the topic list by page. The list is sorted by the topic creation time in descending order. If no topic has been created, an empty list is returned.


## URI<a name="section30715040"></a>

-   URI format

    GET /v2/\{project\_id\}/notifications/topics?offset=\{offset\}&limit=\{limit\}


-   Parameter description

    <a name="table65858198"></a>
    <table><thead align="left"><tr id="row16627584"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p4657088"><a name="p4657088"></a><a name="p4657088"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.2"><p id="p41679865"><a name="p41679865"></a><a name="p41679865"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.650000000000002%" id="mcps1.1.5.1.3"><p id="p20625874"><a name="p20625874"></a><a name="p20625874"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.35%" id="mcps1.1.5.1.4"><p id="p60083059"><a name="p60083059"></a><a name="p60083059"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7485743"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p57385070"><a name="p57385070"></a><a name="p57385070"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.1.5.1.3 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.35%" headers="mcps1.1.5.1.4 "><p id="p12240680154940"><a name="p12240680154940"></a><a name="p12240680154940"></a>Project ID</p>
    <p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row52313669"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p9548790"><a name="p9548790"></a><a name="p9548790"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p2088631120211"><a name="p2088631120211"></a><a name="p2088631120211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.1.5.1.3 "><p id="p37041500"><a name="p37041500"></a><a name="p37041500"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.35%" headers="mcps1.1.5.1.4 "><p id="p146581828102110"><a name="p146581828102110"></a><a name="p146581828102110"></a>Offset</p>
    <p id="p21821344207"><a name="p21821344207"></a><a name="p21821344207"></a>If the value is an integer greater than 0 but less than the number of resources, all resources after this offset will be queried. The default value is <strong id="b168815174914"><a name="b168815174914"></a><a name="b168815174914"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row51489795"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p9923843"><a name="p9923843"></a><a name="p9923843"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.2 "><p id="p65633828"><a name="p65633828"></a><a name="p65633828"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.650000000000002%" headers="mcps1.1.5.1.3 "><p id="p14739853"><a name="p14739853"></a><a name="p14739853"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.35%" headers="mcps1.1.5.1.4 "><a name="ul38160342182720"></a><a name="ul38160342182720"></a><ul id="ul38160342182720"><li>Number of resources returned on each page</li><li>Value range: 1–100<p id="p683218308526"><a name="p683218308526"></a><a name="p683218308526"></a>Commonly used values are <strong id="b85981650205215"><a name="b85981650205215"></a><a name="b85981650205215"></a>10</strong>, <strong id="b106551253205216"><a name="b106551253205216"></a><a name="b106551253205216"></a>20</strong>, and <strong id="b11116125714526"><a name="b11116125714526"></a><a name="b11116125714526"></a>50</strong>.</p>
    <p id="p18225173316526"><a name="p18225173316526"></a><a name="p18225173316526"></a>The default value is <strong id="b842352706165234"><a name="b842352706165234"></a><a name="b842352706165234"></a>100</strong>.</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7999906"></a>

Request example

```
GET https://{SMN_Endpoint}/v2/{project_id}/notifications/topics?offset=0&limit=100
```

## Response<a name="section4890297"></a>

-   Parameter description

    <a name="table32894845"></a>
    <table><thead align="left"><tr id="row40748571"><th class="cellrowborder" valign="top" width="31.59%" id="mcps1.1.4.1.1"><p id="p12299945"><a name="p12299945"></a><a name="p12299945"></a><strong id="b1100369615"><a name="b1100369615"></a><a name="b1100369615"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.59%" id="mcps1.1.4.1.2"><p id="p56771492"><a name="p56771492"></a><a name="p56771492"></a><strong id="b1959114811"><a name="b1959114811"></a><a name="b1959114811"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.82%" id="mcps1.1.4.1.3"><p id="p35088115"><a name="p35088115"></a><a name="p35088115"></a><strong id="b1310872242"><a name="b1310872242"></a><a name="b1310872242"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29721263"><td class="cellrowborder" valign="top" width="31.59%" headers="mcps1.1.4.1.1 "><p id="p58612075"><a name="p58612075"></a><a name="p58612075"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.59%" headers="mcps1.1.4.1.2 "><p id="p49957660"><a name="p49957660"></a><a name="p49957660"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.82%" headers="mcps1.1.4.1.3 "><p id="p20038698"><a name="p20038698"></a><a name="p20038698"></a>Request ID, which is unique</p>
    </td>
    </tr>
    <tr id="row45587811"><td class="cellrowborder" valign="top" width="31.59%" headers="mcps1.1.4.1.1 "><p id="p1625174"><a name="p1625174"></a><a name="p1625174"></a>topic_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.59%" headers="mcps1.1.4.1.2 "><p id="p64530307"><a name="p64530307"></a><a name="p64530307"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.82%" headers="mcps1.1.4.1.3 "><p id="p59572368"><a name="p59572368"></a><a name="p59572368"></a>Number of topics in your account</p>
    <div class="note" id="note48698383125"><a name="note48698383125"></a><a name="note48698383125"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p452954191219"><a name="p452954191219"></a><a name="p452954191219"></a>No matter what offset and limit values you have set in the request, this parameter always returns the total number of topics.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row8821459"><td class="cellrowborder" valign="top" width="31.59%" headers="mcps1.1.4.1.1 "><p id="p43449544"><a name="p43449544"></a><a name="p43449544"></a>topics</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.59%" headers="mcps1.1.4.1.2 "><p id="p29752153"><a name="p29752153"></a><a name="p29752153"></a>Topic structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.82%" headers="mcps1.1.4.1.3 "><p id="p15409255121419"><a name="p15409255121419"></a><a name="p15409255121419"></a>Topic details</p>
    <p id="p61114224"><a name="p61114224"></a><a name="p61114224"></a>See <a href="#table10636317195533">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Topic structure

    <a name="table10636317195533"></a>
    <table><thead align="left"><tr id="row28583391195533"><th class="cellrowborder" valign="top" width="29.69%" id="mcps1.2.4.1.1"><p id="p33553343195533"><a name="p33553343195533"></a><a name="p33553343195533"></a><strong id="b15946175092320"><a name="b15946175092320"></a><a name="b15946175092320"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.050000000000004%" id="mcps1.2.4.1.2"><p id="p33466243195533"><a name="p33466243195533"></a><a name="p33466243195533"></a><strong id="b144700883"><a name="b144700883"></a><a name="b144700883"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.26%" id="mcps1.2.4.1.3"><p id="p26411156195533"><a name="p26411156195533"></a><a name="p26411156195533"></a><strong id="b2090916559234"><a name="b2090916559234"></a><a name="b2090916559234"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8508090195533"><td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.2.4.1.1 "><p id="p18066721195533"><a name="p18066721195533"></a><a name="p18066721195533"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p54118259195533"><a name="p54118259195533"></a><a name="p54118259195533"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.26%" headers="mcps1.2.4.1.3 "><p id="p21502874195533"><a name="p21502874195533"></a><a name="p21502874195533"></a>Resource identifier of a topic, which is unique</p>
    </td>
    </tr>
    <tr id="row39230450195533"><td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.2.4.1.1 "><p id="p23549883195533"><a name="p23549883195533"></a><a name="p23549883195533"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p28492405195533"><a name="p28492405195533"></a><a name="p28492405195533"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.26%" headers="mcps1.2.4.1.3 "><p id="p26183496195533"><a name="p26183496195533"></a><a name="p26183496195533"></a>Topic name</p>
    </td>
    </tr>
    <tr id="row28851380195533"><td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.2.4.1.1 "><p id="p55260426195533"><a name="p55260426195533"></a><a name="p55260426195533"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p46909558195533"><a name="p46909558195533"></a><a name="p46909558195533"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.26%" headers="mcps1.2.4.1.3 "><p id="p41577821195533"><a name="p41577821195533"></a><a name="p41577821195533"></a>Topic display name, which is presented as the name of the email sender in email messages</p>
    </td>
    </tr>
    <tr id="row44134393195533"><td class="cellrowborder" valign="top" width="29.69%" headers="mcps1.2.4.1.1 "><p id="p18116055195533"><a name="p18116055195533"></a><a name="p18116055195533"></a>push_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p58114317195533"><a name="p58114317195533"></a><a name="p58114317195533"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.26%" headers="mcps1.2.4.1.3 "><p id="p9639236195533"><a name="p9639236195533"></a><a name="p9639236195533"></a>Message push policy</p>
    <a name="ul10412105324519"></a><a name="ul10412105324519"></a><ul id="ul10412105324519"><li><strong id="b179312531221"><a name="b179312531221"></a><a name="b179312531221"></a>0</strong>: Failed messages will be saved in message queues.</li><li><strong id="b162877072614"><a name="b162877072614"></a><a name="b162877072614"></a>1</strong>: Failed messages will be discarded.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "request_id": "70bb40bef50e4a14b116a5a527fd7432", 
        "topic_count": 1, 
        "topics": [
            {
                "topic_urn": "urn:smn:regionId:8bad8a40e0f7462f8c1676e3f93a8183:test_topic_v2", 
                "display_name": "testtest", 
                "name": "test_topic_v1", 
                "push_policy": 0            
            }
        ]
    }
    ```


## Returned Value<a name="section44012677"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

