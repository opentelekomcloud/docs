# Creating an Agency<a name="en-us_topic_0046613147"></a>

If you want to share your resources with other accounts or delegate a more professional person or team to manage your resources, the security administrator in your account can create an agency and authorize a delegated account. The delegated account can log in to the public cloud system and switch to your account to manage your resources. You do not need to share security credentials \(such as passwords and access keys\) with other accounts, ensuring the security of your account.

## Procedure<a name="section2672115"></a>

1.  Choose **Management & Deployment** \> **Identity and Access Management**.
2.  In the navigation pane, choose **Agency**.
3.  On the **Agency** page, click **Create**.
4.  On the **Create Agency** page, specify **Agency Name** and **Agency Type**.**Table 1** Agency types

    <a name="table3419708416848"></a><table><thead align="left"><tr id="row4839230716848"><th class="cellrowborder" valign="top" width="21.51%" id="mcps1.2.3.1.1"><p id="p4583867116848"><a name="p4583867116848"></a><a name="p4583867116848"></a>Agency Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="78.49000000000001%" id="mcps1.2.3.1.2"><p id="p2194486616848"><a name="p2194486616848"></a><a name="p2194486616848"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6328607116848"><td class="cellrowborder" valign="top" width="21.51%" headers="mcps1.2.3.1.1 "><p id="p2589811616848"><a name="p2589811616848"></a><a name="p2589811616848"></a>Common account</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.49000000000001%" headers="mcps1.2.3.1.2 "><p id="p1737263316848"><a name="p1737263316848"></a><a name="p1737263316848"></a>Common accounts in the public cloud system. This agency type is used to share resources with other accounts or delegate other accounts to manage the resources in your account.</p>
    </td>
    </tr>
    <tr id="row2213597516848"><td class="cellrowborder" valign="top" width="21.51%" headers="mcps1.2.3.1.1 "><p id="p4818351616848"><a name="p4818351616848"></a><a name="p4818351616848"></a>Cloud service</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.49000000000001%" headers="mcps1.2.3.1.2 "><p id="p1055070116848"><a name="p1055070116848"></a><a name="p1055070116848"></a>Services in the public cloud system. This agency type is used to authorize cloud services to access or maintain user data. For example, after an agency with ECS is created, ECS can obtain users' access keys to call APIs, facilitating O&amp;M and monitoring.</p>
    <div class="note" id="note62113030161136"><a name="note62113030161136"></a><a name="note62113030161136"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p22146364161136"><a name="p22146364161136"></a><a name="p22146364161136"></a>After you create an agency with <strong id="b11175035145542"><a name="b11175035145542"></a><a name="b11175035145542"></a>Agency Type</strong> set to <strong id="b32762662145542"><a name="b32762662145542"></a><a name="b32762662145542"></a>Cloud service</strong>, the agency cannot be modified.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    -   If you set **Agency Type** to **Common** **account**, enter the delegated account name in **Delegated Account**.
    -   If you set **Agency Type** to **Cloud service**, click **Select** and set the cloud service.
5.  Set **Validity Period** and enter **Description**.
6.  In the **Permissions** area, click **Modify** in the **Operation** column of the row that contains the target project.
7.  In the **Modify Permission** dialog box, select permission sets.

    > ![](public_sys-resources/icon-note.gif) **NOTE:** 

    > For details, see [Permissions](https://docs.otc.t-systems.com/permissions/index.html).

8.  Click **OK**.

    The newly created agency is displayed in the agency list.


## Follow-up Operation<a name="section54138067163127"></a>

In the agency list, you can click **Modify** in the row that contains the newly created agency to modify the basic information about the agency, such as the permissions and validity period of the agency.

> ![](public_sys-resources/icon-note.gif) **NOTE:** 

> You can only modify an agency whose **Agency Type** is set to **Common account**.

