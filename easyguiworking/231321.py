import easygui

amazon = "Amazon"
ebay = "Ebay"
craigslist = "Craigslist"

msg = "Where are we going to list this computer"
title = "Listing Website"
choices = [amazon, ebay, craigslist]
choice = easygui.buttonbox(msg, title, choices)

if choice == amazon:
	print(amazon)
elif choice == ebay:
	print(ebay)
elif choice == craigslist:
	print(craigslist)