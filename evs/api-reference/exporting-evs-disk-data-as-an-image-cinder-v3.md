# Exporting EVS Disk Data as an Image<a name="evs_04_3051"></a>

## Function<a name="section54187005111229"></a>

This API is used to export the system disk data or data disk data as an IMS image. The exported image will be displayed in the IMS private image list and can be viewed and used.

## Constraints<a name="section44817321519"></a>

If the target disk is in the  **in-use**  state, stop the server where the disk has been attached before calling this API. If the target disk is a shared disk, stop all servers where the shared disk has been attached before calling this API.

## URI<a name="section44750704111229"></a>

-   URI format

    POST /v3/\{project\_id\}/volumes/\{volume\_id\}/action

-   Parameter description

    <a name="table16835088111229"></a>
    <table><thead align="left"><tr id="row36762725111229"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.1.4.1.1"><p id="p24990771111229"><a name="p24990771111229"></a><a name="p24990771111229"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.1.4.1.2"><p id="p10986545111229"><a name="p10986545111229"></a><a name="p10986545111229"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.1.4.1.3"><p id="p17494919111229"><a name="p17494919111229"></a><a name="p17494919111229"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7802334111229"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="p28009309111229"><a name="p28009309111229"></a><a name="p28009309111229"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.2 "><p id="p54161581111229"><a name="p54161581111229"></a><a name="p54161581111229"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.4.1.3 "><p id="p25011958111229"><a name="p25011958111229"></a><a name="p25011958111229"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row22284688111229"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="p60229298111229"><a name="p60229298111229"></a><a name="p60229298111229"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.2 "><p id="p46734956111229"><a name="p46734956111229"></a><a name="p46734956111229"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.4.1.3 "><p id="p27435111111229"><a name="p27435111111229"></a><a name="p27435111111229"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section2478043111340"></a>

-   Parameter description

    <a name="evs_04_2086_table28675530111340"></a>
    <table><thead align="left"><tr id="evs_04_2086_row30444615111340"><th class="cellrowborder" valign="top" width="23.232323232323232%" id="mcps1.1.5.1.1"><p id="evs_04_2086_p50094757111340"><a name="evs_04_2086_p50094757111340"></a><a name="evs_04_2086_p50094757111340"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.35143514351435%" id="mcps1.1.5.1.2"><p id="evs_04_2086_p31143556111340"><a name="evs_04_2086_p31143556111340"></a><a name="evs_04_2086_p31143556111340"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.96169616961696%" id="mcps1.1.5.1.3"><p id="evs_04_2086_p39600140111340"><a name="evs_04_2086_p39600140111340"></a><a name="evs_04_2086_p39600140111340"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454545%" id="mcps1.1.5.1.4"><p id="evs_04_2086_p53494756111340"><a name="evs_04_2086_p53494756111340"></a><a name="evs_04_2086_p53494756111340"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2086_row38107956111340"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.5.1.1 "><p id="evs_04_2086_p66845605111340"><a name="evs_04_2086_p66845605111340"></a><a name="evs_04_2086_p66845605111340"></a>os-volume_upload_image</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.35143514351435%" headers="mcps1.1.5.1.2 "><p id="evs_04_2086_p45784926111340"><a name="evs_04_2086_p45784926111340"></a><a name="evs_04_2086_p45784926111340"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.96169616961696%" headers="mcps1.1.5.1.3 "><p id="evs_04_2086_p17591560111340"><a name="evs_04_2086_p17591560111340"></a><a name="evs_04_2086_p17591560111340"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.1.5.1.4 "><p id="evs_04_2086_p15630283111340"><a name="evs_04_2086_p15630283111340"></a><a name="evs_04_2086_p15630283111340"></a>Specifies the operation to export the disk data as an image. For details, see <a href="#evs_04_2086_li49734540111454">Parameters in the os-volume_upload_image field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2086_li49734540111454"></a>Parameters in the  **os-volume\_upload\_image**  field

    <a name="evs_04_2086_table1029161111454"></a>
    <table><thead align="left"><tr id="evs_04_2086_row17873550111454"><th class="cellrowborder" valign="top" width="23.232323232323232%" id="mcps1.1.5.1.1"><p id="evs_04_2086_p61357386111454"><a name="evs_04_2086_p61357386111454"></a><a name="evs_04_2086_p61357386111454"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.541454145414543%" id="mcps1.1.5.1.2"><p id="evs_04_2086_p3892401111454"><a name="evs_04_2086_p3892401111454"></a><a name="evs_04_2086_p3892401111454"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.77167716771677%" id="mcps1.1.5.1.3"><p id="evs_04_2086_p46849027111454"><a name="evs_04_2086_p46849027111454"></a><a name="evs_04_2086_p46849027111454"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454545%" id="mcps1.1.5.1.4"><p id="evs_04_2086_p36674858111454"><a name="evs_04_2086_p36674858111454"></a><a name="evs_04_2086_p36674858111454"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2086_row34643012111454"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.5.1.1 "><p id="evs_04_2086_p38471446111454"><a name="evs_04_2086_p38471446111454"></a><a name="evs_04_2086_p38471446111454"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.541454145414543%" headers="mcps1.1.5.1.2 "><p id="evs_04_2086_p29179435111454"><a name="evs_04_2086_p29179435111454"></a><a name="evs_04_2086_p29179435111454"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.77167716771677%" headers="mcps1.1.5.1.3 "><p id="evs_04_2086_p14724020111454"><a name="evs_04_2086_p14724020111454"></a><a name="evs_04_2086_p14724020111454"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.1.5.1.4 "><p id="evs_04_2086_p846816504210"><a name="evs_04_2086_p846816504210"></a><a name="evs_04_2086_p846816504210"></a>Specifies the format of the exported image.</p>
    <p id="evs_04_2086_p51794970111454"><a name="evs_04_2086_p51794970111454"></a><a name="evs_04_2086_p51794970111454"></a>The value can be <strong id="evs_04_2086_b842352706173625"><a name="evs_04_2086_b842352706173625"></a><a name="evs_04_2086_b842352706173625"></a>vhd</strong>, <strong id="evs_04_2086_b842352706173628"><a name="evs_04_2086_b842352706173628"></a><a name="evs_04_2086_b842352706173628"></a>zvhd</strong>, <strong id="evs_04_2086_b13481118111020"><a name="evs_04_2086_b13481118111020"></a><a name="evs_04_2086_b13481118111020"></a>zvhd2</strong>, <strong id="evs_04_2086_b842352706173630"><a name="evs_04_2086_b842352706173630"></a><a name="evs_04_2086_b842352706173630"></a>raw</strong>, or <strong id="evs_04_2086_b842352706173635"><a name="evs_04_2086_b842352706173635"></a><a name="evs_04_2086_b842352706173635"></a>qcow2</strong>. The default value is <strong id="evs_04_2086_b842352706165234"><a name="evs_04_2086_b842352706165234"></a><a name="evs_04_2086_b842352706165234"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row65355785111454"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.5.1.1 "><p id="evs_04_2086_p43351654111454"><a name="evs_04_2086_p43351654111454"></a><a name="evs_04_2086_p43351654111454"></a>image_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.541454145414543%" headers="mcps1.1.5.1.2 "><p id="evs_04_2086_p21823090111454"><a name="evs_04_2086_p21823090111454"></a><a name="evs_04_2086_p21823090111454"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.77167716771677%" headers="mcps1.1.5.1.3 "><p id="evs_04_2086_p22839862111454"><a name="evs_04_2086_p22839862111454"></a><a name="evs_04_2086_p22839862111454"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.1.5.1.4 "><div class="p" id="evs_04_2086_p38089563111454"><a name="evs_04_2086_p38089563111454"></a><a name="evs_04_2086_p38089563111454"></a>Specifies the name of the exported image.<a name="evs_04_2086_ul728185834617"></a><a name="evs_04_2086_ul728185834617"></a><ul id="evs_04_2086_ul728185834617"><li>The name cannot start or end with space.</li><li>The name contains 1 to 128 characters.</li><li>The name contains the following characters: uppercase letters, lowercase letters, Chinese characters, digits, and special characters, such as hyphens (-), periods (.), underscores (_), and spaces.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_2086_row28028525111454"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.5.1.1 "><p id="evs_04_2086_p51331154111454"><a name="evs_04_2086_p51331154111454"></a><a name="evs_04_2086_p51331154111454"></a>force</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.541454145414543%" headers="mcps1.1.5.1.2 "><p id="evs_04_2086_p64182815111454"><a name="evs_04_2086_p64182815111454"></a><a name="evs_04_2086_p64182815111454"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.77167716771677%" headers="mcps1.1.5.1.3 "><p id="evs_04_2086_p31425545111454"><a name="evs_04_2086_p31425545111454"></a><a name="evs_04_2086_p31425545111454"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.1.5.1.4 "><p id="evs_04_2086_p62441207111454"><a name="evs_04_2086_p62441207111454"></a><a name="evs_04_2086_p62441207111454"></a>Specifies whether to forcibly export the image. The default value is <strong id="evs_04_2086_b842352706201136"><a name="evs_04_2086_b842352706201136"></a><a name="evs_04_2086_b842352706201136"></a>false</strong>.</p>
    <a name="evs_04_2086_ul24573010111454"></a><a name="evs_04_2086_ul24573010111454"></a><ul id="evs_04_2086_ul24573010111454"><li>If <strong id="evs_04_2086_b842352706201151"><a name="evs_04_2086_b842352706201151"></a><a name="evs_04_2086_b842352706201151"></a>force</strong> is set to <strong id="evs_04_2086_b842352706201154"><a name="evs_04_2086_b842352706201154"></a><a name="evs_04_2086_b842352706201154"></a>false</strong> and the disk is in the <strong id="evs_04_2086_b84235270620122"><a name="evs_04_2086_b84235270620122"></a><a name="evs_04_2086_b84235270620122"></a>in-use</strong> state, the image cannot be forcibly exported.</li></ul>
    <a name="evs_04_2086_ul44256769111454"></a><a name="evs_04_2086_ul44256769111454"></a><ul id="evs_04_2086_ul44256769111454"><li>If <strong id="evs_04_2086_b770259509201258"><a name="evs_04_2086_b770259509201258"></a><a name="evs_04_2086_b770259509201258"></a>force</strong> is set to <strong id="evs_04_2086_b174167542715230"><a name="evs_04_2086_b174167542715230"></a><a name="evs_04_2086_b174167542715230"></a>true</strong> and the disk is in the <strong id="evs_04_2086_b842352706181628"><a name="evs_04_2086_b842352706181628"></a><a name="evs_04_2086_b842352706181628"></a>in-use</strong> state, the image can be forcibly exported.</li></ul>
    </td>
    </tr>
    <tr id="evs_04_2086_row43451869111454"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.5.1.1 "><p id="evs_04_2086_p50930133111454"><a name="evs_04_2086_p50930133111454"></a><a name="evs_04_2086_p50930133111454"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.541454145414543%" headers="mcps1.1.5.1.2 "><p id="evs_04_2086_p31700070111454"><a name="evs_04_2086_p31700070111454"></a><a name="evs_04_2086_p31700070111454"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.77167716771677%" headers="mcps1.1.5.1.3 "><p id="evs_04_2086_p17568872111454"><a name="evs_04_2086_p17568872111454"></a><a name="evs_04_2086_p17568872111454"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.1.5.1.4 "><p id="evs_04_2086_p18456652114510"><a name="evs_04_2086_p18456652114510"></a><a name="evs_04_2086_p18456652114510"></a>Specifies the container type of the exported image.</p>
    <p id="evs_04_2086_p13792514111454"><a name="evs_04_2086_p13792514111454"></a><a name="evs_04_2086_p13792514111454"></a>The value can be <strong id="evs_04_2086_b175891242151414"><a name="evs_04_2086_b175891242151414"></a><a name="evs_04_2086_b175891242151414"></a>ami</strong>, <strong id="evs_04_2086_b826474991410"><a name="evs_04_2086_b826474991410"></a><a name="evs_04_2086_b826474991410"></a>ari</strong>, <strong id="evs_04_2086_b9987253181416"><a name="evs_04_2086_b9987253181416"></a><a name="evs_04_2086_b9987253181416"></a>aki</strong>, <strong id="evs_04_2086_b27561756131410"><a name="evs_04_2086_b27561756131410"></a><a name="evs_04_2086_b27561756131410"></a>ovf</strong>, or <strong id="evs_04_2086_b1692065815142"><a name="evs_04_2086_b1692065815142"></a><a name="evs_04_2086_b1692065815142"></a>bare</strong>. The default value is <strong id="evs_04_2086_b155421405154"><a name="evs_04_2086_b155421405154"></a><a name="evs_04_2086_b155421405154"></a>bare</strong>.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row148648415911"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.1.5.1.1 "><p id="evs_04_2086_p846811317910"><a name="evs_04_2086_p846811317910"></a><a name="evs_04_2086_p846811317910"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.541454145414543%" headers="mcps1.1.5.1.2 "><p id="evs_04_2086_p946810131899"><a name="evs_04_2086_p946810131899"></a><a name="evs_04_2086_p946810131899"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.77167716771677%" headers="mcps1.1.5.1.3 "><p id="evs_04_2086_p12469713496"><a name="evs_04_2086_p12469713496"></a><a name="evs_04_2086_p12469713496"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.1.5.1.4 "><p id="evs_04_2086_p246912131294"><a name="evs_04_2086_p246912131294"></a><a name="evs_04_2086_p246912131294"></a>Specifies the OS type of the exported image. Currently, only <strong id="evs_04_2086_b842352706201052"><a name="evs_04_2086_b842352706201052"></a><a name="evs_04_2086_b842352706201052"></a>windows</strong> and <strong id="evs_04_2086_b842352706201055"><a name="evs_04_2086_b842352706201055"></a><a name="evs_04_2086_b842352706201055"></a>linux</strong> are supported. The default value is <strong id="evs_04_2086_b84235270620112"><a name="evs_04_2086_b84235270620112"></a><a name="evs_04_2086_b84235270620112"></a>linux</strong>.</p>
    <div class="note" id="evs_04_2086_note18753145612918"><a name="evs_04_2086_note18753145612918"></a><a name="evs_04_2086_note18753145612918"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="evs_04_2086_ul198423111019"></a><a name="evs_04_2086_ul198423111019"></a><ul id="evs_04_2086_ul198423111019"><li>There are two underscores (_) in front of <strong id="evs_04_2086_b842352706172646"><a name="evs_04_2086_b842352706172646"></a><a name="evs_04_2086_b842352706172646"></a>os</strong> and one underscore (_) after <strong id="evs_04_2086_b842352706172711"><a name="evs_04_2086_b842352706172711"></a><a name="evs_04_2086_b842352706172711"></a>os</strong>.</li><li>This parameter setting takes effect only when the <strong id="evs_04_2086_b8423527061761"><a name="evs_04_2086_b8423527061761"></a><a name="evs_04_2086_b8423527061761"></a>__os_type</strong> field is not included in <strong id="evs_04_2086_b84235270617623"><a name="evs_04_2086_b84235270617623"></a><a name="evs_04_2086_b84235270617623"></a>volume_image_metadata</strong> and the disk status is <strong id="evs_04_2086_b84235270617633"><a name="evs_04_2086_b84235270617633"></a><a name="evs_04_2086_b84235270617633"></a>available</strong>.</li><li>If this parameter is not specified, default value <strong id="evs_04_2086_b842352706171511"><a name="evs_04_2086_b842352706171511"></a><a name="evs_04_2086_b842352706171511"></a>linux</strong> is used as the OS type of the image.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "os-volume_upload_image": {
            "image_name": "sxmatch2", 
            "force": true, 
            "container_format": "bare", 
            "disk_format": "vhd",
            "__os_type": "linux"
        }
    }
    ```


## Response<a name="section5535081111830"></a>

-   Parameter description

    <a name="evs_04_2086_table5532594121252"></a>
    <table><thead align="left"><tr id="evs_04_2086_row60048709121252"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2086_p32107236121252"><a name="evs_04_2086_p32107236121252"></a><a name="evs_04_2086_p32107236121252"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2086_p50549312121252"><a name="evs_04_2086_p50549312121252"></a><a name="evs_04_2086_p50549312121252"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2086_p2030156121252"><a name="evs_04_2086_p2030156121252"></a><a name="evs_04_2086_p2030156121252"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2086_row1599615332144"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p799653310145"><a name="evs_04_2086_p799653310145"></a><a name="evs_04_2086_p799653310145"></a>os-volume_upload_image</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p499603310144"><a name="evs_04_2086_p499603310144"></a><a name="evs_04_2086_p499603310144"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p159971233141420"><a name="evs_04_2086_p159971233141420"></a><a name="evs_04_2086_p159971233141420"></a>Specifies the operation to export the disk data as an image. For details, see <a href="#evs_04_2086_li8542654111830">Parameters in the os-volume_upload_image field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row30224973121252"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p129522216412"><a name="evs_04_2086_p129522216412"></a><a name="evs_04_2086_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p1595262111415"><a name="evs_04_2086_p1595262111415"></a><a name="evs_04_2086_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p109527215417"><a name="evs_04_2086_p109527215417"></a><a name="evs_04_2086_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2086_li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2086_li8542654111830"></a>Parameters in the  **os-volume\_upload\_image**  field

    <a name="evs_04_2086_table9775027111830"></a>
    <table><thead align="left"><tr id="evs_04_2086_row50835692111830"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2086_p24050370111830"><a name="evs_04_2086_p24050370111830"></a><a name="evs_04_2086_p24050370111830"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2086_p1922990111830"><a name="evs_04_2086_p1922990111830"></a><a name="evs_04_2086_p1922990111830"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2086_p271585111830"><a name="evs_04_2086_p271585111830"></a><a name="evs_04_2086_p271585111830"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2086_row21998458111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p37044679111830"><a name="evs_04_2086_p37044679111830"></a><a name="evs_04_2086_p37044679111830"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p47829041111830"><a name="evs_04_2086_p47829041111830"></a><a name="evs_04_2086_p47829041111830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p5292410111830"><a name="evs_04_2086_p5292410111830"></a><a name="evs_04_2086_p5292410111830"></a>Specifies the disk status after the image is exported. The correct value is <strong id="evs_04_2086_b842352706201545"><a name="evs_04_2086_b842352706201545"></a><a name="evs_04_2086_b842352706201545"></a>uploading</strong>.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row47631691111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p32961780111830"><a name="evs_04_2086_p32961780111830"></a><a name="evs_04_2086_p32961780111830"></a>image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p52658493111830"><a name="evs_04_2086_p52658493111830"></a><a name="evs_04_2086_p52658493111830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p15940816111830"><a name="evs_04_2086_p15940816111830"></a><a name="evs_04_2086_p15940816111830"></a>Specifies the ID of the exported image.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row9249618111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p11021632111830"><a name="evs_04_2086_p11021632111830"></a><a name="evs_04_2086_p11021632111830"></a>image_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p20337010111830"><a name="evs_04_2086_p20337010111830"></a><a name="evs_04_2086_p20337010111830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p18706116111830"><a name="evs_04_2086_p18706116111830"></a><a name="evs_04_2086_p18706116111830"></a>Specifies the name of the exported image.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row34137321111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p13659606111830"><a name="evs_04_2086_p13659606111830"></a><a name="evs_04_2086_p13659606111830"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p32686283111830"><a name="evs_04_2086_p32686283111830"></a><a name="evs_04_2086_p32686283111830"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p41886703111830"><a name="evs_04_2086_p41886703111830"></a><a name="evs_04_2086_p41886703111830"></a>Specifies the disk type information. For details, see <a href="#evs_04_2086_li28869709111957">Parameters in the volume_type field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row41436015111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p874086111830"><a name="evs_04_2086_p874086111830"></a><a name="evs_04_2086_p874086111830"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p3692104111830"><a name="evs_04_2086_p3692104111830"></a><a name="evs_04_2086_p3692104111830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p64707827111830"><a name="evs_04_2086_p64707827111830"></a><a name="evs_04_2086_p64707827111830"></a>Specifies the container type of the exported image.</p>
    <p id="evs_04_2086_p1432717114914"><a name="evs_04_2086_p1432717114914"></a><a name="evs_04_2086_p1432717114914"></a>The value can be <strong id="evs_04_2086_b459311179"><a name="evs_04_2086_b459311179"></a><a name="evs_04_2086_b459311179"></a>ami</strong>, <strong id="evs_04_2086_b2060151101710"><a name="evs_04_2086_b2060151101710"></a><a name="evs_04_2086_b2060151101710"></a>ari</strong>, <strong id="evs_04_2086_b14611910174"><a name="evs_04_2086_b14611910174"></a><a name="evs_04_2086_b14611910174"></a>aki</strong>, <strong id="evs_04_2086_b8622119172"><a name="evs_04_2086_b8622119172"></a><a name="evs_04_2086_b8622119172"></a>ovf</strong>, or <strong id="evs_04_2086_b136318117173"><a name="evs_04_2086_b136318117173"></a><a name="evs_04_2086_b136318117173"></a>bare</strong>. The default value is <strong id="evs_04_2086_b198418781710"><a name="evs_04_2086_b198418781710"></a><a name="evs_04_2086_b198418781710"></a>bare</strong>.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row45499535111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p61583720111830"><a name="evs_04_2086_p61583720111830"></a><a name="evs_04_2086_p61583720111830"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p22225458111830"><a name="evs_04_2086_p22225458111830"></a><a name="evs_04_2086_p22225458111830"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p60782776111830"><a name="evs_04_2086_p60782776111830"></a><a name="evs_04_2086_p60782776111830"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row10174073111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p18793567111830"><a name="evs_04_2086_p18793567111830"></a><a name="evs_04_2086_p18793567111830"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p45883995111830"><a name="evs_04_2086_p45883995111830"></a><a name="evs_04_2086_p45883995111830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p61636782111830"><a name="evs_04_2086_p61636782111830"></a><a name="evs_04_2086_p61636782111830"></a>Specifies the format of the exported image.</p>
    <p id="evs_04_2086_p110543734915"><a name="evs_04_2086_p110543734915"></a><a name="evs_04_2086_p110543734915"></a>The value can be <strong id="evs_04_2086_b944918918171"><a name="evs_04_2086_b944918918171"></a><a name="evs_04_2086_b944918918171"></a>vhd</strong>, <strong id="evs_04_2086_b164501093179"><a name="evs_04_2086_b164501093179"></a><a name="evs_04_2086_b164501093179"></a>zvhd</strong>, <strong id="evs_04_2086_b164516931717"><a name="evs_04_2086_b164516931717"></a><a name="evs_04_2086_b164516931717"></a>zvhd2</strong>, <strong id="evs_04_2086_b194511094178"><a name="evs_04_2086_b194511094178"></a><a name="evs_04_2086_b194511094178"></a>raw</strong>, or <strong id="evs_04_2086_b345239191717"><a name="evs_04_2086_b345239191717"></a><a name="evs_04_2086_b345239191717"></a>qcow2</strong>. The default value is <strong id="evs_04_2086_b16430101113170"><a name="evs_04_2086_b16430101113170"></a><a name="evs_04_2086_b16430101113170"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row17860134111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p37384724111830"><a name="evs_04_2086_p37384724111830"></a><a name="evs_04_2086_p37384724111830"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p8263770111830"><a name="evs_04_2086_p8263770111830"></a><a name="evs_04_2086_p8263770111830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p61744912111830"><a name="evs_04_2086_p61744912111830"></a><a name="evs_04_2086_p61744912111830"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row18833303111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p49102550111830"><a name="evs_04_2086_p49102550111830"></a><a name="evs_04_2086_p49102550111830"></a>display_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p17883602111830"><a name="evs_04_2086_p17883602111830"></a><a name="evs_04_2086_p17883602111830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p28018462111830"><a name="evs_04_2086_p28018462111830"></a><a name="evs_04_2086_p28018462111830"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row50839573111830"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p24364735111830"><a name="evs_04_2086_p24364735111830"></a><a name="evs_04_2086_p24364735111830"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p27386538111830"><a name="evs_04_2086_p27386538111830"></a><a name="evs_04_2086_p27386538111830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p32651105111830"><a name="evs_04_2086_p32651105111830"></a><a name="evs_04_2086_p32651105111830"></a>Specifies the time when the disk was updated.</p>
    <p id="evs_04_2086_p22151829479"><a name="evs_04_2086_p22151829479"></a><a name="evs_04_2086_p22151829479"></a><span id="evs_04_2086_text982374294912"><a name="evs_04_2086_text982374294912"></a><a name="evs_04_2086_text982374294912"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2086_li28869709111957"></a>Parameters in the  **volume\_type**  field

    <a name="evs_04_2086_table58500796111957"></a>
    <table><thead align="left"><tr id="evs_04_2086_row41681908111957"><th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.1"><p id="evs_04_2086_p20791387111957"><a name="evs_04_2086_p20791387111957"></a><a name="evs_04_2086_p20791387111957"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.2"><p id="evs_04_2086_p6380778111957"><a name="evs_04_2086_p6380778111957"></a><a name="evs_04_2086_p6380778111957"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="evs_04_2086_p55467427111957"><a name="evs_04_2086_p55467427111957"></a><a name="evs_04_2086_p55467427111957"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2086_row63676572111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p57528669111957"><a name="evs_04_2086_p57528669111957"></a><a name="evs_04_2086_p57528669111957"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p29310607111957"><a name="evs_04_2086_p29310607111957"></a><a name="evs_04_2086_p29310607111957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p39999332111957"><a name="evs_04_2086_p39999332111957"></a><a name="evs_04_2086_p39999332111957"></a>Specifies the ID of the disk type.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row24449673111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p34266520111957"><a name="evs_04_2086_p34266520111957"></a><a name="evs_04_2086_p34266520111957"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p24124731111957"><a name="evs_04_2086_p24124731111957"></a><a name="evs_04_2086_p24124731111957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p39662687111957"><a name="evs_04_2086_p39662687111957"></a><a name="evs_04_2086_p39662687111957"></a>Specifies the name of the disk type.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row21419866111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p57287600111957"><a name="evs_04_2086_p57287600111957"></a><a name="evs_04_2086_p57287600111957"></a>deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p9784030111957"><a name="evs_04_2086_p9784030111957"></a><a name="evs_04_2086_p9784030111957"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p36953317111957"><a name="evs_04_2086_p36953317111957"></a><a name="evs_04_2086_p36953317111957"></a>Specifies whether to delete the disk type.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row64144399111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p28313846111957"><a name="evs_04_2086_p28313846111957"></a><a name="evs_04_2086_p28313846111957"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p11720218111957"><a name="evs_04_2086_p11720218111957"></a><a name="evs_04_2086_p11720218111957"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p56704311111957"><a name="evs_04_2086_p56704311111957"></a><a name="evs_04_2086_p56704311111957"></a><span id="evs_04_2086_text10706161911492"><a name="evs_04_2086_text10706161911492"></a><a name="evs_04_2086_text10706161911492"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2086_row40576753111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p65491588111957"><a name="evs_04_2086_p65491588111957"></a><a name="evs_04_2086_p65491588111957"></a>extra_spec</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p3218391111957"><a name="evs_04_2086_p3218391111957"></a><a name="evs_04_2086_p3218391111957"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p43680990111957"><a name="evs_04_2086_p43680990111957"></a><a name="evs_04_2086_p43680990111957"></a>Specifies the disk type specifications. For details, see <a href="#evs_04_2086_li105361616191716">Parameters in the extra_specs field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row57584594111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p33840505111957"><a name="evs_04_2086_p33840505111957"></a><a name="evs_04_2086_p33840505111957"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p56726405111957"><a name="evs_04_2086_p56726405111957"></a><a name="evs_04_2086_p56726405111957"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p63298283111957"><a name="evs_04_2086_p63298283111957"></a><a name="evs_04_2086_p63298283111957"></a>Specifies the description of the disk type.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_row32813641111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p40659264111957"><a name="evs_04_2086_p40659264111957"></a><a name="evs_04_2086_p40659264111957"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p5066079111957"><a name="evs_04_2086_p5066079111957"></a><a name="evs_04_2086_p5066079111957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p19661880111957"><a name="evs_04_2086_p19661880111957"></a><a name="evs_04_2086_p19661880111957"></a>Specifies the time when the disk type was created.</p>
    <p id="evs_04_2086_p1176814616477"><a name="evs_04_2086_p1176814616477"></a><a name="evs_04_2086_p1176814616477"></a><span id="evs_04_2086_text62451486493"><a name="evs_04_2086_text62451486493"></a><a name="evs_04_2086_text62451486493"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2086_row42739193111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p39322569111957"><a name="evs_04_2086_p39322569111957"></a><a name="evs_04_2086_p39322569111957"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p31011493111957"><a name="evs_04_2086_p31011493111957"></a><a name="evs_04_2086_p31011493111957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p59444132111957"><a name="evs_04_2086_p59444132111957"></a><a name="evs_04_2086_p59444132111957"></a>Specifies the time when the disk type was updated.</p>
    <p id="evs_04_2086_p12839783477"><a name="evs_04_2086_p12839783477"></a><a name="evs_04_2086_p12839783477"></a><span id="evs_04_2086_text23111349184911"><a name="evs_04_2086_text23111349184911"></a><a name="evs_04_2086_text23111349184911"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2086_row65235145111957"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_p49555405111957"><a name="evs_04_2086_p49555405111957"></a><a name="evs_04_2086_p49555405111957"></a>deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_p54564832111957"><a name="evs_04_2086_p54564832111957"></a><a name="evs_04_2086_p54564832111957"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_p41188442111957"><a name="evs_04_2086_p41188442111957"></a><a name="evs_04_2086_p41188442111957"></a>Specifies the time when the disk type was deleted.</p>
    <p id="evs_04_2086_p1971441016471"><a name="evs_04_2086_p1971441016471"></a><a name="evs_04_2086_p1971441016471"></a><span id="evs_04_2086_text112018513495"><a name="evs_04_2086_text112018513495"></a><a name="evs_04_2086_text112018513495"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2086_li105361616191716"></a>Parameters in the  **extra\_specs**  field

    <a name="evs_04_2086_evs_04_2071_table1763545695210"></a>
    <table><thead align="left"><tr id="evs_04_2086_evs_04_2071_row16361656165213"><th class="cellrowborder" valign="top" width="21.45%" id="mcps1.1.4.1.1"><p id="evs_04_2086_evs_04_2071_p1763619566527"><a name="evs_04_2086_evs_04_2071_p1763619566527"></a><a name="evs_04_2086_evs_04_2071_p1763619566527"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.41%" id="mcps1.1.4.1.2"><p id="evs_04_2086_evs_04_2071_p18636105619529"><a name="evs_04_2086_evs_04_2071_p18636105619529"></a><a name="evs_04_2086_evs_04_2071_p18636105619529"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2086_evs_04_2071_p186361556155214"><a name="evs_04_2086_evs_04_2071_p186361556155214"></a><a name="evs_04_2086_evs_04_2071_p186361556155214"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2086_evs_04_2071_row56365565526"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_evs_04_2071_p063625610529"><a name="evs_04_2086_evs_04_2071_p063625610529"></a><a name="evs_04_2086_evs_04_2071_p063625610529"></a>volume_backend_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_evs_04_2071_p3636165635219"><a name="evs_04_2086_evs_04_2071_p3636165635219"></a><a name="evs_04_2086_evs_04_2071_p3636165635219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_evs_04_2071_p17636185614527"><a name="evs_04_2086_evs_04_2071_p17636185614527"></a><a name="evs_04_2086_evs_04_2071_p17636185614527"></a><span id="evs_04_2086_evs_04_2071_text205233101097"><a name="evs_04_2086_evs_04_2071_text205233101097"></a><a name="evs_04_2086_evs_04_2071_text205233101097"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2086_evs_04_2071_row156362568523"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_evs_04_2071_p863675695214"><a name="evs_04_2086_evs_04_2071_p863675695214"></a><a name="evs_04_2086_evs_04_2071_p863675695214"></a>availability-zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_evs_04_2071_p8636175665214"><a name="evs_04_2086_evs_04_2071_p8636175665214"></a><a name="evs_04_2086_evs_04_2071_p8636175665214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_evs_04_2071_p18636356185213"><a name="evs_04_2086_evs_04_2071_p18636356185213"></a><a name="evs_04_2086_evs_04_2071_p18636356185213"></a><span id="evs_04_2086_evs_04_2071_text533914121390"><a name="evs_04_2086_evs_04_2071_text533914121390"></a><a name="evs_04_2086_evs_04_2071_text533914121390"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2086_evs_04_2071_row17844276596"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_evs_04_2071_p178418274593"><a name="evs_04_2086_evs_04_2071_p178418274593"></a><a name="evs_04_2086_evs_04_2071_p178418274593"></a>HW:availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_evs_04_2071_p168416276599"><a name="evs_04_2086_evs_04_2071_p168416276599"></a><a name="evs_04_2086_evs_04_2071_p168416276599"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_evs_04_2071_p1540410211408"><a name="evs_04_2086_evs_04_2071_p1540410211408"></a><a name="evs_04_2086_evs_04_2071_p1540410211408"></a><span id="evs_04_2086_evs_04_2071_evs_04_2071_text533914121390"><a name="evs_04_2086_evs_04_2071_evs_04_2071_text533914121390"></a><a name="evs_04_2086_evs_04_2071_evs_04_2071_text533914121390"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2086_evs_04_2071_row3637135611527"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_evs_04_2071_p163710561529"><a name="evs_04_2086_evs_04_2071_p163710561529"></a><a name="evs_04_2086_evs_04_2071_p163710561529"></a>RESKEY:availability_zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_evs_04_2071_p166374562525"><a name="evs_04_2086_evs_04_2071_p166374562525"></a><a name="evs_04_2086_evs_04_2071_p166374562525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_evs_04_2071_p3637756205214"><a name="evs_04_2086_evs_04_2071_p3637756205214"></a><a name="evs_04_2086_evs_04_2071_p3637756205214"></a>Specifies the AZs that support the current disk type.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2086_li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2086_evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2086_evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2086_evs_04_2013_p19541716103019"><a name="evs_04_2086_evs_04_2013_p19541716103019"></a><a name="evs_04_2086_evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2086_evs_04_2013_p39375186103019"><a name="evs_04_2086_evs_04_2013_p39375186103019"></a><a name="evs_04_2086_evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2086_evs_04_2013_p38578950103019"><a name="evs_04_2086_evs_04_2013_p38578950103019"></a><a name="evs_04_2086_evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2086_evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_evs_04_2013_p46815658103019"><a name="evs_04_2086_evs_04_2013_p46815658103019"></a><a name="evs_04_2086_evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_evs_04_2013_p33971979103019"><a name="evs_04_2086_evs_04_2013_p33971979103019"></a><a name="evs_04_2086_evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_evs_04_2013_p21623243103019"><a name="evs_04_2086_evs_04_2013_p21623243103019"></a><a name="evs_04_2086_evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2086_evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2086_evs_04_2013_p59870541103019"><a name="evs_04_2086_evs_04_2013_p59870541103019"></a><a name="evs_04_2086_evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2086_evs_04_2013_p17675690103019"><a name="evs_04_2086_evs_04_2013_p17675690103019"></a><a name="evs_04_2086_evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2086_evs_04_2013_p6087468103019"><a name="evs_04_2086_evs_04_2013_p6087468103019"></a><a name="evs_04_2086_evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2086_evs_04_2013_p54787218103019"><a name="evs_04_2086_evs_04_2013_p54787218103019"></a><a name="evs_04_2086_evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "os-volume_upload_image": {
            "status": "uploading", 
            "size": 40, 
            "id": "16369c5d-384d-4e64-b37a-56d898769362", 
            "image_id": "c5333daa-fbc8-4d1d-bf79-b0567bb45d15", 
            "image_name": "evs-ims-test1027", 
            "volume_type": {
                "description": "None", 
                "deleted": false, 
                "created_at": "2015-05-24T14:47:22.132268", 
                "updated_at": "2017-07-29T11:29:33.730076", 
                "extra_specs": {
                    "volume_backend_name": "<or> iaas blockstorage_SATA <or> iaas blockstorage_SAS <or> iaas blockstoragesata", 
                    "XX:availability_zone": "az-dc-1"
                }, 
                "is_public": true, 
                "deleted_at": null, 
                "id": "8247b6ed-37f0-4c48-8ef1-f0027fb332bc", 
                "name": "SATA"
            }, 
            "container_format": "bare", 
            "disk_format": "vhd", 
            "display_description": "", 
            "updated_at": "2018-01-11T01:50:25.800931"
        }
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badRequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "itemNotFound": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section28290342112319"></a>

-   Normal

    202


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

