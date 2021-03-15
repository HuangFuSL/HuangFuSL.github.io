# Python关闭线程

使用`PyThreadState_SetAsyncExc`函数在子线程中引发异常，从而使线程提前结束。

示例代码如下：

```python
import threading 
import ctypes 
import time 
   
class thread_with_exception(threading.Thread): 
    def __init__(self, name): 
        threading.Thread.__init__(self) 
        self.name = name 
              
    def run(self): 
  
        # target function of the thread class 
        try: 
            while True: 
                print('running ' + self.name) 
        finally: 
            print('ended') 
           
    def get_id(self): 
  
        # returns id of the respective thread 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id
   
    def raise_exception(self): 
        thread_id = self.get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 
       
t1 = thread_with_exception('Thread 1') 
t1.start() 
time.sleep(2) 
t1.raise_exception() 
t1.join() 
```

把`run()`中执行的操作以参数的形式传递：

```python
class KillableThread(threading.Thread):
    """
    A thread class extending threading.Thread, provides a kill() method to stop the thread and a getResult() method to get the return value of the thread.
    """

    def __init__(self, func: Callable, *args, **kwargs):
        super().__init__()
        self.func: Callable = func
        self.funcArg: dict = kwargs
        self.funcTup: Tuple = args
        self.result: Any = None
        self.exception: Any = None

    def run(self):
        """
        Executes the function here
        """
        try:
            self.result = self.func(*self.funcTup, **self.funcArg)
        except BaseException as e:
            self.exception = e

    def get_id(self):
        """
        Get the id of the thread
        """
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def kill(self):
        """
        Stops the thread
        """
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

    def getResult(self):
        if self.exception is None:
            return self.result
        else:
            raise self.exception
```

来源：[https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread](https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/)