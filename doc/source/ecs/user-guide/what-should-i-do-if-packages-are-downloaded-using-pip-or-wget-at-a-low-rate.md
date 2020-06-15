# What Should I Do If Packages Are Downloaded Using PIP or wget at a Low Rate?<a name="EN-US_TOPIC_0107490388"></a>

## Symptom<a name="section4323119112812"></a>

When a user runs the wget command to download software packages, the download rate is far less than the bandwidth.

**Figure  1**  wget-based package downloading<a name="fig17394493307"></a>  
![](figures/wget-based-package-downloading.png "wget-based-package-downloading")

## Possible Causes<a name="section16898143618318"></a>

The official PIP website is accessed using HTTPS. Each time PIP is used to install a third-party Python module, the source code package must be downloaded at the official PIP website. Therefore, openssl packages are required.

## Solution<a name="section2477445336"></a>

Run the following command to install openssl packages:

**yum install openssl openssl-devel**

