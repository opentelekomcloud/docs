# Querying Image Details \(Native OpenStack API v1.1 - Abandoned and Not Recommended\)<a name="EN-US_TOPIC_0066978720"></a>

## Function<a name="section21608354152128"></a>

This API is used to query details of images.

This API has been discarded. The image query API \([Querying Images \(Native OpenStack API\)](querying-images-(native-openstack-api).md)\) is recommended.

## URI<a name="section49016415152128"></a>

GET /v1.1/images/detail

## Request<a name="section49535636152128"></a>

-   Request parameters

    Parameters  **name**,  **container\_format**,  **disk\_format**,  **status**,  **size\_min**,  **size\_max**, and  **changes-since**  can be used to filter the query result.

    <a name="table6909858152128"></a>
    <table><thead align="left"><tr id="row2200986152128"><th class="cellrowborder" valign="top" width="21.8%" id="mcps1.1.5.1.1"><p id="p44062206152128"><a name="p44062206152128"></a><a name="p44062206152128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.1.5.1.2"><p id="p54259611152128"><a name="p54259611152128"></a><a name="p54259611152128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.18%" id="mcps1.1.5.1.3"><p id="p4897115216284"><a name="p4897115216284"></a><a name="p4897115216284"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.35%" id="mcps1.1.5.1.4"><p id="p32952356152128"><a name="p32952356152128"></a><a name="p32952356152128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51895178152128"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.1.5.1.1 "><p id="p42759860152128"><a name="p42759860152128"></a><a name="p42759860152128"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.2 "><p id="p32391798152128"><a name="p32391798152128"></a><a name="p32391798152128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.3 "><p id="p1389675272820"><a name="p1389675272820"></a><a name="p1389675272820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.1.5.1.4 "><p id="p6489949152128"><a name="p6489949152128"></a><a name="p6489949152128"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row58409547152128"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.1.5.1.1 "><p id="p33552889152128"><a name="p33552889152128"></a><a name="p33552889152128"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.2 "><p id="p23431949152128"><a name="p23431949152128"></a><a name="p23431949152128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.3 "><p id="p1389418528284"><a name="p1389418528284"></a><a name="p1389418528284"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.1.5.1.4 "><p id="p18939716152128"><a name="p18939716152128"></a><a name="p18939716152128"></a>Image container type</p>
    </td>
    </tr>
    <tr id="row36239719152128"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.1.5.1.1 "><p id="p49736130152128"><a name="p49736130152128"></a><a name="p49736130152128"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.2 "><p id="p35453405152128"><a name="p35453405152128"></a><a name="p35453405152128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.3 "><p id="p78931452122815"><a name="p78931452122815"></a><a name="p78931452122815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.1.5.1.4 "><p id="p53153517152128"><a name="p53153517152128"></a><a name="p53153517152128"></a>Image file format</p>
    </td>
    </tr>
    <tr id="row8619606152128"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.1.5.1.1 "><p id="p27099480152128"><a name="p27099480152128"></a><a name="p27099480152128"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.2 "><p id="p28309709152128"><a name="p28309709152128"></a><a name="p28309709152128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.3 "><p id="p98911952142816"><a name="p98911952142816"></a><a name="p98911952142816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.1.5.1.4 "><p id="p11385105152128"><a name="p11385105152128"></a><a name="p11385105152128"></a>Image status</p>
    </td>
    </tr>
    <tr id="row35357081152128"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.1.5.1.1 "><p id="p45351308152128"><a name="p45351308152128"></a><a name="p45351308152128"></a>size_min</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.2 "><p id="p56341584152128"><a name="p56341584152128"></a><a name="p56341584152128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.3 "><p id="p178901529283"><a name="p178901529283"></a><a name="p178901529283"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.1.5.1.4 "><p id="p265585152128"><a name="p265585152128"></a><a name="p265585152128"></a>Minimum size of the image</p>
    </td>
    </tr>
    <tr id="row2390265152128"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.1.5.1.1 "><p id="p59393783152128"><a name="p59393783152128"></a><a name="p59393783152128"></a>size_max</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.2 "><p id="p48552350152128"><a name="p48552350152128"></a><a name="p48552350152128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.3 "><p id="p4889125210286"><a name="p4889125210286"></a><a name="p4889125210286"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.1.5.1.4 "><p id="p40426262152128"><a name="p40426262152128"></a><a name="p40426262152128"></a>Maximum size of the image</p>
    </td>
    </tr>
    <tr id="row28292039152128"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.1.5.1.1 "><p id="p9953851152128"><a name="p9953851152128"></a><a name="p9953851152128"></a>changes-since</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.2 "><p id="p10295032152128"><a name="p10295032152128"></a><a name="p10295032152128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.3 "><p id="p128877524288"><a name="p128877524288"></a><a name="p128877524288"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.1.5.1.4 "><p id="p28591249152128"><a name="p28591249152128"></a><a name="p28591249152128"></a>Last update time</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{Endpoint}/v1.1/images/detail?disk_format=qcow2
    ```


## Response<a name="section55994653152128"></a>

-   Response parameters

    <a name="table39273024152128"></a>
    <table><thead align="left"><tr id="row54360090152128"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p41091190152128"><a name="p41091190152128"></a><a name="p41091190152128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p40052127152128"><a name="p40052127152128"></a><a name="p40052127152128"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p50806390152128"><a name="p50806390152128"></a><a name="p50806390152128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21676916152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p10999775152128"><a name="p10999775152128"></a><a name="p10999775152128"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p18566558152128"><a name="p18566558152128"></a><a name="p18566558152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p12601146152128"><a name="p12601146152128"></a><a name="p12601146152128"></a>Image status</p>
    </td>
    </tr>
    <tr id="row46301451152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p59430045152128"><a name="p59430045152128"></a><a name="p59430045152128"></a>virtual_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p49104327152128"><a name="p49104327152128"></a><a name="p49104327152128"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p50947078152128"><a name="p50947078152128"></a><a name="p50947078152128"></a>Virtual size of an image</p>
    </td>
    </tr>
    <tr id="row55870518152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p29218105152128"><a name="p29218105152128"></a><a name="p29218105152128"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p17856313152128"><a name="p17856313152128"></a><a name="p17856313152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p50303566152128"><a name="p50303566152128"></a><a name="p50303566152128"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row50078910152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p29859916152128"><a name="p29859916152128"></a><a name="p29859916152128"></a>deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p2734171152128"><a name="p2734171152128"></a><a name="p2734171152128"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p20835099152128"><a name="p20835099152128"></a><a name="p20835099152128"></a>Whether an image has been deleted</p>
    </td>
    </tr>
    <tr id="row53298164152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p22184056152128"><a name="p22184056152128"></a><a name="p22184056152128"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p52078112152128"><a name="p52078112152128"></a><a name="p52078112152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p33270526152128"><a name="p33270526152128"></a><a name="p33270526152128"></a>Image container type</p>
    </td>
    </tr>
    <tr id="row30999282152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p27913893152128"><a name="p27913893152128"></a><a name="p27913893152128"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p46432832152128"><a name="p46432832152128"></a><a name="p46432832152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p38680656152128"><a name="p38680656152128"></a><a name="p38680656152128"></a>Time when an image was created</p>
    </td>
    </tr>
    <tr id="row12581591152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p12475971152128"><a name="p12475971152128"></a><a name="p12475971152128"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3920764152128"><a name="p3920764152128"></a><a name="p3920764152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p21441395152128"><a name="p21441395152128"></a><a name="p21441395152128"></a>Image file type</p>
    </td>
    </tr>
    <tr id="row58754830152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p61520781152128"><a name="p61520781152128"></a><a name="p61520781152128"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p17127389152128"><a name="p17127389152128"></a><a name="p17127389152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p32565519152128"><a name="p32565519152128"></a><a name="p32565519152128"></a>Time when an image was updated</p>
    </td>
    </tr>
    <tr id="row24654215152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p50834371152128"><a name="p50834371152128"></a><a name="p50834371152128"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p23943412152128"><a name="p23943412152128"></a><a name="p23943412152128"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p57990740152128"><a name="p57990740152128"></a><a name="p57990740152128"></a>Image attribute</p>
    </td>
    </tr>
    <tr id="row52154619152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p63774574152128"><a name="p63774574152128"></a><a name="p63774574152128"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p65466907152128"><a name="p65466907152128"></a><a name="p65466907152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p31649597152128"><a name="p31649597152128"></a><a name="p31649597152128"></a>Tenant to which an image belongs</p>
    </td>
    </tr>
    <tr id="row16410923152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p54216352152128"><a name="p54216352152128"></a><a name="p54216352152128"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p29448369152128"><a name="p29448369152128"></a><a name="p29448369152128"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p4335306152128"><a name="p4335306152128"></a><a name="p4335306152128"></a>Whether an image is protected</p>
    </td>
    </tr>
    <tr id="row39017760152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p6321968152128"><a name="p6321968152128"></a><a name="p6321968152128"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p42317409152128"><a name="p42317409152128"></a><a name="p42317409152128"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p15153476152128"><a name="p15153476152128"></a><a name="p15153476152128"></a>Minimum memory (MB) required for running an image</p>
    </td>
    </tr>
    <tr id="row2163563152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p41030913152128"><a name="p41030913152128"></a><a name="p41030913152128"></a>checksum</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p35169627152128"><a name="p35169627152128"></a><a name="p35169627152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p27650173152128"><a name="p27650173152128"></a><a name="p27650173152128"></a>Image verification sum. This parameter is available after an image file is uploaded.</p>
    </td>
    </tr>
    <tr id="row47524965152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p24316986152128"><a name="p24316986152128"></a><a name="p24316986152128"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p23518872152128"><a name="p23518872152128"></a><a name="p23518872152128"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p24041996152128"><a name="p24041996152128"></a><a name="p24041996152128"></a>Minimum disk capacity (GB) required for running the image</p>
    </td>
    </tr>
    <tr id="row15051376152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p11201934152128"><a name="p11201934152128"></a><a name="p11201934152128"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p34941465152128"><a name="p34941465152128"></a><a name="p34941465152128"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p7073684152128"><a name="p7073684152128"></a><a name="p7073684152128"></a>Whether an image is a public one</p>
    </td>
    </tr>
    <tr id="row63663156152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p56441973152128"><a name="p56441973152128"></a><a name="p56441973152128"></a>deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p8397095152128"><a name="p8397095152128"></a><a name="p8397095152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64073980152128"><a name="p64073980152128"></a><a name="p64073980152128"></a>Time when an image was deleted</p>
    </td>
    </tr>
    <tr id="row39794913152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p2162544152128"><a name="p2162544152128"></a><a name="p2162544152128"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p40948371152128"><a name="p40948371152128"></a><a name="p40948371152128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p25483447152128"><a name="p25483447152128"></a><a name="p25483447152128"></a>Image UUID</p>
    </td>
    </tr>
    <tr id="row28024434152128"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p55386696152128"><a name="p55386696152128"></a><a name="p55386696152128"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p57137398152128"><a name="p57137398152128"></a><a name="p57137398152128"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p8360445152128"><a name="p8360445152128"></a><a name="p8360445152128"></a>Image size. This parameter is available after an image file is uploaded.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    HTTP/1.1 200 OK
    ```

    ```
    Content-Type: application/json; charset=UTF-8
    Content-Length: 495
    X-Openstack-Request-Id: req-68327dda-8078-41fe-b091-01a09ec073da
    Date: Mon, 23 May 2016 02:32:28 GMT
    {
        "images": [
            {
                "status": "active",
                "deleted_at": null,
                "name": "cirros",
                "deleted": false,
                "container_format": "bare",
                "created_at": "2016-05-22T06:04:20.425843",
                "disk_format": "qcow2",
                "updated_at": "2016-05-22T06:04:22.719791",
                "min_disk": 0,
                "protected": false,
                "id": "3c3d1d01-b48a-4639-8a88-08be3b9b5d78",
                "min_ram": 0,
                "checksum": "64d7c1cd2b6f60c92c14662941cb7913",
                "owner": "23f4cb75768d4febb39542ef6fe169f3",
                "is_public": true,
                "virtual_size": null,
                "properties": {
                },
                "size": 13167616
            }
        ]
    }
    ```


## Returned Values<a name="section61208656152128"></a>

-   Normal

    200

-   Abnormal

    <a name="table262968317230"></a>
    <table><thead align="left"><tr id="row5740081817230"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p1895465817230"><a name="p1895465817230"></a><a name="p1895465817230"></a>Returned Values</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p5893233917230"><a name="p5893233917230"></a><a name="p5893233917230"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row879015617230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4091407017230"><a name="p4091407017230"></a><a name="p4091407017230"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2570540117230"><a name="p2570540117230"></a><a name="p2570540117230"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row176271617230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p856227917230"><a name="p856227917230"></a><a name="p856227917230"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2245600317230"><a name="p2245600317230"></a><a name="p2245600317230"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row77743917230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p6297256617230"><a name="p6297256617230"></a><a name="p6297256617230"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p50424217230"><a name="p50424217230"></a><a name="p50424217230"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row56011270191147"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p40619053191147"><a name="p40619053191147"></a><a name="p40619053191147"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1808959191147"><a name="p1808959191147"></a><a name="p1808959191147"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row453818617230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p3204876017230"><a name="p3204876017230"></a><a name="p3204876017230"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p4581273417230"><a name="p4581273417230"></a><a name="p4581273417230"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row966142617230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4437803217230"><a name="p4437803217230"></a><a name="p4437803217230"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p3785084317230"><a name="p3785084317230"></a><a name="p3785084317230"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


