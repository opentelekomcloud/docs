# Accessing a DCS Redis Instance<a name="EN-US_TOPIC_0237970590"></a>

You can access the created DCS instances through your Redis client.

DCS works with multiple types of Redis clients. This section describes how to use the redis-cli and Redis Java \(Jedis\) clients to access a DCS Redis instance. For more information on how to use other Redis clients, visit [https://redis.io/clients](https://redis.io/clients).

## Prerequisites<a name="section42371273"></a>

-   The DCS Redis instance you want to access is in the  **Running**  state.
-   An ECS has been created to serve as your Redis client.

    For more information on how to create ECSs, see the  _Elastic Cloud Server User Guide_.

-   The GNU Compiler Collection \(GCC\) has been installed on the ECS serving as your Redis client.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The ECS serving as your Redis client and the DCS instance to be accessed must belong to the same VPC and can communicate with each other.  

## Procedure<a name="section45797138"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  <a name="li5978963511441"></a>Obtain the IP address:port number of the DCS instance.
    1.  On the  **Cache Manager**  page, click the name of the DCS instance you want to access.
    2.  On the  **Summary** tab page of the instance details page, view the **Connection Address**  \(IP address:port number\) of the DCS instance.

6.  Access the chosen DCS instance.
    -   By using redis-cli
        1.  Download the source code package of your Redis client from  [http://download.redis.io/releases/redis-3.0.7.tar.gz](http://download.redis.io/releases/redis-3.0.7.tar.gz).
        2.  Upload the source code package of your Redis client to the ECS serving as your Redis client.
        3.  Log in to the ECS that serves as your Redis client.
        4.  Run the following command to decompress the  **redis-3.0.7**  directory from the source code package of your Redis client:

            **tar -xzf redis-3.0.7.tar.gz**

        5.  Run the following commands to go to the  **redis-3.0.7**  directory and compile the source code of your Redis client:

            **cd redis-3.0.7**

            **make**

        6.  Run the following commands to access the chosen DCS instance:

            **cd src**

            **./redis-cli -h  _192.168.0.148_  -p  _6379_**

            In the second command, use the DCS instance IP address and port number obtained in  [5](#li5978963511441).

        7.  On redis-cli, run the following command to authenticate access to the selected DCS instance:

            **auth password**

            In this command,  _password_  indicates the password used for login to the chosen DCS instance. This password is defined during DCS Redis instance creation.

            If information similar to the following is displayed, access to the chosen DCS instance is authenticated, and you can now read from and write to the chosen DCS instance:

            ```
            [root@dcs-vm ~]# ./redis-cli -h 192.168.0.148 -p 6379
            192.168.0.148:6379> auth ******
            OK
            192.168.0.148:6379>
            ```

            In this example command output:

            -   **192.168.0.148**  is an example IP address of DCS instance, which is obtained in  [5](#li5978963511441).
            -   **6379**  is an example port number of DCS instance, which is obtained in  [5](#li5978963511441).

    -   By using Jedis
        1.  Obtain the source code of the Jedis client from  [https://github.com/xetorthio/jedis](https://github.com/xetorthio/jedis).
        2.  Write code.
            1.  Example code for a single Jedis connection

                ```
                //Create a connection
                 String host = "192.168.0.150"; 
                 int port = 6379; 
                 String pwd = "passwd"; 
                  
                 Jedis client = new Jedis(host, port); 
                 client.auth(pwd);
                 client.connect(); //Run the set command
                 String result = client.set("key-string", "Hello, Redis!"); 
                 System.out.println( String.format("set command result:%s", result) ); //Run the get command
                 String value = client.get("key-string"); 
                 System.out.println( String.format("get command result:%s", value) );
                ```

            2.  Example code for a Jedis connection pool

                ```
                //Generate configuration information of a Jedis connection pool
                 String ip = "192.168.0.150"; 
                 int port = 6379; 
                 String pwd = "passwd"; 
                 GenericObjectPoolConfig config = new GenericObjectPoolConfig(); 
                 config.setTestOnBorrow(false); 
                 config.setTestOnReturn(false); 
                 config.setMaxTotal(100); 
                 config.setMaxIdle(100); 
                 config.setMaxWaitMillis(2000); 
                 JedisPool pool = new JedisPool(config, ip, port, 100000, pwd);//Generate a Jedis connection pool when the client application is being initialized
                 //Get a Jedis connection from the Jedis connection pool when the client initiates a request
                 Jedis client = pool.getResource(); 
                 try { 
                     //Run commands
                     String result = client.set("key-string", "Hello, Redis!"); 
                     System.out.println( String.format("set command result:%s", result) ); 
                     String value = client.get("key-string"); 
                     System.out.println( String.format("get command result:%s", value) ); 
                 } catch (Exception e) { 
                     // TODO: handle exception
                 } finally { 
                     //Return the Jedis connection to the Jedis connection pool after the client's request is processed
                     if (null != client) { 
                         pool.returnResource(client); 
                     } 
                 } // end of try block
                 //Destroy the Jedis pool when the client application is closed
                 pool.destroy();
                ```

        3.  Compile code according to the  **readme**  file in the source code of the Jedis client. Run the Jedis client to access the chosen DCS Redis instance.



