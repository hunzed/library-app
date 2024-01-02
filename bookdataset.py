import pickle
#import gui
class Book:
    def __init__(self,isbn,book_title,book_author,year_of_publication,publisher,rating='',rating_count=''):
        self.__isbn=isbn
        self.__title=book_title
        self.__author=book_author
        self.__year=year_of_publication
        self.__publisher=publisher
        if rating == '':
            self.__rating= Book.rate(self)
        if rating_count=='':
            self.__ratecount=Book.ratecounts(self)
    def get_isbn(self):
        return self.__isbn
    def rate(self,value=0.0):
        self.__rating = value
        return self.__rating
    def ratecounts(self,value=0):
        self.__ratecount = value
        return self.__ratecount
    def get_rate(self):
        return self.__rating
    def get_ratecount(self):
        return self.__ratecount
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_year(self):
        return self.__year
    def get_publisher(self):
        return self.__publisher
    #def __str__(self):
    #    return f"{self.__isbn},{self.__title},{self.__author},{self.__year},{self.__publisher},{self.rating},{self.ratecount}"
class Location:
    def __init__(self,city=' ',state=' ',country=' '):
        self.city=city
        self.state=state
        self.country=country
    def __str__(self):
        return f'{self.city},{self.state},{self.country}'
    def getcity(self):
        return self.city
    def getstate(self):
        return self.state
    def getcountry(self):
        return self.country
class User:
    def __init__(self,user_id,location,age=''):
        self.__loca=location
        if age == '':
            self.__age=0
        else:
            self.__age=age
        self.__pass = User.__set_password(self)
        self.__id=user_id
        self.__reviewedlist=User.listreviewed(self)
    def get_id(self):
        return self.__id
    def get_location(self):
        return self.__loca
    def __set_password(self):
        varification = [self.__loca.city,self.__loca.state,self.__loca.country]
        for x in range(len(varification)):
            if varification[x]=='':
                varification[x]=' '
        return f"{varification[0][0]}{varification[1][0]}{varification[2][0]}{int(float(self.__age))}"
    def listreviewed(self,value=[]):
        self.__reviewedlist = value
    def get_listreviewed(self):
        return self.__reviewedlist
    def get_age(self):
        return self.__age
    def getpass(self):
        return self.__pass
class Bookdataset:
    def __init__(self):
#       for the first time you run your program, it constructs the book objects using the data in the
#       Books.csv file and saves them in the books list as well as writes them to book.dat file. In subsequent
#       runs, it loads book list with the books objects saved in the file book.dat. The same applies to the user
#       objects.
        self.__books=[]
        self.__users=[]
        Bookdataset.load_books(self)
        Bookdataset.load_users(self)
        Bookdataset.init_rating(self)
        Bookdataset.init_reviewed(self)
        try:
            file = open('book.dat','rb')
        except FileNotFoundError:
            Bookdataset.store_objs(self,'book.dat')
        else:
            pass
        try:
            file = open('user.dat','rb')
        except FileNotFoundError:
            Bookdataset.store_objs(self,'user.dat')
        else:
            pass
        Bookdataset.load_objs(self)
    def getbook(self):
        return self.__books
    def getuser(self):
        return self.__users
    def load_books(self):
        file = open('Books.csv','r')
        line = file.readline()
        while line!='':
            line = file.readline().rstrip('\n')
            if line!='':
                linelist = line.split(',')
                if linelist[0]!='':
                    if linelist[0].endswith('\t"'):
                        linelist[0]= linelist[0][1:linelist[0].index('\t')]
                    self.__books.append(Book(linelist[0],linelist[1],linelist[2],linelist[3],linelist[4]))
        file.close()
    def load_users(self):
        file = open('Users.csv','r')
        line = file.readline()
        #counter=0
        while line!='':
            line = file.readline().rstrip('\n')
            if line!='':
                linelist = line.split(',')
                in1 = 0
                in2 = 0
                x=0
                count = 0
                while x in range(len(line)) and count<2:
                    if count == 0:
                        if line[x]=='"':
                            in1 = x
                            x=len(line)
                            count+=1
                    if count==1:
                        x-=1
                        if line[x]=='"':
                            in2=x
                            count+=1
                    if count == 0:
                        x+=1
                #counter+=1
                #print(counter)
                loclist = line[in1+1:in2].split(',')
                if len(loclist)==3:
                    location = Location(loclist[0],loclist[1][1:],loclist[2][1:])
                elif len(loclist)==2:
                    location = Location(loclist[0],loclist[1][1:])
                elif len(loclist)==1:
                    location = Location(loclist[0])
                else:
                    location = Location()
                self.__users.append(User(linelist[0],location=location,age=linelist[-1]))
        file.close()
    def init_rating(self):
        book_review_dict = {}
        book_review_avg = {}
        file = open('Review_small.csv','r')
        line = file.readline()
        while line!='':
            line = file.readline().rstrip()
            if line!='':
                linelist = line.split(',')
                if linelist[1] not in book_review_dict:
                    book_review_dict[linelist[1]]=[float(linelist[2])]
                else:
                    book_review_dict[linelist[1]].append(float(linelist[2]))
        for x in book_review_dict:
            avg = float(sum(book_review_dict[x]))/float(len(book_review_dict[x]))
            avg = format(avg,".1f")
            book_review_avg[x]=[avg,len(book_review_dict[x])]
        for i in range(len(self.__books)):
            if str(self.__books[i].get_isbn()) in book_review_dict:
                self.__books[i].rate(float((book_review_avg[str(self.__books[i].get_isbn())])[0]))
                self.__books[i].ratecounts(int((book_review_avg[str(self.__books[i].get_isbn())])[1]))
    def init_reviewed(self): 
#       uses the data in the file Review_small.csv to find the books that have been reviewed
#       by each user in the list users and add them to the reviewed list attribute of that user.
        user_review_dict = {}
        file = open('Review_small.csv','r')
        line = file.readline()
        while line!='':
            line = file.readline().rstrip()
            if line!='':
                linelist = line.split(',')
                if linelist[0] not in user_review_dict:
                    user_review_dict[linelist[0]]=[str(linelist[1])]
                else:
                    user_review_dict[linelist[0]].append(str(linelist[1]))
        for i in range(len(self.__users)):
            if str(self.__users[i].get_id()) in user_review_dict:
                self.__users[i].listreviewed(user_review_dict[str(self.__users[i].get_id())])
    def store_objs(self,name): 
#       saves in books.dat the book objects of the books list. It also saves in users.dat the user
#       objects of the books list.
        if name == 'book.dat':
            file = open('book.dat','ab')
            for x in self.__books:
                pickle.dump(x,file)
            file.close()
        elif name=='user.dat':
            file1 = open('user.dat','ab')
            for x in self.__users:
                pickle.dump(x,file1)
            file1.close()
    def load_objs(self): 
#       reads the objects stored in book.dat and append them in the books list. It also reads the
#       objects stored in users.dat and append them to the users list.
        self.__users=[]
        self.__books=[]
        file = open('book.dat','rb')
        while True:
            try:
                self.__books.append(pickle.load(file))
            except EOFError:
                break
        file.close()
        file1 = open('user.dat','rb')
        while True:
            try:
                self.__users.append(pickle.load(file1))
            except EOFError:
                break
        file1.close()
    def Search_books(self,isbn='',title='',author='',year='',publisher='',list=[]): 
#       it can receive any combination of values of a book’s attributes and returns the
#       matching book objects from the books list.
        Isbn = str(isbn)
        Title = str(title)
        Author = str(author)
        Year = str(year)
        Publisher = str(publisher)
        book_search_obj_list=[]
        arg = False
        for book_obj in list:
            if Isbn!='':
                if Isbn == book_obj.get_isbn():
                    book_search_obj_list.append(book_obj)
                    arg=True
                else:
                    continue
            if Title!='':
                if Title == book_obj.get_title():
                    book_search_obj_list.append(book_obj)
                    arg = True
            if Author!='':
                if Author == book_obj.get_author():
                    book_search_obj_list.append(book_obj)
                    arg=True
            if Year!='':
                if Year == book_obj.get_year():
                    book_search_obj_list.append(book_obj)
                    arg=True
            if Publisher!='':
                if Publisher == book_obj.get_publisher():
                    book_search_obj_list.append(book_obj)
                    arg=True
            if Isbn=='' and Title=='' and Author=='' and Year == '' and Publisher=='':
                return f"Nothing searched"
        if arg == False:
            return f"Search result not found"
        book_search_obj_list = set(book_search_obj_list)
        """ENDS HERE"""
        return book_search_obj_list
    def Search_users(self,id='',city='',state='',country='',age='',list=[]): 
#        it can receive any combination of values of a user’s attributes and returns the
#        matching user objects from the users list.
        """Start here"""
        Id = str(id)
        City = (str(city)).lower()
        State = (str(state)).lower()
        Country = (str(country)).lower()
        Age = str(age)
        user_search_obj_list=[]
        arg = False
        for user_obj in list:
            if Id!='':
                if Id == user_obj.get_id():
                    user_search_obj_list.append(user_obj)
                    arg=True
                else:
                    continue
            if City!='':
                if City == user_obj.get_location().city:
                    user_search_obj_list.append(user_obj)
                    arg = True
            if State!='':
                if State == user_obj.get_location().state:
                    user_search_obj_list.append(user_obj)
                    arg=True
            if Country!='':
                if Country == user_obj.get_location().country:
                    user_search_obj_list.append(user_obj)
                    arg=True
            if Age!='':
                if Age == user_obj.get_age():
                    user_search_obj_list.append(user_obj)
                    arg=True
            if Id=='' and City=='' and State=='' and Country == '' and Age=='':
                return f"Nothing searched"
        if arg == False:
            return f"Search result not found"
        user_search_obj_list = set(user_search_obj_list)
        """ENDS HERE"""
        return user_search_obj_list
    def Sort_books(self,values,list):
#       it can sort a books list using any of the books attributes.
        value = int(values)
        if value == 1:
            list_copy=[]
            for copy in list:
                list_copy.append(copy)
            sorted_list=[]
            value_list=[]
            for x in list_copy:
                value_list.append(x.get_isbn())
            value_list.sort()
            for y in value_list:
                for i in  list_copy:
                    if  y == i.get_isbn():
                        #sorted_list.append(i)
                        print('%-10s'%f"ISBN: {i.get_isbn()}",'%-0s'%f"TITLE: {i.get_title()}",'%-0s'%f"AUTHOR: {i.get_author()}",'%-0s'%f"YEAR: {i.get_year()}",f"PUBLISHER: {i.get_publisher()}",f"RATING: {i.get_rate()}",f"RATECOUNT: {i.get_ratecount()}")
                        list_copy.pop(list_copy.index(i))
                        break
            #return sorted_list
        elif value == 2:
            list_copy=[]
            for copy in list:
                list_copy.append(copy)
            sorted_list=[]
            value_list=[]
            for x in list_copy:
                value_list.append(x.get_title())
            value_list.sort()
            for y in value_list:
                for i in  list_copy:
                    if  y == i.get_title():
                        #sorted_list.append(i)
                        print('%-10s'%f"ISBN: {i.get_isbn()}",'%-0s'%f"TITLE: {i.get_title()}",'%-0s'%f"AUTHOR: {i.get_author()}",'%-0s'%f"YEAR: {i.get_year()}",f"PUBLISHER: {i.get_publisher()}",f"RATING: {i.get_rate()}",f"RATECOUNT: {i.get_ratecount()}")
                        list_copy.pop(list_copy.index(i))
                        break
            #return sorted_list
        elif value == 3:
            list_copy=[]
            for copy in list:
                list_copy.append(copy)
            sorted_list=[]
            value_list=[]
            for x in list_copy:
                value_list.append(x.get_author())
            value_list.sort()
            for y in value_list:
                for i in  list_copy:
                    if  y == i.get_author():
                        #sorted_list.append(i)
                        print('%-10s'%f"ISBN: {i.get_isbn()}",'%-0s'%f"TITLE: {i.get_title()}",'%-0s'%f"AUTHOR: {i.get_author()}",'%-0s'%f"YEAR: {i.get_year()}",f"PUBLISHER: {i.get_publisher()}",f"RATING: {i.get_rate()}",f"RATECOUNT: {i.get_ratecount()}")
                        list_copy.pop(list_copy.index(i))
                        break
            #return sorted_list
        elif value == 4:
            list_copy=[]
            for copy in list:
                list_copy.append(copy)
            sorted_list=[]
            value_list=[]
            for x in list_copy:
                value_list.append(x.get_year())
            value_list.sort()
            for y in value_list:
                for i in  list_copy:
                    if  y == i.get_year():
                        #sorted_list.append(i)
                        print('%-10s'%f"ISBN: {i.get_isbn()}",'%-0s'%f"TITLE: {i.get_title()}",'%-0s'%f"AUTHOR: {i.get_author()}",'%-0s'%f"YEAR: {i.get_year()}",f"PUBLISHER: {i.get_publisher()}",f"RATING: {i.get_rate()}",f"RATECOUNT: {i.get_ratecount()}")
                        list_copy.pop(list_copy.index(i))
                        break
            #return sorted_list
        elif value == 5:
            list_copy=[]
            for copy in list:
                list_copy.append(copy)
            sorted_list=[]
            value_list=[]
            for x in list_copy:
                value_list.append(x.get_publisher())
            value_list.sort()
            for y in value_list:
                for i in  list_copy:
                    if  y == i.get_publisher():
                        #sorted_list.append(i)
                        print('%-10s'%f"ISBN: {i.get_isbn()}",'%-0s'%f"TITLE: {i.get_title()}",'%-0s'%f"AUTHOR: {i.get_author()}",'%-0s'%f"YEAR: {i.get_year()}",f"PUBLISHER: {i.get_publisher()}",f"RATING: {i.get_rate()}",f"RATECOUNT: {i.get_ratecount()}")
                        list_copy.pop(list_copy.index(i))
                        break
            #return sorted_list
        elif value == 6:
            list_copy=[]
            for copy in list:
                list_copy.append(copy)
            sorted_list=[]
            value_list=[]
            for x in list_copy:
                value_list.append(x.get_rate())
            value_list.sort()
            value_list.reverse()
            for y in value_list:
                for i in  list_copy:
                    if  y == i.get_rate():
                        #sorted_list.append(i)
                        print('%-10s'%f"ISBN: {i.get_isbn()}",'%-0s'%f"TITLE: {i.get_title()}",'%-0s'%f"AUTHOR: {i.get_author()}",'%-0s'%f"YEAR: {i.get_year()}",f"PUBLISHER: {i.get_publisher()}",f"RATING: {i.get_rate()}",f"RATECOUNT: {i.get_ratecount()}")
                        list_copy.pop(list_copy.index(i))
                        break
            return sorted_list
        elif value == 7:
            list_copy=[]
            for copy in list:
                list_copy.append(copy)
            sorted_list=[]
            value_list=[]
            for x in list_copy:
                value_list.append(x.get_ratecount())
            value_list.sort()
            value_list.reverse()
            for y in value_list:
                for i in  list_copy:
                    if  y == i.get_ratecount():
                        #sorted_list.append(i)
                        print('%-10s'%f"ISBN: {i.get_isbn()}",'%-0s'%f"TITLE: {i.get_title()}",'%-0s'%f"AUTHOR: {i.get_author()}",'%-0s'%f"YEAR: {i.get_year()}",f"PUBLISHER: {i.get_publisher()}",f"RATING: {i.get_rate()}",f"RATECOUNT: {i.get_ratecount()}")
                        list_copy.pop(list_copy.index(i))
                        break
            #return sorted_list
        else:
            print("Nothing selected")
#agui=gui.MyGUI()
#auser = Bookdataset()
#for x in auser.getuser():
#    print(x.get_id(),'---',x.getpass())