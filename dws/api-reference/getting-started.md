# Getting Started<a name="dws_02_0036"></a>

This section describes how to use DWS APIs to manage clusters. The procedure of the management clusters is as follows:

1.  Call the API in  [Authentication](authentication.md)  to obtain the user token, which will be put into the request header for authentication in a subsequent request.
2.  Call the API in  [Querying the Supported Node Types](querying-the-supported-node-types.md)  to obtain the supported node types.
3.  Call the API in  [Creating a Cluster](creating-a-cluster.md)  to create a cluster.
4.  Call the API in  [Querying the Cluster List](querying-the-cluster-list.md)  to obtain the cluster information.
5.  Call the API in  [Querying Cluster Details](querying-cluster-details.md)  to view cluster details.
6.  Call the API in  [Creating a Snapshot](creating-a-snapshot.md)  to create a snapshot.
7.  Call the API in  [Querying Snapshot Details](querying-snapshot-details.md)  to check whether the snapshot is successfully created.
8.  Call the API in  [Restoring a Cluster](restoring-a-cluster.md)  to restore a cluster using its snapshot.
9.  Call the API in  [Deleting a Snapshot](deleting-a-snapshot.md)  to delete an unwanted snapshot.
10. Call the API in  [Deleting a Cluster](deleting-a-cluster.md)  to delete an unwanted cluster.

## Prerequisites<a name="s18b770fcb98c4842a37db54d44696086"></a>

-   You have created a VPC, subnet, and security group and obtained their IDs. For details, see  [Creating a VPC](creating-a-vpc.md).
-   You have obtained the endpoints of IAM and DWS. For details, see  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html).
-   You have obtained the project ID. For details, see  [Obtaining a Project ID](obtaining-a-project-id.md).

## Managing a Cluster<a name="sbee2db72d04f4871b74e0c859bd458f2"></a>

The following values are examples \(replace them based on the actual situation\).

-   IAM endpoint:  **iam\_endpoint** 
-   DWS endpoint:  **dws\_endpoint**
-   VPC ID:  **219ab8a0-1272-4049-a383-8ad0b770fa11**
-   Subnet ID:  **d23ef2e9-8b90-49b3-bc4a-fd7d6bea6bec**
-   Security group ID:  **12e3c23a-8710-4b75-95e4-5c8d7f68ef3c**
-   Project ID:  **9bc552e6-19af-4326-800d-281a92984636**

Perform the following operations to manage the cluster.

1.  Before calling other APIs, call the API in  [Authentication](authentication.md)  to obtain the token and set it as an environment variable.

    ```
    curl -H "Content-Type:application/json" https://{iam_endpoint}/v3/auth/tokens -X POST -d '{
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "testname",
                        "domain": {
                            "name": "testname"
                        },
                        "password": "Passw0rd"
                    }
                }
            },
            "scope": {
                "project": {
                    "name": "eu-de"
                }
            }
        }
    }' -v -k
    ```

    1.  Obtain the value of  **X-Subject-Token**  from the response header as follows.  **X-Subject-Token**  indicates the token.

        ```
        X-Subject-Token:MIIDkgYJKoZIhvcNAQcCoIIDgzCCA38CAQExDTALBglghkgBZQMEAgEwgXXXXX...
        ```

    2.  Run the following command to set the token as an environment variable:

        **export Token=\{X-Subject-Token\}**

        **X-Subject-Token**  is the token obtained in the preceding step.

        ```
        export Token=MIIDkgYJKoZIhvcNAQcCoIIDgzCCA38CAQExDTALBglghkgBZQMEAgEwgXXXXX...
        ```

2.  Call the API in  [Querying the Supported Node Types](querying-the-supported-node-types.md)  to obtain the supported node types.

    ```
    curl -X GET -H 'Content-Type:application/json;charset=utf-8' -H "X-Auth-Token:$Token" https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/node_types -v -k
    ```

    The request response is as follows:

    ```
    STATUS CODE 200
    {
        "node_types": [
            {
                "spec_name": "dws.d1.xlarge",
                "id": "ebe532d6-665f-40e6-a4d4-3c51545b6a67",
                "detail": [
                    {
                        "type": "vCPU", 
                        "value": "4"
                        
                    },
                    {
                        "value": "1675",
                        "type": "LOCAL_DISK",
                        "unit": "GB"
                    },
                    {
                        "type": "mem",
                        "value": "32",
                       
                        "unit": "GB"
                    }
                ]
            },
            {
                "spec_name": "dws.m1.xlarge.ultrahigh",
                "id": "ebe532d6-665f-40e6-a4d4-3c51545b4f71",
                "detail": [
                    {
                        "type": "vCPU",
                        "value": "4"
                    },
                    {
                        "value": "512",
                        "type": "SSD",
                        "unit": "GB"
                    },
                    {
                        "type": "mem",
                        "value": "32",
                        "unit": "GB"
                    }
                ]
            }
        ]
    }
    ```

3.  Call the API in  [Creating a Cluster](creating-a-cluster.md)  to create a cluster.

    The examples for configuring the cluster are as follows:

    -   Cluster name:  **dws-demo**
    -   Administrator username:  **dbadmin**
    -   Administrator password:  **Dws2017demo!**
    -   Port:  **8000**
    -   Node type:  **dws.d1.xlarge**
    -   Number of nodes:  **3**
    -   EIP:  **auto\_assign**

    ```
    curl -X POST -H 'Content-Type:application/json;charset=utf-8' -H "X-Auth-Token:$Token" -d '{
        "node_type": "dws.d1.xlarge",
            "number_of_node": 3,
            "subnet_id": "d23ef2e9-8b90-49b3-bc4a-fd7d6bea6bec",
            "security_group_id": "12e3c23a-8710-4b75-95e4-5c8d7f68ef3c",
            "vpc_id": "219ab8a0-1272-4049-a383-8ad0b770fa11",
            "port": 8000,
            "name": "dws-demo",
            "user_name": "dbadmin",
            "user_pwd": "Dws2017demo!",
            "public_ip": {
                "public_bind_type": "auto_assign"
            }
    }' https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/clusters -v -k
    ```

    If status code  **200**  is returned, the request for creating a cluster is successfully sent.

4.  Call the API in  [Querying the Cluster List](querying-the-cluster-list.md)  to obtain the cluster information.

    ```
    curl -X GET -H 'Content-Type:application/json;charset=utf-8' -H "X-Auth-Token:$Token" https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/clusters -k –v
    ```

    The request response is as follows:

    ```
    {
            "clusters": [
            {
            "id": "7ba031f6-81f4-4670-ad20-c490b91877e5",
            "status": "AVAILABLE",
            "sub_status": "NORMAL",            
            "task_status": null,
            "action_progress": null,
            "node_type": "dws.d1.xlarge",
            "subnet_id": "d23ef2e9-8b90-49b3-bc4a-fd7d6bea6bec",
            "security_group_id": "12e3c23a-8710-4b75-95e4-5c8d7f68ef3c",
            "number_of_node": 3,
            "availability_zone": "eu-de-01",
            "port": 8000,
            "name": "dws-demo",
            "version": "1.1.0",
            "vpc_id": "219ab8a0-1272-4049-a383-8ad0b770fa11",
            "user_name": "dbadmin",
            "public_ip": {
                "public_bind_type": "auto_assign",
                "eip_id": "85b20d7e-9eb7-4b2a-98f3-3c8843ea3574"
             },
            "public_endpoints": [
                {
                    "public_connect_info": "10.0.0.8:8000",
                    "jdbc_url": "jdbc:postgresql://10.0.0.8:8000/<YOUR_DATABASE_NAME>"
                }
             ],
            "endpoints": [
                {
                    "connect_info": "192.168.0.10:8000",
                    "jdbc_url": "jdbc:postgresql://192.168.0.10:8000/<YOUR_DATABASE_NAME>"
                },
                {
                    "connect_info": "192.168.0.12:8000",
                    "jdbc_url": "jdbc:postgresql://192.168.0.12:8000/<YOUR_DATABASE_NAME>"
                }
             ] , 
            "updated": "2018-01-15T12:50:06",
            "created": "2018-01-15T12:50:06"
            }
        ]
    }
    ```

    -   If  **status**  is  **CREATING**, the cluster is being created. If  **status**  is  **AVAILABLE**, the cluster is successfully created.
    -   The UUID of cluster  **dws-demo**  is  **7ba031f6-81f4-4670-ad20-c490b91877e5**. Record the UUID for subsequent use.

5.  Call the API in  [Querying Cluster Details](querying-cluster-details.md)  to view cluster details.

    ```
    curl -X GET -H "Content-Type:application/json" -H "X-Auth-Token:$Token" 
     https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/clusters/7ba031f6-81f4-4670-ad20-c490b91877e5 -k -v
    ```

    The request response is as follows:

    ```
    {
        "cluster": {
            "id": "7ba031f6-81f4-4670-ad20-c490b91877e5",
            "status": "AVAILABLE",
            "name": "dws-demo",
            "updated": "2018-01-15T12:50:06",
            "created": "2018-01-15T12:50:06",
            "user_name": "dbadmin",
            "sub_status": "NORMAL",
            "task_status": null,
            "action_progress": null,
            "node_type": "dws.d1.xlarge",        
            "node_type_id": "5ddb1071-c5d7-40e0-a874-8a032e81a697",
            "subnet_id": "d23ef2e9-8b90-49b3-bc4a-fd7d6bea6bec",
            "security_group_id": "12e3c23a-8710-4b75-95e4-5c8d7f68ef3c",
            "number_of_node": 3,
            "availability_zone": "eu-de-01",
            "port": 8000,        
            "vpc_id": "219ab8a0-1272-4049-a383-8ad0b770fa11",        
            "public_ip": {
                "public_bind_type": "auto_assign",
                "eip_id": "85b20d7e-9eb7-4b2a-98f3-3c8843ea3574"
            },        
            "public_endpoints": [
            {
                    "public_connect_info": "10.0.0.8:8000",
                    "jdbc_url": "jdbc:postgresql://10.0.0.8:8000/<YOUR_DATABASE_NAME>"
             }
             ],
            "endpoints": [
            {
                    "connect_info": "192.168.0.10:8000",
                    "jdbc_url": "jdbc:postgresql://192.168.0.10:8000/<YOUR_DATABASE_NAME>"
            },
            {
                    "connect_info": "192.168.0.12:8000",
                    "jdbc_url": "jdbc:postgresql://192.168.0.12:8000/<YOUR_DATABASE_NAME>"
            }
             ],
            "version": "1.1.0",
            "maintain_window": {
                "day": "Wed",
                "start_time": "22:00",
                "end_time": "02:00"
            }, 
            "tags": null, 
    
            "parameter_group": {
                  "id": "157e9cc4-64a8-11e8-adc0-fa7ae01bbebc",
                  "name": "Default-Parameter-Group-DWS",
                  "status": "In-Sync"
            } 
        }
    }
    ```

    **public\_endpoints**  and  **endpoints**  can be queried from the response. After the cluster is successfully created, you can use  **public\_endpoints**  or  **endpoints**  to access the cluster from an external source.

6.  Call the API in  [Creating a Snapshot](creating-a-snapshot.md)  to create a snapshot.

    Create snapshot  **snapshotForDemoCluster**  for cluster  **dws-demo**.

    ```
    curl -X POST -H "Content-Type:application/json" -H "X-Auth-Token:$Token" -d '{
        "snapshot": {
            "name": "snapshotForDemoCluster",
            "cluster_id": "7ba031f6-81f4-4670-ad20-c490b91877e5",
            "description": "Snapshot description" 
        }
    }' https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/snapshots -k -v
    ```

    The request response is as follows:

    ```
    {
      "snapshot": { 
          "id": "2a4d0f86-67cd-408a-8b66-017454fb7793" 
      }
    }
    ```

    If status code  **200**  is returned, the request for creating a snapshot is successfully sent. Record  **id**  so that the ID can be used when you query the snapshot details later.

7.  Call the API in  [Querying Snapshot Details](querying-snapshot-details.md)  to check whether the snapshot is successfully created.

    ```
    curl -X GET -H 'Content-Type:application/json;charset=utf-8' -H "X-Auth-Token:$Token" https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/snapshots/2a4d0f86-67cd-408a-8b66-017454fb7793 -k -v
    ```

    If the snapshot status in the response is  **AVAILABLE**, the snapshot is successfully created. If the snapshot status is  **CREATING**, the snapshot is being created.

    ```
    { 
        "snapshot": { 
            "id": "2a4d0f86-67cd-408a-8b66-017454fb7793", 
            "name": "snapshotForDemoCluster", 
            "description": "Snapshot description", 
            "started": "2018-01-18T13:59:23Z", 
            "finished": "2018-01-18T13:01:40Z",
            "size": 500, 
            "status": "AVAILABLE", 
            "type": "MANUAL", 
            "cluster_id": "4f87d3c4-9e33-482f-b962-e23b30d1a18c" 
        } 
    }
    ```

8.  Call the API in  [Restoring a Cluster](restoring-a-cluster.md)  to restore a cluster using its snapshot.

    Restore snapshot  **snapshotForDemoCluster**  to new cluster  **dws-restore**.

    ```
    curl -X POST -H 'Content-Type:application/json;charset=utf-8' -H "X-Auth-Token:$Token" -d '{
        "restore": {
            "name": "dws-restore"
        }
    }' https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/snapshots/2a4d0f86-67cd-408a-8b66-017454fb7793/actions -v -k
    ```

    If status code  **200**  is returned, the cluster is successfully restored. You can check the cluster restoration status by performing operations in  [Querying Cluster Details](querying-cluster-details.md).

9.  Call the API in  [Deleting a Snapshot](deleting-a-snapshot.md)  to delete an unwanted snapshot.

    ```
    curl -X DELETE -H 'Content-Type:application/json;charset=utf-8' -H "X-Auth-Token:$Token" https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/snapshots/2a4d0f86-67cd-408a-8b66-017454fb7793 -v -k
    ```

    If status code  **202**  is returned, the snapshot is successfully deleted.

10. Call the API in  [Deleting a Cluster](deleting-a-cluster.md)  to delete an unwanted cluster.

    ```
    curl -X DELETE -H 'Content-Type:application/json;charset=utf-8' -H "X-Auth-Token:$Token" -d '{
        "keep_last_manual_snapshot":0
    }' https://{dws_endpoint}/v1.0/9bc552e6-19af-4326-800d-281a92984636/clusters/7ba031f6-81f4-4670-ad20-c490b91877e5 -v -k
    ```

    If status code  **202**  is returned, the cluster is successfully deleted.


