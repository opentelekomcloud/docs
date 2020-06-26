# Querying Images<a name="EN-US_TOPIC_0020091565"></a>

## Function<a name="section59471393"></a>

This API is used to query images using search criteria and to display the images in a list.

## URI<a name="section65480490"></a>

GET /v2/cloudimages

>![](/images/icon-note.gif) **NOTE:**   
>You can type a question mark \(?\) and an ampersand \(&\) at the end of the URI to define multiple search criteria. For details, see the example request.  

## Request<a name="section192957510423"></a>

-   Request parameters

    <a name="table867855184219"></a>
    <table><thead align="left"><tr id="row18662125134212"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.1"><p id="p16621584210"><a name="p16621584210"></a><a name="p16621584210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.1.5.1.2"><p id="p7662157429"><a name="p7662157429"></a><a name="p7662157429"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.3"><p id="p9662254429"><a name="p9662254429"></a><a name="p9662254429"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.1.5.1.4"><p id="p66625524217"><a name="p66625524217"></a><a name="p66625524217"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row866310519425"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p1866216511420"><a name="p1866216511420"></a><a name="p1866216511420"></a>__isregistered</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p3663125164212"><a name="p3663125164212"></a><a name="p3663125164212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p196631756427"><a name="p196631756427"></a><a name="p196631756427"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1566325104216"><a name="p1566325104216"></a><a name="p1566325104216"></a>Specifies whether the image is available. The value can be <strong id="b84235270616222"><a name="b84235270616222"></a><a name="b84235270616222"></a>true</strong>. The value is <strong id="b2049464823162253"><a name="b2049464823162253"></a><a name="b2049464823162253"></a>true</strong> for all extension APIs by default. Common users can query only the images for which the value of this parameter is <strong id="b846915150162332"><a name="b846915150162332"></a><a name="b846915150162332"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row866345194215"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p1066355184213"><a name="p1066355184213"></a><a name="p1066355184213"></a>__imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p1663205114212"><a name="p1663205114212"></a><a name="p1663205114212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p466313544218"><a name="p466313544218"></a><a name="p466313544218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p66631551425"><a name="p66631551425"></a><a name="p66631551425"></a>Specifies the image type. The following types are supported:</p>
    <a name="ul26635584212"></a><a name="ul26635584212"></a><ul id="ul26635584212"><li>Public image: The value is <strong id="b842352706163515"><a name="b842352706163515"></a><a name="b842352706163515"></a>gold</strong>.</li><li>Private image: The value is <strong id="b1762610292163524"><a name="b1762610292163524"></a><a name="b1762610292163524"></a>private</strong>.</li><li>Shared image: The value is <strong id="b298092137163545"><a name="b298092137163545"></a><a name="b298092137163545"></a>shared</strong>.</li></ul>
    <div class="note" id="note7533222103412"><a name="note7533222103412"></a><a name="note7533222103412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p653413224345"><a name="p653413224345"></a><a name="p653413224345"></a>The <strong id="b246710191919"><a name="b246710191919"></a><a name="b246710191919"></a>__imagetype</strong> of images you share with other tenants or those other tenants share with you and you have accepted is <strong id="b1762175571915"><a name="b1762175571915"></a><a name="b1762175571915"></a>shared</strong>. You can use field <strong id="b6237171042012"><a name="b6237171042012"></a><a name="b6237171042012"></a>owner</strong> to distinguish the two types of shared images. You can use <strong id="b13751829223"><a name="b13751829223"></a><a name="b13751829223"></a>member_status</strong> to filter out shared images you have accepted.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row06401901946"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p9641120347"><a name="p9641120347"></a><a name="p9641120347"></a>__whole_image</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p264160844"><a name="p264160844"></a><a name="p264160844"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1064117013414"><a name="p1064117013414"></a><a name="p1064117013414"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p36411603417"><a name="p36411603417"></a><a name="p36411603417"></a>Specifies whether the image is a full-ECS image. The value can be <strong id="b19541329194712"><a name="b19541329194712"></a><a name="b19541329194712"></a>true</strong> or <strong id="b858493314714"><a name="b858493314714"></a><a name="b858493314714"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row1663165194213"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p12663359421"><a name="p12663359421"></a><a name="p12663359421"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p666315174216"><a name="p666315174216"></a><a name="p666315174216"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p866385174216"><a name="p866385174216"></a><a name="p866385174216"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p26631856423"><a name="p26631856423"></a><a name="p26631856423"></a>Specifies whether the image is protected. The value can be <strong id="b842352706113632"><a name="b842352706113632"></a><a name="b842352706113632"></a>true</strong> or <strong id="b842352706113636"><a name="b842352706113636"></a><a name="b842352706113636"></a>false</strong>. Set it to <strong id="b48612739142847_1"><a name="b48612739142847_1"></a><a name="b48612739142847_1"></a>true</strong> when you query public images. This parameter is optional when you query private images.</p>
    </td>
    </tr>
    <tr id="row136641510425"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p866316513424"><a name="p866316513424"></a><a name="p866316513424"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p366465184215"><a name="p366465184215"></a><a name="p366465184215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p166410544212"><a name="p166410544212"></a><a name="p166410544212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1480263817401"><a name="p1480263817401"></a><a name="p1480263817401"></a>Specifies whether the image is available to other tenants. Available values include:</p>
    <a name="ul111418194429"></a><a name="ul111418194429"></a><ul id="ul111418194429"><li><strong id="b18991733105115"><a name="b18991733105115"></a><a name="b18991733105115"></a>public</strong>: public image</li><li><strong id="b842352706114634"><a name="b842352706114634"></a><a name="b842352706114634"></a>private</strong>: private image</li><li><strong id="b1823217295616"><a name="b1823217295616"></a><a name="b1823217295616"></a>shared</strong>: shared image</li></ul>
    </td>
    </tr>
    <tr id="row36641515426"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p166641052420"><a name="p166641052420"></a><a name="p166641052420"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p1366419504215"><a name="p1366419504215"></a><a name="p1366419504215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1866416511428"><a name="p1866416511428"></a><a name="p1866416511428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p4664115134213"><a name="p4664115134213"></a><a name="p4664115134213"></a>Specifies the image owner.</p>
    </td>
    </tr>
    <tr id="row1066420574214"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p14664145164210"><a name="p14664145164210"></a><a name="p14664145164210"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p136641650427"><a name="p136641650427"></a><a name="p136641650427"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1266416514421"><a name="p1266416514421"></a><a name="p1266416514421"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1266425204213"><a name="p1266425204213"></a><a name="p1266425204213"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="row1666565144210"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p17664252421"><a name="p17664252421"></a><a name="p17664252421"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p46642520425"><a name="p46642520425"></a><a name="p46642520425"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p156641157428"><a name="p156641157428"></a><a name="p156641157428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p56641756429"><a name="p56641756429"></a><a name="p56641756429"></a>Specifies the image status. The value can be one of the following:</p>
    <a name="ul46651451422"></a><a name="ul46651451422"></a><ul id="ul46651451422"><li><strong id="b842352706103333"><a name="b842352706103333"></a><a name="b842352706103333"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="b842352706104325"><a name="b842352706104325"></a><a name="b842352706104325"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="b842352706104450"><a name="b842352706104450"></a><a name="b842352706104450"></a>deleted</strong>: indicates that the image has been deleted.</li><li><strong id="b842352706104518"><a name="b842352706104518"></a><a name="b842352706104518"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="b842352706104558"><a name="b842352706104558"></a><a name="b842352706104558"></a>active</strong>: indicates that the image is available for use. </li></ul>
    </td>
    </tr>
    <tr id="row5665752427"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p4665165194214"><a name="p4665165194214"></a><a name="p4665165194214"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p966545204211"><a name="p966545204211"></a><a name="p966545204211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p136654544219"><a name="p136654544219"></a><a name="p136654544219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p36658534216"><a name="p36658534216"></a><a name="p36658534216"></a>Specifies the image name. Exact matching is used. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row11666551426"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p12665115194213"><a name="p12665115194213"></a><a name="p12665115194213"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p1266515104210"><a name="p1266515104210"></a><a name="p1266515104210"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1666510515424"><a name="p1666510515424"></a><a name="p1666510515424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p116661953423"><a name="p116661953423"></a><a name="p116661953423"></a>Specifies the container type. The value is <strong id="b842352706192014"><a name="b842352706192014"></a><a name="b842352706192014"></a>bare</strong>.</p>
    </td>
    </tr>
    <tr id="row866619519425"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p1566618511424"><a name="p1566618511424"></a><a name="p1566618511424"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p186661255424"><a name="p186661255424"></a><a name="p186661255424"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p26666515421"><a name="p26666515421"></a><a name="p26666515421"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p266685184211"><a name="p266685184211"></a><a name="p266685184211"></a>Specifies the image format. The value can be <strong id="b144536448521"><a name="b144536448521"></a><a name="b144536448521"></a>vhd</strong>, <strong id="b19454194415210"><a name="b19454194415210"></a><a name="b19454194415210"></a>raw</strong>, <strong id="b145544445210"><a name="b145544445210"></a><a name="b145544445210"></a>zvhd</strong>, or <strong id="b1645611449521"><a name="b1645611449521"></a><a name="b1645611449521"></a>qcow2</strong>. The default value is <strong id="b842352706165234"><a name="b842352706165234"></a><a name="b842352706165234"></a>zvhd2</strong>.</p>
    </td>
    </tr>
    <tr id="row2066612519428"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p266612514421"><a name="p266612514421"></a><a name="p266612514421"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p7666145124217"><a name="p7666145124217"></a><a name="p7666145124217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p2666115194210"><a name="p2666115194210"></a><a name="p2666115194210"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p8666953422"><a name="p8666953422"></a><a name="p8666953422"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the <span id="text1343072215515"><a name="text1343072215515"></a><a name="text1343072215515"></a></span><span id="text92721735125119"><a name="text92721735125119"></a><a name="text92721735125119"></a>ECS</span> specifications. Generally, the value is <strong id="b1986818338377"><a name="b1986818338377"></a><a name="b1986818338377"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row116673517423"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p2666355425"><a name="p2666355425"></a><a name="p2666355425"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p666675194212"><a name="p666675194212"></a><a name="p666675194212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p6666125124212"><a name="p6666125124212"></a><a name="p6666125124212"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p16671651424"><a name="p16671651424"></a><a name="p16671651424"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
    </td>
    </tr>
    <tr id="row5667165154210"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p766710510425"><a name="p766710510425"></a><a name="p766710510425"></a>__os_bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p866715517421"><a name="p866715517421"></a><a name="p866715517421"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p2667125124213"><a name="p2667125124213"></a><a name="p2667125124213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1166745154214"><a name="p1166745154214"></a><a name="p1166745154214"></a>Specifies the OS architecture, 32 bit or 64 bit.</p>
    </td>
    </tr>
    <tr id="row1966812510428"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p66677544211"><a name="p66677544211"></a><a name="p66677544211"></a>__platform</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p16667145204212"><a name="p16667145204212"></a><a name="p16667145204212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p4667195184213"><a name="p4667195184213"></a><a name="p4667195184213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p66679515425"><a name="p66679515425"></a><a name="p66679515425"></a>Specifies the image platform type. The value can be <strong id="b54511332185320"><a name="b54511332185320"></a><a name="b54511332185320"></a>Windows</strong>, <strong id="b144527320539"><a name="b144527320539"></a><a name="b144527320539"></a>Ubuntu</strong>, <strong id="b174521232125310"><a name="b174521232125310"></a><a name="b174521232125310"></a>RedHat</strong>, <strong id="b34532320533"><a name="b34532320533"></a><a name="b34532320533"></a>SUSE</strong>, <strong id="b1445316328538"><a name="b1445316328538"></a><a name="b1445316328538"></a>CentOS</strong>, <strong id="b5454153265320"><a name="b5454153265320"></a><a name="b5454153265320"></a>Debian</strong>, <strong id="b1945416327536"><a name="b1945416327536"></a><a name="b1945416327536"></a>OpenSUSE</strong>, <strong id="b54557321535"><a name="b54557321535"></a><a name="b54557321535"></a>Oracle Linux</strong>, <strong id="b545623255320"><a name="b545623255320"></a><a name="b545623255320"></a>Fedora</strong>, <strong id="b164564321538"><a name="b164564321538"></a><a name="b164564321538"></a>Other</strong>, <strong id="b64571532195311"><a name="b64571532195311"></a><a name="b64571532195311"></a>CoreOS</strong>, or <strong id="b1345717329530"><a name="b1345717329530"></a><a name="b1345717329530"></a>EulerOS</strong>.</p>
    </td>
    </tr>
    <tr id="row16686504210"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p56680584218"><a name="p56680584218"></a><a name="p56680584218"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p9668559427"><a name="p9668559427"></a><a name="p9668559427"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1866845194219"><a name="p1866845194219"></a><a name="p1866845194219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p566835104216"><a name="p566835104216"></a><a name="p566835104216"></a>Specifies the start number from which images are queried. The value is the image ID.</p>
    </td>
    </tr>
    <tr id="row4668258426"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p066813534216"><a name="p066813534216"></a><a name="p066813534216"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p566815534214"><a name="p566815534214"></a><a name="p566815534214"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p466814564214"><a name="p466814564214"></a><a name="p466814564214"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p666885174218"><a name="p666885174218"></a><a name="p666885174218"></a>Specifies the number of images to be queried. The value is an integer and is <strong id="b3988183415491"><a name="b3988183415491"></a><a name="b3988183415491"></a>500</strong> by default.</p>
    </td>
    </tr>
    <tr id="row1166945124218"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p136682544216"><a name="p136682544216"></a><a name="p136682544216"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p1166813584217"><a name="p1166813584217"></a><a name="p1166813584217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p116684513428"><a name="p116684513428"></a><a name="p116684513428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1366985164213"><a name="p1366985164213"></a><a name="p1366985164213"></a>Specifies the field for sorting the query results. The value can be an attribute of the image: <strong id="b9475283262"><a name="b9475283262"></a><a name="b9475283262"></a>name</strong>, <strong id="b1747528162620"><a name="b1747528162620"></a><a name="b1747528162620"></a>container_format</strong>, <strong id="b104813287269"><a name="b104813287269"></a><a name="b104813287269"></a>disk_format</strong>, <strong id="b17481128132617"><a name="b17481128132617"></a><a name="b17481128132617"></a>status</strong>, <strong id="b74992892610"><a name="b74992892610"></a><a name="b74992892610"></a>id</strong>, <strong id="b125012882617"><a name="b125012882617"></a><a name="b125012882617"></a>size</strong>, or <strong id="b25042810261"><a name="b25042810261"></a><a name="b25042810261"></a>create_at</strong>. The default value is <strong id="b15152822613"><a name="b15152822613"></a><a name="b15152822613"></a>create_at</strong>.</p>
    </td>
    </tr>
    <tr id="row126691653429"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p136691751424"><a name="p136691751424"></a><a name="p136691751424"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p19669653427"><a name="p19669653427"></a><a name="p19669653427"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p36697514216"><a name="p36697514216"></a><a name="p36697514216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p06691351428"><a name="p06691351428"></a><a name="p06691351428"></a>Specifies whether the query results are sorted in ascending or descending order. Its value can be <strong id="b21722049143851"><a name="b21722049143851"></a><a name="b21722049143851"></a>desc </strong>(default) or<strong id="b61280713143851"><a name="b61280713143851"></a><a name="b61280713143851"></a> asc</strong>. This parameter is used together with parameter <strong id="b37017385142847"><a name="b37017385142847"></a><a name="b37017385142847"></a>sort_key</strong>. The default value is <strong id="b842352706192837"><a name="b842352706192837"></a><a name="b842352706192837"></a>desc</strong>.</p>
    </td>
    </tr>
    <tr id="row1166916594218"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p266945164219"><a name="p266945164219"></a><a name="p266945164219"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p86698564211"><a name="p86698564211"></a><a name="p86698564211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p86692053428"><a name="p86692053428"></a><a name="p86692053428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p948212119591"><a name="p948212119591"></a><a name="p948212119591"></a>Specifies the image OS type. Available values include:</p>
    <a name="ul13550133217591"></a><a name="ul13550133217591"></a><ul id="ul13550133217591"><li>Linux</li><li>Windows</li><li>Other</li></ul>
    </td>
    </tr>
    <tr id="row8671135164212"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p3669205134214"><a name="p3669205134214"></a><a name="p3669205134214"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p196698564212"><a name="p196698564212"></a><a name="p196698564212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1267117517427"><a name="p1267117517427"></a><a name="p1267117517427"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1867114513427"><a name="p1867114513427"></a><a name="p1867114513427"></a>Adds a tag to an image. Tags can be used as a filter to query images.</p>
    <div class="note" id="note46711558427"><a name="note46711558427"></a><a name="note46711558427"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0060804959_p517019273499"><a name="en-us_topic_0060804959_p517019273499"></a><a name="en-us_topic_0060804959_p517019273499"></a>The tagging function has been upgraded. If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key=Value". For example, an existing tag is <strong id="en-us_topic_0060804959_b84235270610509"><a name="en-us_topic_0060804959_b84235270610509"></a><a name="en-us_topic_0060804959_b84235270610509"></a>a.b</strong>. After the tag function upgrade, query the tag using "tag=a=b".</p>
    </div></div>
    </td>
    </tr>
    <tr id="row667195174212"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p5671125134211"><a name="p5671125134211"></a><a name="p5671125134211"></a>member_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p18671452421"><a name="p18671452421"></a><a name="p18671452421"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1967115544213"><a name="p1967115544213"></a><a name="p1967115544213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p267114514427"><a name="p267114514427"></a><a name="p267114514427"></a>Specifies the member status. The value can be <strong id="b8423527069592"><a name="b8423527069592"></a><a name="b8423527069592"></a>accepted</strong>, <strong id="b8423527069596"><a name="b8423527069596"></a><a name="b8423527069596"></a>rejected</strong>, or <strong id="b84235270695911"><a name="b84235270695911"></a><a name="b84235270695911"></a>pending</strong>. <strong id="b203788251295959"><a name="b203788251295959"></a><a name="b203788251295959"></a>accepted</strong>: indicates that the shared image is accepted. <strong id="b137807831210025"><a name="b137807831210025"></a><a name="b137807831210025"></a>rejected</strong> indicates that the image shared by others is rejected. <strong id="b5235343781010"><a name="b5235343781010"></a><a name="b5235343781010"></a>pending</strong> indicates that the image shared by others needs to be confirmed. To use this parameter, set <strong id="b84235270693449"><a name="b84235270693449"></a><a name="b84235270693449"></a>visibility</strong> to <strong id="b84235270693452"><a name="b84235270693452"></a><a name="b84235270693452"></a>shared</strong> during the query.</p>
    </td>
    </tr>
    <tr id="row1467235114215"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p56719584211"><a name="p56719584211"></a><a name="p56719584211"></a>__support_kvm</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p1567118510426"><a name="p1567118510426"></a><a name="p1567118510426"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p76717520424"><a name="p76717520424"></a><a name="p76717520424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p11672352423"><a name="p11672352423"></a><a name="p11672352423"></a>Specifies whether the image supports KVM. If yes, the value is <strong id="b842352706174145"><a name="b842352706174145"></a><a name="b842352706174145"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row967211510424"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p56727584220"><a name="p56727584220"></a><a name="p56727584220"></a>__support_xen</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p10672656426"><a name="p10672656426"></a><a name="p10672656426"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p9672145124215"><a name="p9672145124215"></a><a name="p9672145124215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1467265134214"><a name="p1467265134214"></a><a name="p1467265134214"></a>Specifies whether the image supports Xen. If yes, the value is <strong id="b40128715692258"><a name="b40128715692258"></a><a name="b40128715692258"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row136721255420"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p56721556420"><a name="p56721556420"></a><a name="p56721556420"></a>__support_largememory</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p116721858424"><a name="p116721858424"></a><a name="p116721858424"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p3672175194211"><a name="p3672175194211"></a><a name="p3672175194211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p83811623834"><a name="p83811623834"></a><a name="p83811623834"></a>Specifies whether the image supports large-memory ECSs. If the image supports large-memory ECSs, the value is <strong id="b166569997"><a name="b166569997"></a><a name="b166569997"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p267016642312"><a name="p267016642312"></a><a name="p267016642312"></a>For the supported OSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
    <p id="p86725554217"><a name="p86725554217"></a><a name="p86725554217"></a></p>
    </td>
    </tr>
    <tr id="row186737514427"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p1167212511426"><a name="p1167212511426"></a><a name="p1167212511426"></a>__support_diskintensive</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p1367325104210"><a name="p1367325104210"></a><a name="p1367325104210"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p10673165134215"><a name="p10673165134215"></a><a name="p10673165134215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p46737511429"><a name="p46737511429"></a><a name="p46737511429"></a>Specifies whether the image supports disk-intensive ECSs. If the image supports disk-intensive ECSs, the value is <strong id="b824778374"><a name="b824778374"></a><a name="b824778374"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row967305154212"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p16673105134213"><a name="p16673105134213"></a><a name="p16673105134213"></a>__support_highperformance</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p167365144212"><a name="p167365144212"></a><a name="p167365144212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p136738554219"><a name="p136738554219"></a><a name="p136738554219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p46731856421"><a name="p46731856421"></a><a name="p46731856421"></a>Specifies whether the image supports high-performance ECSs. If the image supports high-performance ECSs, the value is <strong id="b860168415"><a name="b860168415"></a><a name="b860168415"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row186747511421"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p06731156422"><a name="p06731156422"></a><a name="p06731156422"></a>__support_xen_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p2067319510428"><a name="p2067319510428"></a><a name="p2067319510428"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p167412584218"><a name="p167412584218"></a><a name="p167412584218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1967417514427"><a name="p1967417514427"></a><a name="p1967417514427"></a>The image supports GPU-optimized ECSs on the Xen platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the Xen platform, this attribute is not required. This attribute cannot co-exist with <strong id="b842352706175423"><a name="b842352706175423"></a><a name="b842352706175423"></a>__support_xen</strong> and <strong id="b842352706175430"><a name="b842352706175430"></a><a name="b842352706175430"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row767413519423"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p467412519429"><a name="p467412519429"></a><a name="p467412519429"></a>__support_kvm_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p1067415524218"><a name="p1067415524218"></a><a name="p1067415524218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1067416534210"><a name="p1067416534210"></a><a name="p1067416534210"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p6674175174218"><a name="p6674175174218"></a><a name="p6674175174218"></a>Specifies whether the image supports GPU-optimized ECSs on the KVM platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the KVM platform, this attribute is not required. This attribute cannot co-exist with <strong id="b1104343179"><a name="b1104343179"></a><a name="b1104343179"></a>__support_xen</strong> and <strong id="b1737681642"><a name="b1737681642"></a><a name="b1737681642"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row12675651428"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p76746518425"><a name="p76746518425"></a><a name="p76746518425"></a>__support_xen_hana</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p86741051429"><a name="p86741051429"></a><a name="p86741051429"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p1967425124211"><a name="p1967425124211"></a><a name="p1967425124211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p46749512428"><a name="p46749512428"></a><a name="p46749512428"></a>Specifies whether the image supports HANA ECSs on the Xen platform. If yes, the value is <strong id="b1066553282174316"><a name="b1066553282174316"></a><a name="b1066553282174316"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p1567418519426"><a name="p1567418519426"></a><a name="p1567418519426"></a>This attribute cannot co-exist with <strong id="b2095891873"><a name="b2095891873"></a><a name="b2095891873"></a>__support_xen</strong> and <strong id="b228837324"><a name="b228837324"></a><a name="b228837324"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row186751656421"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p1367555174210"><a name="p1367555174210"></a><a name="p1367555174210"></a>__support_kvm_infiniband</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p267520584210"><a name="p267520584210"></a><a name="p267520584210"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p15675145114219"><a name="p15675145114219"></a><a name="p15675145114219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1267555164219"><a name="p1267555164219"></a><a name="p1267555164219"></a>Specifies whether the image supports ECSs with the InfiniBand NIC on the KVM platform. If yes, the value is <strong id="b2040161919154726"><a name="b2040161919154726"></a><a name="b2040161919154726"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p667519594219"><a name="p667519594219"></a><a name="p667519594219"></a>This attribute cannot co-exist with <strong id="b2037544684"><a name="b2037544684"></a><a name="b2037544684"></a>__support_xen</strong>.</p>
    </td>
    </tr>
    <tr id="row13676258423"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p667565184214"><a name="p667565184214"></a><a name="p667565184214"></a>virtual_env_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p86756517427"><a name="p86756517427"></a><a name="p86756517427"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p8675857426"><a name="p8675857426"></a><a name="p8675857426"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p116751451425"><a name="p116751451425"></a><a name="p116751451425"></a>Specifies the environment where the image is used. The value can be <strong id="b19573123342914"><a name="b19573123342914"></a><a name="b19573123342914"></a>FusionCompute</strong>, <strong id="b16574533122912"><a name="b16574533122912"></a><a name="b16574533122912"></a>Ironic</strong>, or <strong id="b11574203314295"><a name="b11574203314295"></a><a name="b11574203314295"></a>DataImage</strong>.</p>
    <a name="ul367615513425"></a><a name="ul367615513425"></a><ul id="ul367615513425"><li>For an <span id="text8399164572420"><a name="text8399164572420"></a><a name="text8399164572420"></a></span><span id="text165624715247"><a name="text165624715247"></a><a name="text165624715247"></a>ECS</span> image (system disk image), the value is <strong id="b13551358133914"><a name="b13551358133914"></a><a name="b13551358133914"></a>FusionCompute</strong>.</li><li>For a data disk image, set the value to <strong id="b4154204217411"><a name="b4154204217411"></a><a name="b4154204217411"></a>DataImage</strong>.</li><li>For a <span id="text2829650144010"><a name="text2829650144010"></a><a name="text2829650144010"></a></span><span id="text88291250134019"><a name="text88291250134019"></a><a name="text88291250134019"></a>BMS</span> image, the value is <strong id="b1282919504405"><a name="b1282919504405"></a><a name="b1282919504405"></a>Ironic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row3677115174211"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p15676751425"><a name="p15676751425"></a><a name="p15676751425"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p166771259429"><a name="p166771259429"></a><a name="p166771259429"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p11677135194219"><a name="p11677135194219"></a><a name="p11677135194219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p206776517428"><a name="p206776517428"></a><a name="p206776517428"></a>Specifies the time when the image was created. Images can be queried by time. The value is in the format of <em id="i842352697105348"><a name="i842352697105348"></a><a name="i842352697105348"></a>Operator:UTC time</em>.</p>
    <p id="p5677125104218"><a name="p5677125104218"></a><a name="p5677125104218"></a>The following operators are supported:</p>
    <p id="p16771756423"><a name="p16771756423"></a><a name="p16771756423"></a>gt: greater than</p>
    <p id="p067716544214"><a name="p067716544214"></a><a name="p067716544214"></a>gte: greater than or equal to</p>
    <p id="p967765184213"><a name="p967765184213"></a><a name="p967765184213"></a>lt: less than</p>
    <p id="p4677175134218"><a name="p4677175134218"></a><a name="p4677175134218"></a>lte: less than or equal to</p>
    <p id="p2677125114219"><a name="p2677125114219"></a><a name="p2677125114219"></a>eq: equal to</p>
    <p id="p767715134217"><a name="p767715134217"></a><a name="p767715134217"></a>neq: not equal to</p>
    <p id="p367717574213"><a name="p367717574213"></a><a name="p367717574213"></a>The time format is <em id="i842352697105633"><a name="i842352697105633"></a><a name="i842352697105633"></a>yyyy-MM-ddThh:mm:ssZ</em> or <em id="i842352697105637"><a name="i842352697105637"></a><a name="i842352697105637"></a>yyyy-MM-dd hh:mm:ss</em>.</p>
    <p id="p46771584218"><a name="p46771584218"></a><a name="p46771584218"></a>For example, to query images whose creation time is earlier than 2018-10-28 10:00:00, set the value of <strong id="b2044855410497"><a name="b2044855410497"></a><a name="b2044855410497"></a>created_at</strong> as follows:</p>
    <p id="p16775518425"><a name="p16775518425"></a><a name="p16775518425"></a>created_at=gt:2018-10-28T10:00:00Z</p>
    </td>
    </tr>
    <tr id="row767815564217"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.1 "><p id="p467717518421"><a name="p467717518421"></a><a name="p467717518421"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p267855194211"><a name="p267855194211"></a><a name="p267855194211"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p13678453427"><a name="p13678453427"></a><a name="p13678453427"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p867815104214"><a name="p867815104214"></a><a name="p867815104214"></a>Specifies the time when the image was modified. Images can be queried by time. The value is in the format of <em id="i1803091373"><a name="i1803091373"></a><a name="i1803091373"></a>Operator:UTC time</em>.</p>
    <p id="p166781952420"><a name="p166781952420"></a><a name="p166781952420"></a>The following operators are supported:</p>
    <a name="ul1455613481312"></a><a name="ul1455613481312"></a><ul id="ul1455613481312"><li>gt: greater than</li><li>gte: greater than or equal to</li><li>lt: less than</li><li>lte: less than or equal to</li><li>eq: equal to</li><li>neq: not equal to</li></ul>
    <p id="p567816519423"><a name="p567816519423"></a><a name="p567816519423"></a>The time format is <em id="i133097135019"><a name="i133097135019"></a><a name="i133097135019"></a>yyyy-MM-ddThh:mm:ssZ</em> or <em id="i123119715503"><a name="i123119715503"></a><a name="i123119715503"></a>yyyy-MM-dd hh:mm:ss</em>.</p>
    <p id="p96782510422"><a name="p96782510422"></a><a name="p96782510422"></a>For example, to query images whose modification time is earlier than 2018-10-28 10:00:00, set the value of <strong id="b11293691505"><a name="b11293691505"></a><a name="b11293691505"></a>created_at </strong>as follows:</p>
    <p id="p1667835114211"><a name="p1667835114211"></a><a name="p1667835114211"></a>updated_at=gt:2018-10-28T10:00:00Z</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{Endpoint}/v2/cloudimages?__imagetype=gold&sort_key=name&limit=1
    ```


## Common Query Methods<a name="section3510131014428"></a>

-   Public images

    GET /v2/cloudimages?\_\_imagetype=gold&visibility=public&protected=true

-   Private images

    GET /v2/cloudimages?owner=\{project\_id\}

-   Available shared images

    GET /v2/cloudimages?member\_status=accepted&visibility=shared&\_\_imagetype=shared

-   Rejected images

    GET /v2/cloudimages?member\_status=rejected&visibility=shared&\_\_imagetype=shared

-   Unaccepted images

    GET /v2/cloudimages?member\_status=pending&visibility=shared&\_\_imagetype=shared


## Response<a name="section2319502"></a>

-   Response parameters

    <a name="table59217371151"></a>
    <table><thead align="left"><tr id="row17922113713513"><th class="cellrowborder" valign="top" width="25.91259125912591%" id="mcps1.1.4.1.1"><p id="p1180134816518"><a name="p1180134816518"></a><a name="p1180134816518"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.872287228722872%" id="mcps1.1.4.1.2"><p id="p48015489515"><a name="p48015489515"></a><a name="p48015489515"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.21512151215122%" id="mcps1.1.4.1.3"><p id="p158017481854"><a name="p158017481854"></a><a name="p158017481854"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4922113716511"><td class="cellrowborder" valign="top" width="25.91259125912591%" headers="mcps1.1.4.1.1 "><p id="p6922637356"><a name="p6922637356"></a><a name="p6922637356"></a>images</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.872287228722872%" headers="mcps1.1.4.1.2 "><p id="p1092313378517"><a name="p1092313378517"></a><a name="p1092313378517"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.21512151215122%" headers="mcps1.1.4.1.3 "><p id="p19231937154"><a name="p19231937154"></a><a name="p19231937154"></a>Specifies image details.</p>
    <p id="p529384616711"><a name="p529384616711"></a><a name="p529384616711"></a>For details, see <a href="#table170389018811">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  images field description

    <a name="table170389018811"></a>
    <table><thead align="left"><tr id="row1730386618811"><th class="cellrowborder" valign="top" width="35.98359835983598%" id="mcps1.2.4.1.1"><p id="p5943589418811"><a name="p5943589418811"></a><a name="p5943589418811"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.352335233523352%" id="mcps1.2.4.1.2"><p id="p4957807018811"><a name="p4957807018811"></a><a name="p4957807018811"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.664066406640664%" id="mcps1.2.4.1.3"><p id="p5640070618811"><a name="p5640070618811"></a><a name="p5640070618811"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25955412182112"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p49472297182122"><a name="p49472297182122"></a><a name="p49472297182122"></a>file</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p47833140182122"><a name="p47833140182122"></a><a name="p47833140182122"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p49279144182122"><a name="p49279144182122"></a><a name="p49279144182122"></a>Specifies the URL for uploading and downloading the image file.</p>
    </td>
    </tr>
    <tr id="row3995446182130"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p53143569182140"><a name="p53143569182140"></a><a name="p53143569182140"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p9661796182140"><a name="p9661796182140"></a><a name="p9661796182140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p44408049182140"><a name="p44408049182140"></a><a name="p44408049182140"></a>Specifies the image owner.</p>
    </td>
    </tr>
    <tr id="row505449918811"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p676131318811"><a name="p676131318811"></a><a name="p676131318811"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p1079549118811"><a name="p1079549118811"></a><a name="p1079549118811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p201960218811"><a name="p201960218811"></a><a name="p201960218811"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="row57822993182152"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p5599273118226"><a name="p5599273118226"></a><a name="p5599273118226"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p3911735318226"><a name="p3911735318226"></a><a name="p3911735318226"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p1438902818226"><a name="p1438902818226"></a><a name="p1438902818226"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row13561662182215"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p59112046182224"><a name="p59112046182224"></a><a name="p59112046182224"></a>self</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p23346436182224"><a name="p23346436182224"></a><a name="p23346436182224"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p12013170182224"><a name="p12013170182224"></a><a name="p12013170182224"></a>Specifies the image URL.</p>
    </td>
    </tr>
    <tr id="row31851202182230"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p28052241182245"><a name="p28052241182245"></a><a name="p28052241182245"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p57639069182245"><a name="p57639069182245"></a><a name="p57639069182245"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p38253046182245"><a name="p38253046182245"></a><a name="p38253046182245"></a>Specifies the image schema.</p>
    </td>
    </tr>
    <tr id="row50454325182249"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p42064932182259"><a name="p42064932182259"></a><a name="p42064932182259"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p51816298182259"><a name="p51816298182259"></a><a name="p51816298182259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p29539523155411"><a name="p29539523155411"></a><a name="p29539523155411"></a>Specifies the image status. The value can be one of the following:</p>
    <a name="ul64671162155411"></a><a name="ul64671162155411"></a><ul id="ul64671162155411"><li><strong id="b1015505198"><a name="b1015505198"></a><a name="b1015505198"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="b1605711213"><a name="b1605711213"></a><a name="b1605711213"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="b1671608078"><a name="b1671608078"></a><a name="b1671608078"></a>deleted</strong>: indicates that the image has been deleted. </li><li><strong id="b1283122830"><a name="b1283122830"></a><a name="b1283122830"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="b4907138219338"><a name="b4907138219338"></a><a name="b4907138219338"></a>active</strong>: indicates that the image is available for use. </li></ul>
    </td>
    </tr>
    <tr id="row1231408218237"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p40020278182313"><a name="p40020278182313"></a><a name="p40020278182313"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p20417056182313"><a name="p20417056182313"></a><a name="p20417056182313"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p43168822182313"><a name="p43168822182313"></a><a name="p43168822182313"></a>Lists the image tags, through which you can manage private images in your own way. You can use the image tag API to add different tags to each image and filter images by tag.</p>
    </td>
    </tr>
    <tr id="row37439331182318"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p39534954182324"><a name="p39534954182324"></a><a name="p39534954182324"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p48214710182324"><a name="p48214710182324"></a><a name="p48214710182324"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p11477145218812"><a name="p11477145218812"></a><a name="p11477145218812"></a>Specifies whether the image is available to other tenants. Available values include:</p>
    <a name="ul73121940981"></a><a name="ul73121940981"></a><ul id="ul73121940981"><li><strong id="b842352706129"><a name="b842352706129"></a><a name="b842352706129"></a>private</strong>: private image</li><li><strong id="b8335173111114"><a name="b8335173111114"></a><a name="b8335173111114"></a>public</strong>: public image</li><li><strong id="b8423527061151"><a name="b8423527061151"></a><a name="b8423527061151"></a>shared</strong>: shared image</li></ul>
    </td>
    </tr>
    <tr id="row23082108182328"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p58323902182336"><a name="p58323902182336"></a><a name="p58323902182336"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p26615602182336"><a name="p26615602182336"></a><a name="p26615602182336"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p8380147182336"><a name="p8380147182336"></a><a name="p8380147182336"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row37805547182342"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p35561972182354"><a name="p35561972182354"></a><a name="p35561972182354"></a>checksum</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p61947473182354"><a name="p61947473182354"></a><a name="p61947473182354"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p51689398182354"><a name="p51689398182354"></a><a name="p51689398182354"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row44808958182358"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p27347571182413"><a name="p27347571182413"></a><a name="p27347571182413"></a>deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p560768182413"><a name="p560768182413"></a><a name="p560768182413"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p45422229182413"><a name="p45422229182413"></a><a name="p45422229182413"></a>Specifies whether the image has been deleted. The value can be <strong id="b183138284911"><a name="b183138284911"></a><a name="b183138284911"></a>true</strong> or <strong id="b3314132819918"><a name="b3314132819918"></a><a name="b3314132819918"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row53780255182416"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p32490464182427"><a name="p32490464182427"></a><a name="p32490464182427"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p14481960182427"><a name="p14481960182427"></a><a name="p14481960182427"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p32188096182427"><a name="p32188096182427"></a><a name="p32188096182427"></a>Specifies whether the image is protected. A protected image cannot be deleted. The value can be <strong id="b11489404919"><a name="b11489404919"></a><a name="b11489404919"></a>true</strong> or <strong id="b2014924018914"><a name="b2014924018914"></a><a name="b2014924018914"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row36425014182430"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p56996481182439"><a name="p56996481182439"></a><a name="p56996481182439"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p53312254182439"><a name="p53312254182439"></a><a name="p53312254182439"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p23325336182439"><a name="p23325336182439"></a><a name="p23325336182439"></a>Specifies the container type. </p>
    </td>
    </tr>
    <tr id="row25669301182443"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p38526266182452"><a name="p38526266182452"></a><a name="p38526266182452"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p33619874182452"><a name="p33619874182452"></a><a name="p33619874182452"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p38855258182452"><a name="p38855258182452"></a><a name="p38855258182452"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the <span id="text1363162522612"><a name="text1363162522612"></a><a name="text1363162522612"></a></span><span id="text531719277268"><a name="text531719277268"></a><a name="text531719277268"></a>ECS</span> flavor. Generally, the value is <strong id="b842352706103121"><a name="b842352706103121"></a><a name="b842352706103121"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row421218589235"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p564272999235"><a name="p564272999235"></a><a name="p564272999235"></a>max_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p470176959235"><a name="p470176959235"></a><a name="p470176959235"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p503369709235"><a name="p503369709235"></a><a name="p503369709235"></a>Specifies the maximum memory of the image in the unit of MB. You can set this parameter based on the <span id="text818523316267"><a name="text818523316267"></a><a name="text818523316267"></a></span><span id="text518503312612"><a name="text518503312612"></a><a name="text518503312612"></a>ECS</span> flavor. Generally, you do not need to set this parameter.</p>
    </td>
    </tr>
    <tr id="row57504296182455"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p845423318254"><a name="p845423318254"></a><a name="p845423318254"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p1370428818254"><a name="p1370428818254"></a><a name="p1370428818254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p3630557218254"><a name="p3630557218254"></a><a name="p3630557218254"></a>Specifies the time when the image was updated. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row1769773418257"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p17502211182519"><a name="p17502211182519"></a><a name="p17502211182519"></a>__os_bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p8393024182519"><a name="p8393024182519"></a><a name="p8393024182519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p8746333182519"><a name="p8746333182519"></a><a name="p8746333182519"></a>Specifies the OS architecture: <strong id="b48951529142847"><a name="b48951529142847"></a><a name="b48951529142847"></a>32</strong> or <strong id="b37910577142847"><a name="b37910577142847"></a><a name="b37910577142847"></a>64</strong>.</p>
    </td>
    </tr>
    <tr id="row39365379182524"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p62280478182534"><a name="p62280478182534"></a><a name="p62280478182534"></a>__os_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p11553944182534"><a name="p11553944182534"></a><a name="p11553944182534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p63454291182534"><a name="p63454291182534"></a><a name="p63454291182534"></a>Specifies the OS version.</p>
    </td>
    </tr>
    <tr id="row839271182539"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p36672817182557"><a name="p36672817182557"></a><a name="p36672817182557"></a>__description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p17708216182557"><a name="p17708216182557"></a><a name="p17708216182557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p25079420182557"><a name="p25079420182557"></a><a name="p25079420182557"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row639399118261"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p22661284182614"><a name="p22661284182614"></a><a name="p22661284182614"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p23624729182614"><a name="p23624729182614"></a><a name="p23624729182614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p34554882182614"><a name="p34554882182614"></a><a name="p34554882182614"></a>Specifies the image format. The value can be <strong id="b34731386558"><a name="b34731386558"></a><a name="b34731386558"></a>vhd</strong>, <strong id="b134741385556"><a name="b134741385556"></a><a name="b134741385556"></a>raw</strong>, <strong id="b74748380552"><a name="b74748380552"></a><a name="b74748380552"></a>zvhd</strong>, or <strong id="b134761438155512"><a name="b134761438155512"></a><a name="b134761438155512"></a>qcow2</strong>. The default value is <strong id="b448329028"><a name="b448329028"></a><a name="b448329028"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="row63056520182618"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p53962863182716"><a name="p53962863182716"></a><a name="p53962863182716"></a>__isregistered</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p8915762182716"><a name="p8915762182716"></a><a name="p8915762182716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p51088093182716"><a name="p51088093182716"></a><a name="p51088093182716"></a>Specifies whether the image has been registered. The value can be <strong id="b10597638151211"><a name="b10597638151211"></a><a name="b10597638151211"></a>true</strong> or <strong id="b19597203831210"><a name="b19597203831210"></a><a name="b19597203831210"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row2950367182721"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p61765095182736"><a name="p61765095182736"></a><a name="p61765095182736"></a>__platform</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p36916779182736"><a name="p36916779182736"></a><a name="p36916779182736"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p37469116182736"><a name="p37469116182736"></a><a name="p37469116182736"></a>Specifies the image platform type. The value can be <strong id="b3109165411219"><a name="b3109165411219"></a><a name="b3109165411219"></a>Windows</strong>, <strong id="b6110125431213"><a name="b6110125431213"></a><a name="b6110125431213"></a>Ubuntu</strong>, <strong id="b1311195411211"><a name="b1311195411211"></a><a name="b1311195411211"></a>RedHat</strong>, <strong id="b711215416121"><a name="b711215416121"></a><a name="b711215416121"></a>SUSE</strong>, <strong id="b111131854121212"><a name="b111131854121212"></a><a name="b111131854121212"></a>CentOS</strong>, <strong id="b2011465411129"><a name="b2011465411129"></a><a name="b2011465411129"></a>Debian</strong>, <strong id="b11155546125"><a name="b11155546125"></a><a name="b11155546125"></a>OpenSUSE</strong>, <strong id="b20115165421215"><a name="b20115165421215"></a><a name="b20115165421215"></a>Oracle Linux</strong>, <strong id="b2011615471212"><a name="b2011615471212"></a><a name="b2011615471212"></a>Fedora</strong>, <strong id="b2117154161211"><a name="b2117154161211"></a><a name="b2117154161211"></a>Other</strong>, <strong id="b1611812549122"><a name="b1611812549122"></a><a name="b1611812549122"></a>CoreOS</strong>, or <strong id="b121181654141212"><a name="b121181654141212"></a><a name="b121181654141212"></a>EulerOS</strong>.</p>
    </td>
    </tr>
    <tr id="row26342105182740"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p49638838182752"><a name="p49638838182752"></a><a name="p49638838182752"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p61322937182752"><a name="p61322937182752"></a><a name="p61322937182752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p1102009182752"><a name="p1102009182752"></a><a name="p1102009182752"></a>Specifies the OS type. The value can be <strong id="b97281323152910"><a name="b97281323152910"></a><a name="b97281323152910"></a>Linux</strong>, <strong id="b872902314297"><a name="b872902314297"></a><a name="b872902314297"></a>Windows</strong>, or <strong id="b7729182313298"><a name="b7729182313298"></a><a name="b7729182313298"></a>Other</strong>.</p>
    </td>
    </tr>
    <tr id="row36189690182758"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p5779514118287"><a name="p5779514118287"></a><a name="p5779514118287"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p5089488218287"><a name="p5089488218287"></a><a name="p5089488218287"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p831474155851"><a name="p831474155851"></a><a name="p831474155851"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
    </td>
    </tr>
    <tr id="row54457844182812"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p39421864182824"><a name="p39421864182824"></a><a name="p39421864182824"></a>virtual_env_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p39054417182824"><a name="p39054417182824"></a><a name="p39054417182824"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p1274513459339"><a name="p1274513459339"></a><a name="p1274513459339"></a>Specifies the environment where the image is used. The value can be <strong id="b279115600"><a name="b279115600"></a><a name="b279115600"></a>FusionCompute</strong>, <strong id="b825217156"><a name="b825217156"></a><a name="b825217156"></a>Ironic</strong>, or <strong id="b1992309829"><a name="b1992309829"></a><a name="b1992309829"></a>DataImage</strong>.</p>
    <a name="ul663520313419"></a><a name="ul663520313419"></a><ul id="ul663520313419"><li>For an <span id="text112717547261"><a name="text112717547261"></a><a name="text112717547261"></a></span><span id="text1271145411263"><a name="text1271145411263"></a><a name="text1271145411263"></a>ECS</span> image, the value is <strong id="b6200101517432"><a name="b6200101517432"></a><a name="b6200101517432"></a>FusionCompute</strong>.</li><li>For a data disk image, set the value to <strong id="b22449504126"><a name="b22449504126"></a><a name="b22449504126"></a>DataImage</strong>.</li><li>For a <span id="text106932038273"><a name="text106932038273"></a><a name="text106932038273"></a></span><span id="text14544582713"><a name="text14544582713"></a><a name="text14544582713"></a>BMS</span> image, the value is <strong id="b975661615437"><a name="b975661615437"></a><a name="b975661615437"></a>Ironic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row62572790182919"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p34522680182932"><a name="p34522680182932"></a><a name="p34522680182932"></a>__image_source_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p44873729182932"><a name="p44873729182932"></a><a name="p44873729182932"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p63045351195118"><a name="p63045351195118"></a><a name="p63045351195118"></a>Specifies the image backend storage type. Only UDS is supported currently. </p>
    </td>
    </tr>
    <tr id="row63838629182939"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p7496393182954"><a name="p7496393182954"></a><a name="p7496393182954"></a>__imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p3228135182954"><a name="p3228135182954"></a><a name="p3228135182954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p5395112132212"><a name="p5395112132212"></a><a name="p5395112132212"></a>Specifies the image type. The following types are supported:</p>
    <a name="ul1882634912228"></a><a name="ul1882634912228"></a><ul id="ul1882634912228"><li>Public image: The value is <strong id="b708092423"><a name="b708092423"></a><a name="b708092423"></a>gold</strong>.</li><li>Private image: The value is <strong id="b629175765"><a name="b629175765"></a><a name="b629175765"></a>private</strong>.</li><li>Shared image: The value is <strong id="b1091618379"><a name="b1091618379"></a><a name="b1091618379"></a>shared</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row36484934182957"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p49948470183018"><a name="p49948470183018"></a><a name="p49948470183018"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p19294250183018"><a name="p19294250183018"></a><a name="p19294250183018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p19330411183018"><a name="p19330411183018"></a><a name="p19330411183018"></a>Specifies the time when the image was created. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row3890812183030"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p62610599183041"><a name="p62610599183041"></a><a name="p62610599183041"></a>virtual_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p38293786183041"><a name="p38293786183041"></a><a name="p38293786183041"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p14788941183041"><a name="p14788941183041"></a><a name="p14788941183041"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row13477777182830"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p14362031182847"><a name="p14362031182847"></a><a name="p14362031182847"></a>deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p22473828182847"><a name="p22473828182847"></a><a name="p22473828182847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p8440757182847"><a name="p8440757182847"></a><a name="p8440757182847"></a>Specifies the time when the image was deleted. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row47506658182851"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p66461089183149"><a name="p66461089183149"></a><a name="p66461089183149"></a>__originalimagename</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p14639168183149"><a name="p14639168183149"></a><a name="p14639168183149"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p44921992183149"><a name="p44921992183149"></a><a name="p44921992183149"></a>Specifies the parent image ID.</p>
    <p id="p112565193443"><a name="p112565193443"></a><a name="p112565193443"></a>If the image is a public image or created from an image file, this value is left empty.</p>
    </td>
    </tr>
    <tr id="row4935361618321"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p28374236183215"><a name="p28374236183215"></a><a name="p28374236183215"></a>__backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p16611755183215"><a name="p16611755183215"></a><a name="p16611755183215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p3374903183215"><a name="p3374903183215"></a><a name="p3374903183215"></a>Specifies the backup ID. To create an image using a backup, set the value to the backup ID. Otherwise, this value is left empty.</p>
    </td>
    </tr>
    <tr id="row32585151183219"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p9749764183233"><a name="p9749764183233"></a><a name="p9749764183233"></a>__productcode</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p51533395183233"><a name="p51533395183233"></a><a name="p51533395183233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p13455455183233"><a name="p13455455183233"></a><a name="p13455455183233"></a>Specifies the ID of the market image product.</p>
    </td>
    </tr>
    <tr id="row66180851183258"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p41163708183313"><a name="p41163708183313"></a><a name="p41163708183313"></a>__image_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p45926072183313"><a name="p45926072183313"></a><a name="p45926072183313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p29024385183313"><a name="p29024385183313"></a><a name="p29024385183313"></a>Specifies the size (bytes) of the image file.</p>
    </td>
    </tr>
    <tr id="row1817642118811"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p19484916183313"><a name="p19484916183313"></a><a name="p19484916183313"></a>__data_origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p34774363183313"><a name="p34774363183313"></a><a name="p34774363183313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p65260010183313"><a name="p65260010183313"></a><a name="p65260010183313"></a>Specifies the image resource.</p>
    <p id="p44760550194513"><a name="p44760550194513"></a><a name="p44760550194513"></a>If the image is a public image, this parameter is left empty.</p>
    </td>
    </tr>
    <tr id="row1013168131918"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p1238917131191"><a name="p1238917131191"></a><a name="p1238917131191"></a>__support_kvm</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p1438991320192"><a name="p1438991320192"></a><a name="p1438991320192"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p1638916137192"><a name="p1638916137192"></a><a name="p1638916137192"></a>Specifies whether the image supports KVM. If yes, the value is <strong id="b1338897782"><a name="b1338897782"></a><a name="b1338897782"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row21311816197"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p239091316191"><a name="p239091316191"></a><a name="p239091316191"></a>__support_xen</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p63905139194"><a name="p63905139194"></a><a name="p63905139194"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p17390181313198"><a name="p17390181313198"></a><a name="p17390181313198"></a>Specifies whether the image supports Xen. If yes, the value is <strong id="b1990568247"><a name="b1990568247"></a><a name="b1990568247"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row12131198151919"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p23912013171913"><a name="p23912013171913"></a><a name="p23912013171913"></a>__support_largememory</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p1939113133194"><a name="p1939113133194"></a><a name="p1939113133194"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p23915133198"><a name="p23915133198"></a><a name="p23915133198"></a>Specifies whether the image supports large-memory ECSs. If the image supports large-memory ECSs, the value is <strong id="b2012422213"><a name="b2012422213"></a><a name="b2012422213"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row1013198201912"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p039121321910"><a name="p039121321910"></a><a name="p039121321910"></a>__support_diskintensive</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p20392513101911"><a name="p20392513101911"></a><a name="p20392513101911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p43928138193"><a name="p43928138193"></a><a name="p43928138193"></a>Specifies whether the image supports disk-intensive ECSs. If the image supports disk-intensive ECSs, the value is <strong id="b1011792108"><a name="b1011792108"></a><a name="b1011792108"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row1452585612185"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p113929133192"><a name="p113929133192"></a><a name="p113929133192"></a>__support_highperformance</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p139218136195"><a name="p139218136195"></a><a name="p139218136195"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p10392713201914"><a name="p10392713201914"></a><a name="p10392713201914"></a>Specifies whether the image supports high-performance ECSs. If the image supports high-performance ECSs, the value is <strong id="b151877904"><a name="b151877904"></a><a name="b151877904"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row10525155651812"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p1739211312199"><a name="p1739211312199"></a><a name="p1739211312199"></a>__support_xen_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p73921613171918"><a name="p73921613171918"></a><a name="p73921613171918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p3393913191912"><a name="p3393913191912"></a><a name="p3393913191912"></a>The image supports GPU-optimized ECSs on the Xen platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the Xen platform, this attribute is not required. This attribute cannot co-exist with <strong id="b605279788"><a name="b605279788"></a><a name="b605279788"></a>__support_xen</strong> and <strong id="b643661079"><a name="b643661079"></a><a name="b643661079"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row8525656141816"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p173932134198"><a name="p173932134198"></a><a name="p173932134198"></a>__support_kvm_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p18393191301910"><a name="p18393191301910"></a><a name="p18393191301910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p1639310137194"><a name="p1639310137194"></a><a name="p1639310137194"></a>Specifies whether the image supports GPU-optimized ECSs on the KVM platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value.</p>
    <p id="p113931113141910"><a name="p113931113141910"></a><a name="p113931113141910"></a>If the image does not support GPU-optimized ECSs on the KVM platform, this attribute is not required. This attribute cannot co-exist with <strong id="b1361377420"><a name="b1361377420"></a><a name="b1361377420"></a>__support_xen</strong> and <strong id="b304338919"><a name="b304338919"></a><a name="b304338919"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row45251256121819"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p1339312134195"><a name="p1339312134195"></a><a name="p1339312134195"></a>__support_xen_hana</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p12394713111920"><a name="p12394713111920"></a><a name="p12394713111920"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p7394141371914"><a name="p7394141371914"></a><a name="p7394141371914"></a>Specifies whether the image supports HANA ECSs on the Xen platform. If yes, the value is <strong id="b1883626270"><a name="b1883626270"></a><a name="b1883626270"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p139441312191"><a name="p139441312191"></a><a name="p139441312191"></a>This attribute cannot co-exist with <strong id="b950954457"><a name="b950954457"></a><a name="b950954457"></a>__support_xen</strong> and <strong id="b150495984"><a name="b150495984"></a><a name="b150495984"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row55251756151811"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p1539418138191"><a name="p1539418138191"></a><a name="p1539418138191"></a>__support_kvm_infiniband</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p1639471351915"><a name="p1639471351915"></a><a name="p1639471351915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p439415130196"><a name="p439415130196"></a><a name="p439415130196"></a>Specifies whether the image supports ECSs with the InfiniBand NIC on the KVM platform. If yes, the value is <strong id="b772751179"><a name="b772751179"></a><a name="b772751179"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p19394913111916"><a name="p19394913111916"></a><a name="p19394913111916"></a>This attribute cannot co-exist with <strong id="b484359826"><a name="b484359826"></a><a name="b484359826"></a>__support_xen</strong>.</p>
    </td>
    </tr>
    <tr id="row1028349015051"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p341211511512"><a name="p341211511512"></a><a name="p341211511512"></a>__system_support_market</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p608164341512"><a name="p608164341512"></a><a name="p608164341512"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p271841421512"><a name="p271841421512"></a><a name="p271841421512"></a>Specifies whether an image can be published in Marketplace.</p>
    <a name="ul12711341518"></a><a name="ul12711341518"></a><ul id="ul12711341518"><li><strong id="b115307561015"><a name="b115307561015"></a><a name="b115307561015"></a>true</strong>: supported</li><li><strong id="b1444518582001"><a name="b1444518582001"></a><a name="b1444518582001"></a>false</strong>: not supported</li></ul>
    </td>
    </tr>
    <tr id="row2045917411334"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p1021161112333"><a name="p1021161112333"></a><a name="p1021161112333"></a>__root_origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p637311103320"><a name="p637311103320"></a><a name="p637311103320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p937411163318"><a name="p937411163318"></a><a name="p937411163318"></a>Indicates that the image is created from an external image file. Example value: <strong id="b842352706155810"><a name="b842352706155810"></a><a name="b842352706155810"></a>file</strong></p>
    </td>
    </tr>
    <tr id="row125991973311"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p1152411163311"><a name="p1152411163311"></a><a name="p1152411163311"></a>__sequence_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p95251143318"><a name="p95251143318"></a><a name="p95251143318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p116891133317"><a name="p116891133317"></a><a name="p116891133317"></a>Specifies the <span id="text99702092918"><a name="text99702092918"></a><a name="text99702092918"></a></span><span id="text8970130132912"><a name="text8970130132912"></a><a name="text8970130132912"></a>ECS</span> system disk slot number corresponding to the image.</p>
    <p id="p468511113315"><a name="p468511113315"></a><a name="p468511113315"></a>Example value: <strong id="b1725596370"><a name="b1725596370"></a><a name="b1725596370"></a>0</strong></p>
    </td>
    </tr>
    <tr id="row126971035123615"><td class="cellrowborder" valign="top" width="35.98359835983598%" headers="mcps1.2.4.1.1 "><p id="p153691656103613"><a name="p153691656103613"></a><a name="p153691656103613"></a>hw_firmware_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.352335233523352%" headers="mcps1.2.4.1.2 "><p id="p236975618366"><a name="p236975618366"></a><a name="p236975618366"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.664066406640664%" headers="mcps1.2.4.1.3 "><p id="p4369115617362"><a name="p4369115617362"></a><a name="p4369115617362"></a>Specifies the <span id="text13144818162917"><a name="text13144818162917"></a><a name="text13144818162917"></a></span><span id="text10144141872913"><a name="text10144141872913"></a><a name="text10144141872913"></a>ECS</span> boot mode. Available values include:</p>
    <a name="ul8369165616362"></a><a name="ul8369165616362"></a><ul id="ul8369165616362"><li><strong id="b1233310017144"><a name="b1233310017144"></a><a name="b1233310017144"></a>bios</strong> indicates the BIOS boot mode.</li><li><strong id="b571354171414"><a name="b571354171414"></a><a name="b571354171414"></a>uefi</strong> indicates the UEFI boot mode.</li></ul>
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
      "images": [
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
          "hw_firmware_type": "bios",
          "status": "active",
          "__support_fc_inject":"true"
        },
        {
          "schema": "/v2/schemas/image",
          "min_disk": 100,
          "created_at": "2018-09-06T14:03:05Z",
          "__image_source_type": "uds",
          "container_format": "bare",
          "file": "/v2/images/0328c25e-c840-4496-81ac-c4e01b214b1f/file",
          "updated_at": "2018-09-25T14:27:40Z",
          "protected": true,
          "checksum": "d41d8cd98f00b204e9800998ecf8427e",
          "__support_kvm_fpga_type": "VU9P_COMMON",
          "id": "0328c25e-c840-4496-81ac-c4e01b214b1f",
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
          "name": "CentOS 7.3 64bit with sdx",
          "self": "/v2/images/0328c25e-c840-4496-81ac-c4e01b214b1f",
          "disk_format": "zvhd2",
          "virtual_size": null,
          "hw_firmware_type": "bios",
          "status": "active",
          "__support_fc_inject":"true"
        }
      ]
    }
    ```


## Returned Values<a name="section20875522"></a>

-   Normal

    200

-   Abnormal

    <a name="table25137814143431"></a>
    <table><thead align="left"><tr id="row38004410143431"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p58458378143431"><a name="p58458378143431"></a><a name="p58458378143431"></a><strong id="b84235270616144"><a name="b84235270616144"></a><a name="b84235270616144"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p18261951143431"><a name="p18261951143431"></a><a name="p18261951143431"></a><strong id="b84235270616147"><a name="b84235270616147"></a><a name="b84235270616147"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2823028143431"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p27338693143431"><a name="p27338693143431"></a><a name="p27338693143431"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p54285918143431"><a name="p54285918143431"></a><a name="p54285918143431"></a>Request error. For details about the returned error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row35083253143431"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p23171273143431"><a name="p23171273143431"></a><a name="p23171273143431"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p25148486143431"><a name="p25148486143431"></a><a name="p25148486143431"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row25009784143431"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p12526651143431"><a name="p12526651143431"></a><a name="p12526651143431"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p46109225143431"><a name="p46109225143431"></a><a name="p46109225143431"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row15098650192329"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p3586211192331"><a name="p3586211192331"></a><a name="p3586211192331"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p22047708192331"><a name="p22047708192331"></a><a name="p22047708192331"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row12329845143431"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p59193425143431"><a name="p59193425143431"></a><a name="p59193425143431"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p9066084143431"><a name="p9066084143431"></a><a name="p9066084143431"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row14485900143431"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p32507226143431"><a name="p32507226143431"></a><a name="p32507226143431"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p7940519143431"><a name="p7940519143431"></a><a name="p7940519143431"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


