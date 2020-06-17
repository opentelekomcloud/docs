# How Can I Connect to a PostgreSQL Database Through JDBC?<a name="rds_faq_0050"></a>

If you are connecting to a PostgreSQL database through Java database connectivity \(JDBC\), the SSL certificate is optional. For security reasons, you are advised to download the SSL certificate to encrypt the connection.

## Prerequisites<a name="sea9673f8b08a450386506c34a14adf87"></a>

You must be familiar with:

-   Computer basics
-   Java programming language
-   JDBC basic knowledge

## Connection with the SSL Certificate<a name="section17811586410"></a>

>![](/images/icon-note.gif) **NOTE:**   
>The JDBC connection is an SSL connection. The SSL certificate needs to be downloaded and verified for connecting to databases.  
>In the  **DB Information**  area on the  **Basic Information**  page, click  ![](figures/down.png)  in the  **SSL**  field to download the root certificate or certificate bundle.  

1.  Connect to the RDS PostgreSQL DB instance through JDBC.

    ```
    jdbc:postgresql://<instance_ip>:<instance_port>/<database_name>?sslmode=verify-full&sslrootcert=<ca.pem>
    ```

    **Table  1**  Parameter description

    <a name="table793953017457"></a>
    <table><thead align="left"><tr id="row693919300454"><th class="cellrowborder" valign="top" width="24.47%" id="mcps1.2.3.1.1"><p id="p9940730194518"><a name="p9940730194518"></a><a name="p9940730194518"></a><strong id="b101311025165717"><a name="b101311025165717"></a><a name="b101311025165717"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75.53%" id="mcps1.2.3.1.2"><p id="p59406301451"><a name="p59406301451"></a><a name="p59406301451"></a><strong id="b93901932115711"><a name="b93901932115711"></a><a name="b93901932115711"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row69401301452"><td class="cellrowborder" rowspan="2" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p69401305450"><a name="p69401305450"></a><a name="p69401305450"></a><em id="i5228536185018"><a name="i5228536185018"></a><a name="i5228536185018"></a>&lt;instance_ip&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p6940133015452"><a name="p6940133015452"></a><a name="p6940133015452"></a>If you are accessing the RDS DB instance through an ECS, <em id="i15296183445713"><a name="i15296183445713"></a><a name="i15296183445713"></a><strong id="b1429573445710"><a name="b1429573445710"></a><a name="b1429573445710"></a>instance_ip</strong></em> indicates the floating IP address displayed on the <strong id="b82967344578"><a name="b82967344578"></a><a name="b82967344578"></a>Basic Information</strong> page of the DB instance to which you intend to connect.</p>
    </td>
    </tr>
    <tr id="row17940173019459"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p2044012409545"><a name="p2044012409545"></a><a name="p2044012409545"></a>If you are accessing the RDS DB instance through an EIP, <em id="i1770194845715"><a name="i1770194845715"></a><a name="i1770194845715"></a><strong id="b11701548165716"><a name="b11701548165716"></a><a name="b11701548165716"></a>instance_ip</strong></em> indicates the EIP that has been bound to the DB instance.</p>
    </td>
    </tr>
    <tr id="row89406308455"><td class="cellrowborder" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p109407302452"><a name="p109407302452"></a><a name="p109407302452"></a><em id="i13432124114503"><a name="i13432124114503"></a><a name="i13432124114503"></a>&lt;instance_port&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p294013013459"><a name="p294013013459"></a><a name="p294013013459"></a>Indicates the database port number displayed on the <strong id="b1569311563248"><a name="b1569311563248"></a><a name="b1569311563248"></a>Basic Information</strong> page. The default port number is <strong id="b16694165618240"><a name="b16694165618240"></a><a name="b16694165618240"></a>5432</strong>.</p>
    </td>
    </tr>
    <tr id="row15940203014452"><td class="cellrowborder" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p594043016454"><a name="p594043016454"></a><a name="p594043016454"></a><em id="i1798184818501"><a name="i1798184818501"></a><a name="i1798184818501"></a>&lt;database_name&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p9940530164511"><a name="p9940530164511"></a><a name="p9940530164511"></a>Indicates the name of the database to which you intend to connect. The default database name is <strong id="b84235270610929"><a name="b84235270610929"></a><a name="b84235270610929"></a>postgres</strong>.</p>
    </td>
    </tr>
    <tr id="row99401430134513"><td class="cellrowborder" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p994073004512"><a name="p994073004512"></a><a name="p994073004512"></a>sslmode</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p794083019454"><a name="p794083019454"></a><a name="p794083019454"></a>Indicates the SSL connection mode. The default mode is verify-full.</p>
    </td>
    </tr>
    <tr id="row2940143020452"><td class="cellrowborder" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p1794093019452"><a name="p1794093019452"></a><a name="p1794093019452"></a>sslrootcert</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p19940330114516"><a name="p19940330114516"></a><a name="p19940330114516"></a>Indicates the directory of the CA certificate for the SSL connection. The certificate should be stored in the directory where the command is executed.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Example script in Java:

    ```
    import java.sql.Connection;
    import java.sql.DriverManager;
    import java.sql.ResultSet;
    import java.sql.Statement;
    
    public class MyConnTest {
    	final public static void main(String[] args) {
    		Connection conn = null;
    		// set sslmode here.
    		// with ssl certificate and path.
    		String url = "jdbc:postgresql://192.168.0.225:5432/my_db_test?sslmode=verify-full&sslrootcert=/home/Ruby/ca.pem";
    
    		try {
    			Class.forName("org.postgresql.Driver");
    			conn = DriverManager.getConnection(url, "root", "password");
    			System.out.println("Database connected");
    
    			Statement stmt = conn.createStatement();
    			ResultSet rs = stmt.executeQuery("SELECT * FROM mytable WHERE columnfoo = 500");
    			while (rs.next()) {
    				System.out.println(rs.getString(1));
    			}
    
    			rs.close();
    			stmt.close();
    			conn.close();
    		} catch (Exception e) {
    			e.printStackTrace();
    			System.out.println("Test failed");
    		} finally {
    			// release resource ....
    		}
    	}
    }
    ```


## Connection Without the SSL Certificate<a name="s12a6f787675c4a6789f8c302301c2a74"></a>

>![](/images/icon-note.gif) **NOTE:**   
>The JDBC connection is an SSL connection, but you do not need to download the SSL certificate because the certificate verification on the server is not required.  

1.  Connect to the RDS PostgreSQL DB instance through JDBC.

    ```
    jdbc:postgresql://<instance_ip>:<instance_port>/<database_name>?sslmode=disable
    ```

    **Table  2**  Parameter description

    <a name="table13983205311910"></a>
    <table><thead align="left"><tr id="row1398418533917"><th class="cellrowborder" valign="top" width="24.47%" id="mcps1.2.3.1.1"><p id="p139842531494"><a name="p139842531494"></a><a name="p139842531494"></a><strong id="b134217402017"><a name="b134217402017"></a><a name="b134217402017"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75.53%" id="mcps1.2.3.1.2"><p id="p139848531597"><a name="p139848531597"></a><a name="p139848531597"></a><strong id="b1491119409015"><a name="b1491119409015"></a><a name="b1491119409015"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49841538915"><td class="cellrowborder" rowspan="2" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p17984653296"><a name="p17984653296"></a><a name="p17984653296"></a><em id="i59845531192"><a name="i59845531192"></a><a name="i59845531192"></a>&lt;instance_ip&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p13984115312911"><a name="p13984115312911"></a><a name="p13984115312911"></a>If you are accessing the RDS DB instance through an ECS, <em id="i36636438016"><a name="i36636438016"></a><a name="i36636438016"></a><strong id="b1866110431109"><a name="b1866110431109"></a><a name="b1866110431109"></a>instance_ip</strong></em> indicates the floating IP address displayed on the <strong id="b146655435017"><a name="b146655435017"></a><a name="b146655435017"></a>Basic Information</strong> page of the DB instance to which you intend to connect.</p>
    </td>
    </tr>
    <tr id="row14985155310915"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p698518532913"><a name="p698518532913"></a><a name="p698518532913"></a>If you are accessing the RDS DB instance through an EIP, <em id="i35732561806"><a name="i35732561806"></a><a name="i35732561806"></a><strong id="b105722561309"><a name="b105722561309"></a><a name="b105722561309"></a>instance_ip</strong></em> indicates the EIP that has been bound to the DB instance.</p>
    </td>
    </tr>
    <tr id="row12985145310920"><td class="cellrowborder" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p1398510531395"><a name="p1398510531395"></a><a name="p1398510531395"></a><em id="i12985953097"><a name="i12985953097"></a><a name="i12985953097"></a>&lt;instance_port&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p149850537915"><a name="p149850537915"></a><a name="p149850537915"></a>Indicates the database port number displayed on the <strong id="b152771859204"><a name="b152771859204"></a><a name="b152771859204"></a>Basic Information</strong> page. The default port number is <strong id="b2027810599011"><a name="b2027810599011"></a><a name="b2027810599011"></a>5432</strong>.</p>
    </td>
    </tr>
    <tr id="row1698513531894"><td class="cellrowborder" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p179856535912"><a name="p179856535912"></a><a name="p179856535912"></a><em id="i1198518531391"><a name="i1198518531391"></a><a name="i1198518531391"></a>&lt;database_name&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p119851531594"><a name="p119851531594"></a><a name="p119851531594"></a>Indicates the name of the database to which you intend to connect. The default database name is <strong id="b426641811"><a name="b426641811"></a><a name="b426641811"></a>postgres</strong>.</p>
    </td>
    </tr>
    <tr id="row1498555318919"><td class="cellrowborder" valign="top" width="24.47%" headers="mcps1.2.3.1.1 "><p id="p098585312915"><a name="p098585312915"></a><a name="p098585312915"></a>sslmode</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.53%" headers="mcps1.2.3.1.2 "><p id="p2985125311915"><a name="p2985125311915"></a><a name="p2985125311915"></a>Indicates the SSL connection mode. <strong id="b8732171712277"><a name="b8732171712277"></a><a name="b8732171712277"></a>disable</strong> indicates that data is not encrypted.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Example script in Java:

    ```
    import java.sql.Connection;
    import java.sql.DriverManager;
    import java.sql.ResultSet;
    import java.sql.Statement;
    
    public class MyConnTest {
    	final public static void main(String[] args) {
    		Connection conn = null;
    		// set sslmode here.
    		// no ssl certificate, so do not specify path.
    		String url = "jdbc:postgresql://192.168.0.225:5432/my_db_test?sslmode=disable";
    		try {
    			Class.forName("org.postgresql.Driver");
    			conn = DriverManager.getConnection(url, "root", "password");
    			System.out.println("Database connected");
    
    			Statement stmt = conn.createStatement();
    			ResultSet rs = stmt.executeQuery("SELECT * FROM mytable WHERE columnfoo = 500");
    			while (rs.next()) {
    				System.out.println(rs.getString(1));
    			}
    			rs.close();
    			stmt.close();
    			conn.close();
    		} catch (Exception e) {
    			e.printStackTrace();
    			System.out.println("Test failed");
    		} finally {
    			// release resource ....
    		}
    	}
    }
    ```


