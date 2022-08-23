#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#ALturky_pro
#Mohamed_sabry
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def shell():
	f = open("link.txt","r");
	link = raw_input("ALturky >>  : ")
	print "\n\n|✓| \n"
        while True:
		sub_link = f.readline()
		if not sub_link:
                               break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
    b = """
     
      @@      *@@@@*      @@                        *@@@
     m@@m       @@        @@                          @@
    m@*@@!      @@      @@@@@@ *@@@  *@@@  *@@@m@@@   @@  m@@* *@@*   *@@*  *@@@@@@@@m *@@@m@@@   m@@*@@m
   m@  *@@      @@        @@     @@    @@    @@* **   @@ m@      @@   m@      @@   *@@   @@* **  @@*   *@@
   @@@!@!@@     @!     m  @@     !@    @@    @!       !@m@@       @@ m!       !@    @@   @!      @@     @@
  !*      @@    @!    :@  @!     !@    @!    @!       !@ *@@m      @@!        !@    !@   @!      @@     !@
   !!!!@!!@     !!     !  !!     !@    !!    !!       !!!!!        @!!        !@!   !!   !!      !@     !!
  !*      !!    !:    !!  !!     !!    !!    !:       :! *!!!      !!:    !!  !@   !!!   !:      !!!   !!!
: : :   : ::: : :: !: :   ::: :  :: !: :!: : :::    : : :  : :     !!     :   :!: : :  : :::      : : : :
                                                                 ::!          ::
                                                               :::          : : ::

 """
    print (b)
Credit()
shell()

