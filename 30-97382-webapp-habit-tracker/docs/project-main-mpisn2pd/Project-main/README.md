# COP4521-Project

Good Habit Tracker

Using MySql database as well as FastAPI swagger API documentation, redoc to manage and test API

starting instructions:

pull the repository: get clone.. whatever you want to use: 
  Personally i use software with a ui called GitKraken, it manages gitflow for you.

Then, cd to the directory and run:
  . venv/bin/activate (for linux/max)

or 

  venv\Scripts\activate (for windows)

Next: 
  pip3 install uvicorn pymysql sqalchemy fastapi pydantic

to run project api: 

python3 -m uvicorn main:app --reload

frontend:

you need to pull, then: 

npm global --install yarn

then inside of the habits.front dir
  First try: yarn install

  or if that yields an error

  yarn add @mui/material @emotion/react @emotion/styled

  and:

  yarn add @mui/material @mui/styled-engine-sc styled-components

cd habits.front

  yarn start

