# Querying the Quota<a name="vpcep_06_0401"></a>

## Function<a name="section547312521673"></a>

This API is used to query the quota of your resources, including VPC endpoint services and VPC endpoints.

## URI<a name="section1347915523719"></a>

GET /v1/\{project\_id\}/quotas?type=\{resource\_type\}

[Table 1](#table1148411527716)  describes the required parameters.

**Table  1**  Parameters

<a name="table1148411527716"></a>
<table><thead align="left"><tr id="row106548523719"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p136545529718"><a name="p136545529718"></a><a name="p136545529718"></a><strong id="b108861620114"><a name="b108861620114"></a><a name="b108861620114"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p06542521472"><a name="p06542521472"></a><a name="p06542521472"></a><strong id="b1544441416111"><a name="b1544441416111"></a><a name="b1544441416111"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p116545521373"><a name="p116545521373"></a><a name="p116545521373"></a><strong id="b7342115131116"><a name="b7342115131116"></a><a name="b7342115131116"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1765475213713"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p12654552071"><a name="p12654552071"></a><a name="p12654552071"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p126547522077"><a name="p126547522077"></a><a name="p126547522077"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p1865418520717"><a name="p1865418520717"></a><a name="p1865418520717"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section104962522074"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table5505175211710"></a>
    <table><thead align="left"><tr id="row1665510521073"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.5.1.1"><p id="p196553528716"><a name="p196553528716"></a><a name="p196553528716"></a><strong id="b84841522161119"><a name="b84841522161119"></a><a name="b84841522161119"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p565513525720"><a name="p565513525720"></a><a name="p565513525720"></a><strong id="b1290416015"><a name="b1290416015"></a><a name="b1290416015"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p1565535214710"><a name="p1565535214710"></a><a name="p1565535214710"></a><strong id="b366412469114"><a name="b366412469114"></a><a name="b366412469114"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p14655165220712"><a name="p14655165220712"></a><a name="p14655165220712"></a><strong id="b1289779380"><a name="b1289779380"></a><a name="b1289779380"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row765515219718"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="p136557522711"><a name="p136557522711"></a><a name="p136557522711"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p1865517522716"><a name="p1865517522716"></a><a name="p1865517522716"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p0655115210718"><a name="p0655115210718"></a><a name="p0655115210718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p32561544163216"><a name="p32561544163216"></a><a name="p32561544163216"></a>Specifies the resource type.</p>
    <a name="ul17816144515482"></a><a name="ul17816144515482"></a><ul id="ul17816144515482"><li><strong id="b395219817292"><a name="b395219817292"></a><a name="b395219817292"></a>endpoint_service</strong>: indicates the VPC endpoint service.</li><li><strong id="b20678830113112"><a name="b20678830113112"></a><a name="b20678830113112"></a>endpoint</strong>: indicates the VPC endpoint.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    This request is to query the quota of VPC endpoint services.

    ```
    GET https://{endpoint}/v1/{project_id}/quotas?type=endpoint_service
    ```


## Response<a name="section115113521171"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="en-us_topic_0130978821_table62266580"></a>
    <table><thead align="left"><tr id="en-us_topic_0130978821_row18576134"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="en-us_topic_0130978821_p28271860"><a name="en-us_topic_0130978821_p28271860"></a><a name="en-us_topic_0130978821_p28271860"></a><strong id="b79351534181412"><a name="b79351534181412"></a><a name="b79351534181412"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.042204220422043%" id="mcps1.2.4.1.2"><p id="en-us_topic_0130978821_p8319290"><a name="en-us_topic_0130978821_p8319290"></a><a name="en-us_topic_0130978821_p8319290"></a><strong id="b3616184815332"><a name="b3616184815332"></a><a name="b3616184815332"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.71537153715372%" id="mcps1.2.4.1.3"><p id="en-us_topic_0130978821_p2773889"><a name="en-us_topic_0130978821_p2773889"></a><a name="en-us_topic_0130978821_p2773889"></a><strong id="b446933517136"><a name="b446933517136"></a><a name="b446933517136"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0130978821_row23358448"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p6963371876"><a name="p6963371876"></a><a name="p6963371876"></a>quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.042204220422043%" headers="mcps1.2.4.1.2 "><p id="p155105916445"><a name="p155105916445"></a><a name="p155105916445"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.71537153715372%" headers="mcps1.2.4.1.3 "><p id="p144861542444"><a name="p144861542444"></a><a name="p144861542444"></a>Specifies quota details. For details, see <a href="#table862171544417">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **Quotas**  parameters

    <a name="table862171544417"></a>
    <table><thead align="left"><tr id="row166213152440"><th class="cellrowborder" valign="top" width="24.29%" id="mcps1.2.4.1.1"><p id="p9612150445"><a name="p9612150445"></a><a name="p9612150445"></a><strong id="b12368161453414"><a name="b12368161453414"></a><a name="b12368161453414"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.259999999999998%" id="mcps1.2.4.1.2"><p id="p9611315194419"><a name="p9611315194419"></a><a name="p9611315194419"></a><strong id="b1394346333"><a name="b1394346333"></a><a name="b1394346333"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.449999999999996%" id="mcps1.2.4.1.3"><p id="p1962151512445"><a name="p1962151512445"></a><a name="p1962151512445"></a><strong id="b1409154957"><a name="b1409154957"></a><a name="b1409154957"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4621115144412"><td class="cellrowborder" valign="top" width="24.29%" headers="mcps1.2.4.1.1 "><p id="p15621015164415"><a name="p15621015164415"></a><a name="p15621015164415"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.259999999999998%" headers="mcps1.2.4.1.2 "><p id="p19621315194411"><a name="p19621315194411"></a><a name="p19621315194411"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p1620155448"><a name="p1620155448"></a><a name="p1620155448"></a>Lists the resources. For details, see <a href="#table1170141514413">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Resource parameters

    <a name="table1170141514413"></a>
    <table><thead align="left"><tr id="row11691153447"><th class="cellrowborder" valign="top" width="24.387561243875613%" id="mcps1.2.4.1.1"><p id="p1162115184419"><a name="p1162115184419"></a><a name="p1162115184419"></a><strong id="b1361633673414"><a name="b1361633673414"></a><a name="b1361633673414"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.187781221877813%" id="mcps1.2.4.1.2"><p id="p136241520441"><a name="p136241520441"></a><a name="p136241520441"></a><strong id="b882535991"><a name="b882535991"></a><a name="b882535991"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.42465753424658%" id="mcps1.2.4.1.3"><p id="p106919154440"><a name="p106919154440"></a><a name="p106919154440"></a><strong id="b1797821552"><a name="b1797821552"></a><a name="b1797821552"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row107041515449"><td class="cellrowborder" valign="top" width="24.387561243875613%" headers="mcps1.2.4.1.1 "><p id="p1969915164416"><a name="p1969915164416"></a><a name="p1969915164416"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.187781221877813%" headers="mcps1.2.4.1.2 "><p id="p1770121584417"><a name="p1770121584417"></a><a name="p1770121584417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.42465753424658%" headers="mcps1.2.4.1.3 "><p id="p1870191515441"><a name="p1870191515441"></a><a name="p1870191515441"></a>Specifies the resource type. You can query the quota of resources of a specified type by configuring this parameter.</p>
    <a name="ul157041517444"></a><a name="ul157041517444"></a><ul id="ul157041517444"><li><strong id="b3630122113520"><a name="b3630122113520"></a><a name="b3630122113520"></a>endpoint_service</strong>: indicates the VPC endpoint service.</li><li><strong id="b177410244356"><a name="b177410244356"></a><a name="b177410244356"></a>endpoint</strong>: indicates the VPC endpoint.</li></ul>
    </td>
    </tr>
    <tr id="row8701815124418"><td class="cellrowborder" valign="top" width="24.387561243875613%" headers="mcps1.2.4.1.1 "><p id="p19704157441"><a name="p19704157441"></a><a name="p19704157441"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.187781221877813%" headers="mcps1.2.4.1.2 "><p id="p070191524412"><a name="p070191524412"></a><a name="p070191524412"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.42465753424658%" headers="mcps1.2.4.1.3 "><p id="p157016155448"><a name="p157016155448"></a><a name="p157016155448"></a>Specifies the number of created resources.</p>
    <p id="p167091564419"><a name="p167091564419"></a><a name="p167091564419"></a>The value ranges from <strong id="b1407708997192551"><a name="b1407708997192551"></a><a name="b1407708997192551"></a>0</strong> to the value of <strong id="b637466560192551"><a name="b637466560192551"></a><a name="b637466560192551"></a>quota</strong>.</p>
    </td>
    </tr>
    <tr id="row370101512448"><td class="cellrowborder" valign="top" width="24.387561243875613%" headers="mcps1.2.4.1.1 "><p id="p1470111594414"><a name="p1470111594414"></a><a name="p1470111594414"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.187781221877813%" headers="mcps1.2.4.1.2 "><p id="p8704154444"><a name="p8704154444"></a><a name="p8704154444"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.42465753424658%" headers="mcps1.2.4.1.3 "><p id="p117041510446"><a name="p117041510446"></a><a name="p117041510446"></a>Specifies the maximum quota of resources.</p>
    <p id="p147012155448"><a name="p147012155448"></a><a name="p147012155448"></a>The value ranges from the default quota value to the maximum quota value.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
    "quotas":{
         "resources":[
                     {
                         "type":"endpoint",
                         "used":4,
                         "quota":150
                    },
                     {
                         "type":"endpoint_service",
                         "used":10,
                         "quota": 100
                    }
                  ]
            }
    }
    ```


## Status Code<a name="section135401523718"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

