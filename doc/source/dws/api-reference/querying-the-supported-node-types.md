# Querying the Supported Node Types<a name="dws_02_0022"></a>

## Function<a name="sdfa13da9174b49a9a669c22a18eacd55"></a>

This API is used to query the node types supported by DWS.

## URI<a name="se3e5263cf68f4a9b828bb8f7b590626a"></a>

-   URI format

    GET /v1.0/\{project\_id\}/node\_types

    **Table  1**  URI parameter description

    <a name="en-us_topic_0067607269_table7515778"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607269_row990949"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607269_p13158007"><a name="en-us_topic_0067607269_p13158007"></a><a name="en-us_topic_0067607269_p13158007"></a><strong id="b84235270617228"><a name="b84235270617228"></a><a name="b84235270617228"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.33%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607269_p59165662"><a name="en-us_topic_0067607269_p59165662"></a><a name="en-us_topic_0067607269_p59165662"></a><strong id="b6167984116271"><a name="b6167984116271"></a><a name="b6167984116271"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607269_p27689346"><a name="en-us_topic_0067607269_p27689346"></a><a name="en-us_topic_0067607269_p27689346"></a><strong id="b84235270617235"><a name="b84235270617235"></a><a name="b84235270617235"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.730000000000004%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607269_p28244554"><a name="en-us_topic_0067607269_p28244554"></a><a name="en-us_topic_0067607269_p28244554"></a><strong id="b842352706172443"><a name="b842352706172443"></a><a name="b842352706172443"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607269_row6107551"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607269_p24949608"><a name="en-us_topic_0067607269_p24949608"></a><a name="en-us_topic_0067607269_p24949608"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607269_p7652366"><a name="en-us_topic_0067607269_p7652366"></a><a name="en-us_topic_0067607269_p7652366"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607269_p15861880"><a name="en-us_topic_0067607269_p15861880"></a><a name="en-us_topic_0067607269_p15861880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.730000000000004%" headers="mcps1.2.5.1.4 "><p id="p1731725075419"><a name="p1731725075419"></a><a name="p1731725075419"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s9036d11fcd964e078e6bb9017057ea8a"></a>

-   Sample request

    ```
    GET /v1.0/89cd04f168b84af6be287f71730fdb4b/node_types
    ```


## Response<a name="s0657e409391846eda0319914a02c09a5"></a>

-   Sample response

    ```
    STATUS CODE 200
    {
        "node_types": [
            {
                "spec_name": "dws.d1.xlarge",
                "id": "ebe532d6-665f-40e6-a4d4-3c51545b6a67",
                "detail": [
                    {
                        "type": "vCPU", 
                        "value": "4"
                        
                    },
                    {
                        "value": "1675",
                        "type": "LOCAL_DISK",
                        "unit": "GB"
                    },
                    {
                        "type": "mem",
                        "value": "32",
                       
                        "unit": "GB"
                    }
                ]
            },
            {
                "spec_name": "dws.m1.xlarge.ultrahigh",
                "id": "ebe532d6-665f-40e6-a4d4-3c51545b4f71",
                "detail": [
                    {
                        "type": "vCPU",
                        "value": "4"
                    },
                    {
                        "value": "512",
                        "type": "SSD",
                        "unit": "GB"
                    },
                    {
                        "type": "mem",
                        "value": "32",
                        "unit": "GB"
                    }
                ]
            }
        ]
    }
    ```


-   Parameter description

    **Table  2**  Response parameter description

    <a name="en-us_topic_0067607269_table37160390"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607269_row42208903"><th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607269_p63478007"><a name="en-us_topic_0067607269_p63478007"></a><a name="en-us_topic_0067607269_p63478007"></a><strong id="b27781172"><a name="b27781172"></a><a name="b27781172"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.447755224477554%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607269_p41444960"><a name="en-us_topic_0067607269_p41444960"></a><a name="en-us_topic_0067607269_p41444960"></a><strong id="b435483990"><a name="b435483990"></a><a name="b435483990"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607269_p1598569"><a name="en-us_topic_0067607269_p1598569"></a><a name="en-us_topic_0067607269_p1598569"></a><strong id="b996539937"><a name="b996539937"></a><a name="b996539937"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.87561243875613%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607269_p62375226"><a name="en-us_topic_0067607269_p62375226"></a><a name="en-us_topic_0067607269_p62375226"></a><strong id="b1228437615"><a name="b1228437615"></a><a name="b1228437615"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607269_row19228540"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607269_p14007894"><a name="en-us_topic_0067607269_p14007894"></a><a name="en-us_topic_0067607269_p14007894"></a>node_types</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607269_p60897649"><a name="en-us_topic_0067607269_p60897649"></a><a name="en-us_topic_0067607269_p60897649"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607269_p33762549"><a name="en-us_topic_0067607269_p33762549"></a><a name="en-us_topic_0067607269_p33762549"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607269_p50411912"><a name="en-us_topic_0067607269_p50411912"></a><a name="en-us_topic_0067607269_p50411912"></a>List of node types</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row51054032"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607269_p41735936"><a name="en-us_topic_0067607269_p41735936"></a><a name="en-us_topic_0067607269_p41735936"></a>spec_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607269_p25167636"><a name="en-us_topic_0067607269_p25167636"></a><a name="en-us_topic_0067607269_p25167636"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607269_p25312629"><a name="en-us_topic_0067607269_p25312629"></a><a name="en-us_topic_0067607269_p25312629"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607269_p37057034"><a name="en-us_topic_0067607269_p37057034"></a><a name="en-us_topic_0067607269_p37057034"></a>Name of a node type</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row65077851"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607269_p36814618"><a name="en-us_topic_0067607269_p36814618"></a><a name="en-us_topic_0067607269_p36814618"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607269_p29194114"><a name="en-us_topic_0067607269_p29194114"></a><a name="en-us_topic_0067607269_p29194114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607269_p15913018"><a name="en-us_topic_0067607269_p15913018"></a><a name="en-us_topic_0067607269_p15913018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607269_p13886058"><a name="en-us_topic_0067607269_p13886058"></a><a name="en-us_topic_0067607269_p13886058"></a>ID of a node type</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row57865663"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607269_p56607127"><a name="en-us_topic_0067607269_p56607127"></a><a name="en-us_topic_0067607269_p56607127"></a>detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607269_p21774588"><a name="en-us_topic_0067607269_p21774588"></a><a name="en-us_topic_0067607269_p21774588"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607269_p18911189"><a name="en-us_topic_0067607269_p18911189"></a><a name="en-us_topic_0067607269_p18911189"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607269_p55411339"><a name="en-us_topic_0067607269_p55411339"></a><a name="en-us_topic_0067607269_p55411339"></a>Node type details</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row28940004"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607269_p62438959"><a name="en-us_topic_0067607269_p62438959"></a><a name="en-us_topic_0067607269_p62438959"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607269_p24390923"><a name="en-us_topic_0067607269_p24390923"></a><a name="en-us_topic_0067607269_p24390923"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607269_p29507743"><a name="en-us_topic_0067607269_p29507743"></a><a name="en-us_topic_0067607269_p29507743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607269_p41317012"><a name="en-us_topic_0067607269_p41317012"></a><a name="en-us_topic_0067607269_p41317012"></a>Attribute value</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row36308794"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607269_p55331235"><a name="en-us_topic_0067607269_p55331235"></a><a name="en-us_topic_0067607269_p55331235"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607269_p52645056"><a name="en-us_topic_0067607269_p52645056"></a><a name="en-us_topic_0067607269_p52645056"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607269_p36391162"><a name="en-us_topic_0067607269_p36391162"></a><a name="en-us_topic_0067607269_p36391162"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607269_p62003000"><a name="en-us_topic_0067607269_p62003000"></a><a name="en-us_topic_0067607269_p62003000"></a>Attribute unit</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row21156092"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607269_p35921916"><a name="en-us_topic_0067607269_p35921916"></a><a name="en-us_topic_0067607269_p35921916"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607269_p23994101"><a name="en-us_topic_0067607269_p23994101"></a><a name="en-us_topic_0067607269_p23994101"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607269_p64473998"><a name="en-us_topic_0067607269_p64473998"></a><a name="en-us_topic_0067607269_p64473998"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607269_p55011311"><a name="en-us_topic_0067607269_p55011311"></a><a name="en-us_topic_0067607269_p55011311"></a>Attribute type</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Value<a name="s4aca364aca0245a694f14a4335b41ff5"></a>

-   Normal

    200

-   Abnormal 

    **Table  3**  Returned value description

    <a name="en-us_topic_0067607269_table42343927"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607269_row24512769"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.2.3.1.1"><p id="en-us_topic_0067607269_p39377290"><a name="en-us_topic_0067607269_p39377290"></a><a name="en-us_topic_0067607269_p39377290"></a><strong id="b84235270610542"><a name="b84235270610542"></a><a name="b84235270610542"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.3.1.2"><p id="en-us_topic_0067607269_p35443891"><a name="en-us_topic_0067607269_p35443891"></a><a name="en-us_topic_0067607269_p35443891"></a><strong id="b1033959324"><a name="b1033959324"></a><a name="b1033959324"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607269_row52382884"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607269_p15155206"><a name="en-us_topic_0067607269_p15155206"></a><a name="en-us_topic_0067607269_p15155206"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607269_p19612160"><a name="en-us_topic_0067607269_p19612160"></a><a name="en-us_topic_0067607269_p19612160"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row42291718"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607269_p3077144"><a name="en-us_topic_0067607269_p3077144"></a><a name="en-us_topic_0067607269_p3077144"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607269_p47922135"><a name="en-us_topic_0067607269_p47922135"></a><a name="en-us_topic_0067607269_p47922135"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row28646034"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607269_p38627455"><a name="en-us_topic_0067607269_p38627455"></a><a name="en-us_topic_0067607269_p38627455"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607269_p41816140"><a name="en-us_topic_0067607269_p41816140"></a><a name="en-us_topic_0067607269_p41816140"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row40800942"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607269_p16541999"><a name="en-us_topic_0067607269_p16541999"></a><a name="en-us_topic_0067607269_p16541999"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607269_p64833508"><a name="en-us_topic_0067607269_p64833508"></a><a name="en-us_topic_0067607269_p64833508"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row46630661"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607269_p18987236"><a name="en-us_topic_0067607269_p18987236"></a><a name="en-us_topic_0067607269_p18987236"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607269_p61571180"><a name="en-us_topic_0067607269_p61571180"></a><a name="en-us_topic_0067607269_p61571180"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607269_row17269710"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607269_p56669285"><a name="en-us_topic_0067607269_p56669285"></a><a name="en-us_topic_0067607269_p56669285"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607269_p26809401"><a name="en-us_topic_0067607269_p26809401"></a><a name="en-us_topic_0067607269_p26809401"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


