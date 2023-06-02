# Java Tips<!-- omit from toc -->

- [Convert an ArrayList containing Integer objects to primitive int\[\]](#convert-an-arraylist-containing-integer-objects-to-primitive-int)
- [Double colon operator `::` in Java 8](#double-colon-operator--in-java-8)
- [Difference between `>>>` and `>>`](#difference-between--and-)
- [Lambda Expression](#lambda-expression)

## [Convert an ArrayList containing Integer objects to primitive int[]](https://stackoverflow.com/questions/718554/how-to-convert-an-arraylist-containing-integers-to-primitive-int-array)

```java
// java-8
List<Integer> x =  new ArrayList<Integer>();
// option 1
int[] arr = list.stream().mapToInt(i -> i).toArray();
// option 2
int[] arr = list.stream().mapToInt(Integer::intValue).toArray();
// avoid null values
//.filter(Objects::nonNull) also works
int[] arr = list.stream().filter(i -> i != null).mapToInt(i -> i).toArray();
```

## [Double colon operator `::` in Java 8](https://stackoverflow.com/questions/20001427/double-colon-operator-in-java-8)

Usually, one would call the reduce method using Math.max(int, int) as follows:

```java
reduce(new IntBinaryOperator() {
    int applyAsInt(int left, int right) {
        return Math.max(left, right);
    }
});
```

That requires a lot of syntax for just calling `Math.max`. That's where lambda expressions come into play. Since Java 8 it is allowed to do the same thing in a much shorter way:

```java
reduce((int left, int right) -> Math.max(left, right));
```

How does this work? The java compiler "detects", that you want to implement a method that accepts two `int`s and returns one `int`. This is equivalent to the formal parameters of the one and only method of interface `IntBinaryOperator` (the parameter of method `reduce` you want to call). So the compiler does the rest for you - it just assumes you want to implement `IntBinaryOperator`.

But as `Math.max(int, int)` itself fulfills the formal requirements of `IntBinaryOperator`, it can be used directly. Because Java 7 does not have any syntax that allows a method itself to be passed as an argument (you can only pass method results, but never method references), the `::` syntax was introduced in Java 8 to reference methods:

```java
reduce(Math::max);
```

Note that this will be interpreted by the compiler, not by the JVM at runtime! Although it produces different bytecodes for all three code snippets, they are semantically equal, so the last two can be considered to be short (and probably more efficient) versions of the `IntBinaryOperator` implementation above.

## [Difference between `>>>` and `>>`](https://stackoverflow.com/questions/2811319/difference-between-and)

`>>` is arithmetic shift right, `>>>` is logical shift right.

In an arithmetic shift, the sign bit is extended to preserve the signedness of the number.

For example: -2 represented in 8 bits would be 11111110 (because the most significant bit has negative weight). Shifting it right one bit using arithmetic shift would give you 11111111, or -1. Logical right shift, however, does not care that the value could possibly represent a signed number; it simply moves everything to the right and fills in from the left with 0s. Shifting our -2 right one bit using logical shift would give 01111111.

## Lambda Expression

- [Are Java 8 Lambdas Closures?](https://www.bruceeckel.com/2015/10/17/are-java-8-lambdas-closures/)
- [Variable used in lambda expression should be final or effectively final](https://stackoverflow.com/questions/34865383/variable-used-in-lambda-expression-should-be-final-or-effectively-final)
