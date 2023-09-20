import main as app

def console():
    print("Hi, this is a basic crud where you can create, read, update and delete data from a database.")
    print("In this case our data will be music albums.")
    print("Let's start :)")

    while True:
        
        i = str(input("What do you want to do now? ('create', 'read', 'update', 'delete'): "))
        if(i == "create"):
            print("We're going to add a new album then.")
            ain = input("What's the name of the album? ")
            yin = input("When did it come out? ")
            anin = input("Who's the artist? ")

            app.create(ain, yin, anin)
            app.read()
            d = input("Do you want to start again? y/n")
            if(d == "y"):
                continue
            elif(d == "n"):
                break


        elif(i == "read"):
            print("This is your current database!")
            app.read()
            d = input("Do you want to start again? y/n")
            if(d == "y"):
                continue
            elif(d == "n"):
                break


        elif(i == "delete"):
            print("With an album's id you can delete its row.")
            idin = int(input("Which albumn do you want to delete? "))
            app.delete(idin)
            app.read()
            d = input("Do you want to start again? y/n")
            if(d == "y"):
                continue
            elif(d == "n"):
                break

        elif(i == "update"):
            print("To update a row you need to specify each column so..")
            in1 = input("Which album do you want to update? ")
            in2 = input("Which year? ")
            in3 = input("Which artist? ")
            print("Now you need to specify your new data.")
            in4 = input("Your new album's name: ")
            in5 = input("Your new album's year: ")
            in6 = input("Your new album's artist: ")

            app.update(in1, in2, in3, in4, in5, in6)
            app.read()
            d = input("Do you want to start again? y/n")
            if(d == "y"):
                continue
            elif(d == "n"):
                break





def run():
    console()
run()