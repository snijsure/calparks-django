
Theme used in this web site is from:
http://usman.it/free-responsive-admin-template/


-------------------------

        mysql -u root -p'sigsense'
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


        python manage.py schemamigration calparks --initial
        python manage.py syncdb
        python manage.py migrate
        ALTER TABLE calparks_userrecommendations alter column user_rating set DEFAULT 0;

