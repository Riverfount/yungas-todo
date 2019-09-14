# yungas-todo

## This repository is a task todo for a tech test of Yungas

[![Build Status](https://travis-ci.org/Riverfount/yungas-todo.svg?branch=master)](https://travis-ci.org/Riverfount/yungas-todo)
[![codecov](https://codecov.io/gh/Riverfount/yungas-todo/branch/master/graph/badge.svg)](https://codecov.io/gh/Riverfount/yungas-todo)

## To Contribute

### For backend

1. Clone this project
1. Copy `contrib/env-sample` to `.env`, this last file needs to be into project's root
1. Execute `pipenv sync -d` to install all dependencies
1. Execute `pipen run pytest` to run all tests
1. That's it, you are ready to contribute to backend of the project

### For frontend

1. After Clone (the same step 1 above)
1. Create file .env.local at root of the project (/web) with the localhost of Django like this: `http://localhost:8000/api/v1`
1. Setup the project with the command: `npm install`
1. Compiles and hot-reloads for development with the command: `npm run serve`
1. That's it, you are ready to contribute to frontend of the project
