# Preparing a Driver for MySQL Database Link<a name="EN-US_TOPIC_0125375600"></a>

## Scenario<a name="s2a343d01599646768adbb1adeaefacd2"></a>

As a component for batch data export, Loader can import and export data using a relational database.

## Prerequisites<a name="s90c31966ac1c433b9e5efde799224add"></a>

You have prepared service data.

## Procedure<a name="s0df8d60e78e044c798e0e0f54d56a004"></a>

1.  Download the  **mysql-connector-java-5.1.21.jar**  MySQL JDBC driver from the MySQL official website.
2.  Upload  **mysql-connector-java-5.1.21.jar** to the Loader installation directory on active and standby MRS master nodes.
    -   In versions earlier than MRS 1.9.2, the path is  **/opt/Bigdata/FusionInsight/FusionInsight-Sqoop-1.99.7/FusionInsight-Sqoop-1.99.7/server/jdbc**
    -   For MRS 1.9.2 or later, the path is  **/opt/Bigdata/MRS\_XXX/install/FusionInsight-Sqoop-1.99.7/FusionInsight-Sqoop-1.99.7/server/jdbc**

        In which xxx indicates the MRS version.

3.  Change the owner of  **mysql-connector-java-5.1.21.jar** to **omm:wheel**.
4.  Modify the  **jdbc.properties**  configuration file.

    Change the key-value of  **MYSQL** to **mysql-connector-java-5.1.21.jar**, for example, MYSQL=mysql-connector-java-5.1.21.jar.

5.  Restart Loader.

