# Creating a Job<a name="EN-US_TOPIC_0125375669"></a>

You can submit developed programs to MRS, execute them, and obtain the execution result on the  **Job Management**  page in an analysis cluster with Kerberos authentication disabled.

## Prerequisites<a name="sb2eb76a9f2e34218a5cebb25821aee87"></a>

Before creating jobs, upload the local data to OBS for computing and analysis. MRS allows data to be exported from OBS to HDFS for computing and analysis. After the analysis and computing are complete, you can either store the data in HDFS or export it to OBS. HDFS and OBS can store compressed data in the format of bz2 or gz.

## Procedure<a name="s9fd52b50176c4cdb8be9442ebf5ffad3"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/wwx437827-中软基础平台部-datasight-image-bbfbe22f-2a2d-4e1b-8f10-a7782fd1d3ed.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Cluster**  \>  **Active Cluster**, select a cluster, and click its name to switch to the cluster details page.
4.  Click  **Job Management** and go to the **Job Management**  tab page.
5.  On the  **Jobs** tab page, click **Create** and go to the **Create Job**  page.

    [Table 1](#t41b1b4e7de204ba0a0573de7c9b1a22f)  describes job configuration information.  

    **Table  1**  Job configuration information

    <a name="t41b1b4e7de204ba0a0573de7c9b1a22f"></a>
    <table><thead align="left"><tr id="reee2bf14c87b49d59a1e28f686c63781"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="a4334da7627fe4a65b213372a62785d64"><a name="a4334da7627fe4a65b213372a62785d64"></a><a name="a4334da7627fe4a65b213372a62785d64"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="ac065ca5cdff34b00915899a878d83c98"><a name="ac065ca5cdff34b00915899a878d83c98"></a><a name="ac065ca5cdff34b00915899a878d83c98"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rfac5bced682f4cbabeb6e5ad247c54c8"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="ab4bb5c9dc62a426e82f17a9106595c03"><a name="ab4bb5c9dc62a426e82f17a9106595c03"></a><a name="ab4bb5c9dc62a426e82f17a9106595c03"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a5e589553134f41239f9d6cea303b1766"><a name="a5e589553134f41239f9d6cea303b1766"></a><a name="a5e589553134f41239f9d6cea303b1766"></a>Job type</p>
    <p id="p8745144184211"><a name="p8745144184211"></a><a name="p8745144184211"></a>Possible types include:</p>
    <a name="ud5ecb924fe8f4f4c90cf4ad44a7c76a6"></a><a name="ud5ecb924fe8f4f4c90cf4ad44a7c76a6"></a><ul id="ud5ecb924fe8f4f4c90cf4ad44a7c76a6"><li>MapReduce</li><li>Spark</li><li>Spark Script</li><li>Hive Script<div class="note" id="n53c0bc27177d43d3870170c1bf70b44d"><a name="n53c0bc27177d43d3870170c1bf70b44d"></a><a name="n53c0bc27177d43d3870170c1bf70b44d"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ab2e889f445e245faad96ec346a558952"><a name="ab2e889f445e245faad96ec346a558952"></a><a name="ab2e889f445e245faad96ec346a558952"></a>To add jobs of the Spark and Hive types, you need to select Spark and Hive components when creating a cluster and the cluster must be in the running state. Spark Script jobs support Spark SQL only, and Spark supports Spark Core and Spark SQL.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="refbfee24384349d587e01ffe8f4a9bf0"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="ac5e94e37a47b40638becc58c9bbc0038"><a name="ac5e94e37a47b40638becc58c9bbc0038"></a><a name="ac5e94e37a47b40638becc58c9bbc0038"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p56747809184242"><a name="p56747809184242"></a><a name="p56747809184242"></a>Job name</p>
    <p id="a60857bdc2df642b8b8a784bf9fbcc6ad"><a name="a60857bdc2df642b8b8a784bf9fbcc6ad"></a><a name="a60857bdc2df642b8b8a784bf9fbcc6ad"></a>This parameter consists of 1 to 64 characters, including letters, digits, hyphens (-), or underscores (_). It cannot be null.</p>
    <div class="note" id="ncada14c7cdf54a1ea777bb04115c03d5"><a name="ncada14c7cdf54a1ea777bb04115c03d5"></a><a name="ncada14c7cdf54a1ea777bb04115c03d5"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a266763530cee44efa275e3eb5d3b41ce"><a name="a266763530cee44efa275e3eb5d3b41ce"></a><a name="a266763530cee44efa275e3eb5d3b41ce"></a>Identical job names are allowed but not recommended.</p>
    </div></div>
    </td>
    </tr>
    <tr id="r12b89f8121a84bfcaf9939f13235b567"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a6e1044718f454048a297560cd911b05b"><a name="a6e1044718f454048a297560cd911b05b"></a><a name="a6e1044718f454048a297560cd911b05b"></a>Program Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0012808240_p655627719565"><a name="zh-cn_topic_0012808240_p655627719565"></a><a name="zh-cn_topic_0012808240_p655627719565"></a>Address of the JAR file of the program for executing jobs</p>
    <div class="note" id="note15626919144040"><a name="note15626919144040"></a><a name="note15626919144040"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p54260708144042"><a name="p54260708144042"></a><a name="p54260708144042"></a>When configuring this parameter, click <span class="uicontrol" id="uicontrol36255677184339"><a name="uicontrol36255677184339"></a><a name="uicontrol36255677184339"></a><b>OBS</b></span>&nbsp;or&nbsp;<span class="uicontrol" id="uicontrol62915606184343"><a name="uicontrol62915606184343"></a><a name="uicontrol62915606184343"></a><b>HDFS</b></span>, specify the file path, and click&nbsp;<span class="uicontrol" id="uicontrol2353869218444"><a name="uicontrol2353869218444"></a><a name="uicontrol2353869218444"></a><b>OK</b></span>.</p>
    </div></div>
    <p id="p43404015161033"><a name="p43404015161033"></a><a name="p43404015161033"></a>This parameter cannot be null.</p>
    <p id="p52747342161040"><a name="p52747342161040"></a><a name="p52747342161040"></a>This parameter must meet the following requirements:</p>
    <a name="u42400e6ea82e41eeb54149ec6aaed27a"></a><a name="u42400e6ea82e41eeb54149ec6aaed27a"></a><ul id="u42400e6ea82e41eeb54149ec6aaed27a"><li>A maximum of 1023 characters are allowed, but special characters (*?&lt;"&gt;|\) are not allowed. The address cannot be empty or full of spaces.</li><li>The path varies depending on the file system:<a name="zh-cn_topic_0012808240_ul56833471484"></a><a name="zh-cn_topic_0012808240_ul56833471484"></a><ul id="zh-cn_topic_0012808240_ul56833471484"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue48783559103035"><a name="parmvalue48783559103035"></a><a name="parmvalue48783559103035"></a><b>s3a://</b></span>, for example,&nbsp;<span class="parmvalue" id="parmvalue9052323184456"><a name="parmvalue9052323184456"></a><a name="parmvalue9052323184456"></a><b>s3a://wordcount/program/hadoop-mapreduce-examples-2.7.x.jar</b></span>.</li><li>HDFS: The path start<span id="ph10557540101248"><a name="ph10557540101248"></a><a name="ph10557540101248"></a>s</span>&nbsp;with&nbsp;<span class="parmvalue" id="parmvalue61413448184512"><a name="parmvalue61413448184512"></a><a name="parmvalue61413448184512"></a><b>/user</b></span> by default.</li></ul>
    </li><li>Spark Script must end with <span class="parmvalue" id="parmvalue20489296184735"><a name="parmvalue20489296184735"></a><a name="parmvalue20489296184735"></a><b>.sql</b></span>; MapReduce and Spark must end with&nbsp;<span class="parmvalue" id="parmvalue45886169184745"><a name="parmvalue45886169184745"></a><a name="parmvalue45886169184745"></a><b>.jar</b></span>.&nbsp;<span class="parmvalue" id="parmvalue5728906518481"><a name="parmvalue5728906518481"></a><a name="parmvalue5728906518481"></a><b>sql</b></span>,&nbsp;<span class="parmvalue" id="parmvalue5098841918485"><a name="parmvalue5098841918485"></a><a name="parmvalue5098841918485"></a><b>jar</b></span> are case-insensitive.</li></ul>
    </td>
    </tr>
    <tr id="rfb022e27827d4b2ea6cc512692b43321"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a369cd2540a9c4b3a9f065196f68c597a"><a name="a369cd2540a9c4b3a9f065196f68c597a"></a><a name="a369cd2540a9c4b3a9f065196f68c597a"></a>Parameter</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p42315513113559"><a name="p42315513113559"></a><a name="p42315513113559"></a>Key parameter for executing jobs</p>
    <p id="afdce421fc89e42fa97c6fd6f84d7041a"><a name="afdce421fc89e42fa97c6fd6f84d7041a"></a><a name="afdce421fc89e42fa97c6fd6f84d7041a"></a>This parameter is assigned by an internal function. MRS is only responsible for inputting the parameter. Separate parameters with spaces.</p>
    <p id="p6925711151153"><a name="p6925711151153"></a><a name="p6925711151153"></a>Format: <em id="i5620649718302"><a name="i5620649718302"></a><a name="i5620649718302"></a>package name</em>.<em id="i3192458818307"><a name="i3192458818307"></a><a name="i3192458818307"></a>class name</em></p>
    <p id="a3d7fad576c944080ac7c6e7f5249d76c"><a name="a3d7fad576c944080ac7c6e7f5249d76c"></a><a name="a3d7fad576c944080ac7c6e7f5249d76c"></a>A maximum of 2047 characters are allowed, but special characters (;|&amp;&gt;',&lt;$) are not allowed. This parameter can be empty.</p>
    <div class="note" id="note62371709174814"><a name="note62371709174814"></a><a name="note62371709174814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1818632720364"><a name="p1818632720364"></a><a name="p1818632720364"></a>When you enter parameters containing sensitive information, for example, a password for login, you can add an at sign (@) before the parameters to encrypt the parameter values and prevent persistence of sensitive information in the form of plaintext. Therefore, when you view job information on the MRS management console, sensitive information will be displayed as asterisks (*).</p>
    <p id="p31871527123616"><a name="p31871527123616"></a><a name="p31871527123616"></a>Example: username=admin @password=admin_123</p>
    </div></div>
    </td>
    </tr>
    <tr id="rc43b8e4a509345cab4f6deaabd22193d"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="af024bfe1076d43a5aa47af87ef30a995"><a name="af024bfe1076d43a5aa47af87ef30a995"></a><a name="af024bfe1076d43a5aa47af87ef30a995"></a>Import from</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a38dd85fb389b45ca82b8fc61cf15cf4d"><a name="a38dd85fb389b45ca82b8fc61cf15cf4d"></a><a name="a38dd85fb389b45ca82b8fc61cf15cf4d"></a>Address for inputting data</p>
    <div class="note" id="note20812668184528"><a name="note20812668184528"></a><a name="note20812668184528"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p53096288184528"><a name="p53096288184528"></a><a name="p53096288184528"></a>When configuring this parameter, click <span class="uicontrol" id="uicontrol8104552184528"><a name="uicontrol8104552184528"></a><a name="uicontrol8104552184528"></a><b>OBS</b></span>&nbsp;or&nbsp;<span class="uicontrol" id="uicontrol5832108184528"><a name="uicontrol5832108184528"></a><a name="uicontrol5832108184528"></a><b>HDFS</b></span>, specify the file path, and click&nbsp;<span class="uicontrol" id="uicontrol52488972184528"><a name="uicontrol52488972184528"></a><a name="uicontrol52488972184528"></a><b>OK</b></span>.</p>
    </div></div>
    <div class="p" id="af31ec6a2c4f84d50866030025cb33237"><a name="af31ec6a2c4f84d50866030025cb33237"></a><a name="af31ec6a2c4f84d50866030025cb33237"></a>The path varies depending on the file system:<a name="u59527a44d328453b935e0f630d3344b6"></a><a name="u59527a44d328453b935e0f630d3344b6"></a><ul id="u59527a44d328453b935e0f630d3344b6"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue2852075103051"><a name="parmvalue2852075103051"></a><a name="parmvalue2852075103051"></a><b>s3a://</b></span>.</li><li>HDFS: The path start<span id="ph1110160101322"><a name="ph1110160101322"></a><a name="ph1110160101322"></a>s</span>&nbsp;with&nbsp;<span class="parmvalue" id="parmvalue33130420184842"><a name="parmvalue33130420184842"></a><a name="parmvalue33130420184842"></a><b>/user</b></span> by default.</li></ul>
    </div>
    <p id="ac2c6aa3521694d95b67435709ca3cadb"><a name="ac2c6aa3521694d95b67435709ca3cadb"></a><a name="ac2c6aa3521694d95b67435709ca3cadb"></a>A maximum of 1023 characters are allowed, but special characters (/:*?"&lt;&gt;|\;&amp;,'`!{}[]$) are not allowed. This parameter can be empty.</p>
    </td>
    </tr>
    <tr id="ra2413bc54794419e8cfbd71aee1c3e1a"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a9317910079a244cd90d8d01d3372a3e6"><a name="a9317910079a244cd90d8d01d3372a3e6"></a><a name="a9317910079a244cd90d8d01d3372a3e6"></a>Export to</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="af5c36a51bdbe4051be008b1daef194b1"><a name="af5c36a51bdbe4051be008b1daef194b1"></a><a name="af5c36a51bdbe4051be008b1daef194b1"></a>Address for outputting data</p>
    <div class="note" id="note24071774185059"><a name="note24071774185059"></a><a name="note24071774185059"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p15319375185059"><a name="p15319375185059"></a><a name="p15319375185059"></a>When configuring this parameter, click <span class="uicontrol" id="uicontrol3656652185059"><a name="uicontrol3656652185059"></a><a name="uicontrol3656652185059"></a><b>OBS</b></span>&nbsp;or&nbsp;<span class="uicontrol" id="uicontrol32909868185059"><a name="uicontrol32909868185059"></a><a name="uicontrol32909868185059"></a><b>HDFS</b></span>, specify the file path, and click&nbsp;<span class="uicontrol" id="uicontrol27753362185059"><a name="uicontrol27753362185059"></a><a name="uicontrol27753362185059"></a><b>OK</b></span>.</p>
    </div></div>
    <div class="p" id="p5554430185132"><a name="p5554430185132"></a><a name="p5554430185132"></a>The path varies depending on the file system:<a name="ul49989877185132"></a><a name="ul49989877185132"></a><ul id="ul49989877185132"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue3956493010312"><a name="parmvalue3956493010312"></a><a name="parmvalue3956493010312"></a><b>s3a://</b></span>.</li><li>HDFS: The path start<span id="ph22704655101342"><a name="ph22704655101342"></a><a name="ph22704655101342"></a>s</span>&nbsp;with&nbsp;<span class="parmvalue" id="parmvalue22565872185132"><a name="parmvalue22565872185132"></a><a name="parmvalue22565872185132"></a><b>/user</b></span> by default.</li></ul>
    </div>
    <p id="p1766256185132"><a name="p1766256185132"></a><a name="p1766256185132"></a>A maximum of 1023 characters are allowed, but special characters (/:*?"&lt;&gt;|\;&amp;,'`!{}[]$) are not allowed. This parameter can be empty.</p>
    </td>
    </tr>
    <tr id="r18bee9be1b28462889e2f7cd897665f6"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a188eada0a50c471fb1ff0a6c48313130"><a name="a188eada0a50c471fb1ff0a6c48313130"></a><a name="a188eada0a50c471fb1ff0a6c48313130"></a>Log path</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a75fcb83ea61f45329f91dca890696234"><a name="a75fcb83ea61f45329f91dca890696234"></a><a name="a75fcb83ea61f45329f91dca890696234"></a>Address for storing job logs that record job running status</p>
    <div class="note" id="note3323391118513"><a name="note3323391118513"></a><a name="note3323391118513"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3066974818513"><a name="p3066974818513"></a><a name="p3066974818513"></a>When configuring this parameter, click <span class="uicontrol" id="uicontrol759227918513"><a name="uicontrol759227918513"></a><a name="uicontrol759227918513"></a><b>OBS</b></span>&nbsp;or&nbsp;<span class="uicontrol" id="uicontrol122164918513"><a name="uicontrol122164918513"></a><a name="uicontrol122164918513"></a><b>HDFS</b></span>, specify the file path, and click&nbsp;<span class="uicontrol" id="uicontrol1099484318513"><a name="uicontrol1099484318513"></a><a name="uicontrol1099484318513"></a><b>OK</b></span>.</p>
    </div></div>
    <p id="a4498f0b3c3fd41859e03587692fcd539"><a name="a4498f0b3c3fd41859e03587692fcd539"></a><a name="a4498f0b3c3fd41859e03587692fcd539"></a>The path varies depending on the file system:</p>
    <a name="ul37232875185145"></a><a name="ul37232875185145"></a><ul id="ul37232875185145"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue1788258310319"><a name="parmvalue1788258310319"></a><a name="parmvalue1788258310319"></a><b>s3a://</b></span>.</li><li>HDFS: The path start<span id="ph59977425101351"><a name="ph59977425101351"></a><a name="ph59977425101351"></a>s</span>&nbsp;with&nbsp;<span class="parmvalue" id="parmvalue8630490185145"><a name="parmvalue8630490185145"></a><a name="parmvalue8630490185145"></a><b>/user</b></span> by default.</li></ul>
    <p id="p27981107185145"><a name="p27981107185145"></a><a name="p27981107185145"></a>A maximum of 1023 characters are allowed, but special characters (/:*?"&lt;&gt;|\;&amp;,'`!{}[]$) are not allowed. This parameter can be empty.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   The OBS path supports  **s3a://**. **s3a://**  is used by default.  
    >-   Files and programs encrypted by the KMS cannot be imported if the OBS path is used.  
    >-   The full path of HDFS and OBS contains a maximum of 1023 characters.  

6.  Confirm job configuration information and click  **OK**.

    After jobs are added, you can manage them.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >By default, each cluster supports a maximum of 10 running jobs.  


