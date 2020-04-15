# Deleting a Protected Instance Tag<a name="sdrs_05_0804"></a>

## Function<a name="section586762416474"></a>

This API is idempotent.

-   During deletion, the tag character set is not verified. The URI must be encoded before the API is invoked. Other services need to decode the URI.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Select a desired tool for URI encoding.  

-   The tag key cannot be left blank or be an empty string. If the key of the tag to be deleted does not exist, 404 will be returned.

## URI<a name="section148681724194714"></a>

-   URI format

    DELETE /v1/\{project\_id\}/protected-instances/\{protected\_instance\_id\}/tags/\{key\}

-   Parameter description

    <a name="table19869724104710"></a>
    <table><thead align="left"><tr id="row9941182444715"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.1.5.1.1"><p id="p29421924124710"><a name="p29421924124710"></a><a name="p29421924124710"></a><strong id="b842352706162023"><a name="b842352706162023"></a><a name="b842352706162023"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.447755224477554%" id="mcps1.1.5.1.2"><p id="p1942182444714"><a name="p1942182444714"></a><a name="p1942182444714"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.268673132686734%" id="mcps1.1.5.1.3"><p id="p1094292474718"><a name="p1094292474718"></a><a name="p1094292474718"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.1.5.1.4"><p id="p494216248471"><a name="p494216248471"></a><a name="p494216248471"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17942152417472"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.1 "><p id="p20942192416476"><a name="p20942192416476"></a><a name="p20942192416476"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.1.5.1.2 "><p id="p1194292474719"><a name="p1194292474719"></a><a name="p1194292474719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.1.5.1.3 "><p id="p14942112410476"><a name="p14942112410476"></a><a name="p14942112410476"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p14942824134715"><a name="p14942824134715"></a><a name="p14942824134715"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row69427244479"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.1 "><p id="p16942624134713"><a name="p16942624134713"></a><a name="p16942624134713"></a>protected_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.1.5.1.2 "><p id="p0942182434710"><a name="p0942182434710"></a><a name="p0942182434710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.1.5.1.3 "><p id="p1694232484719"><a name="p1694232484719"></a><a name="p1694232484719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p394216244475"><a name="p394216244475"></a><a name="p394216244475"></a>Specifies the ID of a protected instance.</p>
    <p id="p1824552055516"><a name="p1824552055516"></a><a name="p1824552055516"></a>For details, see <a href="querying-protected-instances.md">Querying Protected Instances</a>.</p>
    </td>
    </tr>
    <tr id="row594212484714"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.1 "><p id="p1994242417477"><a name="p1994242417477"></a><a name="p1994242417477"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.1.5.1.2 "><p id="p99423241472"><a name="p99423241472"></a><a name="p99423241472"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.1.5.1.3 "><p id="p1694242474714"><a name="p1694242474714"></a><a name="p1694242474714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p20942172419475"><a name="p20942172419475"></a><a name="p20942172419475"></a>Specifies the tag key.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section387732419479"></a>

-   Request parameters

    None

-   Example request

    DELETE https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/67a2cc7e-fb87-41a8-ba28-9c032abcaee1/tags/DEV


## Response<a name="section794735716551"></a>

-   Response parameter

    None

-   Example response

    None


## **Returned Value**<a name="section8878224104719"></a>

-   Normal

    <a name="table688042414711"></a>
    <table><thead align="left"><tr id="row15943192412479"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1943102424714"><a name="p1943102424714"></a><a name="p1943102424714"></a><strong id="b308046617"><a name="b308046617"></a><a name="b308046617"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p199431524144718"><a name="p199431524144718"></a><a name="p199431524144718"></a><strong id="b1128765199"><a name="b1128765199"></a><a name="b1128765199"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7943224104718"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p14943824124711"><a name="p14943824124711"></a><a name="p14943824124711"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p89431524154710"><a name="p89431524154710"></a><a name="p89431524154710"></a>No Content</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    <a name="table488272434713"></a>
    <table><thead align="left"><tr id="row7943624134715"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p894316243477"><a name="p894316243477"></a><a name="p894316243477"></a><strong id="b82839864"><a name="b82839864"></a><a name="b82839864"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p4943172414470"><a name="p4943172414470"></a><a name="p4943172414470"></a><strong id="b1185669954"><a name="b1185669954"></a><a name="b1185669954"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3943132411476"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p18943122410473"><a name="p18943122410473"></a><a name="p18943122410473"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p69431024114719"><a name="p69431024114719"></a><a name="p69431024114719"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row15943102413472"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p10943224194715"><a name="p10943224194715"></a><a name="p10943224194715"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2094332454713"><a name="p2094332454713"></a><a name="p2094332454713"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row169431324144718"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p5943142413478"><a name="p5943142413478"></a><a name="p5943142413478"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p12944424194720"><a name="p12944424194720"></a><a name="p12944424194720"></a>Insufficient permission.</p>
    </td>
    </tr>
    <tr id="row394412417470"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p15944172418479"><a name="p15944172418479"></a><a name="p15944172418479"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p494419248474"><a name="p494419248474"></a><a name="p494419248474"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row7944524194717"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p3944132413479"><a name="p3944132413479"></a><a name="p3944132413479"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p49441024154715"><a name="p49441024154715"></a><a name="p49441024154715"></a>Internal service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


