# Querying and Accessing a VPC Endpoint<a name="vpcep_03_0202"></a>

## Scenarios<a name="section181381057185612"></a>

After a VPC endpoint is created, you can query its details and access it.

## Query a VPC Endpoint<a name="section19334124820566"></a>

Perform the following operations to query details of a VPC endpoint, including the ID, associated VPC endpoint service name, VPC, and status.

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.

1.  Click  **Service List**  and choose  **VPC Endpoint**  under  **Network**.

    On the displayed page, locate the target VPC endpoint by entering a filter in the search box in the upper right corner:

    -   Search by VPC endpoint service name or VPC endpoint ID as follows:
        1.  Select  **VPC endpoint service name**  or  **ID**  in the filter box.
        2.  Enter a keyword in the search box.
        3.  Click  ![](figures/icon-search.png)  to start the search.

            VPC endpoints containing the keyword are displayed in the list.

    -   Search for a VPC endpoint by the preset tag:
        1.  Click  ![](figures/icon-tag-search.png)  in  **Search by Tag**  to expand the tag search area.

            **Figure  1**  Tag search area<a name="fig17552221133112"></a>  
            ![](figures/tag-search-area-10.png "tag-search-area-10")

        2.  Enter a tag and a value.

            Enter a key or value or select a key or value from the drop-down list.

            You can add a maximum of 10 tags to search for VPC endpoints.

        3.  Click  **Search**.

            VPC endpoints containing the specified tag are displayed in the list.

            If you set multiple pairs of tags, VPC endpoints containing all the specified tags are displayed.


2.  In the VPC endpoint list, locate the target endpoint and click its ID.

    After an interface VPC endpoint is created, a private IP address and a private domain name are generated if you select  **Create a Private Domain Name**  during creation.

    **Figure  2**  Summary of the VPC endpoint<a name="fig735142618538"></a>  
    ![](figures/summary-of-the-vpc-endpoint-11.png "summary-of-the-vpc-endpoint-11")

    Details of a VPC endpoint include summary and tags.

    **Table  1**  Parameter description

    <a name="table11373229195910"></a>
    <table><thead align="left"><tr id="row123731829185916"><th class="cellrowborder" valign="top" width="21.09%" id="mcps1.2.4.1.1"><p id="p884314912598"><a name="p884314912598"></a><a name="p884314912598"></a><strong id="b3366113318010"><a name="b3366113318010"></a><a name="b3366113318010"></a>Tab</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.849999999999998%" id="mcps1.2.4.1.2"><p id="p7373142911592"><a name="p7373142911592"></a><a name="p7373142911592"></a><strong id="b1589733417"><a name="b1589733417"></a><a name="b1589733417"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.059999999999995%" id="mcps1.2.4.1.3"><p id="p1037310293590"><a name="p1037310293590"></a><a name="p1037310293590"></a><strong id="b778155451616"><a name="b778155451616"></a><a name="b778155451616"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6601518175912"><td class="cellrowborder" rowspan="8" valign="top" width="21.09%" headers="mcps1.2.4.1.1 "><p id="p1039151214278"><a name="p1039151214278"></a><a name="p1039151214278"></a>Summary</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p136021118205912"><a name="p136021118205912"></a><a name="p136021118205912"></a>ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.2.4.1.3 "><p id="p66023186590"><a name="p66023186590"></a><a name="p66023186590"></a>Specifies the ID of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row6602718105914"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p360218189596"><a name="p360218189596"></a><a name="p360218189596"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6602141819595"><a name="p6602141819595"></a><a name="p6602141819595"></a>Specifies the region where the VPC endpoint is deployed.</p>
    </td>
    </tr>
    <tr id="row1660320181596"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p760319185599"><a name="p760319185599"></a><a name="p760319185599"></a>VPC Endpoint Service Name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p156038185594"><a name="p156038185594"></a><a name="p156038185594"></a>Specifies the name of the VPC endpoint service that is associated with the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1260311185593"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1160321818599"><a name="p1160321818599"></a><a name="p1160321818599"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6603118195917"><a name="p6603118195917"></a><a name="p6603118195917"></a>Specifies the IP address for accessing the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1603161817598"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p17603618185915"><a name="p17603618185915"></a><a name="p17603618185915"></a>Private Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p6603118115914"><a name="p6603118115914"></a><a name="p6603118115914"></a>Specifies the private domain name for accessing the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row9659329903"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p36595295020"><a name="p36595295020"></a><a name="p36595295020"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p365918293014"><a name="p365918293014"></a><a name="p365918293014"></a>Specifies the status of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1465962910011"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1965912291309"><a name="p1965912291309"></a><a name="p1965912291309"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1165915291105"><a name="p1165915291105"></a><a name="p1165915291105"></a>Specifies the type of the VPC endpoint service that is associated with the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1865942911010"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p12793443359"><a name="p12793443359"></a><a name="p12793443359"></a>Created</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p206596291010"><a name="p206596291010"></a><a name="p206596291010"></a>Specifies the creation time of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1262811653513"><td class="cellrowborder" rowspan="3" valign="top" width="21.09%" headers="mcps1.2.4.1.1 "><p id="p20629176113515"><a name="p20629176113515"></a><a name="p20629176113515"></a>Tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p462918633511"><a name="p462918633511"></a><a name="p462918633511"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.059999999999995%" headers="mcps1.2.4.1.3 "><p id="p1963135561417"><a name="p1963135561417"></a><a name="p1963135561417"></a>Specifies the tag key of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1468217176366"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p468221711366"><a name="p468221711366"></a><a name="p468221711366"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1763755161412"><a name="p1763755161412"></a><a name="p1763755161412"></a>Specifies the tag value of the VPC endpoint.</p>
    </td>
    </tr>
    <tr id="row1791516293369"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p12915142913365"><a name="p12915142913365"></a><a name="p12915142913365"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p76320551147"><a name="p76320551147"></a><a name="p76320551147"></a>Specifies the operation on the VPC endpoint tag, for example, you can select <strong id="b128731044142611"><a name="b128731044142611"></a><a name="b128731044142611"></a>Edit</strong> or <strong id="b1287404412616"><a name="b1287404412616"></a><a name="b1287404412616"></a>Delete</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Access a VPC Endpoint \(using a private IP address\)<a name="section125426655618"></a>

Perform the following operations to access a VPC endpoint using its private IP address:

1.  In the VPC that the VPC endpoint belongs to, log in to the backend resource, for example, an ECS.
2.  Select a command based on the backend resource type and run the command to access the VPC endpoint. The command format is as follows:

    _Command_ _Private IP address_:_Port number_

    The following is a command example:

    **curl **_Private IP address:Port number_


## Access a VPC Endpoint \(using a private domain name\)<a name="section990519525715"></a>

You can access a VPC endpoint using its private domain name if you select  **Create a Private Domain Name**  when creating the endpoint.

The system automatically creates a private zone for the generated domain name and adds A record set for the private zone to resolve the domain name into the private IP address of the VPC endpoint.

You can view the corresponding private zone and its resolution records on the DNS console. For more information, see  [Configuring a Private Zone](https://docs.otc.t-systems.com/en-us/usermanual/dns/dns_qs_0006.html).

**Viewing the record set of the private domain name**

1.  Log in to the management console.
2.  In the  **Network**  category, click  **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, choose  **Private Zones**.

    The  **Private Zones**  page is displayed.


1.  In the private zone list, click the name of the target private zone.

    The record set page is displayed.

2.  In the record set list, locate the target A record set and view its information.

    When the value in the  **Status**  column becomes  **Normal**, the resolution takes effect.

    **Figure  3**  Record set of the private domain name<a name="fig1966691952211"></a>  
    ![](figures/record-set-of-the-private-domain-name.png "record-set-of-the-private-domain-name")


**Accessing a VPC endpoint using a private domain name**

1.  In the VPC that the VPC endpoint belongs to, log in to the backend resource, for example, an ECS.
2.  Select a command based on the backend resource type and run the command to access the VPC endpoint. The command format is as follows:

    _Command_ _Private domain name_:_Port number_

    The following is a command example:

    **curl **_Private domain name:Port number_


