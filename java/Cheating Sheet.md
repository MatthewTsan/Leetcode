# Cheating Sheet

## Java Language

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