# TCP async
This is a simple implementation of asynchronous web server based on TCP socket programming.

I've coded it mostly to figure out how asynchronicity works under the hood.
## Structure
The web server is implemented in 4 ways (each file corresponds to its server type):

- base_server.py - synchronous server. Only one connection can be processed at time.
- async_server_selectsyscall.py - asynchronous server. Asynchronicity 
is achieved by using select() system call.
  
- async_server_threading.py - asynchronous server. Asynchronicity
is achieved by using threading Python module.
  
- async_server_generators.py - asynchronous server. Asynchronicity
is achieved by using Python generators and select() system call.
  
## Usage
Simply run a python file:
```code
python3 async_server_selectsyscall.py
```
The will run on localhost:8000 by default. You can interact with it using
any network tool that supports TCP connection, e.g. netcat:
```code
nc localhost 8000
```
Base (synchronous) server:

![base](https://github.com/desobolevsky/TCP_async/blob/master/demo/base.gif)

Asynchronous server (generators implementation):

![async](https://github.com/desobolevsky/TCP_async/blob/master/demo/async.gif)