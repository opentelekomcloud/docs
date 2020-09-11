# Enabling or Adding a Software Repository<a name="sfs_01_0027"></a>

This section explains how to enable or add a software repository in CentOS, SUSE, and Ubuntu.

## CentOS<a name="section5187641210364"></a>

1.  Run the following command to check whether a software repository has been enabled.

    **yum repolist all**

    If  **status**  is  **disabled**, as shown in  [Figure 1](#fig50710110103819), no software repository has been enabled. Proceed to the next step.

    **Figure  1**  Checking software repositories<a name="fig50710110103819"></a>  
    ![](figures/checking-software-repositories.png "checking-software-repositories")

2.  Run the following command to enable a software repository. This step uses  **Public-OTC-CentOS-7-Base**  as an example.

    **yum-config-manager --enable Public-OTC-CentOS-7-Base**

    **Figure  2**  Enabling a software repository<a name="fig14720407104057"></a>  
    ![](figures/enabling-a-software-repository.png "enabling-a-software-repository")

3.  Run the following command to check whether the software repository described in step 2 has been enabled.

    **yum repolist all**

    If  **status**  is  **enabled**, as shown in  [Figure 3](#fig33842796104733), the software repository has been enabled.

    **Figure  3**  Checking whether the software repository has been enabled<a name="fig33842796104733"></a>  
    ![](figures/checking-whether-the-software-repository-has-been-enabled.png "checking-whether-the-software-repository-has-been-enabled")


## SUSE<a name="section2416343611520"></a>

1.  Run the following command to check whether a software repository has been enabled.

    **zypper lr**

    If no software repository is detected, as shown in  [Figure 4](#en-us_topic_0077171435_en-us_topic_0077171435_fig50710110103819), proceed to the next step.

    **Figure  4**  Checking software repositories<a name="en-us_topic_0077171435_en-us_topic_0077171435_fig50710110103819"></a>  
    ![](figures/checking-software-repositories-1.png "checking-software-repositories-1")

2.  Run the following command to add a software repository. This step uses  **opensuse12.2**  as an example.

    **zypper addrepo http://download.opensuse.org/distribution/12.2/repo/oss/ opensuse-main**

    **Figure  5**  Adding a software repository<a name="fig18983675112352"></a>  
    ![](figures/adding-a-software-repository.png "adding-a-software-repository")

3.  Run the following command to update and add software repositories.

    **zypper refresh**

    **Figure  6**  Updating and adding repositories<a name="fig1390229711259"></a>  
    ![](figures/updating-and-adding-repositories.png "updating-and-adding-repositories")

4.  Run the following command to check whether the software repository described in step 2 has been enabled.

    **zypper lr**

    If  **Enabled**  is  **Yes**, as shown in  [Figure 7](#en-us_topic_0077171435_en-us_topic_0077171435_fig33842796104733), the software repository has been enabled.

    **Figure  7**  Checking whether the software repository has been enabled<a name="en-us_topic_0077171435_en-us_topic_0077171435_fig33842796104733"></a>  
    ![](figures/checking-whether-the-software-repository-has-been-enabled-2.png "checking-whether-the-software-repository-has-been-enabled-2")


## Ubuntu<a name="section16938692113347"></a>

1.  Run the following command to add a software repository.

    **apt-add-repository http://archive.canonical.com/ubuntu**

    **Figure  8**  Adding a software repository<a name="en-us_topic_0077171435_en-us_topic_0077171435_fig18983675112352"></a>  
    ![](figures/adding-a-software-repository-3.png "adding-a-software-repository-3")

2.  Run the following command to update and add software repositories.

    **apt-get update**

    **Figure  9**  Updating and adding repositories<a name="en-us_topic_0077171435_en-us_topic_0077171435_fig1390229711259"></a>  
    ![](figures/updating-and-adding-repositories-4.png "updating-and-adding-repositories-4")


