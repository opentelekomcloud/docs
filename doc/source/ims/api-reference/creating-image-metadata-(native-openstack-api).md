# Creating Image Metadata \(Native OpenStack API\)<a name="EN-US_TOPIC_0031615565"></a>

## Function<a name="section66302617144828"></a>

This API is used to create image metadata.

After the API is successfully invoked, the image metadata is created, but the image file does not exist yet.

## URI<a name="section16226363144828"></a>

POST /v2/images

## Request<a name="section22707920144828"></a>

-   Request parameters

    <a name="table53011268153646"></a>
    <table><thead align="left"><tr id="row8255548153646"><th class="cellrowborder" valign="top" width="31.35%" id="mcps1.1.5.1.1"><p id="p64719651153646"><a name="p64719651153646"></a><a name="p64719651153646"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.54%" id="mcps1.1.5.1.2"><p id="p7800370153646"><a name="p7800370153646"></a><a name="p7800370153646"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.86%" id="mcps1.1.5.1.3"><p id="p27850258153646"><a name="p27850258153646"></a><a name="p27850258153646"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.25%" id="mcps1.1.5.1.4"><p id="p41278443153646"><a name="p41278443153646"></a><a name="p41278443153646"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55219556153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p43599013153646"><a name="p43599013153646"></a><a name="p43599013153646"></a>__os_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p41859159153646"><a name="p41859159153646"></a><a name="p41859159153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p35148705153646"><a name="p35148705153646"></a><a name="p35148705153646"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p28472876153646"><a name="p28472876153646"></a><a name="p28472876153646"></a>Specifies the image OS version. For the value range, see <a href="values-of-related-parameters.md">Values of Related Parameters</a>.</p>
    <p id="p24601632153646"><a name="p24601632153646"></a><a name="p24601632153646"></a>If this parameter is not specified, the value will be set to <strong id="b84235270611441"><a name="b84235270611441"></a><a name="b84235270611441"></a>Other Linux(64 bit)</strong>. In that case, the ECS creation using this image may fail, and ECSs created using this image may fail to run properly.</p>
    </td>
    </tr>
    <tr id="row20088096153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p16523075153646"><a name="p16523075153646"></a><a name="p16523075153646"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p63300707153646"><a name="p63300707153646"></a><a name="p63300707153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p27083623153646"><a name="p27083623153646"></a><a name="p27083623153646"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p46289848153646"><a name="p46289848153646"></a><a name="p46289848153646"></a>Specifies whether the image is available to other tenants.</p>
    <p id="p13955448153646"><a name="p13955448153646"></a><a name="p13955448153646"></a>The default value is <strong id="b842352706145544"><a name="b842352706145544"></a><a name="b842352706145544"></a>private</strong>. When creating image metadata, the value of <strong id="b842352706142944"><a name="b842352706142944"></a><a name="b842352706142944"></a>visibility</strong> can be set to <strong id="b842352706142937"><a name="b842352706142937"></a><a name="b842352706142937"></a>private</strong> only.</p>
    </td>
    </tr>
    <tr id="row56649510153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p25207637153646"><a name="p25207637153646"></a><a name="p25207637153646"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p28552749153646"><a name="p28552749153646"></a><a name="p28552749153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p31071317153646"><a name="p31071317153646"></a><a name="p31071317153646"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p33748725153646"><a name="p33748725153646"></a><a name="p33748725153646"></a>Specifies the image name. If this parameter is not specified, its value is empty by default. In that case, ECS creation using this image will fail. The name contains 1 to 255 characters. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row49292214153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p33246399153646"><a name="p33246399153646"></a><a name="p33246399153646"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p8603833153646"><a name="p8603833153646"></a><a name="p8603833153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p25821900153646"><a name="p25821900153646"></a><a name="p25821900153646"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p11199135153646"><a name="p11199135153646"></a><a name="p11199135153646"></a>Specifies whether the image is protected. A protected image cannot be deleted. The default value is <strong id="b1498339853"><a name="b1498339853"></a><a name="b1498339853"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row34714714153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p6985178153646"><a name="p6985178153646"></a><a name="p6985178153646"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p28928513153646"><a name="p28928513153646"></a><a name="p28928513153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p61508237153646"><a name="p61508237153646"></a><a name="p61508237153646"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p16111334153646"><a name="p16111334153646"></a><a name="p16111334153646"></a>Specifies the container format.</p>
    <p id="p10784283153646"><a name="p10784283153646"></a><a name="p10784283153646"></a>The default value is <strong id="b1240645146"><a name="b1240645146"></a><a name="b1240645146"></a>bare</strong>.</p>
    </td>
    </tr>
    <tr id="row29949683153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p10005277153646"><a name="p10005277153646"></a><a name="p10005277153646"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p5121099153646"><a name="p5121099153646"></a><a name="p5121099153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p12155878153646"><a name="p12155878153646"></a><a name="p12155878153646"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p45102037153646"><a name="p45102037153646"></a><a name="p45102037153646"></a>Specifies the image file format. The value can be <strong id="b842352706173625"><a name="b842352706173625"></a><a name="b842352706173625"></a>vhd</strong>, <strong id="b842352706173628"><a name="b842352706173628"></a><a name="b842352706173628"></a>zvhd</strong>, <strong id="b842352706173630"><a name="b842352706173630"></a><a name="b842352706173630"></a>raw</strong>, <strong id="b84235270685239"><a name="b84235270685239"></a><a name="b84235270685239"></a>zvhd2</strong>, or <strong id="b842352706173635"><a name="b842352706173635"></a><a name="b842352706173635"></a>qcow2</strong>. The default value is <strong id="b932831812"><a name="b932831812"></a><a name="b932831812"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="row29386369153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p31485649153646"><a name="p31485649153646"></a><a name="p31485649153646"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p200749153646"><a name="p200749153646"></a><a name="p200749153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p16260734153646"><a name="p16260734153646"></a><a name="p16260734153646"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p42051116153646"><a name="p42051116153646"></a><a name="p42051116153646"></a>Lists the image tags. The tag contains 1 to 255 characters. The value is left blank by default.</p>
    </td>
    </tr>
    <tr id="row50697246153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p12836285153646"><a name="p12836285153646"></a><a name="p12836285153646"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p33106160153646"><a name="p33106160153646"></a><a name="p33106160153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p64353312153646"><a name="p64353312153646"></a><a name="p64353312153646"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p45235764153646"><a name="p45235764153646"></a><a name="p45235764153646"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on <span id="text826912402084"><a name="text826912402084"></a><a name="text826912402084"></a></span><span id="text1496184118812"><a name="text1496184118812"></a><a name="text1496184118812"></a>ECS</span> specifications. The default value is <strong id="b1694630969"><a name="b1694630969"></a><a name="b1694630969"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row4468695153646"><td class="cellrowborder" valign="top" width="31.35%" headers="mcps1.1.5.1.1 "><p id="p26420029153646"><a name="p26420029153646"></a><a name="p26420029153646"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.1.5.1.2 "><p id="p59647611153646"><a name="p59647611153646"></a><a name="p59647611153646"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.1.5.1.3 "><p id="p66727226153646"><a name="p66727226153646"></a><a name="p66727226153646"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.25%" headers="mcps1.1.5.1.4 "><p id="p38417884203334"><a name="p38417884203334"></a><a name="p38417884203334"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
    <p id="p57330868153646"><a name="p57330868153646"></a><a name="p57330868153646"></a>The value of this parameter must be greater than the image system disk capacity. Otherwise, the <span id="text1126650384"><a name="text1126650384"></a><a name="text1126650384"></a></span><span id="text182617501488"><a name="text182617501488"></a><a name="text182617501488"></a>ECS</span> creation may fail.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >Parameters in the request body are strings of no more than 255 characters, and their values can be left blank.  


-   Example request

    ```
    POST https://{Endpoint}/v2/images
    ```

    ```
    {
        "__os_version": "Ubuntu 14.04 server 64bit",
        "container_format": "bare",
        "disk_format": "vhd",
        "min_disk": 1,
        "min_ram": 1024,
        "name": "test",
        "tags": [
            "test",
            "image"
        ],
        "visibility": "private",
        "protected": false,
        "aaaa":"11111"
    }
    ```


## Response<a name="section37386190144828"></a>

-   Response parameters

    <a name="table65680948153746"></a>
    <table><thead align="left"><tr id="row59664825153746"><th class="cellrowborder" valign="top" width="36.36%" id="mcps1.1.4.1.1"><p id="p1012670153746"><a name="p1012670153746"></a><a name="p1012670153746"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.85%" id="mcps1.1.4.1.2"><p id="p352397153746"><a name="p352397153746"></a><a name="p352397153746"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.1.4.1.3"><p id="p28544167153746"><a name="p28544167153746"></a><a name="p28544167153746"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30376173153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p44550985153746"><a name="p44550985153746"></a><a name="p44550985153746"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p39910492153746"><a name="p39910492153746"></a><a name="p39910492153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p11524453153746"><a name="p11524453153746"></a><a name="p11524453153746"></a>Specifies whether the image is available to other tenants. The value is <strong id="b84235270614516"><a name="b84235270614516"></a><a name="b84235270614516"></a>private</strong>.</p>
    </td>
    </tr>
    <tr id="row61065506153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p47358972153746"><a name="p47358972153746"></a><a name="p47358972153746"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p8177445153746"><a name="p8177445153746"></a><a name="p8177445153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p58393284153746"><a name="p58393284153746"></a><a name="p58393284153746"></a>Specifies the image name. If this parameter is not specified, its value is empty by default. In that case, ECS creation using this image will fail. The name contains 1 to 128 characters. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row32235552153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p60942880153746"><a name="p60942880153746"></a><a name="p60942880153746"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p11625005153746"><a name="p11625005153746"></a><a name="p11625005153746"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p2101387153746"><a name="p2101387153746"></a><a name="p2101387153746"></a>Specifies whether the image is protected. A protected image cannot be deleted. The value is <strong id="b842352706141032"><a name="b842352706141032"></a><a name="b842352706141032"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row35994669153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p29887100153746"><a name="p29887100153746"></a><a name="p29887100153746"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p64274239153746"><a name="p64274239153746"></a><a name="p64274239153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p3986378091022"><a name="p3986378091022"></a><a name="p3986378091022"></a>Specifies the container format.</p>
    <p id="p2322970491022"><a name="p2322970491022"></a><a name="p2322970491022"></a>The value is <strong id="b470053974"><a name="b470053974"></a><a name="b470053974"></a>bare</strong>.</p>
    </td>
    </tr>
    <tr id="row58291220153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p23968345153746"><a name="p23968345153746"></a><a name="p23968345153746"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p20244641153746"><a name="p20244641153746"></a><a name="p20244641153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p2302086591022"><a name="p2302086591022"></a><a name="p2302086591022"></a>Specifies the image file format. The value can be <strong id="b290129807"><a name="b290129807"></a><a name="b290129807"></a>vhd</strong>, <strong id="b555538585"><a name="b555538585"></a><a name="b555538585"></a>zvhd</strong>, <strong id="b356600473"><a name="b356600473"></a><a name="b356600473"></a>raw</strong>, or <strong id="b1038206844"><a name="b1038206844"></a><a name="b1038206844"></a>qcow2</strong>. The default value is <strong id="b842352706165234"><a name="b842352706165234"></a><a name="b842352706165234"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="row16647962153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p6307710153746"><a name="p6307710153746"></a><a name="p6307710153746"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p45828379153746"><a name="p45828379153746"></a><a name="p45828379153746"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p21111204153746"><a name="p21111204153746"></a><a name="p21111204153746"></a>Lists the image tags. The tag contains 1 to 255 characters.</p>
    </td>
    </tr>
    <tr id="row32285962153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p65026100153746"><a name="p65026100153746"></a><a name="p65026100153746"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p25195510153746"><a name="p25195510153746"></a><a name="p25195510153746"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p27570397153746"><a name="p27570397153746"></a><a name="p27570397153746"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the ECS specifications limit. The value is generally set to <strong id="b842352706103121"><a name="b842352706103121"></a><a name="b842352706103121"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row46806987153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p33269625153746"><a name="p33269625153746"></a><a name="p33269625153746"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p43985037153746"><a name="p43985037153746"></a><a name="p43985037153746"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p33012089153426"><a name="p33012089153426"></a><a name="p33012089153426"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB. It must be greater than the image system disk capacity. Otherwise, the <span id="text1810514495915"><a name="text1810514495915"></a><a name="text1810514495915"></a></span><span id="text186857585917"><a name="text186857585917"></a><a name="text186857585917"></a>ECS</span> creation may fail.</p>
    </td>
    </tr>
    <tr id="row17715747153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p25689427153746"><a name="p25689427153746"></a><a name="p25689427153746"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p127882921768"><a name="p127882921768"></a><a name="p127882921768"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p29539523155411"><a name="p29539523155411"></a><a name="p29539523155411"></a>Specifies the image status. The value can be one of the following:</p>
    <a name="ul64671162155411"></a><a name="ul64671162155411"></a><ul id="ul64671162155411"><li><strong id="b842352706103333"><a name="b842352706103333"></a><a name="b842352706103333"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="b842352706104325"><a name="b842352706104325"></a><a name="b842352706104325"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="b842352706104450"><a name="b842352706104450"></a><a name="b842352706104450"></a>deleted</strong>: indicates that the image has been deleted. </li><li><strong id="b842352706104518"><a name="b842352706104518"></a><a name="b842352706104518"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="b842352706104558"><a name="b842352706104558"></a><a name="b842352706104558"></a>active</strong>: indicates that the image is available for use. </li></ul>
    </td>
    </tr>
    <tr id="row36868745153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p33578394153746"><a name="p33578394153746"></a><a name="p33578394153746"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p56557754153746"><a name="p56557754153746"></a><a name="p56557754153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p17775385153746"><a name="p17775385153746"></a><a name="p17775385153746"></a>Specifies the time when the image was created. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row25760740153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p6245233153746"><a name="p6245233153746"></a><a name="p6245233153746"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p38569043153746"><a name="p38569043153746"></a><a name="p38569043153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p37084793153746"><a name="p37084793153746"></a><a name="p37084793153746"></a>Specifies the time when the image was updated. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row65327686153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p57051191153746"><a name="p57051191153746"></a><a name="p57051191153746"></a>self</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p46735376153746"><a name="p46735376153746"></a><a name="p46735376153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p27469127153746"><a name="p27469127153746"></a><a name="p27469127153746"></a>Specifies the image URL.</p>
    </td>
    </tr>
    <tr id="row45895558153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p26552727153746"><a name="p26552727153746"></a><a name="p26552727153746"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p64943162153746"><a name="p64943162153746"></a><a name="p64943162153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p25904797153746"><a name="p25904797153746"></a><a name="p25904797153746"></a>Specifies the image ID. After the image creation API is called, the image ID must be saved. The image ID is used to invoke the image uploading API and upload the image.</p>
    </td>
    </tr>
    <tr id="row31816583153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p27006401153746"><a name="p27006401153746"></a><a name="p27006401153746"></a>file</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p21597859153746"><a name="p21597859153746"></a><a name="p21597859153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p4596122153746"><a name="p4596122153746"></a><a name="p4596122153746"></a>Specifies the URL for uploading and downloading the image file.</p>
    </td>
    </tr>
    <tr id="row41365104153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p62239150153746"><a name="p62239150153746"></a><a name="p62239150153746"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p60735714153746"><a name="p60735714153746"></a><a name="p60735714153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p20645801153746"><a name="p20645801153746"></a><a name="p20645801153746"></a>Specifies the URL for accessing the schema.</p>
    </td>
    </tr>
    <tr id="row51594484153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p18403679153746"><a name="p18403679153746"></a><a name="p18403679153746"></a>__image_source_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p17692826153746"><a name="p17692826153746"></a><a name="p17692826153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p23832762153746"><a name="p23832762153746"></a><a name="p23832762153746"></a>Specifies the image backend storage type. Only UDS is supported currently. </p>
    </td>
    </tr>
    <tr id="row13168267153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p59996701153746"><a name="p59996701153746"></a><a name="p59996701153746"></a>__image_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p44870066153746"><a name="p44870066153746"></a><a name="p44870066153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p10596742153746"><a name="p10596742153746"></a><a name="p10596742153746"></a>Specifies the image size. The unit is byte.</p>
    </td>
    </tr>
    <tr id="row28261814153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p7505593153746"><a name="p7505593153746"></a><a name="p7505593153746"></a>__isregistered</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p53402269153746"><a name="p53402269153746"></a><a name="p53402269153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p30616526153746"><a name="p30616526153746"></a><a name="p30616526153746"></a>Specifies whether the image is registered. Only registered images can be queried on the portal. The value is <strong id="b1444301417"><a name="b1444301417"></a><a name="b1444301417"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row64019507153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p18197556153746"><a name="p18197556153746"></a><a name="p18197556153746"></a>__os_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p7501613153746"><a name="p7501613153746"></a><a name="p7501613153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p3650932153746"><a name="p3650932153746"></a><a name="p3650932153746"></a>Specifies the image OS version. For the value range, see <a href="values-of-related-parameters.md">Values of Related Parameters</a>.</p>
    </td>
    </tr>
    <tr id="row27290104153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p63014816153746"><a name="p63014816153746"></a><a name="p63014816153746"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p49609854153746"><a name="p49609854153746"></a><a name="p49609854153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p58975236153746"><a name="p58975236153746"></a><a name="p58975236153746"></a>Specifies the image OS type. The value of this parameter depends on that of <strong id="b842352706143412"><a name="b842352706143412"></a><a name="b842352706143412"></a>__os_version</strong>. The value can be <strong id="b842352706143429"><a name="b842352706143429"></a><a name="b842352706143429"></a>Windows</strong>, <strong id="b842352706143432"><a name="b842352706143432"></a><a name="b842352706143432"></a>Linux</strong>, or <strong id="b842352706143435"><a name="b842352706143435"></a><a name="b842352706143435"></a>other</strong>.</p>
    </td>
    </tr>
    <tr id="row61015077153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p43274176153746"><a name="p43274176153746"></a><a name="p43274176153746"></a>__platform</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p51377616153746"><a name="p51377616153746"></a><a name="p51377616153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p837397153746"><a name="p837397153746"></a><a name="p837397153746"></a>Specifies the OS platform supported by the image. The value of this parameter depends on that of <strong id="b148402235114355"><a name="b148402235114355"></a><a name="b148402235114355"></a>__os_version</strong>.</p>
    </td>
    </tr>
    <tr id="row7536579153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p6483196153746"><a name="p6483196153746"></a><a name="p6483196153746"></a>__os_bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p56341747153746"><a name="p56341747153746"></a><a name="p56341747153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p278785153746"><a name="p278785153746"></a><a name="p278785153746"></a>Specifies the OS bit. The value of this parameter depends on that of <strong id="b1028547871143526"><a name="b1028547871143526"></a><a name="b1028547871143526"></a>__os_version</strong>. The value can be <strong id="b842352706143549"><a name="b842352706143549"></a><a name="b842352706143549"></a>32</strong> or <strong id="b842352706143546"><a name="b842352706143546"></a><a name="b842352706143546"></a>64</strong>.</p>
    </td>
    </tr>
    <tr id="row2509069153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p1908061153746"><a name="p1908061153746"></a><a name="p1908061153746"></a>__imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p36544143153746"><a name="p36544143153746"></a><a name="p36544143153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p7285568153746"><a name="p7285568153746"></a><a name="p7285568153746"></a>Specifies the image type. <strong id="b842352706143620"><a name="b842352706143620"></a><a name="b842352706143620"></a>private</strong> indicates a private image.</p>
    </td>
    </tr>
    <tr id="row34742228153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p62657107153746"><a name="p62657107153746"></a><a name="p62657107153746"></a>virtual_env_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p51489910153746"><a name="p51489910153746"></a><a name="p51489910153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p9933162153746"><a name="p9933162153746"></a><a name="p9933162153746"></a>Specifies the platform type.</p>
    <p id="p1364519165504"><a name="p1364519165504"></a><a name="p1364519165504"></a>Specifies the environment where the image is used. The value can be <strong id="b1977415411508"><a name="b1977415411508"></a><a name="b1977415411508"></a>FusionCompute</strong>, <strong id="b1277465435014"><a name="b1277465435014"></a><a name="b1277465435014"></a>Ironic</strong>, or <strong id="b16775654175015"><a name="b16775654175015"></a><a name="b16775654175015"></a>DataImage</strong>.</p>
    <a name="ul1113018265506"></a><a name="ul1113018265506"></a><ul id="ul1113018265506"><li>For an <span id="text112717547261"><a name="text112717547261"></a><a name="text112717547261"></a></span><span id="text1271145411263"><a name="text1271145411263"></a><a name="text1271145411263"></a>ECS</span> image, the value is <strong id="b6200101517432"><a name="b6200101517432"></a><a name="b6200101517432"></a>FusionCompute</strong>.</li><li>For a data disk image, the value is <strong id="b7466112518368"><a name="b7466112518368"></a><a name="b7466112518368"></a>DataImage</strong>.</li><li>For a <span id="text1054736288"><a name="text1054736288"></a><a name="text1054736288"></a></span><span id="text431595841"><a name="text431595841"></a><a name="text431595841"></a>BMS</span> image, the value is <strong id="b2023346354"><a name="b2023346354"></a><a name="b2023346354"></a>Ironic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row66388651153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p8771616153746"><a name="p8771616153746"></a><a name="p8771616153746"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p38277576153746"><a name="p38277576153746"></a><a name="p38277576153746"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p13475914153746"><a name="p13475914153746"></a><a name="p13475914153746"></a>Specifies the ID of the project to which the image belongs.</p>
    </td>
    </tr>
    <tr id="row54174368153746"><td class="cellrowborder" valign="top" width="36.36%" headers="mcps1.1.4.1.1 "><p id="p26047664153746"><a name="p26047664153746"></a><a name="p26047664153746"></a>virtual_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.85%" headers="mcps1.1.4.1.2 "><p id="p39559770153746"><a name="p39559770153746"></a><a name="p39559770153746"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.1.4.1.3 "><p id="p50224836153746"><a name="p50224836153746"></a><a name="p50224836153746"></a>Specifies the virtual size of the image. The unit is byte.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    STATUS CODE 201
    ```

    ```
    {
        "schema": "/v2/schemas/image",
        "min_disk": 1,
        "created_at": "2016-06-02T07:49:48Z",
        "__image_source_type": "uds",
        "container_format": "bare",
        "__image_size": "0",
        "file": "/v2/images/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba86/file",
        "updated_at": "2016-06-02T07:49:49Z",
        "protected": false,
        "id": "4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba86",
        "__isregistered": "true",
        "min_ram": 1024,
        "owner": "b912fb4a4c464b568ecfca1071b21b10",
        "__os_type": "Linux",
        "__imagetype": "private",
        "visibility": "private",
        "virtual_env_type": "FusionCompute",
        "tags": [
            "test",
            "image"
        ],
        "__platform": "Ubuntu",
        "__os_bit": "64",
        "__os_version": "Ubuntu 14.04 server 64bit",
        "name": "test",
        "self": "/v2/images/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba86",
        "disk_format": "vhd",
        "status": "queued"
    }
    ```


## Returned Values<a name="section55843593"></a>

-   Normal

    201

-   Abnormal

    <a name="table512644917454"></a>
    <table><thead align="left"><tr id="row5075107217454"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p1719616917454"><a name="p1719616917454"></a><a name="p1719616917454"></a><strong id="b64315875161412"><a name="b64315875161412"></a><a name="b64315875161412"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p5071248317454"><a name="p5071248317454"></a><a name="p5071248317454"></a><strong id="b61932747161416"><a name="b61932747161416"></a><a name="b61932747161416"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1407048617454"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p6596756117454"><a name="p6596756117454"></a><a name="p6596756117454"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p4177219617454"><a name="p4177219617454"></a><a name="p4177219617454"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row4040544817454"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p5161589217454"><a name="p5161589217454"></a><a name="p5161589217454"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2013769117454"><a name="p2013769117454"></a><a name="p2013769117454"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row4702149717454"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p5064493517454"><a name="p5064493517454"></a><a name="p5064493517454"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p859904517454"><a name="p859904517454"></a><a name="p859904517454"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row27405030192213"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p15819393192215"><a name="p15819393192215"></a><a name="p15819393192215"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p6302489192215"><a name="p6302489192215"></a><a name="p6302489192215"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row1028254117454"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p2757951117454"><a name="p2757951117454"></a><a name="p2757951117454"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1934790917454"><a name="p1934790917454"></a><a name="p1934790917454"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row3991345717454"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p1176460917454"><a name="p1176460917454"></a><a name="p1176460917454"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1340929017454"><a name="p1340929017454"></a><a name="p1340929017454"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


