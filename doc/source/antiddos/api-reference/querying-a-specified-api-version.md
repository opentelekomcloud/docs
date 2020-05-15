# Querying a Specified API Version<a name="antiddos_02_0007"></a>

## Functions<a name="section63597034"></a>

This API allows you to query a specified API version.

## URI<a name="section35502400"></a>

-   URI format

    GET /\{version\_id\}


## Request<a name="section51086148"></a>

-   Request example

    ```
    GET /v1
    ```


## Response<a name="section57122151"></a>

-   Element description

    <a name="table15327568"></a>
    <table><thead align="left"><tr id="row24486356"><th class="cellrowborder" valign="top" width="30.099999999999998%" id="mcps1.1.4.1.1"><p id="p37237828"><a name="p37237828"></a><a name="p37237828"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.99%" id="mcps1.1.4.1.2"><p id="p63474072"><a name="p63474072"></a><a name="p63474072"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.910000000000004%" id="mcps1.1.4.1.3"><p id="p41126201"><a name="p41126201"></a><a name="p41126201"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42887950"><td class="cellrowborder" valign="top" width="30.099999999999998%" headers="mcps1.1.4.1.1 "><p id="p51371903"><a name="p51371903"></a><a name="p51371903"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.1.4.1.2 "><p id="p2142367152712"><a name="p2142367152712"></a><a name="p2142367152712"></a>Data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.910000000000004%" headers="mcps1.1.4.1.3 "><p id="p30346328"><a name="p30346328"></a><a name="p30346328"></a>Version object</p>
    </td>
    </tr>
    <tr id="row4681502"><td class="cellrowborder" valign="top" width="30.099999999999998%" headers="mcps1.1.4.1.1 "><p id="p1264115702215"><a name="p1264115702215"></a><a name="p1264115702215"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.1.4.1.2 "><p id="p46585119"><a name="p46585119"></a><a name="p46585119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.910000000000004%" headers="mcps1.1.4.1.3 "><p id="p15298296"><a name="p15298296"></a><a name="p15298296"></a>Version ID (Version number), for example, v 1</p>
    </td>
    </tr>
    <tr id="row3466944"><td class="cellrowborder" valign="top" width="30.099999999999998%" headers="mcps1.1.4.1.1 "><p id="p12387033"><a name="p12387033"></a><a name="p12387033"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.1.4.1.2 "><p id="p63825615"><a name="p63825615"></a><a name="p63825615"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.910000000000004%" headers="mcps1.1.4.1.3 "><p id="p2492297"><a name="p2492297"></a><a name="p2492297"></a>URL of the API</p>
    </td>
    </tr>
    <tr id="row144801646162619"><td class="cellrowborder" valign="top" width="30.099999999999998%" headers="mcps1.1.4.1.1 "><p id="p34811461266"><a name="p34811461266"></a><a name="p34811461266"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.1.4.1.2 "><p id="p6550258270"><a name="p6550258270"></a><a name="p6550258270"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.910000000000004%" headers="mcps1.1.4.1.3 "><p id="p448174612618"><a name="p448174612618"></a><a name="p448174612618"></a>If this API version supports microversions, the minimum microversion number is returned. If microversions are not supported, no value is returned.</p>
    </td>
    </tr>
    <tr id="row19836152372716"><td class="cellrowborder" valign="top" width="30.099999999999998%" headers="mcps1.1.4.1.1 "><p id="p383610239276"><a name="p383610239276"></a><a name="p383610239276"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.1.4.1.2 "><p id="p118361023142716"><a name="p118361023142716"></a><a name="p118361023142716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.910000000000004%" headers="mcps1.1.4.1.3 "><p id="p1338013918285"><a name="p1338013918285"></a><a name="p1338013918285"></a>Version status. Valid values are as follows:</p>
    <p id="p12382393282"><a name="p12382393282"></a><a name="p12382393282"></a>CURRENT: Indicates that the version is the primary version.</p>
    <p id="p5382189202813"><a name="p5382189202813"></a><a name="p5382189202813"></a>SUPPORTED: Indicates that the version is an old version, but it is still supported.</p>
    <p id="p738219202816"><a name="p738219202816"></a><a name="p738219202816"></a>DEPRECATED: Indicates that this version is a discarded version and may be deleted later.</p>
    </td>
    </tr>
    <tr id="row1910182213287"><td class="cellrowborder" valign="top" width="30.099999999999998%" headers="mcps1.1.4.1.1 "><p id="p610114226281"><a name="p610114226281"></a><a name="p610114226281"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.1.4.1.2 "><p id="p181019227289"><a name="p181019227289"></a><a name="p181019227289"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.910000000000004%" headers="mcps1.1.4.1.3 "><p id="p4101132219286"><a name="p4101132219286"></a><a name="p4101132219286"></a>Version release time</p>
    </td>
    </tr>
    <tr id="row644342203017"><td class="cellrowborder" valign="top" width="30.099999999999998%" headers="mcps1.1.4.1.1 "><p id="p14446142153012"><a name="p14446142153012"></a><a name="p14446142153012"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.1.4.1.2 "><p id="p16446529302"><a name="p16446529302"></a><a name="p16446529302"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.910000000000004%" headers="mcps1.1.4.1.3 "><p id="p7446152173011"><a name="p7446152173011"></a><a name="p7446152173011"></a>If this API version supports microversions, the maximum microversion number is returned. If microversions are not supported, no value is returned.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Data structure description of  **links**

    <a name="table44508523"></a>
    <table><thead align="left"><tr id="row13604004"><th class="cellrowborder" valign="top" width="30.61%" id="mcps1.1.5.1.1"><p id="p28182506"><a name="p28182506"></a><a name="p28182506"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.02%" id="mcps1.1.5.1.2"><p id="p1081649"><a name="p1081649"></a><a name="p1081649"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.94%" id="mcps1.1.5.1.3"><p id="p20504736"><a name="p20504736"></a><a name="p20504736"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.43%" id="mcps1.1.5.1.4"><p id="p50270944"><a name="p50270944"></a><a name="p50270944"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45414681"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.1.5.1.1 "><p id="p54710514"><a name="p54710514"></a><a name="p54710514"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.02%" headers="mcps1.1.5.1.2 "><p id="p2366611"><a name="p2366611"></a><a name="p2366611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.94%" headers="mcps1.1.5.1.3 "><p id="p53636340152723"><a name="p53636340152723"></a><a name="p53636340152723"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.43%" headers="mcps1.1.5.1.4 "><p id="p25189967"><a name="p25189967"></a><a name="p25189967"></a>URL of the API</p>
    </td>
    </tr>
    <tr id="row25383117"><td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.1.5.1.1 "><p id="p42766607"><a name="p42766607"></a><a name="p42766607"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.02%" headers="mcps1.1.5.1.2 "><p id="p41543166"><a name="p41543166"></a><a name="p41543166"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.94%" headers="mcps1.1.5.1.3 "><p id="p65381003152726"><a name="p65381003152726"></a><a name="p65381003152726"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.43%" headers="mcps1.1.5.1.4 "><p id="p35618305"><a name="p35618305"></a><a name="p35618305"></a>self</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "version": 
       {
          "id": "v1",
          "links": [
            {
              "href": "https://antiddos.eu-de.otc.t-systems.com/v1/",
              "rel": "self"
            }
          ],
          "min_version": "",
          "status": "CURRENT",
          "updated": "2016-10-29T00:00:00Z",
          "version": ""
       }
    }
    ```


## Returned Value<a name="section44337314"></a>

For details, see  [Status Code](status-code.md).

