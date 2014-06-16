Goo.IM
======

API Requirements
----------------

API Requires a superuser in Django's user database named 'dbadmin' -- password can be set blank, but user must be set
as a superuser, or backend authentication will fail.

MYSQL
-----

Database should be created with the following command.

    CREATE DATABASE name DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_unicode_ci;

After first syncdb:

    ALTER TABLE files ADD FULLTEXT(filename, description);

