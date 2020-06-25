# Deleting a Resource Tag<a name="dws_02_0051"></a>

## Function<a name="section14911175173418"></a>

This API is used to delete a resource tag for a resource.

## URI<a name="section99116593419"></a>

-   URI format

    DELETE /v1.0/\{project\_id\}/clusters/\{resource\_id\}/tags/\{key\}


-   Parameter description

    **Table  1**  URI parameter description

    <a name="table59188517349"></a>
    <table><thead align="left"><tr id="row4995115113419"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.1"><p id="p399514583415"><a name="p399514583415"></a><a name="p399514583415"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.2"><p id="p9995554349"><a name="p9995554349"></a><a name="p9995554349"></a><strong id="b84235270684256"><a name="b84235270684256"></a><a name="b84235270684256"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.5.1.3"><p id="p10995195113417"><a name="p10995195113417"></a><a name="p10995195113417"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="59.4059405940594%" id="mcps1.2.5.1.4"><p id="p69958513349"><a name="p69958513349"></a><a name="p69958513349"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1899518515340"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p499735173412"><a name="p499735173412"></a><a name="p499735173412"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="p9997754345"><a name="p9997754345"></a><a name="p9997754345"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="p2997125193411"><a name="p2997125193411"></a><a name="p2997125193411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.5.1.4 "><p id="p11997257345"><a name="p11997257345"></a><a name="p11997257345"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row18997135123413"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p6997650347"><a name="p6997650347"></a><a name="p6997650347"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="p12997205143417"><a name="p12997205143417"></a><a name="p12997205143417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="p1699785203415"><a name="p1699785203415"></a><a name="p1699785203415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.5.1.4 "><p id="p99976514345"><a name="p99976514345"></a><a name="p99976514345"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row299715593419"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p139973515341"><a name="p139973515341"></a><a name="p139973515341"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="p139974593413"><a name="p139974593413"></a><a name="p139974593413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="p999719518344"><a name="p999719518344"></a><a name="p999719518344"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.5.1.4 "><p id="p1199716517344"><a name="p1199716517344"></a><a name="p1199716517344"></a>Tag key</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section493018513415"></a>

-   Sample request

    ```
    DELETE /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/7d85f602-a948-4a30-afd4-e84f47471c15/tags/DEV
    ```

-   Parameter description

    None


## Response<a name="section1267862233212"></a>

Sample response

```
STATUS CODE 204
```

## Returned Value<a name="section119321759349"></a>

-   Normal

    204

-   Abnormal

    **Table  2**  Returned value for failed requests

    <a name="table793510518343"></a>
    <table><thead align="left"><tr id="row15997256340"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p79971958343"><a name="p79971958343"></a><a name="p79971958343"></a><strong id="b84235270615436"><a name="b84235270615436"></a><a name="b84235270615436"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p599715583418"><a name="p599715583418"></a><a name="p599715583418"></a><strong id="b465196551"><a name="b465196551"></a><a name="b465196551"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row199976593411"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p1999715518341"><a name="p1999715518341"></a><a name="p1999715518341"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p599716513347"><a name="p599716513347"></a><a name="p599716513347"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row16997155113419"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p109970523413"><a name="p109970523413"></a><a name="p109970523413"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p699715103413"><a name="p699715103413"></a><a name="p699715103413"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row199714583412"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p129971158344"><a name="p129971158344"></a><a name="p129971158344"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p89976518342"><a name="p89976518342"></a><a name="p89976518342"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row799735153417"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p1599710573417"><a name="p1599710573417"></a><a name="p1599710573417"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p2997175133418"><a name="p2997175133418"></a><a name="p2997175133418"></a>The requested resource was not found or the key does not exist.</p>
    </td>
    </tr>
    <tr id="row9997155103420"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p899715593413"><a name="p899715593413"></a><a name="p899715593413"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p49977533419"><a name="p49977533419"></a><a name="p49977533419"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


