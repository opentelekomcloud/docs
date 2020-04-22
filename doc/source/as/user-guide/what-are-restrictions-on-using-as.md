# What Are Restrictions on Using AS?<a name="EN-US_TOPIC_0042018398"></a>

Only applications that are stateless and can be horizontally scaled can run on instances in an AS group. AS automatically releases instances. Therefore, the instances in AS groups cannot be used to save application status information \(such as sessions\) and related data \(such as database data and logs\).

If the application status or related data must be saved, you can store the information on separate servers.

-   AS requires authentication provided by Identity and Access Management \(IAM\).

    The AS administrator account requires permissions of the tenant guest, ECS administrator, Cloud Eye administrator, and ELB administrator.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the Cloud Eye administrator is not available, you can only use an existing alarm to create an alarm policy. If the ELB administrator is not available, you can still use existing load balancers.  

-   AS resources must comply with quota requirements listed in  [Table 1](#table18879114515369).

    **Table  1**  Quota list

    <a name="table18879114515369"></a>
    <table><thead align="left"><tr id="row1927114039"><th class="cellrowborder" valign="top" width="18.48%" id="mcps1.2.4.1.1"><p id="p27061756192411"><a name="p27061756192411"></a><a name="p27061756192411"></a>Category</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.22%" id="mcps1.2.4.1.2"><p id="p1070716560246"><a name="p1070716560246"></a><a name="p1070716560246"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.3"><p id="p870717564246"><a name="p870717564246"></a><a name="p870717564246"></a>Default Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1585323433"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="p37073567249"><a name="p37073567249"></a><a name="p37073567249"></a>AS group</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="p157083565243"><a name="p157083565243"></a><a name="p157083565243"></a>Maximum number of AS groups that a user can create</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="p170855619247"><a name="p170855619247"></a><a name="p170855619247"></a>25</p>
    </td>
    </tr>
    <tr id="row2079079942"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="p1470845615247"><a name="p1470845615247"></a><a name="p1470845615247"></a>AS configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="p1470914560245"><a name="p1470914560245"></a><a name="p1470914560245"></a>Maximum number of AS configurations that a user can create</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="p070905615241"><a name="p070905615241"></a><a name="p070905615241"></a>100</p>
    </td>
    </tr>
    <tr id="row1666946907"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="p1710205610241"><a name="p1710205610241"></a><a name="p1710205610241"></a>AS policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="p27108567244"><a name="p27108567244"></a><a name="p27108567244"></a>Maximum number of AS policies that can be added to an AS group</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="p771105622416"><a name="p771105622416"></a><a name="p771105622416"></a>50</p>
    </td>
    </tr>
    <tr id="row2086844637"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="p16711145610242"><a name="p16711145610242"></a><a name="p16711145610242"></a>Instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="p107111856172413"><a name="p107111856172413"></a><a name="p107111856172413"></a>Maximum number of instances that can be added to an AS group</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="p471220562249"><a name="p471220562249"></a><a name="p471220562249"></a>200</p>
    </td>
    </tr>
    <tr id="row2138069609"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="p37131256202412"><a name="p37131256202412"></a><a name="p37131256202412"></a>Bandwidth scaling policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="p11713185622412"><a name="p11713185622412"></a><a name="p11713185622412"></a>Maximum number of bandwidth scaling policies that a user can create</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="p671435622413"><a name="p671435622413"></a><a name="p671435622413"></a>50</p>
    </td>
    </tr>
    </tbody>
    </table>


