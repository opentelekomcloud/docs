# Creating a Resource Backup<a name="EN-US_TOPIC_0059304219"></a>

## Function<a name="section21655625"></a>

This API is used to select and directly back up resources.

## URI<a name="section60682897"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/providers/\{provider\_id\}/resources/\{resource\_id\}/action

-   Parameter description

    **Table  1**  Parameter description

    <a name="table3478379"></a>
    <table><thead align="left"><tr id="row24348515"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p26072662"><a name="p26072662"></a><a name="p26072662"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p31510915"><a name="p31510915"></a><a name="p31510915"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p2247312"><a name="p2247312"></a><a name="p2247312"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p47814565"><a name="p47814565"></a><a name="p47814565"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47774571"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p44535049"><a name="p44535049"></a><a name="p44535049"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p50569256"><a name="p50569256"></a><a name="p50569256"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p2469104"><a name="p2469104"></a><a name="p2469104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row55146569"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p37687133"><a name="p37687133"></a><a name="p37687133"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p32758933"><a name="p32758933"></a><a name="p32758933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p36227930"><a name="p36227930"></a><a name="p36227930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p48781203"><a name="p48781203"></a><a name="p48781203"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b393514818119"><a name="b393514818119"></a><a name="b393514818119"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row36377647"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p60908274"><a name="p60908274"></a><a name="p60908274"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p34623133"><a name="p34623133"></a><a name="p34623133"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p53010393"><a name="p53010393"></a><a name="p53010393"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65983437"><a name="p65983437"></a><a name="p65983437"></a>ID of a backup server. For details about how to obtain the server ID, see the <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020805967.html" target="_blank" rel="noopener noreferrer">Elastic Cloud Server API Reference</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >Backup provider IDs mentioned in this document are all  **fc4d5750-22e7-4798-8a46-f48f62c4c1da**.  


## Request<a name="section9275167"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table65163008"></a>
    <table><thead align="left"><tr id="row24708790"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p55254977"><a name="p55254977"></a><a name="p55254977"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p46468128"><a name="p46468128"></a><a name="p46468128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p5822012"><a name="p5822012"></a><a name="p5822012"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p1820924"><a name="p1820924"></a><a name="p1820924"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13277128"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p1705609"><a name="p1705609"></a><a name="p1705609"></a>protect</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p3936679"><a name="p3936679"></a><a name="p3936679"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p50435593"><a name="p50435593"></a><a name="p50435593"></a>protect_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p58751256"><a name="p58751256"></a><a name="p58751256"></a>Backup parameters</p>
    <p id="p12918262208"><a name="p12918262208"></a><a name="p12918262208"></a>For details, see <a href="#table61231291">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **protect\_param**

    **Table  3**  Parameter description of field  **protect\_param**

    <a name="table61231291"></a>
    <table><thead align="left"><tr id="row59177776"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p28670558"><a name="p28670558"></a><a name="p28670558"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p40613901"><a name="p40613901"></a><a name="p40613901"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p1391717"><a name="p1391717"></a><a name="p1391717"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p45620237"><a name="p45620237"></a><a name="p45620237"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4251693"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p8842862"><a name="p8842862"></a><a name="p8842862"></a>backup_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p45183223"><a name="p45183223"></a><a name="p45183223"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p35962481"><a name="p35962481"></a><a name="p35962481"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p27279876"><a name="p27279876"></a><a name="p27279876"></a>Backup name. The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row44192294"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p22806032"><a name="p22806032"></a><a name="p22806032"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p35349286"><a name="p35349286"></a><a name="p35349286"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p44719954"><a name="p44719954"></a><a name="p44719954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65546489"><a name="p65546489"></a><a name="p65546489"></a>Backup description. The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row1128062331110"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p213719391665"><a name="p213719391665"></a><a name="p213719391665"></a>incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p913717392612"><a name="p913717392612"></a><a name="p913717392612"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1913714399617"><a name="p1913714399617"></a><a name="p1913714399617"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p12137039566"><a name="p12137039566"></a><a name="p12137039566"></a>Backup type. Value <strong id="b84235270619123"><a name="b84235270619123"></a><a name="b84235270619123"></a>True</strong> indicates incremental backup and value <strong id="b84235270619127"><a name="b84235270619127"></a><a name="b84235270619127"></a>False</strong> indicates full backup. For the initial backup, full backup is always adopted, in spite of which value is set.</p>
    </td>
    </tr>
    <tr id="row138818832216"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p20918121932210"><a name="p20918121932210"></a><a name="p20918121932210"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p109214199225"><a name="p109214199225"></a><a name="p109214199225"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p16925101912220"><a name="p16925101912220"></a><a name="p16925101912220"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p593081942216"><a name="p593081942216"></a><a name="p593081942216"></a>Entity object type of the backup object</p>
    <p id="p4930919112214"><a name="p4930919112214"></a><a name="p4930919112214"></a>The current value is <strong id="b842352706174637"><a name="b842352706174637"></a><a name="b842352706174637"></a>OS::Nova::Server</strong> indicating that the backup object is an ECS. If this parameter is not passed, the backup object type defaults to <strong id="b715618842191047"><a name="b715618842191047"></a><a name="b715618842191047"></a>OS::Nova::Server</strong>.</p>
    </td>
    </tr>
    <tr id="row156291503185"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p166319031813"><a name="p166319031813"></a><a name="p166319031813"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p863111081818"><a name="p863111081818"></a><a name="p863111081818"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p106311010188"><a name="p106311010188"></a><a name="p106311010188"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p9244511113310"><a name="p9244511113310"></a><a name="p9244511113310"></a>Tag list</p>
    <p id="p52026988"><a name="p52026988"></a><a name="p52026988"></a>This list cannot be an empty list.</p>
    <p id="p183916535015"><a name="p183916535015"></a><a name="p183916535015"></a>The list can contain up to 10 keys.</p>
    <p id="p1338589319"><a name="p1338589319"></a><a name="p1338589319"></a>Keys in this list must be unique.</p>
    </td>
    </tr>
    <tr id="row4259132585510"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p8259325135510"><a name="p8259325135510"></a><a name="p8259325135510"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p1425913251559"><a name="p1425913251559"></a><a name="p1425913251559"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p42591425175510"><a name="p42591425175510"></a><a name="p42591425175510"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p17259112515518"><a name="p17259112515518"></a><a name="p17259112515518"></a>Additional information about the backup object</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  4**  Parameter description of field  **resource\_tag**

    <a name="table896249101917"></a>
    <table><thead align="left"><tr id="row9162134911197"><th class="cellrowborder" valign="top" width="19.400000000000002%" id="mcps1.2.5.1.1"><p id="p7162249101912"><a name="p7162249101912"></a><a name="p7162249101912"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.5.1.2"><p id="p5162849151912"><a name="p5162849151912"></a><a name="p5162849151912"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.5.1.3"><p id="p1916215495193"><a name="p1916215495193"></a><a name="p1916215495193"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.919999999999995%" id="mcps1.2.5.1.4"><p id="p151621949111912"><a name="p151621949111912"></a><a name="p151621949111912"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11162154981914"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.5.1.1 "><p id="p91621649171913"><a name="p91621649171913"></a><a name="p91621649171913"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.2 "><p id="p141641249191910"><a name="p141641249191910"></a><a name="p141641249191910"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.3 "><p id="p1516484971919"><a name="p1516484971919"></a><a name="p1516484971919"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.919999999999995%" headers="mcps1.2.5.1.4 "><p id="p798643483310"><a name="p798643483310"></a><a name="p798643483310"></a>Tag key</p>
    <p id="p036816391334"><a name="p036816391334"></a><a name="p036816391334"></a>It consists of up to 36 characters.</p>
    <p id="p1815945343312"><a name="p1815945343312"></a><a name="p1815945343312"></a>It cannot be an empty string.</p>
    <p id="p139819543334"><a name="p139819543334"></a><a name="p139819543334"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row19164144901912"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.5.1.1 "><p id="p8164134971913"><a name="p8164134971913"></a><a name="p8164134971913"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.2 "><p id="p1216494911199"><a name="p1216494911199"></a><a name="p1216494911199"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.5.1.3 "><p id="p2164549151920"><a name="p2164549151920"></a><a name="p2164549151920"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.919999999999995%" headers="mcps1.2.5.1.4 "><p id="p11608421163420"><a name="p11608421163420"></a><a name="p11608421163420"></a>Tag value</p>
    <p id="p489413816351"><a name="p489413816351"></a><a name="p489413816351"></a>It consists of up to 43 characters.</p>
    <p id="p14194717123517"><a name="p14194717123517"></a><a name="p14194717123517"></a>It can be an empty string.</p>
    <p id="p1146913338362"><a name="p1146913338362"></a><a name="p1146913338362"></a>Spaces before and after a tag value will be deprecated.</p>
    <p id="p86239316407"><a name="p86239316407"></a><a name="p86239316407"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST 
    https://{endpoint}/v1/b942cc8342734d15bcb246babb1953cf/providers/fc4d5750-22e7-4798-8a46-f48f62c4c1da/resources/9506416d-db6c-406e-8bca-c0f43793d914/action
    {
        "protect" : {
        "backup_name" : "backup",
        "description" : "backup des",
        "extra_info" : {
        }
        
      }
    }
    ```


## Response<a name="section16367643"></a>

-   Parameter description

    **Table  5**  Parameter description

    <a name="table3249118"></a>
    <table><thead align="left"><tr id="row31941010"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p37085012"><a name="p37085012"></a><a name="p37085012"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p45133897"><a name="p45133897"></a><a name="p45133897"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p31967053"><a name="p31967053"></a><a name="p31967053"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39194464"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20635053"><a name="p20635053"></a><a name="p20635053"></a>checkpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28006415"><a name="p28006415"></a><a name="p28006415"></a>protect_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p53927157"><a name="p53927157"></a><a name="p53927157"></a>Backup response</p>
    <p id="p17581748172717"><a name="p17581748172717"></a><a name="p17581748172717"></a>For details, see <a href="#table6023603">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **protect\_resp**

    **Table  6**  Parameter description of field  **protect\_resp**

    <a name="table6023603"></a>
    <table><thead align="left"><tr id="row3404451"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p7325143"><a name="p7325143"></a><a name="p7325143"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p10319892"><a name="p10319892"></a><a name="p10319892"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p30604909"><a name="p30604909"></a><a name="p30604909"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63078563"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9089949"><a name="p9089949"></a><a name="p9089949"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p46486015"><a name="p46486015"></a><a name="p46486015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p7270838"><a name="p7270838"></a><a name="p7270838"></a>Backup status</p>
    <p id="p199923219255"><a name="p199923219255"></a><a name="p199923219255"></a>Enum:[ waiting_protect, protecting, available, waiting_restore, restoring, error, waiting_delete, deleting,deleted]</p>
    </td>
    </tr>
    <tr id="row65437548"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p65950058"><a name="p65950058"></a><a name="p65950058"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p47485470"><a name="p47485470"></a><a name="p47485470"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p21117861"><a name="p21117861"></a><a name="p21117861"></a>Creation time, for example, <strong id="b3968854145819"><a name="b3968854145819"></a><a name="b3968854145819"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row55843024"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26991099"><a name="p26991099"></a><a name="p26991099"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55418550"><a name="p55418550"></a><a name="p55418550"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59717526"><a name="p59717526"></a><a name="p59717526"></a>Backup record ID</p>
    </td>
    </tr>
    <tr id="row586823"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p47532697"><a name="p47532697"></a><a name="p47532697"></a>resource_graph</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7136174"><a name="p7136174"></a><a name="p7136174"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p41159234"><a name="p41159234"></a><a name="p41159234"></a>Resource diagram, which displays the inclusion relationship between backups and sub-backups</p>
    </td>
    </tr>
    <tr id="row34888786"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p7419413"><a name="p7419413"></a><a name="p7419413"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24846201"><a name="p24846201"></a><a name="p24846201"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p66385258"><a name="p66385258"></a><a name="p66385258"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row60596410"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9362184"><a name="p9362184"></a><a name="p9362184"></a>protection_plan</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p20685135"><a name="p20685135"></a><a name="p20685135"></a>plan_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p64883223"><a name="p64883223"></a><a name="p64883223"></a>Backup plan information</p>
    <p id="p4797713102910"><a name="p4797713102910"></a><a name="p4797713102910"></a>For details, see <a href="#table21049687">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row657816335619"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p115662037564"><a name="p115662037564"></a><a name="p115662037564"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p115691236563"><a name="p115691236563"></a><a name="p115691236563"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p125732310569"><a name="p125732310569"></a><a name="p125732310569"></a>Additional information</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **plan\_resp**

    **Table  7**  Parameter description of field  **plan\_resp**

    <a name="table21049687"></a>
    <table><thead align="left"><tr id="row64306394"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p41435424"><a name="p41435424"></a><a name="p41435424"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p66918496"><a name="p66918496"></a><a name="p66918496"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p51689132"><a name="p51689132"></a><a name="p51689132"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26070131"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p31305887"><a name="p31305887"></a><a name="p31305887"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p44806725"><a name="p44806725"></a><a name="p44806725"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5466127"><a name="p5466127"></a><a name="p5466127"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row49195146"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25383881"><a name="p25383881"></a><a name="p25383881"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p46556898"><a name="p46556898"></a><a name="p46556898"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13012363"><a name="p13012363"></a><a name="p13012363"></a>Backup policy name</p>
    </td>
    </tr>
    <tr id="row50002403"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23662815"><a name="p23662815"></a><a name="p23662815"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p28932126"><a name="p28932126"></a><a name="p28932126"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p61800880"><a name="p61800880"></a><a name="p61800880"></a>Backup object list</p>
    <p id="p8794115120123"><a name="p8794115120123"></a><a name="p8794115120123"></a>For details, see <a href="#table4765237103212">Table 8</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource**

    **Table  8**  Parameter description of field  **resource**

    <a name="table4765237103212"></a>
    <table><thead align="left"><tr id="row3761173710329"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p7761183753211"><a name="p7761183753211"></a><a name="p7761183753211"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p197611937173220"><a name="p197611937173220"></a><a name="p197611937173220"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p197611337133215"><a name="p197611337133215"></a><a name="p197611337133215"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row176243783215"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p87621337183218"><a name="p87621337183218"></a><a name="p87621337183218"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p177621372321"><a name="p177621372321"></a><a name="p177621372321"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p77622037173219"><a name="p77622037173219"></a><a name="p77622037173219"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row1976319377329"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p137621637143211"><a name="p137621637143211"></a><a name="p137621637143211"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1276353714328"><a name="p1276353714328"></a><a name="p1276353714328"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p07632378329"><a name="p07632378329"></a><a name="p07632378329"></a>Entity object type of the backup object. The value is fixed at <strong id="b1011106231165357"><a name="b1011106231165357"></a><a name="b1011106231165357"></a>OS::Nova::Server</strong>, indicating that the object type is ECSs.</p>
    </td>
    </tr>
    <tr id="row1576412371327"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1476483713216"><a name="p1476483713216"></a><a name="p1476483713216"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p127641337173211"><a name="p127641337173211"></a><a name="p127641337173211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p876473713326"><a name="p876473713326"></a><a name="p876473713326"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row77651537153211"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p7764173719321"><a name="p7764173719321"></a><a name="p7764173719321"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p276433733213"><a name="p276433733213"></a><a name="p276433733213"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p2076413773217"><a name="p2076413773217"></a><a name="p2076413773217"></a>Additional information about the backup object</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "checkpoint" : {
        "status" : "protecting",
        "created_at" : "2017-04-18T01:21:52.701973",
        "id" : "4468f4b8-7c78-4222-a2ca-346b5d557dd2",
        "resource_graph" : null,
        "project_id" : "b942cc8342734d15bcb246babb1953cf",
        "extra_info" : null,
        "protection_plan" : {
          "id" : "fake_04f8ea0f-2000-4389-a5ce-93a3e20d0faf",
          "resources" : [ {
            "type" : "OS::Nova::Server",
            "id" : "9506416d-db6c-406e-8bca-c0f43793d914",
            "name" : "resource_9506416d-db6c-406e-8bca-c0f43793d914",
            "extra_info" : {
        }
          } ],
          "name" : "server protect plan for 9506416d-db6c-406e-8bca-c0f43793d914"
        }
      }
    }
    ```


## Status Codes<a name="section13091062"></a>

-   Normal

    <a name="table45474671"></a>
    <table><thead align="left"><tr id="row6907822"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p22662724"><a name="p22662724"></a><a name="p22662724"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p23741362"><a name="p23741362"></a><a name="p23741362"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44002209"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p7409209"><a name="p7409209"></a><a name="p7409209"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p63275041"><a name="p63275041"></a><a name="p63275041"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table25004673"></a>
    <table><thead align="left"><tr id="row38855211"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p60264372"><a name="p60264372"></a><a name="p60264372"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p49575962"><a name="p49575962"></a><a name="p49575962"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56229956"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p58332570"><a name="p58332570"></a><a name="p58332570"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p27317766"><a name="p27317766"></a><a name="p27317766"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row44533302"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p50427739"><a name="p50427739"></a><a name="p50427739"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58115081"><a name="p58115081"></a><a name="p58115081"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row53273682"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p20200991"><a name="p20200991"></a><a name="p20200991"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p25667593"><a name="p25667593"></a><a name="p25667593"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row29681748"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p55411379"><a name="p55411379"></a><a name="p55411379"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p59136739"><a name="p59136739"></a><a name="p59136739"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row62468609"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p26792557"><a name="p26792557"></a><a name="p26792557"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p22713469"><a name="p22713469"></a><a name="p22713469"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row3094630"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p49338472"><a name="p49338472"></a><a name="p49338472"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p36993282"><a name="p36993282"></a><a name="p36993282"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section10566123417416"></a>

For details, see  [Error Codes](error-codes.md).

