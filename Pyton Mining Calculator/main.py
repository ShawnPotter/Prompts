#EVE Online Mining Calculator
#main.py
#Shawn Potter
#6/12/2017

# This program creates a GUI using Tkinter
# The user is first presented with a question of which type of ship they are flying. Once the user clicks the corrosponding buttons
# the window draws the rest of the buttons onto the screen. Incorrect or Useless buttons will be grayed out and the user will be unable
# to click them. The window has seperate sections relating to the Users: Skills, Ship, Module, and Ore choices. The user will select
# from these options. After hitting the enter button the user will receieve a print out of text inside the text box at the bottom.
# This text will indicate how much of the ore can fit inside their ship and how long it will take to mine that amount of ore.
# Currently, I believe the program only draws new widgets ontop of the old ones (evidenced by when I had different sized radiobuttons
# with text the old widgets were still there and would be overlaping. This will eventually lead to a memory leak issue if given enough time
# and enough repeated clicking of the buttons. Luckily because the application is so lightweight it would take a lot for this to cause a large 
# enough problem. At my current skill level I can not fix this. The application can improved greatly with the inclusion of Classes and further 
# techniques that I haven't learned yet.

# This project took learning tkinter on my own and staring at documentation on multiple websites for hours (mostly docs.python.org 
# but also effbot.org) to gain an understanding what I was trying to do. The end result is likely amatuerish but for now I'm pleased
# with the result. 

# List of Terms:
# Ship Class = The class of ship 
# Mining Frigate = The basic class of mining ship
# Expedition Frigate = An advanced version of the Mining Frigate, boasts larger cargohold capacity and other features
# Mining Barge = Dedicated medium sized mining vessel. Can use the Strip Miner Module
# Exhumer = An advanced version of the Mining Barge
# Module = equipment fit onto ships. Modules can mean a variety of things but in this case it means a Mining Laser
# Miner I & Miner II = Miner Is are the basic mining lasers everyone starts at. Miner IIs are the advanced version
# Strip Miners = An advanced laser able to, as the name suggests, strip mine
# T1 = Tech Level One
# T2 = Tech Level Two
# Crystals = A type of specialized "ammo" that can be loaded into the Strip Miner II module only these improve yield
# Ore: Easy enough, the ore you recieve from the type of asteroid you are mining. The names of each ore type are fictional

import math
import datetime
from tkinter import *

#Pulls the Input Data and runs it through the math
def get_entries():
	#Ore Attributes
	if ore.get() == 1: 
		oreVolume = 0.1
		oreName = "Veldspar"

	elif ore.get() == 2:
		oreVolume = 0.15
		oreName = "Scordite"

	elif ore.get() == 3:
		oreVolume = 0.3
		oreName = "Pyroxeres"

	elif ore.get() == 4:
		oreVolume = 0.35
		oreName = "Plagioclase"

	elif ore.get() == 5:
		oreVolume = 1.2
		oreName = "Kernite"

	elif ore.get() == 6:
		oreVolume = 0.6
		oreName = "Omber"

	elif ore.get() == 7:
		oreVolume = 2
		oreName = "Jaspet"

	elif ore.get() == 8:
		oreVolume = 3
		oreName = "Hemorphite"
		
	elif ore.get() == 9:
		oreVolume = 3
		oreName = "Hedbergite"
		
	elif ore.get() == 10:
		oreVolume = 16
		oreName = "Spodumain"
		
	elif ore.get() == 11:
		oreVolume = 8
		oreName = "Dark Ochre"
		
	elif ore.get() == 12:
		oreVolume = 16
		oreName = "Crokite"
		
	elif ore.get() == 13:
		oreVolume = 16
		oreName = "Bistot"
		
	elif ore.get() == 14:
		oreVolume = 5
		oreName = "Gneiss"
		
	elif ore.get() == 15:
		oreVolume = 16
		oreName = "Arkonor"
		
	elif ore.get() == 16:
		oreVolume = 40
		oreName = "Mercoxit"
		
	#Module Attributes		  
	if module.get() == 1:
		module_cycletime = 1 #seconds
		module_extraction = 40 #unit(s)
	elif module.get() == 2:
		module_cycletime = 1 #seconds
		module_extraction = 60 #unit(s)
	elif module.get() == 3:
		module_cycletime = 180 #seconds
		module_extraction = 675 #unit(s)
	elif module.get() == 4:
		module_cycletime = 180 #seconds
		module_extraction = 450 #unit(s)
	elif module.get() == 5:
		module_cycletime = 180 #seconds
		module_extraction = 450 * 1.625 #unit(s)
	elif module.get() == 6:
		module_cycletime = 180 #seconds
		module_extraction = 450 * 1.75 #unit(s)
	
	cycle_time = module_cycletime
	  
	#Ship Attributes
	#Venture
	if ship.get() == 1:
		hold = 5000
		turrets = 2
		role_bonus = 2
		#ROE is Rate of Extraction
		ROE = (cycle_time
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* (1 + (0.05 * skill_MiningFrig.get()))
				* role_bonus
				* turrets)

	#Prospect
	if ship.get() == 2:
		hold = 10000
		turrets = 2
		role_bonus = 2
		#ROE is Rate of Extraction
		ROE = (cycle_time
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* (1 + (0.05 * skill_MiningFrig.get()))
				* (1 + (0.05 * skill_ExpFrig.get()))
				* role_bonus
				* turrets)

	#Endurance
	if ship.get() == 3:
		hold = 15000
		turrets = 1
		role_bonus = 4
		#ROE is Rate of Extraction
		ROE = (cycle_time
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* (1 + (0.05 * skill_MiningFrig.get()))
				* role_bonus
				* turrets)
		
	#Procurer
	if ship.get() == 4:
		hold = 12000
		turrets = 2
		role_bonus = 1
		final_cycletime = (
					cycle_time
					* (1 - (0.02 * skill_MiningBarge.get()))
					)
		#ROE is Rate of Extraction
		ROE = (module_extraction
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* role_bonus
				* turrets)
		
	#Retriever
	if ship.get() == 5:
		hold = 22000 * (1 + (0.05 * skill_MiningBarge.get()))
		turrets = 2
		role_bonus = 1
		final_cycletime = (
					cycle_time
					* (1 - (0.02 * skill_MiningBarge.get()))
					)	   
		#ROE is Rate of Extraction
		ROE = (module_extraction
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* role_bonus
				* turrets)

	#Covetor
	if ship.get() == 6:
		hold = 7000
		turrets = 2
		role_bonus = 1
		final_cycletime = (
					cycle_time
					* (1 - (0.02 * skill_MiningBarge.get()))
					* 0.75
					)
		#ROE is Rate of Extraction
		ROE = (module_extraction
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* role_bonus
				* turrets)

	#Skiff
	if ship.get() == 7:
		hold = 15000
		turrets = 2
		role_bonus = 1
		final_cycletime = (
					cycle_time
					* (1 - (0.02 * skill_MiningBarge.get()))
					* (1 - (0.02 * skill_Exhumer.get()))
					)
		#ROE is Rate of Extraction
		ROE = (module_extraction
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* (1 + (0.01 * skill_MiningBarge.get()))
				* role_bonus
				* turrets)
	#Mackinaw
	if ship.get() == 8:
		hold = (
			28000
			* (1 + (0.05 * skill_MiningBarge.get())))
		turrets = 2
		role_bonus = 1
		final_cycletime = (
					cycle_time
					* (1 - (0.02 * skill_MiningBarge.get()))
					* (1 - (0.02 * skill_Exhumer.get()))
					)
		#ROE is Rate of Extraction
		ROE = (module_extraction
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* role_bonus
				* turrets)
	#Hulk
	if ship.get() == 9:
		hold = 8500 #ore hold
		turrets = 2 #turret slots
		role_bonus = 1 #role bonus for mining amount 1 = No Role Bonus, 2 = 100% mining bonus
		final_cycletime = (
					cycle_time
					* (1 - (0.02 * skill_MiningBarge.get()))
					* (1 - (0.03 * skill_Exhumer.get()))
					* (0.75)
					)
		#ROE is Rate of Extraction
		ROE = (module_extraction
				* (1 + (0.05 * skill_Mining.get()))
				* (1 + (0.05 * skill_Astro.get()))
				* role_bonus
				* turrets
				)
	AOH = hold / oreVolume #AOH is Amount of Ore in Hold
	
	#TTFH is Time to Full Hold
	if ship.get() < 4:
		TTFH = hold / ROE
	if ship.get() > 3:
		TTFH = (hold / ROE) * final_cycletime
	minutes, seconds = divmod(TTFH, 60)
	return AOH, oreName, minutes, seconds;
#Prints the collated Data out in the textbox
def print_entries():
	AOH, oreName, minutes, seconds = get_entries()
	minutes = int(minutes)
	seconds = int(seconds)
	T.delete('1.0', END)
	T.insert(
		END,"Your ship can hold {} units of {}\n\nYou will mine the maximum amount of ore in {} minutes and {} seconds\n\n".format(
			math.trunc(AOH), oreName, minutes, seconds
			)
		)
#Grays out useless or incorrect choices 
def grayOut_miningfrigate():
	#Mining Skill Radio Buttons
	mSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in mSkill_Options:
		mSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Mining,
			value = val
			)
		mSkill.rowconfigure(
			"all", minsize = 10
			)
		mSkill.grid(
			row = 2,
			column = col,
			sticky = W,
			)
		mSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		

	#Astrogeology Skill Radio Buttons
	aSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in aSkill_Options:
		aSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Astro,
			value=val
			)
		aSkill.grid(
			row = 3,
			column = col,
			sticky = W
			)
		aSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Mining Frigate Skill Radio Buttons
	mfSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in mfSkill_Options:
		mfSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_MiningFrig,
			value=val
			)
		mfSkill.grid(
			row = 4,
			column = col,
			sticky = W
			)
		mfSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Expedition Frigate Skill Radio Buttons
	efSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in efSkill_Options:
		efSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_ExpFrig,
			value=val
			)
		efSkill.grid(
			row = 5,
			column = col,
			sticky = W
			)
		efSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		
	#Mining Barge Skill Radio Buttons
	mbSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in mbSkill_Options:
		mbSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_MiningBarge,
			value=val
			)
		mbSkill.grid(
			row = 6,
			column = col,
			sticky = W
			)
		mbSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		
	#Exhumer Skill Radio Buttons
	eSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in eSkill_Options:
		eSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Exhumer,
			value=val
			)
		eSkill.grid(
			row = 7,
			column = col,
			sticky = W
			)
		eSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Ship Choice Radio Buttons
	ship_Options = [
		("Venture", 1, 8, 1, "normal"),
		("Prospect", 2, 8, 3, "disabled"),
		("Endurance", 3, 8, 5, "disabled"),
		("Procurer", 4, 9, 1, "disabled"),
		("Retriever", 5, 9, 3, "disabled"),
		("Covetor", 6, 9, 5, "disabled"),
		("Skiff", 7, 10, 1, "disabled"),
		("Mackinaw", 8, 10, 3, "disabled"),
		("Hulk", 9, 10, 5, "disabled")
		]

	for text, val, r, col, activity in ship_Options:
		ship_b = Radiobutton(
			frame3,
			text=text,
			variable = ship,
			value=val
			)
		ship_b.grid(
			row = r,
			column = col,
			sticky = W
			)
		ship_b.config(
			state = activity,
			indicatoron = 0,
			width = 8
			)
		
		
	#Module Choice Radio Buttons
	module_Options = [
		("Miner I", 1, 11, 1, "normal"),
		("Miner II", 2, 11, 3, "normal"),
		("Strip Miner I", 3, 12, 1, "disabled"),
		("Strip Miner II", 4, 12, 3, "disabled"),
		("Strip Miner II (T1 Crystals)", 5, 13, 1, "disabled"),
		("Strip Miner II (T2 Crystals)", 6, 13, 3, "disabled"),
		]

	for text, val, r, col, activity in module_Options:
		module_b = Radiobutton(
			frame4,
			text=text,
			variable = module,
			value=val
			)
		module_b.grid(
			row = r,
			column = col,
			sticky = W,
			ipadx = 10
			)
		module_b.config(
			state = activity,
			indicatoron = 0,
			width = 16
			)

	#Ore Choice Radio Buttons
	ore_Options = [
		("Veldspar", 1, 15, 1, 1),
		("Scordite", 2, 15, 3, 1),
		("Pyroxeres", 3, 15, 5, 1),
		("Plagioclase", 4, 16, 1, 1),
		("Kernite", 5, 16, 3, 1),
		("Omber", 6, 16, 5, 1),
		("Jaspet", 7, 17, 1, 1),
		("Hemorphite", 8, 17, 3, 1),
		("Hedbergite", 9, 17, 5, 1),
		("Spodumain", 10, 18, 1, 1),
		("Dark Ochre", 11, 18, 3, 1),
		("Crokite", 12, 18, 5, 1),
		("Bistot", 13, 19, 1, 1),
		("Gneiss", 14, 19, 3, 1),
		("Arkonor", 15, 19, 5, 1),
		("Mercoxit", 16, 20, 1, 1)
		]

	for text, val, r, col, cspan in ore_Options:
		ore_b = Radiobutton(
			frame5,
			text = text,
			variable = ore,
			value = val
			)
		ore_b.grid(
				row = r,
				column = col,
				sticky = W,
				columnspan = cspan,
				ipadx = 10
				)	
		ore_b.config(
			indicatoron = 0,
			width = 8
			)
def grayOut_expeditionfrigate():
	#Mining Skill Radio Buttons
	mSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in mSkill_Options:
		mSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Mining,
			value = val
			)
		mSkill.rowconfigure(
			"all", minsize = 10
			)
		mSkill.grid(
			row = 2,
			column = col,
			sticky = W,
			)
		mSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		

	#Astrogeology Skill Radio Buttons
	aSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in aSkill_Options:
		aSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Astro,
			value = val
			)
		aSkill.grid(
			row = 3,
			column = col,
			sticky = W
			)
		aSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Mining Frigate Skill Radio Buttons
	mfSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in mfSkill_Options:
		mfSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_MiningFrig,
			value = val
			)
		mfSkill.grid(
			row = 4,
			column = col,
			sticky = W
			)
		mfSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Expedition Frigate Skill Radio Buttons
	efSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in efSkill_Options:
		efSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_ExpFrig,
			value = val
			)
		efSkill.grid(
			row = 5,
			column = col,
			sticky = W
			)
		efSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		
	#Mining Barge Skill Radio Buttons
	mbSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in mbSkill_Options:
		mbSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_MiningBarge,
			value = val
			)
		mbSkill.grid(
			row = 6,
			column = col,
			sticky = W
			)
		mbSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		
	#Exhumer Skill Radio Buttons
	eSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in eSkill_Options:
		eSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Exhumer,
			value = val
			)
		eSkill.grid(
			row = 7,
			column = col,
			sticky = W
			)
		eSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Ship Choice Radio Buttons
	ship_Options = [
		("Venture", 1, 8, 1, "disabled"),
		("Prospect", 2, 8, 3, "normal"),
		("Endurance", 3, 8, 5, "normal"),
		("Procurer", 4, 9, 1, "disabled"),
		("Retriever", 5, 9, 3, "disabled"),
		("Covetor", 6, 9, 5, "disabled"),
		("Skiff", 7, 10, 1, "disabled"),
		("Mackinaw", 8, 10, 3, "disabled"),
		("Hulk", 9, 10, 5, "disabled")
		]

	for text, val, r, col, activity in ship_Options:
		ship_b = Radiobutton(
			frame3,
			text=text,
			variable = ship,
			value = val
			)
		ship_b.grid(
			row = r,
			column = col,
			sticky = W
			)
		ship_b.config(
			state = activity,
			indicatoron = 0,
			width = 8
			)
		
		
	#Module Choice Radio Buttons
	module_Options = [
		("Miner I", 1, 11, 1, "normal"),
		("Miner II", 2, 11, 3, "normal"),
		("Strip Miner I", 3, 12, 1, "disabled"),
		("Strip Miner II", 4, 12, 3, "disabled"),
		("Strip Miner II (T1 Crystals)", 5, 13, 1, "disabled"),
		("Strip Miner II (T2 Crystals)", 6, 13, 3, "disabled"),
		]

	for text, val, r, col, activity in module_Options:
		module_b = Radiobutton(
			frame4,
			text = text,
			variable = module,
			value = val
			)
		module_b.grid(
			row = r,
			column = col,
			sticky = W,
			ipadx = 10
			)
		module_b.config(
			state = activity,
			indicatoron = 0,
			width = 16
			)

	#Ore Choice Radio Buttons
	ore_Options = [
		("Veldspar", 1, 15, 1, 1),
		("Scordite", 2, 15, 3, 1),
		("Pyroxeres", 3, 15, 5, 1),
		("Plagioclase", 4, 16, 1, 1),
		("Kernite", 5, 16, 3, 1),
		("Omber", 6, 16, 5, 1),
		("Jaspet", 7, 17, 1, 1),
		("Hemorphite", 8, 17, 3, 1),
		("Hedbergite", 9, 17, 5, 1),
		("Spodumain", 10, 18, 1, 1),
		("Dark Ochre", 11, 18, 3, 1),
		("Crokite", 12, 18, 5, 1),
		("Bistot", 13, 19, 1, 1),
		("Gneiss", 14, 19, 3, 1),
		("Arkonor", 15, 19, 5, 1),
		("Mercoxit", 16, 20, 1, 1)
		]

	for text, val, r, col, cspan in ore_Options:
		ore_b = Radiobutton(
			frame5,
			text = text,
			variable = ore,
			value = val
			)
		ore_b.grid(
				row = r,
				column = col,
				sticky = W,
				columnspan = cspan,
				ipadx = 10
				)	
		ore_b.config(
			indicatoron = 0,
			width = 8
			)
def grayOut_miningbarge():
	#Mining Skill Radio Buttons
	mSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in mSkill_Options:
		mSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Mining,
			value = val
			)
		mSkill.rowconfigure(
			"all", minsize = 10
			)
		mSkill.grid(
			row = 2,
			column = col,
			sticky = W,
			)
		mSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		

	#Astrogeology Skill Radio Buttons
	aSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in aSkill_Options:
		aSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Astro,
			value=val
			)
		aSkill.grid(
			row = 3,
			column = col,
			sticky = W
			)
		aSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Mining Frigate Skill Radio Buttons
	mfSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in mfSkill_Options:
		mfSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_MiningFrig,
			value=val
			)
		mfSkill.grid(
			row = 4,
			column = col,
			sticky = W
			)
		mfSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Expedition Frigate Skill Radio Buttons
	efSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in efSkill_Options:
		efSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_ExpFrig,
			value=val
			)
		efSkill.grid(
			row = 5,
			column = col,
			sticky = W
			)
		efSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		
	#Mining Barge Skill Radio Buttons
	mbSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in mbSkill_Options:
		mbSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_MiningBarge,
			value=val
			)
		mbSkill.grid(
			row = 6,
			column = col,
			sticky = W
			)
		mbSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		
	#Exhumer Skill Radio Buttons
	eSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in eSkill_Options:
		eSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Exhumer,
			value=val
			)
		eSkill.grid(
			row = 7,
			column = col,
			sticky = W
			)
		eSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Ship Choice Radio Buttons
	ship_Options = [
		("Venture", 1, 8, 1, "disabled"),
		("Prospect", 2, 8, 3, "disabled"),
		("Endurance", 3, 8, 5, "disabled"),
		("Procurer", 4, 9, 1, "normal"),
		("Retriever", 5, 9, 3, "normal"),
		("Covetor", 6, 9, 5, "normal"),
		("Skiff", 7, 10, 1, "disabled"),
		("Mackinaw", 8, 10, 3, "disabled"),
		("Hulk", 9, 10, 5, "disabled")
		]

	for text, val, r, col, activity in ship_Options:
		ship_b = Radiobutton(
			frame3,
			text=text,
			variable = ship,
			value=val
			)
		ship_b.grid(
			row = r,
			column = col,
			sticky = W
			)
		ship_b.config(
			state = activity,
			indicatoron = 0,
			width = 8
			)
		
		
	#Module Choice Radio Buttons
	module_Options = [
		("Miner I", 1, 11, 1, "disabled"),
		("Miner II", 2, 11, 3, "disabled"),
		("Strip Miner I", 3, 12, 1, "normal"),
		("Strip Miner II", 4, 12, 3, "normal"),
		("Strip Miner II (T1 Crystals)", 5, 13, 1, "normal"),
		("Strip Miner II (T2 Crystals)", 6, 13, 3, "normal"),
		]

	for text, val, r, col, activity in module_Options:
		module_b = Radiobutton(
			frame4,
			text=text,
			variable = module,
			value=val
			)
		module_b.grid(
			row = r,
			column = col,
			sticky = W,
			ipadx = 10
			)
		module_b.config(
			state = activity,
			indicatoron = 0,
			width = 16
			)

	#Ore Choice Radio Buttons
	ore_Options = [
		("Veldspar", 1, 15, 1, 1),
		("Scordite", 2, 15, 3, 1),
		("Pyroxeres", 3, 15, 5, 1),
		("Plagioclase", 4, 16, 1, 1),
		("Kernite", 5, 16, 3, 1),
		("Omber", 6, 16, 5, 1),
		("Jaspet", 7, 17, 1, 1),
		("Hemorphite", 8, 17, 3, 1),
		("Hedbergite", 9, 17, 5, 1),
		("Spodumain", 10, 18, 1, 1),
		("Dark Ochre", 11, 18, 3, 1),
		("Crokite", 12, 18, 5, 1),
		("Bistot", 13, 19, 1, 1),
		("Gneiss", 14, 19, 3, 1),
		("Arkonor", 15, 19, 5, 1),
		("Mercoxit", 16, 20, 1, 1)
		]

	for text, val, r, col, cspan in ore_Options:
		ore_b = Radiobutton(
			frame5,
			text = text,
			variable = ore,
			value = val
			)
		ore_b.grid(
			row = r,
			column = col,
			sticky = W,
			columnspan = cspan,
			ipadx = 10
			)
		ore_b.config(
			state = activity,
			indicatoron = 0,
			width = 8
			)
def grayOut_exhumer():
	#Mining Skill Radio Buttons
	mSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in mSkill_Options:
		mSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Mining,
			value = val
			)
		mSkill.rowconfigure(
			"all", minsize = 10
			)
		mSkill.grid(
			row = 2,
			column = col,
			sticky = W,
			)
		mSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		

	#Astrogeology Skill Radio Buttons
	aSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in aSkill_Options:
		aSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Astro,
			value=val
			)
		aSkill.grid(
			row = 3,
			column = col,
			sticky = W
			)
		aSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Mining Frigate Skill Radio Buttons
	mfSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in mfSkill_Options:
		mfSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_MiningFrig,
			value=val
			)
		mfSkill.grid(
			row = 4,
			column = col,
			sticky = W
			)
		mfSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Expedition Frigate Skill Radio Buttons
	efSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "disabled")
		]

	for text, val, col, activity in efSkill_Options:
		efSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_ExpFrig,
			value=val
			)
		efSkill.grid(
			row = 5,
			column = col,
			sticky = W
			)
		efSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		
	#Mining Barge Skill Radio Buttons
	mbSkill_Options = [
		("1", 1, 1, "disabled"),
		("2", 2, 2, "disabled"),
		("3", 3, 3, "disabled"),
		("4", 4, 4, "disabled"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in mbSkill_Options:
		mbSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_MiningBarge,
			value=val
			)
		mbSkill.grid(
			row = 6,
			column = col,
			sticky = W
			)
		mbSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)
		
	#Exhumer Skill Radio Buttons
	eSkill_Options = [
		("1", 1, 1, "normal"),
		("2", 2, 2, "normal"),
		("3", 3, 3, "normal"),
		("4", 4, 4, "normal"),
		("5", 5, 5, "normal")
		]

	for text, val, col, activity in eSkill_Options:
		eSkill = Radiobutton(
			frame1,
			text = text,
			variable = skill_Exhumer,
			value=val
			)
		eSkill.grid(
			row = 7,
			column = col,
			sticky = W
			)
		eSkill.config(
			state = activity,
			indicatoron = 0,
			width = 3
			)

	#Ship Choice Radio Buttons
	ship_Options = [
		("Venture", 1, 8, 1, "disabled"),
		("Prospect", 2, 8, 3, "disabled"),
		("Endurance", 3, 8, 5, "disabled"),
		("Procurer", 4, 9, 1, "disabled"),
		("Retriever", 5, 9, 3, "disabled"),
		("Covetor", 6, 9, 5, "disabled"),
		("Skiff", 7, 10, 1, "normal"),
		("Mackinaw", 8, 10, 3, "normal"),
		("Hulk", 9, 10, 5, "normal")
		]

	for text, val, r, col, activity in ship_Options:
		ship_b = Radiobutton(
			frame3,
			text=text,
			variable = ship,
			value=val
			)
		ship_b.grid(
			row = r,
			column = col,
			sticky = W
			)
		ship_b.config(
			state = activity,
			indicatoron = 0,
			width = 8
			)
		
		
	#Module Choice Radio Buttons
	module_Options = [
		("Miner I", 1, 11, 1, "disabled"),
		("Miner II", 2, 11, 3, "disabled"),
		("Strip Miner I", 3, 12, 1, "normal"),
		("Strip Miner II", 4, 12, 3, "normal"),
		("Strip Miner II (T1 Crystals)", 5, 13, 1, "normal"),
		("Strip Miner II (T2 Crystals)", 6, 13, 3, "normal"),
		]

	for text, val, r, col, activity in module_Options:
		module_b = Radiobutton(
			frame4,
			text=text,
			variable = module,
			value=val
			)
		module_b.grid(
			row = r,
			column = col,
			sticky = W,
			ipadx = 10
			)
		module_b.config(
			state = activity,
			indicatoron = 0,
			width = 16
			)

	#Ore Choice Radio Buttons
	ore_Options = [
		("Veldspar", 1, 15, 1, 1),
		("Scordite", 2, 15, 3, 1),
		("Pyroxeres", 3, 15, 5, 1),
		("Plagioclase", 4, 16, 1, 1),
		("Kernite", 5, 16, 3, 1),
		("Omber", 6, 16, 5, 1),
		("Jaspet", 7, 17, 1, 1),
		("Hemorphite", 8, 17, 3, 1),
		("Hedbergite", 9, 17, 5, 1),
		("Spodumain", 10, 18, 1, 1),
		("Dark Ochre", 11, 18, 3, 1),
		("Crokite", 12, 18, 5, 1),
		("Bistot", 13, 19, 1, 1),
		("Gneiss", 14, 19, 3, 1),
		("Arkonor", 15, 19, 5, 1),
		("Mercoxit", 16, 20, 1, 1)
		]

	for text, val, r, col, cspan in ore_Options:
		ore_b = Radiobutton(
			frame5,
			text = text,
			variable = ore,
			value = val
			)
		ore_b.grid(
			row = r,
			column = col,
			sticky = W,
			columnspan = cspan,
			ipadx = 10
			)
		ore_b.config(
			state = activity,
			indicatoron = 0,
			width = 8
			)

#WINDOW
root = Tk()
root.title("EVE Online Mining Calculator")
root.state("zoomed")
root.iconbitmap(r'icon.ico')


#FRAME SETUPS
frame0 = Frame(root)
frame0.grid(
	pady = 5, 
	sticky = W
	)
frame1 = Frame(root)
frame1.grid(
	pady = 5, 
	sticky = W
	)
frame2 = Frame(root)
frame2.grid(
	pady = 5, 
	sticky = E
	)
frame3 = Frame(root)
frame3.grid(
	pady = 5, 
	sticky = W
	)
frame4 = Frame(root)
frame4.grid(
	pady = 5, 
	sticky = W
	)
frame5 = Frame(root)
frame5.grid(
	pady = 5, 
	sticky = W
	)
frame6 = Frame(root)
frame6.grid(
	pady = 5,
	padx = 75,
	sticky = W
	)
for x in range(10):
	frame6.grid_columnconfigure(
		x,
		minsize = 50
		)
frame7 = Frame(root)
frame7.grid(
	pady = 5,
	sticky = W
	)
for x in range(10):
	frame7.grid_columnconfigure(
		x,
		minsize = 40
		)

#MAIN VARIABLES
skill_Mining = IntVar()
skill_Astro = IntVar()
skill_MiningFrig = IntVar()
skill_ExpFrig = IntVar()
skill_MiningBarge = IntVar()
skill_Exhumer = IntVar()
ship_choice = IntVar()
ship = IntVar()
module = IntVar()
ore = IntVar()

#Section Identifier Text
#Ship Class Label
classLabel = Label(
	frame0, 
	text="Choose Ship Class:"
	)
classLabel.config(
	font = ("bold", 13)
	)
classLabel.grid(
	row = 0, 
	column = 0,
	columnspan = 10,
	sticky = E, 
	ipadx = 5
	)
#Character Skill Section Identifier
section1 = Label(
	frame1, 
	text = "Character Skills"
	)
section1.config(
	font = ("bold", 13)
	)
section1.grid(
	row = 1,
	columnspan = 20,
	sticky = W,
	ipadx = 5
	)
#Skill Labels
miningLabel = Label(
	frame1, 
	text="Mining:"
	)
miningLabel.grid(
	row = 2, 
	sticky = E, 
	ipadx = 5
	)
astroLabel = Label(
	frame1, 
	text = "Astrogeology:"
	)
astroLabel.grid(
	row = 3, 
	sticky = E, 
	ipadx = 5
	)
mfrigLabel = Label(
	frame1, 
	text="Mining Frigate:"
	)
mfrigLabel.grid(
	row = 4, 
	sticky = E, 
	ipadx = 5
	)
efrigLabel = Label(
	frame1, 
	text="Expedition Frigate:"
	)
efrigLabel.grid(
	row = 5, 
	sticky = E, 
	ipadx = 5
	)
mBargeLabel = Label(
	frame1, 
	text="Mining Barge:"
	)
mBargeLabel.grid(
	row = 6, 
	sticky = E, 
	ipadx = 5
	)
exhumerLabel = Label(
	frame1, 
	text="Exhumer:"
	)
exhumerLabel.grid(
	row = 7, 
	sticky = E, 
	ipadx = 5
	)
#Ship Hull Section Identifier
section2 = Label(
	frame3,
	text = "Choose Your Hull"
	)
section2.config(
	font = ("bold", 13)
	)
section2.grid(
	row = 7,
	columnspan = 20,
	sticky = W,
	ipadx = 5	
	)
#Ship Label
hullLabel = Label(
	frame3, 
	text="Hull:"
	)
hullLabel.grid(
	column = 0, 
	row = 8, 
	sticky = E, 
	ipadx = 19
	)
#Module Section Identifier
section3 = Label(
	frame4,
	text = "Choose Your Module"
	)
section3.config(
	font = ("bold", 13)
	)
section3.grid(
	row = 10,
	columnspan = 20,
	sticky = W,
	ipadx = 5	
	)
#Module Label
moduleLabel = Label(
	frame4, 
	text="Module:"
	)
moduleLabel.grid(
	column = 0, 
	row = 11, 
	sticky = E, 
	ipadx = 5
	)
#Ore Section Identifier
section4 = Label(
	frame5,
	text = "Choose The Ore"
	)
section4.config(
	font = ("bold", 13)
	)
section4.grid(
	row = 14,
	columnspan = 20,
	sticky = W,
	ipadx = 5	
	)
#Ore Label
oreLabel = Label(
	frame5, 
	text="Ore:"
	)
oreLabel.grid(
	column = 0, 
	row = 15, 
	sticky = E, 
	ipadx = 16
	)

#Ship Type Choice buttons
# Following buttons trigger the grayout_(shipclass) functions which cause radiobuttons 
# to gray out choices which would be useless or cause errors

#Mining Frigate Button
mFrigButton = Button(
	frame0, 
	text='Mining Frigate', 
	command = grayOut_miningfrigate
	)
mFrigButton.grid(
	row = 0, 
	column = 11, 
	pady = 4
	)

#Expedition Frigate Button
eFrigButton = Button(
	frame0, 
	text='Expedition Frigate', 
	command = grayOut_expeditionfrigate
	)
eFrigButton.grid(
	row = 0, 
	column = 12, 
	pady = 4
	)

#Mining Barge Button
mBargeButton = Button(
	frame0, 
	text='Mining Barge', 
	command = grayOut_miningbarge
	)
mBargeButton.grid(
	row = 0, 
	column = 13, 
	pady = 4
	)
#Exhumer Button
exhumerButton = Button(
	frame0, 
	text='Exhumer', 
	command = grayOut_exhumer
	)
exhumerButton.grid(
	row = 0, 
	column = 14, 
	pady = 4
	)

#Quit and Enter Buttons
#Quit Button
QuitButton = Button(
	frame6, 
	text='Quit', 
	command = root.quit
	)
QuitButton.grid(
	row = 21, 
	column = 3, 
	pady = 4
	)

#Enter Button
EnterButton = Button(
	frame6, 
	text='Enter', 
	command = print_entries
	)
EnterButton.grid(
	row = 21, 
	column = 4, 
	pady = 4
	)

#Output Text Box
T = Text(
	frame7,
	height=5,
	width=72
	)
T.grid(
	row=22,
	column=1,
	columnspan=100
	)

#executes the window
mainloop()
