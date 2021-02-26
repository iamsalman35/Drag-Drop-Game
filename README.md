# Drag-Drop-Game
A simple 'Drag&Drop' game to showcase the drag and drop functionalities in HTML5. The client-side was implemented using HTML, CSS and Javascript. The server-side was implemented using Javascript and Perl.

Project Demo : https://drive.google.com/file/d/1X1fdkMzpmoo_K54KVp0n4F4mKYbxFdxT/view?usp=sharing

This project was deployed on a local server(XAMPP).

Steps to configure your XAMPP (Windows)

1)Start the Apache Server, and the MYSQL database from the XAMPP Control Panel.

2)Create a database(name:project) in your localhost myphpadmin. Create three tables(franklin, michael, trevor) inside the 
database. In each of the tables, create two attributes, ID(Datatype : Varchar, Length : 20) and itemlist (Datatype : text)

3)Download the repository, go to c:/xampp/htdocs/, create a folder (Projects), and put all the files as well as the images folder in it.

4)Download strawberry perl, go to C:\Strawberry\c\bin and copy libmysql__.dll. Paste it in C:\xampp\perl\vendor\lib\auto\DBD\mysql

5)To play the game, open a we browser, type in localhost/index.html
