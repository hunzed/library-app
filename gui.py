import tkinter
import pickle
from bookdataset import*
auser = Bookdataset()
class MyGUI:
    def __init__(self):
        #BASIC BUILDER
        self.main_window = tkinter.Tk()
        self.main_window.title ("CMPS 151 Students Book Review")
        self.topframe = tkinter.Frame(self.main_window)
        self.login = tkinter.Button(self.topframe, text='Login', command = self.loginwindow)
        self.login.pack(side = "left")
        self.adduser = tkinter.Button(self.topframe, text='Add User', state=tkinter.DISABLED)
        self.adduser.pack(side = "left")
        self.searchuser = tkinter.Button(self.topframe, text="Search Users", state=tkinter.DISABLED)
        self.searchuser.pack(side = "left")
        self.addbook = tkinter.Button(self.topframe, text="Add Book", state=tkinter.DISABLED)
        self.addbook.pack(side = "left")
        self.searchbook = tkinter.Button(self.topframe, text="Search Books", state=tkinter.DISABLED)
        self.searchbook.pack(side = "left")
        self.sortbook = tkinter.Button(self.topframe, text="Sort Books", state=tkinter.DISABLED)
        self.sortbook.pack(side = "left")
        self.quit = tkinter.Button(self.topframe, text="Quit", command= self.main_window.destroy)
        self.quit.pack(side = "left")
        self.topframe.pack(side = "top")
    ####top frame after log in
        self.loggedinframe = tkinter.Frame(self.main_window)
        self.login = tkinter.Button(self.loggedinframe, text='Logout', command= self.logout)
        self.login.pack(side = "left")
        self.adduser = tkinter.Button(self.loggedinframe, text='Add User', command = self.adduserfunction)
        self.adduser.pack(side = "left")
        self.searchuser = tkinter.Button(self.loggedinframe, text="Search Users", command = self.searchuserfunction)
        self.searchuser.pack(side = "left")
        self.addbook = tkinter.Button(self.loggedinframe, text="Add Book", command= self.addbookfunction)
        self.addbook.pack(side = "left")
        self.searchbook = tkinter.Button(self.loggedinframe, text="Search Books", command= self.searchbooksfunction)
        self.searchbook.pack(side = "left")
        self.sortbook = tkinter.Button(self.loggedinframe, text="Sort Books", command= self.sortbooksfunction)
        self.sortbook.pack(side = "left")
        self.quit = tkinter.Button(self.loggedinframe, text="Quit", command= self.main_window.destroy)
        self.quit.pack(side = "left")
        self.allframes = []
        #mainloop
        tkinter.mainloop()
    ###login
    def loginwindow (self):
        try:
            self.loginframeusername.destroy()
            self.loginframepassword.destroy()
            self.loginframetoploginbutton.destroy()
        except:
            pass
        self.loginframeusername = tkinter.Frame(self.main_window)
        self.loginusernamelabel = tkinter.Label(self.loginframeusername, text = "Username")
        self.loginusernamelabel.pack(side = "left")
        self.loginusernameentry = tkinter.Entry(self.loginframeusername)
        self.loginusernameentry.pack(side = "left")
        self.loginframeusername.pack(side = "top")
        self.loginframeusername.forget()
        #GETS PASSWORD
        self.loginframepassword = tkinter.Frame(self.main_window)
        self.loginpasswordlabel = tkinter.Label(self.loginframepassword, text = "Password")
        self.loginpasswordlabel.pack(side = "left")
        self.loginpasswordentry = tkinter.Entry(self.loginframepassword)
        self.loginpasswordentry.pack(side = "left")
        self.loginframepassword.pack(side = "top")
        self.loginframepassword.forget()
        #BUTTONFORLOGIN
        self.loginframetoploginbutton = tkinter.Frame(self.main_window)
        self.loginbutton = tkinter.Button(self.loginframetoploginbutton, text = "login", command= self.logincheck)
        self.loginbutton.pack()
        self.loginframetoploginbutton.pack()
        self.loginframetoploginbutton.forget()
        self.loginframeusername.pack()
        self.loginframepassword.pack()
        self.loginframetoploginbutton.pack()

    def logincheck (self):
        
        self.usernameentered = self.loginusernameentry.get()
        self.passwordentered = self.loginpasswordentry.get ()
        password = self.passwordchecker(self.usernameentered, self.passwordentered)
        if password == "successful":
                self.loginsucess ()
        else:
                self.loginwindow()
    #needstocheckpasswords
    def passwordchecker(self, username, password):
        """CHANGED HERE PASS"""
        #code for password check for now it just returns successful
        attemptresult = 'unsuccessful'
        for x in auser.getuser():
            if str(username) == x.get_id() and str(password)== x.getpass():
                attemptresult = "successful"
                return (attemptresult)
            else:
                continue
            return attemptresult
        """RETURN UNSUCCESSFUL IF WRONG PASS GIVEN, GOES BACK TO LOGIN WINDOW"""
    def loginsucess(self):
        destroyall = [self.topframe, self.loginframeusername, self.loginframepassword, self.loginframetoploginbutton]
        for frame in destroyall:
            frame.destroy()
            self.loggedinframe.pack(side = "top")
    def logout(self):
        self.main_window.destroy()
        MyGUI()
    def adduserfunction (self):
        self.clearolderframes()
        self.adduserframe = tkinter.Frame(self.main_window)
        if self.adduserframe not in self.allframes:
            self.allframes.append(self.adduserframe)
        self.idframe = tkinter.Frame(self.adduserframe)
        self.cityframe = tkinter.Frame (self.adduserframe)
        self.stateframe= tkinter.Frame (self.adduserframe)
        self.countryframe = tkinter.Frame (self.adduserframe)
        self.ageframe= tkinter.Frame (self.adduserframe)
        self.canceladdbuttonsadduser = tkinter.Frame(self.adduserframe)
        self.idlabel = tkinter.Label(self.idframe, text= "ID          ")
        self.identry = tkinter.Entry(self.idframe)
        self.idlabel.pack(side = "left")
        self.identry.pack (side= "left")
        self.citylabel = tkinter.Label(self.cityframe, text= "City       ")
        self.cityentry = tkinter.Entry(self.cityframe)
        self.citylabel.pack(side = "left")
        self.cityentry.pack (side= "left")
        self.statelabel = tkinter.Label(self.stateframe, text= "State     ")
        self.stateentry = tkinter.Entry(self.stateframe)
        self.statelabel.pack(side = "left")
        self.stateentry.pack (side= "left")
        self.countrylabel = tkinter.Label(self.countryframe, text= "Country")
        self.countryentry = tkinter.Entry(self.countryframe)
        self.countrylabel.pack(side = "left")
        self.countryentry.pack (side= "left")
        self.agelabel = tkinter.Label(self.ageframe, text= "Age       ")
        self.ageentry = tkinter.Entry(self.ageframe)
        self.agelabel.pack(side = "left")
        self.ageentry.pack (side= "left")
        self.cancelbutton = tkinter.Button(self.canceladdbuttonsadduser, text = "Cancel", command= self.canceladduserfunction)
        self.addbutton = tkinter.Button(self.canceladdbuttonsadduser, text = "Add", command= self.addusertousers)
        self.cancelbutton.pack (side= "left")
        self.addbutton.pack (side = "right")
        self.idframe.pack (side = "top")
        self.cityframe.pack (side = "top")
        self.stateframe.pack (side = "top")
        self.countryframe.pack (side = "top")
        self.ageframe.pack (side = "top")
        self.canceladdbuttonsadduser.pack (side = "top")
        self.adduserframe.pack()

    def canceladduserfunction (self):
        try:
            self.adduserframe.destroy()

        except:
            pass

    #loadusertolists+file
    def addusertousers (self):
        user = auser.getuser()
        Id={}
        for id in user:
            Id[id.get_id()]=0
        userID = self.identry.get()
        userCity = self.cityentry.get()
        userState = self.stateentry.get()
        userCountry = self.countryentry.get()
        userAge = self.ageentry.get ()
        location = Location(userCity,userState,userCountry)
        user = User(userID,location,userAge)
        if userID not in Id:
            file = open('user.dat','ab')
            pickle.dump(user,file)
            file.close()
            auser.load_objs()
        else:
            print(f"User with User Id: '{userID}' already exists")
        #####loadUSERFUNCTION HERE
        self.adduserframe.destroy()
        self.adduserfunction()

    def addbookfunction (self):
        
        self.clearolderframes()

        self.addbookframe = tkinter.Frame(self.main_window)
        if self.addbookframe not in self.allframes:
            self.allframes.append(self.addbookframe)


        self.isbnaddbookframe = tkinter.Frame(self.addbookframe)
        self.titleaddbookframe = tkinter.Frame(self.addbookframe)
        self.authoraddbookframe = tkinter.Frame(self.addbookframe)
        self.yearaddbookframe = tkinter.Frame(self.addbookframe)        
        self.publisheraddbookframe = tkinter.Frame(self.addbookframe)
        self.canceladdaddbookframe = tkinter.Frame(self.addbookframe)   


        self.isbnlabel = tkinter.Label(self.isbnaddbookframe, text = "ISBN        ")
        self.isbnentry = tkinter.Entry(self.isbnaddbookframe)
        self.isbnlabel.pack(side = "left")
        self.isbnentry.pack (side = "left")

        self.titlelabel = tkinter.Label(self.titleaddbookframe, text = "Title         ")
        self.titleentry = tkinter.Entry(self.titleaddbookframe)
        self.titlelabel.pack(side = "left")
        self.titleentry.pack (side = "left")

        self.authorlabel = tkinter.Label(self.authoraddbookframe, text = "Author     ")
        self.authorentry = tkinter.Entry(self.authoraddbookframe)
        self.authorlabel.pack(side = "left")
        self.authorentry.pack (side = "left")

        self.yearlabel = tkinter.Label(self.yearaddbookframe, text = "Year        ")
        self.yearentry = tkinter.Entry(self.yearaddbookframe)
        self.yearlabel.pack(side = "left")
        self.yearentry.pack (side = "left")

        self.publisherlabel = tkinter.Label(self.publisheraddbookframe, text = "Publisher")
        self.publisherentry = tkinter.Entry(self.publisheraddbookframe)
        self.publisherlabel.pack(side = "left")
        self.publisherentry.pack (side = "left")

        self.cancelbuttonaddbook = tkinter.Button (self.canceladdaddbookframe, text = "Cancel", command= self.canceladdbook)
        self.addbuttonaddbook = tkinter.Button (self.canceladdaddbookframe, text = "Add", command= self.addaddbook)
        self.cancelbuttonaddbook.pack (side = "left")
        self.addbuttonaddbook.pack (side = "right")


        self.isbnaddbookframe.pack (side = "top")
        self.titleaddbookframe.pack (side = "top")
        self.authoraddbookframe.pack (side = "top")
        self.yearaddbookframe.pack (side = "top")
        self.publisheraddbookframe.pack (side = "top")
        self.canceladdaddbookframe.pack (side = "top")

        self.addbookframe.pack(side = "top")

    def canceladdbook(self):
        try:
            self.addbookframe.destroy()
        except:
            pass

    #loadbooktolists+file
    def addaddbook(self):
        book_list=auser.getbook()
        isbn={}
        for Isbn in book_list:
            isbn[Isbn.get_isbn()]=0
        bookISBN = self.isbnentry.get()
        bookTitle = self.titleentry.get ()
        bookAuthor = self.authorentry.get()
        bookYear = self.yearentry.get()
        bookPublisher = self.publisherentry.get()
        obj = Book(bookISBN,bookTitle,bookAuthor,bookYear,bookPublisher)

        if bookISBN not in isbn:
            file = open('book.dat','ab')
            pickle.dump(obj,file)
            file.close()
            auser.load_objs()
        else:
            print(f"Book with isbn: {bookISBN} already exits")
        ####LOADBOOK
        try:
            self.addbookframe.destroy()
        except:
            pass
        self.addbookfunction()




    def searchuserfunction (self):
        self.clearolderframes()
        self.searchuserframe = tkinter.Frame(self.main_window)

        if self.searchuserframe not in self.allframes:
            self.allframes.append(self.searchuserframe)
        
        self.searchuseridframe= tkinter.Frame(self.searchuserframe)
        self.searchusercityframe= tkinter.Frame(self.searchuserframe)
        self.searchuserstateframe= tkinter.Frame(self.searchuserframe)
        self.searchusercountryframe= tkinter.Frame(self.searchuserframe)
        self.searchuserageframe= tkinter.Frame(self.searchuserframe)
        self.searchusercancelsearchbuttonsframe= tkinter.Frame(self.searchuserframe)    

        self.searchuseridlabel = tkinter.Label (self.searchuseridframe, text= "ID         ")
        self.searchuseridentry = tkinter.Entry (self.searchuseridframe)
        self.searchuseridlabel.pack (side = "left") 
        self.searchuseridentry.pack (side = "left") 

        self.searchusercitylabel = tkinter.Label (self.searchusercityframe, text= "City      ")
        self.searchusercityentry = tkinter.Entry (self.searchusercityframe)
        self.searchusercitylabel.pack (side = "left") 
        self.searchusercityentry.pack (side = "left")

        self.searchuserstatelabel = tkinter.Label (self.searchuserstateframe, text= "State    ")
        self.searchuserstateentry = tkinter.Entry (self.searchuserstateframe)
        self.searchuserstatelabel.pack (side = "left") 
        self.searchuserstateentry.pack (side = "left") 

        self.searchusercountrylabel = tkinter.Label (self.searchusercountryframe, text= "Country")
        self.searchusercountryentry = tkinter.Entry (self.searchusercountryframe)
        self.searchusercountrylabel.pack (side = "left") 
        self.searchusercountryentry.pack (side = "left") 

        self.searchuseragelabel = tkinter.Label (self.searchuserageframe, text= "Age      ")
        self.searchuserageentry = tkinter.Entry (self.searchuserageframe)
        self.searchuseragelabel.pack (side = "left") 
        self.searchuserageentry.pack (side = "left") 

        self.searchusercancelbutton = tkinter.Button (self.searchusercancelsearchbuttonsframe, text = "Cancel", command= self.searchusercancel)
        self.searchusersearchbutton = tkinter.Button (self.searchusercancelsearchbuttonsframe, text = "Search", command= self.searchusersearch)
        self.searchusercancelbutton.pack (side = "left")
        self.searchusersearchbutton.pack (side = "right")

        self.searchuseridframe.pack(side = "top")
        self.searchusercityframe.pack(side = "top")
        self.searchuserstateframe.pack(side = "top")
        self.searchusercountryframe.pack(side = "top")
        self.searchuserageframe.pack(side = "top")
        self.searchusercancelsearchbuttonsframe.pack(side = "top")

        self.searchuserframe.pack()

    def searchusercancel (self):
        self.clearolderframes()

    #searchbooksneedstostillwork
    def searchusersearch (self):
        self.searchid = self.searchuseridentry.get()
        self.searchcity = self.searchusercityentry.get()
        self.searchstate = self.searchuserstateentry.get()
        self.searchcountry = self.searchusercountryentry.get()
        self.searchage = self.searchuserageentry.get()
        userlist = auser.getuser()
        search_set=Bookdataset.Search_users(self,str(self.searchid),self.searchcity,self.searchstate,self.searchcountry,self.searchage,list=userlist)
        #print('%-10s'%'ID','%-20s'%'CITY','%-20s'%'STATE','%-20s'%'COUNTRY','%-20s'%"AGE")
        if search_set != 'Search result not found' and search_set != "Nothing searched":
            for x in search_set:
                #loc = x.get_location().split(',')
                print('-'*100)
                print('%-10s'%f"ID: {x.get_id()}",'%-25s'%f"CITY: {x.get_location().getcity()}",'%-25s'%f"STATE: {x.get_location().getstate()}",'%-25s'%f"COUNTRY: {x.get_location().getcountry()}",f"AGE: {int(float(x.get_age()))}")
                print('-'*100)
        else:
            print(search_set)
        self.clearolderframes()
        self.searchuserfunction()
    def searchbooksfunction (self):

        self.clearolderframes()

        self.searchbooksframe = tkinter.Frame(self.main_window)
        if self.searchbooksframe  not in self.allframes:
            self.allframes.append(self.searchbooksframe )


        self.isbnsearchbookframe = tkinter.Frame(self.searchbooksframe )
        self.titlesearchbookframe = tkinter.Frame(self.searchbooksframe )
        self.authorsearchbookframe = tkinter.Frame(self.searchbooksframe )
        self.yearsearchbookframe = tkinter.Frame(self.searchbooksframe )        
        self.publishersearchbookframe = tkinter.Frame(self.searchbooksframe )
        self.cancelsearchsearchbookframe = tkinter.Frame(self.searchbooksframe )   


        self.isbnlabelsearch = tkinter.Label(self.isbnsearchbookframe, text = "ISBN        ")
        self.isbnentrysearch = tkinter.Entry(self.isbnsearchbookframe)
        self.isbnlabelsearch.pack(side = "left")
        self.isbnentrysearch.pack (side = "left")

        self.titlelabelsearch = tkinter.Label(self.titlesearchbookframe, text = "Title         ")
        self.titleentrysearch = tkinter.Entry(self.titlesearchbookframe)
        self.titlelabelsearch.pack(side = "left")
        self.titleentrysearch.pack (side = "left")

        self.authorlabelsearch = tkinter.Label(self.authorsearchbookframe, text = "Author     ")
        self.authorentrysearch = tkinter.Entry(self.authorsearchbookframe)
        self.authorlabelsearch.pack(side = "left")
        self.authorentrysearch.pack (side = "left")

        self.yearlabelsearch = tkinter.Label(self.yearsearchbookframe, text = "Year        ")
        self.yearentrysearch = tkinter.Entry(self.yearsearchbookframe)
        self.yearlabelsearch.pack(side = "left")
        self.yearentrysearch.pack (side = "left")

        self.publisherlabelsearch = tkinter.Label(self.publishersearchbookframe, text = "Publisher")
        self.publisherentrysearch = tkinter.Entry(self.publishersearchbookframe)
        self.publisherlabelsearch.pack(side = "left")
        self.publisherentrysearch.pack (side = "left")

        self.cancelbuttonsearchbook = tkinter.Button (self.cancelsearchsearchbookframe, text = "Cancel", command= self.cancelsearchbook)
        self.addbuttonsearchbook = tkinter.Button (self.cancelsearchsearchbookframe, text = "Search", command= self.searchsearchbook)
        self.cancelbuttonsearchbook.pack (side = "left")
        self.addbuttonsearchbook.pack (side = "right")


        self.isbnsearchbookframe.pack (side = "top")
        self.titlesearchbookframe.pack (side = "top")
        self.authorsearchbookframe.pack (side = "top")
        self.yearsearchbookframe.pack (side = "top")
        self.publishersearchbookframe.pack (side = "top")
        self.cancelsearchsearchbookframe.pack (side = "top")

        self.searchbooksframe.pack(side = "top")

    def cancelsearchbook (self):
        self.clearolderframes()

    #needstosearch
    def searchsearchbook (self):
        self.searchisbn = self.isbnentrysearch.get()
        self.searchtitle= self.titleentrysearch.get()
        self.searchauthor =self.authorentrysearch.get()
        self.searchyear = self.yearentrysearch.get()
        self.searchpublisher =self.publisherentrysearch.get()
        booklist = auser.getbook()
        search_set=Bookdataset.Search_books(self,str(self.searchisbn),self.searchtitle,self.searchauthor,self.searchyear,self.searchpublisher,list=booklist)
        #print('%-10s'%'ID','%-20s'%'CITY','%-20s'%'STATE','%-20s'%'COUNTRY','%-20s'%"AGE")
        if search_set != 'Search result not found' and search_set != "Nothing searched":
            for x in search_set:
                #loc = x.get_location().split(',')
                print('-'*100)
                print('%-10s'%f"ISBN: {x.get_isbn()}",'%-0s'%f"TITLE: {x.get_title()}",'%-0s'%f"AUTHOR: {x.get_author()}",'%-10s'%f"YEAR: {x.get_year()}",f"PUBLISHER: {x.get_publisher()}")
                print('-'*100)
        else:
            print(search_set)

        self.clearolderframes

        self.searchbooksfunction()
        





    def sortbooksfunction (self):

        self.clearolderframes()
        self.sortbookframe = tkinter.Frame(self.main_window)

        if self.sortbookframe not in self.allframes:
            self.allframes.append(self.sortbookframe)
        

        self.sortoptions = tkinter.Frame(self.sortbookframe)


        self.optionselectedsortbook = tkinter.IntVar()
        self.optionselectedsortbook.set (0)


        self.sortisbn = tkinter.Radiobutton(self.sortoptions,variable = self.optionselectedsortbook, value= 1, text = "ISBN")
        self.sorttitle = tkinter.Radiobutton(self.sortoptions,variable =self.optionselectedsortbook, value= 2, text = "Title")
        self.sortauthor = tkinter.Radiobutton(self.sortoptions,variable = self.optionselectedsortbook, value= 3, text = "Author")
        self.sortyear = tkinter.Radiobutton(self.sortoptions,variable =self.optionselectedsortbook, value= 4, text = "Year")
        self.sortpublisher = tkinter.Radiobutton(self.sortoptions,variable = self.optionselectedsortbook, value= 5, text = "Publisher")
        self.sortrating = tkinter.Radiobutton(self.sortoptions,variable =self.optionselectedsortbook, value= 6, text = "Rating")
        self.sortratingcount = tkinter.Radiobutton(self.sortoptions,variable = self.optionselectedsortbook, value=7, text = "Rating count")


        self.sortisbn.pack (side = "left")
        self.sorttitle.pack (side = "left")
        self.sortauthor.pack (side = "left")
        self.sortyear.pack (side = "left")
        self.sortpublisher.pack (side = "left")
        self.sortrating.pack (side = "left")
        self.sortratingcount.pack (side = "left")


        self.sortoptions.pack (side = "top")

        self.cancelsortbutton = tkinter.Frame (self.sortbookframe)
        

        self.cancelbuttonsort = tkinter.Button (self.cancelsortbutton, text = "Cancel", command= self.cancelsortbooks)
        self.sortbuttonsort = tkinter.Button (self.cancelsortbutton, text = "Sort", command= self.sortsortbooks)

        self.cancelbuttonsort.pack(side = "left")
        self.sortbuttonsort.pack (side = "right")

        self.cancelsortbutton.pack (side = "top")
        self.sortbookframe.pack()

    def cancelsortbooks (self):
        self.clearolderframes()

    #needs to sort books
    def sortsortbooks (self):
        self.selectedsort = self.optionselectedsortbook.get()
        booklist = auser.getbook()
        sorted_prod = Bookdataset.Sort_books(self,self.selectedsort,booklist)
        #if sorted_prod!="Nothing selected":
        #    for x in sorted_prod:
        #        print('%-10s'%f"ISBN: {x.get_isbn()}",'%-0s'%f"TITLE: {x.get_title()}",'%-0s'%f"AUTHOR: {x.get_author()}",'%-10s'%f"YEAR: {x.get_year()}",f"PUBLISHER: {x.get_publisher()}",f"RATING: {x.get_rate()}",f"RATECOUNT: {x.get_ratecount()}")
        #else:
        #   print(sorted_prod)
        ###can use if statement


        self.clearolderframes()
        self.sortbooksfunction()





    #frameclearerfunction
    def clearolderframes (self):
        
        for frame in self.allframes:
            try:
                frame.destroy()
            except:
                pass

MyGUI()