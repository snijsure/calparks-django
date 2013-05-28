
By default settigns in this project assume you have mySQL database available.
Also the setting assume that there is user call calparks for the database.

Here is how you create such user  and set its password to be calparks25

mysql -u root -p'XXXXX'
drop user calparks@localhost;
drop user calparks@'%';
CREATE USER 'calparks'@'localhost' IDENTIFIED BY PASSWORD '*5A9D6BBBAB0AA6252D20D119A6F2CAA8BF7A3FDD';
CREATE USER 'calparks'@'%' IDENTIFIED BY PASSWORD '*5A9D6BBBAB0AA6252D20D119A6F2CAA8BF7A3FDD';
grant all privileges on *.* to calparks@localhost with grant option;
grant all privileges on *.* to calparks@'%' with grant option;
create database calparks character set utf8;
# Now login to system as to make sure everything is setup correctly.
mysql -u calparks -p'calparks25' -D calparks

GRANT ALL PRIVILEGES ON *.* TO 'calparks'@'localhost' IDENTIFIED BY 'calparks' REQUIRE SSL;


Once you have setup the databaee correctly execute following commands:

python manage.py schemamigration calparks --initial
python manage.py syncdb
python manage.py migrate


ALTER TABLE calparks_userrecommendations alter column user_rating set DEFAULT 0;
