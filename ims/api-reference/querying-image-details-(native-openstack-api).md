# Querying Image Details \(Native OpenStack API\)<a name="EN-US_TOPIC_0020091566"></a>

## Function<a name="section39958021"></a>

This API is used to query details about a public or private image.

## URI<a name="section24077873"></a>

GET /v2/images/\{image\_id\}

[Table 1](#table37590215162351)  lists the parameters.

**Table  1**  Parameter description

<a name="table37590215162351"></a>
<table><thead align="left"><tr id="row14906674162351"><th class="cellrowborder" valign="top" width="24.060000000000002%" id="mcps1.2.5.1.1"><p id="p66589937162351"><a name="p66589937162351"></a><a name="p66589937162351"></a><strong id="b84235270616336"><a name="b84235270616336"></a><a name="b84235270616336"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.369999999999997%" id="mcps1.2.5.1.2"><p id="p25075841162351"><a name="p25075841162351"></a><a name="p25075841162351"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.3"><p id="p3182134421246"><a name="p3182134421246"></a><a name="p3182134421246"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.4"><p id="p17877258162351"><a name="p17877258162351"></a><a name="p17877258162351"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row38771763162351"><td class="cellrowborder" valign="top" width="24.060000000000002%" headers="mcps1.2.5.1.1 "><p id="p53505060162351"><a name="p53505060162351"></a><a name="p53505060162351"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.369999999999997%" headers="mcps1.2.5.1.2 "><p id="p38942598162351"><a name="p38942598162351"></a><a name="p38942598162351"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p2739208421246"><a name="p2739208421246"></a><a name="p2739208421246"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><p id="p233856162351"><a name="p233856162351"></a><a name="p233856162351"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section15374270"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v2/images/33ad552d-1149-471c-8190-ff6776174a00
    ```


## Response<a name="section4150710"></a>

-   Response parameters

    <a name="table3940930519484"></a>
    <table><thead align="left"><tr id="row5108650619484"><th class="cellrowborder" valign="top" width="36.9%" id="mcps1.1.4.1.1"><p id="p4436630719484"><a name="p4436630719484"></a><a name="p4436630719484"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.700000000000003%" id="mcps1.1.4.1.2"><p id="p3690111319484"><a name="p3690111319484"></a><a name="p3690111319484"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="36.4%" id="mcps1.1.4.1.3"><p id="p3620014719484"><a name="p3620014719484"></a><a name="p3620014719484"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4653077719484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1089662919484"><a name="p1089662919484"></a><a name="p1089662919484"></a>file</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p1021172419484"><a name="p1021172419484"></a><a name="p1021172419484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p2184333619484"><a name="p2184333619484"></a><a name="p2184333619484"></a>Specifies the URL for uploading and downloading the image file.</p>
    </td>
    </tr>
    <tr id="row6237230419484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1899183819484"><a name="p1899183819484"></a><a name="p1899183819484"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p6194387619484"><a name="p6194387619484"></a><a name="p6194387619484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p5139805919484"><a name="p5139805919484"></a><a name="p5139805919484"></a>Specifies the tenant to which the image belongs.</p>
    </td>
    </tr>
    <tr id="row5992935019484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p2243918519484"><a name="p2243918519484"></a><a name="p2243918519484"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p563467219484"><a name="p563467219484"></a><a name="p563467219484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p5375527619484"><a name="p5375527619484"></a><a name="p5375527619484"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="row1403543619484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p6312849319484"><a name="p6312849319484"></a><a name="p6312849319484"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p1313430319484"><a name="p1313430319484"></a><a name="p1313430319484"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p5724560919484"><a name="p5724560919484"></a><a name="p5724560919484"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row4544843919484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p5744495319484"><a name="p5744495319484"></a><a name="p5744495319484"></a>self</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p2252964019484"><a name="p2252964019484"></a><a name="p2252964019484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p1296154719484"><a name="p1296154719484"></a><a name="p1296154719484"></a>Specifies the image URL.</p>
    </td>
    </tr>
    <tr id="row4954506419484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p5372723719484"><a name="p5372723719484"></a><a name="p5372723719484"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p5693892219484"><a name="p5693892219484"></a><a name="p5693892219484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p4864998419484"><a name="p4864998419484"></a><a name="p4864998419484"></a>Specifies the image schema.</p>
    </td>
    </tr>
    <tr id="row3519667719484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p3235856619484"><a name="p3235856619484"></a><a name="p3235856619484"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p379822119484"><a name="p379822119484"></a><a name="p379822119484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p32131061155224"><a name="p32131061155224"></a><a name="p32131061155224"></a>Specifies the image status. The value can be one of the following:</p>
    <a name="ul43292299155227"></a><a name="ul43292299155227"></a><ul id="ul43292299155227"><li><strong id="b842352706103333"><a name="b842352706103333"></a><a name="b842352706103333"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="b842352706104325"><a name="b842352706104325"></a><a name="b842352706104325"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="b842352706104450"><a name="b842352706104450"></a><a name="b842352706104450"></a>deleted</strong>: indicates that the image has been deleted. </li><li><strong id="b842352706104518"><a name="b842352706104518"></a><a name="b842352706104518"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="b842352706104558"><a name="b842352706104558"></a><a name="b842352706104558"></a>active</strong>: indicates that the image is available for use. </li></ul>
    </td>
    </tr>
    <tr id="row1743970919484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p333030119484"><a name="p333030119484"></a><a name="p333030119484"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p131897419484"><a name="p131897419484"></a><a name="p131897419484"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p3972807119484"><a name="p3972807119484"></a><a name="p3972807119484"></a>Lists the image tags, through which you can manage private images in your own way. You can use the image tag API to add different tags to each image and filter images by tag.</p>
    </td>
    </tr>
    <tr id="row2200832719484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p3784404819484"><a name="p3784404819484"></a><a name="p3784404819484"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p4546904619484"><a name="p4546904619484"></a><a name="p4546904619484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p152431834103310"><a name="p152431834103310"></a><a name="p152431834103310"></a>Specifies whether the image is available to other tenants. Available values include:</p>
    <a name="ul17437224348"></a><a name="ul17437224348"></a><ul id="ul17437224348"><li><strong id="b178441119201919"><a name="b178441119201919"></a><a name="b178441119201919"></a>private</strong>: private image</li><li><strong id="b1431616219197"><a name="b1431616219197"></a><a name="b1431616219197"></a>public</strong>: public image</li><li><strong id="b1262862214197"><a name="b1262862214197"></a><a name="b1262862214197"></a>shared</strong>: shared image</li></ul>
    </td>
    </tr>
    <tr id="row6226467419484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1027383819484"><a name="p1027383819484"></a><a name="p1027383819484"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p2687454619484"><a name="p2687454619484"></a><a name="p2687454619484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p2935464719484"><a name="p2935464719484"></a><a name="p2935464719484"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row6286523719484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p5891947019484"><a name="p5891947019484"></a><a name="p5891947019484"></a>checksum</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p774777119484"><a name="p774777119484"></a><a name="p774777119484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p2358973319484"><a name="p2358973319484"></a><a name="p2358973319484"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row1098100819484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1704644719484"><a name="p1704644719484"></a><a name="p1704644719484"></a>deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p3858499119484"><a name="p3858499119484"></a><a name="p3858499119484"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p3837658419484"><a name="p3837658419484"></a><a name="p3837658419484"></a>Specifies whether the image has been deleted. The value can be <strong>true</strong> or <strong>false</strong>.</p>
    </td>
    </tr>
    <tr id="row984493719484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p5924239319484"><a name="p5924239319484"></a><a name="p5924239319484"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p3390450119484"><a name="p3390450119484"></a><a name="p3390450119484"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p6191008619484"><a name="p6191008619484"></a><a name="p6191008619484"></a>Specifies whether the image is protected. A protected image cannot be deleted. The value can be <strong>true</strong> or <strong>false</strong>.</p>
    </td>
    </tr>
    <tr id="row2031987019484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p3529679319484"><a name="p3529679319484"></a><a name="p3529679319484"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p4046799719484"><a name="p4046799719484"></a><a name="p4046799719484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p5668228819484"><a name="p5668228819484"></a><a name="p5668228819484"></a>Specifies the container type. </p>
    </td>
    </tr>
    <tr id="row4037855219484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p4943728819484"><a name="p4943728819484"></a><a name="p4943728819484"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p4499737219484"><a name="p4499737219484"></a><a name="p4499737219484"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p2090850919484"><a name="p2090850919484"></a><a name="p2090850919484"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the <span id="text18791121017151"><a name="text18791121017151"></a><a name="text18791121017151"></a></span><span id="text1379111108153"><a name="text1379111108153"></a><a name="text1379111108153"></a>ECS</span> flavor. Generally, the value is <strong id="b1979116109153"><a name="b1979116109153"></a><a name="b1979116109153"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row5395885319484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p859097919484"><a name="p859097919484"></a><a name="p859097919484"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p2478073819484"><a name="p2478073819484"></a><a name="p2478073819484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p6108279419484"><a name="p6108279419484"></a><a name="p6108279419484"></a>Specifies the time when the image was updated. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row1287423619484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p3618021119484"><a name="p3618021119484"></a><a name="p3618021119484"></a>__os_bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p4491600719484"><a name="p4491600719484"></a><a name="p4491600719484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p1431795119484"><a name="p1431795119484"></a><a name="p1431795119484"></a>Specifies the OS architecture, 32 bit or 64 bit.</p>
    </td>
    </tr>
    <tr id="row6175270019484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p3591283819484"><a name="p3591283819484"></a><a name="p3591283819484"></a>__os_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p2325879319484"><a name="p2325879319484"></a><a name="p2325879319484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p491406019484"><a name="p491406019484"></a><a name="p491406019484"></a>Specifies the OS version.</p>
    </td>
    </tr>
    <tr id="row4422654119484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p2558005119484"><a name="p2558005119484"></a><a name="p2558005119484"></a>__description</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p5871828719484"><a name="p5871828719484"></a><a name="p5871828719484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p5856077419484"><a name="p5856077419484"></a><a name="p5856077419484"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row5728492419484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p956729019484"><a name="p956729019484"></a><a name="p956729019484"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p3675300019484"><a name="p3675300019484"></a><a name="p3675300019484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p2420299019484"><a name="p2420299019484"></a><a name="p2420299019484"></a>Specifies the image format. The value can be <strong id="b1291851475019"><a name="b1291851475019"></a><a name="b1291851475019"></a>vhd</strong>, <strong id="b8423527069750"><a name="b8423527069750"></a><a name="b8423527069750"></a>raw</strong>, <strong id="b842352706172914"><a name="b842352706172914"></a><a name="b842352706172914"></a>zvhd</strong>, or <strong id="b8423527069758"><a name="b8423527069758"></a><a name="b8423527069758"></a>qcow2</strong>. The default value is <strong id="b842352706165234"><a name="b842352706165234"></a><a name="b842352706165234"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="row1650032219484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p6145769619484"><a name="p6145769619484"></a><a name="p6145769619484"></a>__isregistered</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p1201748319484"><a name="p1201748319484"></a><a name="p1201748319484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p3389204219484"><a name="p3389204219484"></a><a name="p3389204219484"></a>Specifies whether the image has been registered. The value can be <strong>true</strong> or <strong>false</strong>.</p>
    </td>
    </tr>
    <tr id="row3659292519484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1123691819484"><a name="p1123691819484"></a><a name="p1123691819484"></a>__platform</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p3777512719484"><a name="p3777512719484"></a><a name="p3777512719484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p3988644119484"><a name="p3988644119484"></a><a name="p3988644119484"></a>Specifies the image platform type. The value can be <strong id="b42401919105018"><a name="b42401919105018"></a><a name="b42401919105018"></a>Windows</strong>, <strong id="b20240181925016"><a name="b20240181925016"></a><a name="b20240181925016"></a>Ubuntu</strong>, <strong id="b12416199502"><a name="b12416199502"></a><a name="b12416199502"></a>RedHat</strong>, <strong id="b1624131955012"><a name="b1624131955012"></a><a name="b1624131955012"></a>SUSE</strong>, <strong id="b182428194509"><a name="b182428194509"></a><a name="b182428194509"></a>CentOS</strong>, <strong id="b16242019155020"><a name="b16242019155020"></a><a name="b16242019155020"></a>Debian</strong>, <strong id="b182431019175015"><a name="b182431019175015"></a><a name="b182431019175015"></a>OpenSUSE</strong>, <strong id="b19243171975014"><a name="b19243171975014"></a><a name="b19243171975014"></a>Oracle Linux</strong>, <strong id="b924421965018"><a name="b924421965018"></a><a name="b924421965018"></a>Fedora</strong>, <strong id="b13244121911506"><a name="b13244121911506"></a><a name="b13244121911506"></a>Other</strong>, <strong id="b3244151919505"><a name="b3244151919505"></a><a name="b3244151919505"></a>CoreOS</strong>, or <strong id="b12451419195018"><a name="b12451419195018"></a><a name="b12451419195018"></a>EulerOS</strong>.</p>
    </td>
    </tr>
    <tr id="row2343365119484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1907761719484"><a name="p1907761719484"></a><a name="p1907761719484"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p178315519484"><a name="p178315519484"></a><a name="p178315519484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p1021789019484"><a name="p1021789019484"></a><a name="p1021789019484"></a>Specifies the OS type. The value can be <strong id="b15589822145011"><a name="b15589822145011"></a><a name="b15589822145011"></a>Linux</strong>, <strong id="b10590822125013"><a name="b10590822125013"></a><a name="b10590822125013"></a>Windows</strong>, or <strong id="b18590122145013"><a name="b18590122145013"></a><a name="b18590122145013"></a>Other</strong>.</p>
    </td>
    </tr>
    <tr id="row2485214919484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p6686709019484"><a name="p6686709019484"></a><a name="p6686709019484"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p4752519919484"><a name="p4752519919484"></a><a name="p4752519919484"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p60826909104315"><a name="p60826909104315"></a><a name="p60826909104315"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
    </td>
    </tr>
    <tr id="row1769644219484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p2412566319484"><a name="p2412566319484"></a><a name="p2412566319484"></a>virtual_env_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p802166419484"><a name="p802166419484"></a><a name="p802166419484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p125511012134911"><a name="p125511012134911"></a><a name="p125511012134911"></a>Specifies the environment where the image is used. The value can be <strong id="b1988018246509"><a name="b1988018246509"></a><a name="b1988018246509"></a>FusionCompute</strong>, <strong id="b1488022415502"><a name="b1488022415502"></a><a name="b1488022415502"></a>Ironic</strong>, or <strong id="b688132485016"><a name="b688132485016"></a><a name="b688132485016"></a>DataImage</strong>.</p>
    <a name="ul15999422124917"></a><a name="ul15999422124917"></a><ul id="ul15999422124917"><li>For an <span id="text168181855131912"><a name="text168181855131912"></a><a name="text168181855131912"></a></span><span id="text17819455121914"><a name="text17819455121914"></a><a name="text17819455121914"></a>ECS</span> image (system disk image), the value is <strong id="b158201855111918"><a name="b158201855111918"></a><a name="b158201855111918"></a>FusionCompute</strong>.</li><li>For a data disk image, the value is <strong id="b22449504126"><a name="b22449504126"></a><a name="b22449504126"></a>DataImage</strong>.</li><li>For a <span id="text29262115203"><a name="text29262115203"></a><a name="text29262115203"></a></span><span id="text392651112013"><a name="text392651112013"></a><a name="text392651112013"></a>BMS</span> image, the value is <strong id="b1692717114205"><a name="b1692717114205"></a><a name="b1692717114205"></a>Ironic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row932252719484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1692720719484"><a name="p1692720719484"></a><a name="p1692720719484"></a>__image_source_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p2892650319484"><a name="p2892650319484"></a><a name="p2892650319484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p6134541619484"><a name="p6134541619484"></a><a name="p6134541619484"></a>Specifies the image backend storage type. Only UDS is supported currently. </p>
    </td>
    </tr>
    <tr id="row1523783619484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p2630521719484"><a name="p2630521719484"></a><a name="p2630521719484"></a>__imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p5034781819484"><a name="p5034781819484"></a><a name="p5034781819484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p28701642133010"><a name="p28701642133010"></a><a name="p28701642133010"></a>Specifies the image type. The following types are supported:</p>
    <a name="ul387034210305"></a><a name="ul387034210305"></a><ul id="ul387034210305"><li>Public image: The value is <strong id="b842352706163515"><a name="b842352706163515"></a><a name="b842352706163515"></a>gold</strong>.</li><li>Private image: The value is <strong id="b1762610292163524"><a name="b1762610292163524"></a><a name="b1762610292163524"></a>private</strong>.</li><li>Shared image: The value is <strong id="b298092137163545"><a name="b298092137163545"></a><a name="b298092137163545"></a>shared</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row6211992119484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p6565767619484"><a name="p6565767619484"></a><a name="p6565767619484"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p1667154419484"><a name="p1667154419484"></a><a name="p1667154419484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p821782019484"><a name="p821782019484"></a><a name="p821782019484"></a>Specifies the time when the image was created. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row685152319484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1810251119484"><a name="p1810251119484"></a><a name="p1810251119484"></a>virtual_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p5701732019484"><a name="p5701732019484"></a><a name="p5701732019484"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p5500021319484"><a name="p5500021319484"></a><a name="p5500021319484"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row2523987519484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p3116399419484"><a name="p3116399419484"></a><a name="p3116399419484"></a>deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p4125557719484"><a name="p4125557719484"></a><a name="p4125557719484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p5336746519484"><a name="p5336746519484"></a><a name="p5336746519484"></a>Specifies the time when the image was deleted. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row1054514319484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p4885024319484"><a name="p4885024319484"></a><a name="p4885024319484"></a>__originalimagename</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p6455557119484"><a name="p6455557119484"></a><a name="p6455557119484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p6161873519484"><a name="p6161873519484"></a><a name="p6161873519484"></a>Specifies the parent image ID.</p>
    <p id="p1769771019484"><a name="p1769771019484"></a><a name="p1769771019484"></a>If the image is a public image or created from an image file, this value is left empty.</p>
    </td>
    </tr>
    <tr id="row2506166419484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p1672894219484"><a name="p1672894219484"></a><a name="p1672894219484"></a>__backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p1286707219484"><a name="p1286707219484"></a><a name="p1286707219484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p3559993519484"><a name="p3559993519484"></a><a name="p3559993519484"></a>Specifies the backup ID. To create an image using a backup, set the value to the backup ID. Otherwise, this value is left empty.</p>
    </td>
    </tr>
    <tr id="row5196396219484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p4833143119484"><a name="p4833143119484"></a><a name="p4833143119484"></a>__productcode</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p2253182819484"><a name="p2253182819484"></a><a name="p2253182819484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p1313876119484"><a name="p1313876119484"></a><a name="p1313876119484"></a>Specifies the ID of the market image product.</p>
    </td>
    </tr>
    <tr id="row5427752419484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p3440330819484"><a name="p3440330819484"></a><a name="p3440330819484"></a>__image_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p3520454019484"><a name="p3520454019484"></a><a name="p3520454019484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p3299550119484"><a name="p3299550119484"></a><a name="p3299550119484"></a>Specifies the size (bytes) of the image file. The value is greater than 0.</p>
    </td>
    </tr>
    <tr id="row2852405719484"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p2874729419484"><a name="p2874729419484"></a><a name="p2874729419484"></a>__data_origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p4682946319484"><a name="p4682946319484"></a><a name="p4682946319484"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p3509015719484"><a name="p3509015719484"></a><a name="p3509015719484"></a>Specifies the image resource.</p>
    <p id="p4737595819484"><a name="p4737595819484"></a><a name="p4737595819484"></a>If the image is a public image, this parameter is left empty.</p>
    </td>
    </tr>
    <tr id="row55821842155911"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p25275315155911"><a name="p25275315155911"></a><a name="p25275315155911"></a>__sequence_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p5341551155911"><a name="p5341551155911"></a><a name="p5341551155911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p30012506155911"><a name="p30012506155911"></a><a name="p30012506155911"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row59643047203735"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p580552184954"><a name="p580552184954"></a><a name="p580552184954"></a>__support_kvm</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p27540563184954"><a name="p27540563184954"></a><a name="p27540563184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p46304701184954"><a name="p46304701184954"></a><a name="p46304701184954"></a>Specifies whether the image supports KVM. If yes, the value is <strong id="b842352706174145"><a name="b842352706174145"></a><a name="b842352706174145"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row3882825120219"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p23167082184954"><a name="p23167082184954"></a><a name="p23167082184954"></a>__support_xen</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p11995013184954"><a name="p11995013184954"></a><a name="p11995013184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p4154542184954"><a name="p4154542184954"></a><a name="p4154542184954"></a>Specifies whether the image supports Xen. If yes, the value is <strong id="b40128715692258"><a name="b40128715692258"></a><a name="b40128715692258"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row58626039202222"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p39000938184954"><a name="p39000938184954"></a><a name="p39000938184954"></a>__support_largememory</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p57096932184954"><a name="p57096932184954"></a><a name="p57096932184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p651492811217"><a name="p651492811217"></a><a name="p651492811217"></a>Specifies whether the image supports large-memory ECSs. If the image supports large-memory ECSs, the value is <strong id="b125621014125720"><a name="b125621014125720"></a><a name="b125621014125720"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p20363134065018"><a name="p20363134065018"></a><a name="p20363134065018"></a>For the supported OSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
    <p id="p1734114582112"><a name="p1734114582112"></a><a name="p1734114582112"></a></p>
    </td>
    </tr>
    <tr id="row43057536203728"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p47581434184954"><a name="p47581434184954"></a><a name="p47581434184954"></a>__support_diskintensive</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p50609959184954"><a name="p50609959184954"></a><a name="p50609959184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p20887878184954"><a name="p20887878184954"></a><a name="p20887878184954"></a>Specifies whether the image supports disk-intensive ECSs. If the image supports disk-intensive ECSs, the value is <strong id="b842352706174145_1"><a name="b842352706174145_1"></a><a name="b842352706174145_1"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row39724815224743"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p17123543184954"><a name="p17123543184954"></a><a name="p17123543184954"></a>__support_highperformance</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p38086855184954"><a name="p38086855184954"></a><a name="p38086855184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p17225863184954"><a name="p17225863184954"></a><a name="p17225863184954"></a>Specifies whether the image supports high-performance ECSs. If the image supports high-performance ECSs, the value is <strong id="b842352706174145_2"><a name="b842352706174145_2"></a><a name="b842352706174145_2"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row62323042204110"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p26024330184954"><a name="p26024330184954"></a><a name="p26024330184954"></a>__support_xen_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p15739313184954"><a name="p15739313184954"></a><a name="p15739313184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p23482902184954"><a name="p23482902184954"></a><a name="p23482902184954"></a>The image supports GPU-optimized ECSs on the Xen platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the Xen platform, this attribute is not required. This attribute cannot co-exist with <strong id="b842352706175423"><a name="b842352706175423"></a><a name="b842352706175423"></a>__support_xen</strong> and <strong id="b842352706175430"><a name="b842352706175430"></a><a name="b842352706175430"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row1584552720426"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p44343300184954"><a name="p44343300184954"></a><a name="p44343300184954"></a>__support_kvm_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p66845928184954"><a name="p66845928184954"></a><a name="p66845928184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p29779677184954"><a name="p29779677184954"></a><a name="p29779677184954"></a>Specifies whether the image supports GPU-optimized ECSs on the KVM platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value.</p>
    <p id="p44348954184954"><a name="p44348954184954"></a><a name="p44348954184954"></a>If the image does not support GPU-optimized ECSs on the KVM platform, this attribute is not required. This attribute cannot co-exist with <strong id="b842352706175423_1"><a name="b842352706175423_1"></a><a name="b842352706175423_1"></a>__support_xen</strong> and <strong id="b842352706175430_1"><a name="b842352706175430_1"></a><a name="b842352706175430_1"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row16941346204313"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p7047919184954"><a name="p7047919184954"></a><a name="p7047919184954"></a>__support_xen_hana</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p47139696184954"><a name="p47139696184954"></a><a name="p47139696184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p66284528184954"><a name="p66284528184954"></a><a name="p66284528184954"></a>Specifies whether the image supports HANA ECSs on the Xen platform. If yes, the value is <strong id="b1066553282174316"><a name="b1066553282174316"></a><a name="b1066553282174316"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p32685305184954"><a name="p32685305184954"></a><a name="p32685305184954"></a>This attribute cannot co-exist with <strong id="b842352706175423_2"><a name="b842352706175423_2"></a><a name="b842352706175423_2"></a>__support_xen</strong> and <strong id="b842352706175430_2"><a name="b842352706175430_2"></a><a name="b842352706175430_2"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row2879248184946"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p2966201184954"><a name="p2966201184954"></a><a name="p2966201184954"></a>__support_kvm_infiniband</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p38078563184954"><a name="p38078563184954"></a><a name="p38078563184954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p16027374184954"><a name="p16027374184954"></a><a name="p16027374184954"></a>Specifies whether the image supports ECSs with the InfiniBand NIC on the KVM platform. If yes, the value is <strong id="b2040161919154726"><a name="b2040161919154726"></a><a name="b2040161919154726"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p2859675184954"><a name="p2859675184954"></a><a name="p2859675184954"></a>This attribute cannot co-exist with <strong id="b842352706175423_3"><a name="b842352706175423_3"></a><a name="b842352706175423_3"></a>__support_xen</strong>.</p>
    </td>
    </tr>
    <tr id="row159155884217"><td class="cellrowborder" valign="top" width="36.9%" headers="mcps1.1.4.1.1 "><p id="p162261715424"><a name="p162261715424"></a><a name="p162261715424"></a>hw_firmware_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.700000000000003%" headers="mcps1.1.4.1.2 "><p id="p1522517164219"><a name="p1522517164219"></a><a name="p1522517164219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.4%" headers="mcps1.1.4.1.3 "><p id="p11221517194218"><a name="p11221517194218"></a><a name="p11221517194218"></a>Specifies the <span id="text10170135018161"><a name="text10170135018161"></a><a name="text10170135018161"></a></span><span id="text17171115016162"><a name="text17171115016162"></a><a name="text17171115016162"></a>ECS</span> boot mode. Available values include:</p>
    <a name="ul1122141720424"></a><a name="ul1122141720424"></a><ul id="ul1122141720424"><li><strong id="b1566421813282"><a name="b1566421813282"></a><a name="b1566421813282"></a>bios</strong> indicates the BIOS boot mode.</li><li><strong id="b663171914285"><a name="b663171914285"></a><a name="b663171914285"></a>uefi</strong> indicates the UEFI boot mode.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    STATUS CODE 200
    ```

    ```
    {
          "schema": "/v2/schemas/image",
          "min_disk": 100,
          "created_at": "2018-09-06T14:03:27Z",
          "__image_source_type": "uds",
          "container_format": "bare",
          "file": "/v2/images/bc6bed6e-ba3a-4447-afcc-449174a3eb52/file",
          "updated_at": "2018-09-06T15:17:33Z",
          "protected": true,
          "checksum": "d41d8cd98f00b204e9800998ecf8427e",
          "__support_kvm_fpga_type": "VU9P",
          "id": "bc6bed6e-ba3a-4447-afcc-449174a3eb52",
          "__isregistered": "true",
          "min_ram": 2048,
          "__lazyloading": "true",
          "owner": "1bed856811654c1cb661a6ca845ebc77",
          "__os_type": "Linux",
          "__imagetype": "gold",
          "visibility": "public",
          "virtual_env_type": "FusionCompute",
          "tags": [],
          "__platform": "CentOS",
          "size": 0,
          "__os_bit": "64",
          "__os_version": "CentOS 7.3 64bit",
          "name": "CentOS 7.3 64bit vivado",
          "self": "/v2/images/bc6bed6e-ba3a-4447-afcc-449174a3eb52",
          "disk_format": "zvhd2",
          "virtual_size": null,
          "status": "active"
    }
    ```


## Returned Values<a name="section37356392"></a>

-   Normal

    200

-   Abnormal

    <a name="table262968317230"></a>
    <table><thead align="left"><tr id="row5740081817230"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p1895465817230"><a name="p1895465817230"></a><a name="p1895465817230"></a><strong id="b84235270616412"><a name="b84235270616412"></a><a name="b84235270616412"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p5893233917230"><a name="p5893233917230"></a><a name="p5893233917230"></a><strong id="b84235270616415"><a name="b84235270616415"></a><a name="b84235270616415"></a>Description</strong></p>
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


