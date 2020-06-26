# Modifying a Parameter Template<a name="rds_09_0303"></a>

## Function<a name="section29151894373"></a>

This API is used to modify a specified parameter template, including the name, description, and values of specified parameters in the parameter template.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section13115202083319"></a>

-   The following DB engines are supported: MySQL, PostgreSQL, and Microsoft SQL Server.
-   For Microsoft SQL Server, only the following editions are supported: Microsoft SQL Server 2014 SE, 2016 SE, and 2016 EE.

-   The modified parameter template name must be different from the name of an existing or a default parameter template. Default parameter templates cannot be modified.
-   The values of the edited parameters must be within the default value range of the specified database version. For details about the range of parameter values, see the "Modifying Parameters in a Parameter Template" section in the  _Relational Database Service User Guide_.
-   The parameter values to be changed cannot be left blank at the same time.

## URI<a name="section159150933715"></a>

-   URI format

    PUT https://\{_Endpoint_\}/v3/\{_project\_id_\}/configurations/\{config\_id\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/configurations/463b4b58-d0e8-4e2b-9560-5dea4552fde9

-   Parameter description

    **Table  1**  Parameter description

    <a name="table89151953717"></a>
    <table><thead align="left"><tr id="row7165910143717"><th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.1"><p id="p11165161023714"><a name="p11165161023714"></a><a name="p11165161023714"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.799999999999997%" id="mcps1.2.4.1.2"><p id="p12165121083718"><a name="p12165121083718"></a><a name="p12165121083718"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.99%" id="mcps1.2.4.1.3"><p id="p11651110153712"><a name="p11651110153712"></a><a name="p11651110153712"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17165610153712"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p1416591073710"><a name="p1416591073710"></a><a name="p1416591073710"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.799999999999997%" headers="mcps1.2.4.1.2 "><p id="p31651810143710"><a name="p31651810143710"></a><a name="p31651810143710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p3165191063718"><a name="p3165191063718"></a><a name="p3165191063718"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p128929918610"><a name="p128929918610"></a><a name="p128929918610"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row1316571063716"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p1316511033710"><a name="p1316511033710"></a><a name="p1316511033710"></a>config_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.799999999999997%" headers="mcps1.2.4.1.2 "><p id="p1216561017374"><a name="p1216561017374"></a><a name="p1216561017374"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.2.4.1.3 "><p id="p816561014375"><a name="p816561014375"></a><a name="p816561014375"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section149462918370"></a>

-   Parameter description

    >![](/images/icon-notice.gif) **NOTICE:**   
    >At least one parameter in the request body must be specified. Otherwise, the request fails to be delivered.  

    **Table  2**  Parameter description

    <a name="table9962179113713"></a>
    <table><thead align="left"><tr id="row15165121013712"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p616541017372"><a name="p616541017372"></a><a name="p616541017372"></a><strong id="b1749898624"><a name="b1749898624"></a><a name="b1749898624"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.42%" id="mcps1.2.5.1.2"><p id="p15165310143717"><a name="p15165310143717"></a><a name="p15165310143717"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85%" id="mcps1.2.5.1.3"><p id="p316517107374"><a name="p316517107374"></a><a name="p316517107374"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.730000000000004%" id="mcps1.2.5.1.4"><p id="p19165161013720"><a name="p19165161013720"></a><a name="p19165161013720"></a><strong id="b2057993526"><a name="b2057993526"></a><a name="b2057993526"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1516517104373"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p1116561017377"><a name="p1116561017377"></a><a name="p1116561017377"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.42%" headers="mcps1.2.5.1.2 "><p id="p8165191093712"><a name="p8165191093712"></a><a name="p8165191093712"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.5.1.3 "><p id="p1216591012371"><a name="p1216591012371"></a><a name="p1216591012371"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p9165131016374"><a name="p9165131016374"></a><a name="p9165131016374"></a>Specifies the parameter template name. It contains a maximum of 64 characters and can contain only uppercase letters, lowercase letters, digits, hyphens (-), underscores (_), and periods (.).</p>
    </td>
    </tr>
    <tr id="row21651010133713"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p141651310153712"><a name="p141651310153712"></a><a name="p141651310153712"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.42%" headers="mcps1.2.5.1.2 "><p id="p171658107371"><a name="p171658107371"></a><a name="p171658107371"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.5.1.3 "><p id="p41651010183710"><a name="p41651010183710"></a><a name="p41651010183710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p1416513103374"><a name="p1416513103374"></a><a name="p1416513103374"></a>Specifies the parameter template description. It contains a maximum of 256 characters and does not support the following special characters: !&lt;&gt;='&amp;" Its value is left blank by default.</p>
    </td>
    </tr>
    <tr id="row111655104371"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p21658108374"><a name="p21658108374"></a><a name="p21658108374"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.42%" headers="mcps1.2.5.1.2 "><p id="p416513109372"><a name="p416513109372"></a><a name="p416513109372"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.5.1.3 "><p id="p6301203614332"><a name="p6301203614332"></a><a name="p6301203614332"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p181657107373"><a name="p181657107373"></a><a name="p181657107373"></a>Specifies the parameter values defined by users based on the default parameter template. If this parameter is left blank, the parameter value cannot be changed.</p>
    <p id="p17486537123010"><a name="p17486537123010"></a><a name="p17486537123010"></a>For details, see <a href="#table597813911376">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  values field data structure description

    <a name="table597813911376"></a>
    <table><thead align="left"><tr id="row016541014373"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.5.1.1"><p id="p8165171013375"><a name="p8165171013375"></a><a name="p8165171013375"></a><strong id="b1850466727"><a name="b1850466727"></a><a name="b1850466727"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.500000000000004%" id="mcps1.2.5.1.2"><p id="p13165141083710"><a name="p13165141083710"></a><a name="p13165141083710"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.040000000000001%" id="mcps1.2.5.1.3"><p id="p7165131053713"><a name="p7165131053713"></a><a name="p7165131053713"></a><strong id="b1074221853"><a name="b1074221853"></a><a name="b1074221853"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.730000000000004%" id="mcps1.2.5.1.4"><p id="p20165151033710"><a name="p20165151033710"></a><a name="p20165151033710"></a><strong id="b1686454813"><a name="b1686454813"></a><a name="b1686454813"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row516501010377"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.5.1.1 "><p id="p151651710153718"><a name="p151651710153718"></a><a name="p151651710153718"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.500000000000004%" headers="mcps1.2.5.1.2 "><p id="p141651010113713"><a name="p141651010113713"></a><a name="p141651010113713"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p1516541073715"><a name="p1516541073715"></a><a name="p1516541073715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p13165710113715"><a name="p13165710113715"></a><a name="p13165710113715"></a>Specifies the parameter name. For example, in <strong id="b84235270621563"><a name="b84235270621563"></a><a name="b84235270621563"></a>"max_connections": "10"</strong>, the key is <strong id="b842352706215241"><a name="b842352706215241"></a><a name="b842352706215241"></a>max_connections</strong>. If <strong id="b842352706175014"><a name="b842352706175014"></a><a name="b842352706175014"></a>key</strong> is not empty, the parameter <strong id="b842352706175018"><a name="b842352706175018"></a><a name="b842352706175018"></a>value</strong> cannot be empty, either.</p>
    </td>
    </tr>
    <tr id="row116541017376"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.5.1.1 "><p id="p1916591012374"><a name="p1916591012374"></a><a name="p1916591012374"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.500000000000004%" headers="mcps1.2.5.1.2 "><p id="p21652108377"><a name="p21652108377"></a><a name="p21652108377"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.2.5.1.3 "><p id="p516531003715"><a name="p516531003715"></a><a name="p516531003715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p11165610133717"><a name="p11165610133717"></a><a name="p11165610133717"></a>Specifies the parameter value. For example, in <strong id="b953814020215624"><a name="b953814020215624"></a><a name="b953814020215624"></a>"max_connections": "10"</strong>, the value is <strong id="b842352706215633"><a name="b842352706215633"></a><a name="b842352706215633"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    { 
        "name": "configuration_test", 
        "description": "configuration_test", 
        "values": { 
           "max_connections": "10", 
           "autocommit": "OFF" 
        } 
    }
    ```


## Response<a name="section499319173712"></a>

-   Normal response

    None

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

