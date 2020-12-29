# Cheating Sheet

## Java Language
### heap
+ Min Heap: --> to keep the min element always on top, so you can access it in O(1).
```java
PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
```

+ Max Heap: --> to keep the max element always on top, the same order as above.
```java
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());

// equivalent to:
PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(new Comparator<Integer>() {
    @Override
    public int compare(Integer o1, Integer o2) {
        return - Integer.compare(o1, o2);
    }
});
```
+ Method
```java
maxHeap.add(E e);
maxHeap.offer(E e);
maxHeap.peek(); // retrieve but not delete
maxHeap.poll(); // retrieve and delete
maxHeap.remove(E e); // delete specified object
```

### stack and queue
#### Stack class
```java
Stack<Character> stack = new Stack<>();
stack.push(<E>);
stack.pop();
stack.peak();
```


#### deque
```java
ArrayDeque<Integer> deq = new ArrayDeque<Integer>();
```
+ as a stack:
```java
element = deq.pop();
deq.push(<E>);
```

+ as a queue:
|           |   First Element (Head)                        | Last Element (Tail)               |
|----       |   ----                                        | ----                              |
|           |   Throws exception        |   Special value   | Throws exception  | Special value |
|----       |   ----                    |   ----            | ----              | ----          |
| Insert    |   addFirst(e)             |   offerFirst(e)   | addLast(e)        | offerLast(e)  |
| Remove    | 	removeFirst()           |   pollFirst()	    | removeLast()	    | pollLast()    |
| Examine   | 	getFirst()	            |   peekFirst()	    | getLast()	        | peekLast()    |
```java
deq.peek(); // equivalent to deq.peekFirst()
deq.peekFirst();
deq.peekLast();
// This method differs from peek*() only in that 
// it throws an exception if this deque is empty.
deq.getFirst();
deq.getLast();

deq.add(E e);
deq.addFirst(E e);
deq.addLast(E e);

deq.remove();
deq.removeFirst(); // equivalent to deq.remove()
deq.removeLast();
```

### Collections
#### HashMap:
```java
See q146
public LinkedHashMap(int initialCapacity,
                     float loadFactor,
                     boolean accessOrder) {
    super(initialCapacity, loadFactor);
    this.accessOrder = accessOrder;
}

int initialCapacity：初始容量         
float loadFactor ： 客座率，默认0.75f
boolean accessOrder:  false： 基于插入顺序   true：基于访问顺序,
                    默认是false，基于插入顺序，改成true的话，输出的顺序可能会不同
```
也就是说：更新图时，
+ 如果需要按照插入顺序或者访问顺序保存，就使用LinkedHashMap;
+ 如果需要按照键值的顺序保存，就使用TreeMap
+ 如果什么都不需要，使用HashMap(效率高);

#### HashSet
 ```java
Set<> hashSet = new HashSet<>();
hashSet.contains();
hashSet.add();
hashSet.remove();
 ```