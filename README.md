# otostr

# ⚠️ Totally a work in progress, working on it ⚠️

## The promise

Simplify your workflow: automate the boring part of writing unit tests. Just focus on the edge cases, but be lazy.

Does your Python package have one or a few entry points? Do you find yourself debugging your code works by throwing examples to these entry points, and checking if the result makes sense? Do you have to write unit tests?

That's perfect, just continue doing what you are doing. Put your debugging code in `tests/toast.py` and just run `otostr`.

`otostr` is smart, it will:
    * Track all the methods that your debugging code requires to be executed.
    * Whether or not these methods qualify as a unit, and require to be unit-tested [TODO]. (For example, `_private_methods` are not eligible, but you can change that!)
    * The context in which unit-methods are run (i.e. their state), what arguments they are called with, what their return value is and what their side effects are [TODO] (i.e. whether or not they affect their state)
    * It writes human-readable `test_module.py` files, compatible with `pytest` and `coverage` [TODO].
        * Each test case will contain examples based on *real data* (none of that random stuff), coming from your examples in the debug code. 
        * All the mocking will be done for you: don't you worry about external calls; we'll take care of that, so you can run your test suite offline.
    * It will output the coverage percentage of this unit test suite [TODO].
        * Not happy with the coverage %? Just add more examples in your debug code in `tests/toast.py`.

Behind the scenes, `otostr` caches all the examples it has found. So even if you remove an example from your debug code, `otostr` will remember it [TODO]. Don't want that? Just run `otostr clear`[TODO]. 

# Why this is good

When starting a new project, it's undoubtedly good practice to write your unit tests *first*. This is called test-driven develpment (TDD). It's undoubtedly common practice to start working on the fun part first, and write the tests at the end. Unless you are weird like that, you probably see writing tests as a chore.

`otostr` can be run at any stage of your project, and while it can't do TDD for you, it helps to write tests *while* you are writing your code. It gives a turbo boost to whatever debugging activity you are *already* doing, and at the end you get a unit test suite that's *almost* complete.

Why *almost*? While `otostr` can help you achieve a 100% coverage seamleslly, you should not stop there. Your units are only tested with examples that you have thought of in your debugger code, but unit testing done *well* should also include examples that you or someone *might* throw at your units at some point, maybe in years. (i.e. what happens if method `foo` is called with `None` as a parameter? what happens if I feed a negative number to my `fibonacci` function?)

However, the structure of your unit testing suite is already done for you. You can focus on the tricky (and more rewarding!!) part of unit testing: thinking about the edge cases.

So while `otostr` can't replace TDD it can bring back many of its benefits, while allowing you to be as lazy as possible.

## FYI
* Free software: MIT license
* Documentation: https://otostr.readthedocs.io.
