# Viewing a VPC Endpoint Service<a name="vpcep_03_0102"></a>

## Scenarios<a name="section85216505244"></a>

This section describes how to view a VPC endpoint service, including the name, ID, backend resource type, backend resource name, VPC, status, connection approval, service type, and creation time.

## Procedure<a name="section15309424142016"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.

1.  Click  **Service List**  and choose  **VPC Endpoint**  under  **Network**.
2.  In the navigation pane on the left, choose  **VPC Endpoint**  \>  **VPC Endpoint Services**.

    Locate the target VPC endpoint service by entering a filter in the search box in the upper right corner:

    -   Search by the name or ID of the VPC endpoint service as follows:
        1.  Select  **Name**  or  **ID**  in the filter box.
        2.  Enter a keyword in the search box.
        3.  Click  ![](figures/icon-search.png)  to start the search.

            VPC endpoint services containing the keyword are displayed in the list.

    -   Search for a VPC endpoint service by the preset tag:
        1.  Click  ![](figures/icon-tag-search.png)  in  **Search by Tag**  to expand the tag search area.

            **Figure  1**  Tag search area<a name="fig17552221133112"></a>  
            ![](figures/tag-search-area.png "tag-search-area")

        2.  Enter a tag and a value.

            Enter a key or value or select a key or value from the drop-down list.

            You can add a maximum of 10 tags to search for VPC endpoint services.

        3.  Click  **Search**.

            VPC endpoint services containing the specified tag are displayed in the list.

            If you set multiple pairs of tags, VPC endpoint services containing all the specified tags are displayed.


3.  In the VPC endpoint service list, locate the target VPC endpoint service and click its name to view details.

    **Figure  2**  Summary of the VPC endpoint service<a name="fig148852011125319"></a>  
    ![](figures/summary-of-the-vpc-endpoint-service-8.jpg "summary-of-the-vpc-endpoint-service-8")

    Details of a VPC endpoint service include the summary, connection management, permission management, tags, and port mappings. For details, see  [Table 1](#table11373229195910).

    **Table  1**  Parameter description

    <a name="table11373229195910"></a>
    <table><thead align="left"><tr id="row123731829185916"><th class="cellrowborder" valign="top" width="21.09%" id="mcps1.2.4.1.1"><p id="p884314912598"><a name="p884314912598"></a><a name="p884314912598"></a><strong id="b3366113318010"><a name="b3366113318010"></a><a name="b3366113318010"></a>Tab</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.849999999999998%" id="mcps1.2.4.1.2"><p id="p7373142911592"><a name="p7373142911592"></a><a name="p7373142911592"></a><strong id="b1589733417"><a name="b1589733417"></a><a name="b1589733417"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.059999999999995%" id="mcps1.2.4.1.3"><p id="p1037310293590"><a name="p1037310293590"></a><a name="p1037310293590"></a><strong id="b158167361039"><a name="b158167361039"></a><a name="b158167361039"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6601518175912"><td class="cellrowborder" rowspan="9" valign="top" width="21.09%" headers="mcps1.2.4.1.1 "><p id="p1039151214278"><a name="p1039151214278"></a><a name="p1039151214278"></a>Summary</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p136021118205912"><a name="p136021118205912"></a><a name="p136021118205912"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.2.4.1.3 "><p id="p66023186590"><a name="p66023186590"></a><a name="p66023186590"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row6602718105914"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p360218189596"><a name="p360218189596"></a><a name="p360218189596"></a>ID</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6602141819595"><a name="p6602141819595"></a><a name="p6602141819595"></a>Specifies the ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row1660320181596"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p760319185599"><a name="p760319185599"></a><a name="p760319185599"></a>Backend Resource Type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p156038185594"><a name="p156038185594"></a><a name="p156038185594"></a>Specifies the type of the backend resource that provides services to be accessed.</p>
    </td>
    </tr>
    <tr id="row1260311185593"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1160321818599"><a name="p1160321818599"></a><a name="p1160321818599"></a>Backend Resource Name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6603118195917"><a name="p6603118195917"></a><a name="p6603118195917"></a>Specifies the name of the backend resource that provides services to be accessed.</p>
    </td>
    </tr>
    <tr id="row1603161817598"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p17603618185915"><a name="p17603618185915"></a><a name="p17603618185915"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6603118115914"><a name="p6603118115914"></a><a name="p6603118115914"></a>Specifies the region where the VPC endpoint service is deployed.</p>
    </td>
    </tr>
    <tr id="row9659329903"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p36595295020"><a name="p36595295020"></a><a name="p36595295020"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p365918293014"><a name="p365918293014"></a><a name="p365918293014"></a>Specifies the status of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row1465962910011"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1965912291309"><a name="p1965912291309"></a><a name="p1965912291309"></a>Connection Approval</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1165915291105"><a name="p1165915291105"></a><a name="p1165915291105"></a>Specifies whether connection approval is required.</p>
    </td>
    </tr>
    <tr id="row1865942911010"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p12793443359"><a name="p12793443359"></a><a name="p12793443359"></a>Service Type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p206596291010"><a name="p206596291010"></a><a name="p206596291010"></a>Specifies the type of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row1665992916016"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p577414111355"><a name="p577414111355"></a><a name="p577414111355"></a>Created</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p186591299014"><a name="p186591299014"></a><a name="p186591299014"></a>Specifies the creation time of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row1373142925914"><td class="cellrowborder" rowspan="6" valign="top" width="21.09%" headers="mcps1.2.4.1.1 "><p id="p2843209125918"><a name="p2843209125918"></a><a name="p2843209125918"></a>Connection Management</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p437313292597"><a name="p437313292597"></a><a name="p437313292597"></a>VPC Endpoint ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.2.4.1.3 "><p id="p1237342911592"><a name="p1237342911592"></a><a name="p1237342911592"></a>Specifies the ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1931215511014"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p73131155602"><a name="p73131155602"></a><a name="p73131155602"></a>Packet ID</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p13313115516018"><a name="p13313115516018"></a><a name="p13313115516018"></a>Specifies the identifier of the VPC endpoint ID.</p>
    </td>
    </tr>
    <tr id="row1788517341318"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1084733910114"><a name="p1084733910114"></a><a name="p1084733910114"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1290225213217"><a name="p1290225213217"></a><a name="p1290225213217"></a>Specifies the status of the VPC endpoint.</p>
    <p id="p188861834919"><a name="p188861834919"></a><a name="p188861834919"></a>For details about statuses of a VPC endpoint, see <a href="what-are-statuses-of-vpc-endpoint-services-and-vpc-endpoints.md">What Are Statuses of VPC Endpoint Services and VPC Endpoints?</a></p>
    </td>
    </tr>
    <tr id="row194731557216"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1547314559217"><a name="p1547314559217"></a><a name="p1547314559217"></a>Owner</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1747319557218"><a name="p1747319557218"></a><a name="p1747319557218"></a>Specifies the owner who creates the VPC endpoint. The value can be the domain ID of the owner.</p>
    </td>
    </tr>
    <tr id="row148914485317"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p8890481319"><a name="p8890481319"></a><a name="p8890481319"></a>Created</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p11902048934"><a name="p11902048934"></a><a name="p11902048934"></a>Specifies the creation time of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row20920431747"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p109204312410"><a name="p109204312410"></a><a name="p109204312410"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p69207319419"><a name="p69207319419"></a><a name="p69207319419"></a>Specifies whether to allow a VPC endpoint to connect to a VPC endpoint service. The value can be <strong id="b101062711114"><a name="b101062711114"></a><a name="b101062711114"></a>Accept</strong> or <strong id="b297532916119"><a name="b297532916119"></a><a name="b297532916119"></a>Reject</strong>.</p>
    </td>
    </tr>
    <tr id="row491115378110"><td class="cellrowborder" rowspan="2" valign="top" width="21.09%" headers="mcps1.2.4.1.1 "><p id="p0325114917311"><a name="p0325114917311"></a><a name="p0325114917311"></a>Permission Management</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p2911037516"><a name="p2911037516"></a><a name="p2911037516"></a>Authorized Domain ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.2.4.1.3 "><p id="p6371115016133"><a name="p6371115016133"></a><a name="p6371115016133"></a>Specifies the authorized domain ID for connecting to the VPC endpoint. The value can also be *.</p>
    <p id="p391133715118"><a name="p391133715118"></a><a name="p391133715118"></a>If you add an asterisk (*) to the whitelist, it means that all users can access the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row163028403116"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p103025404114"><a name="p103025404114"></a><a name="p103025404114"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p53021640214"><a name="p53021640214"></a><a name="p53021640214"></a>Specifies the operation of deleting an authorized domain ID from the whitelist.</p>
    </td>
    </tr>
    <tr id="row109693491717"><td class="cellrowborder" rowspan="3" valign="top" width="21.09%" headers="mcps1.2.4.1.1 "><p id="p10982151318418"><a name="p10982151318418"></a><a name="p10982151318418"></a>Port Mapping</p>
    <p id="p55792025162714"><a name="p55792025162714"></a><a name="p55792025162714"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p139699494119"><a name="p139699494119"></a><a name="p139699494119"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.2.4.1.3 "><p id="p79691149615"><a name="p79691149615"></a><a name="p79691149615"></a>Specifies the protocol and ports used for communication between the VPC endpoint service and VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row5121531413"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p153772013143615"><a name="p153772013143615"></a><a name="p153772013143615"></a>Service Port</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p111310537120"><a name="p111310537120"></a><a name="p111310537120"></a>Specifies the port provided by the backend service bound to the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row176299161224"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p16294169210"><a name="p16294169210"></a><a name="p16294169210"></a>Terminal Port</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6629161611211"><a name="p6629161611211"></a><a name="p6629161611211"></a>Specifies the port provided by the VPC endpoint, allowing you to access the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row19273741417"><td class="cellrowborder" rowspan="3" valign="top" width="21.09%" headers="mcps1.2.4.1.1 "><p id="p8281976144"><a name="p8281976144"></a><a name="p8281976144"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p142807191418"><a name="p142807191418"></a><a name="p142807191418"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.2.4.1.3 "><p id="p1963135561417"><a name="p1963135561417"></a><a name="p1963135561417"></a>Specifies the tag key of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row1283716140"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1128775141"><a name="p1128775141"></a><a name="p1128775141"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1763755161412"><a name="p1763755161412"></a><a name="p1763755161412"></a>Specifies the tag value of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row15298761416"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p112916718146"><a name="p112916718146"></a><a name="p112916718146"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p76320551147"><a name="p76320551147"></a><a name="p76320551147"></a>Specifies the operation on the VPC endpoint service tag, for example, you can select <strong id="b8379104713511"><a name="b8379104713511"></a><a name="b8379104713511"></a>Edit</strong> or <strong id="b16195105020354"><a name="b16195105020354"></a><a name="b16195105020354"></a>Delete</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


