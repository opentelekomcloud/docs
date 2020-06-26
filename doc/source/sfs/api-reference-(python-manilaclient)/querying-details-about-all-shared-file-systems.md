# Querying Details About All Shared File Systems<a name="EN-US_TOPIC_0090543714"></a>

## Function<a name="section74972015323"></a>

This interface is used to list the basic information of all shared file systems.

## Command<a name="section967536815323"></a>

-   Usage

    ```
    manila list [--all-tenants [<0|1>]] [--name <name>] [--status <status>]
                [--share-server-id <share_server_id>]
                [--metadata [<key=value> [<key=value> ...]]]
                [--extra-specs [<key=value> [<key=value> ...]]]
                [--share-type <share_type>] [--limit <limit>]
                [--offset <offset>] [--sort-key <sort_key>]
                [--sort-dir <sort_dir>] [--snapshot <snapshot>]
                [--host <host>] [--share-network <share_network>]
                [--project-id <project_id>] [--public]
                [--consistency-group <consistency_group>]
                [--columns <columns>]
    ```

-   Parameter description

    <a name="table2498726215323"></a>
    <table><thead align="left"><tr id="row6369985215323"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p5941442615323"><a name="p5941442615323"></a><a name="p5941442615323"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p4783921215323"><a name="p4783921215323"></a><a name="p4783921215323"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p4977098715323"><a name="p4977098715323"></a><a name="p4977098715323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p491814215323"><a name="p491814215323"></a><a name="p491814215323"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6282523015323"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p5567885015323"><a name="p5567885015323"></a><a name="p5567885015323"></a>all-tenants</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p1369299515323"><a name="p1369299515323"></a><a name="p1369299515323"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p3539077615323"><a name="p3539077615323"></a><a name="p3539077615323"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p4808058515323"><a name="p4808058515323"></a><a name="p4808058515323"></a>(Administrators only) Defines whether to list shared file systems of all tenants. This parameter is available only to Administrator and cannot be used by common tenants. To list shared file systems of all tenants, set it to <strong id="b1360012186567"><a name="b1360012186567"></a><a name="b1360012186567"></a>1</strong>. To list shared file systems of the current tenant, set it to <strong id="b18606142155612"><a name="b18606142155612"></a><a name="b18606142155612"></a>0</strong>. When Administrator uses this parameter and sets the value to <strong id="b19978191455618"><a name="b19978191455618"></a><a name="b19978191455618"></a>1</strong>, the shares created by all tenants (including Administrator and all common tenants) can be queried.</p>
    </td>
    </tr>
    <tr id="row20311795105547"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p20576185105741"><a name="p20576185105741"></a><a name="p20576185105741"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p56058299105741"><a name="p56058299105741"></a><a name="p56058299105741"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p44428394105741"><a name="p44428394105741"></a><a name="p44428394105741"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p41930157105741"><a name="p41930157105741"></a><a name="p41930157105741"></a>Specifies the name of the shared file system. The value contains 0 to 255 characters.</p>
    </td>
    </tr>
    <tr id="row3007208815323"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p1992009615323"><a name="p1992009615323"></a><a name="p1992009615323"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p291506415323"><a name="p291506415323"></a><a name="p291506415323"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p3479360815323"><a name="p3479360815323"></a><a name="p3479360815323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p6681887315323"><a name="p6681887315323"></a><a name="p6681887315323"></a>Filters shared file systems by status. Possible values are <strong id="b33613765115619"><a name="b33613765115619"></a><a name="b33613765115619"></a>creating</strong>,<strong id="b34088435115619"><a name="b34088435115619"></a><a name="b34088435115619"></a> error</strong>, <strong id="b38360467115619"><a name="b38360467115619"></a><a name="b38360467115619"></a>available</strong>, <strong id="b57411092135622"><a name="b57411092135622"></a><a name="b57411092135622"></a>deleting</strong>, <strong id="b46937780135622"><a name="b46937780135622"></a><a name="b46937780135622"></a>error_deleting</strong>,<strong id="b20190097115619"><a name="b20190097115619"></a><a name="b20190097115619"></a> manage_starting</strong>, <strong id="b47493145115619"><a name="b47493145115619"></a><a name="b47493145115619"></a>manage_error</strong>,<strong id="b24785127115619"><a name="b24785127115619"></a><a name="b24785127115619"></a> unmanage_starting</strong>,<strong id="b21739555115619"><a name="b21739555115619"></a><a name="b21739555115619"></a> unmanage_error, unmanaged, extending</strong>, <strong id="b61438270115619"><a name="b61438270115619"></a><a name="b61438270115619"></a>extending_error</strong>, <strong id="b16073521115619"><a name="b16073521115619"></a><a name="b16073521115619"></a>shrinking</strong>, <strong id="b10443965115619"><a name="b10443965115619"></a><a name="b10443965115619"></a>shrinking_error</strong>, and <strong id="b26886828115619"><a name="b26886828115619"></a><a name="b26886828115619"></a>shrinking_possible_data_loss_error</strong>.</p>
    </td>
    </tr>
    <tr id="row181317531137"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p3558300911334"><a name="p3558300911334"></a><a name="p3558300911334"></a>share-server-id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p6365146511334"><a name="p6365146511334"></a><a name="p6365146511334"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p5549501711334"><a name="p5549501711334"></a><a name="p5549501711334"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p6591140211334"><a name="p6591140211334"></a><a name="p6591140211334"></a>Specifies the UUID for managing share services. This parameter is currently invalid because the SFS service does not use this feature.</p>
    </td>
    </tr>
    <tr id="row2343853111428"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p1947285911428"><a name="p1947285911428"></a><a name="p1947285911428"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p5870956311456"><a name="p5870956311456"></a><a name="p5870956311456"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p5785415911456"><a name="p5785415911456"></a><a name="p5785415911456"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p5567533211456"><a name="p5567533211456"></a><a name="p5567533211456"></a>Sets that one or more metadata key and value pairs as a dictionary of strings.</p>
    </td>
    </tr>
    <tr id="row5040246111529"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p5606757011529"><a name="p5606757011529"></a><a name="p5606757011529"></a>extra-specs</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p4517934411529"><a name="p4517934411529"></a><a name="p4517934411529"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p3564822211529"><a name="p3564822211529"></a><a name="p3564822211529"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p182483611529"><a name="p182483611529"></a><a name="p182483611529"></a>Specifies the extra-specs key and value pair of the share type. This parameter is reserved and cannot be used as a filter criterion.</p>
    <div class="note" id="note843110123533"><a name="note843110123533"></a><a name="note843110123533"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1274571613530"><a name="p1274571613530"></a><a name="p1274571613530"></a>Currently, SFS provides only one share type whose value is <strong id="b167093501631"><a name="b167093501631"></a><a name="b167093501631"></a>default</strong>. This parameter cannot be used as a filter criterion because SFS does not provide the interface for querying the share type.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row14642252111018"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p45171800111018"><a name="p45171800111018"></a><a name="p45171800111018"></a>share-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p35037151111018"><a name="p35037151111018"></a><a name="p35037151111018"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p19437003111018"><a name="p19437003111018"></a><a name="p19437003111018"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p2011335812718"><a name="p2011335812718"></a><a name="p2011335812718"></a>Specifies the name of a share type. A share type is used to specify the type of the storage service to be allocated. The default value of this parameter is <strong id="b06251533251"><a name="b06251533251"></a><a name="b06251533251"></a>default</strong>.</p>
    <div class="notice" id="note16695142320288"><a name="note16695142320288"></a><a name="note16695142320288"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p11695323122816"><a name="p11695323122816"></a><a name="p11695323122816"></a>Currently, SFS provides only one share type whose value is <strong id="b172256379511"><a name="b172256379511"></a><a name="b172256379511"></a>default</strong>. This parameter cannot be used as a filter criterion because SFS does not provide the interface for querying the share type.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row2581004211135"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p49473899111313"><a name="p49473899111313"></a><a name="p49473899111313"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p47962919111313"><a name="p47962919111313"></a><a name="p47962919111313"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p59791198111313"><a name="p59791198111313"></a><a name="p59791198111313"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p11248890111313"><a name="p11248890111313"></a><a name="p11248890111313"></a>Specifies the maximum number of shared file systems that can be returned. The default value is <strong id="b84235270692512"><a name="b84235270692512"></a><a name="b84235270692512"></a>None</strong>.</p>
    </td>
    </tr>
    <tr id="row4804194211120"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p2849462911124"><a name="p2849462911124"></a><a name="p2849462911124"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p2636359011124"><a name="p2636359011124"></a><a name="p2636359011124"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p5507607711124"><a name="p5507607711124"></a><a name="p5507607711124"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p3197721511124"><a name="p3197721511124"></a><a name="p3197721511124"></a>Shared offset to define the start point of shared file system listing. The default value is <strong id="b37551306616"><a name="b37551306616"></a><a name="b37551306616"></a>None</strong>.</p>
    </td>
    </tr>
    <tr id="row13240137111340"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p6308534111343"><a name="p6308534111343"></a><a name="p6308534111343"></a>sort-key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p41229240111343"><a name="p41229240111343"></a><a name="p41229240111343"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p51234130111343"><a name="p51234130111343"></a><a name="p51234130111343"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p56323885111343"><a name="p56323885111343"></a><a name="p56323885111343"></a>Specifies the keyword for sorting query results. The default value is <strong id="b189181865714"><a name="b189181865714"></a><a name="b189181865714"></a>None</strong>. Possible values are <strong id="b36091081115619"><a name="b36091081115619"></a><a name="b36091081115619"></a>id</strong>, <strong id="b56384274115619"><a name="b56384274115619"></a><a name="b56384274115619"></a>status</strong>, <strong id="b37696424115619"><a name="b37696424115619"></a><a name="b37696424115619"></a>size</strong>, <strong id="b3723499115619"><a name="b3723499115619"></a><a name="b3723499115619"></a>host</strong>, <strong id="b33511492115619"><a name="b33511492115619"></a><a name="b33511492115619"></a>share_proto</strong>, <strong id="b33167972115619"><a name="b33167972115619"></a><a name="b33167972115619"></a>export_location</strong>, <strong id="b30076292115619"><a name="b30076292115619"></a><a name="b30076292115619"></a>availability_zone</strong>, <strong id="b2251173115619"><a name="b2251173115619"></a><a name="b2251173115619"></a>user_id</strong>, <strong id="b20260560115619"><a name="b20260560115619"></a><a name="b20260560115619"></a>project_id</strong>, <strong id="b48127319115619"><a name="b48127319115619"></a><a name="b48127319115619"></a>created_at</strong>, <strong id="b30492689115619"><a name="b30492689115619"></a><a name="b30492689115619"></a>updated_at</strong>, <strong id="b5998753115619"><a name="b5998753115619"></a><a name="b5998753115619"></a>display_name</strong>, <strong id="b53988783115619"><a name="b53988783115619"></a><a name="b53988783115619"></a>name</strong>, <strong id="b16137004115619"><a name="b16137004115619"></a><a name="b16137004115619"></a>share_type_id</strong>, <strong id="b11015313115619"><a name="b11015313115619"></a><a name="b11015313115619"></a>share_type</strong>, <strong id="b32028960115619"><a name="b32028960115619"></a><a name="b32028960115619"></a>share_network_id</strong>, <strong id="b19825184115619"><a name="b19825184115619"></a><a name="b19825184115619"></a>share_network</strong>, <strong id="b44208931115619"><a name="b44208931115619"></a><a name="b44208931115619"></a>snapshot_id</strong>, and <strong id="b62336067115619"><a name="b62336067115619"></a><a name="b62336067115619"></a>snapshot</strong>.</p>
    <div class="notice" id="note10304151713565"><a name="note10304151713565"></a><a name="note10304151713565"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p6305917195613"><a name="p6305917195613"></a><a name="p6305917195613"></a>Currently, python-manilaclient (including version 1.23.0 and earlier versions) on the official website do not support using the <strong id="b1956045915810"><a name="b1956045915810"></a><a name="b1956045915810"></a>sort-key</strong> and <strong id="b632664099"><a name="b632664099"></a><a name="b632664099"></a>sort-dir</strong> parameters to sort the query results. Therefore, this parameter does not take effect.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row50416590111223"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p37615389111226"><a name="p37615389111226"></a><a name="p37615389111226"></a>sort-dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p26947686111226"><a name="p26947686111226"></a><a name="p26947686111226"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p35278927111226"><a name="p35278927111226"></a><a name="p35278927111226"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p39020800111226"><a name="p39020800111226"></a><a name="p39020800111226"></a>Specifies the sorting direction of the share list. The default value is <strong id="b342621171015"><a name="b342621171015"></a><a name="b342621171015"></a>None</strong>. Possible values are <strong id="b11861342115619"><a name="b11861342115619"></a><a name="b11861342115619"></a>asc</strong> (ascending) and <strong id="b39643221115619"><a name="b39643221115619"></a><a name="b39643221115619"></a>desc</strong> (descending).</p>
    <div class="notice" id="note10542131310111"><a name="note10542131310111"></a><a name="note10542131310111"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p754418131115"><a name="p754418131115"></a><a name="p754418131115"></a>Currently, python-manilaclient (including version 1.23.0 and earlier versions) on the official website do not support using the <strong id="b191030561196"><a name="b191030561196"></a><a name="b191030561196"></a>sort-key</strong> and <strong id="b1410611565917"><a name="b1410611565917"></a><a name="b1410611565917"></a>sort-dir</strong> parameters to sort the query results. Therefore, this parameter does not take effect.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row4569551511140"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p3927455111435"><a name="p3927455111435"></a><a name="p3927455111435"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p49688439111435"><a name="p49688439111435"></a><a name="p49688439111435"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p65340636111435"><a name="p65340636111435"></a><a name="p65340636111435"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p58100149111435"><a name="p58100149111435"></a><a name="p58100149111435"></a>Specifies the UUID or name of the source snapshot that was used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="row17530631111539"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p57988137111548"><a name="p57988137111548"></a><a name="p57988137111548"></a>host</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p66527484111548"><a name="p66527484111548"></a><a name="p66527484111548"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p20017161111548"><a name="p20017161111548"></a><a name="p20017161111548"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p10777334111548"><a name="p10777334111548"></a><a name="p10777334111548"></a>Specifies the host name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row40476866111612"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p57400713111612"><a name="p57400713111612"></a><a name="p57400713111612"></a>share-network</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p18946168111612"><a name="p18946168111612"></a><a name="p18946168111612"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p63505427111626"><a name="p63505427111626"></a><a name="p63505427111626"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p43665997111626"><a name="p43665997111626"></a><a name="p43665997111626"></a>Specifies the UUID or name of the share network. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    <tr id="row6449894915323"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p5703239415323"><a name="p5703239415323"></a><a name="p5703239415323"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p5622118715323"><a name="p5622118715323"></a><a name="p5622118715323"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p5762229715323"><a name="p5762229715323"></a><a name="p5762229715323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p3689445115323"><a name="p3689445115323"></a><a name="p3689445115323"></a>Specifies the UUID of the project in which the shared file system was created. This parameter is used together with <strong id="b771137020102"><a name="b771137020102"></a><a name="b771137020102"></a>all_tenants</strong>.</p>
    </td>
    </tr>
    <tr id="row6361460515323"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p5250938515323"><a name="p5250938515323"></a><a name="p5250938515323"></a>public</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p2540178915323"><a name="p2540178915323"></a><a name="p2540178915323"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p4427905815323"><a name="p4427905815323"></a><a name="p4427905815323"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p40052093102658"><a name="p40052093102658"></a><a name="p40052093102658"></a>(Since API v2.8) Specifies the level of visibility for the shared file system. If this parameter is set to <strong id="b09213394410"><a name="b09213394410"></a><a name="b09213394410"></a>true</strong>, the share can be queried by other tenants using interfaces such as the one in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. If this parameter is set to <strong id="b1934314442"><a name="b1934314442"></a><a name="b1934314442"></a>false</strong>, the share is visible only to the tenant who creates it. The default value is <strong id="b89411324415"><a name="b89411324415"></a><a name="b89411324415"></a>false</strong>.</p>
    <div class="note" id="note484733973710"><a name="note484733973710"></a><a name="note484733973710"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p414515407435"><a name="p414515407435"></a><a name="p414515407435"></a>Share access rules added for different tenants are isolated from each other. Therefore, even if a share is set to be visible to other tenants, the share can only be queried by other tenants using the interface in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. Other tenants are not allowed to mount or use the share.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row7025715323"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p47173825111156"><a name="p47173825111156"></a><a name="p47173825111156"></a>consistency-group</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p25279959111156"><a name="p25279959111156"></a><a name="p25279959111156"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p26584473111156"><a name="p26584473111156"></a><a name="p26584473111156"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p51633604111912"><a name="p51633604111912"></a><a name="p51633604111912"></a>Specifies the UUID or name of the consistency group. This parameter is reserved, because consistency groups are not supported currently.</p>
    </td>
    </tr>
    <tr id="row6606457015323"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p12210131111328"><a name="p12210131111328"></a><a name="p12210131111328"></a>columns</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p47517042111328"><a name="p47517042111328"></a><a name="p47517042111328"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p10079442111328"><a name="p10079442111328"></a><a name="p10079442111328"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p22218256111328"><a name="p22218256111328"></a><a name="p22218256111328"></a>Specifies the queried columns, which are separated by commas (,). For example, <strong id="b11209307444"><a name="b11209307444"></a><a name="b11209307444"></a>--columns "ID, Size, Is Public"</strong>.</p>
    <div class="note" id="note0895934184310"><a name="note0895934184310"></a><a name="note0895934184310"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p889513345434"><a name="p889513345434"></a><a name="p889513345434"></a>Different versions may have different column names. Run the <strong id="b11100171911414"><a name="b11100171911414"></a><a name="b11100171911414"></a>manila list</strong> command to obtain all column names.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila list
    ```


-   Example command \(filtering using the  **name**  parameter\)

    ```
    manila list --name sample
    ```


-   Example command \(filtering using the  **status**  parameter\)

    ```
    manila list --status error
    ```


-   Example command \(using the  **limit**  and  **offset**  parameters for paging\)

    ```
    manila list --limit 2 --offset 1
    ```


-   Example command \(filtering using the  **columns**  parameter\)

    ```
    manila list  --columns "ID,Size,Is Public"
    ```


-   Example command \(filtering using a parameter combination\)

    ```
    manila list --name sample_share_name --status error --columns "ID,Size,Is Public"
    ```


## Response<a name="section6079875715323"></a>

-   Parameter description

    <a name="table555881615323"></a>
    <table><thead align="left"><tr id="row5498649515323"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.1.5.1.1"><p id="p2472112615323"><a name="p2472112615323"></a><a name="p2472112615323"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.1.5.1.2"><p id="p5625421815323"><a name="p5625421815323"></a><a name="p5625421815323"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p6029781015323"><a name="p6029781015323"></a><a name="p6029781015323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.1.5.1.4"><p id="p5228445515323"><a name="p5228445515323"></a><a name="p5228445515323"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row718244815323"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p4490741415323"><a name="p4490741415323"></a><a name="p4490741415323"></a>ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p1362188815323"><a name="p1362188815323"></a><a name="p1362188815323"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p2963112615323"><a name="p2963112615323"></a><a name="p2963112615323"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p5131104215323"><a name="p5131104215323"></a><a name="p5131104215323"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="row1867045911390"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p3591218011390"><a name="p3591218011390"></a><a name="p3591218011390"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p2320542911390"><a name="p2320542911390"></a><a name="p2320542911390"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p9730407114225"><a name="p9730407114225"></a><a name="p9730407114225"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p49965488114225"><a name="p49965488114225"></a><a name="p49965488114225"></a>Specifies the name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row3248015113949"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p61762686113949"><a name="p61762686113949"></a><a name="p61762686113949"></a>Size</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p26307337114146"><a name="p26307337114146"></a><a name="p26307337114146"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p64062817114247"><a name="p64062817114247"></a><a name="p64062817114247"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p21705684114247"><a name="p21705684114247"></a><a name="p21705684114247"></a>Specifies the size of the shared file system in GB.</p>
    </td>
    </tr>
    <tr id="row31716950113952"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p18936143113952"><a name="p18936143113952"></a><a name="p18936143113952"></a>Share Proto</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p52022935114146"><a name="p52022935114146"></a><a name="p52022935114146"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p48143349114253"><a name="p48143349114253"></a><a name="p48143349114253"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p7297230114253"><a name="p7297230114253"></a><a name="p7297230114253"></a>Specifies the protocol for sharing file systems. Only NFS is supported at present.</p>
    </td>
    </tr>
    <tr id="row33516352113955"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p30470000113955"><a name="p30470000113955"></a><a name="p30470000113955"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p16571796114147"><a name="p16571796114147"></a><a name="p16571796114147"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p4344064411438"><a name="p4344064411438"></a><a name="p4344064411438"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p2903128211438"><a name="p2903128211438"></a><a name="p2903128211438"></a>Specifies the status of the shared file system. Possible values are <strong id="b33613765115619_1"><a name="b33613765115619_1"></a><a name="b33613765115619_1"></a>creating</strong>,<strong id="b34088435115619_1"><a name="b34088435115619_1"></a><a name="b34088435115619_1"></a> error</strong>, <strong id="b38360467115619_1"><a name="b38360467115619_1"></a><a name="b38360467115619_1"></a>available</strong>, <strong id="b57411092135622_1"><a name="b57411092135622_1"></a><a name="b57411092135622_1"></a>deleting</strong>, <strong id="b46937780135622_1"><a name="b46937780135622_1"></a><a name="b46937780135622_1"></a>error_deleting</strong>,<strong id="b20190097115619_1"><a name="b20190097115619_1"></a><a name="b20190097115619_1"></a> manage_starting</strong>, <strong id="b47493145115619_1"><a name="b47493145115619_1"></a><a name="b47493145115619_1"></a>manage_error</strong>,<strong id="b24785127115619_1"><a name="b24785127115619_1"></a><a name="b24785127115619_1"></a> unmanage_starting</strong>,<strong id="b21739555115619_1"><a name="b21739555115619_1"></a><a name="b21739555115619_1"></a> unmanage_error, unmanaged, extending</strong>, <strong id="b61438270115619_1"><a name="b61438270115619_1"></a><a name="b61438270115619_1"></a>extending_error</strong>, <strong id="b16073521115619_1"><a name="b16073521115619_1"></a><a name="b16073521115619_1"></a>shrinking</strong>, <strong id="b10443965115619_1"><a name="b10443965115619_1"></a><a name="b10443965115619_1"></a>shrinking_error</strong>, and <strong id="b26886828115619_1"><a name="b26886828115619_1"></a><a name="b26886828115619_1"></a>shrinking_possible_data_loss_error</strong>.</p>
    </td>
    </tr>
    <tr id="row24839716113958"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p65860003113958"><a name="p65860003113958"></a><a name="p65860003113958"></a>Is Public</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p1244437114147"><a name="p1244437114147"></a><a name="p1244437114147"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p53852537114328"><a name="p53852537114328"></a><a name="p53852537114328"></a>bool</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p887985164812"><a name="p887985164812"></a><a name="p887985164812"></a>(Since API v2.8) Specifies the level of visibility for the shared file system. If this parameter is set to <strong id="b12927152014619"><a name="b12927152014619"></a><a name="b12927152014619"></a>true</strong>, the share can be queried by other tenants using interfaces such as the one in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. If this parameter is set to <strong id="b79281920154615"><a name="b79281920154615"></a><a name="b79281920154615"></a>false</strong>, the share is visible only to the tenant who creates it. The default value is <strong id="b18928182054612"><a name="b18928182054612"></a><a name="b18928182054612"></a>false</strong>.</p>
    <div class="note" id="note188851756487"><a name="note188851756487"></a><a name="note188851756487"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p28861952484"><a name="p28861952484"></a><a name="p28861952484"></a>Share access rules added for different tenants are isolated from each other. Therefore, even if a share is set to be visible to other tenants, the share can only be queried by other tenants using the interface in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. Other tenants are not allowed to mount or use the share.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row28830258114026"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p53549555114026"><a name="p53549555114026"></a><a name="p53549555114026"></a>Share Type Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p32256802114148"><a name="p32256802114148"></a><a name="p32256802114148"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p17130616114335"><a name="p17130616114335"></a><a name="p17130616114335"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p45941577103020"><a name="p45941577103020"></a><a name="p45941577103020"></a>Specifies the name of a share type. A share type is used to specify the type of the storage service to be allocated. Currently, only one share type is provided for SFS and the value is fixed to <strong id="b1355805716193"><a name="b1355805716193"></a><a name="b1355805716193"></a>default</strong>.</p>
    </td>
    </tr>
    <tr id="row64408582114028"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p49712628114028"><a name="p49712628114028"></a><a name="p49712628114028"></a>Host</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p27106658114148"><a name="p27106658114148"></a><a name="p27106658114148"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p63154538114351"><a name="p63154538114351"></a><a name="p63154538114351"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p15243978114351"><a name="p15243978114351"></a><a name="p15243978114351"></a>Specifies the host name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row7497889114031"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p3349279114031"><a name="p3349279114031"></a><a name="p3349279114031"></a>Availability Zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p9100584114149"><a name="p9100584114149"></a><a name="p9100584114149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p13666816114441"><a name="p13666816114441"></a><a name="p13666816114441"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p33270332114441"><a name="p33270332114441"></a><a name="p33270332114441"></a>Specifies the availability zone.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    root@n-version-client:~/ca# manila list
    +--------------------------------------+-------------------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | ID                                   | Name              | Size | Share Proto | Status    | Is Public | Share Type Name | Host                                                                          | Availability Zone |
    +--------------------------------------+-------------------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | 43e6f55c-b15a-40be-99ad-d77d7558d737 | sample1           | 1    | NFS         | available | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    | 53a08631-b108-47d1-acb2-2cfa6c4f9efe | sample_share_name | 1    | NFS         | error     | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    | bd012a04-c645-484a-bcf5-ea3bb792f354 | sample            | 10   | NFS         | available | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    | e289e6cc-db04-435f-9149-94baf1108400 | 234               | 10   | NFS         | available | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    +--------------------------------------+-------------------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    ```


-   Example response \(filtering using the  **name**  parameter\)

    ```
    root@n-version-client:~/ca# manila list --name sample
    +--------------------------------------+--------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | ID                                   | Name   | Size | Share Proto | Status    | Is Public | Share Type Name | Host                                                                          | Availability Zone |
    +--------------------------------------+--------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | bd012a04-c645-484a-bcf5-ea3bb792f354 | sample | 10   | NFS         | available | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    +--------------------------------------+--------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    ```


-   Example response \(filtering using the  **status**  parameter\)

    ```
    root@n-version-client:~/ca# manila list --status error
    +--------------------------------------+-------------------+------+-------------+--------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | ID                                   | Name              | Size | Share Proto | Status | Is Public | Share Type Name | Host                                                                          | Availability Zone |
    +--------------------------------------+-------------------+------+-------------+--------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | 53a08631-b108-47d1-acb2-2cfa6c4f9efe | sample_share_name | 1    | NFS         | error  | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    +--------------------------------------+-------------------+------+-------------+--------+-----------+-----------------+--------------
    -----------------------------------------------------------------+-------------------+
    ```


-   Example response \(using the  **limit**  and  **offset**  parameters for paging\)

    ```
    root@n-version-client:~/ca# manila list --limit 2 --offset 1
    +--------------------------------------+---------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | ID                                   | Name    | Size | Share Proto | Status    | Is Public | Share Type Name | Host                                                                          | Availability Zone |
    +--------------------------------------+---------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | 43e6f55c-b15a-40be-99ad-d77d7558d737 | sample1 | 1    | NFS         | available | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    | bd012a04-c645-484a-bcf5-ea3bb792f354 | sample  | 10   | NFS         | available | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    +--------------------------------------+---------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    ```


-   Example response \(filtering using the  **columns**  parameter\)

    ```
    root@n-version-client:~/ca# manila list --columns "ID,Size,Is Public"
    +--------------------------------------+------+-----------+
    | Id                                   | Size | Is Public |
    +--------------------------------------+------+-----------+
    | 43e6f55c-b15a-40be-99ad-d77d7558d737 | 1    | False     |
    | 53a08631-b108-47d1-acb2-2cfa6c4f9efe | 1    | False     |
    | bd012a04-c645-484a-bcf5-ea3bb792f354 | 10   | False     |
    | e289e6cc-db04-435f-9149-94baf1108400 | 10   | False     |
    +--------------------------------------+------+-----------+
    ```


-   Example response \(filtering using a parameter combination\)

    ```
    root@n-version-client:~/ca# manila list --name sample_share_name --status error --columns "ID,Size,Is Public"
    +--------------------------------------+------+-----------+
    | Id                                   | Size | Is Public |
    +--------------------------------------+------+-----------+
    | 53a08631-b108-47d1-acb2-2cfa6c4f9efe | 1    | False     |
    +--------------------------------------+------+-----------+
    ```


