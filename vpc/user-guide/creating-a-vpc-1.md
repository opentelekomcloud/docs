# Creating a VPC<a name="en-us_topic_0030971614"></a>

## Scenarios<a name="en-us_topic_0013935842_s128d115360ea47fdb6bcf5e34f3bb4b3"></a>

A VPC provides an isolated virtual network for ECSs. You can configure and manage the network as required.

Create a VPC by following the procedure provided in this section. Then, create subnets, security groups, and VPN connections, and assign EIPs by following the procedures provided in subsequent sections.

## Procedure<a name="en-us_topic_0013935842_sce05194b892247b48bcfab89b255ba06"></a>

1.  Log in to the management console.
2.  Click  ![](figures/en-us_image_0118621993.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  On the  **Dashboard**  page, click  **Create VPC**.

    On the  **Create VPC**  page, set parameters as prompted.

    **Table  1**  Parameter description

    <a name="en-us_topic_0013935842_t4b265b130ad647a4bb2ccc949e6e5c17"></a><table><thead align="left"><tr id="en-us_topic_0013935842_r3852cd8ee6434d38b38d52e3caf730ac"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013935842_a712562f4dca94d67a7b485a2f0990046"><a name="en-us_topic_0013935842_a712562f4dca94d67a7b485a2f0990046"></a><a name="en-us_topic_0013935842_a712562f4dca94d67a7b485a2f0990046"></a><strong id="en-us_topic_0013935842_b842352706114331"><a name="en-us_topic_0013935842_b842352706114331"></a><a name="en-us_topic_0013935842_b842352706114331"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.7%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013935842_a05d3c4cb3b6242959d06d1ae46fe59ff"><a name="en-us_topic_0013935842_a05d3c4cb3b6242959d06d1ae46fe59ff"></a><a name="en-us_topic_0013935842_a05d3c4cb3b6242959d06d1ae46fe59ff"></a><strong id="en-us_topic_0013935842_b84235270694155"><a name="en-us_topic_0013935842_b84235270694155"></a><a name="en-us_topic_0013935842_b84235270694155"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013935842_a334713b697df49e8bf28724b18374d1a"><a name="en-us_topic_0013935842_a334713b697df49e8bf28724b18374d1a"></a><a name="en-us_topic_0013935842_a334713b697df49e8bf28724b18374d1a"></a><strong id="en-us_topic_0013935842_b8423527069420"><a name="en-us_topic_0013935842_b8423527069420"></a><a name="en-us_topic_0013935842_b8423527069420"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013935842_r518cf8dd41de44a498ab2c7faea57c5e"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_ac07253cbefab4f28b573582c5df73b6c"><a name="en-us_topic_0013935842_ac07253cbefab4f28b573582c5df73b6c"></a><a name="en-us_topic_0013935842_ac07253cbefab4f28b573582c5df73b6c"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013935842_a71842be6e0fa41ec8eff21c2bf7da148"><a name="en-us_topic_0013935842_a71842be6e0fa41ec8eff21c2bf7da148"></a><a name="en-us_topic_0013935842_a71842be6e0fa41ec8eff21c2bf7da148"></a>Specifies the VPC name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_ade4c6eb82c3b4fd59952a9a12bd64755"><a name="en-us_topic_0013935842_ade4c6eb82c3b4fd59952a9a12bd64755"></a><a name="en-us_topic_0013935842_ade4c6eb82c3b4fd59952a9a12bd64755"></a>VPC-001</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_ra094e5e271ca4e239db7f60801bfb261"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_ab4d1e405752145149496774a07280521"><a name="en-us_topic_0013935842_ab4d1e405752145149496774a07280521"></a><a name="en-us_topic_0013935842_ab4d1e405752145149496774a07280521"></a>CIDR Block</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013935842_ab6f5bf1788124fba8321b0fde60f607c"><a name="en-us_topic_0013935842_ab6f5bf1788124fba8321b0fde60f607c"></a><a name="en-us_topic_0013935842_ab6f5bf1788124fba8321b0fde60f607c"></a>Specifies the Classless Inter-Domain Routing (CIDR) block for the VPC. The CIDR block of a subnet can be the same as the CIDR block for the VPC (for a single subnet in the VPC) or a subset (for multiple subnets in the VPC).</p>
    <p id="en-us_topic_0013935842_a1bfd255e57704e3c84c6e7bd4a50a2c2"><a name="en-us_topic_0013935842_a1bfd255e57704e3c84c6e7bd4a50a2c2"></a><a name="en-us_topic_0013935842_a1bfd255e57704e3c84c6e7bd4a50a2c2"></a>The following CIDR blocks are supported:</p>
    <p id="en-us_topic_0013935842_a0e9c8076c50446588ea6d2b17747fad6"><a name="en-us_topic_0013935842_a0e9c8076c50446588ea6d2b17747fad6"></a><a name="en-us_topic_0013935842_a0e9c8076c50446588ea6d2b17747fad6"></a>10.0.0.0 – 10.255.255.255</p>
    <p id="en-us_topic_0013935842_en-us_topic_0029397258_p842614151525"><a name="en-us_topic_0013935842_en-us_topic_0029397258_p842614151525"></a><a name="en-us_topic_0013935842_en-us_topic_0029397258_p842614151525"></a>172.16.0.0 – 172.31.255.255 </p>
    <p id="en-us_topic_0013935842_a62ec04bda46d4c01b538ed16bb84c143"><a name="en-us_topic_0013935842_a62ec04bda46d4c01b538ed16bb84c143"></a><a name="en-us_topic_0013935842_a62ec04bda46d4c01b538ed16bb84c143"></a>192.168.0.0 – 192.168.255.255</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_afb56019a902c47daacf0bfd0d032e2df"><a name="en-us_topic_0013935842_afb56019a902c47daacf0bfd0d032e2df"></a><a name="en-us_topic_0013935842_afb56019a902c47daacf0bfd0d032e2df"></a>192.168.0.0/16</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row19661509211138"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_p42735861211138"><a name="en-us_topic_0013935842_p42735861211138"></a><a name="en-us_topic_0013935842_p42735861211138"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013935842_p20140951169"><a name="en-us_topic_0013935842_p20140951169"></a><a name="en-us_topic_0013935842_p20140951169"></a>Specifies the VPC tag, which consists of a key and value pair. You can add a maximum of ten tags to each VPC.</p>
    <p id="en-us_topic_0013935842_p39052702211138"><a name="en-us_topic_0013935842_p39052702211138"></a><a name="en-us_topic_0013935842_p39052702211138"></a>The tag key and value must meet the requirements listed in <a href="#en-us_topic_0030971614__en-us_topic_0013935842_table248245914136">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0013935842_ul122375031712"></a><a name="en-us_topic_0013935842_ul122375031712"></a><ul id="en-us_topic_0013935842_ul122375031712"><li id="en-us_topic_0013935842_li122310507178"><a name="en-us_topic_0013935842_li122310507178"></a><a name="en-us_topic_0013935842_li122310507178"></a>Key: vpc_key1</li><li id="en-us_topic_0013935842_li1723185013177"><a name="en-us_topic_0013935842_li1723185013177"></a><a name="en-us_topic_0013935842_li1723185013177"></a>Value: vpc-01</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_ra369fc73b0af47dd936ccb992e105d17"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_a7663eb0092ab40d7b5dad2da753da036"><a name="en-us_topic_0013935842_a7663eb0092ab40d7b5dad2da753da036"></a><a name="en-us_topic_0013935842_a7663eb0092ab40d7b5dad2da753da036"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013935842_a966b39e120f74ff88516671a500eef21"><a name="en-us_topic_0013935842_a966b39e120f74ff88516671a500eef21"></a><a name="en-us_topic_0013935842_a966b39e120f74ff88516671a500eef21"></a>Specifies the subnet name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_a91b3835692264c65b21b20ce1b9b6b82"><a name="en-us_topic_0013935842_a91b3835692264c65b21b20ce1b9b6b82"></a><a name="en-us_topic_0013935842_a91b3835692264c65b21b20ce1b9b6b82"></a>Subnet-001</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_ra58e3348c9b0473f8d1008b1f90fa1a5"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_a4b9dcc0b33d24bf3b4fae63b1ff99778"><a name="en-us_topic_0013935842_a4b9dcc0b33d24bf3b4fae63b1ff99778"></a><a name="en-us_topic_0013935842_a4b9dcc0b33d24bf3b4fae63b1ff99778"></a>CIDR</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013935842_a1733b4c364fb4b7ebce489630fdd406c"><a name="en-us_topic_0013935842_a1733b4c364fb4b7ebce489630fdd406c"></a><a name="en-us_topic_0013935842_a1733b4c364fb4b7ebce489630fdd406c"></a>Specifies the CIDR block for the subnet. This value must be within the VPC CIDR range.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_a44db5eac56ab42919cea401c205b8d14"><a name="en-us_topic_0013935842_a44db5eac56ab42919cea401c205b8d14"></a><a name="en-us_topic_0013935842_a44db5eac56ab42919cea401c205b8d14"></a>192.168.0.0/24</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_r36f642e39f8943a7a346b7958b28d683"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_a71fa49631e9f4d6dbb12b2f7d87f1eaa"><a name="en-us_topic_0013935842_a71fa49631e9f4d6dbb12b2f7d87f1eaa"></a><a name="en-us_topic_0013935842_a71fa49631e9f4d6dbb12b2f7d87f1eaa"></a>Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013935842_a8d71ad506da04fdba94ab81296fe77ba"><a name="en-us_topic_0013935842_a8d71ad506da04fdba94ab81296fe77ba"></a><a name="en-us_topic_0013935842_a8d71ad506da04fdba94ab81296fe77ba"></a>Specifies the gateway address of the subnet.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_ab64cf588db2042789ae49b92016ffa0a"><a name="en-us_topic_0013935842_ab64cf588db2042789ae49b92016ffa0a"></a><a name="en-us_topic_0013935842_ab64cf588db2042789ae49b92016ffa0a"></a>192.168.0.1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_row18881023161617"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_p8883223101614"><a name="en-us_topic_0013935842_p8883223101614"></a><a name="en-us_topic_0013935842_p8883223101614"></a>Subnet Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0013935842_p1210183691618"><a name="en-us_topic_0013935842_p1210183691618"></a><a name="en-us_topic_0013935842_p1210183691618"></a>Specifies the subnet tag, which consists of a key and value pair. You can add a maximum of ten tags to each subnet.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0013935842_ul19794197131810"></a><a name="en-us_topic_0013935842_ul19794197131810"></a><ul id="en-us_topic_0013935842_ul19794197131810"><li id="en-us_topic_0013935842_li12794137191810"><a name="en-us_topic_0013935842_li12794137191810"></a><a name="en-us_topic_0013935842_li12794137191810"></a>Key: subnet_key1</li><li id="en-us_topic_0013935842_li137943741816"><a name="en-us_topic_0013935842_li137943741816"></a><a name="en-us_topic_0013935842_li137943741816"></a>Value: subnet-01</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  VPC tag key and value requirements

    <a name="en-us_topic_0013935842_table248245914136"></a><table><thead align="left"><tr id="en-us_topic_0013935842_en-us_topic_0067805752_r8f725dd873f74d5689a397a96364525f"><th class="cellrowborder" valign="top" width="17.71%" id="mcps1.2.4.1.1"><p id="en-us_topic_0013935842_en-us_topic_0067805752_ae7200181216040679ba0b08613e317f0"><a name="en-us_topic_0013935842_en-us_topic_0067805752_ae7200181216040679ba0b08613e317f0"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_ae7200181216040679ba0b08613e317f0"></a><strong id="en-us_topic_0013935842_en-us_topic_0067805752_b84235270618434"><a name="en-us_topic_0013935842_en-us_topic_0067805752_b84235270618434"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_b84235270618434"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65.29%" id="mcps1.2.4.1.2"><p id="en-us_topic_0013935842_en-us_topic_0067805752_a30f1778a977845c0a6948f77fd9efada"><a name="en-us_topic_0013935842_en-us_topic_0067805752_a30f1778a977845c0a6948f77fd9efada"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_a30f1778a977845c0a6948f77fd9efada"></a><strong id="en-us_topic_0013935842_en-us_topic_0067805752_b842352706174218"><a name="en-us_topic_0013935842_en-us_topic_0067805752_b842352706174218"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_b842352706174218"></a>Requirements</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.3"><p id="en-us_topic_0013935842_en-us_topic_0067805752_a34827669831a48ec96262bfcabc61519"><a name="en-us_topic_0013935842_en-us_topic_0067805752_a34827669831a48ec96262bfcabc61519"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_a34827669831a48ec96262bfcabc61519"></a><strong id="en-us_topic_0013935842_en-us_topic_0067805752_b842352706174227"><a name="en-us_topic_0013935842_en-us_topic_0067805752_b842352706174227"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_b842352706174227"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0013935842_en-us_topic_0067805752_ra6c6dfb7a5c344f1af2c7664d34e7d80"><td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_en-us_topic_0067805752_a45a01bdce58d410d8ee06b6f374e401b"><a name="en-us_topic_0013935842_en-us_topic_0067805752_a45a01bdce58d410d8ee06b6f374e401b"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_a45a01bdce58d410d8ee06b6f374e401b"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013935842_en-us_topic_0067805752_ub2cf5f68e02742d49e3f8d80289eab77"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_ub2cf5f68e02742d49e3f8d80289eab77"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_ub2cf5f68e02742d49e3f8d80289eab77"><li id="en-us_topic_0013935842_en-us_topic_0067805752_l69b087a6e844481d84cf8668fe7ef490"><a name="en-us_topic_0013935842_en-us_topic_0067805752_l69b087a6e844481d84cf8668fe7ef490"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_l69b087a6e844481d84cf8668fe7ef490"></a>Cannot be left blank.</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_l1c4fa8e37999443a95189f79a4f5336a"><a name="en-us_topic_0013935842_en-us_topic_0067805752_l1c4fa8e37999443a95189f79a4f5336a"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_l1c4fa8e37999443a95189f79a4f5336a"></a>Must be unique for the same VPC and can be the same for different VPCs.</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_l1e143053ab1847cb8781edb26e58e787"><a name="en-us_topic_0013935842_en-us_topic_0067805752_l1e143053ab1847cb8781edb26e58e787"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_l1e143053ab1847cb8781edb26e58e787"></a>Can contain a maximum of 36 characters.</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_lb10c975c495c4de1bc52fc96d084697c"><a name="en-us_topic_0013935842_en-us_topic_0067805752_lb10c975c495c4de1bc52fc96d084697c"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_lb10c975c495c4de1bc52fc96d084697c"></a>Can contain only the following character types:<a name="en-us_topic_0013935842_en-us_topic_0067805752_uccb317c6616b4445aa84b125e5aa017f"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_uccb317c6616b4445aa84b125e5aa017f"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_uccb317c6616b4445aa84b125e5aa017f"><li id="en-us_topic_0013935842_en-us_topic_0067805752_la4975a0b714d486381ef36c8599a4dae"><a name="en-us_topic_0013935842_en-us_topic_0067805752_la4975a0b714d486381ef36c8599a4dae"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_la4975a0b714d486381ef36c8599a4dae"></a>Uppercase letters</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_l05872030add74e7ab50152845826fa0a"><a name="en-us_topic_0013935842_en-us_topic_0067805752_l05872030add74e7ab50152845826fa0a"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_l05872030add74e7ab50152845826fa0a"></a>Lowercase letters</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_le70c062519174a9cae474c99c0f4f976"><a name="en-us_topic_0013935842_en-us_topic_0067805752_le70c062519174a9cae474c99c0f4f976"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_le70c062519174a9cae474c99c0f4f976"></a>Digits</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_li77869551443"><a name="en-us_topic_0013935842_en-us_topic_0067805752_li77869551443"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_li77869551443"></a>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_en-us_topic_0067805752_a735c9e74ec274598ac7051f7d65e7bce"><a name="en-us_topic_0013935842_en-us_topic_0067805752_a735c9e74ec274598ac7051f7d65e7bce"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_a735c9e74ec274598ac7051f7d65e7bce"></a>vpc_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0013935842_en-us_topic_0067805752_rcabbd61ffcd048ec8408a15332fde94d"><td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0013935842_en-us_topic_0067805752_a5f7f1bb378214abcaf0c661567a47535"><a name="en-us_topic_0013935842_en-us_topic_0067805752_a5f7f1bb378214abcaf0c661567a47535"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_a5f7f1bb378214abcaf0c661567a47535"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0013935842_en-us_topic_0067805752_u463eb9034f3d456b81073b15ba62f102"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_u463eb9034f3d456b81073b15ba62f102"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_u463eb9034f3d456b81073b15ba62f102"><li id="en-us_topic_0013935842_en-us_topic_0067805752_l4128d1ac8ff244d19539bdca4eedf161"><a name="en-us_topic_0013935842_en-us_topic_0067805752_l4128d1ac8ff244d19539bdca4eedf161"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_l4128d1ac8ff244d19539bdca4eedf161"></a>Can contain a maximum of 43 characters.</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_lf4772afe9a8143b086ea935ee84656f3"><a name="en-us_topic_0013935842_en-us_topic_0067805752_lf4772afe9a8143b086ea935ee84656f3"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_lf4772afe9a8143b086ea935ee84656f3"></a>Can contain only the following character types:<a name="en-us_topic_0013935842_en-us_topic_0067805752_ub74c759faad544c3b4428accc9c42b80"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_ub74c759faad544c3b4428accc9c42b80"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_ub74c759faad544c3b4428accc9c42b80"><li id="en-us_topic_0013935842_en-us_topic_0067805752_lf275cde186b24b9a9e3d4d52784a16ba"><a name="en-us_topic_0013935842_en-us_topic_0067805752_lf275cde186b24b9a9e3d4d52784a16ba"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_lf275cde186b24b9a9e3d4d52784a16ba"></a>Uppercase letters</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_l3a58e993d925444bb0eba6c38feeedfb"><a name="en-us_topic_0013935842_en-us_topic_0067805752_l3a58e993d925444bb0eba6c38feeedfb"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_l3a58e993d925444bb0eba6c38feeedfb"></a>Lowercase letters</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_l8679b69b2cd9428caecf8e14cafe5d4f"><a name="en-us_topic_0013935842_en-us_topic_0067805752_l8679b69b2cd9428caecf8e14cafe5d4f"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_l8679b69b2cd9428caecf8e14cafe5d4f"></a>Digits</li><li id="en-us_topic_0013935842_en-us_topic_0067805752_li13827436174517"><a name="en-us_topic_0013935842_en-us_topic_0067805752_li13827436174517"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_li13827436174517"></a>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0013935842_en-us_topic_0067805752_a3ac5d865f6a848458eb5fae95f81fee0"><a name="en-us_topic_0013935842_en-us_topic_0067805752_a3ac5d865f6a848458eb5fae95f81fee0"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_a3ac5d865f6a848458eb5fae95f81fee0"></a>vpc-01</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  The external DNS server address is used by default. If you need to change the DNS server address, select  **Custom**  for  **Advanced Settings**  and configure the DNS server addresses. You must ensure that the configured DNS server addresses are available.
6.  Click  **Create Now**.

