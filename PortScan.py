import socket

getHost = input("IP address to scan: ")
toBannerGrab = input("Would you like to grab banners for open ports? (y/n): ")



# Method takes a host address and port as inputs and checks if there are any exceptions when connecting to them. This was chosen since it is faster then making a full connection
def scanPorts(host,port):
        # Creates socket to use for the method.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        # Returns true if there are no exceptions when connecting to the port.
        if (s.connect_ex((host,port))) == 0:
            return True
        else:
            return False



# Method takes a host and port as inputs, and checks to see if they can connect, and if it can grab a banner from the port. If not, it exits the method.
def grabBanner(ip,port):
    try:
        # Creates a socket
        bannerGrab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Sets the timeout so that it doesn't get stuck
        bannerGrab.settimeout(15)
        # Attempts to make a connection with the port
        bannerGrab.connect((ip,port))
        # Takes the banner given by the port, assigns it to the banner variable.
        banner = bannerGrab.recv(1024)
        # If sucsessful, function returns the banner 
        return(banner)
    except:
        # If there is an exception, function notifies that it was unable to grab the banner, and returns nothing.
        print("Unable to grab banner")
        return


# Combines previous functions into a logical flow. Take an ip address and a yes or no to banner grabbing
def runScan(ipAddr,toGrab):
    # For loop for every port
    for x in range(35535):
        # invokes the scanPorts function, and checks if it is true
        if scanPorts(ipAddr,x):
            print("Port "+str(x)+" is open")
            # Checks to see if the user wanted to grab banners. If so, it invokes the grabBanner function with the ip and port. 
            if toGrab == "y":
                print(grabBanner(ipAddr,x))

# Run function with input from user
runScan(getHost,toBannerGrab)