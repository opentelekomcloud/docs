# Querying Images \(Native OpenStack API\)<a name="EN-US_TOPIC_0060804959"></a>

## Function<a name="section59471393"></a>

This API is used to obtain the image list.

This API does not return the complete result at once, but uses pagination.

## Pagination<a name="section165587269201"></a>

Pagination refers to the function of returning a subset of a group of images, a link to obtain the next set of images, and a link of the set of images. By default, a set contains 25 images. You can also use the  **limit**  and  **marker**  parameters to paginate through images manually and specify the number of images that can be returned.

The parameter  **first**  in the response indicates the URL of the first page of images, and parameter  **next**  indicates the URL of the next page of images. When the last page of images is queried, there is no parameter  **next**.

## URI<a name="section65480490"></a>

GET /v2/images

>![](/images/icon-note.gif) **NOTE:**   
>-   You can type a question mark \(?\) and an ampersand \(&\) at the end of the URI to define multiple search criteria. For details, see the example request.  

[Table 1](#table33420935171457)  lists the parameters.

**Table  1**  Parameter description

<a name="table33420935171457"></a>
<table><thead align="left"><tr id="row56943395171457"><th class="cellrowborder" valign="top" width="20.78%" id="mcps1.2.5.1.1"><p id="p2577832171521"><a name="p2577832171521"></a><a name="p2577832171521"></a><strong id="b24725868162658"><a name="b24725868162658"></a><a name="b24725868162658"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.64%" id="mcps1.2.5.1.2"><p id="p7477841171521"><a name="p7477841171521"></a><a name="p7477841171521"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.840000000000002%" id="mcps1.2.5.1.3"><p id="p3754553172418"><a name="p3754553172418"></a><a name="p3754553172418"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.74%" id="mcps1.2.5.1.4"><p id="p57397527172421"><a name="p57397527172421"></a><a name="p57397527172421"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7130167171457"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p31986361171514"><a name="p31986361171514"></a><a name="p31986361171514"></a>__isregistered</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p40758410171514"><a name="p40758410171514"></a><a name="p40758410171514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p43890043172418"><a name="p43890043172418"></a><a name="p43890043172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p37340191172421"><a name="p37340191172421"></a><a name="p37340191172421"></a>Specifies whether the image is available. The value can be <strong id="b84235270616222"><a name="b84235270616222"></a><a name="b84235270616222"></a>true</strong>. The value is <strong id="b2049464823162253"><a name="b2049464823162253"></a><a name="b2049464823162253"></a>true</strong> for all extension APIs by default. Common users can query only the images for which the value of this parameter is <strong id="b846915150162332"><a name="b846915150162332"></a><a name="b846915150162332"></a>true</strong>.</p>
</td>
</tr>
<tr id="row4824363171457"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p18187484171514"><a name="p18187484171514"></a><a name="p18187484171514"></a>__imagetype</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p63900110171514"><a name="p63900110171514"></a><a name="p63900110171514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p64847277172418"><a name="p64847277172418"></a><a name="p64847277172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p10541175163112"><a name="p10541175163112"></a><a name="p10541175163112"></a>Specifies the image type. The following types are supported:</p>
<a name="ul45412511314"></a><a name="ul45412511314"></a><ul id="ul45412511314"><li>Public image: The value is <strong id="b842352706163515"><a name="b842352706163515"></a><a name="b842352706163515"></a>gold</strong>.</li><li>Private image: The value is <strong id="b1762610292163524"><a name="b1762610292163524"></a><a name="b1762610292163524"></a>private</strong>.</li><li>Shared image: The value is <strong id="b298092137163545"><a name="b298092137163545"></a><a name="b298092137163545"></a>shared</strong>.</li></ul>
</td>
</tr>
<tr id="row53979171457"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p41763237171514"><a name="p41763237171514"></a><a name="p41763237171514"></a>protected</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p27379026171514"><a name="p27379026171514"></a><a name="p27379026171514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p32804702172418"><a name="p32804702172418"></a><a name="p32804702172418"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p17378076172421"><a name="p17378076172421"></a><a name="p17378076172421"></a>Specifies whether the image is protected. The value is <strong id="b84235270614836"><a name="b84235270614836"></a><a name="b84235270614836"></a>true</strong> or <strong id="b84235270614840"><a name="b84235270614840"></a><a name="b84235270614840"></a>false</strong>. Set it to <strong id="b48612739142847_1"><a name="b48612739142847_1"></a><a name="b48612739142847_1"></a>true</strong> when you query public images. This parameter is optional when you query private images.</p>
</td>
</tr>
<tr id="row64237648171457"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p51588314171514"><a name="p51588314171514"></a><a name="p51588314171514"></a>visibility</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p17903883171514"><a name="p17903883171514"></a><a name="p17903883171514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p263785172418"><a name="p263785172418"></a><a name="p263785172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p14732836101910"><a name="p14732836101910"></a><a name="p14732836101910"></a>Specifies whether the image is available to other tenants. Available values include:</p>
<a name="ul1056613910205"></a><a name="ul1056613910205"></a><ul id="ul1056613910205"><li><strong id="b6608553717"><a name="b6608553717"></a><a name="b6608553717"></a>public</strong>: public image</li><li><strong id="b64621456270"><a name="b64621456270"></a><a name="b64621456270"></a>private</strong>: private image</li><li><strong id="b317515581874"><a name="b317515581874"></a><a name="b317515581874"></a>shared</strong>: shared image</li></ul>
</td>
</tr>
<tr id="row46885915171457"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p40504458171514"><a name="p40504458171514"></a><a name="p40504458171514"></a>owner</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p59635642171514"><a name="p59635642171514"></a><a name="p59635642171514"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p25988654172418"><a name="p25988654172418"></a><a name="p25988654172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p34708322172421"><a name="p34708322172421"></a><a name="p34708322172421"></a>Specifies the tenant to which the image belongs.</p>
</td>
</tr>
<tr id="row42514069171457"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p45188792171710"><a name="p45188792171710"></a><a name="p45188792171710"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p36413517171710"><a name="p36413517171710"></a><a name="p36413517171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p65237974172418"><a name="p65237974172418"></a><a name="p65237974172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p2325353172421"><a name="p2325353172421"></a><a name="p2325353172421"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row44909088171457"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p13802561171710"><a name="p13802561171710"></a><a name="p13802561171710"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p44265688171710"><a name="p44265688171710"></a><a name="p44265688171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p22641299172418"><a name="p22641299172418"></a><a name="p22641299172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p32131061155224"><a name="p32131061155224"></a><a name="p32131061155224"></a>Specifies the image status. The value can be one of the following:</p>
<a name="ul43292299155227"></a><a name="ul43292299155227"></a><ul id="ul43292299155227"><li><strong id="b842352706103333"><a name="b842352706103333"></a><a name="b842352706103333"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="b842352706104325"><a name="b842352706104325"></a><a name="b842352706104325"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="b842352706104450"><a name="b842352706104450"></a><a name="b842352706104450"></a>deleted</strong>: indicates that the image has been deleted. </li><li><strong id="b842352706104518"><a name="b842352706104518"></a><a name="b842352706104518"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="b842352706104558"><a name="b842352706104558"></a><a name="b842352706104558"></a>active</strong>: indicates that the image is available for use. </li></ul>
</td>
</tr>
<tr id="row44646789171639"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p21468736171710"><a name="p21468736171710"></a><a name="p21468736171710"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p61246065171710"><a name="p61246065171710"></a><a name="p61246065171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p7274972172418"><a name="p7274972172418"></a><a name="p7274972172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p25100359152023"><a name="p25100359152023"></a><a name="p25100359152023"></a>Specifies the image name. Exact matching is used. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
</td>
</tr>
<tr id="row29378995171639"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p22241787171710"><a name="p22241787171710"></a><a name="p22241787171710"></a>container_format</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p56754321171710"><a name="p56754321171710"></a><a name="p56754321171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p31034804172418"><a name="p31034804172418"></a><a name="p31034804172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p62817831172421"><a name="p62817831172421"></a><a name="p62817831172421"></a>Specifies the container type. The default value is <strong id="b1812020615814"><a name="b1812020615814"></a><a name="b1812020615814"></a>bare</strong>.</p>
</td>
</tr>
<tr id="row41290451171646"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p3457793171710"><a name="p3457793171710"></a><a name="p3457793171710"></a>disk_format</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p11645813171710"><a name="p11645813171710"></a><a name="p11645813171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p19611874172418"><a name="p19611874172418"></a><a name="p19611874172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p25954213172421"><a name="p25954213172421"></a><a name="p25954213172421"></a>Specifies the image format. The value can be <strong id="b186984524615"><a name="b186984524615"></a><a name="b186984524615"></a>vhd</strong>, <strong id="b8423527069750"><a name="b8423527069750"></a><a name="b8423527069750"></a>raw</strong>, <strong id="b842352706172914"><a name="b842352706172914"></a><a name="b842352706172914"></a>zvhd</strong>, or <strong id="b8423527069758"><a name="b8423527069758"></a><a name="b8423527069758"></a>qcow2</strong>. The default value is <strong id="b842352706165234"><a name="b842352706165234"></a><a name="b842352706165234"></a>vhd</strong>.</p>
</td>
</tr>
<tr id="row30993478171646"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p9133289171710"><a name="p9133289171710"></a><a name="p9133289171710"></a>min_ram</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p1598950171710"><a name="p1598950171710"></a><a name="p1598950171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p29186361172418"><a name="p29186361172418"></a><a name="p29186361172418"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p63030551172421"><a name="p63030551172421"></a><a name="p63030551172421"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the <span id="text18177164412819"><a name="text18177164412819"></a><a name="text18177164412819"></a></span><span id="text101771044132814"><a name="text101771044132814"></a><a name="text101771044132814"></a>ECS</span> specifications. Generally, the value is <strong id="b18178204410289"><a name="b18178204410289"></a><a name="b18178204410289"></a>0</strong>.</p>
</td>
</tr>
<tr id="row4294549416037"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p5603301516037"><a name="p5603301516037"></a><a name="p5603301516037"></a>min_disk</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p4238040516037"><a name="p4238040516037"></a><a name="p4238040516037"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p1026079116037"><a name="p1026079116037"></a><a name="p1026079116037"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p33012089153426"><a name="p33012089153426"></a><a name="p33012089153426"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
</td>
</tr>
<tr id="row2123326171646"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p61378322171710"><a name="p61378322171710"></a><a name="p61378322171710"></a>__os_bit</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p5588210171710"><a name="p5588210171710"></a><a name="p5588210171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p20135377172418"><a name="p20135377172418"></a><a name="p20135377172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p46808977172421"><a name="p46808977172421"></a><a name="p46808977172421"></a>Specifies the OS architecture, 32 bit or 64 bit.</p>
</td>
</tr>
<tr id="row44306200171658"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p3969636171710"><a name="p3969636171710"></a><a name="p3969636171710"></a>__platform</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p53105072171710"><a name="p53105072171710"></a><a name="p53105072171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p10760011172418"><a name="p10760011172418"></a><a name="p10760011172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p2485190202218"><a name="p2485190202218"></a><a name="p2485190202218"></a>Specifies the image platform type. The value can be <strong id="b775384764619"><a name="b775384764619"></a><a name="b775384764619"></a>Windows</strong>, <strong id="b3754647114613"><a name="b3754647114613"></a><a name="b3754647114613"></a>Ubuntu</strong>, <strong id="b375454794616"><a name="b375454794616"></a><a name="b375454794616"></a>RedHat</strong>, <strong id="b47551647194615"><a name="b47551647194615"></a><a name="b47551647194615"></a>SUSE</strong>, <strong id="b1075514784617"><a name="b1075514784617"></a><a name="b1075514784617"></a>CentOS</strong>, <strong id="b147562476465"><a name="b147562476465"></a><a name="b147562476465"></a>Debian</strong>, <strong id="b18756124714467"><a name="b18756124714467"></a><a name="b18756124714467"></a>OpenSUSE</strong>, <strong id="b375710478467"><a name="b375710478467"></a><a name="b375710478467"></a>Oracle Linux</strong>, <strong id="b157571047134618"><a name="b157571047134618"></a><a name="b157571047134618"></a>Fedora</strong>, <strong id="b37581947134618"><a name="b37581947134618"></a><a name="b37581947134618"></a>Other</strong>, <strong id="b67581476464"><a name="b67581476464"></a><a name="b67581476464"></a>CoreOS</strong>, or <strong id="b2075910472462"><a name="b2075910472462"></a><a name="b2075910472462"></a>EulerOS</strong>.</p>
</td>
</tr>
<tr id="row9909482171658"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p5556492171710"><a name="p5556492171710"></a><a name="p5556492171710"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p47422720171710"><a name="p47422720171710"></a><a name="p47422720171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p5646864172418"><a name="p5646864172418"></a><a name="p5646864172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p27827411172421"><a name="p27827411172421"></a><a name="p27827411172421"></a>Specifies the start number from which images are queried. The value is the image ID.</p>
</td>
</tr>
<tr id="row12166148171658"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p12628035171710"><a name="p12628035171710"></a><a name="p12628035171710"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p16237895171710"><a name="p16237895171710"></a><a name="p16237895171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p1378961172418"><a name="p1378961172418"></a><a name="p1378961172418"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p19305703172421"><a name="p19305703172421"></a><a name="p19305703172421"></a>Specifies the number of images to be queried. The value is an integer. By default, 25 images can be queried.</p>
</td>
</tr>
<tr id="row15101772171658"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p47145990171710"><a name="p47145990171710"></a><a name="p47145990171710"></a>sort_key</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p60728885171710"><a name="p60728885171710"></a><a name="p60728885171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p11895688172418"><a name="p11895688172418"></a><a name="p11895688172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p48105504172421"><a name="p48105504172421"></a><a name="p48105504172421"></a>Specifies the field for sorting the query results. The value can be an attribute of the image: <strong id="b4906134934613"><a name="b4906134934613"></a><a name="b4906134934613"></a>name</strong>, <strong id="b13906649184613"><a name="b13906649184613"></a><a name="b13906649184613"></a>container_format</strong>, <strong id="b17907849164613"><a name="b17907849164613"></a><a name="b17907849164613"></a>disk_format</strong>, <strong id="b10907149114615"><a name="b10907149114615"></a><a name="b10907149114615"></a>status</strong>, <strong id="b49081349134614"><a name="b49081349134614"></a><a name="b49081349134614"></a>id</strong>, <strong id="b6909949164620"><a name="b6909949164620"></a><a name="b6909949164620"></a>size</strong>, or <strong id="b69091449154615"><a name="b69091449154615"></a><a name="b69091449154615"></a>create_at</strong>. The default value is <strong id="b1091024918462"><a name="b1091024918462"></a><a name="b1091024918462"></a>create_at</strong>.</p>
</td>
</tr>
<tr id="row50874737171658"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p17835230171710"><a name="p17835230171710"></a><a name="p17835230171710"></a>sort_dir</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p35367554171710"><a name="p35367554171710"></a><a name="p35367554171710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p6026804172418"><a name="p6026804172418"></a><a name="p6026804172418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p38085944172421"><a name="p38085944172421"></a><a name="p38085944172421"></a>Specifies whether the query results are sorted in ascending or descending order. Its value can be <strong id="b21722049143851"><a name="b21722049143851"></a><a name="b21722049143851"></a>desc </strong>(default) or<strong id="b61280713143851"><a name="b61280713143851"></a><a name="b61280713143851"></a> asc</strong>. This parameter is used together with parameter <strong id="b37017385142847"><a name="b37017385142847"></a><a name="b37017385142847"></a>sort_key</strong>. The default value is <strong id="b842352706192943"><a name="b842352706192943"></a><a name="b842352706192943"></a>desc</strong>.</p>
</td>
</tr>
<tr id="row25115385114914"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p21080313114914"><a name="p21080313114914"></a><a name="p21080313114914"></a>__os_type</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p49589429114924"><a name="p49589429114924"></a><a name="p49589429114924"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p63675406114914"><a name="p63675406114914"></a><a name="p63675406114914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p57434227114914"><a name="p57434227114914"></a><a name="p57434227114914"></a>Specifies the image OS type. The value can be <strong id="b842352706105959"><a name="b842352706105959"></a><a name="b842352706105959"></a>Linux</strong>, <strong id="b8423527061104"><a name="b8423527061104"></a><a name="b8423527061104"></a>Windows</strong>, or <strong id="b84235270611011"><a name="b84235270611011"></a><a name="b84235270611011"></a>Other</strong>.</p>
</td>
</tr>
<tr id="row4436325311929"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p3665371811929"><a name="p3665371811929"></a><a name="p3665371811929"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p1616121311929"><a name="p1616121311929"></a><a name="p1616121311929"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p3398983911929"><a name="p3398983911929"></a><a name="p3398983911929"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p1525288141944"><a name="p1525288141944"></a><a name="p1525288141944"></a>Specifies a tag added to an image. Tags can be used as a filter to query images.</p>
<div class="note" id="note10170152764913"><a name="note10170152764913"></a><a name="note10170152764913"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p517019273499"><a name="p517019273499"></a><a name="p517019273499"></a>The tagging function has been upgraded. If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key=Value". For example, an existing tag is <strong id="b84235270610509"><a name="b84235270610509"></a><a name="b84235270610509"></a>a.b</strong>. After the tag function upgrade, query the tag using "tag=a=b".</p>
</div></div>
</td>
</tr>
<tr id="row43430748111132"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p28229739111132"><a name="p28229739111132"></a><a name="p28229739111132"></a>member_status</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p4907555111132"><a name="p4907555111132"></a><a name="p4907555111132"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p61967659111132"><a name="p61967659111132"></a><a name="p61967659111132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p53324459111132"><a name="p53324459111132"></a><a name="p53324459111132"></a>Specifies the member status. The value can be <strong id="b8423527069592"><a name="b8423527069592"></a><a name="b8423527069592"></a>accepted</strong>, <strong id="b8423527069596"><a name="b8423527069596"></a><a name="b8423527069596"></a>rejected</strong>, or <strong id="b84235270695911"><a name="b84235270695911"></a><a name="b84235270695911"></a>pending</strong>. <strong id="b203788251295959"><a name="b203788251295959"></a><a name="b203788251295959"></a>accepted</strong>: indicates that the shared image is accepted. <strong id="b137807831210025"><a name="b137807831210025"></a><a name="b137807831210025"></a>rejected</strong> indicates that the image shared by others is rejected. <strong id="b5235343781010"><a name="b5235343781010"></a><a name="b5235343781010"></a>pending</strong> indicates that the image shared by others needs to be confirmed. To use this parameter, set <strong id="b84235270693449"><a name="b84235270693449"></a><a name="b84235270693449"></a>visibility</strong> to <strong id="b84235270693452"><a name="b84235270693452"></a><a name="b84235270693452"></a>shared</strong> during the query.</p>
</td>
</tr>
<tr id="row607872792117"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p2484690921449"><a name="p2484690921449"></a><a name="p2484690921449"></a>__support_kvm</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p6644261721449"><a name="p6644261721449"></a><a name="p6644261721449"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p1314289321449"><a name="p1314289321449"></a><a name="p1314289321449"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p5794144221449"><a name="p5794144221449"></a><a name="p5794144221449"></a>Specifies whether the image supports KVM. If yes, the value is <strong id="b842352706174145"><a name="b842352706174145"></a><a name="b842352706174145"></a>true</strong>. Otherwise, this attribute is not required.</p>
</td>
</tr>
<tr id="row2242102211315"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p2101233521141"><a name="p2101233521141"></a><a name="p2101233521141"></a>__support_xen</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p2427761221141"><a name="p2427761221141"></a><a name="p2427761221141"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p2032954521141"><a name="p2032954521141"></a><a name="p2032954521141"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p3608043021141"><a name="p3608043021141"></a><a name="p3608043021141"></a>Specifies whether the image supports Xen. If yes, the value is <strong id="b40128715692258"><a name="b40128715692258"></a><a name="b40128715692258"></a>true</strong>. Otherwise, this attribute is not required.</p>
</td>
</tr>
<tr id="row14291359211318"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p16614938211414"><a name="p16614938211414"></a><a name="p16614938211414"></a>__support_largememory</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p3632756211414"><a name="p3632756211414"></a><a name="p3632756211414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p25817810211414"><a name="p25817810211414"></a><a name="p25817810211414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p10867869211414"><a name="p10867869211414"></a><a name="p10867869211414"></a>Specifies whether the image supports large-memory ECSs. If the image supports large-memory ECSs, the value is <strong id="b842352706174145_1"><a name="b842352706174145_1"></a><a name="b842352706174145_1"></a>true</strong>. Otherwise, this attribute is not required. For details about the image OSs supported by large-memory ECSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
</td>
</tr>
<tr id="row52211464211322"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p6452067211434"><a name="p6452067211434"></a><a name="p6452067211434"></a>__support_diskintensive</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p52855412211434"><a name="p52855412211434"></a><a name="p52855412211434"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p53429945211434"><a name="p53429945211434"></a><a name="p53429945211434"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p16679154915811"><a name="p16679154915811"></a><a name="p16679154915811"></a>Specifies whether the image supports disk-intensive ECSs. If the image supports disk-intensive ECSs, the value is <strong id="b842352706174145_2"><a name="b842352706174145_2"></a><a name="b842352706174145_2"></a>true</strong>. Otherwise, this attribute is not required. For details about the image OSs supported by disk-intensive ECSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
</td>
</tr>
<tr id="row13134583211325"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p35006343211449"><a name="p35006343211449"></a><a name="p35006343211449"></a>__support_highperformance</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p18255910211449"><a name="p18255910211449"></a><a name="p18255910211449"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p2333756211449"><a name="p2333756211449"></a><a name="p2333756211449"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p23586946211449"><a name="p23586946211449"></a><a name="p23586946211449"></a>Specifies whether the image supports high-performance ECSs. If the image supports high-performance ECSs, the value is <strong id="b842352706174145_3"><a name="b842352706174145_3"></a><a name="b842352706174145_3"></a>true</strong>. Otherwise, this attribute is not required. For details about the image OSs supported by high-performance computing ECSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
</td>
</tr>
<tr id="row66912955211328"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p17122048211459"><a name="p17122048211459"></a><a name="p17122048211459"></a>__support_xen_gpu_type</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p44708641211459"><a name="p44708641211459"></a><a name="p44708641211459"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p64630134211459"><a name="p64630134211459"></a><a name="p64630134211459"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p113841114719"><a name="p113841114719"></a><a name="p113841114719"></a>Specifies whether the image supports GPU-optimized ECSs on the Xen platform. For the OSs supported by GPU-accelerated ECSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>. If the image does not support GPU-optimized ECSs on the Xen platform, this attribute is not required. This attribute cannot co-exist with <strong id="b842352706175423"><a name="b842352706175423"></a><a name="b842352706175423"></a>__support_xen</strong> and <strong id="b842352706175430"><a name="b842352706175430"></a><a name="b842352706175430"></a>__support_kvm</strong>.</p>
</td>
</tr>
<tr id="row550534121153"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p17764802211519"><a name="p17764802211519"></a><a name="p17764802211519"></a>__support_kvm_gpu_type</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p29662897211519"><a name="p29662897211519"></a><a name="p29662897211519"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p53884489211519"><a name="p53884489211519"></a><a name="p53884489211519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p23107258211519"><a name="p23107258211519"></a><a name="p23107258211519"></a>Specifies whether the image supports GPU-optimized ECSs on the KVM platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the KVM platform, this attribute is not required. This attribute cannot co-exist with <strong id="b842352706175423_1"><a name="b842352706175423_1"></a><a name="b842352706175423_1"></a>__support_xen</strong> and <strong id="b842352706175430_1"><a name="b842352706175430_1"></a><a name="b842352706175430_1"></a>__support_kvm</strong>.</p>
</td>
</tr>
<tr id="row48915660211510"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p866834211519"><a name="p866834211519"></a><a name="p866834211519"></a>__support_xen_hana</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p3104731211519"><a name="p3104731211519"></a><a name="p3104731211519"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p50156693211519"><a name="p50156693211519"></a><a name="p50156693211519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p069717225820"><a name="p069717225820"></a><a name="p069717225820"></a>Specifies whether the image supports HANA ECSs on the Xen platform. If yes, the value is <strong id="b1066553282174316"><a name="b1066553282174316"></a><a name="b1066553282174316"></a>true</strong>. Otherwise, this attribute is not required.</p>
<p id="p56971922588"><a name="p56971922588"></a><a name="p56971922588"></a>This attribute cannot co-exist with <strong id="b842352706175423_2"><a name="b842352706175423_2"></a><a name="b842352706175423_2"></a>__support_xen</strong> and <strong id="b842352706175430_2"><a name="b842352706175430_2"></a><a name="b842352706175430_2"></a>__support_kvm</strong>.</p>
</td>
</tr>
<tr id="row135722301704"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p1677823711015"><a name="p1677823711015"></a><a name="p1677823711015"></a>__support_kvm_infiniband</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p147787374015"><a name="p147787374015"></a><a name="p147787374015"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p028830316"><a name="p028830316"></a><a name="p028830316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p18515175113010"><a name="p18515175113010"></a><a name="p18515175113010"></a>Specifies whether the image supports ECSs with the InfiniBand NIC on the KVM platform. If yes, the value is <strong id="b2040161919154726"><a name="b2040161919154726"></a><a name="b2040161919154726"></a>true</strong>. Otherwise, this attribute is not required.</p>
<p id="p155169515013"><a name="p155169515013"></a><a name="p155169515013"></a>This attribute cannot co-exist with <strong id="b842352706175423_3"><a name="b842352706175423_3"></a><a name="b842352706175423_3"></a>__support_xen</strong>.</p>
</td>
</tr>
<tr id="row932118481247"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p14187217143019"><a name="p14187217143019"></a><a name="p14187217143019"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p8313953143019"><a name="p8313953143019"></a><a name="p8313953143019"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p2341610143019"><a name="p2341610143019"></a><a name="p2341610143019"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p55452691143019"><a name="p55452691143019"></a><a name="p55452691143019"></a>Specifies the time when the image was created. Images can be queried by time. The value is in the format of <em id="i842352697105348"><a name="i842352697105348"></a><a name="i842352697105348"></a>Operator:UTC time</em>.</p>
<p id="p32947284143515"><a name="p32947284143515"></a><a name="p32947284143515"></a>The following operators are supported:</p>
<a name="ul638941319348"></a><a name="ul638941319348"></a><ul id="ul638941319348"><li>gt: greater than</li><li>gte: greater than or equal to</li><li>lt: less than</li><li>lte: less than or equal to</li><li>eq: equal to</li><li>neq: not equal to</li></ul>
<p id="p18028286143153"><a name="p18028286143153"></a><a name="p18028286143153"></a>The time format is <em id="i842352697105633"><a name="i842352697105633"></a><a name="i842352697105633"></a>yyyy-MM-ddThh:mm:ssZ</em> or <em id="i842352697105637"><a name="i842352697105637"></a><a name="i842352697105637"></a>yyyy-MM-dd hh:mm:ss</em>.</p>
<p id="p47377274144446"><a name="p47377274144446"></a><a name="p47377274144446"></a>For example, to query images whose creation time is earlier than Oct 28, 2018 10:00:00, set the value of <strong id="b15991133173517"><a name="b15991133173517"></a><a name="b15991133173517"></a>created_at</strong> to <strong id="b158321541174811"><a name="b158321541174811"></a><a name="b158321541174811"></a>gt:2018-10-28T10:00:00Z</strong>.</p>
</td>
</tr>
<tr id="row82121252162418"><td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.2.5.1.1 "><p id="p5543103144620"><a name="p5543103144620"></a><a name="p5543103144620"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.5.1.2 "><p id="p46338199144620"><a name="p46338199144620"></a><a name="p46338199144620"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.840000000000002%" headers="mcps1.2.5.1.3 "><p id="p62406652144620"><a name="p62406652144620"></a><a name="p62406652144620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.74%" headers="mcps1.2.5.1.4 "><p id="p52031456144646"><a name="p52031456144646"></a><a name="p52031456144646"></a>Specifies the time when the image was modified. Images can be queried by time. The value is in the format of <em id="i842352697105348_1"><a name="i842352697105348_1"></a><a name="i842352697105348_1"></a>Operator:UTC time</em>.</p>
<p id="p65629927144646"><a name="p65629927144646"></a><a name="p65629927144646"></a>The following operators are supported:</p>
<a name="ul207912567349"></a><a name="ul207912567349"></a><ul id="ul207912567349"><li>gt: greater than</li><li>gte: greater than or equal to</li><li>lt: less than</li><li>lte: less than or equal to</li><li>eq: equal to</li><li>neq: not equal to</li></ul>
<p id="p37800263144646"><a name="p37800263144646"></a><a name="p37800263144646"></a>The time format is <em id="i842352697105633_1"><a name="i842352697105633_1"></a><a name="i842352697105633_1"></a>yyyy-MM-ddThh:mm:ssZ</em> or <em id="i842352697105637_1"><a name="i842352697105637_1"></a><a name="i842352697105637_1"></a>yyyy-MM-dd hh:mm:ss</em>.</p>
<p id="p4658051144646"><a name="p4658051144646"></a><a name="p4658051144646"></a>For example, to query images whose creation time is earlier than Oct 28, 2018 10:00:00, set the value of <strong id="b3138203725016"><a name="b3138203725016"></a><a name="b3138203725016"></a>updated_at</strong> to <strong id="b71481837105014"><a name="b71481837105014"></a><a name="b71481837105014"></a>gt:2018-10-28T10:00:00Z</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Common Query Methods<a name="section105891407155"></a>

-   Public images

    GET /v2/images?\_\_imagetype=gold&visibility=public&protected=true

-   Private images

    GET /v2/images?owner=\{project\_id\}

-   Available shared images

    GET /v2/images?member\_status=accepted&visibility=shared&\_\_imagetype=shared

-   Rejected images

    GET /v2/images?member\_status=rejected&visibility=shared&\_\_imagetype=shared

-   Unaccepted images

    GET /v2/images?member\_status=pending&visibility=shared&\_\_imagetype=shared


## Request<a name="section52453505"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v2/images
    ```


## Response<a name="section10077261173340"></a>

-   Response parameters

    <a name="table13195036194916"></a>
    <table><thead align="left"><tr id="row60394066194916"><th class="cellrowborder" valign="top" width="38.550000000000004%" id="mcps1.1.4.1.1"><p id="p60081139194916"><a name="p60081139194916"></a><a name="p60081139194916"></a><strong id="b24725868162658_1"><a name="b24725868162658_1"></a><a name="b24725868162658_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.27%" id="mcps1.1.4.1.2"><p id="p61997487194916"><a name="p61997487194916"></a><a name="p61997487194916"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.18%" id="mcps1.1.4.1.3"><p id="p55740570194916"><a name="p55740570194916"></a><a name="p55740570194916"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18692334194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p37684049194916"><a name="p37684049194916"></a><a name="p37684049194916"></a>__isregistered</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p15996779194916"><a name="p15996779194916"></a><a name="p15996779194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p20670704194916"><a name="p20670704194916"></a><a name="p20670704194916"></a>Specifies whether the image is available. The value can be <strong id="b84235270616222_1"><a name="b84235270616222_1"></a><a name="b84235270616222_1"></a>true</strong>. The value is <strong id="b2049464823162253_1"><a name="b2049464823162253_1"></a><a name="b2049464823162253_1"></a>true</strong> for all extension APIs by default. Common users can query only the images for which the value of this parameter is <strong id="b846915150162332_1"><a name="b846915150162332_1"></a><a name="b846915150162332_1"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row51818614194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p36558171194916"><a name="p36558171194916"></a><a name="p36558171194916"></a>__imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p11081443194916"><a name="p11081443194916"></a><a name="p11081443194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p25181653194916"><a name="p25181653194916"></a><a name="p25181653194916"></a>Specifies the image type. The following types are supported:</p>
    <a name="ul25308291194916"></a><a name="ul25308291194916"></a><ul id="ul25308291194916"><li>Public image: The value is <strong id="b842352706163515_1"><a name="b842352706163515_1"></a><a name="b842352706163515_1"></a>gold</strong>.</li><li>Private image: The value is <strong id="b1762610292163524_1"><a name="b1762610292163524_1"></a><a name="b1762610292163524_1"></a>private</strong>.</li><li>Shared image: The value is <strong id="b298092137163545_1"><a name="b298092137163545_1"></a><a name="b298092137163545_1"></a>shared</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row20369060194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p39281165194916"><a name="p39281165194916"></a><a name="p39281165194916"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p25691866194916"><a name="p25691866194916"></a><a name="p25691866194916"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p666381194916"><a name="p666381194916"></a><a name="p666381194916"></a>Specifies whether the image is protected. Set it to <strong id="b48612739142847_1_1"><a name="b48612739142847_1_1"></a><a name="b48612739142847_1_1"></a>true</strong> when you query public images. This parameter is optional when you query private images.</p>
    </td>
    </tr>
    <tr id="row5997430194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p16029804194916"><a name="p16029804194916"></a><a name="p16029804194916"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p11960319194916"><a name="p11960319194916"></a><a name="p11960319194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p15545818173013"><a name="p15545818173013"></a><a name="p15545818173013"></a>Specifies whether the image is available to other tenants. The value can be one of the following:</p>
    <a name="ul2480149153015"></a><a name="ul2480149153015"></a><ul id="ul2480149153015"><li><strong id="b164525621714"><a name="b164525621714"></a><a name="b164525621714"></a>public</strong>: public image</li><li><strong id="b1442917102173"><a name="b1442917102173"></a><a name="b1442917102173"></a>private</strong>: private image</li><li><strong id="b995714115175"><a name="b995714115175"></a><a name="b995714115175"></a>shared</strong>: shared image</li></ul>
    </td>
    </tr>
    <tr id="row62029643194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p58345161194916"><a name="p58345161194916"></a><a name="p58345161194916"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p13641590194916"><a name="p13641590194916"></a><a name="p13641590194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p31226997194916"><a name="p31226997194916"></a><a name="p31226997194916"></a>Specifies the tenant to which the image belongs.</p>
    </td>
    </tr>
    <tr id="row12607524194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p14576499194916"><a name="p14576499194916"></a><a name="p14576499194916"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p6281007194916"><a name="p6281007194916"></a><a name="p6281007194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p38999531194916"><a name="p38999531194916"></a><a name="p38999531194916"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="row15451466194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p43609220194916"><a name="p43609220194916"></a><a name="p43609220194916"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p35010019194916"><a name="p35010019194916"></a><a name="p35010019194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p17239254194916"><a name="p17239254194916"></a><a name="p17239254194916"></a>Specifies the image status. The value can be one of the following:</p>
    <a name="ul20935566194916"></a><a name="ul20935566194916"></a><ul id="ul20935566194916"><li><strong id="b842352706103333_1"><a name="b842352706103333_1"></a><a name="b842352706103333_1"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="b842352706104325_1"><a name="b842352706104325_1"></a><a name="b842352706104325_1"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="b842352706104450_1"><a name="b842352706104450_1"></a><a name="b842352706104450_1"></a>deleted</strong>: indicates that the image has been deleted. </li><li><strong id="b842352706104518_1"><a name="b842352706104518_1"></a><a name="b842352706104518_1"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="b842352706104558_1"><a name="b842352706104558_1"></a><a name="b842352706104558_1"></a>active</strong>: indicates that the image is available for use. </li></ul>
    </td>
    </tr>
    <tr id="row39884627194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p9429320194916"><a name="p9429320194916"></a><a name="p9429320194916"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p58506224194916"><a name="p58506224194916"></a><a name="p58506224194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p41383666194916"><a name="p41383666194916"></a><a name="p41383666194916"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row15180307194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p21645353194916"><a name="p21645353194916"></a><a name="p21645353194916"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p12805641194916"><a name="p12805641194916"></a><a name="p12805641194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p30624037194916"><a name="p30624037194916"></a><a name="p30624037194916"></a>Specifies the container type.</p>
    </td>
    </tr>
    <tr id="row7180877194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p44780194194916"><a name="p44780194194916"></a><a name="p44780194194916"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p251278194916"><a name="p251278194916"></a><a name="p251278194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p20353524194916"><a name="p20353524194916"></a><a name="p20353524194916"></a>Specifies the image format. The value can be <strong id="b1642017344484"><a name="b1642017344484"></a><a name="b1642017344484"></a>vhd</strong>, <strong id="b11421113464814"><a name="b11421113464814"></a><a name="b11421113464814"></a>raw</strong>, <strong id="b12421034174814"><a name="b12421034174814"></a><a name="b12421034174814"></a>zvhd</strong>, or <strong id="b13422163412483"><a name="b13422163412483"></a><a name="b13422163412483"></a>qcow2</strong>. The default value is <strong id="b842352706165234_1"><a name="b842352706165234_1"></a><a name="b842352706165234_1"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="row48963992194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p6660406194916"><a name="p6660406194916"></a><a name="p6660406194916"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p11056800194916"><a name="p11056800194916"></a><a name="p11056800194916"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p23185596194916"><a name="p23185596194916"></a><a name="p23185596194916"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the <span id="text168511714174719"><a name="text168511714174719"></a><a name="text168511714174719"></a></span><span id="text1985191412474"><a name="text1985191412474"></a><a name="text1985191412474"></a>ECS</span> specifications. Generally, the value is <strong id="b5851181412473"><a name="b5851181412473"></a><a name="b5851181412473"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row7343772194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p57974621194916"><a name="p57974621194916"></a><a name="p57974621194916"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p65558873194916"><a name="p65558873194916"></a><a name="p65558873194916"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p8668516194916"><a name="p8668516194916"></a><a name="p8668516194916"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
    </td>
    </tr>
    <tr id="row11115416194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p27933499194916"><a name="p27933499194916"></a><a name="p27933499194916"></a>__os_bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p64492127194916"><a name="p64492127194916"></a><a name="p64492127194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p56479792194916"><a name="p56479792194916"></a><a name="p56479792194916"></a>Specifies the OS architecture, 32 bit or 64 bit.</p>
    </td>
    </tr>
    <tr id="row38556080194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p36034782194916"><a name="p36034782194916"></a><a name="p36034782194916"></a>__platform</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p66792165194916"><a name="p66792165194916"></a><a name="p66792165194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p608798220230"><a name="p608798220230"></a><a name="p608798220230"></a>Specifies the image platform type. The value can be <strong id="b13114336144815"><a name="b13114336144815"></a><a name="b13114336144815"></a>Windows</strong>, <strong id="b6115143618488"><a name="b6115143618488"></a><a name="b6115143618488"></a>Ubuntu</strong>, <strong id="b1711517365484"><a name="b1711517365484"></a><a name="b1711517365484"></a>RedHat</strong>, <strong id="b10116136184816"><a name="b10116136184816"></a><a name="b10116136184816"></a>SUSE</strong>, <strong id="b1011673634813"><a name="b1011673634813"></a><a name="b1011673634813"></a>CentOS</strong>, <strong id="b11161364488"><a name="b11161364488"></a><a name="b11161364488"></a>Debian</strong>, <strong id="b1911716364486"><a name="b1911716364486"></a><a name="b1911716364486"></a>OpenSUSE</strong>, <strong id="b2117183604819"><a name="b2117183604819"></a><a name="b2117183604819"></a>Oracle Linux</strong>, <strong id="b2011893624818"><a name="b2011893624818"></a><a name="b2011893624818"></a>Fedora</strong>, <strong id="b1311803614817"><a name="b1311803614817"></a><a name="b1311803614817"></a>Other</strong>, <strong id="b1311843613487"><a name="b1311843613487"></a><a name="b1311843613487"></a>CoreOS</strong>, or <strong id="b11119736164819"><a name="b11119736164819"></a><a name="b11119736164819"></a>EulerOS</strong>.</p>
    </td>
    </tr>
    <tr id="row37562102194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p22631450194916"><a name="p22631450194916"></a><a name="p22631450194916"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p40139575194916"><a name="p40139575194916"></a><a name="p40139575194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p30080128194916"><a name="p30080128194916"></a><a name="p30080128194916"></a>Specifies the start number from which images are queried. The value is the image ID.</p>
    </td>
    </tr>
    <tr id="row2285700194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p50923991194916"><a name="p50923991194916"></a><a name="p50923991194916"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p44380894194916"><a name="p44380894194916"></a><a name="p44380894194916"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p38082658194916"><a name="p38082658194916"></a><a name="p38082658194916"></a>Specifies the number of images to be queried. The value is an integer. By default, 25 images can be queried.</p>
    </td>
    </tr>
    <tr id="row7199609194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p46297477194916"><a name="p46297477194916"></a><a name="p46297477194916"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p23034091194916"><a name="p23034091194916"></a><a name="p23034091194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p53822101194916"><a name="p53822101194916"></a><a name="p53822101194916"></a>Specifies the field for sorting the query results. The value can be an attribute of the image: <strong id="b37518521645"><a name="b37518521645"></a><a name="b37518521645"></a>name, container_format, disk_format, status, id, </strong>or <strong id="b4095755416348"><a name="b4095755416348"></a><a name="b4095755416348"></a>size</strong>. The default value is <strong id="b3307366916348"><a name="b3307366916348"></a><a name="b3307366916348"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row14636864194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p44735327194916"><a name="p44735327194916"></a><a name="p44735327194916"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p41423416194916"><a name="p41423416194916"></a><a name="p41423416194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p66962369194916"><a name="p66962369194916"></a><a name="p66962369194916"></a>Specifies whether the query results are sorted in ascending or descending order. Its value can be <strong id="b21722049143851_1"><a name="b21722049143851_1"></a><a name="b21722049143851_1"></a>desc </strong>(default) or<strong id="b61280713143851_1"><a name="b61280713143851_1"></a><a name="b61280713143851_1"></a> asc</strong>. This parameter is used together with parameter <strong id="b37017385142847_1"><a name="b37017385142847_1"></a><a name="b37017385142847_1"></a>sort_key</strong>. The default value is <strong id="b93108807219308"><a name="b93108807219308"></a><a name="b93108807219308"></a>desc</strong>.</p>
    </td>
    </tr>
    <tr id="row65790409194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p27422885194916"><a name="p27422885194916"></a><a name="p27422885194916"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p2689444194916"><a name="p2689444194916"></a><a name="p2689444194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p16518422194916"><a name="p16518422194916"></a><a name="p16518422194916"></a>Specifies the image OS type. The value can be <strong id="b371084484818"><a name="b371084484818"></a><a name="b371084484818"></a>Linux</strong>, <strong id="b17710194434815"><a name="b17710194434815"></a><a name="b17710194434815"></a>Windows</strong>, or <strong id="b137117444482"><a name="b137117444482"></a><a name="b137117444482"></a>Other</strong>.</p>
    </td>
    </tr>
    <tr id="row14448077194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p29443552194916"><a name="p29443552194916"></a><a name="p29443552194916"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p39840346194916"><a name="p39840346194916"></a><a name="p39840346194916"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p5842575194916"><a name="p5842575194916"></a><a name="p5842575194916"></a>Specifies a tag added to an image. Tags can be used as a filter to query images.</p>
    </td>
    </tr>
    <tr id="row52583181194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p31379234194916"><a name="p31379234194916"></a><a name="p31379234194916"></a>member_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p56269834194916"><a name="p56269834194916"></a><a name="p56269834194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p61562668194916"><a name="p61562668194916"></a><a name="p61562668194916"></a>Specifies the member status. The value can be <strong id="b8423527069592_1"><a name="b8423527069592_1"></a><a name="b8423527069592_1"></a>accepted</strong>, <strong id="b8423527069596_1"><a name="b8423527069596_1"></a><a name="b8423527069596_1"></a>rejected</strong>, or <strong id="b84235270695911_1"><a name="b84235270695911_1"></a><a name="b84235270695911_1"></a>pending</strong>. <strong id="b203788251295959_1"><a name="b203788251295959_1"></a><a name="b203788251295959_1"></a>accepted</strong>: indicates that the shared image is accepted. <strong id="b137807831210025_1"><a name="b137807831210025_1"></a><a name="b137807831210025_1"></a>rejected</strong> indicates that the image shared by others is rejected. <strong id="b5235343781010_1"><a name="b5235343781010_1"></a><a name="b5235343781010_1"></a>pending</strong> indicates that the image shared by others needs to be confirmed. To use this parameter, set <strong id="b84235270693449_1"><a name="b84235270693449_1"></a><a name="b84235270693449_1"></a>visibility</strong> to <strong id="b84235270693452_1"><a name="b84235270693452_1"></a><a name="b84235270693452_1"></a>shared</strong> during the query.</p>
    </td>
    </tr>
    <tr id="row17193106194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p50464322194916"><a name="p50464322194916"></a><a name="p50464322194916"></a>__support_kvm</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p48394540194916"><a name="p48394540194916"></a><a name="p48394540194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p27643702194916"><a name="p27643702194916"></a><a name="p27643702194916"></a>Specifies whether the image supports KVM. If yes, the value is <strong id="b842352706174145_4"><a name="b842352706174145_4"></a><a name="b842352706174145_4"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row47466733194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p19600163194916"><a name="p19600163194916"></a><a name="p19600163194916"></a>__support_xen</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p16086851194916"><a name="p16086851194916"></a><a name="p16086851194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p27966591194916"><a name="p27966591194916"></a><a name="p27966591194916"></a>Specifies whether the image supports Xen. If yes, the value is <strong id="b40128715692258_1"><a name="b40128715692258_1"></a><a name="b40128715692258_1"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row50372727194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p53659116194916"><a name="p53659116194916"></a><a name="p53659116194916"></a>__support_largememory</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p4364568194916"><a name="p4364568194916"></a><a name="p4364568194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p17985694194916"><a name="p17985694194916"></a><a name="p17985694194916"></a>Specifies whether the image supports large-memory ECSs. If the image supports large-memory ECSs, the value is <strong id="b842352706174145_5"><a name="b842352706174145_5"></a><a name="b842352706174145_5"></a>true</strong>. Otherwise, this attribute is not required. For details about the image OSs supported by large-memory ECSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row47555109194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p26758612194916"><a name="p26758612194916"></a><a name="p26758612194916"></a>__support_diskintensive</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p6470349194916"><a name="p6470349194916"></a><a name="p6470349194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p54336230194916"><a name="p54336230194916"></a><a name="p54336230194916"></a>Specifies whether the image supports disk-intensive ECSs. If the image supports disk-intensive ECSs, the value is <strong id="b842352706174145_6"><a name="b842352706174145_6"></a><a name="b842352706174145_6"></a>true</strong>. Otherwise, this attribute is not required. For details about the image OSs supported by disk-intensive ECSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row39158471194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p17719577194916"><a name="p17719577194916"></a><a name="p17719577194916"></a>__support_highperformance</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p29023139194916"><a name="p29023139194916"></a><a name="p29023139194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p2064082194916"><a name="p2064082194916"></a><a name="p2064082194916"></a>Specifies whether the image supports high-performance ECSs. If the image supports high-performance ECSs, the value is <strong id="b842352706174145_7"><a name="b842352706174145_7"></a><a name="b842352706174145_7"></a>true</strong>. Otherwise, this attribute is not required. For details about the image OSs supported by high-performance computing ECSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row32972949194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p53563221194916"><a name="p53563221194916"></a><a name="p53563221194916"></a>__support_xen_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p46282730194916"><a name="p46282730194916"></a><a name="p46282730194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p51460488194916"><a name="p51460488194916"></a><a name="p51460488194916"></a>Specifies whether the image supports GPU-optimized ECSs on the Xen platform. For the OSs supported by GPU-accelerated ECSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>. If the image does not support GPU-optimized ECSs on the Xen platform, this attribute is not required. This attribute cannot co-exist with <strong id="b842352706175423_4"><a name="b842352706175423_4"></a><a name="b842352706175423_4"></a>__support_xen</strong> and <strong id="b842352706175430_3"><a name="b842352706175430_3"></a><a name="b842352706175430_3"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row7573455194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p9470103194916"><a name="p9470103194916"></a><a name="p9470103194916"></a>__support_kvm_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p57647928194916"><a name="p57647928194916"></a><a name="p57647928194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p15191025194916"><a name="p15191025194916"></a><a name="p15191025194916"></a>Specifies whether the image supports GPU-optimized ECSs on the KVM platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the KVM platform, this attribute is not required. This attribute cannot co-exist with <strong id="b842352706175423_5"><a name="b842352706175423_5"></a><a name="b842352706175423_5"></a>__support_xen</strong> and <strong id="b842352706175430_4"><a name="b842352706175430_4"></a><a name="b842352706175430_4"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row22513498194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p11654048194916"><a name="p11654048194916"></a><a name="p11654048194916"></a>__support_xen_hana</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p25213664194916"><a name="p25213664194916"></a><a name="p25213664194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p29040940194916"><a name="p29040940194916"></a><a name="p29040940194916"></a>Specifies whether the image supports HANA ECSs on the Xen platform. If yes, the value is <strong id="b1066553282174316_1"><a name="b1066553282174316_1"></a><a name="b1066553282174316_1"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p60041868194916"><a name="p60041868194916"></a><a name="p60041868194916"></a>This attribute cannot co-exist with <strong id="b842352706175423_6"><a name="b842352706175423_6"></a><a name="b842352706175423_6"></a>__support_xen</strong> and <strong id="b842352706175430_5"><a name="b842352706175430_5"></a><a name="b842352706175430_5"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row31553169194916"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p5669919194916"><a name="p5669919194916"></a><a name="p5669919194916"></a>__support_kvm_infiniband</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p22029043194916"><a name="p22029043194916"></a><a name="p22029043194916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p39522058194916"><a name="p39522058194916"></a><a name="p39522058194916"></a>Specifies whether the image supports ECSs with the InfiniBand NIC on the KVM platform. If yes, the value is <strong id="b2040161919154726_1"><a name="b2040161919154726_1"></a><a name="b2040161919154726_1"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p20154205194916"><a name="p20154205194916"></a><a name="p20154205194916"></a>This attribute cannot co-exist with <strong id="b842352706175423_7"><a name="b842352706175423_7"></a><a name="b842352706175423_7"></a>__support_xen</strong>.</p>
    </td>
    </tr>
    <tr id="row1867223234610"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p1021161112333"><a name="p1021161112333"></a><a name="p1021161112333"></a>__root_origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p637311103320"><a name="p637311103320"></a><a name="p637311103320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p937411163318"><a name="p937411163318"></a><a name="p937411163318"></a>Indicates that the image is created from an external image file. Example value: <strong id="b842352706155810"><a name="b842352706155810"></a><a name="b842352706155810"></a>file</strong></p>
    </td>
    </tr>
    <tr id="row4531435114611"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p1152411163311"><a name="p1152411163311"></a><a name="p1152411163311"></a>__sequence_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p95251143318"><a name="p95251143318"></a><a name="p95251143318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p116891133317"><a name="p116891133317"></a><a name="p116891133317"></a>Specifies the <span id="text1516210342102"><a name="text1516210342102"></a><a name="text1516210342102"></a></span><span id="text416283412103"><a name="text416283412103"></a><a name="text416283412103"></a>ECS</span> system disk slot number corresponding to the image.</p>
    <p id="p468511113315"><a name="p468511113315"></a><a name="p468511113315"></a>Example value: <strong id="b842352706155810_1"><a name="b842352706155810_1"></a><a name="b842352706155810_1"></a>0</strong></p>
    </td>
    </tr>
    <tr id="row119872568501"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p31333900172519"><a name="p31333900172519"></a><a name="p31333900172519"></a>images</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p778421215514"><a name="p778421215514"></a><a name="p778421215514"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p154910205516"><a name="p154910205516"></a><a name="p154910205516"></a>Specifies the resource type.</p>
    </td>
    </tr>
    <tr id="row398710569507"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p31509198115122"><a name="p31509198115122"></a><a name="p31509198115122"></a>first</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p1978441285118"><a name="p1978441285118"></a><a name="p1978441285118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p10564152015112"><a name="p10564152015112"></a><a name="p10564152015112"></a>Specifies the URL of the first page of images.</p>
    </td>
    </tr>
    <tr id="row15987135611503"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p65807153115133"><a name="p65807153115133"></a><a name="p65807153115133"></a>next</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p19798812175111"><a name="p19798812175111"></a><a name="p19798812175111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p556472025120"><a name="p556472025120"></a><a name="p556472025120"></a>Specifies the URL of the next page of images. When the last page of images is queried, there is no parameter <strong id="b8423527069934_1"><a name="b8423527069934_1"></a><a name="b8423527069934_1"></a>next</strong>.</p>
    </td>
    </tr>
    <tr id="row698785617509"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p37867696115128"><a name="p37867696115128"></a><a name="p37867696115128"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p1781511129513"><a name="p1781511129513"></a><a name="p1781511129513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p195811620145120"><a name="p195811620145120"></a><a name="p195811620145120"></a>Specifies the URL for the schema describing a list of images.</p>
    </td>
    </tr>
    <tr id="row16942857114013"><td class="cellrowborder" valign="top" width="38.550000000000004%" headers="mcps1.1.4.1.1 "><p id="p1630281818413"><a name="p1630281818413"></a><a name="p1630281818413"></a>hw_firmware_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.1.4.1.2 "><p id="p2030231864116"><a name="p2030231864116"></a><a name="p2030231864116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.18%" headers="mcps1.1.4.1.3 "><p id="p7302161874115"><a name="p7302161874115"></a><a name="p7302161874115"></a>Specifies the <span id="text1721618104620"><a name="text1721618104620"></a><a name="text1721618104620"></a></span><span id="text07221183460"><a name="text07221183460"></a><a name="text07221183460"></a>ECS</span> boot mode. Available values include:</p>
    <a name="ul730291810417"></a><a name="ul730291810417"></a><ul id="ul730291810417"><li><strong id="b1981236122719"><a name="b1981236122719"></a><a name="b1981236122719"></a>bios</strong> indicates the BIOS boot mode.</li><li><strong id="b32031938162720"><a name="b32031938162720"></a><a name="b32031938162720"></a>uefi</strong> indicates the UEFI boot mode.</li></ul>
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
      "schema": "/v2/schemas/images",
      "next": "/v2/images?__isregistered=true&marker=0328c25e-c840-4496-81ac-c4e01b214b1f&__imagetype=gold&limit=2",
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
          "status": "active"
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
          "status": "active"
        }
      ],
      "first": "/v2/images?__isregistered=true&__imagetype=gold&limit=2"
    }
    ```


## Returned Values<a name="section20875522"></a>

-   Normal

    200

-   Abnormal

    <a name="table25137814143431"></a>
    <table><thead align="left"><tr id="row38004410143431"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p58458378143431"><a name="p58458378143431"></a><a name="p58458378143431"></a><strong id="b84235270611188"><a name="b84235270611188"></a><a name="b84235270611188"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p18261951143431"><a name="p18261951143431"></a><a name="p18261951143431"></a><strong id="b84235270616929"><a name="b84235270616929"></a><a name="b84235270616929"></a>Description</strong></p>
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


