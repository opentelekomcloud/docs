# Copying Jobs<a name="EN-US_TOPIC_0125375460"></a>

This section describes how to replicate MRS jobs.

## Background<a name="section757713132145"></a>

Currently, all types of jobs except for Spark SQL and Distcp jobs can be replicated.

## Procedure<a name="section5720065913226"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  Click  **Jobs**.
5.  In the  **Operation** column corresponding to the to-be-replicated job, choose **More \> Copy**.

    The  **Copy Job**  dialog box is displayed.

6.  Set job parameters, and click  **OK**.

    [Table 1](#table11042081442)  describes job configuration information.

    After being successfully submitted, a job changes to the  **Running**  state by default. You do not need to manually execute the job.

    **Table  1**  Job configuration information

    <a name="table11042081442"></a>
    <table><thead align="left"><tr id="reee2bf14c87b49d59a1e28f686c63781"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="a4334da7627fe4a65b213372a62785d64"><a name="a4334da7627fe4a65b213372a62785d64"></a><a name="a4334da7627fe4a65b213372a62785d64"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="ac065ca5cdff34b00915899a878d83c98"><a name="ac065ca5cdff34b00915899a878d83c98"></a><a name="ac065ca5cdff34b00915899a878d83c98"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rfac5bced682f4cbabeb6e5ad247c54c8"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="ab4bb5c9dc62a426e82f17a9106595c03"><a name="ab4bb5c9dc62a426e82f17a9106595c03"></a><a name="ab4bb5c9dc62a426e82f17a9106595c03"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a068a11d08a0a47e1887a0554a877b3d9"><a name="a068a11d08a0a47e1887a0554a877b3d9"></a><a name="a068a11d08a0a47e1887a0554a877b3d9"></a>Job type</p>
    <p id="aa6f1ee86fc34472983458a8710bfbc1e"><a name="aa6f1ee86fc34472983458a8710bfbc1e"></a><a name="aa6f1ee86fc34472983458a8710bfbc1e"></a>Possible types include:</p>
    <a name="uc5d8f46ff1364b27802c5c314f5c3cf0"></a><a name="uc5d8f46ff1364b27802c5c314f5c3cf0"></a><ul id="uc5d8f46ff1364b27802c5c314f5c3cf0"><li>MapReduce</li><li>Spark</li><li>Spark Script</li><li>Hive Script</li></ul>
    <div class="note" id="n478e3ddb2e2f4da58f43cb127939e44a"><a name="n478e3ddb2e2f4da58f43cb127939e44a"></a><a name="n478e3ddb2e2f4da58f43cb127939e44a"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a571682f2baeb491f87cf7c0b45e8cba2"><a name="a571682f2baeb491f87cf7c0b45e8cba2"></a><a name="a571682f2baeb491f87cf7c0b45e8cba2"></a>To add jobs of the Spark and Hive types, you need to select Spark and Hive components when creating a cluster and the cluster <span id="p5516cccbe32e4056be704d480cd48336"><a name="p5516cccbe32e4056be704d480cd48336"></a><a name="p5516cccbe32e4056be704d480cd48336"></a>must be in the running state</span>. Spark Script jobs support Spark SQL only, and Spark supports Spark Core and Spark SQL.</p>
    </div></div>
    </td>
    </tr>
    <tr id="refbfee24384349d587e01ffe8f4a9bf0"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="ac5e94e37a47b40638becc58c9bbc0038"><a name="ac5e94e37a47b40638becc58c9bbc0038"></a><a name="ac5e94e37a47b40638becc58c9bbc0038"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="abd753118528e4bae90071ac366292b32"><a name="abd753118528e4bae90071ac366292b32"></a><a name="abd753118528e4bae90071ac366292b32"></a>Job name</p>
    <p id="a60857bdc2df642b8b8a784bf9fbcc6ad"><a name="a60857bdc2df642b8b8a784bf9fbcc6ad"></a><a name="a60857bdc2df642b8b8a784bf9fbcc6ad"></a>This parameter consists of 1 to 64 characters, including letters, digits, hyphens (-), or underscores (_). It cannot be null.</p>
    <div class="note" id="ncada14c7cdf54a1ea777bb04115c03d5"><a name="ncada14c7cdf54a1ea777bb04115c03d5"></a><a name="ncada14c7cdf54a1ea777bb04115c03d5"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a266763530cee44efa275e3eb5d3b41ce"><a name="a266763530cee44efa275e3eb5d3b41ce"></a><a name="a266763530cee44efa275e3eb5d3b41ce"></a>Identical job names are allowed but not recommended.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r12b89f8121a84bfcaf9939f13235b567"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a6e1044718f454048a297560cd911b05b"><a name="a6e1044718f454048a297560cd911b05b"></a><a name="a6e1044718f454048a297560cd911b05b"></a>Program Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="ae09d7e2c59ec459eb4f05061327a2725"><a name="ae09d7e2c59ec459eb4f05061327a2725"></a><a name="ae09d7e2c59ec459eb4f05061327a2725"></a>Address of the JAR file of the program for executing jobs</p>
    <div class="note" id="n3885d524bbb94c54bf9a407e82c4aa43"><a name="n3885d524bbb94c54bf9a407e82c4aa43"></a><a name="n3885d524bbb94c54bf9a407e82c4aa43"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a96878fc0f1bd4eada1c938cbb95b03f2"><a name="a96878fc0f1bd4eada1c938cbb95b03f2"></a><a name="a96878fc0f1bd4eada1c938cbb95b03f2"></a>When configuring this parameter, click <strong id="a0e574fd5eda544d68de0fc6a1569140b"><a name="a0e574fd5eda544d68de0fc6a1569140b"></a><a name="a0e574fd5eda544d68de0fc6a1569140b"></a>OBS</strong>&nbsp;or&nbsp;<strong id="a6c20fd6f18f74a008a3d3b4d46e23a28"><a name="a6c20fd6f18f74a008a3d3b4d46e23a28"></a><a name="a6c20fd6f18f74a008a3d3b4d46e23a28"></a>HDFS</strong>, specify the file path, and click&nbsp;<strong id="a47f7856853144b04aa058fd9754ed48e"><a name="a47f7856853144b04aa058fd9754ed48e"></a><a name="a47f7856853144b04aa058fd9754ed48e"></a>OK</strong>.</p>
    </div></div>
    <p id="a60f1d69876464ba2a5544aad7a7d7794"><a name="a60f1d69876464ba2a5544aad7a7d7794"></a><a name="a60f1d69876464ba2a5544aad7a7d7794"></a>This parameter cannot be null.</p>
    <p id="ab46664edc96f4611a8ddb7721b036914"><a name="ab46664edc96f4611a8ddb7721b036914"></a><a name="ab46664edc96f4611a8ddb7721b036914"></a>This parameter must meet the following requirements:</p>
    <a name="ue350679412b241039115eeb8e97d74e3"></a><a name="ue350679412b241039115eeb8e97d74e3"></a><ul id="ue350679412b241039115eeb8e97d74e3"><li>A maximum of 1023 characters are allowed, but special characters (<span id="p5e76477760284feebd1450f0c13331dd"><a name="p5e76477760284feebd1450f0c13331dd"></a><a name="p5e76477760284feebd1450f0c13331dd"></a>*?&lt;"&gt;|\</span>) are not allowed. The address cannot be empty or full of spaces.</li><li>The path varies depending on the file system:<a name="u130ee8bc0100454f8f9a9db7818c7987"></a><a name="u130ee8bc0100454f8f9a9db7818c7987"></a><ul id="u130ee8bc0100454f8f9a9db7818c7987"><li>OBS: The path must start with <span class="parmvalue" id="p115c2677ca5841e893a935012be1e899"><a name="p115c2677ca5841e893a935012be1e899"></a><a name="p115c2677ca5841e893a935012be1e899"></a><b>s3a://</b></span>,&nbsp;for example,&nbsp;<strong id="a8aaaa8120b9a403390142f210cf72919"><a name="a8aaaa8120b9a403390142f210cf72919"></a><a name="a8aaaa8120b9a403390142f210cf72919"></a>s3a://wordcount/program/hadoop-mapreduce-examples-2.7.x.jar</strong>.</li><li>HDFS: The path must start with <span class="parmvalue" id="pd7b50972532446c989f0909671924b67"><a name="pd7b50972532446c989f0909671924b67"></a><a name="pd7b50972532446c989f0909671924b67"></a><b>/user</b></span>.</li></ul>
    </li><li><span>Spark Script must end with </span><span class="parmvalue" id="pbafed4b352b840c0a8c65a4d5e3f8deb"><a name="pbafed4b352b840c0a8c65a4d5e3f8deb"></a><a name="pbafed4b352b840c0a8c65a4d5e3f8deb"></a><b>.sql</b></span><span>; MapReduce and Spark&nbsp;must end with&nbsp;</span><span class="parmvalue" id="p9a0e75771a554fe7a59e25640b532a1e"><a name="p9a0e75771a554fe7a59e25640b532a1e"></a><a name="p9a0e75771a554fe7a59e25640b532a1e"></a><b>.jar</b></span><span id="p84f18f8af94b4dcab304768ab338759d"><a name="p84f18f8af94b4dcab304768ab338759d"></a><a name="p84f18f8af94b4dcab304768ab338759d"></a>.</span><span>&nbsp;</span><strong id="a72afe1e49acf4222825dd20925d1bc91"><a name="a72afe1e49acf4222825dd20925d1bc91"></a><a name="a72afe1e49acf4222825dd20925d1bc91"></a>sql</strong><span>&nbsp;and&nbsp;</span><strong id="a2b820959b2aa4c8b8144e97cc71f216c"><a name="a2b820959b2aa4c8b8144e97cc71f216c"></a><a name="a2b820959b2aa4c8b8144e97cc71f216c"></a>jar</strong><span> are case-insensitive.</span></li></ul>
    </td>
    </tr>
    <tr id="rfb022e27827d4b2ea6cc512692b43321"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a369cd2540a9c4b3a9f065196f68c597a"><a name="a369cd2540a9c4b3a9f065196f68c597a"></a><a name="a369cd2540a9c4b3a9f065196f68c597a"></a>Parameter</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a07e9488946c74c95ae68b9454e92102a"><a name="a07e9488946c74c95ae68b9454e92102a"></a><a name="a07e9488946c74c95ae68b9454e92102a"></a>Key parameter for executing jobs</p>
    <p id="afb8efb8324ee4bdea0b2045f6cbbd00a"><a name="afb8efb8324ee4bdea0b2045f6cbbd00a"></a><a name="afb8efb8324ee4bdea0b2045f6cbbd00a"></a>This parameter is assigned by an internal function. MRS is only responsible for inputting the parameter. Separate parameters with spaces.</p>
    <p id="aaac65d870b7a4c7db59abf887ecc6fb7"><a name="aaac65d870b7a4c7db59abf887ecc6fb7"></a><a name="aaac65d870b7a4c7db59abf887ecc6fb7"></a>Format: <em id="a35c4340c40684b13a90dc92ed9ca9434"><a name="a35c4340c40684b13a90dc92ed9ca9434"></a><a name="a35c4340c40684b13a90dc92ed9ca9434"></a>package name</em>.<em id="a9e8b7c4e84f644cab1f42cd46f525034"><a name="a9e8b7c4e84f644cab1f42cd46f525034"></a><a name="a9e8b7c4e84f644cab1f42cd46f525034"></a>class name</em></p>
    <p id="aa0b27cda390641b493db8bd628a3aa56"><a name="aa0b27cda390641b493db8bd628a3aa56"></a><a name="aa0b27cda390641b493db8bd628a3aa56"></a>A maximum of 2047 characters are allowed, but special characters (;|&amp;&gt;',&lt;$) are not allowed. This parameter can be empty.</p>
    <div class="note" id="n3cd805f63e294e58bbcaf4656767901a"><a name="n3cd805f63e294e58bbcaf4656767901a"></a><a name="n3cd805f63e294e58bbcaf4656767901a"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ad17761d83ab34a3dbb995c79e4477cd9"><a name="ad17761d83ab34a3dbb995c79e4477cd9"></a><a name="ad17761d83ab34a3dbb995c79e4477cd9"></a>When you enter parameters containing sensitive information, for example, a password for login, you can add an at sign (@) before the parameters to encrypt the parameter values and prevent persistence of sensitive information in the form of plaintext. Therefore, when you view job information on the MRS management console, sensitive information will be displayed as asterisks (*).</p>
    <p id="a15a40889f12842899e6b75f3a8491e57"><a name="a15a40889f12842899e6b75f3a8491e57"></a><a name="a15a40889f12842899e6b75f3a8491e57"></a>Example: username=admin @password=admin_123</p>
    </div></div>
    </td>
    </tr>
    <tr id="rc43b8e4a509345cab4f6deaabd22193d"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="af024bfe1076d43a5aa47af87ef30a995"><a name="af024bfe1076d43a5aa47af87ef30a995"></a><a name="af024bfe1076d43a5aa47af87ef30a995"></a>Import from</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a174d68350c7a4808b8205f6bb48b68ad"><a name="a174d68350c7a4808b8205f6bb48b68ad"></a><a name="a174d68350c7a4808b8205f6bb48b68ad"></a>Address for inputting data</p>
    <div class="note" id="nb428bfb7e86941469cc089578e1644bd"><a name="nb428bfb7e86941469cc089578e1644bd"></a><a name="nb428bfb7e86941469cc089578e1644bd"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a911a64c61c55472e887ae1b7b8165983"><a name="a911a64c61c55472e887ae1b7b8165983"></a><a name="a911a64c61c55472e887ae1b7b8165983"></a>When configuring this parameter, click <strong id="a71dbe3b49eef41f1b37806e1772dcd8f"><a name="a71dbe3b49eef41f1b37806e1772dcd8f"></a><a name="a71dbe3b49eef41f1b37806e1772dcd8f"></a>OBS</strong>&nbsp;or&nbsp;<strong id="en-us_topic_0012808240_b749588714107"><a name="en-us_topic_0012808240_b749588714107"></a><a name="en-us_topic_0012808240_b749588714107"></a>HDFS</strong>, specify the file path, and click&nbsp;<strong id="ad72c3bf0c52141fb883809576dc9ba4c"><a name="ad72c3bf0c52141fb883809576dc9ba4c"></a><a name="ad72c3bf0c52141fb883809576dc9ba4c"></a>OK</strong>.</p>
    </div></div>
    <div class="p" id="a5dba8f40eea740cabfb0aa70b76feb38"><a name="a5dba8f40eea740cabfb0aa70b76feb38"></a><a name="a5dba8f40eea740cabfb0aa70b76feb38"></a>The path varies depending on the file system:<a name="ubb899d66fa14460fb93b6e0529b51f12"></a><a name="ubb899d66fa14460fb93b6e0529b51f12"></a><ul id="ubb899d66fa14460fb93b6e0529b51f12"><li>OBS: The path must start with <span class="parmvalue" id="p9005c623835c4ad6b17aab8f25115e84"><a name="p9005c623835c4ad6b17aab8f25115e84"></a><a name="p9005c623835c4ad6b17aab8f25115e84"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="p251f9c6949374abd91d88cd4195c49cd"><a name="p251f9c6949374abd91d88cd4195c49cd"></a><a name="p251f9c6949374abd91d88cd4195c49cd"></a><b>/user</b></span>.</li></ul>
    </div>
    <p id="ac2c6aa3521694d95b67435709ca3cadb"><a name="ac2c6aa3521694d95b67435709ca3cadb"></a><a name="ac2c6aa3521694d95b67435709ca3cadb"></a>A maximum of 1023 characters are allowed, but special characters (<span id="p8703db70f0ce43a492c60d2ebb2c2d31"><a name="p8703db70f0ce43a492c60d2ebb2c2d31"></a><a name="p8703db70f0ce43a492c60d2ebb2c2d31"></a>*?&lt;"&gt;|\</span>) are not allowed. This parameter can be empty.</p>
    </td>
    </tr>
    <tr id="ra2413bc54794419e8cfbd71aee1c3e1a"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a9317910079a244cd90d8d01d3372a3e6"><a name="a9317910079a244cd90d8d01d3372a3e6"></a><a name="a9317910079a244cd90d8d01d3372a3e6"></a>Export to</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a86d55879a80a406386776f77b823a9dd"><a name="a86d55879a80a406386776f77b823a9dd"></a><a name="a86d55879a80a406386776f77b823a9dd"></a>Address for outputting data</p>
    <div class="note" id="n8c7470fcd2074eddb47e934096c08fb4"><a name="n8c7470fcd2074eddb47e934096c08fb4"></a><a name="n8c7470fcd2074eddb47e934096c08fb4"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a5872dc60d0a74eaea705554375446b52"><a name="a5872dc60d0a74eaea705554375446b52"></a><a name="a5872dc60d0a74eaea705554375446b52"></a>When configuring this parameter, click <strong id="a96c25c9462784e64b4a6744d517d3501"><a name="a96c25c9462784e64b4a6744d517d3501"></a><a name="a96c25c9462784e64b4a6744d517d3501"></a>OBS</strong>&nbsp;or&nbsp;<strong id="a7b1b3ef92dd241e7be7c6a6eba385a93"><a name="a7b1b3ef92dd241e7be7c6a6eba385a93"></a><a name="a7b1b3ef92dd241e7be7c6a6eba385a93"></a>HDFS</strong>, specify the file path, and click&nbsp;<strong id="a1255b938bb2047e2afd7957376f1cd26"><a name="a1255b938bb2047e2afd7957376f1cd26"></a><a name="a1255b938bb2047e2afd7957376f1cd26"></a>OK</strong>.</p>
    </div></div>
    <div class="p" id="a8b79bfcf42444328a41695442102714a"><a name="a8b79bfcf42444328a41695442102714a"></a><a name="a8b79bfcf42444328a41695442102714a"></a>The path varies depending on the file system:<a name="ue044b547c51b48fb93c6e5d8705e5471"></a><a name="ue044b547c51b48fb93c6e5d8705e5471"></a><ul id="ue044b547c51b48fb93c6e5d8705e5471"><li>OBS: The path must start with <span class="parmvalue" id="pc1750d33446e491b9000b00e7b1f66fe"><a name="pc1750d33446e491b9000b00e7b1f66fe"></a><a name="pc1750d33446e491b9000b00e7b1f66fe"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="p4dcc3fbc89c84a4287343d09f70eb112"><a name="p4dcc3fbc89c84a4287343d09f70eb112"></a><a name="p4dcc3fbc89c84a4287343d09f70eb112"></a><b>/user</b></span>.</li></ul>
    </div>
    <p id="aeb464c60f5f5462b95aa82870fd73baa"><a name="aeb464c60f5f5462b95aa82870fd73baa"></a><a name="aeb464c60f5f5462b95aa82870fd73baa"></a>A maximum of 1023 characters are allowed, but special characters (<span id="p2e46d25d69a0471287716ebcd288d7e5"><a name="p2e46d25d69a0471287716ebcd288d7e5"></a><a name="p2e46d25d69a0471287716ebcd288d7e5"></a>*?&lt;"&gt;|\</span>) are not allowed. This parameter can be empty.</p>
    </td>
    </tr>
    <tr id="r18bee9be1b28462889e2f7cd897665f6"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a188eada0a50c471fb1ff0a6c48313130"><a name="a188eada0a50c471fb1ff0a6c48313130"></a><a name="a188eada0a50c471fb1ff0a6c48313130"></a>Log path</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0012808240_p438042811381"><a name="en-us_topic_0012808240_p438042811381"></a><a name="en-us_topic_0012808240_p438042811381"></a>Address for storing job logs that record job running status</p>
    <div class="note" id="n1d5510678cc542de800ca4c983745d82"><a name="n1d5510678cc542de800ca4c983745d82"></a><a name="n1d5510678cc542de800ca4c983745d82"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a953180ca8618472688d6f4369d831d1d"><a name="a953180ca8618472688d6f4369d831d1d"></a><a name="a953180ca8618472688d6f4369d831d1d"></a>When configuring this parameter, click <strong id="a757c65ddbdf6451298a3deb315ec4b5c"><a name="a757c65ddbdf6451298a3deb315ec4b5c"></a><a name="a757c65ddbdf6451298a3deb315ec4b5c"></a>OBS</strong>&nbsp;or&nbsp;<strong id="en-us_topic_0012808240_b512490141029"><a name="en-us_topic_0012808240_b512490141029"></a><a name="en-us_topic_0012808240_b512490141029"></a>HDFS</strong>, specify the file path, and click&nbsp;<strong id="aca2c26d651084cc0bb27cde1e343747f"><a name="aca2c26d651084cc0bb27cde1e343747f"></a><a name="aca2c26d651084cc0bb27cde1e343747f"></a>OK</strong>.</p>
    </div></div>
    <div class="p" id="a0f64aee84e6f4cf98b083dc5589d0c64"><a name="a0f64aee84e6f4cf98b083dc5589d0c64"></a><a name="a0f64aee84e6f4cf98b083dc5589d0c64"></a>The path varies depending on the file system:<a name="u6129ba3a21314a6bb56652839e3507cb"></a><a name="u6129ba3a21314a6bb56652839e3507cb"></a><ul id="u6129ba3a21314a6bb56652839e3507cb"><li>OBS: The path must start with <span class="parmvalue" id="p8657a730ca414cf18535b976d6075d16"><a name="p8657a730ca414cf18535b976d6075d16"></a><a name="p8657a730ca414cf18535b976d6075d16"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="p5209b256eb9d459a881b638f5dc71bca"><a name="p5209b256eb9d459a881b638f5dc71bca"></a><a name="p5209b256eb9d459a881b638f5dc71bca"></a><b>/user</b></span>.</li></ul>
    </div>
    <p id="aa3268c276b8340499e618df309b23a94"><a name="aa3268c276b8340499e618df309b23a94"></a><a name="aa3268c276b8340499e618df309b23a94"></a>A maximum of 1023 characters are allowed, but special characters (<span id="pfa6d01029b4a472ba150cd31ef562e05"><a name="pfa6d01029b4a472ba150cd31ef562e05"></a><a name="pfa6d01029b4a472ba150cd31ef562e05"></a>*?&lt;"&gt;|\</span>) are not allowed. This parameter can be empty.</p>
    </td>
    </tr>
    </tbody>
    </table>


