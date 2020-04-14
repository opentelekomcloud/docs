# Creating an Image<a name="EN-US_TOPIC_0020092109"></a>

## Function<a name="section29995926"></a>

This API is used to create a private image. The following methods are supported:

-   Create a private image from an ECS.
-   Create a private image from an external image file uploaded to an OBS bucket.

The API is an asynchronous one. If it is successfully called, the cloud service system receives the request. However, you need to use the asynchronous job query API to query the image creation status. For details, see  [Asynchronous Job Query](asynchronous-job-query.md).

You cannot export public images \(such as Windows, SUSE Linux, Red Hat Linux, Oracle Linux, and Ubuntu\) or private images created using these public images.

## URI<a name="section1527883"></a>

POST /v2/cloudimages/action

## Request<a name="section13750947"></a>

-   Parameters for creating an image from an ECS

    <a name="table62551043151553"></a>
    <table><thead align="left"><tr id="row63356413151553"><th class="cellrowborder" valign="top" width="21.242124212421242%" id="mcps1.1.5.1.1"><p id="p41292683151745"><a name="p41292683151745"></a><a name="p41292683151745"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.172217221722175%" id="mcps1.1.5.1.2"><p id="p51323166151745"><a name="p51323166151745"></a><a name="p51323166151745"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.5.1.3"><p id="p36943663151745"><a name="p36943663151745"></a><a name="p36943663151745"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.73417341734174%" id="mcps1.1.5.1.4"><p id="p16401653151745"><a name="p16401653151745"></a><a name="p16401653151745"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58293752151553"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.1.5.1.1 "><p id="p24173439151553"><a name="p24173439151553"></a><a name="p24173439151553"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.172217221722175%" headers="mcps1.1.5.1.2 "><p id="p18429535194412"><a name="p18429535194412"></a><a name="p18429535194412"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p23692580151553"><a name="p23692580151553"></a><a name="p23692580151553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.1.5.1.4 "><p id="p40050833151553"><a name="p40050833151553"></a><a name="p40050833151553"></a>Specifies the name of the system disk image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row57744127151553"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.1.5.1.1 "><p id="p46762671151553"><a name="p46762671151553"></a><a name="p46762671151553"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.172217221722175%" headers="mcps1.1.5.1.2 "><p id="p29679979151553"><a name="p29679979151553"></a><a name="p29679979151553"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p55268124151553"><a name="p55268124151553"></a><a name="p55268124151553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.1.5.1.4 "><p id="p47533098151553"><a name="p47533098151553"></a><a name="p47533098151553"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>. The value contains a maximum of 1024 characters and consists of only letters and digits. Carriage returns and angle brackets (&lt; &gt;) are not allowed. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row25144703151553"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.1.5.1.1 "><p id="p23455075151553"><a name="p23455075151553"></a><a name="p23455075151553"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.172217221722175%" headers="mcps1.1.5.1.2 "><p id="p203181545144419"><a name="p203181545144419"></a><a name="p203181545144419"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p8122243151553"><a name="p8122243151553"></a><a name="p8122243151553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.1.5.1.4 "><p id="p53921936151553"><a name="p53921936151553"></a><a name="p53921936151553"></a>Specifies the ID of the <span id="text13824145813499"><a name="text13824145813499"></a><a name="text13824145813499"></a></span><span id="text78241658114918"><a name="text78241658114918"></a><a name="text78241658114918"></a>ECS</span> used to create the image.</p>
    <p id="p188578234320"><a name="p188578234320"></a><a name="p188578234320"></a>To obtain the <span id="text19693162115016"><a name="text19693162115016"></a><a name="text19693162115016"></a></span><span id="text669317255014"><a name="text669317255014"></a><a name="text669317255014"></a>ECS</span> ID, perform the following operations:</p>
    <a name="ol388062213448"></a><a name="ol388062213448"></a><ol id="ol388062213448"><li>Log in to management console.</li><li>Under <strong id="b125126462014"><a name="b125126462014"></a><a name="b125126462014"></a>Computing</strong>, click <strong id="b1298610211209"><a name="b1298610211209"></a><a name="b1298610211209"></a>Elastic Cloud Server</strong>.</li><li>In the ECS list, click the name of the <span id="text19221104075012"><a name="text19221104075012"></a><a name="text19221104075012"></a></span><span id="text4221184010501"><a name="text4221184010501"></a><a name="text4221184010501"></a>ECS</span> and view its ID.</li></ol>
    </td>
    </tr>
    <tr id="row24935094113949"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.1.5.1.1 "><p id="p2769180113957"><a name="p2769180113957"></a><a name="p2769180113957"></a>data_images</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.172217221722175%" headers="mcps1.1.5.1.2 "><p id="p22843825113957"><a name="p22843825113957"></a><a name="p22843825113957"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p12614986113957"><a name="p12614986113957"></a><a name="p12614986113957"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.1.5.1.4 "><p id="p877019466455"><a name="p877019466455"></a><a name="p877019466455"></a>Specifies the data disk information to be converted. This parameter is mandatory when the data disk of an <span id="text188721725125318"><a name="text188721725125318"></a><a name="text188721725125318"></a></span><span id="text0872625115317"><a name="text0872625115317"></a><a name="text0872625115317"></a>ECS</span> is used to create a private data disk image. For details, see <a href="#table19600131217507">Table 1</a>.</p>
    <p id="p88041225142519"><a name="p88041225142519"></a><a name="p88041225142519"></a>If the ECS data disk is not used to create a data disk image, the parameter is empty by default.</p>
    <div class="note" id="note131418296548"><a name="note131418296548"></a><a name="note131418296548"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p43151290549"><a name="p43151290549"></a><a name="p43151290549"></a>When you create a data disk image using a data disk, if other parameters (such as <strong id="b141191829546"><a name="b141191829546"></a><a name="b141191829546"></a>name</strong>, <strong id="b172221432445"><a name="b172221432445"></a><a name="b172221432445"></a>description</strong>, and <strong id="b271084317411"><a name="b271084317411"></a><a name="b271084317411"></a>tags</strong>) in this table have values, the system uses the value of <strong id="b196401971651"><a name="b196401971651"></a><a name="b196401971651"></a>data_images</strong>. You cannot specify <strong id="b438516291553"><a name="b438516291553"></a><a name="b438516291553"></a>instance_id</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row30504483181035"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.1.5.1.1 "><p id="p56306980181056"><a name="p56306980181056"></a><a name="p56306980181056"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.172217221722175%" headers="mcps1.1.5.1.2 "><p id="p64571566181056"><a name="p64571566181056"></a><a name="p64571566181056"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p62914385181056"><a name="p62914385181056"></a><a name="p62914385181056"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.1.5.1.4 "><p id="p62900404181056"><a name="p62900404181056"></a><a name="p62900404181056"></a>Lists the image tags. This parameter is left blank by default.</p>
    <p id="p20992085173243"><a name="p20992085173243"></a><a name="p20992085173243"></a>Use either <strong id="b84235270693042"><a name="b84235270693042"></a><a name="b84235270693042"></a>tags</strong> or <strong id="b84235270693044"><a name="b84235270693044"></a><a name="b84235270693044"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row36234066184027"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.1.5.1.1 "><p id="p30481145184039"><a name="p30481145184039"></a><a name="p30481145184039"></a>image_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.172217221722175%" headers="mcps1.1.5.1.2 "><p id="p53053656184039"><a name="p53053656184039"></a><a name="p53053656184039"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p2378868184039"><a name="p2378868184039"></a><a name="p2378868184039"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.1.5.1.4 "><p id="p5510142012586"><a name="p5510142012586"></a><a name="p5510142012586"></a>Lists the image tags. This parameter is left blank by default.</p>
    <p id="p58470580184039"><a name="p58470580184039"></a><a name="p58470580184039"></a>Use either <strong id="b1234904531"><a name="b1234904531"></a><a name="b1234904531"></a>tags</strong> or <strong id="b1135817067"><a name="b1135817067"></a><a name="b1135817067"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row542396829715"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.1.5.1.1 "><p id="p313381039715"><a name="p313381039715"></a><a name="p313381039715"></a>max_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.172217221722175%" headers="mcps1.1.5.1.2 "><p id="p553584299715"><a name="p553584299715"></a><a name="p553584299715"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p548477719715"><a name="p548477719715"></a><a name="p548477719715"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.1.5.1.4 "><p id="p134845069715"><a name="p134845069715"></a><a name="p134845069715"></a>Specifies the maximum memory of the image in the unit of MB.</p>
    </td>
    </tr>
    <tr id="row345004879812"><td class="cellrowborder" valign="top" width="21.242124212421242%" headers="mcps1.1.5.1.1 "><p id="p430760399812"><a name="p430760399812"></a><a name="p430760399812"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.172217221722175%" headers="mcps1.1.5.1.2 "><p id="p666071449812"><a name="p666071449812"></a><a name="p666071449812"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.3 "><p id="p264695859812"><a name="p264695859812"></a><a name="p264695859812"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.73417341734174%" headers="mcps1.1.5.1.4 "><p id="p636616759812"><a name="p636616759812"></a><a name="p636616759812"></a>Specifies the minimum memory of the image in the unit of MB. The default value is <strong id="b84235270617155"><a name="b84235270617155"></a><a name="b84235270617155"></a>0</strong>, indicating that the memory is not restricted.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Data structure description of the  **data\_images**  field

    <a name="table19600131217507"></a>
    <table><thead align="left"><tr id="row660120127503"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.1"><p id="p1268419544509"><a name="p1268419544509"></a><a name="p1268419544509"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.55%" id="mcps1.2.5.1.2"><p id="p1268475455020"><a name="p1268475455020"></a><a name="p1268475455020"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.23%" id="mcps1.2.5.1.3"><p id="p11684354145015"><a name="p11684354145015"></a><a name="p11684354145015"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.480000000000004%" id="mcps1.2.5.1.4"><p id="p1268725475017"><a name="p1268725475017"></a><a name="p1268725475017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1060141285015"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p960112128502"><a name="p960112128502"></a><a name="p960112128502"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.55%" headers="mcps1.2.5.1.2 "><p id="p660115122507"><a name="p660115122507"></a><a name="p660115122507"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.5.1.3 "><p id="p060181211501"><a name="p060181211501"></a><a name="p060181211501"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p196011512175018"><a name="p196011512175018"></a><a name="p196011512175018"></a>Specifies the name of a data disk image.</p>
    </td>
    </tr>
    <tr id="row16601512145018"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p14601112195015"><a name="p14601112195015"></a><a name="p14601112195015"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.55%" headers="mcps1.2.5.1.2 "><p id="p460114121505"><a name="p460114121505"></a><a name="p460114121505"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.5.1.3 "><p id="p1060191295017"><a name="p1060191295017"></a><a name="p1060191295017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p9601141215507"><a name="p9601141215507"></a><a name="p9601141215507"></a>Specifies the data disk ID.</p>
    </td>
    </tr>
    <tr id="row1991233195111"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p1699313318516"><a name="p1699313318516"></a><a name="p1699313318516"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.55%" headers="mcps1.2.5.1.2 "><p id="p13372545165110"><a name="p13372545165110"></a><a name="p13372545165110"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.5.1.3 "><p id="p19993203319512"><a name="p19993203319512"></a><a name="p19993203319512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p1993113395112"><a name="p1993113395112"></a><a name="p1993113395112"></a>Specifies the data disk description.</p>
    </td>
    </tr>
    <tr id="row11650164016513"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p1065112403516"><a name="p1065112403516"></a><a name="p1065112403516"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.55%" headers="mcps1.2.5.1.2 "><p id="p19397194545118"><a name="p19397194545118"></a><a name="p19397194545118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23%" headers="mcps1.2.5.1.3 "><p id="p7651134011512"><a name="p7651134011512"></a><a name="p7651134011512"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p2651174010519"><a name="p2651174010519"></a><a name="p2651174010519"></a>Specifies the data disk image tag.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameters description when an image file uploaded to the OBS bucket is used to create an image

    <a name="table2165501011128"></a>
    <table><thead align="left"><tr id="row2548881211128"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.5.1.1"><p id="p5132791211128"><a name="p5132791211128"></a><a name="p5132791211128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.18%" id="mcps1.1.5.1.2"><p id="p6392024111128"><a name="p6392024111128"></a><a name="p6392024111128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.84%" id="mcps1.1.5.1.3"><p id="p1015703811128"><a name="p1015703811128"></a><a name="p1015703811128"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.55%" id="mcps1.1.5.1.4"><p id="p1741376811128"><a name="p1741376811128"></a><a name="p1741376811128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row122909411128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p3244779311128"><a name="p3244779311128"></a><a name="p3244779311128"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p1102555211128"><a name="p1102555211128"></a><a name="p1102555211128"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p2065450811128"><a name="p2065450811128"></a><a name="p2065450811128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p25100359152023"><a name="p25100359152023"></a><a name="p25100359152023"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row2475079711128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p5865753511128"><a name="p5865753511128"></a><a name="p5865753511128"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p5363988111128"><a name="p5363988111128"></a><a name="p5363988111128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p4986312411128"><a name="p4986312411128"></a><a name="p4986312411128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p1238125611128"><a name="p1238125611128"></a><a name="p1238125611128"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>. The value contains a maximum of 1024 characters and consists of only letters and digits. Carriage returns and angle brackets (&lt; &gt;) are not allowed. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row39976861514"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p8997687153"><a name="p8997687153"></a><a name="p8997687153"></a>os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p129979821519"><a name="p129979821519"></a><a name="p129979821519"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p39971984157"><a name="p39971984157"></a><a name="p39971984157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p1099798111518"><a name="p1099798111518"></a><a name="p1099798111518"></a>Specifies the OS type.</p>
    <p id="p11611164381516"><a name="p11611164381516"></a><a name="p11611164381516"></a>The value can be <strong id="b37171745192714"><a name="b37171745192714"></a><a name="b37171745192714"></a>Linux</strong>, <strong id="b17732194514279"><a name="b17732194514279"></a><a name="b17732194514279"></a>Windows</strong>, or <strong id="b157331445152713"><a name="b157331445152713"></a><a name="b157331445152713"></a>Other</strong>.</p>
    </td>
    </tr>
    <tr id="row21556993144512"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p1647705215747"><a name="p1647705215747"></a><a name="p1647705215747"></a>os_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p5957279815747"><a name="p5957279815747"></a><a name="p5957279815747"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p6066734915747"><a name="p6066734915747"></a><a name="p6066734915747"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p16255898151029"><a name="p16255898151029"></a><a name="p16255898151029"></a>Specifies the OS version.</p>
    <p id="p1510826515747"><a name="p1510826515747"></a><a name="p1510826515747"></a>This parameter is valid if an external image file uploaded to the OBS bucket is used to create an image. For its value, see <a href="values-of-related-parameters.md">Values of Related Parameters</a>.</p>
    </td>
    </tr>
    <tr id="row35447872144512"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p2534737915133"><a name="p2534737915133"></a><a name="p2534737915133"></a>image_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p3987185215133"><a name="p3987185215133"></a><a name="p3987185215133"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p839458515133"><a name="p839458515133"></a><a name="p839458515133"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p18464621151313"><a name="p18464621151313"></a><a name="p18464621151313"></a>Specifies the URL of the external image file in the OBS bucket.</p>
    <p id="p58228438102659"><a name="p58228438102659"></a><a name="p58228438102659"></a>This parameter is mandatory if an external image file in the OBS bucket is used to create an image. The format is <em id="i84235269710445"><a name="i84235269710445"></a><a name="i84235269710445"></a>OBS bucket name</em>:<em id="i84235269710449"><a name="i84235269710449"></a><a name="i84235269710449"></a>Image file name</em>.</p>
    <div class="notice" id="note24311794102659"><a name="note24311794102659"></a><a name="note24311794102659"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p17479562102659"><a name="p17479562102659"></a><a name="p17479562102659"></a>The storage class of the OBS bucket must be <strong id="b84235270695721"><a name="b84235270695721"></a><a name="b84235270695721"></a>Standard</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row52667843144512"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p9282872151517"><a name="p9282872151517"></a><a name="p9282872151517"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p13715176151517"><a name="p13715176151517"></a><a name="p13715176151517"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p37187452151517"><a name="p37187452151517"></a><a name="p37187452151517"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p39357309151539"><a name="p39357309151539"></a><a name="p39357309151539"></a>Specifies the minimum size of the system disk in the unit of GB.</p>
    <p id="p22166530152043"><a name="p22166530152043"></a><a name="p22166530152043"></a>This parameter is mandatory if an external image file in the OBS bucket is used to create an image. The value ranges from 1 GB to 1024 GB.</p>
    </td>
    </tr>
    <tr id="row65041573144517"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p37508960152058"><a name="p37508960152058"></a><a name="p37508960152058"></a>is_config</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p18326949152058"><a name="p18326949152058"></a><a name="p18326949152058"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p8087923152058"><a name="p8087923152058"></a><a name="p8087923152058"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p39377742152947"><a name="p39377742152947"></a><a name="p39377742152947"></a>Specifies whether automatic configuration is enabled.</p>
    <p id="p36345323152949"><a name="p36345323152949"></a><a name="p36345323152949"></a>The value can be <strong id="b2021115381211"><a name="b2021115381211"></a><a name="b2021115381211"></a>true</strong> or <strong id="b1421293822118"><a name="b1421293822118"></a><a name="b1421293822118"></a>false</strong>.</p>
    <p id="p886649318525"><a name="p886649318525"></a><a name="p886649318525"></a>If automatic configuration is required, set the value to <strong id="b842352706165031"><a name="b842352706165031"></a><a name="b842352706165031"></a>true</strong>. Otherwise, set the value to <strong id="b842352706165047"><a name="b842352706165047"></a><a name="b842352706165047"></a>false</strong> The default value is <strong id="b842352706145544"><a name="b842352706145544"></a><a name="b842352706145544"></a>false</strong>.</p>
    <p id="p51142001152058"><a name="p51142001152058"></a><a name="p51142001152058"></a>For details about automatic configuration, see <strong id="b842352706165430"><a name="b842352706165430"></a><a name="b842352706165430"></a>Creating a Linux System Disk Image from an External Image File</strong> &gt; <strong id="b842352706165449"><a name="b842352706165449"></a><a name="b842352706165449"></a>Registering an External Image File as a Private Image (Linux)</strong> in <em id="i73616130509"><a name="i73616130509"></a><a name="i73616130509"></a>Image Management Service User Guide</em>.</p>
    </td>
    </tr>
    <tr id="row396276471500"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p211045061500"><a name="p211045061500"></a><a name="p211045061500"></a>cmk_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p950318415538"><a name="p950318415538"></a><a name="p950318415538"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p210781641500"><a name="p210781641500"></a><a name="p210781641500"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p296097181500"><a name="p296097181500"></a><a name="p296097181500"></a>Specifies the master key used for encrypting an image. For its value, see the <em id="i842352697163941"><a name="i842352697163941"></a><a name="i842352697163941"></a>Key Management Service User Guide</em>.</p>
    </td>
    </tr>
    <tr id="row65425243181152"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p27909231181157"><a name="p27909231181157"></a><a name="p27909231181157"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p46055199181157"><a name="p46055199181157"></a><a name="p46055199181157"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p39483611181157"><a name="p39483611181157"></a><a name="p39483611181157"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p04478170592"><a name="p04478170592"></a><a name="p04478170592"></a>Specifies image tags. The value is left blank by default.</p>
    <p id="p14856631113148"><a name="p14856631113148"></a><a name="p14856631113148"></a>Set either <strong id="b762116418247"><a name="b762116418247"></a><a name="b762116418247"></a>tags</strong> or <strong id="b762214132417"><a name="b762214132417"></a><a name="b762214132417"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row59883440184127"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p1916128184130"><a name="p1916128184130"></a><a name="p1916128184130"></a>image_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p20988681184130"><a name="p20988681184130"></a><a name="p20988681184130"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p22361635184130"><a name="p22361635184130"></a><a name="p22361635184130"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p66462038184130"><a name="p66462038184130"></a><a name="p66462038184130"></a>Lists the image tags. This parameter is left blank by default. Use either <strong id="b167360860"><a name="b167360860"></a><a name="b167360860"></a>tags</strong> or <strong id="b1164038671"><a name="b1164038671"></a><a name="b1164038671"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row44624222161131"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p57792233161131"><a name="p57792233161131"></a><a name="p57792233161131"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p50659272161131"><a name="p50659272161131"></a><a name="p50659272161131"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p9760356161131"><a name="p9760356161131"></a><a name="p9760356161131"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p5522511816122"><a name="p5522511816122"></a><a name="p5522511816122"></a>Specifies the image type.</p>
    <p id="p52391332161131"><a name="p52391332161131"></a><a name="p52391332161131"></a>The value can be <strong id="b14189194419563"><a name="b14189194419563"></a><a name="b14189194419563"></a>ECS</strong>, <strong id="b17189244145611"><a name="b17189244145611"></a><a name="b17189244145611"></a>BMS</strong>, <strong id="b7190154415565"><a name="b7190154415565"></a><a name="b7190154415565"></a>FusionCompute</strong>, or <strong id="b1419134414562"><a name="b1419134414562"></a><a name="b1419134414562"></a>Ironic</strong>. The default value is <strong id="b3972135917553"><a name="b3972135917553"></a><a name="b3972135917553"></a>ECS</strong>.</p>
    <a name="ul861233019438"></a><a name="ul861233019438"></a><ul id="ul861233019438"><li><strong id="b1684814112568"><a name="b1684814112568"></a><a name="b1684814112568"></a>ECS</strong> and <strong id="b28496155615"><a name="b28496155615"></a><a name="b28496155615"></a>FusionCompute</strong>: indicate an ECS image.</li><li><strong id="b94781739564"><a name="b94781739564"></a><a name="b94781739564"></a>BMS</strong> and <strong id="b64793317564"><a name="b64793317564"></a><a name="b64793317564"></a>Ironic</strong>: indicate a BMS image.</li></ul>
    </td>
    </tr>
    <tr id="row22066143995"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p42527152995"><a name="p42527152995"></a><a name="p42527152995"></a>max_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p22147253995"><a name="p22147253995"></a><a name="p22147253995"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p49097046995"><a name="p49097046995"></a><a name="p49097046995"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p17437821995"><a name="p17437821995"></a><a name="p17437821995"></a>Specifies the maximum memory of the image in the unit of MB.</p>
    </td>
    </tr>
    <tr id="row4319589949"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.1 "><p id="p349886759949"><a name="p349886759949"></a><a name="p349886759949"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.1.5.1.2 "><p id="p155104169949"><a name="p155104169949"></a><a name="p155104169949"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.1.5.1.3 "><p id="p483841659949"><a name="p483841659949"></a><a name="p483841659949"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.55%" headers="mcps1.1.5.1.4 "><p id="p268033079949"><a name="p268033079949"></a><a name="p268033079949"></a>Specifies the minimum memory required by the image in the unit of MB. The default value is <strong id="b420568273"><a name="b420568273"></a><a name="b420568273"></a>0</strong>, indicating that the memory is not restricted.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example requests
    -   Request for creating a system disk image with parameter  **tags**  using an ECS

        ```
        POST https://{Endpoint}/v2/cloudimages/action
        ```

        ```
        {
               "name": "ims_test",
               "description": "Create a system disk image from an ECS",
               "instance_id": "877a2cda-ba63-4e1e-b95f-e67e48b6129a",
               "tags": [
                     "aaa.111",
                     "bbb.333",
                     "ccc.444"
                 ]
        }
        ```

    -   Request for creating a data disk image with parameter  **tags**  using the data disk of an ECS

        ```
        POST https://{Endpoint}/v2/cloudimages/action
        ```

        ```
        {
               "data_images": [{"name": "ims_data_image_test",
               "description": "Create a data disk image from the data disk of an ECS",
               "volume_id": "c5dfbd0c-bf0a-4798-a453-61dc6b54aa30",
               "tags": [
                          "aaa.111",
                          "bbb.333",
                          "ccc.444"
                      ]
               }]
        }
        ```

    -   Request for creating an image using an external image file uploaded to the OBS bucket

        ```
        POST https://{Endpoint}/v2/cloudimages/action
        ```

        ```
        {
              "name": "ims_test_file",
          "description": "Create an image from a file in the OBS bucket",
              "image_url": "ims-image:centos70.qcow2",
              "os_version": "CentOS 7.0 64bit",
              "is_config_init": true,
              "min_disk": 40,
              "is_config": true,
              "tags": [  
                    "aaa.111",  
                    "bbb.333",  
                    "ccc.444"  
              ]     
        }
        ```

    -   Request for creating a system disk image with parameter  **image\_tags**  using an ECS

        ```
        POST https://{Endpoint}/v2/cloudimages/action
        ```

        ```
        {
               "name": "ims_test",
               "description": "Create a system disk image from an ECS",
               "instance_id": "877a2cda-ba63-4e1e-b95f-e67e48b6129a",
               "image_tags": [{"key":"key2","value":"value2"},{"key":"key1","value":"value1"}]
        } 
        ```

    -   Request for creating a data disk image with parameter  **image\_tags**  using the data disk of an ECS

        ```
        POST /v2/cloudimages/action
        ```

        ```
        {
               "data_images": [{"name": "ims_data_image_test",
               "description": "Create a data disk image from the data disk of an ECS",
               "volume_id": "c5dfbd0c-bf0a-4798-a453-61dc6b54aa30",
               "image_tags": [{"key":"key2","value":"value2"},{"key":"key1","value":"value1"}]
               }]
        }
        ```

    -   Request for creating an image using an external image file uploaded to the OBS bucket

        ```
        POST https://{Endpoint}/v2/cloudimages/action
        ```

        ```
        {
               "name": "ims_test_file",
               "description": "Create an image from a file in the OBS bucket",
               "image_url": "ims-image:centos70.qcow2",
               "os_version": "CentOS 7.0 64bit",
               "is_config_init": true,
               "min_disk": 40,
               
               "image_tags": [{"key":"key2","value":"value2"},{"key":"key1","value":"value1"}]    
        }
        ```



## Response<a name="section56649665"></a>

-   Response parameters

    <a name="table1337332211159"></a>
    <table><thead align="left"><tr id="row1133156911159"><th class="cellrowborder" valign="top" width="23.84%" id="mcps1.1.4.1.1"><p id="p4544189211159"><a name="p4544189211159"></a><a name="p4544189211159"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.97%" id="mcps1.1.4.1.2"><p id="p556206921988"><a name="p556206921988"></a><a name="p556206921988"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.19%" id="mcps1.1.4.1.3"><p id="p5691464411159"><a name="p5691464411159"></a><a name="p5691464411159"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4668343211159"><td class="cellrowborder" valign="top" width="23.84%" headers="mcps1.1.4.1.1 "><p id="p2326164111159"><a name="p2326164111159"></a><a name="p2326164111159"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.1.4.1.2 "><p id="p89821791988"><a name="p89821791988"></a><a name="p89821791988"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.19%" headers="mcps1.1.4.1.3 "><p id="p514473411159"><a name="p514473411159"></a><a name="p514473411159"></a>Specifies the asynchronous job ID.</p>
    <p id="p19968122117312"><a name="p19968122117312"></a><a name="p19968122117312"></a>For details, see <a href="asynchronous-job-query.md">Asynchronous Job Query</a>.</p>
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
        "job_id": "8a12fc664fb4daa3014fb4e581380005"
    }
    ```


## Returned Values<a name="section40084941"></a>

-   Normal

    200

-   Abnormal

    <a name="table1069408417333"></a>
    <table><thead align="left"><tr id="row4772021317333"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p4013206717333"><a name="p4013206717333"></a><a name="p4013206717333"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p2947196917333"><a name="p2947196917333"></a><a name="p2947196917333"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3841925517333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p2495195017333"><a name="p2495195017333"></a><a name="p2495195017333"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p784206117333"><a name="p784206117333"></a><a name="p784206117333"></a>Request error. For details about the returned error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row3122722917333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4637763817333"><a name="p4637763817333"></a><a name="p4637763817333"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p6560116717333"><a name="p6560116717333"></a><a name="p6560116717333"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row5353959117333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4173958717333"><a name="p4173958717333"></a><a name="p4173958717333"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2546341217333"><a name="p2546341217333"></a><a name="p2546341217333"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row5197513192250"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p21898657192252"><a name="p21898657192252"></a><a name="p21898657192252"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p28960832192252"><a name="p28960832192252"></a><a name="p28960832192252"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row2784412417333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4078159117333"><a name="p4078159117333"></a><a name="p4078159117333"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1497458717333"><a name="p1497458717333"></a><a name="p1497458717333"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row55355517333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4483799017333"><a name="p4483799017333"></a><a name="p4483799017333"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p799858217333"><a name="p799858217333"></a><a name="p799858217333"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


