# Deleting a DB Instance<a name="dds_api_0022"></a>

## Function<a name="section29874939"></a>

This API is used to delete a DB instance.

## URI<a name="section439002"></a>

-   URI format

    DELETE /v3/\{project\_id\}/instances/\{instance\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4508766"></a>
    <table><thead align="left"><tr id="row21306406"><th class="cellrowborder" valign="top" width="22.05%" id="mcps1.2.4.1.1"><p id="p48097351"><a name="p48097351"></a><a name="p48097351"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.2"><p id="p3571397"><a name="p3571397"></a><a name="p3571397"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.88%" id="mcps1.2.4.1.3"><p id="p2775334615440"><a name="p2775334615440"></a><a name="p2775334615440"></a><strong id="b1211711271793"><a name="b1211711271793"></a><a name="b1211711271793"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10946294"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p14234617"><a name="p14234617"></a><a name="p14234617"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p12153337"><a name="p12153337"></a><a name="p12153337"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p19338596163746"><a name="p19338596163746"></a><a name="p19338596163746"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row1412808"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p47328638"><a name="p47328638"></a><a name="p47328638"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p8414476"><a name="p8414476"></a><a name="p8414476"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p10483995"><a name="p10483995"></a><a name="p10483995"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="section3951024"></a>

-   Request header

    ```
    DELETE https://DDS endpoint/v3/{project_id}/instances/{instance_id}
    ```

-   Request body

    N/A


## Responses<a name="section35559222"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table29807226151454"></a>
    <table><thead align="left"><tr id="row3223123151454"><th class="cellrowborder" valign="top" width="24.122412241224122%" id="mcps1.2.4.1.1"><p id="p59746450151454"><a name="p59746450151454"></a><a name="p59746450151454"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.544254425442546%" id="mcps1.2.4.1.2"><p id="p7624314151454"><a name="p7624314151454"></a><a name="p7624314151454"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p125849352116"><a name="p125849352116"></a><a name="p125849352116"></a><strong id="b83503302093"><a name="b83503302093"></a><a name="b83503302093"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19231203392012"><td class="cellrowborder" valign="top" width="24.122412241224122%" headers="mcps1.2.4.1.1 "><p id="p417012163212"><a name="p417012163212"></a><a name="p417012163212"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.544254425442546%" headers="mcps1.2.4.1.2 "><p id="p317018169216"><a name="p317018169216"></a><a name="p317018169216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1017071652111"><a name="p1017071652111"></a><a name="p1017071652111"></a>Indicates the workflow ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
          "job_id": "252f11f1-2912-4c06-be55-1999bde659c5"
    }
    ```


## **Status Code**<a name="section5382712154838"></a>

For more information, see  [Status Code](status-code.md).

## Error Code<a name="section6522193710339"></a>

For more information, see  [Error Code](error-code.md).

