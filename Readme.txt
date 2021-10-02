Python Developer Machine Test Question
======================================

1) Create python environment and install requirement from "requirement.txt" file.
2) Create database by name "admaren_test"
3) Mingrate models by running "python manage.py migrate"
4) Run project.


Authentication API
==================

1) Login API:
    URL:     http://localhost:8000/user/login/
    Method:  POST
    Payload: {"username": "", "password": ""}
    (copy token for refresh)

2) Refresh API:
    URL:     http://localhost:8000/user/refresh/
    Method:  POST
    Payload: {"token": ""}


CRUD APIs:
==========

1) Overview API (total count, listing):
    URL:     http://localhost:8000/snippet/snippet/
    Method:  GET
    NOTE: Default showing all available snippets with a hyperlink to respective detail APIs.
    Click on "Extra Actions" for get total number of snippet.

2) Create API:
    URL:     http://localhost:8000/snippet/snippet/
    Method:  POST
    Payload: {"tag_title": "","content": ""}

3) Detail API:
    URL:     http://localhost:8000/snippet/snippet/1/
    Method:  GET
    NOTE: You have to pass snippet id through URL.

4) Update API:
    URL:     http://localhost:8000/snippet/snippet/1/
    Method:  PUT/PATCH
    Payload: {"tag_title": "", "content": ""}
    NOTE: You have to pass snippet id through URL.

5) Delete API:
    URL:     http://localhost:8000/snippet/snippet/1/
    Method:  DELETE
    NOTE: You have to pass snippet id through URL.

6) Tag list API:
    URL:     http://localhost:8000/snippet/tag/
    Method:  GET

7) Tag Detail API:
    URL:     http://localhost:8000/snippet/tag/1/
    Method:  GET
    NOTE: You have to pass snippet id through URL.
