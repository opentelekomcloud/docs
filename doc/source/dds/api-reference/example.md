# Example<a name="dds_api_0017"></a>

This section describes how to create a cluster instance by calling APIs.

>![](/images/icon-note.gif) **NOTE:**   
>The validity period of a token obtained from IAM is 24 hours. If you want to use a token for authentication, cache it to avoid frequent IAM API calling.  

## Involved APIs<a name="dds_api_0013_en-us_topic_0121682346_section872994"></a>

If you use a token for authentication, you must obtain the user's token and add  **X-Auth-Token**  to the request message header of the service API when making an API call.

-   API for obtaining tokens from IAM
-   Creating a DDS DB instance using an open API

## Procedure<a name="dds_api_0013_en-us_topic_0121682346_section7856948"></a>

1.  Obtain the token by following instructions in section  [Token Authentication](token-authentication.md).
2.  Send  **POST https://_DDS__ endpoint_/v3/\{_project\_id_\}/instances**.
3.  Add  **X-Auth-Token**  to the request header.
4.  Specify the following parameters in the request body:

    >![](/images/icon-note.gif) **NOTE:**   
    >The values of  **region**  and  **availability\_zone**  are used as examples.  
    >For details about the API used for creating DB instances, see  [Creating a DB Instance](creating-a-db-instance.md).  

    ```
    {
      "name": "test-cluster", //DB instance name
      "datastore": {
        "type": "DDS-Community", // Database type and version
         "version": "3.4", //Database version
         "storage_engine": "wiredTiger" //Storage engine
      },
        "region": "aaa", //Region name
        "availability_zone": "bbb", //AZ name
        "vpc_id": "674e9b42-cd8d-4d25-a2e6-5abcc565b961", //VPC ID
        "subnet_id": "f1df08c5-71d1-406a-aff0-de435a51007b", //Subnet ID
       "security_group_id": "7aa51dbf-5b63-40db-9724-dad3c4828b58", //Security group ID
       "password": "Test@123", //Administrator password
       "disk_encryption_id": "d4825f1b-5e47-4ff7-8ca9-0960da1770b1", //Key ID for encrypting disks
       "mode": "Sharding", //Sharded-cluster instance type
      "flavor": [
        {
           "type":"mongos", //mongos node
          "num": 2, //Quantity
          "spec_code": "dds.mongodb.s2.medium.4.mongos" //Node resource code
        },
        {
           "type":"shard", //shard node
          "num": 2, //Quantity
          "storage": "ULTRAHIGH", //Disk type
          "size": 20, //Disk size
          "spec_code": "dds.mongodb.s2.medium.4.shard" //Node resource code
        },
        {
           "type":"config", //config node
          "num": 1, //Quantity
          "storage": "ULTRAHIGH", //Disk type
          "size": 20, //Disk size
          "spec_code": "dds.mongodb.s2.large.2.config" //Node resource type
        }
      ],
      "backup_strategy": {
        "start_time": "08:15-09:15", //Backup time window
        "keep_days": "8"  //Retention days of backup files
      }
    }
    ```

    If the following information is displayed, the request is successful:

    ```
    {
      "id": "46125c43ca4d424a9f5c97354223c4e0in02",
      "name": "test-cluster",
      "datastore": {
        "type": "DDS-Community",
        "version": "3.4",
        "storage_engine": "wiredTiger"
      },
      "created": "2019-01-14 08:50:27",
      "status": "creating",
      "region": "aaa",
      "availability_zone": "bbb",
      "vpc_id": "674e9b42-cd8d-4d25-a2e6-5abcc565b961",
      "subnet_id": "f1df08c5-71d1-406a-aff0-de435a51007b",
      "security_group_id": "7aa51dbf-5b63-40db-9724-dad3c4828b58",
      "disk_encryption_id": "d4825f1b-5e47-4ff7-8ca9-0960da1770b1",
      "mode": "Sharding",
      "flavor": [
        {
          "type": "mongos",
          "num": 2,
          "spec_code": "dds.mongodb.s2.medium.4.mongos"
        },
        {
          "type": "shard",
          "num": 2,
          "size": 20,
          "spec_code": "dds.mongodb.s2.medium.4.shard"
        },
        {
          "type": "config",
          "num": 1,
          "size": 20,
          "spec_code": "dds.mongodb.s2.large.2.config"
        }
      ],
      "backup_strategy": {
        "start_time": "08:15-09:15",
        "keep_days": "8"
      },
      "job_id": "c0c606b6-470a-48c7-97a2-6c7f146014d4"
    }
    ```

    If the request fails, an error code and error information are returned. For details, see section  [Error Code](error-code.md).


