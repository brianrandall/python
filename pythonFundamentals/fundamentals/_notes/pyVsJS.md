```js
function add (a, b) {
    sum = (a + b);
    if (sum === 5) {
        return "i am not doing this"
    } 
    else if (sum === 8) {
        "i'm still not doing this"
    }
    else {
        return sum
    }
    return sum
}

console.log(sum(5, 6))
```

```py
def add(a, b):
    sum = a + b
    if sum == 5:
        return "i am not doing this"
    elif sum == 8:
        return "i'm still not doing this"
    else
        return sum

print(add(5,6))
```

## differences between js and python
- js
    - {} based
    - uses () for conditional statements
    - console.log to print
    - function
    - "else if"
    - ===


- py
    - indent based
    - does not use () for conditional statements
    - print
    - no ";"
    - def (for functions)
    - elif
    - ==

## DATA TYPES
- JS
    - numbers -> float, int -> 1, 2, 3, etc
    - strings -> "  "
    - boolean -> true, false
    - objects -> {
        key: value,
    }
    - arrays arr[1, 2, 3] -> index[arr[0]]
- PY
    - number
    - string
    - bool -> True, False (capital T/F!!)
    - dictionaries -> { 
        key: value pairs,
     }
    - lists -> [  ] -> index based 
    - tuples -> (  ) -> can't be changed
        - must make a copy in order to change contents
    