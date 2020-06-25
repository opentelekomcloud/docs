# Responses \(Batch Operation\)<a name="EN-US_TOPIC_0142195139"></a>

The following responses are only for resetting the passwords for logging in to ECSs in batches and for modifying ECS specifications in a batch. For details about the responses of other batch operations, see  [Responses \(Task\)](responses-(task).md).

-   Normal responses

    <a name="table757167711151"></a>
    <table><thead align="left"><tr id="row5251903911151"><th class="cellrowborder" valign="top" width="19.3%" id="mcps1.1.4.1.1"><p id="p2618376611151"><a name="p2618376611151"></a><a name="p2618376611151"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.4.1.2"><p id="p4051029311151"><a name="p4051029311151"></a><a name="p4051029311151"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.23%" id="mcps1.1.4.1.3"><p id="p6010832511151"><a name="p6010832511151"></a><a name="p6010832511151"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3693617411151"><td class="cellrowborder" valign="top" width="19.3%" headers="mcps1.1.4.1.1 "><p id="p20542115442814"><a name="p20542115442814"></a><a name="p20542115442814"></a>response</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.4.1.2 "><p id="p813044011151"><a name="p813044011151"></a><a name="p813044011151"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.23%" headers="mcps1.1.4.1.3 "><p id="p5458589811151"><a name="p5458589811151"></a><a name="p5458589811151"></a>Specifies the response returned after a request is successfully submitted. For details, see <a href="#table849372311389">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **response**  field description

    <a name="table849372311389"></a>
    <table><thead align="left"><tr id="row149352343810"><th class="cellrowborder" valign="top" width="19.23%" id="mcps1.2.4.1.1"><p id="p750932333817"><a name="p750932333817"></a><a name="p750932333817"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.2"><p id="p155091823113810"><a name="p155091823113810"></a><a name="p155091823113810"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.35%" id="mcps1.2.4.1.3"><p id="p65095237388"><a name="p65095237388"></a><a name="p65095237388"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row650932316389"><td class="cellrowborder" valign="top" width="19.23%" headers="mcps1.2.4.1.1 "><p id="p4509182353818"><a name="p4509182353818"></a><a name="p4509182353818"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p7509723193816"><a name="p7509723193816"></a><a name="p7509723193816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35%" headers="mcps1.2.4.1.3 "><p id="p12509823153812"><a name="p12509823153812"></a><a name="p12509823153812"></a>Specifies the ID of the ECS on which the operation has been successfully performed.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal responses

    <a name="table6467239411151"></a>
    <table><thead align="left"><tr id="row2581079811151"><th class="cellrowborder" valign="top" width="19.18%" id="mcps1.1.4.1.1"><p id="p1029990211151"><a name="p1029990211151"></a><a name="p1029990211151"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.55%" id="mcps1.1.4.1.2"><p id="p2898571411151"><a name="p2898571411151"></a><a name="p2898571411151"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.27000000000001%" id="mcps1.1.4.1.3"><p id="p6614149111151"><a name="p6614149111151"></a><a name="p6614149111151"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5586052011151"><td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.1.4.1.1 "><p id="p146911628184218"><a name="p146911628184218"></a><a name="p146911628184218"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.1.4.1.2 "><p id="p1936686411151"><a name="p1936686411151"></a><a name="p1936686411151"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.27000000000001%" headers="mcps1.1.4.1.3 "><p id="p2558244011151"><a name="p2558244011151"></a><a name="p2558244011151"></a>Specifies the error in a batch request. For details, see <a href="#table6409189311151">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row133513134412"><td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.1.4.1.1 "><p id="p11335231184414"><a name="p11335231184414"></a><a name="p11335231184414"></a>internalError</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.1.4.1.2 "><p id="p173351331164413"><a name="p173351331164413"></a><a name="p173351331164413"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.27000000000001%" headers="mcps1.1.4.1.3 "><p id="p7335123118446"><a name="p7335123118446"></a><a name="p7335123118446"></a>Specifies the error in each request among the requests submitted in a batch. For details, see <a href="#table1540134517514">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **error**  field structure

    <a name="table6409189311151"></a>
    <table><thead align="left"><tr id="row2324327311151"><th class="cellrowborder" valign="top" width="19.23%" id="mcps1.2.4.1.1"><p id="p365693111151"><a name="p365693111151"></a><a name="p365693111151"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.2"><p id="p2777597711151"><a name="p2777597711151"></a><a name="p2777597711151"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.35%" id="mcps1.2.4.1.3"><p id="p3526170111151"><a name="p3526170111151"></a><a name="p3526170111151"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3762550011151"><td class="cellrowborder" valign="top" width="19.23%" headers="mcps1.2.4.1.1 "><p id="p2776668011151"><a name="p2776668011151"></a><a name="p2776668011151"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p3450864111151"><a name="p3450864111151"></a><a name="p3450864111151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35%" headers="mcps1.2.4.1.3 "><p id="p4373654211151"><a name="p4373654211151"></a><a name="p4373654211151"></a>Describes a batch operation error.</p>
    </td>
    </tr>
    <tr id="row5808456411151"><td class="cellrowborder" valign="top" width="19.23%" headers="mcps1.2.4.1.1 "><p id="p722924311151"><a name="p722924311151"></a><a name="p722924311151"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.2 "><p id="p4869780211151"><a name="p4869780211151"></a><a name="p4869780211151"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.35%" headers="mcps1.2.4.1.3 "><p id="p5220791411151"><a name="p5220791411151"></a><a name="p5220791411151"></a>Specifies the code for a batch operation error.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **internalEroCMM.0101r**  field description

    <a name="table1540134517514"></a>
    <table><thead align="left"><tr id="row164084513512"><th class="cellrowborder" valign="top" width="19.23%" id="mcps1.2.4.1.1"><p id="p440104565114"><a name="p440104565114"></a><a name="p440104565114"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.2"><p id="p440104513519"><a name="p440104513519"></a><a name="p440104513519"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.17%" id="mcps1.2.4.1.3"><p id="p35584555110"><a name="p35584555110"></a><a name="p35584555110"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row432344514579"><td class="cellrowborder" valign="top" width="19.23%" headers="mcps1.2.4.1.1 "><p id="p6323194545719"><a name="p6323194545719"></a><a name="p6323194545719"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.2 "><p id="p932314459576"><a name="p932314459576"></a><a name="p932314459576"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.17%" headers="mcps1.2.4.1.3 "><p id="p63238459570"><a name="p63238459570"></a><a name="p63238459570"></a>Specifies the ID of the ECS on which a request failed.</p>
    </td>
    </tr>
    <tr id="row1455154516515"><td class="cellrowborder" valign="top" width="19.23%" headers="mcps1.2.4.1.1 "><p id="p25544513512"><a name="p25544513512"></a><a name="p25544513512"></a>error_message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.2 "><p id="p10559459511"><a name="p10559459511"></a><a name="p10559459511"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.17%" headers="mcps1.2.4.1.3 "><p id="p955174512511"><a name="p955174512511"></a><a name="p955174512511"></a>Describes a single request failure.</p>
    </td>
    </tr>
    <tr id="row165514450511"><td class="cellrowborder" valign="top" width="19.23%" headers="mcps1.2.4.1.1 "><p id="p491643915115"><a name="p491643915115"></a><a name="p491643915115"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.2 "><p id="p165574575119"><a name="p165574575119"></a><a name="p165574575119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.17%" headers="mcps1.2.4.1.3 "><p id="p15551545135117"><a name="p15551545135117"></a><a name="p15551545135117"></a>Specifies the code for a single request error.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    Normal response

    ```
    { 
        "response": [
                      {
                        "id": "616fb98f-46ca-475e-917e-2563e5a8cd19"   
                      },
                      {
                        "id": "516fb98f-46ca-475e-917e-2563e5a8cd12"   
                      }
                   ]
    } 
    ```

    Abnormal response

    ```
    {
         "error": {
                     "code": "Ecs.xxxx",
                     "message": "xxxxxxxxxxxxxxx" 
                   },
         "internalError": [
                     {
                        "id": "616fb98f-46ca-475e-917e-2563e5a8cd19",
                        "error_code": "ECS.XXXX",
                        "error_message": "xxxxxxxxxxxxxxx" 
                      },
                     {
                         "id": "516fb98f-46ca-475e-917e-2563e5a8cd12",
                         "error_code": "ECS.XXXX",
                         "error_message": "xxxxxxxxxxxxxxx" 
                     }
                  ]
    }
    ```


