Correct conversion
[copy_files] Filed copied: main_0_0.sql
[copy_files] Filed copied: main_0_1.sql
[exec_bash_compare] Command to run:
service mysql start > /dev/null 2>&1
timeout 30 bash -c 'service mysql start > /dev/null 2>&1'
[exec_bash_compare] Return code: 0
[exec_bash_compare] Student stdout:
[exec_bash_compare] Student stdout length: 0
[exec_bash_compare] Student stderr:
[exec_bash_compare] Student stderr length: 0
[exec_bash_compare] Desired stdout:
[exec_bash_compare] Desired stdout length: 0
[exec_bash_compare] Command to run:
/usr/bin/mysqladmin -u root -p"root" password "root" > /dev/null 2>&1
timeout 30 bash -c '/usr/bin/mysqladmin -u root -p"root" password "root" > /dev/null 2>&1'
[exec_bash_compare] Return code: 0
[exec_bash_compare] Student stdout:
[exec_bash_compare] Student stdout length: 0
[exec_bash_compare] Student stderr:
[exec_bash_compare] Student stderr length: 0
[exec_bash_compare] Desired stdout:
[exec_bash_compare] Desired stdout length: 0
[exec_bash_compare] Command to run:
cat main_0_0.sql | mysql -hlocalhost -uroot -proot > /dev/null 2>&1
timeout 30 bash -c 'cat main_0_0.sql | mysql -hlocalhost -uroot -proot > /dev/null 2>&1'
[exec_bash_compare] Return code: 0
[exec_bash_compare] Student stdout:
[exec_bash_compare] Student stdout length: 0
[exec_bash_compare] Student stderr:
[exec_bash_compare] Student stderr length: 0
[exec_bash_compare] Desired stdout:
[exec_bash_compare] Desired stdout length: 0
[exec_bash_compare] Command to run:
cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -proot 2>&1 | grep -v '''Using a password'''
timeout 30 bash -c 'cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -proot 2>&1 | grep -v '"'"''"'"''"'"'Using a password'"'"''"'"''"'"''
[exec_bash_compare] Return code: 0
[exec_bash_compare] Student stdout:
ERROR 1046 (3D000) at line 5: No database selected
[exec_bash_compare] Student stdout length: 51
[exec_bash_compare] Student stderr:
[exec_bash_compare] Student stderr length: 0
[exec_bash_compare] Desired stdout:
[exec_bash_compare] Desired stdout length: 0