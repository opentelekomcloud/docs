# Creating a Security Group<a name="en-us_topic_0030971612"></a>

## Scenarios<a name="en-us_topic_0013748715_sffef656c3c374bd991340bf92387eaa3"></a>

To improve ECS access security, you can create a security group and add ECSs in the VPC to the security group. We recommend that you allocate ECSs that have different Internet access policies to different security groups.

## Procedure<a name="en-us_topic_0013748715_section21550084202956"></a>

1.  Log in to the management console.
2.  Click  ![](figures/en-us_image_0118621993.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Security Group**.
5.  On the  **Security Group** page, click **Create Security Group**.
6.  In the  **Create Security Group** area, set the parameters as prompted. [Table 1](#en-us_topic_0013748715_table65377617111335)  lists the parameters to be configured.

    **Figure  1**  Create Security Group<a name="en-us_topic_0013748715_fig10594164462512"></a>
    ![](figures/create-security-group.png "Create Security Group")

    **Table  1**  Parameter description

    <a name="en-us_topic_0013748715_table65377617111335"></a><table><thead align="left"><tr id="en-us_topic_0013748715_row63201700111335"><th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013748715_p24582101111429"><a name="en-us_topic_0013748715_p24582101111429"></a><a name="en-us_topic_0013748715_p24582101111429"></a><strong id="en-us_topic_0013748715_b842352706114331"><a name="en-us_topic_0013748715_b842352706114331"></a><a name="en-us_topic_0013748715_b842352706114331"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.24000000000001%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013748715_p44993128111429"><a name="en-us_topic_0013748715_p44993128111429"></a><a name="en-us_topic_0013748715_p44993128111429"></a><strong id="en-us_topic_0013748715_b84235270691113"><a name="en-us_topic_0013748715_b84235270691113"></a><a name="en-us_topic_0013748715_b84235270691113"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.34%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013748715_p20564789111429"><a name="en-us_topic_0013748715_p20564789111429"></a><a name="en-us_topic_0013748715_p20564789111429"></a><strong id="en-us_topic_0013748715_b8423527069420"><a name="en-us_topic_0013748715_b8423527069420"></a><a name="en-us_topic_0013748715_b8423527069420"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013748715_row27615987111335"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748715_p36766359111429"><a name="en-us_topic_0013748715_p36766359111429"></a><a name="en-us_topic_0013748715_p36766359111429"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.24000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748715_p25285117111429"><a name="en-us_topic_0013748715_p25285117111429"></a><a name="en-us_topic_0013748715_p25285117111429"></a>Specifies the security group name. This parameter is mandatory.</p>
    <p id="en-us_topic_0013748715_p26239466111429"><a name="en-us_topic_0013748715_p26239466111429"></a><a name="en-us_topic_0013748715_p26239466111429"></a>The security group name can contain a maximum of 64 characters, which may consist of letters, digits, underscores (_), hyphens (-), and periods (.). The name cannot contain spaces.</p>
    <div class="note" id="en-us_topic_0013748715_note26071625172323"><a name="en-us_topic_0013748715_note26071625172323"></a><a name="en-us_topic_0013748715_note26071625172323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0013748715_p33318039172323"><a name="en-us_topic_0013748715_p33318039172323"></a><a name="en-us_topic_0013748715_p33318039172323"></a>You can change the security group name after a security group is created. It is recommended that you use different names for different security groups.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="20.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748715_p2544634111429"><a name="en-us_topic_0013748715_p2544634111429"></a><a name="en-us_topic_0013748715_p2544634111429"></a>sg-318b</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013748715_row62170006111335"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013748715_p43099508111429"><a name="en-us_topic_0013748715_p43099508111429"></a><a name="en-us_topic_0013748715_p43099508111429"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.24000000000001%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013748715_p1399275111429"><a name="en-us_topic_0013748715_p1399275111429"></a><a name="en-us_topic_0013748715_p1399275111429"></a>Provides supplementary information about the security group. This parameter is optional.</p>
    <p id="en-us_topic_0013748715_p12593482111429"><a name="en-us_topic_0013748715_p12593482111429"></a><a name="en-us_topic_0013748715_p12593482111429"></a>The security group description can contain a maximum of 255 characters and cannot contain angle brackets (&lt;) or (&gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.34%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013748715_p13439131111429"><a name="en-us_topic_0013748715_p13439131111429"></a><a name="en-us_topic_0013748715_p13439131111429"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

