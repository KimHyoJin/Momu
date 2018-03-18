#READ ME

### Environment Setting

#### MySQL

'''
sudo apt-get install build-essential
sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev
sudo service mysql start
mysql -u root -p
>> CREATE DATABASE momudb;
'''

#### Django

'''
python3 -m venv venv

. venv/bin/activate

pip install --upgrade pip
pip install django
pip install djangorestframework
pip install mysqlclient
'''