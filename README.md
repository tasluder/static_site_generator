# static_site_generator
This project has a really cool premise: take a .md file and turn it into a static website automatically. However, the learning curve has been steep on this one! There is a cool axiom that a problem written down is a problem halved - thanks Kidlin - so I want to do some of my own documentation to make sure I know where my roadblocks are and work through them.

This will be broken down into the different segments that match what boot.dev has outlined - I'm not just copying and pasting what the websites say - I want to learn a bit more, so I'll be trying to put it in my own words.

## Chapter 1: Static Sites
### mod1: Build a Static Site Generator
This module explains what static sites do, and it only asks us to echo "bootdev cli is ready!"

Done.

### mod2: HTML
This module has us set up an HTML file and goes over some of the basics of HTML. I did a lot of frontend training... I agree... it's not for me. 

It also has us set up a new dir and use Python's built in [HTTP server](https://docs.python.org/3/library/http.server.html) to serve the contents of that directory. Cool!

Done.

### mod3: CSS
HTML makes sense to me... the tags the links... almost all of it. CSS? No. I hate it! I think the reason is because I'm not necessarily a super creative type in this fashion, so it's a struggle to make something pretty when it's so complicated to get there. I would much rather just have a basic website and *good* functionality instead of decent functionality and a pretty website.

We linked the CSS file we created to the HTML file and gave ourselves a basic design to our website.

Done.

### mod4: Markdown
A quick review of Markdown - I love it. Just a simple question to answer and we move on.

### mod5: Cheat Sheet
This goes over some of the basic formatting for both HTML and MD - a few good resources are given [markdownguide.org](https://www.markdownguide.org/cheat-sheet/) and [html element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

A quick question to answer and we're off. Done.

### mod6: Cheat Sheet
Another quick question to answer and we're done. Boom.

## Chapter 2: Nodes
This chapter has us dig in a bit more in some different ways.

### mod1: TextNode
This TextNode class that we're creating will serve as the in-between -- it's the plain text version of either the Markdown input or the HTML output (does this mean we could also go in reverse? maybe, right? Could I take an HTML file and turn it into a Markdown file? I would assume so, but that's getting carried away -- I'll start a to-do section and toss this down there).

This module had us do a couple of things:
1. Create a basic shell script to run our program - done.
2. Creae a new directory to house our code - done.
3. Create a .gitignore file - done.
4. Create the TextNode class:
    a little more to do on this one -- I had to create a clas that takes three parameters:
    1. ```self.text``` - the content within the node (node... I'm curious what this term is based in? Quick search found this: [Node](https://developer.mozilla.org/en-US/docs/Web/API/Node) -- references back to the DOM (and I only know about this because of what I've done previously working on frontend development) the lesson doesn't really cover this aspect and the new term threw me for a bit of a loop honestly.)
    2. ```self.text_type``` - what type of text the node is - this is how we will know to style the text (bold, italic, etc.)
    3. ```self.url``` - the url of the link or image if ```self.text_type``` is one of those two - it defaults to ```None```.
5. Create an ```__eq__``` method for the TextNode class that returns ```True``` if *all* parameters of two TextNode objects are equal.
6. Create a ```__repr__``` method that returns a string representation of the object (what's the difference between this choice and ```__str__```?)  

### mod2: TextNode Tests
OK - another steep curve here - unit testing. I understand what a test is supposed to do conceptually, but in practice this is the first time boot.dev has asked us to write a test.

This module has us using the ```self.assertEqual()``` method to verify that our new TextNode class works as expected. [Documentation](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual) tells me that this method ensures that the first and second arguments passed in are equal. If they are, the test passes, and if they aren't, the test fails. Now that I'm writing this readme.md up, I found an answer for a question I had... I wanted to make sure that I could find out if two objects are *not* equal... well, duh... that would be ```self.assertNotEqual()```, but that wasn't in the module. I may go back and add a test or two to make sure I know how this works.

I ran the tests and they worked - done.

### mod3: HTMLNode
This module has us create a class which represents HTML nodes. The constructor takes *up to* 4 attributes:
1. tag - a string that represents which HTML tag will be used as plain text letters
2. value - a string that represents what's actually inside of your tags
3. children - a list of HTMLNode objects which represent the children of this node (If this node is a div and there's a child p or ol/ul within it, the p, ol, ul will be represented in this list)
4. props - a dictionary of pairs representing the attributes of the tag - a link tag ```<a>``` willl have the key-value pair of ```{"href": "https://www.example.com"}``` to store the link - or it could be an image source for an ```<img>``` tag.

This module asks us to make the different attributes optional, and so we set them to defaults of (for example) ```tag = None```.

For this class, we created three methods to use with it:
1. to_html: this does nothing at the moment and instead only ```raise NotImplementedError("this method is not implemented yet.")```
2. props_to_html: this method returns a string that represents the HTML attributes that were passed in. props accepts a dictionary, so it takes a bit of indexing and organizing with f strings to make it work.
3. repr: this methods allows us to print the ```HTMLNode``` object to see all of it's input attributes.

Finally, we're asked to create tests for this new class. When we write tests we need to plug in example attributes to the class, create a new object, and predict what the result should be.

Done and done.

### mod4: LeafNode
This module is very similar to the previous one, but now we are creating a ```LeafNode```. This is a *type* of ```HTMLNode``` that represents a single HTML tag with no children. It's constructor will be slightly different from the ```HTMLNode``` class because it doesn't allow for children. A ```LeafNode``` is the terminus of a potential line of notes from ```HTMLNode```.

To create this node, we have to create a child class of the ```HTMLNode``` class. The constructor should **not** allow for children *and* the ```value``` data member is required. These two things make sense - we shouldn't allow for a leaf off of a leaf, and because it's the last possible tag, it should actually have something to print to the screen.

We just have to create one method here ```to_html()```. This method will take the value passed in and wrap it in the ```tag``` that is also provided. If there is no ```tag``` provided, the ```value``` should be returned as raw text.

Here are some examples:
```
LeafNode("p", "This is a paragraph of text.")
LeafNode("a", "Click me!", {"href": "https://www.google.com"})
```
The above should render as:
```
<p>This is a paragraph of text.</p>
<a href="https://www.google.com">Click me!</a>
```

In hindsight - it's nice to slow down a bit and see exactly where the attributes should go from the beginning instead of trying to make it do something else... I think I originally tried to have the attributes print as their own tags?! D'oh! It's fixed now.

We add some tests, and we're done!

### mod5: ParentNode
This module has us build the ```ParentNode``` -- these nodes will hold and nest the ```LeafNode```s from above. That means that this node class won't take a ```value``` argument and the ```children``` argument is *not* optional. It won't take values because it won't have its own content, just the content of the children which will be in it. It has to have children because it wouldn't be a parent element without the elements within it.

Creating the classes match the others with slight modifications. Done.

* Create the ```to_html()``` method:
1. If there is no ```tag``` provided, raise a ```ValueError```
2. If there are no ```children``` provided, raise a ```ValueError```
3. Else, it should return a string representing the HTML tag of the node *and its children*. We were asked to do this recursively (yay). To do this, we iterate over each of the children with the ```to_html()``` method, concatenate the results and insert those strings inside the opening and closing tags of the parent.
4. *note*: We were explicitly told that this doesn't have to look visually appealing, it just needs to be correct so that it can be interpreted correctly.

### mod6: TextNode to HTMLNode
This module takes a ```TextNode``` and concerts it to an ```HTMLNode``` - further, we will specify which *type* of node. These will be able to adjust to the following types and will end as a ```LeafNode```.

```
* text_type_text = "text" -- no tags, raw text
* text_type_bold = "bold" -- <b> tag + text
* text_type_italic = "italic" -- <i> tag + text
* text_type_code = "code" -- <code> tag + text
* text_type_link = "link" -- <a href= "example.com"> tag + text
* text_type_image = "image" <img src = "example.com" alt = "example alt text"> EMPTY STRING
```

This one is a little bit tricky - can't forget that the ```props``` value will hold the elements for the link and image types and that is passed in as a *dictionary* not a list.

Added some tests, and we're good to go!

## Chapter 3: Inline

### mod1: Split Delimiter
This module asks us to bolster the ```TextNode``` functionality a bit more -- rather than just model a ```TextNode```, we will need to be able to convert a raw string into a **list** of ```TextNode``` objects.

The example:
```
This is text with a **bolded** word
```
Converts to:
```
[
    TextNode("This is text with a ", "text"),
    TextNode("bolded", "bold"),
    TextNode(" word", "text"),
]
```

This module tells us to keep it simple and only support a single level of nesting when it comes to inline elements (no bold & anchor tags on the same line).

We will create a new function ``` def split_nodes_delimiter(old_nodes, delimiter, text_type):``` that accepts a string of text, the delimiter we'll use to break the string, and the type of text we expect bassed on the previous ```TextNode``` to ```HTMLNode``` functionality we created.

This is a weird one... when you build this function, the original list ```old_nodes``` needs to be a regular text_type, and then we define the type of text we're looking for in the function... I feel like there is a better way to write these two things out... for instance, could we pass in a string to the ```TextNode``` constructor, look for the delimiter, and then newly define the ```self.text_type``` based on the delimiter we find? Probably...

Regardless of extended functionality, I've written this code in and added tests -- done and done!

### mod2: Extract Links
OK - up next is using regex (regular expressions) to search for particular patterns in text strings that we'll need to extract. Notably: addresses for links in ```<a>``` tags and source links in ```<img>``` tags.

For my own sake - I am documenting this website as a tool to help navigate regex - [regexr](regexr.com).

This module assigns us to write two functions:
1. ```extract_markdown_images(text)``` -- given a raw string, we will use regex to extract the alt text for an image and the URL associated with the image. This should be a **list** of **tuples** that is returned. A list to accept more than one potential image, and in tuples to make sure that it is immutable and we don't accidentally put the wrong image links with the wrong alt text. Boot.dev gives us this expression to extract image alt text and their links: ```r"!\[(.*?)\]\((.*?)\)"``` plugging this in to regexr gives us this:
* the "!" character looks for the image alt text in Markdown
* then we begin to look for the text within the first bracket "["
* we close the bracket we opened with "]"
* then we do the same thing for parentheses "(" & ")" to find the link associated with the image

Now to build the function - we should use the ```re``` library from Python and use the ```re.findall()``` method to find expressions that match the above. It will return as a list, so I just have to place those items in their appropriate tuple and we'll be good to go. I'll place this in the textnode.py file since we're passing in the pre-HTML text here. After a bit of experimenting and reading the documentation, ```re.findall()``` automatically returns lists of tuples... nice. Initially I tried creating a new list and ```.append()```, but I think my code doesn't require that, so I tidied it up a bit.

2. ```extract_markdown_links(text)``` -- given a raw string, we will use regex to extract the anchor text and url. I think this is more or less the same exact thing, but we just need to adjust our ```re.findall()``` method to make sure we grab the correct items.

For this function, it's more or less the same exact thing, right? I'll just remove the exclamation point and it should do what I want. This won't account for the use of brackets otherwise... or parentheses, but neither does the original regex expression used.

Ok - it works the way I want it to. I'll add this to the test suite, and we'll be good to go. Tests pass!

### mod3: Split Images and Links
*I always read through the module once before writing these steps, and the final note from this module is that **this** is the most challenging step in this project - yay.*

This module asks us to write two new functions that are similar to our ```split_nodes_delimiter``` function, but our new funcs should put to use the regex extractions we just created. We will define:
1. ```def split_nodes_image(old_nodes)``` -- given a list of ```old_nodes``` this function will return a new list of ```TextNode```s that contain the ```text```, ```text_type```, and a ```url``` if provided - else ```url = None```.
The example provided below:
```
node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    text_type_text,
)
new_nodes = split_nodes_image([node])
```
**should yield:**
```
[
    TextNode("This is text with an ", text_type_text),
    TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
    TextNode(" and another ", text_type_text),
    TextNode(
        "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
    ),
]
```

We've been instructed that these two functions will be very similar to one another and will mimic what the previous ```split_nodes_delimiter``` did; however, these functions won't need a delimiter or text type because the ```old_nodes``` strings that are passed in will be specifically passed in to their appropriate function.

2. ```def split_nodes_link(old_nodes)``` -- 

### mod4: Text to TextNodes

## Chapter 4: Blocks

### mod1: Split Blocks

### mod2: Block Types

### mod3: Block to HTML

## Chapter 5: Website

### mod1: Copy Static

### mod2: Generate Page

### mod3: Generate Pages Recursively

### mod4: Submit The Link.

## To-Do:
* Finish the project... on step **14 / 23**.
* Can I take an HTML file and turn it into a Markdown file?
* Write a test that utilizes ```self.assertNotEqual()```
* Look for a way to have the ```TextNode``` constructor redefine it's own ```self.text_type``` property based on a delimiter it finds within the string passed to it.
* Part of good documentation also includes commenting on my code... I will need to parse my own code and comment it to make sure it is clear to read.