# Creating an AS Configuration<a name="EN-US_TOPIC_0043063055"></a>

## Function<a name="section66578044"></a>

This interface is used to create an AS configuration.

-   An AS configuration is a template of ECSs in an AS group. It defines the specifications of the instances to be added to the AS group.
-   The AS configuration is decoupled from the AS group. An AS configuration can be used by multiple AS groups.
-   Up to 100 AS configurations can be created for each user.

## URI<a name="section62331491"></a>

POST /autoscaling-api/v1/\{project\_id\}/scaling\_configuration

**Table  1**  Parameter description

<a name="table35416756"></a>
<table><thead align="left"><tr id="row47063428"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p54041329"><a name="p54041329"></a><a name="p54041329"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p15271547"><a name="p15271547"></a><a name="p15271547"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p29035785"><a name="p29035785"></a><a name="p29035785"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="p3088388"><a name="p3088388"></a><a name="p3088388"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48832851"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p63146847"><a name="p63146847"></a><a name="p63146847"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p14620943"><a name="p14620943"></a><a name="p14620943"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p43445707"><a name="p43445707"></a><a name="p43445707"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section24112512"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table30400195"></a>
    <table><thead align="left"><tr id="row25496434"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p51945267"><a name="p51945267"></a><a name="p51945267"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.2"><p id="p46817064"><a name="p46817064"></a><a name="p46817064"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p34085817"><a name="p34085817"></a><a name="p34085817"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.5.1.4"><p id="p9487824"><a name="p9487824"></a><a name="p9487824"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30316242"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p39696553"><a name="p39696553"></a><a name="p39696553"></a>scaling_configuration_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p61304253"><a name="p61304253"></a><a name="p61304253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p66697461"><a name="p66697461"></a><a name="p66697461"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p33785274"><a name="p33785274"></a><a name="p33785274"></a>Specifies the AS configuration name. The name contains only letters, digits, underscores (_), and hyphens (-), and cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row35632012"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p511887"><a name="p511887"></a><a name="p511887"></a>instance_config</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p41462866"><a name="p41462866"></a><a name="p41462866"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p15686522173916"><a name="p15686522173916"></a><a name="p15686522173916"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p45638969"><a name="p45638969"></a><a name="p45638969"></a>Specifies the ECS configuration. For details, see <a href="#table5981573891121">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **instance\_config**  field description

    <a name="table5981573891121"></a>
    <table><thead align="left"><tr id="r4c26d84153be4464b22847e9b6182390"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.1"><p id="ae87dd78bead34b4bb60b8b3f402c44f2"><a name="ae87dd78bead34b4bb60b8b3f402c44f2"></a><a name="ae87dd78bead34b4bb60b8b3f402c44f2"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.2"><p id="p5549735191529"><a name="p5549735191529"></a><a name="p5549735191529"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="a4950d94907064b47a4bda4858a33cdc0"><a name="a4950d94907064b47a4bda4858a33cdc0"></a><a name="a4950d94907064b47a4bda4858a33cdc0"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.57425742574257%" id="mcps1.2.5.1.4"><p id="a797f28c561484893b5f5cfc317582ba5"><a name="a797f28c561484893b5f5cfc317582ba5"></a><a name="a797f28c561484893b5f5cfc317582ba5"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4833983694940"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p2321261094940"><a name="p2321261094940"></a><a name="p2321261094940"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p117325794940"><a name="p117325794940"></a><a name="p117325794940"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p2792498494940"><a name="p2792498494940"></a><a name="p2792498494940"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="p5714172410748"><a name="p5714172410748"></a><a name="p5714172410748"></a>Specifies the ECS ID. When using the existing ECS specifications as the template to create AS configurations, specify this parameter. In this case, the <strong id="b84235270618340"><a name="b84235270618340"></a><a name="b84235270618340"></a>flavorRef</strong>, <strong id="b84235270618345"><a name="b84235270618345"></a><a name="b84235270618345"></a>imageRef</strong>, <strong id="b84235270618349"><a name="b84235270618349"></a><a name="b84235270618349"></a>disk</strong>, and <strong id="b4205314195116"><a name="b4205314195116"></a><a name="b4205314195116"></a>security_groups</strong> fields do not take effect.</p>
    <p id="p3937759195828"><a name="p3937759195828"></a><a name="p3937759195828"></a>If the <strong id="b842352706183458"><a name="b842352706183458"></a><a name="b842352706183458"></a>instance_id</strong> field is not specified, <strong id="b884057306183518"><a name="b884057306183518"></a><a name="b884057306183518"></a>flavorRef</strong>, <strong id="b1056433101183518"><a name="b1056433101183518"></a><a name="b1056433101183518"></a>imageRef</strong>, and <strong id="b1299744514183518"><a name="b1299744514183518"></a><a name="b1299744514183518"></a>disk</strong> fields are mandatory.</p>
    </td>
    </tr>
    <tr id="r91b06878f5da4447abf9b85bf4c82bc6"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="a509afeee56a44a43897bac222c61f3ff"><a name="a509afeee56a44a43897bac222c61f3ff"></a><a name="a509afeee56a44a43897bac222c61f3ff"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p6610046591529"><a name="p6610046591529"></a><a name="p6610046591529"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="af5eccdf2dbd04ef8ae9a07f3f57472e0"><a name="af5eccdf2dbd04ef8ae9a07f3f57472e0"></a><a name="af5eccdf2dbd04ef8ae9a07f3f57472e0"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="a068eef21ab6b4492876594074b9a6ea8"><a name="a068eef21ab6b4492876594074b9a6ea8"></a><a name="a068eef21ab6b4492876594074b9a6ea8"></a>Specifies the ECS flavor ID. A maximum of 10 flavors can be selected. Use a comma (,) to separate multiple flavor IDs. You can obtain its value from the API for querying details about flavors and extended flavor information. </p>
    </td>
    </tr>
    <tr id="rc85492fa8fb7484b8f9ce867ee9c9db6"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="a0ef3b55b17824d92a0b4fff8a3b9fc6f"><a name="a0ef3b55b17824d92a0b4fff8a3b9fc6f"></a><a name="a0ef3b55b17824d92a0b4fff8a3b9fc6f"></a>imageRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p5253743991529"><a name="p5253743991529"></a><a name="p5253743991529"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="a0b7ade9132b143a18449fed7c25c1794"><a name="a0b7ade9132b143a18449fed7c25c1794"></a><a name="a0b7ade9132b143a18449fed7c25c1794"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="a1aafc582cb754139946238475192748d"><a name="a1aafc582cb754139946238475192748d"></a><a name="a1aafc582cb754139946238475192748d"></a>Specifies the image ID. Its value is the same as that of <strong id="b84235270619918"><a name="b84235270619918"></a><a name="b84235270619918"></a>image_id</strong> for specifying the image selected during ECS creation. Obtain the value using the API for querying images. .</p>
    </td>
    </tr>
    <tr id="r7d3d6a0636424a11aef13684aeacd387"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="a2fd0f5cb13fa4b2e9cce0a57e5755405"><a name="a2fd0f5cb13fa4b2e9cce0a57e5755405"></a><a name="a2fd0f5cb13fa4b2e9cce0a57e5755405"></a>disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p2767417091529"><a name="p2767417091529"></a><a name="p2767417091529"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="a59f1976b777c49dabc9f22e498393078"><a name="a59f1976b777c49dabc9f22e498393078"></a><a name="a59f1976b777c49dabc9f22e498393078"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="aeafe48e042c04c619ee16094cf39bdca"><a name="aeafe48e042c04c619ee16094cf39bdca"></a><a name="aeafe48e042c04c619ee16094cf39bdca"></a>Specifies the disk group information. System disks are mandatory and data disks are optional. For details, see <a href="#table279810959126">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row3676444084457"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p438140798456"><a name="p438140798456"></a><a name="p438140798456"></a>key_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p592794868456"><a name="p592794868456"></a><a name="p592794868456"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p369090508456"><a name="p369090508456"></a><a name="p369090508456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="p368430348456"><a name="p368430348456"></a><a name="p368430348456"></a>Specifies the name of the SSH key pair used to log in to the ECS.</p>
    </td>
    </tr>
    <tr id="r20296d7eb44f447f8a64bbc0a96e87d2"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="a44d4ff71822642e8a3299c7beebc4da7"><a name="a44d4ff71822642e8a3299c7beebc4da7"></a><a name="a44d4ff71822642e8a3299c7beebc4da7"></a>personality</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p1269859791529"><a name="p1269859791529"></a><a name="p1269859791529"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="af0a4b1b96a534569986e2f66b4c3a81f"><a name="af0a4b1b96a534569986e2f66b4c3a81f"></a><a name="af0a4b1b96a534569986e2f66b4c3a81f"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="a76bd6d9b0fcf4bc795d8cd02cd71669b"><a name="a76bd6d9b0fcf4bc795d8cd02cd71669b"></a><a name="a76bd6d9b0fcf4bc795d8cd02cd71669b"></a>Specifies information about the injected file. Only text files can be injected. A maximum of five files can be injected at a time and the maximum size of each file is 1 KB. For details, see <a href="#table3396587291242">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row53959709102955"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p8660319102955"><a name="p8660319102955"></a><a name="p8660319102955"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p30397262102955"><a name="p30397262102955"></a><a name="p30397262102955"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p16206163593912"><a name="p16206163593912"></a><a name="p16206163593912"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="p42992030"><a name="p42992030"></a><a name="p42992030"></a>Specifies the EIP of the ECS. The EIP can be configured in two ways. For details, see <a href="#table105840310312">Table 7</a>.</p>
    <a name="ul41483341153130"></a><a name="ul41483341153130"></a><ul id="ul41483341153130"><li>Do not use an EIP. In this case, this parameter is unavailable.</li><li>Automatically assign an EIP. You need to specify the information about the new EIP.</li></ul>
    </td>
    </tr>
    <tr id="row65213387183650"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p47793031183650"><a name="p47793031183650"></a><a name="p47793031183650"></a>user_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p46030270183650"><a name="p46030270183650"></a><a name="p46030270183650"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p37464410183650"><a name="p37464410183650"></a><a name="p37464410183650"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="p75316311525"><a name="p75316311525"></a><a name="p75316311525"></a>Specifies the user data to be injected during the ECS creation process. Text, text files, and gzip files can be injected. </p>
    <p id="p18531131105212"><a name="p18531131105212"></a><a name="p18531131105212"></a>Constraints:</p>
    <a name="ul954173117522"></a><a name="ul954173117522"></a><ul id="ul954173117522"><li>The content to be injected must be encoded with base64. The maximum size of the content to be injected (before encoding) is 32 KB.</li></ul>
    <p id="p2062915093518"><a name="p2062915093518"></a><a name="p2062915093518"></a>Examples:</p>
    <a name="ul13541314520"></a><a name="ul13541314520"></a><ul id="ul13541314520"><li>Linux<pre class="screen" id="screen16541531125220"><a name="screen16541531125220"></a><a name="screen16541531125220"></a>#! /bin/bash
    echo user_test &gt;&gt; /home/user.txt</pre>
    </li><li>Windows<pre class="screen" id="screen35418316520"><a name="screen35418316520"></a><a name="screen35418316520"></a>rem cmd
    echo 111 &gt; c:\aaa.txt</pre>
    </li></ul>
    </td>
    </tr>
    <tr id="row5961124394643"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p6378139794643"><a name="p6378139794643"></a><a name="p6378139794643"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p6601952394643"><a name="p6601952394643"></a><a name="p6601952394643"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p4598115094643"><a name="p4598115094643"></a><a name="p4598115094643"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="p3348564594643"><a name="p3348564594643"></a><a name="p3348564594643"></a>Specifies the ECS metadata. For details, see <a href="#table6119722495435">Table 10</a>.</p>
    </td>
    </tr>
    <tr id="row1574783418203"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p14930144516201"><a name="p14930144516201"></a><a name="p14930144516201"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p1693074517206"><a name="p1693074517206"></a><a name="p1693074517206"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p10175134115396"><a name="p10175134115396"></a><a name="p10175134115396"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="p9394187112314"><a name="p9394187112314"></a><a name="p9394187112314"></a>Specifies security groups. For details, see <a href="#table144645712211">Table 11</a>. </p>
    <p id="p14930194512015"><a name="p14930194512015"></a><a name="p14930194512015"></a>If the security group is specified both in the AS configuration and AS group, the security group specified in the AS configuration prevails. If the security group is not specified in either of them, the default security group is used. For your convenience, you are advised to specify the security group in the AS configuration.</p>
    </td>
    </tr>
    <tr id="row099113253218"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p1777713012214"><a name="p1777713012214"></a><a name="p1777713012214"></a>market_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p1377718301220"><a name="p1377718301220"></a><a name="p1377718301220"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="p17779301420"><a name="p17779301420"></a><a name="p17779301420"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="p0897134016220"><a name="p0897134016220"></a><a name="p0897134016220"></a>This parameter is reserved.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **disk**  field description

    <a name="table279810959126"></a>
    <table><thead align="left"><tr id="r357c6f0bb9f342809f9c348ed70a9968"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="ab740b0232cd54c0e85af7cd7a1291270"><a name="ab740b0232cd54c0e85af7cd7a1291270"></a><a name="ab740b0232cd54c0e85af7cd7a1291270"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.2"><p id="p5608268791811"><a name="p5608268791811"></a><a name="p5608268791811"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="aec91c4d91bd64bebba818293af6106c2"><a name="aec91c4d91bd64bebba818293af6106c2"></a><a name="aec91c4d91bd64bebba818293af6106c2"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="a2c67dda839364047a779f76c6d45c2a1"><a name="a2c67dda839364047a779f76c6d45c2a1"></a><a name="a2c67dda839364047a779f76c6d45c2a1"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r184900d8743c4eac936d0f08517229ba"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="a2b40e8a57985423ea748cbba0db2f958"><a name="a2b40e8a57985423ea748cbba0db2f958"></a><a name="a2b40e8a57985423ea748cbba0db2f958"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p4640382191811"><a name="p4640382191811"></a><a name="p4640382191811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="a93c78ee974024a56a7e7ef417cd54fa0"><a name="a93c78ee974024a56a7e7ef417cd54fa0"></a><a name="a93c78ee974024a56a7e7ef417cd54fa0"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="ad58bc0b1affa4c0f9d6f03cef81dd4f0"><a name="ad58bc0b1affa4c0f9d6f03cef81dd4f0"></a><a name="ad58bc0b1affa4c0f9d6f03cef81dd4f0"></a>Specifies the disk size. The unit is GB.</p>
    <p id="p43554686145747"><a name="p43554686145747"></a><a name="p43554686145747"></a>The system disk size ranges from 1 to 1024 and must be greater than or equal to the minimum size (<strong id="b1978214517138"><a name="b1978214517138"></a><a name="b1978214517138"></a>min_disk</strong> value) of the system disk specified in the image.</p>
    <p id="p5562853216262"><a name="p5562853216262"></a><a name="p5562853216262"></a>The data disk size ranges from 10 to 32768.</p>
    </td>
    </tr>
    <tr id="r2f1e5724d07040ea9695bb591a5f5c5e"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="a722115890c2146c48fef0bd6aef24dd1"><a name="a722115890c2146c48fef0bd6aef24dd1"></a><a name="a722115890c2146c48fef0bd6aef24dd1"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p61313191811"><a name="p61313191811"></a><a name="p61313191811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="ae311d77181a6412887d36d37fce61759"><a name="ae311d77181a6412887d36d37fce61759"></a><a name="ae311d77181a6412887d36d37fce61759"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p54864902"><a name="p54864902"></a><a name="p54864902"></a>Specifies the ECS system disk type. The disk type must match the available disk type.</p>
    <a name="ul32900150164116"></a><a name="ul32900150164116"></a><ul id="ul32900150164116"><li><strong id="b842352706144153"><a name="b842352706144153"></a><a name="b842352706144153"></a>SATA</strong>: common I/O disk type</li><li><strong id="b842352706144157"><a name="b842352706144157"></a><a name="b842352706144157"></a>SAS</strong>: high I/O disk type</li><li><strong id="b84235270614420"><a name="b84235270614420"></a><a name="b84235270614420"></a>SSD</strong>: ultra-high I/O disk type</li><li><strong id="b14801824142717"><a name="b14801824142717"></a><a name="b14801824142717"></a>co-p1</strong>: high I/O (performance-optimized I) disk type</li><li><strong id="b973015355271"><a name="b973015355271"></a><a name="b973015355271"></a>uh-l1</strong>: ultra-high I/O (latency-optimized) disk type</li></ul>
    <div class="note" id="note1189393515548"><a name="note1189393515548"></a><a name="note1189393515548"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p188949357544"><a name="p188949357544"></a><a name="p188949357544"></a>For HANA, HL1, and HL2 ECSs, use co-p1 and uh-l1 disks. For other ECSs, do not use co-p1 or uh-l1 disks.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r252618b0a3c741db83283ef15bd6c2da"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="a5bc291d03ad648e4a94aedd34e30633d"><a name="a5bc291d03ad648e4a94aedd34e30633d"></a><a name="a5bc291d03ad648e4a94aedd34e30633d"></a>disk_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p4966361791811"><a name="p4966361791811"></a><a name="p4966361791811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="ad99ff23668e34c8daf7da9183db829a7"><a name="ad99ff23668e34c8daf7da9183db829a7"></a><a name="ad99ff23668e34c8daf7da9183db829a7"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p166542512353"><a name="p166542512353"></a><a name="p166542512353"></a>Specifies a disk type. The options are as follows:</p>
    <a name="ul1050113813519"></a><a name="ul1050113813519"></a><ul id="ul1050113813519"><li><strong id="b842352706182939"><a name="b842352706182939"></a><a name="b842352706182939"></a>DATA</strong>: indicates a data disk.</li><li><strong id="b842352706182952"><a name="b842352706182952"></a><a name="b842352706182952"></a>SYS</strong>: indicates a system disk.</li></ul>
    </td>
    </tr>
    <tr id="row49633994175534"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p60930547175534"><a name="p60930547175534"></a><a name="p60930547175534"></a>dedicated_storage_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p36427236175534"><a name="p36427236175534"></a><a name="p36427236175534"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p64924998175534"><a name="p64924998175534"></a><a name="p64924998175534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p24433472175534"><a name="p24433472175534"></a><a name="p24433472175534"></a>Specifies a DSS device ID for creating an ECS disk.</p>
    <div class="note" id="note5234646218286"><a name="note5234646218286"></a><a name="note5234646218286"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p135611818286"><a name="p135611818286"></a><a name="p135611818286"></a>Specify DSS devices for all disks in an AS configuration or not. If DSS devices are specified, all the data stores must belong to the same AZ, and the disk types supported by a DSS device for a disk must be the same as the <strong id="b842352706162857"><a name="b842352706162857"></a><a name="b842352706162857"></a>volume_type</strong> value.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row58688944175538"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p56184018175538"><a name="p56184018175538"></a><a name="p56184018175538"></a>data_disk_image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p54611596175538"><a name="p54611596175538"></a><a name="p54611596175538"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p61463175175538"><a name="p61463175175538"></a><a name="p61463175175538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p88867165126"><a name="p88867165126"></a><a name="p88867165126"></a>Specifies the ID of a data disk image used to export data disks of an ECS.</p>
    </td>
    </tr>
    <tr id="row3824652814281"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p1096104114281"><a name="p1096104114281"></a><a name="p1096104114281"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p1542916014281"><a name="p1542916014281"></a><a name="p1542916014281"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p4180241014281"><a name="p4180241014281"></a><a name="p4180241014281"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p3055206514281"><a name="p3055206514281"></a><a name="p3055206514281"></a>Specifies the disk backup snapshot ID for restoring the system disk and data disks using a full-ECS backup when a full-ECS image is used.</p>
    <div class="note" id="note829347714332"><a name="note829347714332"></a><a name="note829347714332"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p753243314332"><a name="p753243314332"></a><a name="p753243314332"></a>Each disk in an AS configuration must correspond to a disk backup in the full-ECS backup by <strong id="b13727599185528"><a name="b13727599185528"></a><a name="b13727599185528"></a>snapshot_id</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1774725017296"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p12748155016294"><a name="p12748155016294"></a><a name="p12748155016294"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p64975104309"><a name="p64975104309"></a><a name="p64975104309"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p197488507290"><a name="p197488507290"></a><a name="p197488507290"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p6748135052911"><a name="p6748135052911"></a><a name="p6748135052911"></a>Specifies the metadata for creating disks. For details, see <a href="#table24491331595">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **metadata**  Field Description for Creating Disks

    <a name="table24491331595"></a>
    <table><thead align="left"><tr id="row64501831795"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p445012311913"><a name="p445012311913"></a><a name="p445012311913"></a><strong id="b1928321516472"><a name="b1928321516472"></a><a name="b1928321516472"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p7450431292"><a name="p7450431292"></a><a name="p7450431292"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p164501831490"><a name="p164501831490"></a><a name="p164501831490"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p164505318913"><a name="p164505318913"></a><a name="p164505318913"></a><strong id="b90161613473"><a name="b90161613473"></a><a name="b90161613473"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row104511531798"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p84519311991"><a name="p84519311991"></a><a name="p84519311991"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p945123112920"><a name="p945123112920"></a><a name="p945123112920"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1545163119918"><a name="p1545163119918"></a><a name="p1545163119918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p134511731497"><a name="p134511731497"></a><a name="p134511731497"></a>Specifies encryption in <strong id="b022414329338"><a name="b022414329338"></a><a name="b022414329338"></a>metadata</strong>. The value can be <strong id="b1122512327339"><a name="b1122512327339"></a><a name="b1122512327339"></a>0</strong> (encryption disabled) or <strong id="b1722533219332"><a name="b1722533219332"></a><a name="b1722533219332"></a>1</strong> (encryption enabled).</p>
    <p id="p194512312091"><a name="p194512312091"></a><a name="p194512312091"></a>If this parameter does not exist, the disk will not be encrypted by default.</p>
    </td>
    </tr>
    <tr id="row104521331796"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p345233110911"><a name="p345233110911"></a><a name="p345233110911"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p164526314915"><a name="p164526314915"></a><a name="p164526314915"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1545219314916"><a name="p1545219314916"></a><a name="p1545219314916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p445210311990"><a name="p445210311990"></a><a name="p445210311990"></a>Specifies the CMK ID, which indicates encryption in <strong id="b133078414409"><a name="b133078414409"></a><a name="b133078414409"></a>metadata</strong>. This parameter is used with <strong id="b5308184144018"><a name="b5308184144018"></a><a name="b5308184144018"></a>__system__encrypted</strong>.</p>
    <div class="note" id="note19452031492"><a name="note19452031492"></a><a name="note19452031492"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1645283120918"><a name="p1645283120918"></a><a name="p1645283120918"></a>For details about how to obtain the CMK ID, see "Querying the List of CMKs" in <em id="i107281545193411"><a name="i107281545193411"></a><a name="i107281545193411"></a>Key Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **personality**  field description

    <a name="table3396587291242"></a>
    <table><thead align="left"><tr id="r6a6a3c4936384d2eb9ba188a74782106"><th class="cellrowborder" valign="top" width="20.588235294117645%" id="mcps1.2.5.1.1"><p id="ae52b461d7be445538179892250c454d3"><a name="ae52b461d7be445538179892250c454d3"></a><a name="ae52b461d7be445538179892250c454d3"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.568627450980394%" id="mcps1.2.5.1.2"><p id="p5313561291856"><a name="p5313561291856"></a><a name="p5313561291856"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.686274509803921%" id="mcps1.2.5.1.3"><p id="a705bd328b65e40609a925747b9b9ca19"><a name="a705bd328b65e40609a925747b9b9ca19"></a><a name="a705bd328b65e40609a925747b9b9ca19"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.15686274509804%" id="mcps1.2.5.1.4"><p id="ab09337e1921045d0b2301b9433de15a4"><a name="ab09337e1921045d0b2301b9433de15a4"></a><a name="ab09337e1921045d0b2301b9433de15a4"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r1cc46c416c9344afb67c18b2db04eb1e"><td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.1 "><p id="ab1fd3be8a3b14d9b928d9be020d9cce1"><a name="ab1fd3be8a3b14d9b928d9be020d9cce1"></a><a name="ab1fd3be8a3b14d9b928d9be020d9cce1"></a>path</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.568627450980394%" headers="mcps1.2.5.1.2 "><p id="p901735291856"><a name="p901735291856"></a><a name="p901735291856"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.5.1.3 "><p id="a1fd06f02d7fa4bb78375adaac8c7c83a"><a name="a1fd06f02d7fa4bb78375adaac8c7c83a"></a><a name="a1fd06f02d7fa4bb78375adaac8c7c83a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.15686274509804%" headers="mcps1.2.5.1.4 "><p id="af9b3fb4e3d3646689b1a9eaa9272e59f"><a name="af9b3fb4e3d3646689b1a9eaa9272e59f"></a><a name="af9b3fb4e3d3646689b1a9eaa9272e59f"></a>Specifies the path of the injected file.</p>
    <a name="ul174946235321"></a><a name="ul174946235321"></a><ul id="ul174946235321"><li>For Linux OSs, specify the path, for example, <strong id="b881049913163448"><a name="b881049913163448"></a><a name="b881049913163448"></a>/etc/foo.txt</strong>, for storing the injected file.</li><li>For Windows, the injected file is automatically stored in the root directory of drive C. You only need to specify the file name, for example, <strong id="b19455189172515"><a name="b19455189172515"></a><a name="b19455189172515"></a>foo</strong>. The file name contains only letters and digits.</li></ul>
    </td>
    </tr>
    <tr id="r65c4416353bf4344af2fe51be83fdf9b"><td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.1 "><p id="a23bd88691709477a978e415c1a0fe6da"><a name="a23bd88691709477a978e415c1a0fe6da"></a><a name="a23bd88691709477a978e415c1a0fe6da"></a>content</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.568627450980394%" headers="mcps1.2.5.1.2 "><p id="p5931687991856"><a name="p5931687991856"></a><a name="p5931687991856"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.5.1.3 "><p id="ac90e2333d4f0408ab96039ff47c0b6cd"><a name="ac90e2333d4f0408ab96039ff47c0b6cd"></a><a name="ac90e2333d4f0408ab96039ff47c0b6cd"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.15686274509804%" headers="mcps1.2.5.1.4 "><p id="aaa250f7a45114ceaa046e414c3e414aa"><a name="aaa250f7a45114ceaa046e414c3e414aa"></a><a name="aaa250f7a45114ceaa046e414c3e414aa"></a>Specifies the content of the injected file.</p>
    <p id="p19417814183420"><a name="p19417814183420"></a><a name="p19417814183420"></a>The value must be the information after the content of the injected file is encoded using Base64.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **public\_ip**  field description

    <a name="table105840310312"></a>
    <table><thead align="left"><tr id="row2228809910312"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p6050559410312"><a name="p6050559410312"></a><a name="p6050559410312"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p200607310312"><a name="p200607310312"></a><a name="p200607310312"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p2827424910312"><a name="p2827424910312"></a><a name="p2827424910312"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p851285010312"><a name="p851285010312"></a><a name="p851285010312"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1845221910312"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p1823473210312"><a name="p1823473210312"></a><a name="p1823473210312"></a>eip</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p61831810312"><a name="p61831810312"></a><a name="p61831810312"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p260112527395"><a name="p260112527395"></a><a name="p260112527395"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p3025472310312"><a name="p3025472310312"></a><a name="p3025472310312"></a>Specifies the EIP automatically assigned to the ECS. For details, see <a href="#table35964662103154">Table 8</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** **eip**  field description

    <a name="table35964662103154"></a>
    <table><thead align="left"><tr id="row62589803103154"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p36609296103154"><a name="p36609296103154"></a><a name="p36609296103154"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p12562985103154"><a name="p12562985103154"></a><a name="p12562985103154"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p10968863103154"><a name="p10968863103154"></a><a name="p10968863103154"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p16062681103154"><a name="p16062681103154"></a><a name="p16062681103154"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26008767103154"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p26335419103154"><a name="p26335419103154"></a><a name="p26335419103154"></a>ip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p52794162103154"><a name="p52794162103154"></a><a name="p52794162103154"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p48468750103154"><a name="p48468750103154"></a><a name="p48468750103154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p11217393102451"><a name="p11217393102451"></a><a name="p11217393102451"></a>Specifies the EIP type.</p>
    <p id="p1468485318810"><a name="p1468485318810"></a><a name="p1468485318810"></a>Enumerated value of the IP address type: 5_bgp (indicates dynamic BGP)</p>
    </td>
    </tr>
    <tr id="row5044530610333"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p5953796110333"><a name="p5953796110333"></a><a name="p5953796110333"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p5784552510333"><a name="p5784552510333"></a><a name="p5784552510333"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p5497590910333"><a name="p5497590910333"></a><a name="p5497590910333"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p2386361710333"><a name="p2386361710333"></a><a name="p2386361710333"></a>Specifies the bandwidth of an IP address. For details, see <a href="#table18754238103344">Table 9</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9** **bandwidth**  field description

    <a name="table18754238103344"></a>
    <table><thead align="left"><tr id="row11404567103344"><th class="cellrowborder" valign="top" width="20.588235294117645%" id="mcps1.2.5.1.1"><p id="p51354766103344"><a name="p51354766103344"></a><a name="p51354766103344"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.588235294117645%" id="mcps1.2.5.1.2"><p id="p66095344103344"><a name="p66095344103344"></a><a name="p66095344103344"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.666666666666668%" id="mcps1.2.5.1.3"><p id="p52122663103344"><a name="p52122663103344"></a><a name="p52122663103344"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.15686274509804%" id="mcps1.2.5.1.4"><p id="p61186203103344"><a name="p61186203103344"></a><a name="p61186203103344"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57135411103344"><td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.1 "><p id="p64565592103344"><a name="p64565592103344"></a><a name="p64565592103344"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.2 "><p id="p16576173511573"><a name="p16576173511573"></a><a name="p16576173511573"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.3 "><p id="p23701607103344"><a name="p23701607103344"></a><a name="p23701607103344"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.15686274509804%" headers="mcps1.2.5.1.4 "><p id="p28107425418"><a name="p28107425418"></a><a name="p28107425418"></a>Specifies the bandwidth (Mbit/s). The value range is <strong id="b842352706143022"><a name="b842352706143022"></a><a name="b842352706143022"></a>1</strong> to <strong id="b842352706143025"><a name="b842352706143025"></a><a name="b842352706143025"></a>500</strong>.</p>
    <div class="note" id="note193569549262"><a name="note193569549262"></a><a name="note193569549262"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul889214120276"></a><a name="ul889214120276"></a><ul id="ul889214120276"><li>The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.</li><li>The minimum unit for bandwidth varies depending on the bandwidth range.<a name="ul62431057184317"></a><a name="ul62431057184317"></a><ul id="ul62431057184317"><li>The minimum unit is 1 Mbit/s if the allowed bandwidth size ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).</li><li>The minimum unit is 50 Mbit/s if the allowed bandwidth size ranges 300 Mbit/s to 500 Mbit/s (with 500 Mbit/s included).</li></ul>
    </li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row31493547103344"><td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.1 "><p id="p840519103344"><a name="p840519103344"></a><a name="p840519103344"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.2 "><p id="p973211103344"><a name="p973211103344"></a><a name="p973211103344"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.3 "><p id="p11721296103344"><a name="p11721296103344"></a><a name="p11721296103344"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.15686274509804%" headers="mcps1.2.5.1.4 "><p id="p44928433102758"><a name="p44928433102758"></a><a name="p44928433102758"></a>Specifies the bandwidth sharing type.</p>
    <p id="p737015157592"><a name="p737015157592"></a><a name="p737015157592"></a>Enumerated values of the sharing type:</p>
    <a name="ul2738203453114"></a><a name="ul2738203453114"></a><ul id="ul2738203453114"><li><strong id="b842352706183913"><a name="b842352706183913"></a><a name="b842352706183913"></a>PER</strong>: dedicated</li></ul>
    <p id="p62203121153252"><a name="p62203121153252"></a><a name="p62203121153252"></a>Only dedicated bandwidth is available.</p>
    </td>
    </tr>
    <tr id="row46301101103436"><td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.1 "><p id="p59401706103436"><a name="p59401706103436"></a><a name="p59401706103436"></a>charging_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.2 "><p id="p198831642801"><a name="p198831642801"></a><a name="p198831642801"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.3 "><p id="p33424546103436"><a name="p33424546103436"></a><a name="p33424546103436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.15686274509804%" headers="mcps1.2.5.1.4 "><p id="p11173478141019"><a name="p11173478141019"></a><a name="p11173478141019"></a>Specifies the bandwidth billing mode.</p>
    <p id="p19258123004916"><a name="p19258123004916"></a><a name="p19258123004916"></a><strong id="b842352706184041"><a name="b842352706184041"></a><a name="b842352706184041"></a>traffic</strong>: billed by traffic.</p>
    <p id="p672818222397"><a name="p672818222397"></a><a name="p672818222397"></a>If the parameter value is out of the preceding options, creating the ECS will fail.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10** **metadata**  field description

    <a name="table6119722495435"></a>
    <table><thead align="left"><tr id="row5794517795435"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p6304778595435"><a name="p6304778595435"></a><a name="p6304778595435"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.2"><p id="p659697895435"><a name="p659697895435"></a><a name="p659697895435"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="p6459317995435"><a name="p6459317995435"></a><a name="p6459317995435"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.5.1.4"><p id="p6466497295435"><a name="p6466497295435"></a><a name="p6466497295435"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row337137495435"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p460751359557"><a name="p460751359557"></a><a name="p460751359557"></a>User-defined field key pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p410984619557"><a name="p410984619557"></a><a name="p410984619557"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p406410849557"><a name="p406410849557"></a><a name="p406410849557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.5.1.4 "><p id="p226413089557"><a name="p226413089557"></a><a name="p226413089557"></a>The total length of the user-defined data cannot be longer than 512 bytes. The user-defined key cannot be empty, contain periods (.), or start with symbol dollar ($).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  11** **security\_groups**  field description

    <a name="table144645712211"></a>
    <table><thead align="left"><tr id="row9451145752211"><th class="cellrowborder" valign="top" width="21.568627450980394%" id="mcps1.2.5.1.1"><p id="p98056272236"><a name="p98056272236"></a><a name="p98056272236"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.607843137254903%" id="mcps1.2.5.1.2"><p id="p48061927162310"><a name="p48061927162310"></a><a name="p48061927162310"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.666666666666668%" id="mcps1.2.5.1.3"><p id="p1080610274234"><a name="p1080610274234"></a><a name="p1080610274234"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.15686274509804%" id="mcps1.2.5.1.4"><p id="p280619278231"><a name="p280619278231"></a><a name="p280619278231"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12454155742210"><td class="cellrowborder" valign="top" width="21.568627450980394%" headers="mcps1.2.5.1.1 "><p id="p8806202702310"><a name="p8806202702310"></a><a name="p8806202702310"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.2 "><p id="p118065277232"><a name="p118065277232"></a><a name="p118065277232"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.3 "><p id="p12806132742318"><a name="p12806132742318"></a><a name="p12806132742318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.15686274509804%" headers="mcps1.2.5.1.4 "><p id="p180615275233"><a name="p180615275233"></a><a name="p180615275233"></a>Specifies the ID of the security group.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to create an AS configuration with name  **as-config-tlzp**, image ID  **627a1223-2ca3-46a7-8d5f-7aef22c74ee6**, flavor ID  **s3.xlarge.4**, 40 GB SATA system disk, and SSH key name  **100vm\_key**.

    ```
    POST https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_configuration
    
    { 
        "scaling_configuration_name": "as-config-tlzq", 
        "instance_config": { 
            "flavorRef": "s3.xlarge.4", 
            "imageRef": "627a1223-2ca3-46a7-8d5f-7aef22c74ee6", 
            "disk": [ 
                { 
                    "size": 40, 
                    "volume_type": "SATA", 
                    "disk_type": "SYS" 
                } 
            ], 
            "key_name": "100vm_key" ,
    	"security_groups": [{
    		"id": "6c22a6c0-b5d2-4a84-ac56-51090dcc33be"
    	}], 
            "multi_flavor_priority_policy": "PICK_FIRST"
        } 
    }
    ```


## Response Message<a name="section15686020"></a>

-   Response parameters

    **Table  12**  Response parameters

    <a name="table39717481"></a>
    <table><thead align="left"><tr id="row15677883"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.1"><p id="p61948991"><a name="p61948991"></a><a name="p61948991"></a><strong id="b1212643914012"><a name="b1212643914012"></a><a name="b1212643914012"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p51812368"><a name="p51812368"></a><a name="p51812368"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49%" id="mcps1.2.4.1.3"><p id="p36052245"><a name="p36052245"></a><a name="p36052245"></a><strong id="b17344194114015"><a name="b17344194114015"></a><a name="b17344194114015"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34550710"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.1 "><p id="p47144157"><a name="p47144157"></a><a name="p47144157"></a>scaling_configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p60580335"><a name="p60580335"></a><a name="p60580335"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.4.1.3 "><p id="p8060118"><a name="p8060118"></a><a name="p8060118"></a>Specifies the AS configuration ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "scaling_configuration_id": "f8327883-6a07-4497-9a61-68c03e8e72a2"
    }
    ```


## Returned Values<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="table3454809"></a>
    <table><thead align="left"><tr id="row59223347"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p32361769"><a name="p32361769"></a><a name="p32361769"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p4057632"><a name="p4057632"></a><a name="p4057632"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60232767"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p47015983"><a name="p47015983"></a><a name="p47015983"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p50198296"><a name="p50198296"></a><a name="p50198296"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row49131481"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p20226985"><a name="p20226985"></a><a name="p20226985"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p27773061"><a name="p27773061"></a><a name="p27773061"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row48630964"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p46793998"><a name="p46793998"></a><a name="p46793998"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p32217513"><a name="p32217513"></a><a name="p32217513"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row21522166"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p65573909"><a name="p65573909"></a><a name="p65573909"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p9886408"><a name="p9886408"></a><a name="p9886408"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row21868813"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p26543418"><a name="p26543418"></a><a name="p26543418"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p2533231"><a name="p2533231"></a><a name="p2533231"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row22799085"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p34786562"><a name="p34786562"></a><a name="p34786562"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p66248115"><a name="p66248115"></a><a name="p66248115"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row59362130"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p43603258"><a name="p43603258"></a><a name="p43603258"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p42202994"><a name="p42202994"></a><a name="p42202994"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p30123063"><a name="p30123063"></a><a name="p30123063"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p24049039"><a name="p24049039"></a><a name="p24049039"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row15114764"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p16336406"><a name="p16336406"></a><a name="p16336406"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p48180537"><a name="p48180537"></a><a name="p48180537"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row30971651"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p25675773"><a name="p25675773"></a><a name="p25675773"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p66471715"><a name="p66471715"></a><a name="p66471715"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row61374531"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p5281111"><a name="p5281111"></a><a name="p5281111"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p25116876"><a name="p25116876"></a><a name="p25116876"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row24725298"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p56592155"><a name="p56592155"></a><a name="p56592155"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p20561848"><a name="p20561848"></a><a name="p20561848"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row50838910"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p24311045"><a name="p24311045"></a><a name="p24311045"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p23037620"><a name="p23037620"></a><a name="p23037620"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row6011995"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p17209562"><a name="p17209562"></a><a name="p17209562"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p51797270"><a name="p51797270"></a><a name="p51797270"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

