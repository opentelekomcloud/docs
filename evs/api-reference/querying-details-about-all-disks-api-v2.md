# Querying Details About All Disks<a name="evs_04_2005"></a>

## Function<a name="section37076589"></a>

This API is used to query details about all disks.

## URI<a name="section65253851"></a>

-   URI format

    GET /v2/\{project\_id\}/cloudvolumes/detail

-   Parameter description

    <a name="table17404391"></a>
    <table><thead align="left"><tr id="row60677108"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.1"><p id="p15898735"><a name="p15898735"></a><a name="p15898735"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.06%" id="mcps1.1.4.1.2"><p id="p12729171"><a name="p12729171"></a><a name="p12729171"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.61%" id="mcps1.1.4.1.3"><p id="p24429894"><a name="p24429894"></a><a name="p24429894"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32664435"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p28573568"><a name="p28573568"></a><a name="p28573568"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.1.4.1.2 "><p id="p32757653"><a name="p32757653"></a><a name="p32757653"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.61%" headers="mcps1.1.4.1.3 "><p id="p36124251"><a name="p36124251"></a><a name="p36124251"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request filter parameters

    <a name="table4291376694520"></a>
    <table><thead align="left"><tr id="row75210794520"><th class="cellrowborder" valign="top" width="15.78%" id="mcps1.1.5.1.1"><p id="p6092069194520"><a name="p6092069194520"></a><a name="p6092069194520"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.1.5.1.2"><p id="p3562891594520"><a name="p3562891594520"></a><a name="p3562891594520"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.29%" id="mcps1.1.5.1.3"><p id="p26101294520"><a name="p26101294520"></a><a name="p26101294520"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.7%" id="mcps1.1.5.1.4"><p id="p2114201394520"><a name="p2114201394520"></a><a name="p2114201394520"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3478152794520"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.5.1.1 "><p id="p6584033094520"><a name="p6584033094520"></a><a name="p6584033094520"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p3146649394520"><a name="p3146649394520"></a><a name="p3146649394520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.3 "><p id="p6575797694520"><a name="p6575797694520"></a><a name="p6575797694520"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.7%" headers="mcps1.1.5.1.4 "><p id="p2479584494520"><a name="p2479584494520"></a><a name="p2479584494520"></a><span id="text1258514515457"><a name="text1258514515457"></a><a name="text1258514515457"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="row2183600894520"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.5.1.1 "><p id="p2388619194520"><a name="p2388619194520"></a><a name="p2388619194520"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p5573333994520"><a name="p5573333994520"></a><a name="p5573333994520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.3 "><p id="p1810664494520"><a name="p1810664494520"></a><a name="p1810664494520"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.7%" headers="mcps1.1.5.1.4 "><p id="p5735206594520"><a name="p5735206594520"></a><a name="p5735206594520"></a>Specifies the disk name. <span id="text190068615920169"><a name="text190068615920169"></a><a name="text190068615920169"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row4640654394520"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.5.1.1 "><p id="p83363894520"><a name="p83363894520"></a><a name="p83363894520"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p41584594520"><a name="p41584594520"></a><a name="p41584594520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.3 "><p id="p3368350994520"><a name="p3368350994520"></a><a name="p3368350994520"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.7%" headers="mcps1.1.5.1.4 "><p id="p4400972694520"><a name="p4400972694520"></a><a name="p4400972694520"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row6054321594520"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.5.1.1 "><p id="p505334394520"><a name="p505334394520"></a><a name="p505334394520"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p666761194520"><a name="p666761194520"></a><a name="p666761194520"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.3 "><p id="p320564494520"><a name="p320564494520"></a><a name="p320564494520"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.7%" headers="mcps1.1.5.1.4 "><p id="p5833065094520"><a name="p5833065094520"></a><a name="p5833065094520"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p227915467717"><a name="p227915467717"></a><a name="p227915467717"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    </td>
    </tr>
    <tr id="row23814382153012"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.5.1.1 "><p id="p54096667153021"><a name="p54096667153021"></a><a name="p54096667153021"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p1313706153028"><a name="p1313706153028"></a><a name="p1313706153028"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.3 "><p id="p16317649153012"><a name="p16317649153012"></a><a name="p16317649153012"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.7%" headers="mcps1.1.5.1.4 "><p id="p10344004153039"><a name="p10344004153039"></a><a name="p10344004153039"></a>Specifies the AZ.</p>
    </td>
    </tr>
    <tr id="row5521380794520"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.5.1.1 "><p id="p4313339594520"><a name="p4313339594520"></a><a name="p4313339594520"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p414407094520"><a name="p414407094520"></a><a name="p414407094520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.3 "><p id="p12542794520"><a name="p12542794520"></a><a name="p12542794520"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.7%" headers="mcps1.1.5.1.4 "><p id="p1015961694520"><a name="p1015961694520"></a><a name="p1015961694520"></a>Specifies the keyword based on which the returned results are sorted. The value can be <strong id="b8179170145811"><a name="b8179170145811"></a><a name="b8179170145811"></a>id</strong>, <strong id="b9180110105816"><a name="b9180110105816"></a><a name="b9180110105816"></a>status</strong>, <strong id="b1181508585"><a name="b1181508585"></a><a name="b1181508585"></a>size</strong>, or <strong id="b1918113085812"><a name="b1918113085812"></a><a name="b1918113085812"></a>created_at</strong>, and the default value is <strong id="b161826015814"><a name="b161826015814"></a><a name="b161826015814"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row2432768294520"><td class="cellrowborder" valign="top" width="15.78%" headers="mcps1.1.5.1.1 "><p id="p2438521994520"><a name="p2438521994520"></a><a name="p2438521994520"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p2904568894520"><a name="p2904568894520"></a><a name="p2904568894520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.5.1.3 "><p id="p389050594520"><a name="p389050594520"></a><a name="p389050594520"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.7%" headers="mcps1.1.5.1.4 "><div class="p" id="p85141444124814"><a name="p85141444124814"></a><a name="p85141444124814"></a>Specifies the result sorting order. The default value is <strong id="b1590792375812"><a name="b1590792375812"></a><a name="b1590792375812"></a>desc</strong>.<a name="ul1097217103492"></a><a name="ul1097217103492"></a><ul id="ul1097217103492"><li><strong id="b195172510587"><a name="b195172510587"></a><a name="b195172510587"></a>desc</strong>: indicates the descending order.</li><li><strong id="b17211027125810"><a name="b17211027125810"></a><a name="b17211027125810"></a>asc</strong>: indicates the ascending order.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section50413755"></a>

The following example shows how to query the disks in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/cloudvolumes/detail?status=available
    ```


## Response<a name="section51070612"></a>

-   Parameter description

    <a name="table84066241518"></a>
    <table><thead align="left"><tr id="row12406192413112"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.1"><p id="p44071924617"><a name="p44071924617"></a><a name="p44071924617"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p1740719241010"><a name="p1740719241010"></a><a name="p1740719241010"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p13407524412"><a name="p13407524412"></a><a name="p13407524412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1540722420116"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p7407924310"><a name="p7407924310"></a><a name="p7407924310"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p12407102418117"><a name="p12407102418117"></a><a name="p12407102418117"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1440714241716"><a name="p1440714241716"></a><a name="p1440714241716"></a>Specifies the list of queried disks. For details, see <a href="#li7558467201357">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="row9632115616119"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li7558467201357"></a>Parameters in the  **volumes**  field

    <a name="table2981836711145"></a>
    <table><thead align="left"><tr id="row3364554311145"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.1"><p id="p4093449711145"><a name="p4093449711145"></a><a name="p4093449711145"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p2735998811145"><a name="p2735998811145"></a><a name="p2735998811145"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p5978048211145"><a name="p5978048211145"></a><a name="p5978048211145"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1038087811145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p3554478611145"><a name="p3554478611145"></a><a name="p3554478611145"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p6055544711145"><a name="p6055544711145"></a><a name="p6055544711145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1981792311145"><a name="p1981792311145"></a><a name="p1981792311145"></a><span id="text193761052172315"><a name="text193761052172315"></a><a name="text193761052172315"></a>Specifies the disk ID.</span></p>
    </td>
    </tr>
    <tr id="row4414357911145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p1886016511145"><a name="p1886016511145"></a><a name="p1886016511145"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p5127838711145"><a name="p5127838711145"></a><a name="p5127838711145"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p2076537311145"><a name="p2076537311145"></a><a name="p2076537311145"></a>Specifies the disk URI. For details, see <a href="#li1043159617124">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row5267063211145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p3846276911145"><a name="p3846276911145"></a><a name="p3846276911145"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p2847654611145"><a name="p2847654611145"></a><a name="p2847654611145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p354371011145"><a name="p354371011145"></a><a name="p354371011145"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="row3189339611145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p3322829411145"><a name="p3322829411145"></a><a name="p3322829411145"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p713731711145"><a name="p713731711145"></a><a name="p713731711145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p5306151211145"><a name="p5306151211145"></a><a name="p5306151211145"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row779156211145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p2713676711145"><a name="p2713676711145"></a><a name="p2713676711145"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p5059453311145"><a name="p5059453311145"></a><a name="p5059453311145"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3029347411145"><a name="p3029347411145"></a><a name="p3029347411145"></a>Specifies the disk attachment information. For details, see <a href="#li3900093617124">Parameters in the attachments field</a>.</p>
    </td>
    </tr>
    <tr id="row420581811145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p512694011145"><a name="p512694011145"></a><a name="p512694011145"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p1262901111145"><a name="p1262901111145"></a><a name="p1262901111145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p4660854311145"><a name="p4660854311145"></a><a name="p4660854311145"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="row1682370811145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p2054314211145"><a name="p2054314211145"></a><a name="p2054314211145"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p5338183311145"><a name="p5338183311145"></a><a name="p5338183311145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p6415551111145"><a name="p6415551111145"></a><a name="p6415551111145"></a>Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.</p>
    <p id="p152173372473"><a name="p152173372473"></a><a name="p152173372473"></a><span id="text88578719717"><a name="text88578719717"></a><a name="text88578719717"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row4052869111145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p6159857511145"><a name="p6159857511145"></a><a name="p6159857511145"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p2342864611145"><a name="p2342864611145"></a><a name="p2342864611145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3605277911145"><a name="p3605277911145"></a><a name="p3605277911145"></a>Specifies the snapshot ID. This parameter has a value if the disk is created from a snapshot.</p>
    </td>
    </tr>
    <tr id="row5603956011145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p4291047811145"><a name="p4291047811145"></a><a name="p4291047811145"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p5319669311145"><a name="p5319669311145"></a><a name="p5319669311145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p5741254811145"><a name="p5741254811145"></a><a name="p5741254811145"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="row4695089011145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p4492573411145"><a name="p4492573411145"></a><a name="p4492573411145"></a>os-vol-tenant-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p1510579811145"><a name="p1510579811145"></a><a name="p1510579811145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p5645845111145"><a name="p5645845111145"></a><a name="p5645845111145"></a>Specifies the ID of the tenant to which the disk belongs. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="row3836401911145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p2047785411145"><a name="p2047785411145"></a><a name="p2047785411145"></a>volume_image_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p4809349011145"><a name="p4809349011145"></a><a name="p4809349011145"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p6261854611145"><a name="p6261854611145"></a><a name="p6261854611145"></a>Specifies the metadata of the disk image.</p>
    <div class="note" id="note15692019279"><a name="note15692019279"></a><a name="note15692019279"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2009_p1888154732118"><a name="evs_04_2009_p1888154732118"></a><a name="evs_04_2009_p1888154732118"></a>For details about <strong id="evs_04_2009_b664802919300"><a name="evs_04_2009_b664802919300"></a><a name="evs_04_2009_b664802919300"></a>volume_image_metadata</strong>, see <strong id="evs_04_2009_b0649629203016"><a name="evs_04_2009_b0649629203016"></a><a name="evs_04_2009_b0649629203016"></a>Querying Image Details</strong> in the <em id="evs_04_2009_i186501329183018"><a name="evs_04_2009_i186501329183018"></a><a name="evs_04_2009_i186501329183018"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row2669600511145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p1489277711145"><a name="p1489277711145"></a><a name="p1489277711145"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p6546428211145"><a name="p6546428211145"></a><a name="p6546428211145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1442502411145"><a name="p1442502411145"></a><a name="p1442502411145"></a>Specifies the time when the disk was created.</p>
    <p id="p15772145473814"><a name="p15772145473814"></a><a name="p15772145473814"></a><span id="text151181202390"><a name="text151181202390"></a><a name="text151181202390"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row6271635911145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p4686035111145"><a name="p4686035111145"></a><a name="p4686035111145"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p3759207111145"><a name="p3759207111145"></a><a name="p3759207111145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p47786148539"><a name="en-us_topic_0098680634_p47786148539"></a><a name="en-us_topic_0098680634_p47786148539"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="row1431806011145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p1891222511145"><a name="p1891222511145"></a><a name="p1891222511145"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p5549524211145"><a name="p5549524211145"></a><a name="p5549524211145"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3869865011145"><a name="p3869865011145"></a><a name="p3869865011145"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="row1274353211145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p2559317611145"><a name="p2559317611145"></a><a name="p2559317611145"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p5978137211145"><a name="p5978137211145"></a><a name="p5978137211145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p8780414125315"><a name="en-us_topic_0098680634_p8780414125315"></a><a name="en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="ul185931714111"></a><a name="ul185931714111"></a><ul id="ul185931714111"><li><strong id="b72091815195712"><a name="b72091815195712"></a><a name="b72091815195712"></a>true</strong>: specifies a bootable disk.</li><li><strong id="b3175717185714"><a name="b3175717185714"></a><a name="b3175717185714"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row3693082411145"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p3860677311145"><a name="p3860677311145"></a><a name="p3860677311145"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p4014092711145"><a name="p4014092711145"></a><a name="p4014092711145"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p38279193144214"><a name="p38279193144214"></a><a name="p38279193144214"></a>Specifies the disk metadata. For details, see <a href="#li29114110314">Parameters in the metadata field</a>.</p>
    <p id="p34393810144258"><a name="p34393810144258"></a><a name="p34393810144258"></a>If <strong id="b842352706182520"><a name="b842352706182520"></a><a name="b842352706182520"></a>metadata</strong> does not contain the <strong id="b842352706143434"><a name="b842352706143434"></a><a name="b842352706143434"></a>hw:passthrough</strong> field, the disk device type is VBD.</p>
    <p id="p63879909144259"><a name="p63879909144259"></a><a name="p63879909144259"></a>If <strong id="b842352706182629"><a name="b842352706182629"></a><a name="b842352706182629"></a>metadata</strong> does not contain the <strong id="b842352706143455"><a name="b842352706143455"></a><a name="b842352706143455"></a>__system__encrypted</strong> field, the disk is not encrypted.</p>
    </td>
    </tr>
    <tr id="row27570907112011"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p18650967112011"><a name="p18650967112011"></a><a name="p18650967112011"></a>os-vol-host-attr:host</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p34333384112011"><a name="p34333384112011"></a><a name="p34333384112011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p43991208112011"><a name="p43991208112011"></a><a name="p43991208112011"></a><span id="text203605127103"><a name="text203605127103"></a><a name="text203605127103"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row5671275145922"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p637448871502"><a name="p637448871502"></a><a name="p637448871502"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p630621881502"><a name="p630621881502"></a><a name="p630621881502"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p248703561502"><a name="p248703561502"></a><a name="p248703561502"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="note3800959821323"><a name="note3800959821323"></a><a name="note3800959821323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p45212589213213"><a name="p45212589213213"></a><a name="p45212589213213"></a>This field is no longer used. Use <strong id="b84235270610834"><a name="b84235270610834"></a><a name="b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row63276793114824"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p53765166114828"><a name="p53765166114828"></a><a name="p53765166114828"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p60011165114828"><a name="p60011165114828"></a><a name="p60011165114828"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p4781191416535"><a name="en-us_topic_0098680634_p4781191416535"></a><a name="en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="ul161621719119"></a><a name="ul161621719119"></a><ul id="ul161621719119"><li><strong id="b133401139135710"><a name="b133401139135710"></a><a name="b133401139135710"></a>true</strong>: specifies a shared disk.</li><li><strong id="b1432074014578"><a name="b1432074014578"></a><a name="b1432074014578"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li1043159617124"></a>Parameters in the  **links**  field

    <a name="table4005083311851"></a>
    <table><thead align="left"><tr id="row4647546111851"><th class="cellrowborder" valign="top" width="19.27807219278072%" id="mcps1.1.4.1.1"><p id="p641601411851"><a name="p641601411851"></a><a name="p641601411851"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.0975902409759%" id="mcps1.1.4.1.2"><p id="p4993509511851"><a name="p4993509511851"></a><a name="p4993509511851"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.624337566243376%" id="mcps1.1.4.1.3"><p id="p6579322611851"><a name="p6579322611851"></a><a name="p6579322611851"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2765107611851"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p2514470311851"><a name="p2514470311851"></a><a name="p2514470311851"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2345507511851"><a name="p2345507511851"></a><a name="p2345507511851"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p812224311851"><a name="p812224311851"></a><a name="p812224311851"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="row599132611851"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p1553537811851"><a name="p1553537811851"></a><a name="p1553537811851"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p5040609911851"><a name="p5040609911851"></a><a name="p5040609911851"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p193416911851"><a name="p193416911851"></a><a name="p193416911851"></a>Specifies the shortcut link marker name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li3900093617124"></a>Parameters in the  **attachments**  field

    <a name="table3471673811913"></a>
    <table><thead align="left"><tr id="row950913211913"><th class="cellrowborder" valign="top" width="19.27807219278072%" id="mcps1.1.4.1.1"><p id="p3204224811913"><a name="p3204224811913"></a><a name="p3204224811913"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.0975902409759%" id="mcps1.1.4.1.2"><p id="p4528532911913"><a name="p4528532911913"></a><a name="p4528532911913"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.624337566243376%" id="mcps1.1.4.1.3"><p id="p2610634411913"><a name="p2610634411913"></a><a name="p2610634411913"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3423911011913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p2190452911913"><a name="p2190452911913"></a><a name="p2190452911913"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2943640011913"><a name="p2943640011913"></a><a name="p2943640011913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p6002094011913"><a name="p6002094011913"></a><a name="p6002094011913"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="row331754911913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p28604711913"><a name="p28604711913"></a><a name="p28604711913"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2316983311913"><a name="p2316983311913"></a><a name="p2316983311913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p1570218411913"><a name="p1570218411913"></a><a name="p1570218411913"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="row41611216113819"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p26997962113823"><a name="p26997962113823"></a><a name="p26997962113823"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p39351338113823"><a name="p39351338113823"></a><a name="p39351338113823"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p16333436113823"><a name="p16333436113823"></a><a name="p16333436113823"></a>Specifies the time when the disk was attached.</p>
    <p id="p103581088395"><a name="p103581088395"></a><a name="p103581088395"></a><span id="text136037162396"><a name="text136037162396"></a><a name="text136037162396"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row710192811913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p3838529111913"><a name="p3838529111913"></a><a name="p3838529111913"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2220087511913"><a name="p2220087511913"></a><a name="p2220087511913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p3370764811913"><a name="p3370764811913"></a><a name="p3370764811913"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="row3493337611913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p1103121411913"><a name="p1103121411913"></a><a name="p1103121411913"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2111318111913"><a name="p2111318111913"></a><a name="p2111318111913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p1089110111913"><a name="p1089110111913"></a><a name="p1089110111913"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row3091104611913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p2076682611913"><a name="p2076682611913"></a><a name="p2076682611913"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p439134611913"><a name="p439134611913"></a><a name="p439134611913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p2192276811913"><a name="p2192276811913"></a><a name="p2192276811913"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="row6308718811913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p978858311913"><a name="p978858311913"></a><a name="p978858311913"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p5467773011913"><a name="p5467773011913"></a><a name="p5467773011913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p4371205011913"><a name="p4371205011913"></a><a name="p4371205011913"></a>Specifies the ID of the attached resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li29114110314"></a>Parameters in the  **metadata**  field

    <a name="evs_04_3004_table3430728295554"></a>
    <table><thead align="left"><tr id="evs_04_3004_row4496975195554"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_3004_p8809200174410"><a name="evs_04_3004_p8809200174410"></a><a name="evs_04_3004_p8809200174410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="evs_04_3004_p168135017449"><a name="evs_04_3004_p168135017449"></a><a name="evs_04_3004_p168135017449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_3004_p1282213034412"><a name="evs_04_3004_p1282213034412"></a><a name="evs_04_3004_p1282213034412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_3004_row456195295554"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p1562408795622"><a name="evs_04_3004_p1562408795622"></a><a name="evs_04_3004_p1562408795622"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p5759155095622"><a name="evs_04_3004_p5759155095622"></a><a name="evs_04_3004_p5759155095622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_3004_p177192813501"><a name="evs_04_3004_p177192813501"></a><a name="evs_04_3004_p177192813501"></a>Specifies the parameter that describes the encryption function in <strong id="evs_04_3004_b84235270614509"><a name="evs_04_3004_b84235270614509"></a><a name="evs_04_3004_b84235270614509"></a>metadata</strong>. The value can be <strong id="evs_04_3004_b842352706145015"><a name="evs_04_3004_b842352706145015"></a><a name="evs_04_3004_b842352706145015"></a>0</strong> or <strong id="evs_04_3004_b842352706145020"><a name="evs_04_3004_b842352706145020"></a><a name="evs_04_3004_b842352706145020"></a>1</strong>.<a name="evs_04_3004_ul141951225145011"></a><a name="evs_04_3004_ul141951225145011"></a><ul id="evs_04_3004_ul141951225145011"><li><strong id="evs_04_3004_b842352706145038"><a name="evs_04_3004_b842352706145038"></a><a name="evs_04_3004_b842352706145038"></a>0</strong>: indicates the disk is not encrypted.</li><li><strong id="evs_04_3004_b842352706145058"><a name="evs_04_3004_b842352706145058"></a><a name="evs_04_3004_b842352706145058"></a>1</strong>: indicates the disk is encrypted.</li><li>If this parameter does not appear, the disk is not encrypted by default.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_3004_row247050109562"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p241272995622"><a name="evs_04_3004_p241272995622"></a><a name="evs_04_3004_p241272995622"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p6121338895622"><a name="evs_04_3004_p6121338895622"></a><a name="evs_04_3004_p6121338895622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_3004_p4159804295622"><a name="evs_04_3004_p4159804295622"></a><a name="evs_04_3004_p4159804295622"></a>Specifies the parameter that describes the encryption CMK ID in <strong id="evs_04_3004_b84235270615116"><a name="evs_04_3004_b84235270615116"></a><a name="evs_04_3004_b84235270615116"></a>metadata</strong>. This parameter is used together with <strong id="evs_04_3004_b842352706143827"><a name="evs_04_3004_b842352706143827"></a><a name="evs_04_3004_b842352706143827"></a>__system__encrypted</strong> for encryption. The length of <strong id="evs_04_3004_b84235270614396"><a name="evs_04_3004_b84235270614396"></a><a name="evs_04_3004_b84235270614396"></a>cmkid</strong> is fixed at 36 bytes.</p>
    </td>
    </tr>
    <tr id="evs_04_3004_row60499086104915"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p1478896104915"><a name="evs_04_3004_p1478896104915"></a><a name="evs_04_3004_p1478896104915"></a>hw:passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p52681767104915"><a name="evs_04_3004_p52681767104915"></a><a name="evs_04_3004_p52681767104915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_3004_p17177177145116"><a name="evs_04_3004_p17177177145116"></a><a name="evs_04_3004_p17177177145116"></a>Specifies the parameter that describes the disk device type in <strong id="evs_04_3004_b84235270615173"><a name="evs_04_3004_b84235270615173"></a><a name="evs_04_3004_b84235270615173"></a>metadata</strong>. The value can be <strong id="evs_04_3004_b842352706151718"><a name="evs_04_3004_b842352706151718"></a><a name="evs_04_3004_b842352706151718"></a>true</strong> or <strong id="evs_04_3004_b842352706151722"><a name="evs_04_3004_b842352706151722"></a><a name="evs_04_3004_b842352706151722"></a>false</strong>.<a name="evs_04_3004_ul14462208141855"></a><a name="evs_04_3004_ul14462208141855"></a><ul id="evs_04_3004_ul14462208141855"><li>If this parameter is set to <strong id="evs_04_3004_b55868159103732"><a name="evs_04_3004_b55868159103732"></a><a name="evs_04_3004_b55868159103732"></a>true</strong>, the disk device type is SCSI, that is, Small Computer System Interface (SCSI), which allows ECS OSs to directly access the underlying storage media and supports SCSI reservation commands.</li><li>If this parameter is set to <strong>false</strong>, the disk device type is VBD (the default type), that is, Virtual Block Device (VBD), which supports only simple SCSI read/write commands.</li><li>If this parameter does not appear, the disk device type is VBD.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_3004_row991210132288"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p3500156018292"><a name="evs_04_3004_p3500156018292"></a><a name="evs_04_3004_p3500156018292"></a>full_clone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p1655411118292"><a name="evs_04_3004_p1655411118292"></a><a name="evs_04_3004_p1655411118292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_3004_p47931946183150"><a name="evs_04_3004_p47931946183150"></a><a name="evs_04_3004_p47931946183150"></a>Specifies the clone method. When the disk is created from a snapshot, the parameter value is <strong id="evs_04_3004_b84235270616922"><a name="evs_04_3004_b84235270616922"></a><a name="evs_04_3004_b84235270616922"></a>0</strong>, indicating the linked cloning method.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p19541716103019"><a name="evs_04_2013_p19541716103019"></a><a name="evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p39375186103019"><a name="evs_04_2013_p39375186103019"></a><a name="evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p38578950103019"><a name="evs_04_2013_p38578950103019"></a><a name="evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p46815658103019"><a name="evs_04_2013_p46815658103019"></a><a name="evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p33971979103019"><a name="evs_04_2013_p33971979103019"></a><a name="evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p21623243103019"><a name="evs_04_2013_p21623243103019"></a><a name="evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p59870541103019"><a name="evs_04_2013_p59870541103019"></a><a name="evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p17675690103019"><a name="evs_04_2013_p17675690103019"></a><a name="evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p6087468103019"><a name="evs_04_2013_p6087468103019"></a><a name="evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2013_p54787218103019"><a name="evs_04_2013_p54787218103019"></a><a name="evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "volumes": [
            {
                "id": "c6ccc84e-feff-4114-ad83-42a11c0434e2", 
                "links": [
                    {
                        "href": "https://volume.az0.dc1.domainname.com/v2/9e179fd535e44f19a9dabb36deadf47e/volumes/c6ccc84e-feff-4114-ad83-42a11c0434e2", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.az0.dc1.domainname.com/9e179fd535e44f19a9dabb36deadf47e/volumes/c6ccc84e-feff-4114-ad83-42a11c0434e2", 
                        "rel": "bookmark"
                    }
                ], 
                "name": "test_volume", 
                "status": "available", 
                "attachments": [ ], 
                "description": null, 
                "size": 100, 
                "metadata": null, 
                "bootable": "false", 
                "availability_zone": "az-dc-1", 
                "os-vol-host-attr:host": "az-dc-1#sata", 
                "source_volid": null, 
                "snapshot_id": null, 
                "created_at": "2015-09-17T06:37:16.275659", 
                "volume_type": "SATA", 
                "os-vol-tenant-attr:tenant_id": "9e179fd535e44f19a9dabb36deadf47e", 
                "volume_image_metadata": null
            }, 
            {
                "id": "a05d9342-bf27-44a6-8ab8-33afc7545d19", 
                "links": [
                    {
                        "href": "https://volume.az0.dc1.domainname.com/v2/9e179fd535e44f19a9dabb36deadf47e/volumes/a05d9342-bf27-44a6-8ab8-33afc7545d19", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.az0.dc1.domainname.com/9e179fd535e44f19a9dabb36deadf47e/volumes/a05d9342-bf27-44a6-8ab8-33afc7545d19", 
                        "rel": "bookmark"
                    }
                ], 
                "name": "test_volume", 
                "status": "available", 
                "attachments": [ ], 
                "description": null, 
                "size": 100, 
                "metadata": null, 
                "bootable": "false", 
                "availability_zone": "az-dc-1", 
                "os-vol-host-attr:host": "az-dc-1#sata", 
                "source_volid": null, 
                "snapshot_id": null, 
                "created_at": "2015-09-17T06:37:16.192556", 
                "volume_type": "SATA", 
                "os-vol-tenant-attr:tenant_id": "9e179fd535e44f19a9dabb36deadf47e", 
                "volume_image_metadata": null
            }
        ]
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


## Status Codes<a name="section56982329"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

