#Day 15

#Reccomendation is PyCharm but I'm really digging VS Code so sticking with it. 
 
#If Microsoft sees this I <3 you and want to work for you... You know when I first started computing in '96 the first machine we got was a Compaq Win 95 machine.. now skipping the usuals I started to poke around and see what could be deleted or how changing apps could allow me greater access... I can't remember the game but it was like an 'Air Wolf' clone with Blackhawks and a weird level that looked like the grand canyon.. I was shit hot at it and it also allowed use of a joystick which was epic at the time but I digress, I mention this because I managed to get the software running without a key (and no it was not free ware).. Holy Shit I thought, I'm a hacker man! though I did not know what this meant for years.

#It was actually this 'event' that started me tinkering with electronics, like opening my sisters sterio and snipping every single wire and using some sellotape I managed to wire everything back up and somehow it still worked! I wasn't a nuesance per say but I did have a wondering how things worked. I

#Years forward and in Secondary School (Comprehensive in my case) I and a few others who were 'inclined' discovered net send and that we could use it to send eachother messages without the teacher seeing... we were ninjas! it only went wrong once mind when one of the school Bullies discovered how to use net send and sent a message saying that the "headmistress was a c*nt!" to every computer on the domain (which was every computer in every department in the entire school)... The IT Team killed that off pretty quick... 

#I started programming at Uni, cracking copywright soon after but that (I don't do that anymore I pay for everything), I REALLY enjoyed some of the things at Uni, be it using my Philips 12" laptop in lectures (I was the only one that used a laptop at the time and I miss that damn thing it was so 'pokey' for a 12 laptop and could do all sorts on a whopping 4GB of RAM ((MAX RAM back in the day)) ) Playing AOE2 on our 'house network' in year 2, running software that should not have been on my HTC Universal (I loved that too) a phone with a rotating touchscreen and built in keyboard.. jeez I had 3 of them the Black one from O2 and the silver from T-Mobile (T-Mob had it better as the backlit keyboard was RED! not white like on the others). I took one on a pub crawl one day and used the IR Blaster to change the TVs in all the pubs to other things, they never suspected it was the guy with the inch thick computer phone in his pocket.. also ViJay (ViJay555) if there is any chance in the universe that you see this, you did amazing work on the Windows Mobile Development side of things and I miss our chats on XDA Developers.. now move forward a considerable number of years I am using my skills for good with Ethical Hacking, Penetration Testing even this Python Course to 'git good' at it once more. I hope the outcome is a job that not only pays the bills but allows me to grow some more, hopefully someone sees this and hilariously submits a PR on it and says something like 'Hi I'm XYZ from XYZ company, you're funny and we need you'

#Most of this Days lesson is focussed on installing PyCharm on various machines but we should be coding shortly.


#Coffee Machine Starting code 

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#One of the tasks will be to add the coffee emoji to this project, luckily VS Code can interpret them too so we're still good on Code!