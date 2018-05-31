Omnicam Project - Build by Blink Technologies Pte Ltd

### Initiating git and adding remote repository

Create a new folder for your files. Change directory to the newly created folder.

Initialise git inside the folder. Do not add any other files inside this folder. Then add this repository as remote in your git settings:

```
git init
git remote add origin https://github.com/blinktechsg/omnicam.git
git fetch && git checkout master
```

You will be able to see all the files downloaded from the repository to your directory.

### Create migration files

Before using, you need to create a database with the name you named in settings.py. Once you created the database, do

```
python manage.py makemigrations device project utility
```

to create the migrations files needed to create the tables inside database. Then do 

```
python manage.py migrate
```

### Downloading necessary javascripts and CSS files from other repository.

Navigate to the directory (in blink folder) where **bower.json** is found

```
bower update
```

to download the files specified in the **bower.json**

You can then `python manage.py runserver` to view your webpage.