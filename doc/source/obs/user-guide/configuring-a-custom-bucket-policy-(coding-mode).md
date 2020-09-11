# Configuring a Custom Bucket Policy \(Coding Mode\)<a name="obs_03_0141"></a>

You can configure a custom bucket policy by coding. The size of a custom bucket policy cannot exceed 20 KB.

## Procedure<a name="section19588639165015"></a>

1.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Permissions**  to go to the permission management page.
3.  On the  **Bucket Policies**  tab page, configure a custom bucket policy according to your needs.

    On the right of  **Custom Bucket Policies**, select  **Coding mode**  to configure the policy in the coding mode.

4.  The coding format is as follows:

    ```
    {
       "Statement":[
           {
               "Action":[
                   "CreateBucket",
                   "DeleteBucket"
               ],
               "Effect":"Allow",
               "Principal":{
                   "ID":[
                       "domain/account ID", 
                       "domain/account ID:user/User ID" 
                   ]
               },
               "Condition":{
                   "NumericNotEquals":{
                       "Referer":"sdf"
                   },
                   "StringNotLike":{
                       "Delimiter":"ouio"
                   }
               },
               "Resource":"000-02/key01"
           }
       ]
     }
    ```

    **Table  1**  Parameter description

    <a name="table788413983114"></a>
    <table><thead align="left"><tr id="row3884698312"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p1888415933115"><a name="p1888415933115"></a><a name="p1888415933115"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p4884189113116"><a name="p4884189113116"></a><a name="p4884189113116"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row118844913113"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p988416916313"><a name="p988416916313"></a><a name="p988416916313"></a>Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p13885179143120"><a name="p13885179143120"></a><a name="p13885179143120"></a>Actions on which the bucket policy takes effect. For details, see <a href="actions.md">Actions</a>.</p>
    </td>
    </tr>
    <tr id="row48856913118"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p68858920313"><a name="p68858920313"></a><a name="p68858920313"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p15885109173115"><a name="p15885109173115"></a><a name="p15885109173115"></a>For details about bucket policy effects, see <a href="effect.md">Effect</a>.</p>
    </td>
    </tr>
    <tr id="row288519173115"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p11885594314"><a name="p11885594314"></a><a name="p11885594314"></a>Principal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p10473324123114"><a name="p10473324123114"></a><a name="p10473324123114"></a>Authorized users on whom the bucket policy takes effect. You can obtain the user ID on the <strong id="b367616232377"><a name="b367616232377"></a><a name="b367616232377"></a>My Credential</strong> page by logging in to the console as the user to be authorized. Principal format:</p>
    <a name="ul747322483120"></a><a name="ul747322483120"></a><ul id="ul747322483120"><li>"domain/<em id="i437117258387"><a name="i437117258387"></a><a name="i437117258387"></a>account ID</em>" (when the principal is an account)</li><li>"domain/<em id="i1227313238390"><a name="i1227313238390"></a><a name="i1227313238390"></a>account ID</em>:user/<em id="i173421318163919"><a name="i173421318163919"></a><a name="i173421318163919"></a>User ID</em>" (when the principal is a user under an account)</li></ul>
    <div class="note" id="note169801412124317"><a name="note169801412124317"></a><a name="note169801412124317"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p109801412154311"><a name="p109801412154311"></a><a name="p109801412154311"></a>For <strong id="b2078993175616"><a name="b2078993175616"></a><a name="b2078993175616"></a>Account ID</strong>, input the <strong id="b137894355618"><a name="b137894355618"></a><a name="b137894355618"></a>Domain ID</strong> that can be found on the <strong id="b1278918312564"><a name="b1278918312564"></a><a name="b1278918312564"></a>My Credential</strong> page.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row10885189133118"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p48851198314"><a name="p48851198314"></a><a name="p48851198314"></a>Condition</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1088519943110"><a name="p1088519943110"></a><a name="p1088519943110"></a>Conditions under which the bucket policy takes effect. For details, see <a href="conditions.md">Conditions</a>.</p>
    </td>
    </tr>
    <tr id="row17885692319"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p488511933113"><a name="p488511933113"></a><a name="p488511933113"></a>Resource</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p588515943114"><a name="p588515943114"></a><a name="p588515943114"></a>Resources on which the bucket policy takes effect. For details, see <a href="resources.md">Resources</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Save**.

