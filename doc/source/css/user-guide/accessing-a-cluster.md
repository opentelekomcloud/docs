# Accessing a Cluster<a name="css_01_0012"></a>

After a cluster is created, you can access the cluster to use Elasticsearch to perform operations, for example, defining index data, importing data, searching for data, and much more. For more information about Elasticsearch, see the  [Elasticsearch Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html). You can use any of the following methods to access a cluster:

-   [Accessing a Cluster Using Kibana on the Management Console](#section9848115695612)
-   [Accessing a Cluster by Calling Elasticsearch APIs on the ECS That Is Located in the Same VPC as the Cluster](#section16223134914582)

## Accessing a Cluster Using Kibana on the Management Console<a name="section9848115695612"></a>

1.  Log in to the CSS management console.
2.  In the left navigation pane, click  **Clusters**.
3.  On the displayed  **Clusters**  page, locate the row where the target cluster resides and click  **Kibana**  in the  **Operation**  column.
4.  On the Kibana page that is displayed, you can create indices, query indices and documents, and analyze document fields. For details about Kibana, see  [What Is Kibana?](what-is-kibana.md). For details about how to import data to Elasticsearch, see the following sections:
    -   [Using Logstash to Import Data to Elasticsearch](using-logstash-to-import-data-to-elasticsearch.md)
    -   [Using Kibana or APIs to Import Data to Elasticsearch](using-kibana-or-apis-to-import-data-to-elasticsearch.md)


## Accessing a Cluster by Calling Elasticsearch APIs on the ECS That Is Located in the Same VPC as the Cluster<a name="section16223134914582"></a>

The ECS that you use to access the cluster by calling Elasticsearch APIs, must meet the following requirements. For details about how to create and log in to an ECS, see  [Logging In to an ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0092494193.html)  or  [Logging In to an ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0092494193.html).

-   Sufficient disk space is allocated for the ECS.
-   The ECS and the cluster must be in the same VPC.
-   The security group of the ECS must be the same as that of the cluster.

    If this requirement is not met, modify the ECS security group or configure the inbound and outbound rules of the ECS security group to allow the ECS security group to be accessed by all security groups of the cluster. For details, see  [Configuring Security Group Rules](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0030878383.html).

-   For security group rule settings of the target CSS cluster, set  **Protocol**  to  **TCP**  and  **Port Range**  to  **9200**  or a port range including port  **9200**  for both the outbound and inbound directions.

To access a cluster by invoking Elasticsearch APIs on the ECS that is located in the same VPC as the cluster, perform the following steps:

1.  Create and then log in to an ECS that meets the requirements.
2.  To access a cluster, use the private network address and port number of one node in the cluster. You can obtain the private network addresses of nodes from the  **Private Network Address**  column in the cluster list. If there is only one node in the cluster, the private network address and port number of the only node are displayed. If there are multiple nodes in the cluster, private network addresses and port numbers of all nodes are displayed.

    Assume that there are two nodes in a cluster. Value  **10.62.179.32:9200 10.62.179.33:9200**  indicates that the private network addresses of the two nodes are  **10.62.179.32**  and  **10.62.179.33**  respectively, and port  **9200**  is used to access both nodes.

3.  Run the cURL command to execute the API or invoke the API by using a program and then execute the program to use the cluster. For details about Elasticsearch operations and APIs, see the  [Elasticsearch Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).

    For example, run the following cURL command to check the index information in the cluster. In this example, the private network address of one node in the cluster is  **10.62.179.32**  and port  **9200**  is used to access the port.

    -   If the cluster you will access is enabled with the communication encryption function, you need to access the cluster using HTTPS and add  **-k**  to the cURL command.

        The CSS server will use a shared, self-signed certificate if communication encryption is used. As the client will not be able to authenticate the certificate in that case, we recommend that you disable certificate validation for clients. Please note you should restrict access, for example, via security groups, to ensure authenticity.

        ```
        curl -k 'https://10.62.179.32:9200/_cat/indices'
        ```

    -   If the cluster you access does not have the communication encryption enabled, run the following command:

        ```
        curl 'http://10.62.179.32:9200/_cat/indices'
        ```

    >![](/images/icon-note.gif) **NOTE:**   
    >In the preceding command, the private network address and port number of only one node in the cluster are used. If the node fails, the command will fail to be executed. If the cluster contains multiple nodes, you can replace the private network address and port number of the faulty node with those of any available node in the cluster. If the cluster contains only one node, restore the node and execute the command again.  

    If communication encryption is not enabled in the cluster, the command output is similar to that shown in the following figure.

    **Figure  1**  Command output<a name="fig129821943205913"></a>  
    ![](figures/command-output.png "command-output")


