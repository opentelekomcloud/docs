# Configuring the JDBC Connection to Connect to a Cluster Using IAM Authentication<a name="dws_01_0132"></a>

When you use the JDBC application program to connect to a cluster, set the IAM username, credential, and other information as you configure the JDBC URL. After doing this, when you try to access a database, the system will automatically generate a temporary credential and a connection will be set up.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Currently, only clusters whose version is 1.3.1 or later \(including 1.3.1\) and corresponding JDBC driver provided by DWS can access the databases in IAM authentication mode. Download the JDBC driver. For details, see section  [Downloading the JDBC or ODBC Driver](downloading-the-jdbc-or-odbc-driver.md).  

## Configuring JDBC Connection Parameters<a name="section660621017949"></a>

**Table  1**  Database connection parameters

<a name="table18711649194147"></a>
<table><thead align="left"><tr id="row49861304194147"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.3.1.1"><p id="p32179157194147"><a name="p32179157194147"></a><a name="p32179157194147"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="87%" id="mcps1.2.3.1.2"><p id="p37754612194147"><a name="p37754612194147"></a><a name="p37754612194147"></a><strong id="b16755195015575"><a name="b16755195015575"></a><a name="b16755195015575"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row35428286194147"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p23266394194147"><a name="p23266394194147"></a><a name="p23266394194147"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p21919088194147"><a name="p21919088194147"></a><a name="p21919088194147"></a>gsjdbc4.jar/gsjdbc200.jar database connection descriptor The following is an example:</p>
<p id="p19802965194147"><a name="p19802965194147"></a><a name="p19802965194147"></a>jdbc:dws:iam://dws-IAM-demo:eu-de/postgres?AccessKeyID=XXXXXXXXXXXXXXXXXXXX&amp;SecretAccessKey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;DbUser=user_test&amp;AutoCreate=true</p>
<div class="note" id="note66045482194147"><a name="note66045482194147"></a><a name="note66045482194147"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul22562631194147"></a><a name="ul22562631194147"></a><ul id="ul22562631194147"><li><strong id="b1467917475813"><a name="b1467917475813"></a><a name="b1467917475813"></a>jdbc:dws:iam</strong> is a prefix in the URL format.</li><li><strong id="b18288898583"><a name="b18288898583"></a><a name="b18288898583"></a>dws-IAM-demo</strong> indicates the name of the cluster containing the database.</li><li>eu-de is the region where the cluster resides. For details about the DWS regions, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</li><li><strong id="b84235270694539"><a name="b84235270694539"></a><a name="b84235270694539"></a>postgres</strong> indicates the name of the database to which you want to connect.</li><li><strong id="b15322545135916"><a name="b15322545135916"></a><a name="b15322545135916"></a>AccessKeyID</strong> and <strong id="b17451152115913"><a name="b17451152115913"></a><a name="b17451152115913"></a>SecretAccessKey</strong> is the access key ID and secret access key corresponding to the IAM user specified by <strong id="b12729441801"><a name="b12729441801"></a><a name="b12729441801"></a>DbUser</strong>.</li><li>Set <strong id="b883961818012"><a name="b883961818012"></a><a name="b883961818012"></a>DbUser</strong> to the IAM username. Note that the current version does not support hyphens (-) in the IAM username.<a name="ul1742725215153"></a><a name="ul1742725215153"></a><ul id="ul1742725215153"><li>If the user specified by <strong id="b163721148219"><a name="b163721148219"></a><a name="b163721148219"></a>DbUser</strong> exists in the database, the temporary user credential has the same permissions as the existing user.</li><li>If the user specified by <strong id="b2450181212210"><a name="b2450181212210"></a><a name="b2450181212210"></a>DbUser</strong> does not exist in the database and the value of <strong id="b16464261827"><a name="b16464261827"></a><a name="b16464261827"></a>AutoCreate</strong> is <strong id="b854614297219"><a name="b854614297219"></a><a name="b854614297219"></a>true</strong>, a new user named by the value of <strong id="b1251517431622"><a name="b1251517431622"></a><a name="b1251517431622"></a>DbUser</strong> is automatically created. The created user is a common database user by default.</li></ul>
</li><li>Parameter <strong id="b162337237"><a name="b162337237"></a><a name="b162337237"></a>AutoCreate</strong> is optional. The default value is <strong id="b1185958845"><a name="b1185958845"></a><a name="b1185958845"></a>false</strong>. It indicates whether to automatically create a database user named by the value of <strong id="b1383011411741"><a name="b1383011411741"></a><a name="b1383011411741"></a>DbUser</strong> in the database.<a name="ul1483102224417"></a><a name="ul1483102224417"></a><ul id="ul1483102224417"><li>The value <strong id="b136421349244"><a name="b136421349244"></a><a name="b136421349244"></a>true</strong> indicates that a user is automatically created. If the user already exists, the user will not be created again.</li><li>The value <strong id="b64437255"><a name="b64437255"></a><a name="b64437255"></a>false</strong> indicates that a user is not created. If the username specified by <strong id="b8613350154"><a name="b8613350154"></a><a name="b8613350154"></a>DbUser</strong> does not exist in the database, an error is returned.</li></ul>
</li></ul>
</div></div>
</td>
</tr>
<tr id="row39648088194147"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p40139830194147"><a name="p40139830194147"></a><a name="p40139830194147"></a>info</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p25787388194147"><a name="p25787388194147"></a><a name="p25787388194147"></a>Database connection properties. Common properties include the following:</p>
<a name="ul23321221194147"></a><a name="ul23321221194147"></a><ul id="ul23321221194147"><li><strong id="b842352706103355"><a name="b842352706103355"></a><a name="b842352706103355"></a>ssl</strong>: a Boolean type. It indicates whether the SSL connection is used.</li><li><strong id="b842352706103459"><a name="b842352706103459"></a><a name="b842352706103459"></a>loglevel</strong>: an Integer type. It sets the log amount recorded in DriverManager for LogStream or LogWriter.<p id="p3597914194147"><a name="p3597914194147"></a><a name="p3597914194147"></a>Currently, <span class="parmname" id="parmname769647905105031"><a name="parmname769647905105031"></a><a name="parmname769647905105031"></a><b>org.postgresql.Driver.DEBUG</b></span> and <span class="parmname" id="parmname769647905105047"><a name="parmname769647905105047"></a><a name="parmname769647905105047"></a><b>org.postgresql.Driver.INFO</b></span> logs are supported. If the value is <strong id="b181882107131"><a name="b181882107131"></a><a name="b181882107131"></a>1</strong>, only <strong id="b75015186131"><a name="b75015186131"></a><a name="b75015186131"></a>org.postgresql.Driver.INFO</strong> (little information) is recorded. If the value is greater than or equal to <strong id="b653319574133"><a name="b653319574133"></a><a name="b653319574133"></a>2</strong>, <strong id="b8555725161610"><a name="b8555725161610"></a><a name="b8555725161610"></a>org.postgresql.Driver.DEBUG</strong> and <strong id="b1354093051613"><a name="b1354093051613"></a><a name="b1354093051613"></a>org.postgresql.Driver.INFO</strong> logs are printed, and detailed log information is generated. Its default value is <strong id="b147212553165"><a name="b147212553165"></a><a name="b147212553165"></a>0</strong>, which indicates that no logs are printed.</p>
</li><li><strong id="b842352706103312"><a name="b842352706103312"></a><a name="b842352706103312"></a>charSet</strong>: a string type. It indicates character sets used when data is sent from the database or the database receives data.</li><li><strong id="b1751152983"><a name="b1751152983"></a><a name="b1751152983"></a>prepareThreshold</strong>: an Integer type. It is used to determine the execution times of PreparedStatement before the information is converted into prepared statements on the server. The default value is <span class="parmvalue" id="parmvalue555125744105735"><a name="parmvalue555125744105735"></a><a name="parmvalue555125744105735"></a><b>5</b></span>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section50467166194735"></a>

```
//The following uses gsjdbc4.jar as an example. 
//The following encapsulates the database connection obtaining operations into an interface. You can connect to the database by specifying the region where the cluster is located, cluster name, access key ID, secret access key, and the corresponding IAM username.
public static Connection GetConnection(String clustername, String regionname, String AK, String SK, String username)
    {
        //Driver class
        String driver = "org.postgresql.Driver";
        //Database connection descriptor
        String sourceURL = "jdbc:dws:iam://" + clustername + ":" + regionname + "/postgres?" + "AccessKeyID=" + AK + "&SecretAccessKey=" + SK + "&DbUser=" + username + "&autoCreate=true";
        
        Connection conn = null;
        
        try
        {
            //Load the driver.
            Class.forName(driver);
        }
        catch( Exception e )
        {
             return null;
        }
        
        try
        {
             //Create a connection.
            conn = DriverManager.getConnection(sourceURL);
            System.out.println("Connection succeed!");
         }
        catch(Exception e)
        {
             return null;
        }
        
        return conn;
    };
```

