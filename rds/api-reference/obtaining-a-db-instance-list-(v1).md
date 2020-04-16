# Obtaining a DB Instance List<a name="en-us_topic_0056890053"></a>

## Function<a name="section36524518102048"></a>

This API is used to obtain a DB instance list.

## URI<a name="section51263775102048"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/instances

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table10271366102048"></a>
    <table><thead align="left"><tr id="row47701174102048"><th class="cellrowborder" valign="top" width="21.029999999999998%" id="mcps1.2.4.1.1"><p id="p4909390317443"><a name="p4909390317443"></a><a name="p4909390317443"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.73%" id="mcps1.2.4.1.2"><p id="p2043144817443"><a name="p2043144817443"></a><a name="p2043144817443"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.239999999999995%" id="mcps1.2.4.1.3"><p id="p6346699117443"><a name="p6346699117443"></a><a name="p6346699117443"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row105028141826"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.2.4.1.1 "><p id="p13174559113628"><a name="p13174559113628"></a><a name="p13174559113628"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.73%" headers="mcps1.2.4.1.2 "><p id="p60506382113628"><a name="p60506382113628"></a><a name="p60506382113628"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p2069905113628"><a name="p2069905113628"></a><a name="p2069905113628"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section7261641113422"></a>

None

## Normal Response<a name="section13572792102048"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table22623598113753"></a>
    <table><thead align="left"><tr id="row17747370113753"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.1"><p id="p28250852113753"><a name="p28250852113753"></a><a name="p28250852113753"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.93%" id="mcps1.2.4.1.2"><p id="p29359431113817"><a name="p29359431113817"></a><a name="p29359431113817"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.07%" id="mcps1.2.4.1.3"><p id="p29303715113817"><a name="p29303715113817"></a><a name="p29303715113817"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60503790113753"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p424441111380"><a name="p424441111380"></a><a name="p424441111380"></a>instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.93%" headers="mcps1.2.4.1.2 "><p id="p825302311380"><a name="p825302311380"></a><a name="p825302311380"></a>List data structure. For details, see <a href="#table13892167113923">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p53074421114057"><a name="p53074421114057"></a><a name="p53074421114057"></a>Indicates the DB instance information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instances field data structure description

    <a name="table2798610317111"></a>
    <table><thead align="left"><tr id="row2769032417111"><th class="cellrowborder" valign="top" width="27.1%" id="mcps1.2.4.1.1"><p id="p2832381017111"><a name="p2832381017111"></a><a name="p2832381017111"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.83%" id="mcps1.2.4.1.2"><p id="p1252728417111"><a name="p1252728417111"></a><a name="p1252728417111"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.07%" id="mcps1.2.4.1.3"><p id="p807710717111"><a name="p807710717111"></a><a name="p807710717111"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5026592617111"><td class="cellrowborder" valign="top" width="27.1%" headers="mcps1.2.4.1.1 "><p id="p4500821417111"><a name="p4500821417111"></a><a name="p4500821417111"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.83%" headers="mcps1.2.4.1.2 "><p id="p2178669817111"><a name="p2178669817111"></a><a name="p2178669817111"></a>Dictionary data structure. For details, see <a href="#table13892167113923">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p4481123517111"><a name="p4481123517111"></a><a name="p4481123517111"></a>Indicates the DB instance information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  instance field data structure description

    <a name="table13892167113923"></a>
    <table><thead align="left"><tr id="row20191590113923"><th class="cellrowborder" valign="top" width="27.29%" id="mcps1.2.4.1.1"><p id="p24906070113923"><a name="p24906070113923"></a><a name="p24906070113923"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.64%" id="mcps1.2.4.1.2"><p id="p37775651113940"><a name="p37775651113940"></a><a name="p37775651113940"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.07%" id="mcps1.2.4.1.3"><p id="p39928854113940"><a name="p39928854113940"></a><a name="p39928854113940"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19159393113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p1700482113933"><a name="p1700482113933"></a><a name="p1700482113933"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p3521345113933"><a name="p3521345113933"></a><a name="p3521345113933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p16793553113933"><a name="p16793553113933"></a><a name="p16793553113933"></a>Indicates the DB instance status.</p>
    <div class="p" id="p16231005500"><a name="p16231005500"></a><a name="p16231005500"></a>Value:<a name="ul3066104695748"></a><a name="ul3066104695748"></a><ul id="ul3066104695748"><li>If the value is <strong id="b84235270616547_1"><a name="b84235270616547_1"></a><a name="b84235270616547_1"></a>BUILD</strong>, the instance is being created.</li><li>If the value is <strong id="b842352706165415"><a name="b842352706165415"></a><a name="b842352706165415"></a>ACTIVE</strong>, the instance is normal.</li><li>If the value is <strong id="b842352706165427"><a name="b842352706165427"></a><a name="b842352706165427"></a>FAILED</strong>, the instance is abnormal.</li><li>If the value is <strong id="b84235270616547_3"><a name="b84235270616547_3"></a><a name="b84235270616547_3"></a>MODIFYING</strong>, the instance is being scaled up.</li><li>If the value is <strong id="b84235270616547_5"><a name="b84235270616547_5"></a><a name="b84235270616547_5"></a>REBOOTING</strong>, the instance is being rebooted.</li><li>If the value is <strong id="b84235270616547_7"><a name="b84235270616547_7"></a><a name="b84235270616547_7"></a>RESTORING</strong>, the instance is being restored.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row20624439113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p18100570113933"><a name="p18100570113933"></a><a name="p18100570113933"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p56860035113933"><a name="p56860035113933"></a><a name="p56860035113933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p42260084113933"><a name="p42260084113933"></a><a name="p42260084113933"></a>Indicates the DB instance name.</p>
    </td>
    </tr>
    <tr id="row51007855113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p514774113933"><a name="p514774113933"></a><a name="p514774113933"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p41696720113933"><a name="p41696720113933"></a><a name="p41696720113933"></a>List data structure. For details, see <a href="#table26919596115413">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p21991179113933"><a name="p21991179113933"></a><a name="p21991179113933"></a>Indicates the link address.</p>
    </td>
    </tr>
    <tr id="row18449512113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p36455087113933"><a name="p36455087113933"></a><a name="p36455087113933"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p72034113933"><a name="p72034113933"></a><a name="p72034113933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p5834831113933"><a name="p5834831113933"></a><a name="p5834831113933"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row56351242113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p2859292113933"><a name="p2859292113933"></a><a name="p2859292113933"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p30276081113933"><a name="p30276081113933"></a><a name="p30276081113933"></a>Dictionary data structure. For details, see <a href="#table47858865115627">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p36443511113933"><a name="p36443511113933"></a><a name="p36443511113933"></a>Indicates the volume information.</p>
    </td>
    </tr>
    <tr id="row878722113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p66243285113933"><a name="p66243285113933"></a><a name="p66243285113933"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p64105908113933"><a name="p64105908113933"></a><a name="p64105908113933"></a>Dictionary data structure. For details, see <a href="#table45121734115759">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p25196092113933"><a name="p25196092113933"></a><a name="p25196092113933"></a>Indicates the DB instance specifications.</p>
    </td>
    </tr>
    <tr id="row9224457113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p27617556113933"><a name="p27617556113933"></a><a name="p27617556113933"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p22429540113933"><a name="p22429540113933"></a><a name="p22429540113933"></a>Dictionary data structure. For details, see <a href="#table25266871114925">Table 8</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p4853461113933"><a name="p4853461113933"></a><a name="p4853461113933"></a>Indicates the database information.</p>
    </td>
    </tr>
    <tr id="row40203164113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p57586062113933"><a name="p57586062113933"></a><a name="p57586062113933"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p33959480113933"><a name="p33959480113933"></a><a name="p33959480113933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p66363387113933"><a name="p66363387113933"></a><a name="p66363387113933"></a>Indicates the region where the DB instance is deployed.</p>
    </td>
    </tr>
    <tr id="row41260228113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p6725246113933"><a name="p6725246113933"></a><a name="p6725246113933"></a>ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p7874025113933"><a name="p7874025113933"></a><a name="p7874025113933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p33816293113933"><a name="p33816293113933"></a><a name="p33816293113933"></a>Indicates the DB instance IP address.</p>
    </td>
    </tr>
    <tr id="row30225743113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p54765209113933"><a name="p54765209113933"></a><a name="p54765209113933"></a>replica_of</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p6796974113933"><a name="p6796974113933"></a><a name="p6796974113933"></a>Dictionary data structure. For details, see <a href="#table2070063511535">Table 9</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p13684044113933"><a name="p13684044113933"></a><a name="p13684044113933"></a>Indicates the primary DB instance ID corresponding to the read replica.</p>
    </td>
    </tr>
    <tr id="row24190140113923"><td class="cellrowborder" valign="top" width="27.29%" headers="mcps1.2.4.1.1 "><p id="p56462656113933"><a name="p56462656113933"></a><a name="p56462656113933"></a>hostname</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.64%" headers="mcps1.2.4.1.2 "><p id="p10072423113933"><a name="p10072423113933"></a><a name="p10072423113933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.07%" headers="mcps1.2.4.1.3 "><p id="p57893957153621"><a name="p57893957153621"></a><a name="p57893957153621"></a>Indicates the domain name. Its value is <strong id="b842352706141227"><a name="b842352706141227"></a><a name="b842352706141227"></a>null</strong>.</p>
    <p id="p10559926113933"><a name="p10559926113933"></a><a name="p10559926113933"></a>Currently, this parameter is not supported.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  links field data structure description

    <a name="table26919596115413"></a>
    <table><thead align="left"><tr id="row44057485115413"><th class="cellrowborder" valign="top" width="27.35%" id="mcps1.2.4.1.1"><p id="p11886518115413"><a name="p11886518115413"></a><a name="p11886518115413"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.39%" id="mcps1.2.4.1.2"><p id="p31336353115426"><a name="p31336353115426"></a><a name="p31336353115426"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.26%" id="mcps1.2.4.1.3"><p id="p55216670115426"><a name="p55216670115426"></a><a name="p55216670115426"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37663412115413"><td class="cellrowborder" valign="top" width="27.35%" headers="mcps1.2.4.1.1 "><p id="p35317088115420"><a name="p35317088115420"></a><a name="p35317088115420"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.39%" headers="mcps1.2.4.1.2 "><p id="p42111909115420"><a name="p42111909115420"></a><a name="p42111909115420"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.3 "><p id="p55621491115420"><a name="p55621491115420"></a><a name="p55621491115420"></a>Its value is <strong id="b842352706173121"><a name="b842352706173121"></a><a name="b842352706173121"></a>self</strong> or <strong id="b842352706173123"><a name="b842352706173123"></a><a name="b842352706173123"></a>bookmark</strong>.</p>
    </td>
    </tr>
    <tr id="row56851695115354"><td class="cellrowborder" valign="top" width="27.35%" headers="mcps1.2.4.1.1 "><p id="p5682579711546"><a name="p5682579711546"></a><a name="p5682579711546"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.39%" headers="mcps1.2.4.1.2 "><p id="p3948688111546"><a name="p3948688111546"></a><a name="p3948688111546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.26%" headers="mcps1.2.4.1.3 "><p id="p4432076011546"><a name="p4432076011546"></a><a name="p4432076011546"></a>Its value is <strong id="b842352706121418"><a name="b842352706121418"></a><a name="b842352706121418"></a>""</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  volume field data structure description

    <a name="table47858865115627"></a>
    <table><thead align="left"><tr id="row38235811115627"><th class="cellrowborder" valign="top" width="27.12%" id="mcps1.2.4.1.1"><p id="p2631636115657"><a name="p2631636115657"></a><a name="p2631636115657"></a><strong id="b84235270691445_13"><a name="b84235270691445_13"></a><a name="b84235270691445_13"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.160000000000004%" id="mcps1.2.4.1.2"><p id="p11836002115657"><a name="p11836002115657"></a><a name="p11836002115657"></a><strong id="b842352706164541_9"><a name="b842352706164541_9"></a><a name="b842352706164541_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.72%" id="mcps1.2.4.1.3"><p id="p19192116115657"><a name="p19192116115657"></a><a name="p19192116115657"></a><strong id="b842352706163417_13"><a name="b842352706163417_13"></a><a name="b842352706163417_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46055645115627"><td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.1 "><p id="p48601022115650"><a name="p48601022115650"></a><a name="p48601022115650"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.160000000000004%" headers="mcps1.2.4.1.2 "><p id="p44368671115650"><a name="p44368671115650"></a><a name="p44368671115650"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.72%" headers="mcps1.2.4.1.3 "><p id="p37092593115650"><a name="p37092593115650"></a><a name="p37092593115650"></a>Indicates the volume type.</p>
    </td>
    </tr>
    <tr id="row32945781115420"><td class="cellrowborder" valign="top" width="27.12%" headers="mcps1.2.4.1.1 "><p id="p49608823115430"><a name="p49608823115430"></a><a name="p49608823115430"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.160000000000004%" headers="mcps1.2.4.1.2 "><p id="p58891736115430"><a name="p58891736115430"></a><a name="p58891736115430"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.72%" headers="mcps1.2.4.1.3 "><p id="p5501313115430"><a name="p5501313115430"></a><a name="p5501313115430"></a>Indicates the volume size.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  flavor field data structure description

    <a name="table45121734115759"></a>
    <table><thead align="left"><tr id="row66369319115759"><th class="cellrowborder" valign="top" width="27.077292270772922%" id="mcps1.2.4.1.1"><p id="p7205782115759"><a name="p7205782115759"></a><a name="p7205782115759"></a><strong id="b84235270691445_15"><a name="b84235270691445_15"></a><a name="b84235270691445_15"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.27587241275872%" id="mcps1.2.4.1.2"><p id="p46797465115759"><a name="p46797465115759"></a><a name="p46797465115759"></a><strong id="b842352706164541_11"><a name="b842352706164541_11"></a><a name="b842352706164541_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.64683531646835%" id="mcps1.2.4.1.3"><p id="p32498329115759"><a name="p32498329115759"></a><a name="p32498329115759"></a><strong id="b842352706163417_15"><a name="b842352706163417_15"></a><a name="b842352706163417_15"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15118973115759"><td class="cellrowborder" valign="top" width="27.077292270772922%" headers="mcps1.2.4.1.1 "><p id="p16677294115759"><a name="p16677294115759"></a><a name="p16677294115759"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.27587241275872%" headers="mcps1.2.4.1.2 "><p id="p8683539115759"><a name="p8683539115759"></a><a name="p8683539115759"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.64683531646835%" headers="mcps1.2.4.1.3 "><p id="p32278036115759"><a name="p32278036115759"></a><a name="p32278036115759"></a>Indicates the specification ID.</p>
    </td>
    </tr>
    <tr id="row22066875115759"><td class="cellrowborder" valign="top" width="27.077292270772922%" headers="mcps1.2.4.1.1 "><p id="p42586483115759"><a name="p42586483115759"></a><a name="p42586483115759"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.27587241275872%" headers="mcps1.2.4.1.2 "><p id="p36228097173722"><a name="p36228097173722"></a><a name="p36228097173722"></a>List data structure. For details, see <a href="#table26919596115413">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.64683531646835%" headers="mcps1.2.4.1.3 "><p id="p36499162173722"><a name="p36499162173722"></a><a name="p36499162173722"></a>Indicates the link address.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  datastore field data structure description

    <a name="table25266871114925"></a>
    <table><thead align="left"><tr id="row38909932114925"><th class="cellrowborder" valign="top" width="26.840000000000003%" id="mcps1.2.4.1.1"><p id="p64696753114925"><a name="p64696753114925"></a><a name="p64696753114925"></a><strong id="b84235270691445_17"><a name="b84235270691445_17"></a><a name="b84235270691445_17"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.53%" id="mcps1.2.4.1.2"><p id="p53345150115013"><a name="p53345150115013"></a><a name="p53345150115013"></a><strong id="b842352706164541_13"><a name="b842352706164541_13"></a><a name="b842352706164541_13"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.630000000000003%" id="mcps1.2.4.1.3"><p id="p25989888115013"><a name="p25989888115013"></a><a name="p25989888115013"></a><strong id="b842352706163417_17"><a name="b842352706163417_17"></a><a name="b842352706163417_17"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36381481114925"><td class="cellrowborder" valign="top" width="26.840000000000003%" headers="mcps1.2.4.1.1 "><p id="p1773920111507"><a name="p1773920111507"></a><a name="p1773920111507"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.53%" headers="mcps1.2.4.1.2 "><p id="p2758918711507"><a name="p2758918711507"></a><a name="p2758918711507"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.3 "><p id="p2013169811507"><a name="p2013169811507"></a><a name="p2013169811507"></a>Indicates the DB engine type.</p>
    </td>
    </tr>
    <tr id="row24365299114925"><td class="cellrowborder" valign="top" width="26.840000000000003%" headers="mcps1.2.4.1.1 "><p id="p2005483711507"><a name="p2005483711507"></a><a name="p2005483711507"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.53%" headers="mcps1.2.4.1.2 "><p id="p1382910911507"><a name="p1382910911507"></a><a name="p1382910911507"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.3 "><p id="p4641602511507"><a name="p4641602511507"></a><a name="p4641602511507"></a>Indicates the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  replica\_of field data structure description

    <a name="table2070063511535"></a>
    <table><thead align="left"><tr id="row1017359011535"><th class="cellrowborder" valign="top" width="26.93%" id="mcps1.2.4.1.1"><p id="p1875447211535"><a name="p1875447211535"></a><a name="p1875447211535"></a><strong id="b84235270691445_19"><a name="b84235270691445_19"></a><a name="b84235270691445_19"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.42%" id="mcps1.2.4.1.2"><p id="p42146161115320"><a name="p42146161115320"></a><a name="p42146161115320"></a><strong id="b842352706164541_15"><a name="b842352706164541_15"></a><a name="b842352706164541_15"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.65%" id="mcps1.2.4.1.3"><p id="p58395846115320"><a name="p58395846115320"></a><a name="p58395846115320"></a><strong id="b842352706163417_19"><a name="b842352706163417_19"></a><a name="b842352706163417_19"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5934370811535"><td class="cellrowborder" valign="top" width="26.93%" headers="mcps1.2.4.1.1 "><p id="p31671150115314"><a name="p31671150115314"></a><a name="p31671150115314"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.42%" headers="mcps1.2.4.1.2 "><p id="p15226378115314"><a name="p15226378115314"></a><a name="p15226378115314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.3 "><p id="p25377139115314"><a name="p25377139115314"></a><a name="p25377139115314"></a>Indicates the primary DB instance ID.</p>
    </td>
    </tr>
    <tr id="row2921722111535"><td class="cellrowborder" valign="top" width="26.93%" headers="mcps1.2.4.1.1 "><p id="p42282384115314"><a name="p42282384115314"></a><a name="p42282384115314"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.42%" headers="mcps1.2.4.1.2 "><p id="p2321098115314"><a name="p2321098115314"></a><a name="p2321098115314"></a>List data structure. For details, see <a href="#table26919596115413">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.3 "><p id="p53791240115314"><a name="p53791240115314"></a><a name="p53791240115314"></a>Indicates the link address.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "instances": [
        {
          "instance": {
            "status": "ACTIVE",
            "name": "rds-new-channle-read",
            "links": [
              {
                "rel": "self",
                "href": ""
              },
              {
                "rel": "bookmark",
                "href": ""
              }
            ],
            "id": "37f52707-2fb3-482c-a444-77a70a4eafd6",
            "volume": {
              "type": "COMMON",
              "size": 100
            },
            "flavor": {
              "id": "7fbf27c5-07e5-43dc-cf13-ad7a0f1c5d9a",
              "links": [
                {
                  "rel": "self",
                  "href": ""
                },
                {
                  "rel": "bookmark",
                  "href": ""
                }
              ]
            },
            "datastore": {
              "type": "PostgreSQL",
              "version": "PostgreSQL-9.5.5"
            },
            
            "region": "eu-de",
            "ip": "192.168.1.29",
            "replica_of": [
              {
                "id": "c42cdd29-9912-4b57-91a8-c37a845566b1",
                "links": [
                  {
                    "rel": "self",
                    "href": ""
                  },
                  {
                    "rel": "bookmark",
                    "href": ""
                  }
                ]
              }
            ],
            "hostname": null
          }
        }
      ]
    }
    ```


## Abnormal Response<a name="section64738761102048"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

