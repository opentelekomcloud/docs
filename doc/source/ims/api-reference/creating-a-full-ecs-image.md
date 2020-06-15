# Creating a Full-ECS Image<a name="EN-US_TOPIC_0092380109"></a>

## Function<a name="section29995926"></a>

This API is used to create a full-ECS image from an ECS or a Cloud Server Backup Service \(CSBS\) backup. The API is an asynchronous one. If it is successfully called, the cloud system receives the request to create a full-ECS image. However, you need to use the asynchronous job query API to query the image creation status. For details, see  [Asynchronous Job Query](asynchronous-job-query.md).

## Constraints \(Creating a Full-ECS Image Using an ECS\)<a name="section192601957181516"></a>

-   When creating a full-ECS image from an ECS, ensure that the ECS has been properly configured. Otherwise, creating ECSs using the full-ECS image may fail.
-   Only a running or stopped ECS can be used to create a full-ECS image.
-   A Windows ECS used to create a full-ECS image cannot have a spanned volume. Otherwise, data may be lost when the full-ECS image is used to create ECSs.
-   A Linux ECS used to create a full-ECS image cannot have a disk group or logical disk that contains multiple physical disks. Otherwise, data may be lost when the full-ECS image is used to create ECSs.
-   If a full-ECS image is available in an AZ, it can be used to create ECSs only in this AZ.
-   If a full-ECS image is available in a region, the full-ECS image can be used to create ECSs only in this region.
-   The system disk cannot be detached during full-ECS image creation.
-   A full-ECS image cannot be shared with other tenants.
-   A full-ECS image cannot be published as a Marketplace image.
-   A full-ECS image cannot be exported or replicated.
-   When creating a full-ECS image using a Windows ECS, you need to change the SAN policy of the ECS to OnlineAll. Otherwise, EVS disks attached to the ECSs created using the image may be offline.

    Windows has three types of SAN policies:  **OnlineAll**,  **OfflineShared**, and  **OfflineInternal**.

    **Table  1** SAN policies  in Windows

    <a name="en-us_topic_0116125142_en-us_topic_0089178278_table615679113016"></a>
    <table><thead align="left"><tr id="en-us_topic_0116125142_en-us_topic_0089178278_row1115619943013"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.3.1.1"><p id="en-us_topic_0116125142_en-us_topic_0089178278_p6156139123011"><a name="en-us_topic_0116125142_en-us_topic_0089178278_p6156139123011"></a><a name="en-us_topic_0116125142_en-us_topic_0089178278_p6156139123011"></a><strong id="en-us_topic_0116125142_b842352706201211"><a name="en-us_topic_0116125142_b842352706201211"></a><a name="en-us_topic_0116125142_b842352706201211"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="85%" id="mcps1.2.3.1.2"><p id="en-us_topic_0116125142_en-us_topic_0089178278_p4156149133011"><a name="en-us_topic_0116125142_en-us_topic_0089178278_p4156149133011"></a><a name="en-us_topic_0116125142_en-us_topic_0089178278_p4156149133011"></a><strong id="en-us_topic_0116125142_b842352706105039"><a name="en-us_topic_0116125142_b842352706105039"></a><a name="en-us_topic_0116125142_b842352706105039"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0116125142_en-us_topic_0089178278_row151561899304"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0116125142_en-us_topic_0089178278_p111566915309"><a name="en-us_topic_0116125142_en-us_topic_0089178278_p111566915309"></a><a name="en-us_topic_0116125142_en-us_topic_0089178278_p111566915309"></a>OnlineAll</p>
    </td>
    <td class="cellrowborder" valign="top" width="85%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0116125142_en-us_topic_0089178278_p191569916308"><a name="en-us_topic_0116125142_en-us_topic_0089178278_p191569916308"></a><a name="en-us_topic_0116125142_en-us_topic_0089178278_p191569916308"></a>Indicates that all newly detected disks are automatically brought online.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0116125142_en-us_topic_0089178278_row16156149183018"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0116125142_en-us_topic_0089178278_p141568914305"><a name="en-us_topic_0116125142_en-us_topic_0089178278_p141568914305"></a><a name="en-us_topic_0116125142_en-us_topic_0089178278_p141568914305"></a>OfflineShared</p>
    </td>
    <td class="cellrowborder" valign="top" width="85%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0116125142_en-us_topic_0089178278_p2015609163015"><a name="en-us_topic_0116125142_en-us_topic_0089178278_p2015609163015"></a><a name="en-us_topic_0116125142_en-us_topic_0089178278_p2015609163015"></a>Indicates that all disks on sharable buses, such as iSCSI and FC, are left offline by default, while disks on non-sharable buses are kept online.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0116125142_en-us_topic_0089178278_row41567943014"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0116125142_en-us_topic_0089178278_p131561497304"><a name="en-us_topic_0116125142_en-us_topic_0089178278_p131561497304"></a><a name="en-us_topic_0116125142_en-us_topic_0089178278_p131561497304"></a>OfflineInternal</p>
    </td>
    <td class="cellrowborder" valign="top" width="85%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0116125142_en-us_topic_0089178278_p13156149173012"><a name="en-us_topic_0116125142_en-us_topic_0089178278_p13156149173012"></a><a name="en-us_topic_0116125142_en-us_topic_0089178278_p13156149173012"></a>Indicates that all newly detected disks are left offline as default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    1.  Execute  **cmd.exe**  and run the following command to query the current SAN policy of the ECS using DiskPart:

        **diskpart**

    2.  Run the following command to view the SAN policy of the ECS:

        **san**

        -   If the SAN policy is  **OnlineAll**, run the  **exit**  command to exit DiskPart.

        -   If the SAN policy is not  **OnlineAll**, go to  [3](#en-us_topic_0116125142_en-us_topic_0089178278_li15110228143312).

    3.  <a name="en-us_topic_0116125142_en-us_topic_0089178278_li15110228143312"></a>Run the following command to change the SAN policy of the ECS to OnlineAll:

        **san policy=onlineall**



## Constraints \(Creating a Full-ECS Image Using a CSBS Backup\)<a name="section2912711202014"></a>

-   When creating a full-ECS image from a CSBS backup, ensure that the ECS corresponding to the CSBS backup has been properly configured. Otherwise, creating ECSs using the full-ECS image may fail.
-   A CSBS backup used to create a full-ECS image cannot have shared disks.
-   Only an available CSBS backup can be used to create a full-ECS image. A CSBS backup can be used to create only one full-ECS image.
-   A full-ECS image cannot be shared with other tenants.
-   A full-ECS image cannot be published as a Marketplace image.
-   A full-ECS image cannot be exported or replicated.

## URI<a name="section1527883"></a>

POST /v1/cloudimages/wholeimages/action

## Request<a name="section13750947"></a>

-   Parameters for creating a full-ECS image using an ECS

    <a name="table62551043151553"></a>
    <table><thead align="left"><tr id="row63356413151553"><th class="cellrowborder" valign="top" width="18.8%" id="mcps1.1.5.1.1"><p id="p41292683151745"><a name="p41292683151745"></a><a name="p41292683151745"></a><strong id="b24725868162658"><a name="b24725868162658"></a><a name="b24725868162658"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.2"><p id="p51323166151745"><a name="p51323166151745"></a><a name="p51323166151745"></a><strong id="b84235270616551"><a name="b84235270616551"></a><a name="b84235270616551"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.1.5.1.3"><p id="p36943663151745"><a name="p36943663151745"></a><a name="p36943663151745"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.370000000000005%" id="mcps1.1.5.1.4"><p id="p16401653151745"><a name="p16401653151745"></a><a name="p16401653151745"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58293752151553"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p24173439151553"><a name="p24173439151553"></a><a name="p24173439151553"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.2 "><p id="p11891563151553"><a name="p11891563151553"></a><a name="p11891563151553"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.3 "><p id="p23692580151553"><a name="p23692580151553"></a><a name="p23692580151553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p40050833151553"><a name="p40050833151553"></a><a name="p40050833151553"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row57744127151553"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p46762671151553"><a name="p46762671151553"></a><a name="p46762671151553"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.2 "><p id="p29679979151553"><a name="p29679979151553"></a><a name="p29679979151553"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.3 "><p id="p55268124151553"><a name="p55268124151553"></a><a name="p55268124151553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p47533098151553"><a name="p47533098151553"></a><a name="p47533098151553"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row44108176111744"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p17224683111759"><a name="p17224683111759"></a><a name="p17224683111759"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.2 "><p id="p53022050111759"><a name="p53022050111759"></a><a name="p53022050111759"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.3 "><p id="p66927678111759"><a name="p66927678111759"></a><a name="p66927678111759"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p52432871111759"><a name="p52432871111759"></a><a name="p52432871111759"></a>Lists the image tags. The value is left blank by default.</p>
    <p id="p20992085173243"><a name="p20992085173243"></a><a name="p20992085173243"></a>Use either <strong id="b84235270693042"><a name="b84235270693042"></a><a name="b84235270693042"></a>tags</strong> or <strong id="b84235270693044"><a name="b84235270693044"></a><a name="b84235270693044"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row34501036184256"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p21354848113521"><a name="p21354848113521"></a><a name="p21354848113521"></a>image_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.2 "><p id="p29922489113521"><a name="p29922489113521"></a><a name="p29922489113521"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.3 "><p id="p56528150113521"><a name="p56528150113521"></a><a name="p56528150113521"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p58098807113521"><a name="p58098807113521"></a><a name="p58098807113521"></a>Lists the image tags. The value is left blank by default.</p>
    <p id="p19190125113278"><a name="p19190125113278"></a><a name="p19190125113278"></a>Use either <strong id="b614879775"><a name="b614879775"></a><a name="b614879775"></a>tags</strong> or <strong id="b151069106"><a name="b151069106"></a><a name="b151069106"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row64339672194146"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p46228041194154"><a name="p46228041194154"></a><a name="p46228041194154"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.2 "><p id="p53483863194154"><a name="p53483863194154"></a><a name="p53483863194154"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.3 "><p id="p37225621194154"><a name="p37225621194154"></a><a name="p37225621194154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p62485291194154"><a name="p62485291194154"></a><a name="p62485291194154"></a>Specifies the <span id="text18466173712420"><a name="text18466173712420"></a><a name="text18466173712420"></a></span><span id="text1646653782418"><a name="text1646653782418"></a><a name="text1646653782418"></a>ECS</span> ID. This parameter is required when an <span id="text1175534192418"><a name="text1175534192418"></a><a name="text1175534192418"></a></span><span id="text17558419248"><a name="text17558419248"></a><a name="text17558419248"></a>ECS</span> is used to create a full-ECS image.</p>
    <p id="p188578234320"><a name="p188578234320"></a><a name="p188578234320"></a>To obtain the <span id="text7967637181111"><a name="text7967637181111"></a><a name="text7967637181111"></a></span><span id="text496753717119"><a name="text496753717119"></a><a name="text496753717119"></a>ECS</span> ID, perform the following operations:</p>
    <a name="ol388062213448"></a><a name="ol388062213448"></a><ol id="ol388062213448"><li>Log in to management console.</li><li>Under <strong id="b2076333910118"><a name="b2076333910118"></a><a name="b2076333910118"></a>Computing</strong>, click <strong id="b117778398119"><a name="b117778398119"></a><a name="b117778398119"></a>Elastic Cloud Server</strong>.</li><li>In the <span id="text1524519316253"><a name="text1524519316253"></a><a name="text1524519316253"></a></span><span id="text1624511362513"><a name="text1624511362513"></a><a name="text1624511362513"></a>ECS</span> list, click the name of the <span id="text19262135415117"><a name="text19262135415117"></a><a name="text19262135415117"></a></span><span id="text1126255420116"><a name="text1126255420116"></a><a name="text1126255420116"></a>ECS</span> and view its ID.</li></ol>
    </td>
    </tr>
    <tr id="row1703703091128"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p3782220891128"><a name="p3782220891128"></a><a name="p3782220891128"></a>max_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.2 "><p id="p4369999891128"><a name="p4369999891128"></a><a name="p4369999891128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.3 "><p id="p5003895391128"><a name="p5003895391128"></a><a name="p5003895391128"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p2662336891128"><a name="p2662336891128"></a><a name="p2662336891128"></a>Specifies the maximum memory of the image in the unit of MB. This parameter is not configured by default.</p>
    </td>
    </tr>
    <tr id="row246785619125"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.1.5.1.1 "><p id="p528064539125"><a name="p528064539125"></a><a name="p528064539125"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.2 "><p id="p494643019125"><a name="p494643019125"></a><a name="p494643019125"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.3 "><p id="p471854589125"><a name="p471854589125"></a><a name="p471854589125"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p639257399125"><a name="p639257399125"></a><a name="p639257399125"></a>Specifies the minimum memory of the image in the unit of MB. The default value is <strong id="b84235270617155"><a name="b84235270617155"></a><a name="b84235270617155"></a>0</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameters in the request body when a CSBS backup is used to create a full-ECS image

    <a name="table6920488194359"></a>
    <table><thead align="left"><tr id="row39939980194359"><th class="cellrowborder" valign="top" width="17.86%" id="mcps1.1.5.1.1"><p id="p13912942194359"><a name="p13912942194359"></a><a name="p13912942194359"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.91%" id="mcps1.1.5.1.2"><p id="p53206504194359"><a name="p53206504194359"></a><a name="p53206504194359"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.86%" id="mcps1.1.5.1.3"><p id="p14759587194359"><a name="p14759587194359"></a><a name="p14759587194359"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.370000000000005%" id="mcps1.1.5.1.4"><p id="p54675911194359"><a name="p54675911194359"></a><a name="p54675911194359"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66672634194359"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.1 "><p id="p31774311194359"><a name="p31774311194359"></a><a name="p31774311194359"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p23582388194359"><a name="p23582388194359"></a><a name="p23582388194359"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p31125257194359"><a name="p31125257194359"></a><a name="p31125257194359"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p38117903194359"><a name="p38117903194359"></a><a name="p38117903194359"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row58911100194359"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.1 "><p id="p7069805194359"><a name="p7069805194359"></a><a name="p7069805194359"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p35783334194359"><a name="p35783334194359"></a><a name="p35783334194359"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p12768976194359"><a name="p12768976194359"></a><a name="p12768976194359"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p27654163194359"><a name="p27654163194359"></a><a name="p27654163194359"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row47560877194359"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.1 "><p id="p27225799194359"><a name="p27225799194359"></a><a name="p27225799194359"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p57806093194359"><a name="p57806093194359"></a><a name="p57806093194359"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p51781993194359"><a name="p51781993194359"></a><a name="p51781993194359"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p187265217338"><a name="p187265217338"></a><a name="p187265217338"></a>Lists the image tags. The value is left blank by default.</p>
    <p id="p672662143316"><a name="p672662143316"></a><a name="p672662143316"></a>Use either <strong id="b580364321"><a name="b580364321"></a><a name="b580364321"></a>tags</strong> or <strong id="b1027093972"><a name="b1027093972"></a><a name="b1027093972"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row14362188103319"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.1 "><p id="p15525181013316"><a name="p15525181013316"></a><a name="p15525181013316"></a>image_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p13525141093317"><a name="p13525141093317"></a><a name="p13525141093317"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p15525101013313"><a name="p15525101013313"></a><a name="p15525101013313"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p1552671016330"><a name="p1552671016330"></a><a name="p1552671016330"></a>Lists the image tags. The value is left blank by default.</p>
    <p id="p1252611043314"><a name="p1252611043314"></a><a name="p1252611043314"></a>Use either <strong id="b521025933317"><a name="b521025933317"></a><a name="b521025933317"></a>tags</strong> or <strong id="b7211559183313"><a name="b7211559183313"></a><a name="b7211559183313"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row38983230194359"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.1 "><p id="p46832185194431"><a name="p46832185194431"></a><a name="p46832185194431"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p35310613194431"><a name="p35310613194431"></a><a name="p35310613194431"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p41587430194431"><a name="p41587430194431"></a><a name="p41587430194431"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p185905910502"><a name="p185905910502"></a><a name="p185905910502"></a>Specifies the CSBS backup ID.</p>
    <div class="p" id="p96251131795"><a name="p96251131795"></a><a name="p96251131795"></a>To obtain the CSBS backup ID, perform the following operations:<a name="ol2385105535715"></a><a name="ol2385105535715"></a><ol id="ol2385105535715"><li>Log in to the management console.</li><li>Under <strong id="b05263113304"><a name="b05263113304"></a><a name="b05263113304"></a>Storage</strong>, click <strong id="b19997121713300"><a name="b19997121713300"></a><a name="b19997121713300"></a>Cloud Server Backup Service</strong>.</li><li>In the backup list, expand details of the backup to obtain its ID.</li></ol>
    </div>
    </td>
    </tr>
    <tr id="row98737391719"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.1 "><p id="p1286840291719"><a name="p1286840291719"></a><a name="p1286840291719"></a>max_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p3570762791719"><a name="p3570762791719"></a><a name="p3570762791719"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p663667391719"><a name="p663667391719"></a><a name="p663667391719"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p2403410391919"><a name="p2403410391919"></a><a name="p2403410391919"></a>Specifies the maximum memory of the image in the unit of MB. This parameter is not configured by default.</p>
    </td>
    </tr>
    <tr id="row5694598992137"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.1 "><p id="p4922241692137"><a name="p4922241692137"></a><a name="p4922241692137"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p2759277292137"><a name="p2759277292137"></a><a name="p2759277292137"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="p2042202392137"><a name="p2042202392137"></a><a name="p2042202392137"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.370000000000005%" headers="mcps1.1.5.1.4 "><p id="p4357120492137"><a name="p4357120492137"></a><a name="p4357120492137"></a>Specifies the minimum memory of the image in the unit of MB. The default value is <strong id="b434776240"><a name="b434776240"></a><a name="b434776240"></a>0</strong>, indicating that the memory is not restricted.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example requests
    -   Creating a full-ECS image from an ECS

        ```
        POST https://{Endpoint}/v1/cloudimages/wholeimages/action
        ```

        If parameter  **tags**  is used:

        ```
        {
               "name": "instance_whole_image",
               "description": "creating an image from an ECS",
               "instance_id": "877a2cda-ba63-4e1e-b95f-e67e48b6129a",
               "tags": [
                   "aaa.111",
                   "bbb.333",
                   "ccc.444"
               ]
        }
        ```

        If parameter  **image\_tags**  is used:

        ```
        {
               "name": "instance_whole_image",
               "description": "creating an image from an ECS",
               "instance_id": "877a2cda-ba63-4e1e-b95f-e67e48b6129a",
               "image_tags": [{"key":"key2","value":"value2"},{"key":"key1","value":"value1"}]
        } 
        ```

    -   Creating a full-ECS image from a CSBS backup.

        ```
        POST https://{Endpoint}/v1/cloudimages/wholeimages/action
        ```

        If parameter  **tags**  is used:

        ```
        {
             "name": "backup_whole_image",
             "description": "Creating a full-ECS image using a CSBS backup",
             "backup_id": "9b27efab-4a17-4c06-bfa2-3e0cf021d3c3",
             "tags": [
                   "aaa.111",
                   "bbb.333",
                   "ccc.444"
              ]
        }
        ```

        If parameter  **image\_tags**  is used:

        ```
        {
             "name": "backup_whole_image",
             "description": "Creating a full-ECS image using a CSBS backup",
             "backup_id": "9b27efab-4a17-4c06-bfa2-3e0cf021d3c3",
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
        "job_id": "4010a32b5f909853015f90aaa24b0015"
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


