# Querying Tags<a name="EN-US_TOPIC_0067360382"></a>

## Function<a name="section66482596175825"></a>

This API is used to query image tags using search criteria and display them in a list.

## URI<a name="section64320492175833"></a>

GET /v1/cloudimages/tags

>![](/images/icon-note.gif) **NOTE:**   
>You can type a question mark \(?\) and an ampersand \(&\) at the end of the URI to define multiple search criteria. For details, see the example request.  

## Request<a name="section65284921175841"></a>

-   Request parameters

    <a name="table867855184219"></a>
    <table><thead align="left"><tr id="en-us_topic_0020091565_row18662125134212"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.1"><p id="en-us_topic_0020091565_p16621584210"><a name="en-us_topic_0020091565_p16621584210"></a><a name="en-us_topic_0020091565_p16621584210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.1.5.1.2"><p id="en-us_topic_0020091565_p7662157429"><a name="en-us_topic_0020091565_p7662157429"></a><a name="en-us_topic_0020091565_p7662157429"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.3"><p id="en-us_topic_0020091565_p9662254429"><a name="en-us_topic_0020091565_p9662254429"></a><a name="en-us_topic_0020091565_p9662254429"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.1.5.1.4"><p id="en-us_topic_0020091565_p66625524217"><a name="en-us_topic_0020091565_p66625524217"></a><a name="en-us_topic_0020091565_p66625524217"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020091565_row866310519425"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p1866216511420"><a name="en-us_topic_0020091565_p1866216511420"></a><a name="en-us_topic_0020091565_p1866216511420"></a>__isregistered</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p3663125164212"><a name="en-us_topic_0020091565_p3663125164212"></a><a name="en-us_topic_0020091565_p3663125164212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p196631756427"><a name="en-us_topic_0020091565_p196631756427"></a><a name="en-us_topic_0020091565_p196631756427"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1566325104216"><a name="en-us_topic_0020091565_p1566325104216"></a><a name="en-us_topic_0020091565_p1566325104216"></a>Specifies whether the image is available. The value can be <strong id="en-us_topic_0020091565_b84235270616222"><a name="en-us_topic_0020091565_b84235270616222"></a><a name="en-us_topic_0020091565_b84235270616222"></a>true</strong>. The value is <strong id="en-us_topic_0020091565_b2049464823162253"><a name="en-us_topic_0020091565_b2049464823162253"></a><a name="en-us_topic_0020091565_b2049464823162253"></a>true</strong> for all extension APIs by default. Common users can query only the images for which the value of this parameter is <strong id="en-us_topic_0020091565_b846915150162332"><a name="en-us_topic_0020091565_b846915150162332"></a><a name="en-us_topic_0020091565_b846915150162332"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row866345194215"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p1066355184213"><a name="en-us_topic_0020091565_p1066355184213"></a><a name="en-us_topic_0020091565_p1066355184213"></a>__imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p1663205114212"><a name="en-us_topic_0020091565_p1663205114212"></a><a name="en-us_topic_0020091565_p1663205114212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p466313544218"><a name="en-us_topic_0020091565_p466313544218"></a><a name="en-us_topic_0020091565_p466313544218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p66631551425"><a name="en-us_topic_0020091565_p66631551425"></a><a name="en-us_topic_0020091565_p66631551425"></a>Specifies the image type. The following types are supported:</p>
    <a name="en-us_topic_0020091565_ul26635584212"></a><a name="en-us_topic_0020091565_ul26635584212"></a><ul id="en-us_topic_0020091565_ul26635584212"><li>Public image: The value is <strong id="en-us_topic_0020091565_b842352706163515"><a name="en-us_topic_0020091565_b842352706163515"></a><a name="en-us_topic_0020091565_b842352706163515"></a>gold</strong>.</li><li>Private image: The value is <strong id="en-us_topic_0020091565_b1762610292163524"><a name="en-us_topic_0020091565_b1762610292163524"></a><a name="en-us_topic_0020091565_b1762610292163524"></a>private</strong>.</li><li>Shared image: The value is <strong id="en-us_topic_0020091565_b298092137163545"><a name="en-us_topic_0020091565_b298092137163545"></a><a name="en-us_topic_0020091565_b298092137163545"></a>shared</strong>.</li></ul>
    <div class="note" id="en-us_topic_0020091565_note7533222103412"><a name="en-us_topic_0020091565_note7533222103412"></a><a name="en-us_topic_0020091565_note7533222103412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0020091565_p653413224345"><a name="en-us_topic_0020091565_p653413224345"></a><a name="en-us_topic_0020091565_p653413224345"></a>The <strong id="en-us_topic_0020091565_b246710191919"><a name="en-us_topic_0020091565_b246710191919"></a><a name="en-us_topic_0020091565_b246710191919"></a>__imagetype</strong> of images you share with other tenants or those other tenants share with you and you have accepted is <strong id="en-us_topic_0020091565_b1762175571915"><a name="en-us_topic_0020091565_b1762175571915"></a><a name="en-us_topic_0020091565_b1762175571915"></a>shared</strong>. You can use field <strong id="en-us_topic_0020091565_b6237171042012"><a name="en-us_topic_0020091565_b6237171042012"></a><a name="en-us_topic_0020091565_b6237171042012"></a>owner</strong> to distinguish the two types of shared images. You can use <strong id="en-us_topic_0020091565_b13751829223"><a name="en-us_topic_0020091565_b13751829223"></a><a name="en-us_topic_0020091565_b13751829223"></a>member_status</strong> to filter out shared images you have accepted.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row06401901946"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p9641120347"><a name="en-us_topic_0020091565_p9641120347"></a><a name="en-us_topic_0020091565_p9641120347"></a>__whole_image</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p264160844"><a name="en-us_topic_0020091565_p264160844"></a><a name="en-us_topic_0020091565_p264160844"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1064117013414"><a name="en-us_topic_0020091565_p1064117013414"></a><a name="en-us_topic_0020091565_p1064117013414"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p36411603417"><a name="en-us_topic_0020091565_p36411603417"></a><a name="en-us_topic_0020091565_p36411603417"></a>Specifies whether the image is a full-ECS image. The value can be <strong id="en-us_topic_0020091565_b19541329194712"><a name="en-us_topic_0020091565_b19541329194712"></a><a name="en-us_topic_0020091565_b19541329194712"></a>true</strong> or <strong id="en-us_topic_0020091565_b858493314714"><a name="en-us_topic_0020091565_b858493314714"></a><a name="en-us_topic_0020091565_b858493314714"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row1663165194213"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p12663359421"><a name="en-us_topic_0020091565_p12663359421"></a><a name="en-us_topic_0020091565_p12663359421"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p666315174216"><a name="en-us_topic_0020091565_p666315174216"></a><a name="en-us_topic_0020091565_p666315174216"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p866385174216"><a name="en-us_topic_0020091565_p866385174216"></a><a name="en-us_topic_0020091565_p866385174216"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p26631856423"><a name="en-us_topic_0020091565_p26631856423"></a><a name="en-us_topic_0020091565_p26631856423"></a>Specifies whether the image is protected. The value can be <strong id="en-us_topic_0020091565_b842352706113632"><a name="en-us_topic_0020091565_b842352706113632"></a><a name="en-us_topic_0020091565_b842352706113632"></a>true</strong> or <strong id="en-us_topic_0020091565_b842352706113636"><a name="en-us_topic_0020091565_b842352706113636"></a><a name="en-us_topic_0020091565_b842352706113636"></a>false</strong>. Set it to <strong id="en-us_topic_0020091565_b48612739142847_1"><a name="en-us_topic_0020091565_b48612739142847_1"></a><a name="en-us_topic_0020091565_b48612739142847_1"></a>true</strong> when you query public images. This parameter is optional when you query private images.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row136641510425"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p866316513424"><a name="en-us_topic_0020091565_p866316513424"></a><a name="en-us_topic_0020091565_p866316513424"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p366465184215"><a name="en-us_topic_0020091565_p366465184215"></a><a name="en-us_topic_0020091565_p366465184215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p166410544212"><a name="en-us_topic_0020091565_p166410544212"></a><a name="en-us_topic_0020091565_p166410544212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1480263817401"><a name="en-us_topic_0020091565_p1480263817401"></a><a name="en-us_topic_0020091565_p1480263817401"></a>Specifies whether the image is available to other tenants. Available values include:</p>
    <a name="en-us_topic_0020091565_ul111418194429"></a><a name="en-us_topic_0020091565_ul111418194429"></a><ul id="en-us_topic_0020091565_ul111418194429"><li><strong id="en-us_topic_0020091565_b18991733105115"><a name="en-us_topic_0020091565_b18991733105115"></a><a name="en-us_topic_0020091565_b18991733105115"></a>public</strong>: public image</li><li><strong id="en-us_topic_0020091565_b842352706114634"><a name="en-us_topic_0020091565_b842352706114634"></a><a name="en-us_topic_0020091565_b842352706114634"></a>private</strong>: private image</li><li><strong id="en-us_topic_0020091565_b1823217295616"><a name="en-us_topic_0020091565_b1823217295616"></a><a name="en-us_topic_0020091565_b1823217295616"></a>shared</strong>: shared image</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row36641515426"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p166641052420"><a name="en-us_topic_0020091565_p166641052420"></a><a name="en-us_topic_0020091565_p166641052420"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p1366419504215"><a name="en-us_topic_0020091565_p1366419504215"></a><a name="en-us_topic_0020091565_p1366419504215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1866416511428"><a name="en-us_topic_0020091565_p1866416511428"></a><a name="en-us_topic_0020091565_p1866416511428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p4664115134213"><a name="en-us_topic_0020091565_p4664115134213"></a><a name="en-us_topic_0020091565_p4664115134213"></a>Specifies the image owner.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row1066420574214"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p14664145164210"><a name="en-us_topic_0020091565_p14664145164210"></a><a name="en-us_topic_0020091565_p14664145164210"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p136641650427"><a name="en-us_topic_0020091565_p136641650427"></a><a name="en-us_topic_0020091565_p136641650427"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1266416514421"><a name="en-us_topic_0020091565_p1266416514421"></a><a name="en-us_topic_0020091565_p1266416514421"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1266425204213"><a name="en-us_topic_0020091565_p1266425204213"></a><a name="en-us_topic_0020091565_p1266425204213"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row1666565144210"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p17664252421"><a name="en-us_topic_0020091565_p17664252421"></a><a name="en-us_topic_0020091565_p17664252421"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p46642520425"><a name="en-us_topic_0020091565_p46642520425"></a><a name="en-us_topic_0020091565_p46642520425"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p156641157428"><a name="en-us_topic_0020091565_p156641157428"></a><a name="en-us_topic_0020091565_p156641157428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p56641756429"><a name="en-us_topic_0020091565_p56641756429"></a><a name="en-us_topic_0020091565_p56641756429"></a>Specifies the image status. The value can be one of the following:</p>
    <a name="en-us_topic_0020091565_ul46651451422"></a><a name="en-us_topic_0020091565_ul46651451422"></a><ul id="en-us_topic_0020091565_ul46651451422"><li><strong id="en-us_topic_0020091565_b842352706103333"><a name="en-us_topic_0020091565_b842352706103333"></a><a name="en-us_topic_0020091565_b842352706103333"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="en-us_topic_0020091565_b842352706104325"><a name="en-us_topic_0020091565_b842352706104325"></a><a name="en-us_topic_0020091565_b842352706104325"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="en-us_topic_0020091565_b842352706104450"><a name="en-us_topic_0020091565_b842352706104450"></a><a name="en-us_topic_0020091565_b842352706104450"></a>deleted</strong>: indicates that the image has been deleted.</li><li><strong id="en-us_topic_0020091565_b842352706104518"><a name="en-us_topic_0020091565_b842352706104518"></a><a name="en-us_topic_0020091565_b842352706104518"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="en-us_topic_0020091565_b842352706104558"><a name="en-us_topic_0020091565_b842352706104558"></a><a name="en-us_topic_0020091565_b842352706104558"></a>active</strong>: indicates that the image is available for use. </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row5665752427"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p4665165194214"><a name="en-us_topic_0020091565_p4665165194214"></a><a name="en-us_topic_0020091565_p4665165194214"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p966545204211"><a name="en-us_topic_0020091565_p966545204211"></a><a name="en-us_topic_0020091565_p966545204211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p136654544219"><a name="en-us_topic_0020091565_p136654544219"></a><a name="en-us_topic_0020091565_p136654544219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p36658534216"><a name="en-us_topic_0020091565_p36658534216"></a><a name="en-us_topic_0020091565_p36658534216"></a>Specifies the image name. Exact matching is used. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row11666551426"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p12665115194213"><a name="en-us_topic_0020091565_p12665115194213"></a><a name="en-us_topic_0020091565_p12665115194213"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p1266515104210"><a name="en-us_topic_0020091565_p1266515104210"></a><a name="en-us_topic_0020091565_p1266515104210"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1666510515424"><a name="en-us_topic_0020091565_p1666510515424"></a><a name="en-us_topic_0020091565_p1666510515424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p116661953423"><a name="en-us_topic_0020091565_p116661953423"></a><a name="en-us_topic_0020091565_p116661953423"></a>Specifies the container type. The value is <strong id="en-us_topic_0020091565_b842352706192014"><a name="en-us_topic_0020091565_b842352706192014"></a><a name="en-us_topic_0020091565_b842352706192014"></a>bare</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row866619519425"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p1566618511424"><a name="en-us_topic_0020091565_p1566618511424"></a><a name="en-us_topic_0020091565_p1566618511424"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p186661255424"><a name="en-us_topic_0020091565_p186661255424"></a><a name="en-us_topic_0020091565_p186661255424"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p26666515421"><a name="en-us_topic_0020091565_p26666515421"></a><a name="en-us_topic_0020091565_p26666515421"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p266685184211"><a name="en-us_topic_0020091565_p266685184211"></a><a name="en-us_topic_0020091565_p266685184211"></a>Specifies the image format. The value can be <strong id="en-us_topic_0020091565_b144536448521"><a name="en-us_topic_0020091565_b144536448521"></a><a name="en-us_topic_0020091565_b144536448521"></a>vhd</strong>, <strong id="en-us_topic_0020091565_b19454194415210"><a name="en-us_topic_0020091565_b19454194415210"></a><a name="en-us_topic_0020091565_b19454194415210"></a>raw</strong>, <strong id="en-us_topic_0020091565_b145544445210"><a name="en-us_topic_0020091565_b145544445210"></a><a name="en-us_topic_0020091565_b145544445210"></a>zvhd</strong>, or <strong id="en-us_topic_0020091565_b1645611449521"><a name="en-us_topic_0020091565_b1645611449521"></a><a name="en-us_topic_0020091565_b1645611449521"></a>qcow2</strong>. The default value is <strong id="en-us_topic_0020091565_b842352706165234"><a name="en-us_topic_0020091565_b842352706165234"></a><a name="en-us_topic_0020091565_b842352706165234"></a>zvhd2</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row2066612519428"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p266612514421"><a name="en-us_topic_0020091565_p266612514421"></a><a name="en-us_topic_0020091565_p266612514421"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p7666145124217"><a name="en-us_topic_0020091565_p7666145124217"></a><a name="en-us_topic_0020091565_p7666145124217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p2666115194210"><a name="en-us_topic_0020091565_p2666115194210"></a><a name="en-us_topic_0020091565_p2666115194210"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p8666953422"><a name="en-us_topic_0020091565_p8666953422"></a><a name="en-us_topic_0020091565_p8666953422"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the <span id="en-us_topic_0020091565_text1343072215515"><a name="en-us_topic_0020091565_text1343072215515"></a><a name="en-us_topic_0020091565_text1343072215515"></a></span><span id="en-us_topic_0020091565_text92721735125119"><a name="en-us_topic_0020091565_text92721735125119"></a><a name="en-us_topic_0020091565_text92721735125119"></a>ECS</span> specifications. Generally, the value is <strong id="en-us_topic_0020091565_b1986818338377"><a name="en-us_topic_0020091565_b1986818338377"></a><a name="en-us_topic_0020091565_b1986818338377"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row116673517423"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p2666355425"><a name="en-us_topic_0020091565_p2666355425"></a><a name="en-us_topic_0020091565_p2666355425"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p666675194212"><a name="en-us_topic_0020091565_p666675194212"></a><a name="en-us_topic_0020091565_p666675194212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p6666125124212"><a name="en-us_topic_0020091565_p6666125124212"></a><a name="en-us_topic_0020091565_p6666125124212"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p16671651424"><a name="en-us_topic_0020091565_p16671651424"></a><a name="en-us_topic_0020091565_p16671651424"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row5667165154210"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p766710510425"><a name="en-us_topic_0020091565_p766710510425"></a><a name="en-us_topic_0020091565_p766710510425"></a>__os_bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p866715517421"><a name="en-us_topic_0020091565_p866715517421"></a><a name="en-us_topic_0020091565_p866715517421"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p2667125124213"><a name="en-us_topic_0020091565_p2667125124213"></a><a name="en-us_topic_0020091565_p2667125124213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1166745154214"><a name="en-us_topic_0020091565_p1166745154214"></a><a name="en-us_topic_0020091565_p1166745154214"></a>Specifies the OS architecture, 32 bit or 64 bit.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row1966812510428"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p66677544211"><a name="en-us_topic_0020091565_p66677544211"></a><a name="en-us_topic_0020091565_p66677544211"></a>__platform</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p16667145204212"><a name="en-us_topic_0020091565_p16667145204212"></a><a name="en-us_topic_0020091565_p16667145204212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p4667195184213"><a name="en-us_topic_0020091565_p4667195184213"></a><a name="en-us_topic_0020091565_p4667195184213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p66679515425"><a name="en-us_topic_0020091565_p66679515425"></a><a name="en-us_topic_0020091565_p66679515425"></a>Specifies the image platform type. The value can be <strong id="en-us_topic_0020091565_b54511332185320"><a name="en-us_topic_0020091565_b54511332185320"></a><a name="en-us_topic_0020091565_b54511332185320"></a>Windows</strong>, <strong id="en-us_topic_0020091565_b144527320539"><a name="en-us_topic_0020091565_b144527320539"></a><a name="en-us_topic_0020091565_b144527320539"></a>Ubuntu</strong>, <strong id="en-us_topic_0020091565_b174521232125310"><a name="en-us_topic_0020091565_b174521232125310"></a><a name="en-us_topic_0020091565_b174521232125310"></a>RedHat</strong>, <strong id="en-us_topic_0020091565_b34532320533"><a name="en-us_topic_0020091565_b34532320533"></a><a name="en-us_topic_0020091565_b34532320533"></a>SUSE</strong>, <strong id="en-us_topic_0020091565_b1445316328538"><a name="en-us_topic_0020091565_b1445316328538"></a><a name="en-us_topic_0020091565_b1445316328538"></a>CentOS</strong>, <strong id="en-us_topic_0020091565_b5454153265320"><a name="en-us_topic_0020091565_b5454153265320"></a><a name="en-us_topic_0020091565_b5454153265320"></a>Debian</strong>, <strong id="en-us_topic_0020091565_b1945416327536"><a name="en-us_topic_0020091565_b1945416327536"></a><a name="en-us_topic_0020091565_b1945416327536"></a>OpenSUSE</strong>, <strong id="en-us_topic_0020091565_b54557321535"><a name="en-us_topic_0020091565_b54557321535"></a><a name="en-us_topic_0020091565_b54557321535"></a>Oracle Linux</strong>, <strong id="en-us_topic_0020091565_b545623255320"><a name="en-us_topic_0020091565_b545623255320"></a><a name="en-us_topic_0020091565_b545623255320"></a>Fedora</strong>, <strong id="en-us_topic_0020091565_b164564321538"><a name="en-us_topic_0020091565_b164564321538"></a><a name="en-us_topic_0020091565_b164564321538"></a>Other</strong>, <strong id="en-us_topic_0020091565_b64571532195311"><a name="en-us_topic_0020091565_b64571532195311"></a><a name="en-us_topic_0020091565_b64571532195311"></a>CoreOS</strong>, or <strong id="en-us_topic_0020091565_b1345717329530"><a name="en-us_topic_0020091565_b1345717329530"></a><a name="en-us_topic_0020091565_b1345717329530"></a>EulerOS</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row16686504210"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p56680584218"><a name="en-us_topic_0020091565_p56680584218"></a><a name="en-us_topic_0020091565_p56680584218"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p9668559427"><a name="en-us_topic_0020091565_p9668559427"></a><a name="en-us_topic_0020091565_p9668559427"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1866845194219"><a name="en-us_topic_0020091565_p1866845194219"></a><a name="en-us_topic_0020091565_p1866845194219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p566835104216"><a name="en-us_topic_0020091565_p566835104216"></a><a name="en-us_topic_0020091565_p566835104216"></a>Specifies the start number from which images are queried. The value is the image ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row4668258426"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p066813534216"><a name="en-us_topic_0020091565_p066813534216"></a><a name="en-us_topic_0020091565_p066813534216"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p566815534214"><a name="en-us_topic_0020091565_p566815534214"></a><a name="en-us_topic_0020091565_p566815534214"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p466814564214"><a name="en-us_topic_0020091565_p466814564214"></a><a name="en-us_topic_0020091565_p466814564214"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p666885174218"><a name="en-us_topic_0020091565_p666885174218"></a><a name="en-us_topic_0020091565_p666885174218"></a>Specifies the number of images to be queried. The value is an integer and is <strong id="en-us_topic_0020091565_b3988183415491"><a name="en-us_topic_0020091565_b3988183415491"></a><a name="en-us_topic_0020091565_b3988183415491"></a>500</strong> by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row1166945124218"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p136682544216"><a name="en-us_topic_0020091565_p136682544216"></a><a name="en-us_topic_0020091565_p136682544216"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p1166813584217"><a name="en-us_topic_0020091565_p1166813584217"></a><a name="en-us_topic_0020091565_p1166813584217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p116684513428"><a name="en-us_topic_0020091565_p116684513428"></a><a name="en-us_topic_0020091565_p116684513428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1366985164213"><a name="en-us_topic_0020091565_p1366985164213"></a><a name="en-us_topic_0020091565_p1366985164213"></a>Specifies the field for sorting the query results. The value can be an attribute of the image: <strong id="en-us_topic_0020091565_b9475283262"><a name="en-us_topic_0020091565_b9475283262"></a><a name="en-us_topic_0020091565_b9475283262"></a>name</strong>, <strong id="en-us_topic_0020091565_b1747528162620"><a name="en-us_topic_0020091565_b1747528162620"></a><a name="en-us_topic_0020091565_b1747528162620"></a>container_format</strong>, <strong id="en-us_topic_0020091565_b104813287269"><a name="en-us_topic_0020091565_b104813287269"></a><a name="en-us_topic_0020091565_b104813287269"></a>disk_format</strong>, <strong id="en-us_topic_0020091565_b17481128132617"><a name="en-us_topic_0020091565_b17481128132617"></a><a name="en-us_topic_0020091565_b17481128132617"></a>status</strong>, <strong id="en-us_topic_0020091565_b74992892610"><a name="en-us_topic_0020091565_b74992892610"></a><a name="en-us_topic_0020091565_b74992892610"></a>id</strong>, <strong id="en-us_topic_0020091565_b125012882617"><a name="en-us_topic_0020091565_b125012882617"></a><a name="en-us_topic_0020091565_b125012882617"></a>size</strong>, or <strong id="en-us_topic_0020091565_b25042810261"><a name="en-us_topic_0020091565_b25042810261"></a><a name="en-us_topic_0020091565_b25042810261"></a>create_at</strong>. The default value is <strong id="en-us_topic_0020091565_b15152822613"><a name="en-us_topic_0020091565_b15152822613"></a><a name="en-us_topic_0020091565_b15152822613"></a>create_at</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row126691653429"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p136691751424"><a name="en-us_topic_0020091565_p136691751424"></a><a name="en-us_topic_0020091565_p136691751424"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p19669653427"><a name="en-us_topic_0020091565_p19669653427"></a><a name="en-us_topic_0020091565_p19669653427"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p36697514216"><a name="en-us_topic_0020091565_p36697514216"></a><a name="en-us_topic_0020091565_p36697514216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p06691351428"><a name="en-us_topic_0020091565_p06691351428"></a><a name="en-us_topic_0020091565_p06691351428"></a>Specifies whether the query results are sorted in ascending or descending order. Its value can be <strong id="en-us_topic_0020091565_b21722049143851"><a name="en-us_topic_0020091565_b21722049143851"></a><a name="en-us_topic_0020091565_b21722049143851"></a>desc </strong>(default) or<strong id="en-us_topic_0020091565_b61280713143851"><a name="en-us_topic_0020091565_b61280713143851"></a><a name="en-us_topic_0020091565_b61280713143851"></a> asc</strong>. This parameter is used together with parameter <strong id="en-us_topic_0020091565_b37017385142847"><a name="en-us_topic_0020091565_b37017385142847"></a><a name="en-us_topic_0020091565_b37017385142847"></a>sort_key</strong>. The default value is <strong id="en-us_topic_0020091565_b842352706192837"><a name="en-us_topic_0020091565_b842352706192837"></a><a name="en-us_topic_0020091565_b842352706192837"></a>desc</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row1166916594218"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p266945164219"><a name="en-us_topic_0020091565_p266945164219"></a><a name="en-us_topic_0020091565_p266945164219"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p86698564211"><a name="en-us_topic_0020091565_p86698564211"></a><a name="en-us_topic_0020091565_p86698564211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p86692053428"><a name="en-us_topic_0020091565_p86692053428"></a><a name="en-us_topic_0020091565_p86692053428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p948212119591"><a name="en-us_topic_0020091565_p948212119591"></a><a name="en-us_topic_0020091565_p948212119591"></a>Specifies the image OS type. Available values include:</p>
    <a name="en-us_topic_0020091565_ul13550133217591"></a><a name="en-us_topic_0020091565_ul13550133217591"></a><ul id="en-us_topic_0020091565_ul13550133217591"><li>Linux</li><li>Windows</li><li>Other</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row8671135164212"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p3669205134214"><a name="en-us_topic_0020091565_p3669205134214"></a><a name="en-us_topic_0020091565_p3669205134214"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p196698564212"><a name="en-us_topic_0020091565_p196698564212"></a><a name="en-us_topic_0020091565_p196698564212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1267117517427"><a name="en-us_topic_0020091565_p1267117517427"></a><a name="en-us_topic_0020091565_p1267117517427"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1867114513427"><a name="en-us_topic_0020091565_p1867114513427"></a><a name="en-us_topic_0020091565_p1867114513427"></a>Adds a tag to an image. Tags can be used as a filter to query images.</p>
    <div class="note" id="en-us_topic_0020091565_note46711558427"><a name="en-us_topic_0020091565_note46711558427"></a><a name="en-us_topic_0020091565_note46711558427"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0020091565_en-us_topic_0060804959_p517019273499"><a name="en-us_topic_0020091565_en-us_topic_0060804959_p517019273499"></a><a name="en-us_topic_0020091565_en-us_topic_0060804959_p517019273499"></a>The tagging function has been upgraded. If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key=Value". For example, an existing tag is <strong id="en-us_topic_0020091565_en-us_topic_0060804959_b84235270610509"><a name="en-us_topic_0020091565_en-us_topic_0060804959_b84235270610509"></a><a name="en-us_topic_0020091565_en-us_topic_0060804959_b84235270610509"></a>a.b</strong>. After the tag function upgrade, query the tag using "tag=a=b".</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row667195174212"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p5671125134211"><a name="en-us_topic_0020091565_p5671125134211"></a><a name="en-us_topic_0020091565_p5671125134211"></a>member_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p18671452421"><a name="en-us_topic_0020091565_p18671452421"></a><a name="en-us_topic_0020091565_p18671452421"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1967115544213"><a name="en-us_topic_0020091565_p1967115544213"></a><a name="en-us_topic_0020091565_p1967115544213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p267114514427"><a name="en-us_topic_0020091565_p267114514427"></a><a name="en-us_topic_0020091565_p267114514427"></a>Specifies the member status. The value can be <strong id="en-us_topic_0020091565_b8423527069592"><a name="en-us_topic_0020091565_b8423527069592"></a><a name="en-us_topic_0020091565_b8423527069592"></a>accepted</strong>, <strong id="en-us_topic_0020091565_b8423527069596"><a name="en-us_topic_0020091565_b8423527069596"></a><a name="en-us_topic_0020091565_b8423527069596"></a>rejected</strong>, or <strong id="en-us_topic_0020091565_b84235270695911"><a name="en-us_topic_0020091565_b84235270695911"></a><a name="en-us_topic_0020091565_b84235270695911"></a>pending</strong>. <strong id="en-us_topic_0020091565_b203788251295959"><a name="en-us_topic_0020091565_b203788251295959"></a><a name="en-us_topic_0020091565_b203788251295959"></a>accepted</strong>: indicates that the shared image is accepted. <strong id="en-us_topic_0020091565_b137807831210025"><a name="en-us_topic_0020091565_b137807831210025"></a><a name="en-us_topic_0020091565_b137807831210025"></a>rejected</strong> indicates that the image shared by others is rejected. <strong id="en-us_topic_0020091565_b5235343781010"><a name="en-us_topic_0020091565_b5235343781010"></a><a name="en-us_topic_0020091565_b5235343781010"></a>pending</strong> indicates that the image shared by others needs to be confirmed. To use this parameter, set <strong id="en-us_topic_0020091565_b84235270693449"><a name="en-us_topic_0020091565_b84235270693449"></a><a name="en-us_topic_0020091565_b84235270693449"></a>visibility</strong> to <strong id="en-us_topic_0020091565_b84235270693452"><a name="en-us_topic_0020091565_b84235270693452"></a><a name="en-us_topic_0020091565_b84235270693452"></a>shared</strong> during the query.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row1467235114215"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p56719584211"><a name="en-us_topic_0020091565_p56719584211"></a><a name="en-us_topic_0020091565_p56719584211"></a>__support_kvm</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p1567118510426"><a name="en-us_topic_0020091565_p1567118510426"></a><a name="en-us_topic_0020091565_p1567118510426"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p76717520424"><a name="en-us_topic_0020091565_p76717520424"></a><a name="en-us_topic_0020091565_p76717520424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p11672352423"><a name="en-us_topic_0020091565_p11672352423"></a><a name="en-us_topic_0020091565_p11672352423"></a>Specifies whether the image supports KVM. If yes, the value is <strong id="en-us_topic_0020091565_b842352706174145"><a name="en-us_topic_0020091565_b842352706174145"></a><a name="en-us_topic_0020091565_b842352706174145"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row967211510424"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p56727584220"><a name="en-us_topic_0020091565_p56727584220"></a><a name="en-us_topic_0020091565_p56727584220"></a>__support_xen</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p10672656426"><a name="en-us_topic_0020091565_p10672656426"></a><a name="en-us_topic_0020091565_p10672656426"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p9672145124215"><a name="en-us_topic_0020091565_p9672145124215"></a><a name="en-us_topic_0020091565_p9672145124215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1467265134214"><a name="en-us_topic_0020091565_p1467265134214"></a><a name="en-us_topic_0020091565_p1467265134214"></a>Specifies whether the image supports Xen. If yes, the value is <strong id="en-us_topic_0020091565_b40128715692258"><a name="en-us_topic_0020091565_b40128715692258"></a><a name="en-us_topic_0020091565_b40128715692258"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row136721255420"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p56721556420"><a name="en-us_topic_0020091565_p56721556420"></a><a name="en-us_topic_0020091565_p56721556420"></a>__support_largememory</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p116721858424"><a name="en-us_topic_0020091565_p116721858424"></a><a name="en-us_topic_0020091565_p116721858424"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p3672175194211"><a name="en-us_topic_0020091565_p3672175194211"></a><a name="en-us_topic_0020091565_p3672175194211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p83811623834"><a name="en-us_topic_0020091565_p83811623834"></a><a name="en-us_topic_0020091565_p83811623834"></a>Specifies whether the image supports large-memory ECSs. If the image supports large-memory ECSs, the value is <strong id="en-us_topic_0020091565_b166569997"><a name="en-us_topic_0020091565_b166569997"></a><a name="en-us_topic_0020091565_b166569997"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="en-us_topic_0020091565_p267016642312"><a name="en-us_topic_0020091565_p267016642312"></a><a name="en-us_topic_0020091565_p267016642312"></a>For the supported OSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
    <p id="en-us_topic_0020091565_p86725554217"><a name="en-us_topic_0020091565_p86725554217"></a><a name="en-us_topic_0020091565_p86725554217"></a></p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row186737514427"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p1167212511426"><a name="en-us_topic_0020091565_p1167212511426"></a><a name="en-us_topic_0020091565_p1167212511426"></a>__support_diskintensive</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p1367325104210"><a name="en-us_topic_0020091565_p1367325104210"></a><a name="en-us_topic_0020091565_p1367325104210"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p10673165134215"><a name="en-us_topic_0020091565_p10673165134215"></a><a name="en-us_topic_0020091565_p10673165134215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p46737511429"><a name="en-us_topic_0020091565_p46737511429"></a><a name="en-us_topic_0020091565_p46737511429"></a>Specifies whether the image supports disk-intensive ECSs. If the image supports disk-intensive ECSs, the value is <strong id="en-us_topic_0020091565_b824778374"><a name="en-us_topic_0020091565_b824778374"></a><a name="en-us_topic_0020091565_b824778374"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row967305154212"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p16673105134213"><a name="en-us_topic_0020091565_p16673105134213"></a><a name="en-us_topic_0020091565_p16673105134213"></a>__support_highperformance</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p167365144212"><a name="en-us_topic_0020091565_p167365144212"></a><a name="en-us_topic_0020091565_p167365144212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p136738554219"><a name="en-us_topic_0020091565_p136738554219"></a><a name="en-us_topic_0020091565_p136738554219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p46731856421"><a name="en-us_topic_0020091565_p46731856421"></a><a name="en-us_topic_0020091565_p46731856421"></a>Specifies whether the image supports high-performance ECSs. If the image supports high-performance ECSs, the value is <strong id="en-us_topic_0020091565_b860168415"><a name="en-us_topic_0020091565_b860168415"></a><a name="en-us_topic_0020091565_b860168415"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row186747511421"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p06731156422"><a name="en-us_topic_0020091565_p06731156422"></a><a name="en-us_topic_0020091565_p06731156422"></a>__support_xen_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p2067319510428"><a name="en-us_topic_0020091565_p2067319510428"></a><a name="en-us_topic_0020091565_p2067319510428"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p167412584218"><a name="en-us_topic_0020091565_p167412584218"></a><a name="en-us_topic_0020091565_p167412584218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1967417514427"><a name="en-us_topic_0020091565_p1967417514427"></a><a name="en-us_topic_0020091565_p1967417514427"></a>The image supports GPU-optimized ECSs on the Xen platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the Xen platform, this attribute is not required. This attribute cannot co-exist with <strong id="en-us_topic_0020091565_b842352706175423"><a name="en-us_topic_0020091565_b842352706175423"></a><a name="en-us_topic_0020091565_b842352706175423"></a>__support_xen</strong> and <strong id="en-us_topic_0020091565_b842352706175430"><a name="en-us_topic_0020091565_b842352706175430"></a><a name="en-us_topic_0020091565_b842352706175430"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row767413519423"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p467412519429"><a name="en-us_topic_0020091565_p467412519429"></a><a name="en-us_topic_0020091565_p467412519429"></a>__support_kvm_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p1067415524218"><a name="en-us_topic_0020091565_p1067415524218"></a><a name="en-us_topic_0020091565_p1067415524218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1067416534210"><a name="en-us_topic_0020091565_p1067416534210"></a><a name="en-us_topic_0020091565_p1067416534210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p6674175174218"><a name="en-us_topic_0020091565_p6674175174218"></a><a name="en-us_topic_0020091565_p6674175174218"></a>Specifies whether the image supports GPU-optimized ECSs on the KVM platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the KVM platform, this attribute is not required. This attribute cannot co-exist with <strong id="en-us_topic_0020091565_b1104343179"><a name="en-us_topic_0020091565_b1104343179"></a><a name="en-us_topic_0020091565_b1104343179"></a>__support_xen</strong> and <strong id="en-us_topic_0020091565_b1737681642"><a name="en-us_topic_0020091565_b1737681642"></a><a name="en-us_topic_0020091565_b1737681642"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row12675651428"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p76746518425"><a name="en-us_topic_0020091565_p76746518425"></a><a name="en-us_topic_0020091565_p76746518425"></a>__support_xen_hana</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p86741051429"><a name="en-us_topic_0020091565_p86741051429"></a><a name="en-us_topic_0020091565_p86741051429"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p1967425124211"><a name="en-us_topic_0020091565_p1967425124211"></a><a name="en-us_topic_0020091565_p1967425124211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p46749512428"><a name="en-us_topic_0020091565_p46749512428"></a><a name="en-us_topic_0020091565_p46749512428"></a>Specifies whether the image supports HANA ECSs on the Xen platform. If yes, the value is <strong id="en-us_topic_0020091565_b1066553282174316"><a name="en-us_topic_0020091565_b1066553282174316"></a><a name="en-us_topic_0020091565_b1066553282174316"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="en-us_topic_0020091565_p1567418519426"><a name="en-us_topic_0020091565_p1567418519426"></a><a name="en-us_topic_0020091565_p1567418519426"></a>This attribute cannot co-exist with <strong id="en-us_topic_0020091565_b2095891873"><a name="en-us_topic_0020091565_b2095891873"></a><a name="en-us_topic_0020091565_b2095891873"></a>__support_xen</strong> and <strong id="en-us_topic_0020091565_b228837324"><a name="en-us_topic_0020091565_b228837324"></a><a name="en-us_topic_0020091565_b228837324"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row186751656421"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p1367555174210"><a name="en-us_topic_0020091565_p1367555174210"></a><a name="en-us_topic_0020091565_p1367555174210"></a>__support_kvm_infiniband</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p267520584210"><a name="en-us_topic_0020091565_p267520584210"></a><a name="en-us_topic_0020091565_p267520584210"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p15675145114219"><a name="en-us_topic_0020091565_p15675145114219"></a><a name="en-us_topic_0020091565_p15675145114219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p1267555164219"><a name="en-us_topic_0020091565_p1267555164219"></a><a name="en-us_topic_0020091565_p1267555164219"></a>Specifies whether the image supports ECSs with the InfiniBand NIC on the KVM platform. If yes, the value is <strong id="en-us_topic_0020091565_b2040161919154726"><a name="en-us_topic_0020091565_b2040161919154726"></a><a name="en-us_topic_0020091565_b2040161919154726"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="en-us_topic_0020091565_p667519594219"><a name="en-us_topic_0020091565_p667519594219"></a><a name="en-us_topic_0020091565_p667519594219"></a>This attribute cannot co-exist with <strong id="en-us_topic_0020091565_b2037544684"><a name="en-us_topic_0020091565_b2037544684"></a><a name="en-us_topic_0020091565_b2037544684"></a>__support_xen</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row13676258423"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p667565184214"><a name="en-us_topic_0020091565_p667565184214"></a><a name="en-us_topic_0020091565_p667565184214"></a>virtual_env_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p86756517427"><a name="en-us_topic_0020091565_p86756517427"></a><a name="en-us_topic_0020091565_p86756517427"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p8675857426"><a name="en-us_topic_0020091565_p8675857426"></a><a name="en-us_topic_0020091565_p8675857426"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p116751451425"><a name="en-us_topic_0020091565_p116751451425"></a><a name="en-us_topic_0020091565_p116751451425"></a>Specifies the environment where the image is used. The value can be <strong id="en-us_topic_0020091565_b19573123342914"><a name="en-us_topic_0020091565_b19573123342914"></a><a name="en-us_topic_0020091565_b19573123342914"></a>FusionCompute</strong>, <strong id="en-us_topic_0020091565_b16574533122912"><a name="en-us_topic_0020091565_b16574533122912"></a><a name="en-us_topic_0020091565_b16574533122912"></a>Ironic</strong>, or <strong id="en-us_topic_0020091565_b11574203314295"><a name="en-us_topic_0020091565_b11574203314295"></a><a name="en-us_topic_0020091565_b11574203314295"></a>DataImage</strong>.</p>
    <a name="en-us_topic_0020091565_ul367615513425"></a><a name="en-us_topic_0020091565_ul367615513425"></a><ul id="en-us_topic_0020091565_ul367615513425"><li>For an <span id="en-us_topic_0020091565_text8399164572420"><a name="en-us_topic_0020091565_text8399164572420"></a><a name="en-us_topic_0020091565_text8399164572420"></a></span><span id="en-us_topic_0020091565_text165624715247"><a name="en-us_topic_0020091565_text165624715247"></a><a name="en-us_topic_0020091565_text165624715247"></a>ECS</span> image (system disk image), the value is <strong id="en-us_topic_0020091565_b13551358133914"><a name="en-us_topic_0020091565_b13551358133914"></a><a name="en-us_topic_0020091565_b13551358133914"></a>FusionCompute</strong>.</li><li>For a data disk image, set the value to <strong id="en-us_topic_0020091565_b4154204217411"><a name="en-us_topic_0020091565_b4154204217411"></a><a name="en-us_topic_0020091565_b4154204217411"></a>DataImage</strong>.</li><li>For a <span id="en-us_topic_0020091565_text2829650144010"><a name="en-us_topic_0020091565_text2829650144010"></a><a name="en-us_topic_0020091565_text2829650144010"></a></span><span id="en-us_topic_0020091565_text88291250134019"><a name="en-us_topic_0020091565_text88291250134019"></a><a name="en-us_topic_0020091565_text88291250134019"></a>BMS</span> image, the value is <strong id="en-us_topic_0020091565_b1282919504405"><a name="en-us_topic_0020091565_b1282919504405"></a><a name="en-us_topic_0020091565_b1282919504405"></a>Ironic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row3677115174211"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p15676751425"><a name="en-us_topic_0020091565_p15676751425"></a><a name="en-us_topic_0020091565_p15676751425"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p166771259429"><a name="en-us_topic_0020091565_p166771259429"></a><a name="en-us_topic_0020091565_p166771259429"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p11677135194219"><a name="en-us_topic_0020091565_p11677135194219"></a><a name="en-us_topic_0020091565_p11677135194219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p206776517428"><a name="en-us_topic_0020091565_p206776517428"></a><a name="en-us_topic_0020091565_p206776517428"></a>Specifies the time when the image was created. Images can be queried by time. The value is in the format of <em id="en-us_topic_0020091565_i842352697105348"><a name="en-us_topic_0020091565_i842352697105348"></a><a name="en-us_topic_0020091565_i842352697105348"></a>Operator:UTC time</em>.</p>
    <p id="en-us_topic_0020091565_p5677125104218"><a name="en-us_topic_0020091565_p5677125104218"></a><a name="en-us_topic_0020091565_p5677125104218"></a>The following operators are supported:</p>
    <p id="en-us_topic_0020091565_p16771756423"><a name="en-us_topic_0020091565_p16771756423"></a><a name="en-us_topic_0020091565_p16771756423"></a>gt: greater than</p>
    <p id="en-us_topic_0020091565_p067716544214"><a name="en-us_topic_0020091565_p067716544214"></a><a name="en-us_topic_0020091565_p067716544214"></a>gte: greater than or equal to</p>
    <p id="en-us_topic_0020091565_p967765184213"><a name="en-us_topic_0020091565_p967765184213"></a><a name="en-us_topic_0020091565_p967765184213"></a>lt: less than</p>
    <p id="en-us_topic_0020091565_p4677175134218"><a name="en-us_topic_0020091565_p4677175134218"></a><a name="en-us_topic_0020091565_p4677175134218"></a>lte: less than or equal to</p>
    <p id="en-us_topic_0020091565_p2677125114219"><a name="en-us_topic_0020091565_p2677125114219"></a><a name="en-us_topic_0020091565_p2677125114219"></a>eq: equal to</p>
    <p id="en-us_topic_0020091565_p767715134217"><a name="en-us_topic_0020091565_p767715134217"></a><a name="en-us_topic_0020091565_p767715134217"></a>neq: not equal to</p>
    <p id="en-us_topic_0020091565_p367717574213"><a name="en-us_topic_0020091565_p367717574213"></a><a name="en-us_topic_0020091565_p367717574213"></a>The time format is <em id="en-us_topic_0020091565_i842352697105633"><a name="en-us_topic_0020091565_i842352697105633"></a><a name="en-us_topic_0020091565_i842352697105633"></a>yyyy-MM-ddThh:mm:ssZ</em> or <em id="en-us_topic_0020091565_i842352697105637"><a name="en-us_topic_0020091565_i842352697105637"></a><a name="en-us_topic_0020091565_i842352697105637"></a>yyyy-MM-dd hh:mm:ss</em>.</p>
    <p id="en-us_topic_0020091565_p46771584218"><a name="en-us_topic_0020091565_p46771584218"></a><a name="en-us_topic_0020091565_p46771584218"></a>For example, to query images whose creation time is earlier than 2018-10-28 10:00:00, set the value of <strong id="en-us_topic_0020091565_b2044855410497"><a name="en-us_topic_0020091565_b2044855410497"></a><a name="en-us_topic_0020091565_b2044855410497"></a>created_at</strong> as follows:</p>
    <p id="en-us_topic_0020091565_p16775518425"><a name="en-us_topic_0020091565_p16775518425"></a><a name="en-us_topic_0020091565_p16775518425"></a>created_at=gt:2018-10-28T10:00:00Z</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020091565_row767815564217"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0020091565_p467717518421"><a name="en-us_topic_0020091565_p467717518421"></a><a name="en-us_topic_0020091565_p467717518421"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0020091565_p267855194211"><a name="en-us_topic_0020091565_p267855194211"></a><a name="en-us_topic_0020091565_p267855194211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0020091565_p13678453427"><a name="en-us_topic_0020091565_p13678453427"></a><a name="en-us_topic_0020091565_p13678453427"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0020091565_p867815104214"><a name="en-us_topic_0020091565_p867815104214"></a><a name="en-us_topic_0020091565_p867815104214"></a>Specifies the time when the image was modified. Images can be queried by time. The value is in the format of <em id="en-us_topic_0020091565_i1803091373"><a name="en-us_topic_0020091565_i1803091373"></a><a name="en-us_topic_0020091565_i1803091373"></a>Operator:UTC time</em>.</p>
    <p id="en-us_topic_0020091565_p166781952420"><a name="en-us_topic_0020091565_p166781952420"></a><a name="en-us_topic_0020091565_p166781952420"></a>The following operators are supported:</p>
    <a name="en-us_topic_0020091565_ul1455613481312"></a><a name="en-us_topic_0020091565_ul1455613481312"></a><ul id="en-us_topic_0020091565_ul1455613481312"><li>gt: greater than</li><li>gte: greater than or equal to</li><li>lt: less than</li><li>lte: less than or equal to</li><li>eq: equal to</li><li>neq: not equal to</li></ul>
    <p id="en-us_topic_0020091565_p567816519423"><a name="en-us_topic_0020091565_p567816519423"></a><a name="en-us_topic_0020091565_p567816519423"></a>The time format is <em id="en-us_topic_0020091565_i133097135019"><a name="en-us_topic_0020091565_i133097135019"></a><a name="en-us_topic_0020091565_i133097135019"></a>yyyy-MM-ddThh:mm:ssZ</em> or <em id="en-us_topic_0020091565_i123119715503"><a name="en-us_topic_0020091565_i123119715503"></a><a name="en-us_topic_0020091565_i123119715503"></a>yyyy-MM-dd hh:mm:ss</em>.</p>
    <p id="en-us_topic_0020091565_p96782510422"><a name="en-us_topic_0020091565_p96782510422"></a><a name="en-us_topic_0020091565_p96782510422"></a>For example, to query images whose modification time is earlier than 2018-10-28 10:00:00, set the value of <strong id="en-us_topic_0020091565_b11293691505"><a name="en-us_topic_0020091565_b11293691505"></a><a name="en-us_topic_0020091565_b11293691505"></a>created_at </strong>as follows:</p>
    <p id="en-us_topic_0020091565_p1667835114211"><a name="en-us_topic_0020091565_p1667835114211"></a><a name="en-us_topic_0020091565_p1667835114211"></a>updated_at=gt:2018-10-28T10:00:00Z</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{Endpoint}/v1/cloudimages/tags?limit=5&page=1 
    ```


## Response<a name="section14290290175847"></a>

-   Response parameters

    <a name="table226625411834"></a>
    <table><thead align="left"><tr id="row614233041834"><th class="cellrowborder" valign="top" width="36.14361436143614%" id="mcps1.1.4.1.1"><p id="p92317031834"><a name="p92317031834"></a><a name="p92317031834"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.89228922892289%" id="mcps1.1.4.1.2"><p id="p370103231834"><a name="p370103231834"></a><a name="p370103231834"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.964096409640966%" id="mcps1.1.4.1.3"><p id="p450461591834"><a name="p450461591834"></a><a name="p450461591834"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row248602881834"><td class="cellrowborder" valign="top" width="36.14361436143614%" headers="mcps1.1.4.1.1 "><p id="p4174861834"><a name="p4174861834"></a><a name="p4174861834"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.89228922892289%" headers="mcps1.1.4.1.2 "><p id="p547751991834"><a name="p547751991834"></a><a name="p547751991834"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.964096409640966%" headers="mcps1.1.4.1.3 "><p id="p76061301834"><a name="p76061301834"></a><a name="p76061301834"></a>Lists the tags.</p>
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
       "tags": [
          "jjjj.11111",
          "uuuu.22222",
          "234.4",
          "test",
          "image"
       ]
    }
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >In the new specification, equal signs are used as separators.  


## Returned Value<a name="section44555097175929"></a>

-   Normal

    200

-   Abnormal

    <a name="table442321051854"></a>
    <table><thead align="left"><tr id="row517409891854"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p302705861854"><a name="p302705861854"></a><a name="p302705861854"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p359984201854"><a name="p359984201854"></a><a name="p359984201854"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row301908981854"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p295436771854"><a name="p295436771854"></a><a name="p295436771854"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p442276121854"><a name="p442276121854"></a><a name="p442276121854"></a>Request error. For details about the returned error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row625041911854"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p296746801854"><a name="p296746801854"></a><a name="p296746801854"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p548388411854"><a name="p548388411854"></a><a name="p548388411854"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row237875241854"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p477413171854"><a name="p477413171854"></a><a name="p477413171854"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p418415071854"><a name="p418415071854"></a><a name="p418415071854"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row410292481854"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p350348041854"><a name="p350348041854"></a><a name="p350348041854"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p192468391854"><a name="p192468391854"></a><a name="p192468391854"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row390038311854"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p51937511854"><a name="p51937511854"></a><a name="p51937511854"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p180406671854"><a name="p180406671854"></a><a name="p180406671854"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row281482781854"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p654180601854"><a name="p654180601854"></a><a name="p654180601854"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p643715141854"><a name="p643715141854"></a><a name="p643715141854"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


