# MenloHacks III Puzzle
This was a puzzle developed for MenloHacks III. It was not successfully solved, even after providing hints.
 
## Part 1
The first part of the puzzle contains the following 926128068, which is in epoch time. Going to an epoch time converter
online will tell you that this date is May 8, 1999. In order to continue, you need to know something about internet 
history. In 1999, pets.com was all the rage. If you go to the wayback machine, you can see what it looked like on May 8,
1999. On the page, you'll see "dog chews pack" for $8.29. Perfect! It's from Aspen pet products. Going to 
puzzle.menlohacks.com/aspen will get you to the next stage.

### 1. Base64 Text
The code `KDY4LCA0NTYp==` is encoded in base64. You can tell this by the double equal sign at the end of the encoding; this is a signal the encoding is base64, and actually isn’t even part of the encoding at all.  If you just search base64 decode online there are plenty of simple decoders that can decode this for you. It comes out to `(68, 456)`. In programming, this looks like what is typically referred to as a tuple. However, just seeing this, it’s hard to know what it means.

### 2. Resizing The Image

There is a long `1x31,008` pixel image located after the base64 on the first page. The image is indecipherable as is, but it can be decoded. You may notice that the two numbers above (68 and 456) multiply to 31,008. This is no coincidence. In one of the most common uses of a tuple, an image shape is being encoded. In this example, the image is `456x68` (in typical fashion, y is placed before x). Now, you just have to find a way to “squeeze” the original image into the new shape. Here’s how I did it, using the opencv and numpy libraries in python:
```
img = cv2.imread("puzzle_img_original.png")
```
Here’s img:
```
array([[[255, 255, 255]],

       [[255, 255, 255]],

       [[255, 255, 255]],

       ..., 
       [[255, 255, 255]],

       [[255, 255, 255]],

       [[255, 255, 255]]], dtype=uint8)
```
We notice here that opencv has interpreted this as an rgb image, so it’s cloned each value three times. I just took an arbitrary color:
```
channel = img[:,:,0]
```
Now we’re back to something like the original image:
```
array([[255],
       [255],
       [255],
       ..., 
       [255],
       [255],
       [255]], dtype=uint8)
```
Now, we have to do the real work. Opencv returns numpy arrays. Numpy has a function, reshape, that lets you do this:
```
reshaped = channel.reshape([68, 456])
```
Now, it’s reshaped!
```
array([[255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       ..., 
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255],
       [255, 255, 255, ..., 255, 255, 255]], dtype=uint8)
```
All we have to do is write the image:
```
cv2.imwrite(“new_image.png”, reshaped)
```

And here’s the image:


![Reshaped](/media/reshaped.png "Reshaped")

### 3. Enigma?
here’s also a third component of the first page. In the javascript console, you’ll see:
```
Wehrmacht - WALZENLAGE 1, 2, 4 - UMKEHRWALZE B - GRUNDSTELLUNG A, C, D - RINGSTELLUNG A, B, D - STECKERVERBINDUNGEN A-B, C-D
```

What is that about? If you’re like a lot of people, you looked this up and figured out it’s part of the enigma code. However, there’s no enigma on this page; best to remember this for later.

## Part 2
Now, we have a page that looks like this:

![Enigma](/media/Enigma.png "Enigma")

This step should be easy, provided you saw the enigma information on the previous step. If we just enter the configuration from the previous step into an online enigma decoder, you’ll get that it says this:
PUZZLEMENLOHACKSCOMTURINGISTHEBOMB
Enigma can only decode capital letters, so this makes sense. Let's go to the
 next page.

## Part 3

![Integrity](/media/Integrity.png "Integrity")

This one tripped up a lot of you. It’s fairly cryptic, and if you don’t know what it’s talking about, it’s hard to get. One thing I tried to do with this part of the puzzle is to make it easier for people who follow proper web dev protocols. Often, if you load a <script> tag in a page, you just put the src and not much else. However, if you’re loading from a cdn, it’s recommended to use SRI, which checks the code you’re getting with a cryptographic hash to make sure the file hasn’t been manipulated in transit. What does SRI stand for? Subresource Integrity. Let’s look for some of that on the page:

![Integrity Solution](/media/IntegritySolution.png "Integrity Solution")

Look! We found a tag with an integrity attribute! Let’s paste that into the address bar to see if it works:
puzzle.menlohacks.com/sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=

It worked!

## Part 4
The next page looks like this:

![Login](/media/Login.png "Login")

This looks like login credentials! Now, how do we use them? Well, remember the end goal of this is to send an announcement. Announcements are sent through live.menlohacks.com and the app. If you paid attention to my presentation, you’ll know that they both have the same backend: vivere. In the views.py for vivere, there’s an undocumented method that lets you post to /admin/announcements:

![Announcement Post](/media/announcementPost.png "Announcement Post")

Here’s a sample solution (I wrote this solution during MenloHacks so I didn’t test it for obvious reasons, but it should work):
```
$.ajax({

url: "https://api.menlohacks.com/admin/announcement",

contentType: 'application/json; charset=utf-8',

headers: {

"X-MenloHacks-Authorization": $.cookie("token") //your auth token for the account

},

data : JSON.stringify({

body: “I won the puzzle!”

}),

type: "POST",

});
```
And we’ve sent the announcement! That’s it! (Note that this will not work 
anymore, as we deleted the jason account).

Great job to Akshay for solving this puzzle!