import mysql.connector
try:
    conn=mysql.connector.connect(user='root', password='simrankaurkhaira1467', host='localhost')
    mycursor=conn.cursor()
    mycursor.execute("CREATE DATABASE python")
    mycursor.execute("USE python")
    mycursor("""CREATE TABLE Book
    (
    bookid int primary key not null,
    titleid int,
    location varchar(30),
    genre varchar(30)
    )""")
    mycursor("""CREATE TABLE Titles
    (
    titleid int primary key not null,
    title varchar(30),
    isbn int,
    publisherid int,
    publicationyear int
    )""")
    mycursor("""CREATE TABLE Publishers
    (
    publisherid int primary key not null ,
    name varchar(30),
    streetaddress varchar(40),
    suitenumber int,
    zipcodeid int
    )""")
    mycursor("""CREATE TABLE ZipCodes
        (
        zipcodeid int primary key not null,
        city varchar(10),
        state varchar(10),
        zipcode int
        )""")
    mycursor("""CREATE TABLE Authorstitles
        (
        authortitleid int primary key not null,
        authorid int,
        title int
        )""")
    mycursor("""CREATE TABLE Authors
        (
        authorid int primary key not null,
        firstname varchar(10),
        middlename varchar(10),
        lastname varchar(10)
        )""")
    print("SHOW TABLES")
    print(mycursor.fetchall())

    insert_into_books=''' INSERT INTO Book(bookid,titleid,location,genre) VALUES(1,12,'dehradun','dramatic')'''
    insert_into_titles = ''' INSERT INTO Titles(titleid,title,isbn,publicationid,publicationyear) VALUES(12,'anytitle',12345,2013)'''
    insert_into_publishers=''' INSERT INTO Publishers(publisherid,name,streetaddress,suitenumber,zipcodeid) VALUES(12345,'hemant','old dalanwala',193,2)'''
    insert_into_zipcodes = ''' INSERT INTO ZipCodes(zipcodeid,city,state,zipcode) VALUES(2,'dehradun','uttarakhand',248001')'''
    insert_into_authortitles = ''' INSERT INTO Authortitles(authortitleid,authorid,title) VALUES(123,1,'abc')'''
    insert_into_authors = ''' INSERT INTO Authors(authorid,firstname,middlename,lastname) VALUES(1,'chetan','bhagat','singh')'''

    select_query_books='''SELECT * FROM Books'''
    select_query_titles = '''SELECT * FROM Titles'''
    select_query_publishers = '''SELECT * FROM Publishers'''
    select_query_zipcodes = '''SELECT * FROM ZipCodes'''
    select_query_authortitles = '''SELECT * FROM Authorstitles'''
    select_query_authors = '''SELECT * FROM Authors'''

    #inserting data into tables and
    print(mycursor.execute(insert_into_books))
    print(mycursor.execute(select_query_books))
    print(mycursor.fetchall())
    print(mycursor.execute(insert_into_titles))
    print(mycursor.execute(select_query_titles))
    print(mycursor.fetchall())
    print(mycursor.execute(insert_into_publishers))
    print(mycursor.execute(select_query_publishers))
    print(mycursor.fetchall())
    print(mycursor.execute(insert_into_zipcodes))
    print(mycursor.execute(select_query_zipcodes))
    print(mycursor.fetchall())
    print(mycursor.execute(insert_into_authortitles))
    print(mycursor.execute(select_query_authortitles))
    print(mycursor.fetchall())
    print(mycursor.execute(insert_into_authors))
    print(mycursor.execute(select_query_authors))
    print(mycursor.fetchall())

    update_query_books='''UPDATE Book SET location='raipur' where id=1'''
    print(mycursor.execute(update_query_books))
    mycursor.commit()
except:
    print("could not connect...")