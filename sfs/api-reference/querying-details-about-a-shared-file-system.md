# Querying Details About a Shared File System<a name="sfs_02_0024"></a>

## Function<a name="sa35e3b1b802c440d80b01848e6abb0d8"></a>

This API is used to query the details about a shared file system.

## URI<a name="s734971f486b940efb4775991bc6247df"></a>

-   GET /v2/\{project\_id\}/shares/\{share\_id\}
-   Parameter description

    <a name="en-us_topic_0064390794_table35026424"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390794_row976457"><th class="cellrowborder" valign="top" width="16.458354164583543%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.408659134086594%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.217978202179786%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.91500849915009%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390794_row47357582"><td class="cellrowborder" valign="top" width="16.458354164583543%" headers="mcps1.1.5.1.1 "><p id="aac7ff468e5e141eb8d10c5b8d84aae9b"><a name="aac7ff468e5e141eb8d10c5b8d84aae9b"></a><a name="aac7ff468e5e141eb8d10c5b8d84aae9b"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.408659134086594%" headers="mcps1.1.5.1.2 "><p id="a90b78ed430914480bb4a3a8be3351c7e"><a name="a90b78ed430914480bb4a3a8be3351c7e"></a><a name="a90b78ed430914480bb4a3a8be3351c7e"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.217978202179786%" headers="mcps1.1.5.1.3 "><p id="a3c76a7e2f5ca45a29064883c4f0cd175"><a name="a3c76a7e2f5ca45a29064883c4f0cd175"></a><a name="a3c76a7e2f5ca45a29064883c4f0cd175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.91500849915009%" headers="mcps1.1.5.1.4 "><p id="a5fbbf92ea611436eb7ab37750fd212a4"><a name="a5fbbf92ea611436eb7ab37750fd212a4"></a><a name="a5fbbf92ea611436eb7ab37750fd212a4"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row20038698"><td class="cellrowborder" valign="top" width="16.458354164583543%" headers="mcps1.1.5.1.1 "><p id="a007bb5af73844806a205886365c1ea38"><a name="a007bb5af73844806a205886365c1ea38"></a><a name="a007bb5af73844806a205886365c1ea38"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.408659134086594%" headers="mcps1.1.5.1.2 "><p id="a9c15a356d77a497d8b2206784ea1cf8d"><a name="a9c15a356d77a497d8b2206784ea1cf8d"></a><a name="a9c15a356d77a497d8b2206784ea1cf8d"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.217978202179786%" headers="mcps1.1.5.1.3 "><p id="a1e454347116f4d32a6ddab1f23458dea"><a name="a1e454347116f4d32a6ddab1f23458dea"></a><a name="a1e454347116f4d32a6ddab1f23458dea"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.91500849915009%" headers="mcps1.1.5.1.4 "><p id="a4f33abc5c1084642a0be5319cf1f297a"><a name="a4f33abc5c1084642a0be5319cf1f297a"></a><a name="a4f33abc5c1084642a0be5319cf1f297a"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="secb9b5ca6f8a494db9a8aae54bcdddb1"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="sb8a94205fc72482cb8e91f6c75aa6f0f"></a>

-   Parameter description

    <a name="en-us_topic_0064390794_table35656026"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390794_row59925661"><th class="cellrowborder" valign="top" width="19.43%" id="mcps1.1.4.1.1"><p id="p183391214165618"><a name="p183391214165618"></a><a name="p183391214165618"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.99%" id="mcps1.1.4.1.2"><p id="p6339191412567"><a name="p6339191412567"></a><a name="p6339191412567"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.4.1.3"><p id="p143551414135616"><a name="p143551414135616"></a><a name="p143551414135616"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390794_row26965262"><td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.4.1.1 "><p id="ad48aad8630094c7f8ca05c2593b65a90"><a name="ad48aad8630094c7f8ca05c2593b65a90"></a><a name="ad48aad8630094c7f8ca05c2593b65a90"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.1.4.1.2 "><p id="ab99bca782d874b3380113625859621af"><a name="ab99bca782d874b3380113625859621af"></a><a name="ab99bca782d874b3380113625859621af"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.4.1.3 "><p id="adbde64fb91f64349abb9c7d8f91dffe5"><a name="adbde64fb91f64349abb9c7d8f91dffe5"></a><a name="adbde64fb91f64349abb9c7d8f91dffe5"></a>Specifies the share object.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **share**  field

    <a name="table865635334010"></a>
    <table><thead align="left"><tr id="row66561053144018"><th class="cellrowborder" valign="top" width="18.87%" id="mcps1.1.4.1.1"><p id="p3656853114011"><a name="p3656853114011"></a><a name="p3656853114011"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.939999999999998%" id="mcps1.1.4.1.2"><p id="p9656753184012"><a name="p9656753184012"></a><a name="p9656753184012"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.19%" id="mcps1.1.4.1.3"><p id="p96561453184014"><a name="p96561453184014"></a><a name="p96561453184014"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18656155374012"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p28090732115456"><a name="en-us_topic_0064390794_p28090732115456"></a><a name="en-us_topic_0064390794_p28090732115456"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p60756818115456"><a name="en-us_topic_0064390794_p60756818115456"></a><a name="en-us_topic_0064390794_p60756818115456"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p53809467171857"><a name="en-us_topic_0064390794_p53809467171857"></a><a name="en-us_topic_0064390794_p53809467171857"></a>Specifies the links of shared file systems.</p>
    </td>
    </tr>
    <tr id="row6656205311402"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p20630446115456"><a name="en-us_topic_0064390794_p20630446115456"></a><a name="en-us_topic_0064390794_p20630446115456"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p60453459115456"><a name="en-us_topic_0064390794_p60453459115456"></a><a name="en-us_topic_0064390794_p60453459115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p35525415171857"><a name="en-us_topic_0064390794_p35525415171857"></a><a name="en-us_topic_0064390794_p35525415171857"></a>Specifies the availability zone.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row5492535895012"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1976898095012"><a name="en-us_topic_0064390794_p1976898095012"></a><a name="en-us_topic_0064390794_p1976898095012"></a>share_server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p4995572295012"><a name="en-us_topic_0064390794_p4995572295012"></a><a name="en-us_topic_0064390794_p4995572295012"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1988170695012"><a name="en-us_topic_0064390794_p1988170695012"></a><a name="en-us_topic_0064390794_p1988170695012"></a>Specifies the UUID for managing share services.</p>
    </td>
    </tr>
    <tr id="row5656135314017"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p27750209115456"><a name="en-us_topic_0064390794_p27750209115456"></a><a name="en-us_topic_0064390794_p27750209115456"></a>share_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p33174447115456"><a name="en-us_topic_0064390794_p33174447115456"></a><a name="en-us_topic_0064390794_p33174447115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p59674002171857"><a name="en-us_topic_0064390794_p59674002171857"></a><a name="en-us_topic_0064390794_p59674002171857"></a>Specifies the UUID of the share network. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row39279891115440"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p39186779115456"><a name="en-us_topic_0064390794_p39186779115456"></a><a name="en-us_topic_0064390794_p39186779115456"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p20012545115456"><a name="en-us_topic_0064390794_p20012545115456"></a><a name="en-us_topic_0064390794_p20012545115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p17092907171857"><a name="en-us_topic_0064390794_p17092907171857"></a><a name="en-us_topic_0064390794_p17092907171857"></a>Specifies the UUID of the source snapshot that is used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row5321904710035"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1577556910035"><a name="en-us_topic_0064390794_p1577556910035"></a><a name="en-us_topic_0064390794_p1577556910035"></a>snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2164239410035"><a name="en-us_topic_0064390794_p2164239410035"></a><a name="en-us_topic_0064390794_p2164239410035"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p206571653164019"><a name="p206571653164019"></a><a name="p206571653164019"></a>Specifies whether snapshots are supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.2 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row66254026115429"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66240344115456"><a name="en-us_topic_0064390794_p66240344115456"></a><a name="en-us_topic_0064390794_p66240344115456"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p63867663115456"><a name="en-us_topic_0064390794_p63867663115456"></a><a name="en-us_topic_0064390794_p63867663115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p45589478171857"><a name="en-us_topic_0064390794_p45589478171857"></a><a name="en-us_topic_0064390794_p45589478171857"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row25775244115437"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p57485250115456"><a name="en-us_topic_0064390794_p57485250115456"></a><a name="en-us_topic_0064390794_p57485250115456"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p25793701115456"><a name="en-us_topic_0064390794_p25793701115456"></a><a name="en-us_topic_0064390794_p25793701115456"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p42544068172855"><a name="en-us_topic_0064390794_p42544068172855"></a><a name="en-us_topic_0064390794_p42544068172855"></a>Specifies the size (GB) of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row2811743793851"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p206584533405"><a name="p206584533405"></a><a name="p206584533405"></a>share_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p1465875384011"><a name="p1465875384011"></a><a name="p1465875384011"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p86584538409"><a name="p86584538409"></a><a name="p86584538409"></a>Specifies the UUID of the consistency group. This parameter is reserved, because consistency groups are not supported currently. This field is supported by API versions from v2.31 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row14146850115432"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p43647722115456"><a name="en-us_topic_0064390794_p43647722115456"></a><a name="en-us_topic_0064390794_p43647722115456"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p45804593115456"><a name="en-us_topic_0064390794_p45804593115456"></a><a name="en-us_topic_0064390794_p45804593115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p36017679171857"><a name="en-us_topic_0064390794_p36017679171857"></a><a name="en-us_topic_0064390794_p36017679171857"></a>Specifies the UUID of the project to which the shared file system belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row27677209115427"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p30561506115456"><a name="en-us_topic_0064390794_p30561506115456"></a><a name="en-us_topic_0064390794_p30561506115456"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p59562882115456"><a name="en-us_topic_0064390794_p59562882115456"></a><a name="en-us_topic_0064390794_p59562882115456"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390792_p42083247173855"><a name="en-us_topic_0064390792_p42083247173855"></a><a name="en-us_topic_0064390792_p42083247173855"></a>Sets one or more metadata key and value pairs as a dictionary of strings. <strong id="b184781248290"><a name="b184781248290"></a><a name="b184781248290"></a>share_used</strong> is the key, and the corresponding value is the used capacity of the shared file system in the unit of Bytes. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row21024096115415"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p23577146115456"><a name="en-us_topic_0064390794_p23577146115456"></a><a name="en-us_topic_0064390794_p23577146115456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p30700686115456"><a name="en-us_topic_0064390794_p30700686115456"></a><a name="en-us_topic_0064390794_p30700686115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p9195044171857"><a name="en-us_topic_0064390794_p9195044171857"></a><a name="en-us_topic_0064390794_p9195044171857"></a>Specifies the status of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row665580195924"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p265919537402"><a name="p265919537402"></a><a name="p265919537402"></a>task_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p5905231595924"><a name="en-us_topic_0064390794_p5905231595924"></a><a name="en-us_topic_0064390794_p5905231595924"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1850821095924"><a name="en-us_topic_0064390794_p1850821095924"></a><a name="en-us_topic_0064390794_p1850821095924"></a>Specifies the data migration status. This parameter is reserved, because data migration is not supported currently. This field is supported by API v2.5 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row939599610316"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p2287823910316"><a name="en-us_topic_0064390794_p2287823910316"></a><a name="en-us_topic_0064390794_p2287823910316"></a>has_replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p4870772510316"><a name="en-us_topic_0064390794_p4870772510316"></a><a name="en-us_topic_0064390794_p4870772510316"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p5301165710316"><a name="en-us_topic_0064390794_p5301165710316"></a><a name="en-us_topic_0064390794_p5301165710316"></a>Specifies whether replicas exist. This parameter is reserved, because replication is not supported currently. This field is supported by API versions from v2.11 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row48841735810"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1388510311817"><a name="en-us_topic_0064390794_p1388510311817"></a><a name="en-us_topic_0064390794_p1388510311817"></a>replication_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p1366065374015"><a name="p1366065374015"></a><a name="p1366065374015"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p7660135312409"><a name="p7660135312409"></a><a name="p7660135312409"></a>Specifies the replication type. This parameter is reserved, because replication is not supported currently. This field is supported by API versions from v2.11 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row38372338115421"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p61202789115456"><a name="en-us_topic_0064390794_p61202789115456"></a><a name="en-us_topic_0064390794_p61202789115456"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p58478870115456"><a name="en-us_topic_0064390794_p58478870115456"></a><a name="en-us_topic_0064390794_p58478870115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p59409689171857"><a name="en-us_topic_0064390794_p59409689171857"></a><a name="en-us_topic_0064390794_p59409689171857"></a>Describes the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row35274029115424"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p58169755115456"><a name="en-us_topic_0064390794_p58169755115456"></a><a name="en-us_topic_0064390794_p58169755115456"></a>host</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p14129699115456"><a name="en-us_topic_0064390794_p14129699115456"></a><a name="en-us_topic_0064390794_p14129699115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p24446366171857"><a name="en-us_topic_0064390794_p24446366171857"></a><a name="en-us_topic_0064390794_p24446366171857"></a>Specifies the name of the host. This field is visible only to the administrator.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row10855127115417"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66003741115456"><a name="en-us_topic_0064390794_p66003741115456"></a><a name="en-us_topic_0064390794_p66003741115456"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p44702790115456"><a name="en-us_topic_0064390794_p44702790115456"></a><a name="en-us_topic_0064390794_p44702790115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p37552527171857"><a name="en-us_topic_0064390794_p37552527171857"></a><a name="en-us_topic_0064390794_p37552527171857"></a>Specifies the name of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row6259894411544"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66214260115456"><a name="en-us_topic_0064390794_p66214260115456"></a><a name="en-us_topic_0064390794_p66214260115456"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p61754840115456"><a name="en-us_topic_0064390794_p61754840115456"></a><a name="en-us_topic_0064390794_p61754840115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p62484878171857"><a name="en-us_topic_0064390794_p62484878171857"></a><a name="en-us_topic_0064390794_p62484878171857"></a>Specifies the date and time stamp when the shared file system was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row2256685795641"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1597610695641"><a name="en-us_topic_0064390794_p1597610695641"></a><a name="en-us_topic_0064390794_p1597610695641"></a>access_rules_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p6230051595641"><a name="en-us_topic_0064390794_p6230051595641"></a><a name="en-us_topic_0064390794_p6230051595641"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1317697095641"><a name="en-us_topic_0064390794_p1317697095641"></a><a name="en-us_topic_0064390794_p1317697095641"></a>Specifies the configuration status of the access rule. Possible values are <strong id="b19546203419592"><a name="b19546203419592"></a><a name="b19546203419592"></a>active</strong> (effective), <strong id="b1754703465911"><a name="b1754703465911"></a><a name="b1754703465911"></a>error</strong> (configuration failed), and <strong id="b12548163412590"><a name="b12548163412590"></a><a name="b12548163412590"></a>syncing</strong> (configuration in progress). This field is supported by API v2.10 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row66328432115411"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p11825073115456"><a name="en-us_topic_0064390794_p11825073115456"></a><a name="en-us_topic_0064390794_p11825073115456"></a>share_proto</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p18306875115456"><a name="en-us_topic_0064390794_p18306875115456"></a><a name="en-us_topic_0064390794_p18306875115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p51666373171857"><a name="en-us_topic_0064390794_p51666373171857"></a><a name="en-us_topic_0064390794_p51666373171857"></a>Specifies the protocol for sharing file systems.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1997612012118"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p866120531402"><a name="p866120531402"></a><a name="p866120531402"></a>share_type_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p6682275212118"><a name="en-us_topic_0064390794_p6682275212118"></a><a name="en-us_topic_0064390794_p6682275212118"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p55872650172937"><a name="en-us_topic_0064390794_p55872650172937"></a><a name="en-us_topic_0064390794_p55872650172937"></a>Specifies the storage service type assigned for the shared file system, such as high-performance storage (composed of SSDs) and large-capacity storage (composed of SATA disks). This field is supported by API v2.6 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row6380688295244"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p1661195316408"><a name="p1661195316408"></a><a name="p1661195316408"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2135204095244"><a name="en-us_topic_0064390794_p2135204095244"></a><a name="en-us_topic_0064390794_p2135204095244"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p5179364095244"><a name="en-us_topic_0064390794_p5179364095244"></a><a name="en-us_topic_0064390794_p5179364095244"></a>Specifies the UUID of the share type.</p>
    </td>
    </tr>
    <tr id="row356045811811"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p945114017196"><a name="p945114017196"></a><a name="p945114017196"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p54519014190"><a name="p54519014190"></a><a name="p54519014190"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p114511106197"><a name="p114511106197"></a><a name="p114511106197"></a>Specifies the volume type. The definition of this parameter is the same as that of <strong id="b189076474597"><a name="b189076474597"></a><a name="b189076474597"></a>share_type</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1256499495932"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p3662553154018"><a name="p3662553154018"></a><a name="p3662553154018"></a>export_locations</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p666212536404"><a name="p666212536404"></a><a name="p666212536404"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p366245394013"><a name="p366245394013"></a><a name="p366245394013"></a>Lists the mount locations. Currently, only a single mount location is supported. This parameter exists only when <strong id="b127413522592"><a name="b127413522592"></a><a name="b127413522592"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b5275165210593"><a name="b5275165210593"></a><a name="b5275165210593"></a>2.9</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1105050495936"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p136621153164018"><a name="p136621153164018"></a><a name="p136621153164018"></a>export_location</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p15662253204012"><a name="p15662253204012"></a><a name="p15662253204012"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p7662115334014"><a name="p7662115334014"></a><a name="p7662115334014"></a>Specifies the mount location. This parameter exists only when <strong id="b0632175595913"><a name="b0632175595913"></a><a name="b0632175595913"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b763335519596"><a name="b763335519596"></a><a name="b763335519596"></a>2.9</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row760346112115"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1190063912115"><a name="en-us_topic_0064390794_p1190063912115"></a><a name="en-us_topic_0064390794_p1190063912115"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2442773012115"><a name="en-us_topic_0064390794_p2442773012115"></a><a name="en-us_topic_0064390794_p2442773012115"></a>bool</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p19950543172949"><a name="en-us_topic_0064390794_p19950543172949"></a><a name="en-us_topic_0064390794_p19950543172949"></a>Specifies the visibility level of the shared file system. If it is set to <strong id="b1629310588596"><a name="b1629310588596"></a><a name="b1629310588596"></a>true</strong>, the file system can be seen publicly. If it is set to <strong id="b11294155810597"><a name="b11294155810597"></a><a name="b11294155810597"></a>false</strong>, the file system can be seen privately. The default value is <strong id="b52945581598"><a name="b52945581598"></a><a name="b52945581598"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row138591369913"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p116621253104020"><a name="p116621253104020"></a><a name="p116621253104020"></a>source_share_group_snapshot_member_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p1486018614919"><a name="en-us_topic_0064390794_p1486018614919"></a><a name="en-us_topic_0064390794_p1486018614919"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p11663125315409"><a name="p11663125315409"></a><a name="p11663125315409"></a>Specifies the UUID of the snapshot's source. This parameter is reserved, because consistency snapshots are not supported currently. This field is supported by API v2.31 and later versions.</p>
    </td>
    </tr>
    <tr id="row10663153174013"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p36631453184015"><a name="p36631453184015"></a><a name="p36631453184015"></a>revert_to_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p176631153144013"><a name="p176631153144013"></a><a name="p176631153144013"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p5663205374018"><a name="p5663205374018"></a><a name="p5663205374018"></a>Specifies whether rollback from snapshot is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.27 and later versions.</p>
    </td>
    </tr>
    <tr id="row146631553184010"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p366385320408"><a name="p366385320408"></a><a name="p366385320408"></a>create_share_from_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p066315316409"><a name="p066315316409"></a><a name="p066315316409"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p1566325312408"><a name="p1566325312408"></a><a name="p1566325312408"></a>Specifies whether creation of shared file systems from snapshot is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.24 and later versions.</p>
    </td>
    </tr>
    <tr id="row12663125334015"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p1866345364011"><a name="p1866345364011"></a><a name="p1866345364011"></a>mount_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p966355374010"><a name="p966355374010"></a><a name="p966355374010"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p266435320407"><a name="p266435320407"></a><a name="p266435320407"></a>Specifies whether snapshot mount is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.32 and later versions.</p>
    </td>
    </tr>
    <tr id="row4664165311405"><td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.1.4.1.1 "><p id="p15664105324019"><a name="p15664105324019"></a><a name="p15664105324019"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p866416534403"><a name="p866416534403"></a><a name="p866416534403"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p9664653164011"><a name="p9664653164011"></a><a name="p9664653164011"></a>Specifies the user ID. This field is supported by API v2.16 and later versions.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "share": {
        "status": "available",
        "share_type_name": "sla",
        "description": "My custom share London",
        "links": [
          {
            "href": "https://192.168.196.47:8796/v2/07412155bf474db9a2f697fd978593d7/shares/f26d867f-9876-433d-8db2-25d210f29309",
            "rel": "self"
          },
          {
            "href": "https://192.168.196.47:8796/07412155bf474db9a2f697fd978593d7/shares/f26d867f-9876-433d-8db2-25d210f29309",
            "rel": "bookmark"
          }
        ],
        "availability_zone": "az1.dc1",
        "share_network_id": null,
        "share_server_id": null,
        "share_group_id": null,
        "host": "DJ38@a4588256-3880-4136-b3c9-4c3aade8a84b#a4588256-3880-4136-b3c9-4c3aade8a84b",
        "revert_to_snapshot_support": null,
        "access_rules_status": "active",
        "snapshot_id": null,
        "create_share_from_snapshot_support": null,
        "is_public": false,
        "task_state": null,
        "snapshot_support": true,
        "id": "f26d867f-9876-433d-8db2-25d210f29309",
        "size": 1,
        "source_share_group_snapshot_member_id": null,
        "user_id": "daa3f8f8d7254465841da769298a76f6",
        "name": "luzhongguo_1",
        "share_type": "8ae4e74e-83f4-4980-8ab8-e637f9294e0b",
        "has_replicas": false,
        "replication_type": null,
        "created_at": "2018-12-25T08:45:22.525899",
        "share_proto": "NFS",
        "volume_type": "sla",
        "mount_snapshot_support": null,
        "project_id": "07412155bf474db9a2f697fd978593d7",
        "metadata": {
          "share_key": "test",
          "share_used": "1",
        }
      }
    }
    ```


## Status Codes<a name="sd0bab72141f0458d815c2ca68d706d8d"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0064390794_table55361044"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390794_row7322556"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="en-us_topic_0064390794_p56256135"><a name="en-us_topic_0064390794_p56256135"></a><a name="en-us_topic_0064390794_p56256135"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="en-us_topic_0064390794_p60453091"><a name="en-us_topic_0064390794_p60453091"></a><a name="en-us_topic_0064390794_p60453091"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390794_row64862199"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p19346796"><a name="en-us_topic_0064390794_p19346796"></a><a name="en-us_topic_0064390794_p19346796"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p23586666"><a name="en-us_topic_0064390794_p23586666"></a><a name="en-us_topic_0064390794_p23586666"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row10953403"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p14810456"><a name="en-us_topic_0064390794_p14810456"></a><a name="en-us_topic_0064390794_p14810456"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p58796306"><a name="en-us_topic_0064390794_p58796306"></a><a name="en-us_topic_0064390794_p58796306"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row59404709"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p47052116"><a name="en-us_topic_0064390794_p47052116"></a><a name="en-us_topic_0064390794_p47052116"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p53125076"><a name="en-us_topic_0064390794_p53125076"></a><a name="en-us_topic_0064390794_p53125076"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row8363642"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p6366390"><a name="en-us_topic_0064390794_p6366390"></a><a name="en-us_topic_0064390794_p6366390"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p45915542"><a name="en-us_topic_0064390794_p45915542"></a><a name="en-us_topic_0064390794_p45915542"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row10586695"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p52215961"><a name="en-us_topic_0064390794_p52215961"></a><a name="en-us_topic_0064390794_p52215961"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p1634435"><a name="en-us_topic_0064390794_p1634435"></a><a name="en-us_topic_0064390794_p1634435"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row14709921"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p50652963"><a name="en-us_topic_0064390794_p50652963"></a><a name="en-us_topic_0064390794_p50652963"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p9249362"><a name="en-us_topic_0064390794_p9249362"></a><a name="en-us_topic_0064390794_p9249362"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row16135397"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p31898818"><a name="en-us_topic_0064390794_p31898818"></a><a name="en-us_topic_0064390794_p31898818"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p33667455"><a name="en-us_topic_0064390794_p33667455"></a><a name="en-us_topic_0064390794_p33667455"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row34571641"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p48839530"><a name="en-us_topic_0064390794_p48839530"></a><a name="en-us_topic_0064390794_p48839530"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p63687823"><a name="en-us_topic_0064390794_p63687823"></a><a name="en-us_topic_0064390794_p63687823"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row36319496"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p56198103"><a name="en-us_topic_0064390794_p56198103"></a><a name="en-us_topic_0064390794_p56198103"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p55752527"><a name="en-us_topic_0064390794_p55752527"></a><a name="en-us_topic_0064390794_p55752527"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row32010697"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p42729680"><a name="en-us_topic_0064390794_p42729680"></a><a name="en-us_topic_0064390794_p42729680"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p38552084"><a name="en-us_topic_0064390794_p38552084"></a><a name="en-us_topic_0064390794_p38552084"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row11424440"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p52964449"><a name="en-us_topic_0064390794_p52964449"></a><a name="en-us_topic_0064390794_p52964449"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p62262011"><a name="en-us_topic_0064390794_p62262011"></a><a name="en-us_topic_0064390794_p62262011"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row23487194"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p23414560"><a name="en-us_topic_0064390794_p23414560"></a><a name="en-us_topic_0064390794_p23414560"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p17531178"><a name="en-us_topic_0064390794_p17531178"></a><a name="en-us_topic_0064390794_p17531178"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row23562876"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p29544808"><a name="en-us_topic_0064390794_p29544808"></a><a name="en-us_topic_0064390794_p29544808"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p44319244"><a name="en-us_topic_0064390794_p44319244"></a><a name="en-us_topic_0064390794_p44319244"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row63328883"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390794_p29365919"><a name="en-us_topic_0064390794_p29365919"></a><a name="en-us_topic_0064390794_p29365919"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390794_p29829272"><a name="en-us_topic_0064390794_p29829272"></a><a name="en-us_topic_0064390794_p29829272"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


