# Managing Queue Policies<a name="EN-US_TOPIC_0143117169"></a>

## Scenario<a name="section1682010274457"></a>

Configure queue policies if multiple users or services need to access the same message queue.

## Procedure<a name="section2821122734518"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png)  in the upper left corner to select a region and a project.
3.  Click  **Service List**, and choose  **Application \> Distributed Message Service**  to open the DMS console.
4.  In the navigation pane, choose  **Queue Manager**.
5.  Click the name of a queue for which you want to add a queue policy.
6.  On the queue details page, click the  **Policy Management**  tab.
7.  On the  **Policy Management**  tab page, click  **Create Queue Policy**.
8.  Specify parameters as shown in  [Table 1](#table97629762619).

    **Table  1**  Queue policy parameters

    <a name="table97629762619"></a>
    <table><thead align="left"><tr id="row27639713260"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="p376387142610"><a name="p376387142610"></a><a name="p376387142610"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="p1676318718268"><a name="p1676318718268"></a><a name="p1676318718268"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row318770182315"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p195741521233"><a name="p195741521233"></a><a name="p195741521233"></a>Queue Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p3574521237"><a name="p3574521237"></a><a name="p3574521237"></a>Name of the queue to which the new policy will be applied.</p>
    </td>
    </tr>
    <tr id="row21724731619"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p1518164741619"><a name="p1518164741619"></a><a name="p1518164741619"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><a name="ul20181955131715"></a><a name="ul20181955131715"></a><ul id="ul20181955131715"><li><strong id="b56312155416"><a name="b56312155416"></a><a name="b56312155416"></a>Allow</strong></li><li><strong id="b17206175417"><a name="b17206175417"></a><a name="b17206175417"></a>Deny</strong></li></ul>
    <p id="p18960119101919"><a name="p18960119101919"></a><a name="p18960119101919"></a>The default permission is <strong id="b144808010816"><a name="b144808010816"></a><a name="b144808010816"></a>Allow</strong>.</p>
    </td>
    </tr>
    <tr id="row16413114205019"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p1041313415508"><a name="p1041313415508"></a><a name="p1041313415508"></a>Policy Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><a name="ul138913298508"></a><a name="ul138913298508"></a><ul id="ul138913298508"><li><strong id="b20805131910411"><a name="b20805131910411"></a><a name="b20805131910411"></a>User-based</strong></li><li><strong id="b1789682044111"><a name="b1789682044111"></a><a name="b1789682044111"></a>Service-based</strong></li></ul>
    <p id="p117221916131914"><a name="p117221916131914"></a><a name="p117221916131914"></a>The default policy type is <strong id="b8605101316820"><a name="b8605101316820"></a><a name="b8605101316820"></a>User-based</strong>.</p>
    </td>
    </tr>
    <tr id="row57631271260"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p4763147182613"><a name="p4763147182613"></a><a name="p4763147182613"></a>Users</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p1976311712615"><a name="p1976311712615"></a><a name="p1976311712615"></a>This parameter is configurable if<strong id="b457016821014"><a name="b457016821014"></a><a name="b457016821014"></a> Policy Type</strong> is <strong id="b593825942188"><a name="b593825942188"></a><a name="b593825942188"></a>User-based</strong>.</p>
    <a name="ul1176357192615"></a><a name="ul1176357192615"></a><ul id="ul1176357192615"><li><strong id="b29881945134"><a name="b29881945134"></a><a name="b29881945134"></a>All users</strong></li><li><strong id="b94736711310"><a name="b94736711310"></a><a name="b94736711310"></a>Specified users</strong>: The user list can be any of the following three or any comma-separated combination of the following three: domain IDs, domain names, and Uniform Resource Names (URNs).<p id="p133481159145817"><a name="p133481159145817"></a><a name="p133481159145817"></a>URN is a unique resource ID in the format of urn:csp:service:region_id:domain_id:resourcetype:resource or urn:csp:service:region_id:domain_id:resource.</p>
    <p id="p1048833204415"><a name="p1048833204415"></a><a name="p1048833204415"></a>Fields:</p>
    <a name="ul79447401313"></a><a name="ul79447401313"></a><ul id="ul79447401313"><li><strong id="b3761971110237"><a name="b3761971110237"></a><a name="b3761971110237"></a>csp</strong>: cloud service provider</li><li><strong id="b62551385102352"><a name="b62551385102352"></a><a name="b62551385102352"></a>service</strong>: abbreviation of a service name, for example, SMN</li><li><strong id="b126405318910"><a name="b126405318910"></a><a name="b126405318910"></a>region_id</strong>: region ID, for example, <strong id="b913613326714"><a name="b913613326714"></a><a name="b913613326714"></a>eu-de</strong></li><li><strong id="b25986568102445"><a name="b25986568102445"></a><a name="b25986568102445"></a>domain_id</strong>: domain ID</li><li><strong id="b2650463110255"><a name="b2650463110255"></a><a name="b2650463110255"></a>resourcetype</strong>: resource type</li><li><strong id="b54293746102525"><a name="b54293746102525"></a><a name="b54293746102525"></a>resource</strong>: resource name, for example, <strong id="b58029856102538"><a name="b58029856102538"></a><a name="b58029856102538"></a>Topic_test</strong></li></ul>
    <p id="p6486411185420"><a name="p6486411185420"></a><a name="p6486411185420"></a>URN example: rrn:csp:smn:eu-de:e23bf08ebb924730b452426c60849564:user:Topic_test</p>
    </li></ul>
    <p id="p155741858125412"><a name="p155741858125412"></a><a name="p155741858125412"></a>By default, <strong id="b8283185919137"><a name="b8283185919137"></a><a name="b8283185919137"></a>All users</strong> is selected.</p>
    </td>
    </tr>
    <tr id="row17764975263"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p1764137112612"><a name="p1764137112612"></a><a name="p1764137112612"></a>Services</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p127648714264"><a name="p127648714264"></a><a name="p127648714264"></a>Service authorized to access DMS if <strong id="b276584015186"><a name="b276584015186"></a><a name="b276584015186"></a>Policy Type</strong> is <strong id="b976514016182"><a name="b976514016182"></a><a name="b976514016182"></a>Service-based</strong>. Currently, only SMN is authorized to access DMS.</p>
    </td>
    </tr>
    <tr id="row37641718268"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p07646792618"><a name="p07646792618"></a><a name="p07646792618"></a>Actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p8764479261"><a name="p8764479261"></a><a name="p8764479261"></a>Actions on the chosen queue.</p>
    <a name="ul0764107202618"></a><a name="ul0764107202618"></a><ul id="ul0764107202618"><li>DMS:GetQueue</li><li>DMS:CreateGroup</li><li>DMS:GetGroups</li><li>DMS:DeleteGroup</li><li>DMS:ProduceMessages</li><li>DMS:ConsumeMessages</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


