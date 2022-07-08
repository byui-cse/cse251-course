![](../site/banner.png)

# 11 Prepare: Java Threads

Most of this lesson will be going over Java program examples.  Please take the time to copy these examples to your computer and run them.

> If you don't have a Java compiler on your computer, you can create a free account at [replit.com.](www.replit.com) that will allow you to write, compile and run Java programs.


## How does Java run programs

A Java program is compiled into an executable.  That executable is made of bytes called Java Bytecode.  There is a Java Interpreter for each type of operating system - as you can see in the figure below.  Python has the same structure except Python programs are not compiled but interpreted when run.

We have other Object-oriented programming (OOP) languages such as Python, C++, C#, etc.  In the case of Java, everything (code) needs to be in a class.  For example, there are no global variables outside of classes.

![](overview.png)

Hello World in Java:

```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
```

## What is a Thread in Java

Java program has a main thread.  Just like PThreads, Java threads run in parallel where threads run on different CPUs.  In the quote below, system-level threads are also called kernel threads.

>In Java, threads are mapped to system-level threads which are operating system's resources. If you create threads uncontrollably, you may run out of these resources quickly.
>
>The context switching between threads is done by the operating system as well – in order to emulate parallelism. A simplistic view is that – the more threads you spawn, the less time each thread spends doing actual work.
>
>https://www.baeldung.com/thread-pool-java-and-guava


## Threading using a class

There are a few different ways you can use threads in Java.  The first method is to create a class that is sub-classed from the Java Thread class.  Here you override the `run()` method.  **Thread.currentThread().getId()** returns the id of the current thread.  These ids are random but not consistent for the life of the program while running.

```java
class MyThread extends Thread {  
    
    @Override
    public void run() {  
        System.out.println("thread is running..." + Thread.currentThread().getId());  
    }

}

// Main Class
class ThreadClassExample1 {
    public static void main(String[] args) {
        int threads = 4; 
        for (int i = 0; i < threads; i++) {
            MyThread object = new MyThread();
            object.start();
        }
    }
}
```

Output:

```
thread is running...13
thread is running...16
thread is running...15
thread is running...14
```

---
Example of a constructor in a threaded class where the name of the thread is an argument.

```java
class MyThread2 extends Thread {  

    MyThread2(String name) {
        // Consturctor: Pass the name to the parent class
        super(name);
    }
    
    @Override
    public void run() {  
        System.out.println("thread is running... " + getName());  
    }

}

// Main Class
class ThreadClassExample2 {
    public static void main(String[] args) {
        int threads = 4; 
        for (int i = 0; i < threads; i++) {
            String name = "name-" + i;
            MyThread2 object = new MyThread2(name);
            object.start();
        }
    }
}
```

Output:

```
thread is running... name-0
thread is running... name-3
thread is running... name-2
thread is running... name-1
```

## Threading using an interface

This is the preferred method of using threads in Java by using an interface to Runnable.  When you create a Runnable object, you can pass it to a new thread.

```java
// https://www.geeksforgeeks.org/multithreading-in-java/

class MultithreadingDemo implements Runnable {
    public void run() {
        try {
            // Displaying the thread that is running
            System.out.println("Thread " + Thread.currentThread().getId() + " is running");
        }
        catch (Exception e) {
            // Throwing an exception
            System.out.println("Exception is caught");
        }
    }
}
 
// Main Class
class Multithread {
    public static void main(String[] args) {
        int threads = 8;
        for (int i = 0; i < threads; i++) {
            Thread object = new Thread(new MultithreadingDemo());
            object.start();
        }
    }
}
```

Output:

```
Thread 13 is running
Thread 20 is running
Thread 17 is running
Thread 18 is running
Thread 19 is running
Thread 14 is running
Thread 15 is running
Thread 16 is running
```

## Thread Using Join()

Java also has a `join()` statement.  The difference with Java is that the join() function must be placed in a try/catch block.

```java
// https://www.geeksforgeeks.org/joining-threads-in-java
  
class ThreadJoining implements Runnable 
{ 
    public void run() { 
        for (int i = 0; i < 2; i++) { 
            try { 
                Thread.sleep(500); 
                System.out.println("Current Thread: " + Thread.currentThread().getName()); 
            } 
            catch(Exception ex) { 
                System.out.println("Exception has" + " been caught" + ex); 
            } 
        } 
    } 
} 
  
class ThreadJoinExample 
{ 
    public static void main (String[] args) 
    { 
        // creating two threads 
        Thread t1 = new Thread(new ThreadJoining()); 
        Thread t2 = new Thread(new ThreadJoining()); 
        Thread t3 = new Thread(new ThreadJoining()); 
  
        // thread t1 starts 
        t1.start(); 
        t2.start(); 
        t3.start(); 

        // The join() statements must be in a Try/Catch block

        try { 
            t1.join(); 
            t2.join(); 
            t3.join(); 
        } 
        catch(Exception ex) { 
            System.out.println("Exception has " + "been caught" + ex); 
        } 

        System.out.println("After all of the join() statements");
    } 
} 
```

Output:

```
Current Thread: Thread-2
Current Thread: Thread-1
Current Thread: Thread-0
Current Thread: Thread-1
Current Thread: Thread-0
Current Thread: Thread-2
After all of the join() statements
```

## Thread Pools

Java also has thread pools.

>The Thread Pool pattern helps to save resources in a multithreaded application, and also to contain the parallelism in certain predefined limits.
>
>When you use a thread pool, you write your concurrent code in the form of parallel tasks and submit them for execution to an instance of a thread pool. This instance controls several re-used threads for executing these tasks.
>
>https://www.baeldung.com/thread-pool-java-and-guava

```java
// https://www.geeksforgeeks.org/thread-pools-java/

import java.text.SimpleDateFormat;  
import java.util.Date; 
import java.util.concurrent.ExecutorService; 
import java.util.concurrent.Executors; 
  
// Task class to be executed (Step 1) 
class Task implements Runnable    
{ 
    private String name; 
      
    public Task(String s) { 
        name = s; 
    } 
      
    // Prints task name and sleeps for 1s 
    // This Whole process is repeated 5 times 
    public void run() { 
        try { 
            for (int i = 0; i < 3; i++) { 
                if (i == 0) { 
                    Date d = new Date(); 
                    SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss"); 
                    System.out.println("Initialization Time for"
                            + " task name - "+ name +" = " +ft.format(d));    
                    //prints the initialization time for every task  
                } 
                else { 
                    Date d = new Date(); 
                    SimpleDateFormat ft = new SimpleDateFormat("hh:mm:ss"); 
                    System.out.println("Executing Time for task name - "+ 
                            name +" = " +ft.format(d));    
                    // prints the execution time for every task  
                } 
                Thread.sleep(1000); 
            } 
            System.out.println(name+" complete"); 
        } 
          
        catch(InterruptedException e) { 
            e.printStackTrace(); 
        } 
    } 
} 

class TestPool
{ 
     // Maximum number of threads in thread pool 
    static final int MAX_T = 3;              
  
    public static void main(String[] args) { 
        // creates five tasks 
        Runnable r1 = new Task("task 1"); 
        Runnable r2 = new Task("task 2"); 
        Runnable r3 = new Task("task 3"); 
        Runnable r4 = new Task("task 4"); 
        Runnable r5 = new Task("task 5");       
          
        // creates a thread pool with MAX_T no. of  
        // threads as the fixed pool size(Step 2) 
        ExecutorService pool = Executors.newFixedThreadPool(MAX_T);   
         
        // passes the Task objects to the pool to execute (Step 3) 
        pool.execute(r1); 
        pool.execute(r2); 
        pool.execute(r3); 
        pool.execute(r4); 
        pool.execute(r5);  
          
        // pool shutdown ( Step 4) 
        pool.shutdown();     
    } 
} 
```

Output:

```
Initialization Time for task name - task 2 = 11:02:32
Initialization Time for task name - task 1 = 11:02:32
Initialization Time for task name - task 3 = 11:02:32
Executing Time for task name - task 3 = 11:02:33
Executing Time for task name - task 1 = 11:02:33
Executing Time for task name - task 2 = 11:02:33
Executing Time for task name - task 3 = 11:02:34
Executing Time for task name - task 1 = 11:02:34
Executing Time for task name - task 2 = 11:02:34
task 1 complete
task 3 complete
Initialization Time for task name - task 4 = 11:02:35
Initialization Time for task name - task 5 = 11:02:35
task 2 complete
Executing Time for task name - task 5 = 11:02:36
Executing Time for task name - task 4 = 11:02:36
Executing Time for task name - task 5 = 11:02:37
Executing Time for task name - task 4 = 11:02:37
task 5 complete
task 4 complete
```

## Lamda Threads

Python and Java has lamda functions.  Here are two different methods of using lamda functions with threads.

```java
class thread_lamda {

    public static void main(String[] args) {

        // Create a Runnable object and then create two threads to run that object.
        Runnable task = new Runnable() {
            @Override
            public void run() {
              System.out.println(Thread.currentThread().getName() + " is running");
            }
        };

        Thread thread1 = new Thread(task);
        Thread thread2 = new Thread(task);

        thread1.start();
        thread2.start();
        try {
            thread1.join();
            thread2.join();
        } 
        catch (Exception e) {
        }

        System.out.println("------------------------------------------------------");

        // Create a thread using a lamda function
        Thread t1 = new Thread(() -> {
            System.out.println(Thread.currentThread().getName() + " is running");
        });

        t1.start();
        try {
            t1.join();
        } 
        catch (Exception e) {
        }

    }
}
```

Output:

```
Thread-0 is running
Thread-1 is running
------------------------------------------------------
Thread-2 is running
```


## Bounded Buffer Problem

Here is the standard Bounded Buffer problem written in Java.  The producer and consumer are Runnable objects.

```java
// https://www.baeldung.com/java-blocking-queue

import java.util.concurrent.*;

class NumbersProducer implements Runnable {
    private BlockingQueue<Integer> numbersQueue;
    private final int poisonPill;
    private final int poisonPillPerProducer;
    private CyclicBarrier barrier;
    
    public NumbersProducer(BlockingQueue<Integer> numbersQueue, CyclicBarrier barrier, int poisonPill, int poisonPillPerProducer) {
        this.numbersQueue = numbersQueue;
        this.poisonPill = poisonPill;
        this.poisonPillPerProducer = poisonPillPerProducer;
        this.barrier = barrier;
    }

    public void run() {
        try {
            for (int i = 0; i < 100; i++) {
                int number = ThreadLocalRandom.current().nextInt(100);
                // System.out.println(Thread.currentThread().getName() + " ADDING: " + number);
                numbersQueue.put(number);
            }

            // Wait until all of the threads are finished.
            try {
                barrier.await();
            } catch (Exception e) {
            }

            // Send a mssage to the consumers that it is finished.
            for (int j = 0; j < poisonPillPerProducer; j++) {
                numbersQueue.put(poisonPill);
            }

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

    }
}


class NumbersConsumer implements Runnable {
    private BlockingQueue<Integer> queue;
    private final int poisonPill;
    
    public NumbersConsumer(BlockingQueue<Integer> queue, int poisonPill) {
        this.queue = queue;
        this.poisonPill = poisonPill;
    }
    public void run() {
        try {
            while (true) {
                Integer number = queue.take();
                if (number.equals(poisonPill)) {
                    return;
                }
                System.out.println(Thread.currentThread().getName() + " result: " + number);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

class bounded_buffer {

    public static void main(String[] args) {
        int BOUND = 10;
        int N_PRODUCERS = 4;
        int N_CONSUMERS = Runtime.getRuntime().availableProcessors();
        int poisonPill = Integer.MAX_VALUE;
        int poisonPillPerProducer = N_CONSUMERS / N_PRODUCERS;

        // Barrier for the producers
        CyclicBarrier barrier = new CyclicBarrier(N_PRODUCERS);

        // We need to keep track of all threads created
        Thread producers[] = new Thread[N_PRODUCERS];
        Thread consumers[] = new Thread[N_CONSUMERS];

        BlockingQueue<Integer> queue = new LinkedBlockingQueue<>(BOUND);

        for (int i = 0; i < N_PRODUCERS; i++) {
            producers[i] = new Thread(new NumbersProducer(queue, barrier, poisonPill, poisonPillPerProducer));
            producers[i].start();
        }

        for (int j = 0; j < N_CONSUMERS; j++) {
            consumers[j] = new Thread(new NumbersConsumer(queue, poisonPill));
            consumers[j].start();
        }

        // Wait for all of them to finish
        try {
            for (int i = 0; i < N_PRODUCERS; i++) {
                producers[i].join();
            }
    
            for (int j = 0; j < N_CONSUMERS; j++) {
                consumers[j].join();
            }
        } 
        catch (Exception e) {
        }
    }
}
```

Output (Only the first 20 lines):

```
Thread-6 result: 70
Thread-12 result: 39
Thread-10 result: 58
Thread-10 result: 66
Thread-11 result: 12
Thread-9 result: 84 
Thread-4 result: 85 
Thread-4 result: 86 
Thread-4 result: 43 
Thread-4 result: 26 
Thread-7 result: 7  
Thread-8 result: 67 
Thread-5 result: 22 
Thread-8 result: 91 
Thread-7 result: 43 
Thread-4 result: 42 
Thread-9 result: 26 
Thread-11 result: 34
Thread-10 result: 46
Thread-10 result: 92
```

## Thread Priorities

I just wanted to mention that Java Threads have priorities where you can assign which threads you would like to run more on the computer.

>Every Java thread has a priority that helps the operating system determine the order in which threads are scheduled.
>
>Java thread priorities are in the range between MIN_PRIORITY (a constant of 1) and MAX_PRIORITY (a constant of 10). By default, every thread is given priority NORM_PRIORITY (a constant of 5).
>
>Threads with higher priority are more important to a program and should be allocated processor time before lower-priority threads. However, thread priorities cannot guarantee the order in which threads execute and are very much platform dependent.
>
>https://www.tutorialspoint.com/java/java_multithreading.htm


## Thread Locks

In Java there are Locks and Synchronization.  Here is a [good article](https://winterbe.com/posts/2015/04/30/java8-concurrency-tutorial-synchronized-locks-examples/) on the differences. 


## Misc

In the Java world, there is open source project called `Project Loom` that is trying to see if they can create real light weight threads called `fibers`.  [Website](https://wiki.openjdk.java.net/display/loom/Main)

## Links

- https://www.tutorialspoint.com/java/java_multithreading.htm
- https://www.javatpoint.com/java-thread-pool
- https://www.geeksforgeeks.org/joining-threads-in-java/#:~:text=Related%20Articles&text=java.,another%20thread%20completes%20its%20execution.
- http://tutorials.jenkov.com/java-concurrency/creating-and-starting-threads.html#:~:text=A%20Java%20Thread%20is%20like,VM%20to%20run%20your%20application.
- https://www.youtube.com/watch?v=eQk5AWcTS8w
