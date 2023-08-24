import json
import inquirer

#User chooses the website

def selectWebsite():
    allWebsites = [
    inquirer.List('url',
                    message="Za koju stranicu želiš napraviti tablicu",
                    choices=['drnis.hr', 'djecji-vrtic-drnis.hr',  'ss-ivana-mestrovica-drnis.hr', 'ogsko.hr', 'zena-drnis.hr', 'vrtic-trogir.hr', 'djecji-vrtic-marina.hr', 'pucko-otvoreno-uciliste-drnis.hr', 'promina.hr', 'dv-seget.hr', "eko-promina.hr", 'narodna-knjiznica-drnis.hr', 'gmd.hr', 'biskupija.hr', 'ligaprotivrakadrnis.hr', "nkdosk.hr", 'kalun.hr', 'gradskacistoca-drnis.hr',  'jvp-drnis.hr',  'komunalno-drustvo-biskupija.hr',  'lag-krka.hr', 'silvijasunara.com', 'ljekarna-drnis.hr'],
                ),
    ]

    selectedWebsite = inquirer.prompt(allWebsites)

    file = open(r"C:\Users\jurer\OneDrive\Osobni\Documents\My Web Projects\scripts\websitesData\docCategories.json", "r")
    websites = json.load(file)

    websiteCategories = [] #List of categories for the selected website

    imageFloat = "" #Image float property for the selected website

    imageFloatDefault = "" #Default image float property

    websiteGen = ""

    subSelectedCategory = []

    #User chooses the category
    for i in websites:
        if (i["url"] == selectedWebsite["url"]):
            if (i["url"] == "ogsko.hr" or i["url"] == "ss-ivana-mestrovica-drnis.hr"):
                subSelectedCategory = i["subCategory"]

            websiteCategories = i["categories"]
            imageFloat = i["imageFloat"]
            imageFloatDefault = i["imageFloatDefault"]
            websiteGen = i["websiteGen"]
            break;

    websiteCategories = [
    inquirer.List('category',
                    message="Odaberi kategoriju mape u koju želiš spremiti slike",
                    choices=websiteCategories,
                ),
    ]

    selectedCategory = inquirer.prompt(websiteCategories)

    selectedSubCategory = ""

    if (selectedCategory["category"] == "08_DOKUMENTI") or (selectedCategory["category"] == "06_NASTAVA"):
        subSelectedCategory = [
        inquirer.List('subCategory',
                        message="Odaberi podkategoriju mape u koju želiš spremiti slike",
                        choices=subSelectedCategory,
                    ),
        ]

        selectedSubCategory = inquirer.prompt(subSelectedCategory)["subCategory"]

    postTitle = input("Unesi naslov nove objave: ")


    return selectedWebsite, selectedCategory, postTitle, imageFloat, websiteGen, imageFloatDefault, selectedSubCategory