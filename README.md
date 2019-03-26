# Assignment: Hashtable

In this assignment, you'll create four primary classes: an abstract Hashtable superclass and three concrete subclasses of it.  The three subclasses define one additional method, `get_hash()`, which returns the hash key for the data type being supported.  You'll support three types of keys: strings, guids, and image bytes.  The three classes are as follows:

```
                Hashtable (abstract class)
                 /           |           \
                /            |            \
    StringHashtable    GuidHashtable    ImageHashtable
```

Our hashtable implementation only allows one value under a given key.  If a second value is added with an existing key, the previous value is removed.

## The Hash Function

Each of your subclasses will define the `get_hash()` method differently.  In all cases, it returns a number in the 0-9 range, which is the length of your bucket list (i.e. the index of the bucket the key will be assigned to).  In all cases, you do not have to process the entire contents of the hash function input values -- just process enough to get a uniform distribution.

Your hash should be stable for a given key, meaning that repeated calls with the same key will always return the same hash index.

* The StringHashtable should compute the index based on (some part of) the contents of the string.
* The GuidHashtable should compute the index based on (some part of) the given guid.  Each guid is composed of 40 charaters: 0-15 is the millisecond the guid was created, 16-23 is a counter that resets at a random number at each change in millisecond, and 24-39 is the IP address where the guid was created.
* The ImageHashtable should compute the index based on the given image bytes.  The parameter will be sent in as the filename of the graphic, but your method needs to open the image, read (some of) the bytes, and calculate the index based on the bytes of the image.

In each case, try to implement a clever, fast, effective hash function that will load your list of buckets as uniformly as possible.  Do not use the built-in hash functionality in Python or proven algorithms like `md5` or `sha`.  The logic needs to be your creation.

## Constructor

In your constructor, create a list of 10 buckets.  We're using a low number so debugging and printing is easier (it will load up fairly quickly).  Initialize each bucket as empty python list `[]`.

In other words, your buckets do not start with `null` values.  They start with 10 empty lists.  The following shows the structure of the `.buckets` variable:

```
.buckets[0] = [ ]
.buckets[1] = [ ]
.buckets[2] = [ ]
.buckets[3] = [ ]
.buckets[4] = [ ]
.buckets[5] = [ ]
.buckets[6] = [ ]
.buckets[7] = [ ]
.buckets[8] = [ ]
.buckets[9] = [ ]
```


## Methods

The methods you need to support are given below.  Note that the `get_hash()` method is abstract in the superclass.

```
Hashtable class:
    Constructor
    set(key, value)
    get(key)
    remove(key)
    get_hash(key)

StringHashtable class (Hashtable subclass):
    get_hash(key)

GuidHashtable class (Hashtable subclass):
    get_hash(key)

ImageHashtable class (Hashtable subclass):
    get_hash(key)

```


## Debug Printing

The `print(repr(th))` calls should help in debugging your code. The following is an example of the string hash table.

```
## Note that your loading will likely be different due to differences
## in how each of us implements the hash function.

  [0]  darkwinged fungus gnats
       huntsman spiders (golden huntsman)
       scorpions
       lynx spiders
  [1]  aphids
       hard scales
       cobweb spiders (black widow)
       cellar spiders
       crab spiders
  [2]  weevils/bark beetles
       seed bugs
       thrips
       camel spiders
  [3]  ants
       indian meal moth
       codling moth
       crevice weaving spiders
  [4]  longhorned/roundheaded wood borers
       ground beetles
       assassin bugs
       wolf spilycosidaeders
  [5]  sac spiders (yellow sac spider)
       woodlouse spider
       pseudoscorpions
  [6]  leaf beetles
       peach twig borer
       jumping spiders (bold jumper)
       ticks (rocky mt. wood tick)
  [7]  armyworms/cutworms
       clearwing moths
       funnel web spiders (hobo)
       eriophyid mites (blister/rust/gall mites)
  [8]  carpet/warehouse beetles
       millipedes
       flatheaded/metallic wood borer
       ground spiders
       soft ticks (poultry tick)
  [9]  white grubs
       web-spinning spider mites
       orb-weaving spiders (banded garden spider)

```



## Submitting the Assignment

Submit your code to the Grader at http://caplearning.net/.
