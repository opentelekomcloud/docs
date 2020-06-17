# How Can I Install the PostgreSQL Client?<a name="rds_faq_0029"></a>

PostgreSQL provides  [client installation packages](https://yum.postgresql.org/)  and the required dynamic shared library packages for different OSs on its official website.

>![](/images/icon-notice.gif) **NOTICE:**   
>Ensure that the database client matches the DB engine version of your RDS PostgreSQL DB instances.  

This following uses latest  [PostgreSQL 9.5](https://yum.postgresql.org/9.5/redhat/rhel-6-x86_64/repoview/postgresqldbserver95.group.html)  in Red Hat Linux 6 as an example to describe how to obtain the required installation package and complete the installation.

## Procedure<a name="s7f42b10588bf490a89a0971f46cad43f"></a>

1.  Obtain the PostgreSQL client installation package.

    Find the  [link](https://yum.postgresql.org/9.5/redhat/rhel-6-x86_64/repoview/postgresql95.html)  to the required version on the download page. postgresql95 is used as an example in the following figure.

    **Figure  1**  Downloading the PostgreSQL client installation package<a name="f249a2b1150ba4c008cc9b389cb16b05d"></a>  
    ![](figures/downloading-the-postgresql-client-installation-package.png "downloading-the-postgresql-client-installation-package")

2.  Obtain the dynamic shared library package required for the PostgreSQL client.

    Find the  [link](https://yum.postgresql.org/9.5/redhat/rhel-6-x86_64/repoview/postgresql95-libs.html)  to the required version on the download page. postgresql95-libs is used as an example in the following figure.

    **Figure  2**  Downloading the dynamic shared library package<a name="fdef8c43a1fed4c118275430df63a90d4"></a>  
    ![](figures/downloading-the-dynamic-shared-library-package.png "downloading-the-dynamic-shared-library-package")

3.  Upload the installation and dynamic shared library packages to the ECS.

    >![](/images/icon-note.gif) **NOTE:**   
    >When you create an ECS, select an OS, such as Red Hat 6.6, and bind an EIP to it. Then, upload the installation and dynamic shared library packages to the ECS using a remote tool, and use PuTTY to connect to the ECS.  

4.  Run the following command to install the PostgreSQL client:

    ```
    sudo rpm -ivh postgresql95-9.5.7-1PGDG.rhel6.x86_64.rpm postgresql95-libs-9.5.7-1PGDG.rhel6.x86_64.rpm
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If any conflicts occur during the installation, add the  **replacefiles**  parameter to the command and try to install the client again. Example:  
    >    ```  
    >    rpm -ivh --replacefiles postgresql95-9.5.7-1PGDG.rhel6.x86_64.rpm postgresql95-libs-9.5.7-1PGDG.rhel6.x86_64.rpm  
    >    ```  
    >-   If a message is displayed prompting you to install a dependency package, you can add the  **nodeps**  parameter to the command and install the client again. Example:  
    >    ```  
    >    rpm -ivh --nodeps postgresql95-9.5.7-1PGDG.rhel6.x86_64.rpm postgresql95-libs-9.5.7-1PGDG.rhel6.x86_64.rpm  
    >    ```  


