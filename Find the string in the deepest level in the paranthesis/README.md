    INPUT            -> OUTPUT
    "ab(c(d)e)"      ->  "d"
    "[a{{b}c}d(e)]"  ->  "b"
    "((a)b(cd)ef)"    ->  "a", "cd"
    "(ab[]c){d{e}}"  ->  "", "e"
    "Hello, World!"  ->  "Hello, World!"