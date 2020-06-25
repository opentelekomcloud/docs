# Changing DB Instance Specifications<a name="en-us_topic_0056890050"></a>

## Function<a name="section31046129101956"></a>

This API is used to change DB instance specifications.

>![](/images/icon-notice.gif) **NOTICE:**   
>Services will be interrupted for 5 to 10 minutes when you change DB instance specifications. Exercise caution when performing this operation.  

## URI<a name="section16941204101956"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/instances/\{instanceId\}/action

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table1491724101956"></a>
    <table><thead align="left"><tr id="row58880760101956"><th class="cellrowborder" valign="top" width="21.61%" id="mcps1.2.4.1.1"><p id="p4612244101956"><a name="p4612244101956"></a><a name="p4612244101956"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.01%" id="mcps1.2.4.1.2"><p id="p38047444101956"><a name="p38047444101956"></a><a name="p38047444101956"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.38%" id="mcps1.2.4.1.3"><p id="p61944096101956"><a name="p61944096101956"></a><a name="p61944096101956"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51415905101956"><td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.2.4.1.1 "><p id="p3938815101956"><a name="p3938815101956"></a><a name="p3938815101956"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.4.1.2 "><p id="p50608609101956"><a name="p50608609101956"></a><a name="p50608609101956"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.38%" headers="mcps1.2.4.1.3 "><p id="p5656688101956"><a name="p5656688101956"></a><a name="p5656688101956"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row50910195101956"><td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.2.4.1.1 "><p id="p30085168101956"><a name="p30085168101956"></a><a name="p30085168101956"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.01%" headers="mcps1.2.4.1.2 "><p id="p20979533101956"><a name="p20979533101956"></a><a name="p20979533101956"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.38%" headers="mcps1.2.4.1.3 "><p id="p21620594101956"><a name="p21620594101956"></a><a name="p21620594101956"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions
    1.  The new specifications cannot be the same as the original specifications.
    2.  The instance class can be modified only for DB instances whose status is  **Available**.
    3.  Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section19724157101956"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table24309628101956"></a>
    <table><thead align="left"><tr id="row53446469101956"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p34196722101956"><a name="p34196722101956"></a><a name="p34196722101956"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.4.1.2"><p id="p18471079101956"><a name="p18471079101956"></a><a name="p18471079101956"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p19762445101956"><a name="p19762445101956"></a><a name="p19762445101956"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57254219101956"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p7080202101956"><a name="p7080202101956"></a><a name="p7080202101956"></a>resize</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.2 "><p id="p36625522101956"><a name="p36625522101956"></a><a name="p36625522101956"></a>Dictionary data structure. For details, see <a href="#table50214959101956">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p57786747101956"><a name="p57786747101956"></a><a name="p57786747101956"></a>Specifies the information about the returned parameter <strong id="b842352706113940"><a name="b842352706113940"></a><a name="b842352706113940"></a>flavorRef</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  resize field data structure description

    <a name="table50214959101956"></a>
    <table><thead align="left"><tr id="row10175857101956"><th class="cellrowborder" valign="top" width="24.872487248724873%" id="mcps1.2.4.1.1"><p id="p18938068101956"><a name="p18938068101956"></a><a name="p18938068101956"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.7941794179418%" id="mcps1.2.4.1.2"><p id="p57588511101956"><a name="p57588511101956"></a><a name="p57588511101956"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p34157819101956"><a name="p34157819101956"></a><a name="p34157819101956"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15319951101956"><td class="cellrowborder" valign="top" width="24.872487248724873%" headers="mcps1.2.4.1.1 "><p id="p32956548101956"><a name="p32956548101956"></a><a name="p32956548101956"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.7941794179418%" headers="mcps1.2.4.1.2 "><p id="p52234754101956"><a name="p52234754101956"></a><a name="p52234754101956"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3156656101956"><a name="p3156656101956"></a><a name="p3156656101956"></a>Specifies the specification ID (<strong id="b84235270617142"><a name="b84235270617142"></a><a name="b84235270617142"></a>flavors.str_id</strong> in the response message in <a href="obtaining-all-db-instance-specifications-18.md">Obtaining All DB Instance Specifications</a>).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    { 
        "resize":{ 
            "flavorRef":"0d922098-553c-4123-80df-e627a1d41a0d" 
        } 
    }
    ```


## Normal Response<a name="section36069544101956"></a>

None

## Abnormal Response<a name="section26427218101956"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

