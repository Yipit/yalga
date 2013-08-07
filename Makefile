db:
	echo "drop database lunchgameapp" | mysql -uroot
	echo "create database lunchgameapp" | mysql -uroot
	python manage.py syncdb --noinput
