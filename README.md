# load_aml
Proyecto de carga masiva de registros en SQL Server, con Python

# Consideraciones

> Python 3.7

## Configurar DSN

1. Instalar unixodbc & freetds
    ```shell
    brew update
    brew install unixodbc freetds
    ```
2. Editar archivo freetds.conf
    ```shell
    vi /usr/local/etc/freetds.conf
    ```
    Editar el host y puerto dentro del archivo:
    ```shell
    [MYMSSQL]
    host = mssqlhost.xyz.com
    port = 1433
    tds version = 7.3
    ```

3. Probar conexión
    ```shell
    tsql -S MYMSSQL -U myuser -P mypassword
    ```
    Si todo va bien debe ver lo siguiente:
    ```shell
    locale is "en_US.UTF-8"
    locale charset is "UTF-8"
    using default charset "UTF-8"
    1>
    ```

4. Editar los archivos odbcinst.ini y odbc.ini.
    1. Ejecutar `odbcinst.ini -j` para obtener la ubicacion de los archivos `odbcinst.ini` y `odbc.ini`.
    2. Editar el archivo `odbcinst.ini` para incluir lo siguiente:
        ```conf
        [FreeTDS]
        Description=FreeTDS Driver for Linux & MSSQL
        Driver=/usr/local/lib/libtdsodbc.so
        Setup=/usr/local/lib/libtdsodbc.so
        UsageCount=1
        ```
    3. Editar el archivo `odbc.ini` para incluir lo siguiente:
        ```conf
        [MYMSSQL]
        Description         = Test to SQLServer
        Driver              = FreeTDS
        Servername          = MYMSSQL
        ```

        Tener en cuenta que "Driver" es el nombre de la entrada en `odbcinst.ini` y "Servername" es el nombre de la entrada en `freetds.conf`.
    4. Probar la conexión:
        ```shell
        isql MYMSSQL myuser mypassword
        ```
        Si todo va bien se debe ver:
        ```shell
        +---------------------------------------+
        | Connected!                            |
        |                                       |
        | sql-statement                         |
        | help [tablename]                      |
        | quit                                  |
        |                                       |
        +---------------------------------------+
        ```
## Exportar variables de ambiente Username & Password
Exportar las variables de ambiente `AML_USERNAME` & `AML_PASSWORD`.
```shell
export AML_USERNAME=STP_USERNAME
export AML_PASSWORD=STP_PASSWORD
```