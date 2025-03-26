## Usage

Get tasks:

```console
$ curl -X GET http://localhost:8000/tasks/
```

Create task:

```console
curl -X POST -H "Content-Type: application/json" -d '{"title": "Hello, World!", "description": "Optional"}' http://localhost:8000/tasks/
```

Mark task as completed:

```console
curl -X PUT http://localhost:8000/tasks/1?completed=1
```

Delete task:

```console
curl -X DELETE http://localhost:8000/tasks/1
```
