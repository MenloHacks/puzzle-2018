# MenloHacks III Puzzle
This was a puzzle developed for MenloHacks III. It was not successfully solved, even after providing hints.
 
## Part 1
The first part of the puzzle contains the following 926128068, which is in epoch time. Going to an epoch time converter
online will tell you that this date is May 8, 1999. In order to continue, you need to know something about internet 
history. In 1999, pets.com was all the rage. If you go to the wayback machine, you can see what it looked like on May 8,
1999. On the page, you'll see "dog chews pack" for $8.29. Perfect! It's from Aspen pet products. Going to 
puzzle.menlohacks.com/aspen will get you to the next stage.

## Part 2
One going to that link, we find a page that contains only a single image, bishop.png. It looks pretty random, and that's because most of it is. However, there is order in it. In chess, a bishop moves diagonally, so it makes sense to check the diagonals. Here's how I did it:
```
import cv2
import numpy as np
img = cv2.imread("bishop.png")
print(np.diagonal(img))
```
The output is as follows:
```
array([[101, 120, 116, 114,  97,  99, 116, 101, 100, 116, 104, 101,  97,
        115,  99, 105, 105],
       [101, 120, 116, 114,  97,  99, 116, 101, 100, 116, 104, 101,  97,
        115,  99, 105, 105],
       [101, 120, 116, 114,  97,  99, 116, 101, 100, 116, 104, 101,  97,
        115,  99, 105, 105]], dtype=uint8)
```
Interestingly, most of the numbers are fairly close to each other. They're also in the range of lowercase alphabetical ascii codes. Plugging them into an ascii code converter gives you this:
extractedtheascii
Going to puzzle.menlohacks.com/extractedtheascii will get you to the next stage.

## Part 3
On that page, you'll see the following:
Apply yourself to this puzzle.
username: thomas
password
You need to figure out that you need to go to the application system (apply.menlohacks.com). Use the credentials thomas@menlohacks.com for the username and simply "password" as the password (as hinted).

## Part 3
On that page, you'll see the following:

Apply yourself to this puzzle.

username: thomas

password

You need to figure out that you need to go to the application system (apply.menlohacks.com). Use the credentials thomas@menlohacks.com for the username and simply "password" as the password (as hinted).

## Part 4
On the application system, you'll see my "forms." Here are the links to them:

https://cdn.filestackcontent.com/gL2wTCn7RQyx0i5JoAT3

https://cdn.filestackcontent.com/zxnk6uIMTnad54y8Y2Jp

By "tell everyone," the first "form" hints that you eventually need to make an announcement on our announcements system. The second "form" hints that it's necessary to look for other clues, along with just the forms, to solve the puzzle.

## Part 5

Whether you are looking for more clues or are trying to sabotage anyone else doing the puzzle, you might try to upload a form on top of one of the ones that is currently uploaded. If you do, you'll get a silent error in your console, with the following link: goo.gl/aNCX3A.

## Part 6

If you know that you need to make an announcement and you found the rickroll, you may already guess that you need to use the same login account, with the password being the stuff after the "v=" in the URL. OK, maybe you didn't get that. If you didn't, check the metadata of the second pdf. You'll see "clue:v=" (or something like that), which should tell you tell.

## Part 7
Now we have login credentials. How do we use them? This looks like login credentials! Now, how do we use them? Well, remember the end goal of this is to send an announcement. Announcements are sent through live.menlohacks.com and the app. If you paid attention to my presentation, you’ll know that they both have the same backend: vivere. In the views.py for vivere, there’s an undocumented method that lets you post to /admin/announcements:



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
anymore, as we removed the account).

