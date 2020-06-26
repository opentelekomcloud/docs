# Creating a Log Topic<a name="lts_02_0007"></a>

## Function<a name="section15294573"></a>

This function describes how to create a log topic under the created log group. You can view and query raw logs under a log topic.

## URI<a name="section3433433"></a>

-   URI format

    POST /v2.0/\{project\_id\}/log-groups/\{group\_id\}/log-topics


-   Parameter description

    **Table  1**  Parameter description

    <a name="table7695029"></a>
    <table><thead align="left"><tr id="row45779900"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p17184445"><a name="p17184445"></a><a name="p17184445"></a><strong id="b10725142516429"><a name="b10725142516429"></a><a name="b10725142516429"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="p49762843"><a name="p49762843"></a><a name="p49762843"></a><strong id="b27837266429"><a name="b27837266429"></a><a name="b27837266429"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="p4258493"><a name="p4258493"></a><a name="p4258493"></a><strong id="b5744132774212"><a name="b5744132774212"></a><a name="b5744132774212"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="p9393676"><a name="p9393676"></a><a name="p9393676"></a><strong id="b1260018287429"><a name="b1260018287429"></a><a name="b1260018287429"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22690287"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p25973967"><a name="p25973967"></a><a name="p25973967"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p23516563"><a name="p23516563"></a><a name="p23516563"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p25793444"><a name="p25793444"></a><a name="p25793444"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p8894185"><a name="p8894185"></a><a name="p8894185"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row12938802"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p41410081"><a name="p41410081"></a><a name="p41410081"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p65882297"><a name="p65882297"></a><a name="p65882297"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p34865825"><a name="p34865825"></a><a name="p34865825"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p5559553"><a name="p5559553"></a><a name="p5559553"></a>Specifies the ID of the created log group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section30900897"></a>

-   Request parameters

    **Table  2**  Parameter description

    <a name="table36118091"></a>
    <table><thead align="left"><tr id="row15629542"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p58033394"><a name="p58033394"></a><a name="p58033394"></a><strong id="b172971544164215"><a name="b172971544164215"></a><a name="b172971544164215"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p3084470"><a name="p3084470"></a><a name="p3084470"></a><strong id="b5113445204213"><a name="b5113445204213"></a><a name="b5113445204213"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p48515547"><a name="p48515547"></a><a name="p48515547"></a><strong id="b3117164694218"><a name="b3117164694218"></a><a name="b3117164694218"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p37445257"><a name="p37445257"></a><a name="p37445257"></a><strong id="b1680247144218"><a name="b1680247144218"></a><a name="b1680247144218"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13166951"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p59890077"><a name="p59890077"></a><a name="p59890077"></a>log_topic_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p19258068"><a name="p19258068"></a><a name="p19258068"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p16399667"><a name="p16399667"></a><a name="p16399667"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p53304675"><a name="p53304675"></a><a name="p53304675"></a>Specifies the log topic name.</p>
    <p id="ae7552ec5f29b4af9b0ceb23ca7befc5a"><a name="ae7552ec5f29b4af9b0ceb23ca7befc5a"></a><a name="ae7552ec5f29b4af9b0ceb23ca7befc5a"></a>The configuration rules are as follows:</p>
    <a name="ul16409171764511"></a><a name="ul16409171764511"></a><ul id="ul16409171764511"><li>Must be a string of 1 to 64 characters.</li><li>Only allows uppercase and lowercase letters, digits, special characters, underscores (_), hyphens (-), and periods (.). The name cannot start or end with a period.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST  
    /v2.0/{project_id}/log-groups/{group_id}/log-topics
    { 
    "log_topic_name":"testTopic01"
    }
    ```


## Response<a name="section9672624"></a>

-   Response parameters

    **Table  3**  Parameter description

    <a name="table51161625"></a>
    <table><thead align="left"><tr id="row50747809"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p16931828"><a name="p16931828"></a><a name="p16931828"></a><strong id="b20337741439"><a name="b20337741439"></a><a name="b20337741439"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p29300865"><a name="p29300865"></a><a name="p29300865"></a><strong id="b13520165194317"><a name="b13520165194317"></a><a name="b13520165194317"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="p24559854"><a name="p24559854"></a><a name="p24559854"></a><strong id="b952510604318"><a name="b952510604318"></a><a name="b952510604318"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43191139"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p8821385"><a name="p8821385"></a><a name="p8821385"></a>log_topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p43443591"><a name="p43443591"></a><a name="p43443591"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p29270022"><a name="p29270022"></a><a name="p29270022"></a>Specifies the log topic ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {  
       "log_topic_id":"a25d64c8-3028-11e9-9660-286ed488ce71"
    }
    ```


## Returned Value<a name="section19944758"></a>

-   Normal

    201

-   Abnormal

    For details about status code, see  [Status Code](status-code.md).


