# YOUR BUCKET LIST!
#### Video Demo:  https://www.youtube.com/watch?v=NUsvtYJ29fs

#### Description:
The name of this project is **"Your Bucket List!"**

This is a WEB application that allows you to store multiple lists of your TO-DO things.
You have access to:
### Bucketlist - for things you want to do before you die,
### Watchlist - for storing names of films or searies that you wish to see,
### Readlist - for all the books that you want to read,
### Tasklist - for everyday tasks or projects, things that you want to keep track of.

----------

The application consists of five pages - four lists described above and the main mage, that also allows you to register new entries to any of the chosen list.

I have decided to use a Flask framework as taught in the lectures, so the main part of the app is written in Python. I used some of the ideas showed in CS50.
The app uses SQL database to store all of the entries in one table created as per below:

    CREATE TABLE bucketlist (
        id INTEGER,
        name TEXT,
        status TEXT, 
        type TEXT, 
        date TEXT,
        PRIMARY KEY(id)
    );

I have decided that instead of creating multiple tables (one per each list of to-dos), it will be better for scalability to create just one, and add a "type" column to the table, to allow distinguishing of entries. 
Based on the category chosen from the select menu upon registration of a new to-do, the SQL INSERT query is modified in a way that sets the "type" of an entry to one of the four available lists.

-----------
### The app consists of three actual html files: 

layout.html - for avoiding repeating the same code; 

index.html - for the main page where you can register new entries to your database;

bucketlist.html - the layout that is used by flask in app.py to generate each of four lists of things to do.

## Main page:
Write the name of your goal and choose the category from a list of four available types. Press "Add Your Goal" to add entry to the designated list.

## Bucketlist, Watchlist, Readlist, Tasklist:
These pages consist of a table, that is generated with a "for" loop on the entries selected from the SQL query. 
You can view your goals here.

The Date column shows you whether the task has been completed or not. When you click on "Set to DONE" button next to each entry, the Date will automatically change to todays date.
You can also "Set to NOT DONE" if you pressed the button by mistake, or you can delate the entry altogether if you decide that it should no longer be on the list.


#### The app has been mainly styled with Bootstrap framework with some retouches. 
#### The background photo has been taken from my personal archives - I took it near my hometown many years ago. It reminds me of my purpose in life and it inspires me to grow.
---
### Please, enjoy my first application!

----
#### April 30th 2022
#### Rivet M. Lorddom