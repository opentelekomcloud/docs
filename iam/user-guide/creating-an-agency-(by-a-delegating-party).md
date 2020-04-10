# Creating an Agency \(by a Delegating Party\)<a name="en-us_topic_0046613147"></a>

By creating an agency, you can share your resources with other accounts, or delegate more professional personnel or teams to manage your resources. The delegated account can log in to the cloud system and switch to your account to manage your resources. You do not need to share security credentials \(such as passwords and access keys\) with other accounts, ensuring the security of your account.

## Procedure<a name="section2672115"></a>

1.  In the navigation pane, choose  **Agencies**.
2.  On the  **Agencies**  page, click  **Create Agency**.
3.  Specify  **Agency Name**  and  **Agency Type**.

    **Table  1**  Agency types

    <a name="table5607179122211"></a>
    <table><thead align="left"><tr id="row19607109132216"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="p8464131619225"><a name="p8464131619225"></a><a name="p8464131619225"></a><strong id="b8423527061059"><a name="b8423527061059"></a><a name="b8423527061059"></a>Agency Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="p16466101617224"><a name="p16466101617224"></a><a name="p16466101617224"></a><strong id="b36291382142815"><a name="b36291382142815"></a><a name="b36291382142815"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1060715911225"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p104684169229"><a name="p104684169229"></a><a name="p104684169229"></a>Common account</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p64704162225"><a name="p64704162225"></a><a name="p64704162225"></a>Common accounts in the cloud system. This agency type is used to share resources with other accounts or delegate other accounts to manage the resources in your account.</p>
    </td>
    </tr>
    <tr id="row126078962210"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p1847261611225"><a name="p1847261611225"></a><a name="p1847261611225"></a>Cloud service</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p1447431614222"><a name="p1447431614222"></a><a name="p1447431614222"></a>Services in the cloud system. This agency type is used to authorize cloud services to access or maintain user data. For example, after an agency with ECS is created, ECS can obtain users' access keys to call APIs, facilitating O&amp;M and monitoring.</p>
    </td>
    </tr>
    </tbody>
    </table>

    -   If you set  **Agency Type**  to  **Common account**, enter the domain name of a common account for which the trust relationship is to be established in  **Delegated Account**.
    -   If you set  **Agency Type**  to  **Cloud service**, click  **Select**  and set the cloud service.

4.  Set  **Validity Period**  and enter  **Description**.
5.  In the  **Permissions**  area, locate the row that contains the target region and project and click  **Modify**  in the  **Operation**  column, and select policies for the delegating enterprise.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For details about the permissions, see  [Permission Description](https://docs.otc.t-systems.com/permissions/index.html).  

6.  Click  **OK**.

    The newly created agency is displayed in the agency list. The delegated account can manage resources in the delegating account by switching the role.


## Follow-up Operation<a name="section54138067163127"></a>

In the agency list, you can click  **Modify**  in the row that contains the newly created agency to modify the basic information about the agency, such as the permissions and validity period of the agency.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Cloud service agencies cannot be modified.  

