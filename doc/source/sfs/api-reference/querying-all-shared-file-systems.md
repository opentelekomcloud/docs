# Querying All Shared File Systems<a name="sfs_02_0022"></a>

## Function<a name="section35417005112634"></a>

This API is used to list the basic information of all shared file systems.

## URI<a name="section56431007112911"></a>

-   GET /v2/\{project\_id\}/shares?all\_tenants=\{all\_tenants\}&status=\{status\}&limit=\{limit\}&offset=\{offset\}&sort\_key=\{sort\_key\}&sort\_dir=\{sort\_dir\}&project\_id=\{project\_id\}&is\_public=\{is\_public\}&metadata=\{metadata\}& export\_location\_id=\{export\_location\_id\}& export\_location\_path=\{export\_location\_path\}& name\~=\{name\}& description\~=\{description\}& with\_count=\{with\_count\}
-   Parameter description

    <a name="table1936210911319"></a>
    <table><thead align="left"><tr id="row2818054511319"><th class="cellrowborder" valign="top" width="16.17%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.66%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.11%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.059999999999995%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4580752711319"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p31893403113152"><a name="p31893403113152"></a><a name="p31893403113152"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p33228870113152"><a name="p33228870113152"></a><a name="p33228870113152"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p7183962113152"><a name="p7183962113152"></a><a name="p7183962113152"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p45030013113152"><a name="p45030013113152"></a><a name="p45030013113152"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    <tr id="row36441474115817"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p66078304115817"><a name="p66078304115817"></a><a name="p66078304115817"></a>all_tenants</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p50742382115817"><a name="p50742382115817"></a><a name="p50742382115817"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p16492244115817"><a name="p16492244115817"></a><a name="p16492244115817"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p60803387115817"><a name="p60803387115817"></a><a name="p60803387115817"></a>This parameter is available only to users with administrator permissions. Specifies whether to list shared file systems of all tenants. To list shared file systems of all tenants, set it to <strong id="b71208721310018"><a name="b71208721310018"></a><a name="b71208721310018"></a>1</strong>. To list shared file systems only of the current tenant, set it to <strong id="b83357843610021"><a name="b83357843610021"></a><a name="b83357843610021"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row31531724213534"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p8567926213542"><a name="p8567926213542"></a><a name="p8567926213542"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p22913431213542"><a name="p22913431213542"></a><a name="p22913431213542"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p44048661213542"><a name="p44048661213542"></a><a name="p44048661213542"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p11171799213542"><a name="p11171799213542"></a><a name="p11171799213542"></a>This parameter is available only to users with administrator permissions. Specifies the UUID of the project to which the shared file system belongs. This parameter needs to be used together with <strong id="b415113865910"><a name="b415113865910"></a><a name="b415113865910"></a>all_tenants</strong>.</p>
    </td>
    </tr>
    <tr id="row57379135115842"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p17198368115842"><a name="p17198368115842"></a><a name="p17198368115842"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p50890569115842"><a name="p50890569115842"></a><a name="p50890569115842"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p28495459115842"><a name="p28495459115842"></a><a name="p28495459115842"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p1893725121718"><a name="p1893725121718"></a><a name="p1893725121718"></a>Filters shared file systems by status. Possible values are:</p>
    <a name="ul437945121818"></a><a name="ul437945121818"></a><ul id="ul437945121818"><li><strong id="b927045061010"><a name="b927045061010"></a><a name="b927045061010"></a>creating</strong>: The shared file system is being created.</li><li><strong id="b20389183371119"><a name="b20389183371119"></a><a name="b20389183371119"></a>error</strong>: The shared file system fails to be created.</li><li><strong id="b491004941111"><a name="b491004941111"></a><a name="b491004941111"></a>available</strong>: The shared file system is available.</li><li><strong id="b8718165991113"><a name="b8718165991113"></a><a name="b8718165991113"></a>deleting</strong>: The shared file system is being deleted.</li><li><strong id="b01411831171311"><a name="b01411831171311"></a><a name="b01411831171311"></a>error_deleting</strong>: The shared file system fails to be deleted.</li><li><strong id="b12809134810134"><a name="b12809134810134"></a><a name="b12809134810134"></a>extending</strong>: The shared file system is being expanded.</li><li><strong id="b3942143161413"><a name="b3942143161413"></a><a name="b3942143161413"></a>extending_error</strong>: The shared file system fails to be expanded.</li><li><strong id="b104281323161419"><a name="b104281323161419"></a><a name="b104281323161419"></a>shrinking</strong>: The shared file system is being shrunk.</li><li><strong id="b14545193917144"><a name="b14545193917144"></a><a name="b14545193917144"></a>shrinking_error</strong>: The shared file system fails to be shrunk.</li><li><strong id="b0222133771519"><a name="b0222133771519"></a><a name="b0222133771519"></a>shrinking_possible_data_loss_error</strong>: The shared file system fails to be shrunk due to data loss.</li><li><strong id="b7455258191517"><a name="b7455258191517"></a><a name="b7455258191517"></a>manage_starting</strong>: Shared file system management starts.</li><li><strong id="b179981816111610"><a name="b179981816111610"></a><a name="b179981816111610"></a>manage_error</strong>: The shared file system fails to be managed.</li><li><strong id="b10318113216177"><a name="b10318113216177"></a><a name="b10318113216177"></a>unmanage_starting</strong>: Canceling shared file system management starts.</li><li><strong id="b112077588183"><a name="b112077588183"></a><a name="b112077588183"></a>unmanage_error</strong>: Failed to cancel shared file system management.</li><li><strong id="b13383091919"><a name="b13383091919"></a><a name="b13383091919"></a>unmanaged</strong>: The shared file system is not managed.</li></ul>
    </td>
    </tr>
    <tr id="row62597525115844"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p37234804115844"><a name="p37234804115844"></a><a name="p37234804115844"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p63229180115844"><a name="p63229180115844"></a><a name="p63229180115844"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p21289940115844"><a name="p21289940115844"></a><a name="p21289940115844"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p38523289121046"><a name="p38523289121046"></a><a name="p38523289121046"></a>Specifies the maximum number of shared file systems that can be returned. If this parameter is not specified, all the shared file systems are returned by default.</p>
    </td>
    </tr>
    <tr id="row66750965115847"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p38119081115847"><a name="p38119081115847"></a><a name="p38119081115847"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p637886115847"><a name="p637886115847"></a><a name="p637886115847"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p51668828115847"><a name="p51668828115847"></a><a name="p51668828115847"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p31972906121046"><a name="p31972906121046"></a><a name="p31972906121046"></a>Specifies the offset to define the start point from 0 of shared file system listing. The value must be greater than or equal to <strong id="b13693165385918"><a name="b13693165385918"></a><a name="b13693165385918"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row44975276115839"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p19118728115839"><a name="p19118728115839"></a><a name="p19118728115839"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p5113096115839"><a name="p5113096115839"></a><a name="p5113096115839"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p11507604115839"><a name="p11507604115839"></a><a name="p11507604115839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p59700757115839"><a name="p59700757115839"></a><a name="p59700757115839"></a>Specifies the keyword for sorting the queried shared file systems. Possible values are <strong id="a68cbb73a521242a59d3d9ad3f9b66102"><a name="a68cbb73a521242a59d3d9ad3f9b66102"></a><a name="a68cbb73a521242a59d3d9ad3f9b66102"></a>id</strong>, <strong id="a1d2bc637a7ee459ea2d83bc913bc6259"><a name="a1d2bc637a7ee459ea2d83bc913bc6259"></a><a name="a1d2bc637a7ee459ea2d83bc913bc6259"></a>status</strong>, <strong id="a51003601a3144968b4f51eca32e55877"><a name="a51003601a3144968b4f51eca32e55877"></a><a name="a51003601a3144968b4f51eca32e55877"></a>size</strong>, <strong id="af2c02598b99b446fb1cea0ebdedb2cee"><a name="af2c02598b99b446fb1cea0ebdedb2cee"></a><a name="af2c02598b99b446fb1cea0ebdedb2cee"></a>host</strong>, <strong id="a88f2323c96914bcd81387dd1215f70dd"><a name="a88f2323c96914bcd81387dd1215f70dd"></a><a name="a88f2323c96914bcd81387dd1215f70dd"></a>share_proto</strong>, <strong id="b119317573612"><a name="b119317573612"></a><a name="b119317573612"></a>availability_zone_id</strong>, <strong id="af67a9d0389164fcba7bd3495f75b6d69"><a name="af67a9d0389164fcba7bd3495f75b6d69"></a><a name="af67a9d0389164fcba7bd3495f75b6d69"></a>user_id</strong>, <strong id="a2dc83dbfc872472d8d425382519399a0"><a name="a2dc83dbfc872472d8d425382519399a0"></a><a name="a2dc83dbfc872472d8d425382519399a0"></a>project_id</strong>, <strong id="a887747186c964040ae955538fa409363"><a name="a887747186c964040ae955538fa409363"></a><a name="a887747186c964040ae955538fa409363"></a>created_at</strong>, <strong id="a94572296c0754a9fabb3b158651fe1bb"><a name="a94572296c0754a9fabb3b158651fe1bb"></a><a name="a94572296c0754a9fabb3b158651fe1bb"></a>updated_at</strong>, <strong id="a9abc7f7170e64e3ea69588a7a3ab142a"><a name="a9abc7f7170e64e3ea69588a7a3ab142a"></a><a name="a9abc7f7170e64e3ea69588a7a3ab142a"></a>display_name</strong>, <strong id="a1d06947d49c14dfd9e4b14dc63e783e3"><a name="a1d06947d49c14dfd9e4b14dc63e783e3"></a><a name="a1d06947d49c14dfd9e4b14dc63e783e3"></a>name</strong>, <strong id="a45fb80e0661844949301b3c492fc698b"><a name="a45fb80e0661844949301b3c492fc698b"></a><a name="a45fb80e0661844949301b3c492fc698b"></a>share_type_id</strong>, <strong id="a99a1214b2d214c1d984827e4e504892d"><a name="a99a1214b2d214c1d984827e4e504892d"></a><a name="a99a1214b2d214c1d984827e4e504892d"></a>share_network_id</strong>, and <strong id="acbb6e40ebba240c396ac7cb495cc7e2d"><a name="acbb6e40ebba240c396ac7cb495cc7e2d"></a><a name="acbb6e40ebba240c396ac7cb495cc7e2d"></a>snapshot_id</strong>. By default, the value is sorted by <strong id="b1186814912114"><a name="b1186814912114"></a><a name="b1186814912114"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row28691532115825"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p42312794115825"><a name="p42312794115825"></a><a name="p42312794115825"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p4784300115825"><a name="p4784300115825"></a><a name="p4784300115825"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p51984043115825"><a name="p51984043115825"></a><a name="p51984043115825"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p49957950115825"><a name="p49957950115825"></a><a name="p49957950115825"></a>Specifies the direction to sort shared file systems. Possible values are <strong id="b5812645095432"><a name="b5812645095432"></a><a name="b5812645095432"></a>asc</strong> (ascending) and <strong id="b4180123695432"><a name="b4180123695432"></a><a name="b4180123695432"></a>desc</strong> (descending).</p>
    </td>
    </tr>
    <tr id="row5827083212846"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p2231690212846"><a name="p2231690212846"></a><a name="p2231690212846"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p3290281212935"><a name="p3290281212935"></a><a name="p3290281212935"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p65186226212935"><a name="p65186226212935"></a><a name="p65186226212935"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p45592923212935"><a name="p45592923212935"></a><a name="p45592923212935"></a>When this parameter is set to <strong id="b65906355223130"><a name="b65906355223130"></a><a name="b65906355223130"></a>true</strong>, the current tenant can query all its own shared file systems and other tenants' shared file systems whose <strong id="b84235270611715"><a name="b84235270611715"></a><a name="b84235270611715"></a>is_public</strong> is set to <strong id="b4057183223139"><a name="b4057183223139"></a><a name="b4057183223139"></a>true</strong>. When this parameter is set to <strong id="b25237589223148"><a name="b25237589223148"></a><a name="b25237589223148"></a>false</strong>, the current tenant can query only the shared file systems owned by the tenant.</p>
    </td>
    </tr>
    <tr id="row1582111919371"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p164001838193717"><a name="p164001838193717"></a><a name="p164001838193717"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p24006387374"><a name="p24006387374"></a><a name="p24006387374"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p12400173811373"><a name="p12400173811373"></a><a name="p12400173811373"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p1740010383379"><a name="p1740010383379"></a><a name="p1740010383379"></a>Specifies the metadata information used to query the shared file systems. The value consists of one or more key and value pairs organized as a dictionary of strings. </p>
    </td>
    </tr>
    <tr id="row12752111333712"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p42641245133713"><a name="p42641245133713"></a><a name="p42641245133713"></a>export_location_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p826411456379"><a name="p826411456379"></a><a name="p826411456379"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p32641445123710"><a name="p32641445123710"></a><a name="p32641445123710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p94173413410"><a name="p94173413410"></a><a name="p94173413410"></a>Specifies the field used for filtering based on the UUID of the mount path. This field is supported by API v2.35 and later versions.</p>
    </td>
    </tr>
    <tr id="row5872073713"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p4629451143719"><a name="p4629451143719"></a><a name="p4629451143719"></a>export_location_path</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p146291051143715"><a name="p146291051143715"></a><a name="p146291051143715"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p1662918516377"><a name="p1662918516377"></a><a name="p1662918516377"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p124171041194115"><a name="p124171041194115"></a><a name="p124171041194115"></a>Specifies the field used for filtering based on the mount path. This field is supported by API v2.35 and later versions.</p>
    </td>
    </tr>
    <tr id="row1794181619375"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p109811855113720"><a name="p109811855113720"></a><a name="p109811855113720"></a>name~</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p14981355123714"><a name="p14981355123714"></a><a name="p14981355123714"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p19811255103713"><a name="p19811255103713"></a><a name="p19811255103713"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p2981195518377"><a name="p2981195518377"></a><a name="p2981195518377"></a>Specifies the field used for fuzzy filtering based on the name of a shared file system. This field is supported by API v2.36 and later versions.</p>
    </td>
    </tr>
    <tr id="row166762318373"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p2053640203812"><a name="p2053640203812"></a><a name="p2053640203812"></a>description~</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p9536105381"><a name="p9536105381"></a><a name="p9536105381"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p115368018388"><a name="p115368018388"></a><a name="p115368018388"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p12536403388"><a name="p12536403388"></a><a name="p12536403388"></a>Specifies the field used for fuzzy filtering based on the description of a shared file system. This field is supported by API v2.36 and later versions.</p>
    </td>
    </tr>
    <tr id="row9931152817371"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.1 "><p id="p129105163813"><a name="p129105163813"></a><a name="p129105163813"></a>with_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.1.5.1.2 "><p id="p169114543816"><a name="p169114543816"></a><a name="p169114543816"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p15911159384"><a name="p15911159384"></a><a name="p15911159384"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p1591759388"><a name="p1591759388"></a><a name="p1591759388"></a>Specifies whether the number of queried shared file systems is returned. This field is supported by API v2.42 and later versions. This parameter is specified by <strong id="b1176483713510"><a name="b1176483713510"></a><a name="b1176483713510"></a>?with_count=true</strong> in the URI. The default value is <strong id="b14015507518"><a name="b14015507518"></a><a name="b14015507518"></a>false</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section31808412113213"></a>

-   Parameter description

    None


-   Example request

    GET https://\{endpoint\}/v2/16e1ab15c35a457e9c2b2aa189f544e1/shares


## Response<a name="section20475353113911"></a>

-   Parameter description

    <a name="tda30386a6e9d4540a4eb716742253a1b"></a>
    <table><thead align="left"><tr id="r8ada73019fa5407c8e16f6e1f7bc4bb1"><th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.1.4.1.1"><p id="p412618165533"><a name="p412618165533"></a><a name="p412618165533"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p16126216195320"><a name="p16126216195320"></a><a name="p16126216195320"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.519999999999996%" id="mcps1.1.4.1.3"><p id="p91267164531"><a name="p91267164531"></a><a name="p91267164531"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r1a20df0633434edc9d860eaf14b9a981"><td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.4.1.1 "><p id="a7a0494ee07fe4977b3a761e9700c2259"><a name="a7a0494ee07fe4977b3a761e9700c2259"></a><a name="a7a0494ee07fe4977b3a761e9700c2259"></a>shares</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p12755739205314"><a name="p12755739205314"></a><a name="p12755739205314"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.519999999999996%" headers="mcps1.1.4.1.3 "><p id="afa73e2f572e845479878686baa515ac2"><a name="afa73e2f572e845479878686baa515ac2"></a><a name="afa73e2f572e845479878686baa515ac2"></a>For details, see the description of the <strong id="b489314381680"><a name="b489314381680"></a><a name="b489314381680"></a>share</strong> field.</p>
    </td>
    </tr>
    <tr id="row153543017449"><td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.4.1.1 "><p id="p576242834212"><a name="p576242834212"></a><a name="p576242834212"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p15762142814219"><a name="p15762142814219"></a><a name="p15762142814219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.519999999999996%" headers="mcps1.1.4.1.3 "><p id="p16762162818429"><a name="p16762162818429"></a><a name="p16762162818429"></a>Specifies the number of returned shared file systems.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **share**  field

    <a name="tbcad918897d14fb49b92a4459d3f00fe"></a>
    <table><thead align="left"><tr id="r2549a099434b498b960a737e31dd5e22"><th class="cellrowborder" valign="top" width="16.83831616838316%" id="mcps1.1.4.1.1"><p id="p164075195530"><a name="p164075195530"></a><a name="p164075195530"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.227677232276772%" id="mcps1.1.4.1.2"><p id="p17407319185319"><a name="p17407319185319"></a><a name="p17407319185319"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.93400659934007%" id="mcps1.1.4.1.3"><p id="p740761935310"><a name="p740761935310"></a><a name="p740761935310"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r24e1fdd135614ddfb8bb62cd8b059790"><td class="cellrowborder" valign="top" width="16.83831616838316%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390791_p304425717377"><a name="en-us_topic_0064390791_p304425717377"></a><a name="en-us_topic_0064390791_p304425717377"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.227677232276772%" headers="mcps1.1.4.1.2 "><p id="a2739fe34fda84872ad4752a2a5904442"><a name="a2739fe34fda84872ad4752a2a5904442"></a><a name="a2739fe34fda84872ad4752a2a5904442"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.93400659934007%" headers="mcps1.1.4.1.3 "><p id="a8bd7dc44dfea4902ae6c3be200d16795"><a name="a8bd7dc44dfea4902ae6c3be200d16795"></a><a name="a8bd7dc44dfea4902ae6c3be200d16795"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="r363789c82fb941e5942a1a3569abd611"><td class="cellrowborder" valign="top" width="16.83831616838316%" headers="mcps1.1.4.1.1 "><p id="a9b70ba3dfb524a28b1b3308298b55cfe"><a name="a9b70ba3dfb524a28b1b3308298b55cfe"></a><a name="a9b70ba3dfb524a28b1b3308298b55cfe"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.227677232276772%" headers="mcps1.1.4.1.2 "><p id="p104941041105614"><a name="p104941041105614"></a><a name="p104941041105614"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.93400659934007%" headers="mcps1.1.4.1.3 "><p id="ab65a11ddbc14429399cc3444020b3e54"><a name="ab65a11ddbc14429399cc3444020b3e54"></a><a name="ab65a11ddbc14429399cc3444020b3e54"></a>Specifies the request link information of the shared file system.</p>
    </td>
    </tr>
    <tr id="reac38228b7ce4af8a38a972bfaa5ee93"><td class="cellrowborder" valign="top" width="16.83831616838316%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390791_p235133117377"><a name="en-us_topic_0064390791_p235133117377"></a><a name="en-us_topic_0064390791_p235133117377"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.227677232276772%" headers="mcps1.1.4.1.2 "><p id="ad559eba8660d4a39ba10681c9f2d174e"><a name="ad559eba8660d4a39ba10681c9f2d174e"></a><a name="ad559eba8660d4a39ba10681c9f2d174e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.93400659934007%" headers="mcps1.1.4.1.3 "><p id="a17d9eed397184e7a8eba7e87435d098a"><a name="a17d9eed397184e7a8eba7e87435d098a"></a><a name="a17d9eed397184e7a8eba7e87435d098a"></a>Specifies the name of the shared file system.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "count": 1,
        "shares": [
        {
            "id": "1390cb29-539b-4926-8953-d8d6b106071a",
            "links": [
            {
                "href": "https://192.168.196.47:8796/v2/f24555bfcf3146ca936d21bcb548687e/shares/1390cb29-539b-4926-8953-d8d6b106071a",
                "rel": "self"
            },
            {
                "href": "https://192.168.196.47:8796/f24555bfcf3146ca936d21bcb548687e/shares/1390cb29-539b-4926-8953-d8d6b106071a",
                "rel": "bookmark"
            }
            ],
            "name": null
        }
    ]
    }
    ```


## Status Codes<a name="section14343996114232"></a>

-   Normal

    200

-   Abnormal

    <a name="t2090d44083d34718a5469023c0c64add"></a>
    <table><thead align="left"><tr id="ra369a8c86fba486db6b80296100f3699"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="aef56a0bee1724b0993bff1e74bd97796"><a name="aef56a0bee1724b0993bff1e74bd97796"></a><a name="aef56a0bee1724b0993bff1e74bd97796"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="a7923be73f3d642c48f49e12d9f575dbd"><a name="a7923be73f3d642c48f49e12d9f575dbd"></a><a name="a7923be73f3d642c48f49e12d9f575dbd"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r9caf832a2eb74734a12db37bb5922e9c"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390791_p887409917377"><a name="en-us_topic_0064390791_p887409917377"></a><a name="en-us_topic_0064390791_p887409917377"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ac915b170d5f2455096491b02762241ac"><a name="ac915b170d5f2455096491b02762241ac"></a><a name="ac915b170d5f2455096491b02762241ac"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="r10cfd100de64484f99318a78375120ff"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a8193fd1ffce7479897c3de382c2eed15"><a name="a8193fd1ffce7479897c3de382c2eed15"></a><a name="a8193fd1ffce7479897c3de382c2eed15"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390791_p52210117377"><a name="en-us_topic_0064390791_p52210117377"></a><a name="en-us_topic_0064390791_p52210117377"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="r7a403b9870eb4da5b2a875a5b1539ffd"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="adbf7968a9dac42c49b53777be2aaf544"><a name="adbf7968a9dac42c49b53777be2aaf544"></a><a name="adbf7968a9dac42c49b53777be2aaf544"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a0bc87a6af4f1456e8086bde01aebec6b"><a name="a0bc87a6af4f1456e8086bde01aebec6b"></a><a name="a0bc87a6af4f1456e8086bde01aebec6b"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="r3422b1bb54164104949a1a121c137932"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a26dbdb35ea5c4d08b5c6ea8b184b8656"><a name="a26dbdb35ea5c4d08b5c6ea8b184b8656"></a><a name="a26dbdb35ea5c4d08b5c6ea8b184b8656"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="acf1017be1cb84275bbbb87052f6ab21a"><a name="acf1017be1cb84275bbbb87052f6ab21a"></a><a name="acf1017be1cb84275bbbb87052f6ab21a"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="r98d495bd3a4f4d0b87572a4bd4173ce1"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a8c7636bd87f64006979cb1f8fdf6bbcc"><a name="a8c7636bd87f64006979cb1f8fdf6bbcc"></a><a name="a8c7636bd87f64006979cb1f8fdf6bbcc"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a969e484ebb1d4f95a1c5d8803eb5805b"><a name="a969e484ebb1d4f95a1c5d8803eb5805b"></a><a name="a969e484ebb1d4f95a1c5d8803eb5805b"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="rde52d6cce4fb49bda58bd438829c8b74"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390791_p781488717377"><a name="en-us_topic_0064390791_p781488717377"></a><a name="en-us_topic_0064390791_p781488717377"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="afa6f5ee4d9d5461ca179b522cbea0d34"><a name="afa6f5ee4d9d5461ca179b522cbea0d34"></a><a name="afa6f5ee4d9d5461ca179b522cbea0d34"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="r101c5bbfb8784aa883c87c38ef66d1ba"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a4d23d1ea32c3487e8fa03fa7a39543d8"><a name="a4d23d1ea32c3487e8fa03fa7a39543d8"></a><a name="a4d23d1ea32c3487e8fa03fa7a39543d8"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390791_p300388217377"><a name="en-us_topic_0064390791_p300388217377"></a><a name="en-us_topic_0064390791_p300388217377"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="r6206a8382c46402ab86f280e940f1756"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a0c0a0346efed4a158e3f78aad3f92502"><a name="a0c0a0346efed4a158e3f78aad3f92502"></a><a name="a0c0a0346efed4a158e3f78aad3f92502"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390791_p752846017377"><a name="en-us_topic_0064390791_p752846017377"></a><a name="en-us_topic_0064390791_p752846017377"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="r1f59abfea4d945d5853b088375ec075b"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a4de368473ace407db9497a6d22044206"><a name="a4de368473ace407db9497a6d22044206"></a><a name="a4de368473ace407db9497a6d22044206"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a1e52611413ef42368e1fc74cedce0b14"><a name="a1e52611413ef42368e1fc74cedce0b14"></a><a name="a1e52611413ef42368e1fc74cedce0b14"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="r33f68eb575084d3d9c7a652797fa1d77"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a696b29b12cea423cbd6649f0ffd68db8"><a name="a696b29b12cea423cbd6649f0ffd68db8"></a><a name="a696b29b12cea423cbd6649f0ffd68db8"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ad20c3d1dc2b146f0a4632048769e0e72"><a name="ad20c3d1dc2b146f0a4632048769e0e72"></a><a name="ad20c3d1dc2b146f0a4632048769e0e72"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="rc1e0e831ad8742b6b88bdfea358028be"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="af622f29f0130447f8615637fb7feb757"><a name="af622f29f0130447f8615637fb7feb757"></a><a name="af622f29f0130447f8615637fb7feb757"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ac3e5fdea4e1d4f7c9d3668ee30ed96f7"><a name="ac3e5fdea4e1d4f7c9d3668ee30ed96f7"></a><a name="ac3e5fdea4e1d4f7c9d3668ee30ed96f7"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="r1ffb7ea16483434fbcdc681f373bb28d"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a636bca04b6c74339a4e3f28eaa7e32bc"><a name="a636bca04b6c74339a4e3f28eaa7e32bc"></a><a name="a636bca04b6c74339a4e3f28eaa7e32bc"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="af68a220ad6d3488cad0a0361f2f94967"><a name="af68a220ad6d3488cad0a0361f2f94967"></a><a name="af68a220ad6d3488cad0a0361f2f94967"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="r6658762006d1444084add1f582fae6bd"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a71922f19bd4b44a88fc41255846b5660"><a name="a71922f19bd4b44a88fc41255846b5660"></a><a name="a71922f19bd4b44a88fc41255846b5660"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390791_p361803117377"><a name="en-us_topic_0064390791_p361803117377"></a><a name="en-us_topic_0064390791_p361803117377"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="rec0c716ad62543e4ac5806fcb22b8c54"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a612773caf040494fa785db348dd7e335"><a name="a612773caf040494fa785db348dd7e335"></a><a name="a612773caf040494fa785db348dd7e335"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="aa509f60996454e90b1521e61e3da4d9d"><a name="aa509f60996454e90b1521e61e3da4d9d"></a><a name="aa509f60996454e90b1521e61e3da4d9d"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


