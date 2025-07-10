# mmtech-exam
MediaMeter Back-End Developer Arambulo Technical Exam

--DB CREATION--
Open MySQLWorkbench and connect to your root localhost (or any existing mysql preferred server)

Choose between:
1. Query Version:
    - Copy and paste the text inside db-create.sql inside the query. If cannot be found, open click the Create a new SQL tab
        under the File button on the upper left corner.
2. Upload Version
    - under the edit button on the upper left corner, click the "Open a SQL Script" button, and open the db-create.sql

If both versions cannot be done, you can open the MySQL Shell and do the following
1. type /sql and press Enter
2. do Query Version that is stated above but input it in the shell.

--DB-CONNECTION--

- Currently the DB is default connected to "localhost" with port "3306" with username and password as "root" in order to change this, 
kindly add a .env file with adding the parameters of the following:

DB_HOST="preferred host name"
DB_PORT="preferred port"
DB_NAME=task_manager
DB_USER="preferred user"
DB_PASSWORD="preferred password"

Do not include the "" in adding the parameters to the .env

--RUN PROGRAM--
Click the taskManager.py and the code will not work.