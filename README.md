# Bookmarks

In this repository you will find the test carried out to enter, as a python developer, the company Keeper Solutions.

First it is necessary to clone the project: "git clone https://github.com/jean0123/Bookmarks.git".

After the project has been cloned, a virtual environment must be created. When created, the following command must be run to install the dependencies: "pip install -r requirements.txt".

At the end of the installation of the dependencies, it is necessary to run the command "python manage.py migrate" so that the respective migrations are installed in the database.

Finally you can run the project with "python manage.py runserver".

They can enter the Django admin, either as common users or as administrators. The administrator will be able to see all the bookmarks and common users will only be able to see their own bookmarks.

A group of permissions was created, assigned to a role, so that common users do not have access to any component of the system that you do not want to enable to everyone.

To test the endpoints, please copy and paste the respective commands found in the "Test_endpoints" file.
