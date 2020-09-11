# Querying Details of a VPC Endpoint<a name="vpcep_06_0304"></a>

## Function<a name="section16885652"></a>

This API is used to query details of a VPC endpoint.

## URI<a name="section17753146"></a>

GET /v1/\{project\_id\}/vpc-endpoints/\{vpc\_endpoint\_id\}

[Table 1](#table22005568)  describes the required parameters.

**Table  1**  Parameters

<a name="table22005568"></a>
<table><thead align="left"><tr id="row13047058"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p50178752"><a name="p50178752"></a><a name="p50178752"></a><strong id="b784315133388"><a name="b784315133388"></a><a name="b784315133388"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p37947078"><a name="p37947078"></a><a name="p37947078"></a><strong id="b953712152384"><a name="b953712152384"></a><a name="b953712152384"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p53814477"><a name="p53814477"></a><a name="p53814477"></a><strong id="b18591191619384"><a name="b18591191619384"></a><a name="b18591191619384"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row64005372"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p17052668"><a name="p17052668"></a><a name="p17052668"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p39088885"><a name="p39088885"></a><a name="p39088885"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p12083086"><a name="p12083086"></a><a name="p12083086"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row41638910"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p17308522"><a name="p17308522"></a><a name="p17308522"></a>vpc_endpoint_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p59813067"><a name="p59813067"></a><a name="p59813067"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p13020297"><a name="p13020297"></a><a name="p13020297"></a>Specifies the ID of the VPC endpoint.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section25560587"></a>

-   Parameter description

    None

-   Example request

    This request is to query details of the VPC endpoint service whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed83**.

    ```
    GET https://{endpoint}/v1/{project_id}/vpc-endpoints/4189d3c2-8882-4871-a3c2-d380272eed83
    ```


## Response<a name="section57141695"></a>

-   Parameter description

    **Table  2**  Response parameters

    <a name="table37620597"></a>
    <table><thead align="left"><tr id="row54996362"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p25520307"><a name="p25520307"></a><a name="p25520307"></a><strong id="b60772533"><a name="b60772533"></a><a name="b60772533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p53878948"><a name="p53878948"></a><a name="p53878948"></a><strong id="b14320349163814"><a name="b14320349163814"></a><a name="b14320349163814"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p2118662"><a name="p2118662"></a><a name="p2118662"></a><strong id="b1646384373"><a name="b1646384373"></a><a name="b1646384373"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37393920"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p9008699"><a name="p9008699"></a><a name="p9008699"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p58616031"><a name="p58616031"></a><a name="p58616031"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p50278034"><a name="p50278034"></a><a name="p50278034"></a>Specifies the unique ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row49849130"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p11247738"><a name="p11247738"></a><a name="p11247738"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p38651566"><a name="p38651566"></a><a name="p38651566"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p20173443232"><a name="p20173443232"></a><a name="p20173443232"></a>Specifies the type of the VPC endpoint service that is associated with the VPC endpoint.</p>
    <a name="ul649612552553"></a><a name="ul649612552553"></a><ul id="ul649612552553"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    </td>
    </tr>
    <tr id="row58377895"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p30989061"><a name="p30989061"></a><a name="p30989061"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p27086052"><a name="p27086052"></a><a name="p27086052"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p583352918492"><a name="p583352918492"></a><a name="p583352918492"></a>Specifies the connection status of the VPC endpoint.</p>
    <a name="ul32642017171417"></a><a name="ul32642017171417"></a><ul id="ul32642017171417"><li><strong id="b1796719346516"><a name="b1796719346516"></a><a name="b1796719346516"></a>pendingAcceptance</strong>: indicates that the VPC endpoint is pending acceptance.</li><li><strong id="b1321917323393"><a name="b1321917323393"></a><a name="b1321917323393"></a>creating</strong>: indicates the VPC endpoint is being created.</li><li><strong id="b5827333123919"><a name="b5827333123919"></a><a name="b5827333123919"></a>accepted</strong>: indicates the VPC endpoint has been accepted.</li><li><strong id="b1997793453910"><a name="b1997793453910"></a><a name="b1997793453910"></a>rejected</strong>: indicates the VPC endpoint has been rejected.</li><li><strong id="b11250636123918"><a name="b11250636123918"></a><a name="b11250636123918"></a>failed</strong>: indicates the creation of the VPC endpoint failed.</li><li><strong id="b649012385392"><a name="b649012385392"></a><a name="b649012385392"></a>deleting</strong>: indicates the VPC endpoint is being deleted.</li></ul>
    </td>
    </tr>
    <tr id="row1388715392538"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p8122041105310"><a name="p8122041105310"></a><a name="p8122041105310"></a>active_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p15122134112535"><a name="p15122134112535"></a><a name="p15122134112535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p14324144165119"><a name="p14324144165119"></a><a name="p14324144165119"></a>Specifies the domain status.</p>
    <a name="ul13303174918418"></a><a name="ul13303174918418"></a><ul id="ul13303174918418"><li><strong id="vpcep_06_0303_b34043383318171"><a name="vpcep_06_0303_b34043383318171"></a><a name="vpcep_06_0303_b34043383318171"></a>frozen</strong>: indicates that the domain is frozen.</li><li><strong id="vpcep_06_0303_b8423527061970"><a name="vpcep_06_0303_b8423527061970"></a><a name="vpcep_06_0303_b8423527061970"></a>active</strong>: indicates that the domain is normal.</li></ul>
    </td>
    </tr>
    <tr id="row51268101"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p59075518"><a name="p59075518"></a><a name="p59075518"></a>endpoint_service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p20387688"><a name="p20387688"></a><a name="p20387688"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p40790059"><a name="p40790059"></a><a name="p40790059"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row31566213"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p6726431"><a name="p6726431"></a><a name="p6726431"></a>marker_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p7970021"><a name="p7970021"></a><a name="p7970021"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p41592001"><a name="p41592001"></a><a name="p41592001"></a>Specifies the packet ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row38783689"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p54471134"><a name="p54471134"></a><a name="p54471134"></a>endpoint_service_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p50085756"><a name="p50085756"></a><a name="p50085756"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p30414410"><a name="p30414410"></a><a name="p30414410"></a>Specifies the ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row5294234"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p26179828"><a name="p26179828"></a><a name="p26179828"></a>enable_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p40191314"><a name="p40191314"></a><a name="p40191314"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p72792580273"><a name="p72792580273"></a><a name="p72792580273"></a>Specifies whether to create a private domain name.</p>
    <a name="ul145169269292"></a><a name="ul145169269292"></a><ul id="ul145169269292"><li><strong id="b9726154032110"><a name="b9726154032110"></a><a name="b9726154032110"></a>true</strong>: indicates that a private domain name is created.</li><li><strong id="b2911242202119"><a name="b2911242202119"></a><a name="b2911242202119"></a>false</strong>: indicates that a private domain name is not created.</li></ul>
    <div class="note" id="note1021533535814"><a name="note1021533535814"></a><a name="note1021533535814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="vpcep_06_0303_p119994525918"><a name="vpcep_06_0303_p119994525918"></a><a name="vpcep_06_0303_p119994525918"></a>When a VPC endpoint for connecting to a gateway VPC endpoint service is created, no private domain name is created no matter <strong id="vpcep_06_0303_b960193116271"><a name="vpcep_06_0303_b960193116271"></a><a name="vpcep_06_0303_b960193116271"></a>enable_dns</strong> is set to <strong id="vpcep_06_0303_b1156335172819"><a name="vpcep_06_0303_b1156335172819"></a><a name="vpcep_06_0303_b1156335172819"></a>true</strong> or <strong id="vpcep_06_0303_b844393752815"><a name="vpcep_06_0303_b844393752815"></a><a name="vpcep_06_0303_b844393752815"></a>false</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row40003590"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p19065375"><a name="p19065375"></a><a name="p19065375"></a>dns_names</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p791512"><a name="p791512"></a><a name="p791512"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p64112473"><a name="p64112473"></a><a name="p64112473"></a>Specifies the domain name for accessing the associated VPC endpoint service.</p>
    <p id="p1755062051318"><a name="p1755062051318"></a><a name="p1755062051318"></a>This parameter is only available when <strong id="vpcep_06_0303_b513454594811"><a name="vpcep_06_0303_b513454594811"></a><a name="vpcep_06_0303_b513454594811"></a>enable_dns</strong> is set to <strong id="vpcep_06_0303_b10660919124617"><a name="vpcep_06_0303_b10660919124617"></a><a name="vpcep_06_0303_b10660919124617"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row40141348"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p30223781"><a name="p30223781"></a><a name="p30223781"></a>ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p32207235"><a name="p32207235"></a><a name="p32207235"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p136794324466"><a name="p136794324466"></a><a name="p136794324466"></a>Specifies the IP address for accessing the associated VPC endpoint service.</p>
    <p id="p3149164017153"><a name="p3149164017153"></a><a name="p3149164017153"></a>This parameter is returned only under the following conditions:</p>
    <a name="ul146842035181816"></a><a name="ul146842035181816"></a><ul id="ul146842035181816"><li>You query a VPC endpoint for accessing an interface VPC endpoint service.</li><li>The connection approval function is enabled for the VPC endpoint service, and the connection has been approved.<p id="p753135720212"><a name="p753135720212"></a><a name="p753135720212"></a>The status of the VPC endpoint can be <strong id="b918718321178"><a name="b918718321178"></a><a name="b918718321178"></a>Accepted</strong> or <strong id="b14930933772"><a name="b14930933772"></a><a name="b14930933772"></a>Rejected</strong>. The <strong id="b11266144183514"><a name="b11266144183514"></a><a name="b11266144183514"></a>Rejected</strong> status only appears when the VPC endpoint is accepted and then rejected.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row596514534219"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p72595555215"><a name="p72595555215"></a><a name="p72595555215"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p1725913551625"><a name="p1725913551625"></a><a name="p1725913551625"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p53427648"><a name="p53427648"></a><a name="p53427648"></a>Specifies the ID of the VPC where the VPC endpoint is to be created.</p>
    </td>
    </tr>
    <tr id="row52205435"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p781836"><a name="p781836"></a><a name="p781836"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p63328721"><a name="p63328721"></a><a name="p63328721"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p1593291111113"><a name="p1593291111113"></a><a name="p1593291111113"></a>Specifies the ID of the subnet created in the VPC specified by <strong id="vpcep_06_0303_b1757761010202"><a name="vpcep_06_0303_b1757761010202"></a><a name="vpcep_06_0303_b1757761010202"></a>vpc_id</strong>. The value is in the UUID format.</p>
    <p id="p48629317123"><a name="p48629317123"></a><a name="p48629317123"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row62848201"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p57539553"><a name="p57539553"></a><a name="p57539553"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p30192201"><a name="p30192201"></a><a name="p30192201"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row65516150"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p5207934"><a name="p5207934"></a><a name="p5207934"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p19189523"><a name="p19189523"></a><a name="p19189523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p27321481"><a name="p27321481"></a><a name="p27321481"></a>Specifies the update time of the VPC endpoint.</p>
    <p id="p181016810016"><a name="p181016810016"></a><a name="p181016810016"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row30518784"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p56102419"><a name="p56102419"></a><a name="p56102419"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p48002062"><a name="p48002062"></a><a name="p48002062"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p62961818"><a name="p62961818"></a><a name="p62961818"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row323004311252"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p13103244015"><a name="p13103244015"></a><a name="p13103244015"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p21037441512"><a name="p21037441512"></a><a name="p21037441512"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p1510414411116"><a name="p1510414411116"></a><a name="p1510414411116"></a>Lists the resource tags. For details, see <a href="#table489217571060">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row198546211357"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p152721023351"><a name="p152721023351"></a><a name="p152721023351"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p12721234511"><a name="p12721234511"></a><a name="p12721234511"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p84071479448"><a name="p84071479448"></a><a name="p84071479448"></a>Specifies the error message.</p>
    <p id="p45203393322"><a name="p45203393322"></a><a name="p45203393322"></a>This field is returned when the status of the VPC endpoint changes to <strong id="b97214711155"><a name="b97214711155"></a><a name="b97214711155"></a>failed</strong>. For details, see <a href="#table14419242754">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row20357162719161"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p165011381477"><a name="p165011381477"></a><a name="p165011381477"></a>whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p450173820473"><a name="p450173820473"></a><a name="p450173820473"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p2538528143320"><a name="p2538528143320"></a><a name="p2538528143320"></a>Specifies the whitelist for controlling access to the VPC endpoint.</p>
    <p id="p386713773414"><a name="p386713773414"></a><a name="p386713773414"></a>If you do not specify this parameter, an empty whitelist is returned.</p>
    <p id="p14661112073410"><a name="p14661112073410"></a><a name="p14661112073410"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row780312293161"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p050938124710"><a name="p050938124710"></a><a name="p050938124710"></a>enable_whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p85019382479"><a name="p85019382479"></a><a name="p85019382479"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p1458051113412"><a name="p1458051113412"></a><a name="p1458051113412"></a>Specifies whether to enable access control.</p>
    <a name="ul1343419257325"></a><a name="ul1343419257325"></a><ul id="ul1343419257325"><li><strong id="vpcep_06_0303_b11313153317138"><a name="vpcep_06_0303_b11313153317138"></a><a name="vpcep_06_0303_b11313153317138"></a>true</strong>: indicates that access control is enabled.</li><li><strong id="vpcep_06_0303_b12134145911314"><a name="vpcep_06_0303_b12134145911314"></a><a name="vpcep_06_0303_b12134145911314"></a>false</strong>: indicates that access control is disabled.</li></ul>
    <p id="p16973392358"><a name="p16973392358"></a><a name="p16973392358"></a>If you do not specify this parameter, the whitelist is not enabled.</p>
    <p id="p69731393355"><a name="p69731393355"></a><a name="p69731393355"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row1598111334163"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p9502038174719"><a name="p9502038174719"></a><a name="p9502038174719"></a>routetables</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p650203810476"><a name="p650203810476"></a><a name="p650203810476"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p422280153614"><a name="p422280153614"></a><a name="p422280153614"></a>Lists the IDs of route tables.</p>
    <p id="p17737722113611"><a name="p17737722113611"></a><a name="p17737722113611"></a>If you do not specify this parameter, the route table ID of the VPC is returned.</p>
    <p id="p18501138164714"><a name="p18501138164714"></a><a name="p18501138164714"></a>This parameter is available only if you create a VPC endpoint for connecting to a gateway VPC endpoint service.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **ResourceTags**  parameters

    <a name="table489217571060"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.4.1.1"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><strong id="vpcep_06_0201_b1866348132314"><a name="vpcep_06_0201_b1866348132314"></a><a name="vpcep_06_0201_b1866348132314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><strong id="vpcep_06_0201_b616714104231"><a name="vpcep_06_0201_b616714104231"></a><a name="vpcep_06_0201_b616714104231"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.91%" id="mcps1.2.4.1.3"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><strong id="vpcep_06_0201_b163691023811"><a name="vpcep_06_0201_b163691023811"></a><a name="vpcep_06_0201_b163691023811"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters. This parameter cannot be left empty. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a>Specifies the tag value. A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Error parameters

    <a name="table14419242754"></a>
    <table><thead align="left"><tr id="vpcep_06_0202_row4652255153018"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="vpcep_06_0202_p665015573309"><a name="vpcep_06_0202_p665015573309"></a><a name="vpcep_06_0202_p665015573309"></a><strong id="vpcep_06_0202_b085424117110"><a name="vpcep_06_0202_b085424117110"></a><a name="vpcep_06_0202_b085424117110"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.630000000000003%" id="mcps1.2.4.1.2"><p id="vpcep_06_0202_p865015710307"><a name="vpcep_06_0202_p865015710307"></a><a name="vpcep_06_0202_p865015710307"></a><strong id="vpcep_06_0202_b1597841565"><a name="vpcep_06_0202_b1597841565"></a><a name="vpcep_06_0202_b1597841565"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.029999999999994%" id="mcps1.2.4.1.3"><p id="vpcep_06_0202_p1565011575303"><a name="vpcep_06_0202_p1565011575303"></a><a name="vpcep_06_0202_p1565011575303"></a><strong id="vpcep_06_0202_b1010514442017"><a name="vpcep_06_0202_b1010514442017"></a><a name="vpcep_06_0202_b1010514442017"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0202_row865255513010"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0202_p96501057153013"><a name="vpcep_06_0202_p96501057153013"></a><a name="vpcep_06_0202_p96501057153013"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.630000000000003%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0202_p6650155710309"><a name="vpcep_06_0202_p6650155710309"></a><a name="vpcep_06_0202_p6650155710309"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.029999999999994%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0202_p12650557133019"><a name="vpcep_06_0202_p12650557133019"></a><a name="vpcep_06_0202_p12650557133019"></a>Specifies the error code.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0202_row186521755153018"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0202_p10650057123018"><a name="vpcep_06_0202_p10650057123018"></a><a name="vpcep_06_0202_p10650057123018"></a>error_message</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.630000000000003%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0202_p14650157113016"><a name="vpcep_06_0202_p14650157113016"></a><a name="vpcep_06_0202_p14650157113016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.029999999999994%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0202_p156501957183013"><a name="vpcep_06_0202_p156501957183013"></a><a name="vpcep_06_0202_p156501957183013"></a>Specifies the error message.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "id": "4189d3c2-8882-4871-a3c2-d380272eed83",
        "service_type": "interface",
        "marker_id": 322312312312,
        "status": "accepted",
        "vpc_id": "4189d3c2-8882-4871-a3c2-d380272eed83",
        "enable_dns": false,
        "endpoint_service_name": "test123",
        "endpoint_service_id": "test123",
        "project_id": "6e9dfd51d1124e8d8498dce894923a0d",
        "whitelist": [
            "127.0.0.1"
        ],
        "enable_whitelist": true,
        "created_at": "2018-01-30T07:42:01.174",
        "update_at": "2018-01-30T07:42:01.174",
        "tags": [
            {
                "key": "test1",
                "value": "test1"
            }
        ]
    }
    ```


## Status Code<a name="section65074583"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).

