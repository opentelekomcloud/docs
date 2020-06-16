# Preparing the Bootstrap Action Script<a name="EN-US_TOPIC_0127245536"></a>

Currently, bootstrap actions support Linux shell scripts only. Script files must end with  **.sh**.

## Uploading the Installation Packages and Files to an OBS Bucket<a name="en-us_topic_0114229329_section83904734414"></a>

Before compiling a script, you need to upload all required installation packages, configuration packages, and relevant files to the OBS bucket in the same region. Because networks of different regions are isolated from each other, MRS VMs cannot download OBS files from other regions.

## Compiling a Script for Downloading Files from the OBS Bucket<a name="en-us_topic_0114229329_section0113103017196"></a>

You can specify the file to be downloaded from OBS in the script. If you upload files to a private bucket, you need to run the  **hadoop fs**  command to download the files. The following example shows that the  **s3a://yourbucket/myfile.tar.gz**  file will be downloaded to the local host and decompressed to the  **/your-dir**  directory.

```
#!/bin/bash
source /opt/client/bigdata_env;hadoop fs -Dfs.s3a.endpoint=<obs-endpoint> -Dfs.s3a.access.key=<your-ak> -Dfs.s3a.secret.key=<your-sk> -copyToLocal s3a://yourbucket/myfile.tar.gz ./
mkdir -p /<your-dir>
tar -zxvf myfile.tar.gz -C /<your-dir>
```

>![](/images/icon-note.gif) **NOTE:**   
>-   The Hadoop client has been preinstalled on the MRS node. You can run the  **hadoop fs**  command to download or upload data from or to OBS.  
>-   Obtain the obs-endpoint of each region. For details, see  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html).  
>-   [Sample Scripts](sample-scripts.md#EN-US_TOPIC_0127245539)  shows that the installation packages have been uploaded to the public readable OBS bucket. Therefore, you can run the  **curl**  command in the sample script to download the installation packages.  

## Uploading the Script to an OBS Bucket<a name="en-us_topic_0114229329_section1156312564207"></a>

After script compilation, upload the script to the OBS bucket in the same region. At the time you specify, each node in the cluster downloads the script from OBS and executes the script as user  **root**.

