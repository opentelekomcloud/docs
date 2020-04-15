# API Usage<a name="EN-US_TOPIC_0090543968"></a>

This chapter describes how to use manila commands provided by python-manilaclient, and how to invoke the APIs provided by SFS using manila commands.

## Prerequisites<a name="section49212545145647"></a>

-   python-manilaclient has been installed in the execution environment. For details, see  [Software Compatibility](before-you-start.md#section1821310111813).
-   You can access the APIs provided by SFS in the execution environment.

## Configuring Environment Variables<a name="section3378012145643"></a>

To run manila commands correctly, you need to configure environment variables, including an IAM authentication account and API command configuration information.

1.  Log in to the execution environment.
2.  Import environment variables.

    Run the following command on a Linux host to import the environment variables required for invoking the OpenStack Manila APIs provided by SFS. Note that you should replace  _<os-user-domain-name\>_  and  _<os-username\>_  with the actual values before running the command. For detailed description of the parameters, see  [Table 1](#table6953183014475).

    ```
    export OS_USER_DOMAIN_NAME=<os-user-domain-name>
    export OS_USERNAME=<os-username>
    export OS_PASSWORD=<os-password>
    export OS_PROJECT_NAME=<os-project_name>
    export OS_AUTH_URL=<os-auth-url>
    export OS_ENDPOINT_TYPE=<os-endpoint-type>
    export PYTHONWARNINGS=ignore
    export MANILACLIENT_INSECURE=True
    ```

    **Table  1**  Parameter description

    <a name="table6953183014475"></a>
    <table><thead align="left"><tr id="row3944153094715"><th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.1"><p id="p1194413094714"><a name="p1194413094714"></a><a name="p1194413094714"></a><strong id="b842352706162655"><a name="b842352706162655"></a><a name="b842352706162655"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="7.519248075192481%" id="mcps1.2.5.1.2"><p id="p109445300471"><a name="p109445300471"></a><a name="p109445300471"></a><strong id="b842352706162657"><a name="b842352706162657"></a><a name="b842352706162657"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.3"><p id="p1694453054716"><a name="p1694453054716"></a><a name="p1694453054716"></a><strong id="b1824863294017"><a name="b1824863294017"></a><a name="b1824863294017"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p894413010475"><a name="p894413010475"></a><a name="p894413010475"></a><strong id="b842352706231346"><a name="b842352706231346"></a><a name="b842352706231346"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row159451930194717"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p1194473015478"><a name="p1194473015478"></a><a name="p1194473015478"></a>OS_USER_DOMAIN_NAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.5.1.2 "><p id="p594418308472"><a name="p594418308472"></a><a name="p594418308472"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.3 "><p id="p169451230134714"><a name="p169451230134714"></a><a name="p169451230134714"></a>Domain name of an IAM account</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p794511300473"><a name="p794511300473"></a><a name="p794511300473"></a>-</p>
    <p id="p17945930134719"><a name="p17945930134719"></a><a name="p17945930134719"></a></p>
    </td>
    </tr>
    <tr id="row179471330124715"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p1694543074713"><a name="p1694543074713"></a><a name="p1694543074713"></a>OS_USERNAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.5.1.2 "><p id="p1194583016475"><a name="p1194583016475"></a><a name="p1194583016475"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.3 "><p id="p10945163012475"><a name="p10945163012475"></a><a name="p10945163012475"></a>User name of an IAM account</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p11945830154716"><a name="p11945830154716"></a><a name="p11945830154716"></a>-</p>
    </td>
    </tr>
    <tr id="row29491730184714"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p694816305472"><a name="p694816305472"></a><a name="p694816305472"></a>OS_PASSWORD</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.5.1.2 "><p id="p49485302479"><a name="p49485302479"></a><a name="p49485302479"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.3 "><p id="p0948430144713"><a name="p0948430144713"></a><a name="p0948430144713"></a>Password of an IAM account</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p1394803011477"><a name="p1394803011477"></a><a name="p1394803011477"></a>-</p>
    </td>
    </tr>
    <tr id="row89494308478"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p1194953018478"><a name="p1194953018478"></a><a name="p1194953018478"></a>OS_PROJECT_NAME</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.5.1.2 "><p id="p189491530164715"><a name="p189491530164715"></a><a name="p189491530164715"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.3 "><p id="p4949143054714"><a name="p4949143054714"></a><a name="p4949143054714"></a>Project name. Set this parameter based on the project to which the account belongs, for example, eu-de or singapore.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p8949193004715"><a name="p8949193004715"></a><a name="p8949193004715"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row1395123020476"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p15949173013479"><a name="p15949173013479"></a><a name="p15949173013479"></a>OS_AUTH_URL</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.5.1.2 "><p id="p1295123004719"><a name="p1295123004719"></a><a name="p1295123004719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.3 "><p id="p16951430114715"><a name="p16951430114715"></a><a name="p16951430114715"></a>URL for IAM authentication, which is used to authenticate the IAM account. Set this parameter based on the actual authentication URL.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p1195115307471"><a name="p1195115307471"></a><a name="p1195115307471"></a>https://iam.eu-de.otc.t-systems.com/v3</p>
    </td>
    </tr>
    <tr id="row1695220309475"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p1995113016478"><a name="p1995113016478"></a><a name="p1995113016478"></a>OS_ENDPOINT_TYPE</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.5.1.2 "><p id="p9951123011478"><a name="p9951123011478"></a><a name="p9951123011478"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.3 "><p id="p12951133010477"><a name="p12951133010477"></a><a name="p12951133010477"></a>Endpoint type. The value is fixed to <strong id="b12721131712467"><a name="b12721131712467"></a><a name="b12721131712467"></a>publicURL</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p209529304474"><a name="p209529304474"></a><a name="p209529304474"></a>publicURL</p>
    </td>
    </tr>
    <tr id="row10953230124715"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p189521530194714"><a name="p189521530194714"></a><a name="p189521530194714"></a>PYTHONWARNINGS</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.5.1.2 "><p id="p1595214301478"><a name="p1595214301478"></a><a name="p1595214301478"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.3 "><p id="p395383054713"><a name="p395383054713"></a><a name="p395383054713"></a>Whether to ignore the warning. If the value is <strong id="b126437194711"><a name="b126437194711"></a><a name="b126437194711"></a>ignore</strong>, the python warning information is ignored.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p1395353015471"><a name="p1395353015471"></a><a name="p1395353015471"></a>ignore</p>
    </td>
    </tr>
    <tr id="row828213235211"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p142831723325"><a name="p142831723325"></a><a name="p142831723325"></a>MANILACLIENT_INSECURE</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.519248075192481%" headers="mcps1.2.5.1.2 "><p id="p17283523824"><a name="p17283523824"></a><a name="p17283523824"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.3 "><p id="p14283132312217"><a name="p14283132312217"></a><a name="p14283132312217"></a>Whether to enable the insecure mode to communicate with the server. The default value is <strong id="b143995431324"><a name="b143995431324"></a><a name="b143995431324"></a>False</strong>. If the value is <strong id="b889218523216"><a name="b889218523216"></a><a name="b889218523216"></a>False</strong>, the security mode is enabled. If the value is <strong id="b945413153310"><a name="b945413153310"></a><a name="b945413153310"></a>True</strong>, the insecure mode is enabled and certificate authentication is ignored. Currently, SFS supports only the insecure mode and the value is fixed to <strong id="b12671152010513"><a name="b12671152010513"></a><a name="b12671152010513"></a>True</strong>.</p>
    <div class="note" id="note5967440161614"><a name="note5967440161614"></a><a name="note5967440161614"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p89671540151616"><a name="p89671540151616"></a><a name="p89671540151616"></a>Currently, IAM does not open the interface for downloading and obtaining the CA certificate. Python 2.7.9 and later versions do not allow the client to use a self-signed certificate. Therefore, the current SFS provides only the insecure mode for communicating with IAM, ignoring certificate authentication.</p>
    </div></div>
    <div class="notice" id="note5909134411618"><a name="note5909134411618"></a><a name="note5909134411618"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p139091444101611"><a name="p139091444101611"></a><a name="p139091444101611"></a>When the insecure mode is used to communicate with the IAM, ensure that the IAM authentication URL is correct.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p82837236211"><a name="p82837236211"></a><a name="p82837236211"></a>True</p>
    </td>
    </tr>
    </tbody>
    </table>

    Example command:

    ```
    export OS_USER_DOMAIN_NAME=sample-iam-dommain-name
    export OS_USERNAME=sample-iam-username
    export OS_PASSWORD=sample-iam-user-password
    export OS_PROJECT_NAME=eu-de
    export OS_AUTH_URL=https://iam.eu-de.otc.t-systems.com/v3
    export OS_ENDPOINT_TYPE=publicURL
    export PYTHONWARNINGS=ignore
    export MANILACLIENT_INSECURE=True
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To save the environment variable information in the local environment, you can write the preceding command to a file, and then run the  **source** _file name_  command to import the environment variable. For example, to save the environment variables to the manilarc file, perform the following operations:  
    >1.  Run the  **vi manilarc**  command to create and edit the manilarc file. Press  **i**  to enter the editing mode and write the following command:  
    >    ```  
    >    export OS_USER_DOMAIN_NAME=sample-iam-dommain-name  
    >    export OS_USERNAME=sample-iam-username  
    >    export OS_PASSWORD=sample-iam-user-password  
    >    export OS_PROJECT_NAME=eu-de  
    >    export OS_AUTH_URL=https://iam.eu-de.otc.t-systems.com/v3  
    >    export OS_ENDPOINT_TYPE=publicURL  
    >    export PYTHONWARNINGS=ignore  
    >    export MANILACLIENT_INSECURE=True  
    >    ```  
    >2.  Run the  **source manilarc**  command to import environment variables.  

3.  Run the  **manila list**  command to check whether the environment variables are successfully imported.

    ```
    root@n-version-client:~/ca# manila list
    +--------------------------------------+---------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | ID                                   | Name    | Size | Share Proto | Status    | Is Public | Share Type Name | Host                                                                          | Availability Zone |
    +--------------------------------------+---------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    | 416112b6-e5c9-4a46-8dd1-80749fc09336 | sample1 | 1    | NFS         | available | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    | 52820f82-1419-4f4c-a032-e97e310f5505 | sample  | 10   | NFS         | available | False     | default         | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe | eu-de-01          |
    +--------------------------------------+---------+------+-------------+-----------+-----------+-----------------+-------------------------------------------------------------------------------+-------------------+
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the command fails to be executed, check whether the environment variables configured in Step 2 are correct.  


## Invoking APIs<a name="section6542345219541"></a>

After environment variables are successfully configured, you can run manila commands to invoke the APIs provided by SFS. The command format is as follows:

```
manila <command> [arguments...]
```

You can run the  **manila help**  command to view all manila commands, and the  **manila help **_<Command\> _command to obtain help details of a specific command. The following uses the  **manila show**  command as an example.

```
root@n-version-client:~/ca# manila help show
usage: manila show <share>

Show details about a NAS share.

Positional arguments:
  <share>  Name or ID of the NAS share.
```

## **Return Value**<a name="section18278002204532"></a>

When running the  **manila <command\>**  command, if the correct command output is returned, or no exception appears during running the command, the execution of the command is normal. Take  **manila show**  as an example:

```
root@n-version-client:~/ca# manila show 416112b6-e5c9-4a46-8dd1-80749fc09336
+-----------------------------+-------------------------------------------------------------------------------+
| Property                    | Value                                                                         |
+-----------------------------+-------------------------------------------------------------------------------+
| status                      | available                                                                     |
| share_type_name             | default                                                                       |
| description                 | None                                                                          |
| availability_zone           | eu-de-01                                                                      |
| share_network_id            | None                                                                          |
| export_locations            |                                                                               |
|                             | path = sfs-nas1.eu-de.otc.t-systems.com:/share-cff11cb8                       |
|                             | id = 6014f802-7b74-4fb2-8436-a58c94f86e84                                     |
|                             | preferred = False                                                             |
| host                        | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe |
| access_rules_status         | active                                                                        |
| snapshot_id                 | None                                                                          |
| is_public                   | False                                                                         |
| task_state                  | None                                                                          |
| snapshot_support            | True                                                                          |
| id                          | 416112b6-e5c9-4a46-8dd1-80749fc09336                                          |
| size                        | 1                                                                             |
| name                        | sample1                                                                       |
| share_type                  | 500fcfac-357b-4f0f-beeb-240d09da4dab                                          |
| has_replicas                | False                                                                         |
| replication_type            | None                                                                          |
| created_at                  | 2017-10-24T13:27:55.936861                                                    |
| share_proto                 | NFS                                                                           |
| consistency_group_id        | None                                                                          |
| source_cgsnapshot_member_id | None                                                                          |
| project_id                  | 703fdd5a62c84cbfb1385c212881f695                                              |
| metadata                    | {u'share_used': u'0'}                                                         |
+-----------------------------+-------------------------------------------------------------------------------+
```

