# Deleting a Resource Tag<a name="smn_api_56004"></a>

## Description<a name="section7759134242010"></a>

-   API name

    DeleteResourceTag


-   Function

    The API is idempotent. When deleting a tag, the system does not check its character set. The tag key cannot be left blank or be an empty string. If the key of the tag to be deleted does not exist, 404 will be returned. 


## URI<a name="section97591842102016"></a>

-   URI format

    DELETE /v2/\{project\_id\}/\{resource\_type\}/\{resource\_id\}/tags/\{key\}


-   Parameter description

    <a name="table7791104212204"></a>
    <table><thead align="left"><tr id="row1796344252017"><th class="cellrowborder" valign="top" width="26.39%" id="mcps1.1.5.1.1"><p id="p79631442192013"><a name="p79631442192013"></a><a name="p79631442192013"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.61%" id="mcps1.1.5.1.2"><p id="p10963442162017"><a name="p10963442162017"></a><a name="p10963442162017"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.830000000000002%" id="mcps1.1.5.1.3"><p id="p1963124212201"><a name="p1963124212201"></a><a name="p1963124212201"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.17%" id="mcps1.1.5.1.4"><p id="p196304213203"><a name="p196304213203"></a><a name="p196304213203"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19963842192019"><td class="cellrowborder" valign="top" width="26.39%" headers="mcps1.1.5.1.1 "><p id="p49631428205"><a name="p49631428205"></a><a name="p49631428205"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.61%" headers="mcps1.1.5.1.2 "><p id="p10963742172017"><a name="p10963742172017"></a><a name="p10963742172017"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.1.5.1.3 "><p id="p109639429204"><a name="p109639429204"></a><a name="p109639429204"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.17%" headers="mcps1.1.5.1.4 "><p id="p11963154216205"><a name="p11963154216205"></a><a name="p11963154216205"></a>Project ID</p>
    <p id="p118812918506"><a name="p118812918506"></a><a name="p118812918506"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row20963154222018"><td class="cellrowborder" valign="top" width="26.39%" headers="mcps1.1.5.1.1 "><p id="p99531421797"><a name="p99531421797"></a><a name="p99531421797"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.61%" headers="mcps1.1.5.1.2 "><p id="p1495310421799"><a name="p1495310421799"></a><a name="p1495310421799"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.1.5.1.3 "><p id="p149531342296"><a name="p149531342296"></a><a name="p149531342296"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.17%" headers="mcps1.1.5.1.4 "><p id="p52661238184213"><a name="p52661238184213"></a><a name="p52661238184213"></a>Resource type</p>
    <p id="p278251314214"><a name="p278251314214"></a><a name="p278251314214"></a>The value can be the following:</p>
    <p id="p14550953686"><a name="p14550953686"></a><a name="p14550953686"></a><strong id="b06956914163"><a name="b06956914163"></a><a name="b06956914163"></a>smn_topic</strong>: topic</p>
    <p id="p8682201993"><a name="p8682201993"></a><a name="p8682201993"></a></p>
    <p id="p13305168121110"><a name="p13305168121110"></a><a name="p13305168121110"></a></p>
    </td>
    </tr>
    <tr id="row1396310428206"><td class="cellrowborder" valign="top" width="26.39%" headers="mcps1.1.5.1.1 "><p id="p1363485413187"><a name="p1363485413187"></a><a name="p1363485413187"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.61%" headers="mcps1.1.5.1.2 "><p id="p463417547182"><a name="p463417547182"></a><a name="p463417547182"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.830000000000002%" headers="mcps1.1.5.1.3 "><p id="p7634195417180"><a name="p7634195417180"></a><a name="p7634195417180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.17%" headers="mcps1.1.5.1.4 "><p id="p176341254201810"><a name="p176341254201810"></a><a name="p176341254201810"></a>Resource ID</p>
    <p id="p57491711103514"><a name="p57491711103514"></a><a name="p57491711103514"></a>Obtain a resource ID:</p>
    <a name="ul111761720155610"></a><a name="ul111761720155610"></a><ul id="ul111761720155610"><li>Add <strong id="smn_api_56002_b1046628401"><a name="smn_api_56002_b1046628401"></a><a name="smn_api_56002_b1046628401"></a>X-SMN-RESOURCEID-TYPE=name</strong> in the request header and set the resource ID to the topic name.</li><li>Call the <strong id="smn_api_56002_b84235270694340"><a name="smn_api_56002_b84235270694340"></a><a name="smn_api_56002_b84235270694340"></a>GetResourceInstances</strong> API to obtain the resource ID.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section882210424202"></a>

-   Request example

    ```
    DELETE https://{SMN_Endpoint}/v2/{project_id}/{resource_type}/{resource_id}/tags/{key}
    ```


## Response<a name="section7917112413357"></a>

None

## Returned Value<a name="section8822184216209"></a>

See  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

