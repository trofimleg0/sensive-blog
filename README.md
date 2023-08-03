# Blog by Yuri Grigorievich

Yuri Grigorievich's blog about commercial success. I share tips on business, life and about raising children.

![Screenshots](screenshots/site.png)

## Launch

You will need Python version 3 to run the site.

Download the code from GitHub. Install the dependencies:

```sh
pip install -r requirements.txt
```

Create a SQLite database

```sh
python3 manage.py migrate
```

Start the development server

```
python3 manage.py runserver
```

## Environment variables

Some of the project settings come from environment variables. To define them, create a `.env` file next to `manage.py` and write the data there in this format: `VARIABLE=value`.

There are 3 variables available:
- `DEBUG` — debug mode. Set `True` to see debug information in case of an error.
- `SECRET_KEY` — project secret key
- `DATABASE_FILEPATH` — The full path to the SQLite database file, for example: `/home/user/schoolbase.sqlite3`
- `ALLOWED_HOSTS` — [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


## Project Goals

The code is written for educational purposes - for a course on Python and web development on the [Devman](https://dvmn.org).
