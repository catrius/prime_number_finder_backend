# Previous Prime Number Backend


[![CircleCI](https://circleci.com/gh/catrius/prime_number_finder_backend.svg?style=svg)](https://app.circleci.com/pipelines/github/catrius/prime_number_finder_backend)
[![codecov](https://codecov.io/gh/catrius/catrius_blog_backend/branch/develop/graph/badge.svg?token=LMYKDU47UL)](https://codecov.io/gh/catrius/catrius_blog_backend)

## Stack

- Python >= 3.7
- Postgresql >= 12.3
- CircleCI
- CodeCov
- ElasticBeanstalk

### Websites
    - Backend: https://api-previous-prime-number.catri.us/
    - Frontend: https://previous-prime-number.catri.us/

### Deployment
- The deploy runs automatically on Master branch after it passes all tests or CircleCI. Or it can be done it manually by running `eb deploy`.
    
### Environment variables

+ Set up environment variables in `.env` file, which can be cloned from `.env.sample`

### Development

Use [**poetry**](https://python-poetry.org/docs/) to manage development environment

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
poetry shell
poetry install
```

Remember to migrate the database
```bash
python manage.py migrate
```

Finally start the server with
```bash
python manage.py runserver
```

### Testing

```bash
flake8
coverage run manage.py test && coverage report
```

