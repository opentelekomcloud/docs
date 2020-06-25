# Assigning an EIP and Binding It to an ECS<a name="en-us_topic_0013748738"></a>

## Scenarios<a name="s974a02c09b8e44f59dcc9335de2d030a"></a>

You can assign an EIP and bind it to an ECS so that the ECS can access the Internet.

## Assigning an EIP<a name="section16739352111811"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Elastic IP**.
4.  On the displayed page, click  **Assign EIP**.
5.  Set the parameters as prompted.

    **Figure  1**  Assign EIP<a name="fig61031316104110"></a>  
    ![](figures/assign-eip.png "assign-eip")

    **Table  1**  Parameter description

    <a name="tb8e92f5357304d0297e9c203270c546e"></a>
    <table><thead align="left"><tr id="r66aedde49c144d8a84278fc61dadffdd"><th class="cellrowborder" valign="top" width="31.65%" id="mcps1.2.4.1.1"><p id="aafd79e8ecf074d0da2b802ca103815d1"><a name="aafd79e8ecf074d0da2b802ca103815d1"></a><a name="aafd79e8ecf074d0da2b802ca103815d1"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.29%" id="mcps1.2.4.1.2"><p id="a30252599cf9146418f791259ec182081"><a name="a30252599cf9146418f791259ec182081"></a><a name="a30252599cf9146418f791259ec182081"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.3"><p id="a02cb30a37b3a49abb2a82c12344214df"><a name="a02cb30a37b3a49abb2a82c12344214df"></a><a name="a02cb30a37b3a49abb2a82c12344214df"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row69311030161113"><td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.1 "><p id="p1211443310119"><a name="p1211443310119"></a><a name="p1211443310119"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.29%" headers="mcps1.2.4.1.2 "><p id="p411903317112"><a name="p411903317112"></a><a name="p411903317112"></a>Specifies the desired region. Regions are geographic areas isolated from each other. Resources are region-specific and cannot be used across regions through internal network connections. For low network latency and quick resource access, select the nearest region.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p7738111114910"><a name="p7738111114910"></a><a name="p7738111114910"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row1755815445016"><td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.1 "><p id="p0829195012711"><a name="p0829195012711"></a><a name="p0829195012711"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.29%" headers="mcps1.2.4.1.2 "><a name="ul48291050376"></a><a name="ul48291050376"></a><ul id="ul48291050376"><li><strong id="b8332452162712"><a name="b8332452162712"></a><a name="b8332452162712"></a>Dynamic BGP</strong>: When changes occur on a network using dynamic BGP, routing protocols provide automatic, real-time optimization of network configurations, ensuring network stability and improving user experience.</li><li><strong id="b10944114901910"><a name="b10944114901910"></a><a name="b10944114901910"></a>Mail BGP</strong>: EIPs with port 25 enabled are used.</li></ul>
    <p id="p13668174021018"><a name="p13668174021018"></a><a name="p13668174021018"></a>The EIP type can be selected only when you assign an EIP.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p18829105015715"><a name="p18829105015715"></a><a name="p18829105015715"></a>Dynamic BGP</p>
    </td>
    </tr>
    <tr id="row34521952120"><td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.1 "><p id="p28291050473"><a name="p28291050473"></a><a name="p28291050473"></a>Bandwidth Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.29%" headers="mcps1.2.4.1.2 "><p id="p1182920501978"><a name="p1182920501978"></a><a name="p1182920501978"></a>The following bandwidth types are available:</p>
    <a name="ul14829145016717"></a><a name="ul14829145016717"></a><ul id="ul14829145016717"><li><strong id="b14650281553"><a name="b14650281553"></a><a name="b14650281553"></a>Dedicated</strong>: The bandwidth can be used by only one EIP.</li><li><strong id="b1785064814460"><a name="b1785064814460"></a><a name="b1785064814460"></a>Shared</strong>: The bandwidth can be allocated to multiple EIPs. These EIPs can share the bandwidth.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p582925010715"><a name="p582925010715"></a><a name="p582925010715"></a>Dedicated</p>
    </td>
    </tr>
    <tr id="row220919163166"><td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.1 "><p id="p741017230161"><a name="p741017230161"></a><a name="p741017230161"></a>Bandwidth Size</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.29%" headers="mcps1.2.4.1.2 "><p id="p44131723121613"><a name="p44131723121613"></a><a name="p44131723121613"></a>Specifies the bandwidth size in Mbit/s.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p15417172316166"><a name="p15417172316166"></a><a name="p15417172316166"></a>100</p>
    </td>
    </tr>
    <tr id="row1798051216168"><td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.1 "><p id="p44256235163"><a name="p44256235163"></a><a name="p44256235163"></a>Bandwidth Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.29%" headers="mcps1.2.4.1.2 "><p id="p134282234164"><a name="p134282234164"></a><a name="p134282234164"></a>Specifies the name of the bandwidth.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p2430182381611"><a name="p2430182381611"></a><a name="p2430182381611"></a>bandwidth</p>
    </td>
    </tr>
    <tr id="row72697164367"><td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.1 "><p id="p32701616183611"><a name="p32701616183611"></a><a name="p32701616183611"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.29%" headers="mcps1.2.4.1.2 "><p id="p9270111616363"><a name="p9270111616363"></a><a name="p9270111616363"></a>Specifies the EIP tag that consists of a key and value pair.</p>
    <p id="p011163020377"><a name="p011163020377"></a><a name="p011163020377"></a>The tag key and value must meet the requirements listed in <a href="#table36606052153313">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><a name="ul1423104520372"></a><a name="ul1423104520372"></a><ul id="ul1423104520372"><li>Key: Ipv4_key1</li><li>Value: 192.168.12.10</li></ul>
    </td>
    </tr>
    <tr id="rf9c18d6cf2554db48da9ab7a351d00a7"><td class="cellrowborder" valign="top" width="31.65%" headers="mcps1.2.4.1.1 "><p id="ad3ab73d5ac10468fa5c52ab44adb0196"><a name="ad3ab73d5ac10468fa5c52ab44adb0196"></a><a name="ad3ab73d5ac10468fa5c52ab44adb0196"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0029397266_p816336174522"><a name="en-us_topic_0029397266_p816336174522"></a><a name="en-us_topic_0029397266_p816336174522"></a>Specifies the number of EIPs to be assigned.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="ab9a9778fda6e45d7b5710ab0d310f64c"><a name="ab9a9778fda6e45d7b5710ab0d310f64c"></a><a name="ab9a9778fda6e45d7b5710ab0d310f64c"></a>1</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  EIP tag requirements

    <a name="table36606052153313"></a>
    <table><thead align="left"><tr id="en-us_topic_0068145818_rd57708e01e6443a9805ca72f554fae7f"><th class="cellrowborder" valign="top" width="18.54%" id="mcps1.2.4.1.1"><p id="en-us_topic_0068145818_abc7708d69440476086850b219c70efa8"><a name="en-us_topic_0068145818_abc7708d69440476086850b219c70efa8"></a><a name="en-us_topic_0068145818_abc7708d69440476086850b219c70efa8"></a><strong id="en-us_topic_0068145818_b842352706165123"><a name="en-us_topic_0068145818_b842352706165123"></a><a name="en-us_topic_0068145818_b842352706165123"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.39%" id="mcps1.2.4.1.2"><p id="en-us_topic_0068145818_a0df2f83c3277432ab05b525e4ffb1c2c"><a name="en-us_topic_0068145818_a0df2f83c3277432ab05b525e4ffb1c2c"></a><a name="en-us_topic_0068145818_a0df2f83c3277432ab05b525e4ffb1c2c"></a><strong id="en-us_topic_0068145818_b842352706174218"><a name="en-us_topic_0068145818_b842352706174218"></a><a name="en-us_topic_0068145818_b842352706174218"></a>Requirement</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.3"><p id="en-us_topic_0068145818_a902e732241f94e96b0b1b718cf7ed639"><a name="en-us_topic_0068145818_a902e732241f94e96b0b1b718cf7ed639"></a><a name="en-us_topic_0068145818_a902e732241f94e96b0b1b718cf7ed639"></a><strong id="en-us_topic_0068145818_b842352706174227"><a name="en-us_topic_0068145818_b842352706174227"></a><a name="en-us_topic_0068145818_b842352706174227"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0068145818_r95612b479088487b99e620f90b71f798"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0068145818_a7694a48138124d1daf3804556a27bfd6"><a name="en-us_topic_0068145818_a7694a48138124d1daf3804556a27bfd6"></a><a name="en-us_topic_0068145818_a7694a48138124d1daf3804556a27bfd6"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0068145818_uac40e19ce4ac49d0913d48b334564c45"></a><a name="en-us_topic_0068145818_uac40e19ce4ac49d0913d48b334564c45"></a><ul id="en-us_topic_0068145818_uac40e19ce4ac49d0913d48b334564c45"><li>Cannot be left blank.</li><li>Must be unique for each EIP.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0068145818_uccb317c6616b4445aa84b125e5aa017f"></a><a name="en-us_topic_0068145818_uccb317c6616b4445aa84b125e5aa017f"></a><ul id="en-us_topic_0068145818_uccb317c6616b4445aa84b125e5aa017f"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0068145818_a1a10de6d67c04555a3508a8cdc3500e7"><a name="en-us_topic_0068145818_a1a10de6d67c04555a3508a8cdc3500e7"></a><a name="en-us_topic_0068145818_a1a10de6d67c04555a3508a8cdc3500e7"></a>Ipv4_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0068145818_r32a79d8bde844fda8a6254383317e58f"><td class="cellrowborder" valign="top" width="18.54%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0068145818_a1ebd1dda592448d49631c7f099519113"><a name="en-us_topic_0068145818_a1ebd1dda592448d49631c7f099519113"></a><a name="en-us_topic_0068145818_a1ebd1dda592448d49631c7f099519113"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.39%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0068145818_uaf17b1ea9b9a4e58b95cafefa2898283"></a><a name="en-us_topic_0068145818_uaf17b1ea9b9a4e58b95cafefa2898283"></a><ul id="en-us_topic_0068145818_uaf17b1ea9b9a4e58b95cafefa2898283"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0068145818_ub74c759faad544c3b4428accc9c42b80"></a><a name="en-us_topic_0068145818_ub74c759faad544c3b4428accc9c42b80"></a><ul id="en-us_topic_0068145818_ub74c759faad544c3b4428accc9c42b80"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0068145818_a21a035aeb72143f5ab0fd45a08248d08"><a name="en-us_topic_0068145818_a21a035aeb72143f5ab0fd45a08248d08"></a><a name="en-us_topic_0068145818_a21a035aeb72143f5ab0fd45a08248d08"></a>192.168.12.10</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Assign Now**.
7.  Click  **Submit**.

## Binding an EIP<a name="section6234163111911"></a>

1.  On the  **EIPs**  page, locate the row that contains the target EIP, and click  **Bind**.
2.  Select the desired instance.

    **Figure  2**  Bind EIP<a name="fig42552497182029"></a>  
    ![](figures/bind-eip.png "bind-eip")

3.  Click  **OK**.

An IPv6 client on the Internet can access the ECS that has an EIP bound in a VPC. For details about the implementation and constraints, see  [How Does an IPv6 Client on the Internet Access the ECS That Has an EIP Bound in a VPC?](how-does-an-ipv6-client-on-the-internet-access-the-ecs-that-has-an-eip-bound-in-a-vpc.md).

