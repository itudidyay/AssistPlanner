import json, csv, requests, datetime

schoolData = {
    "California State University, Maritime Academy": {"id": 1, "code": "CSUMA"},
    "Evergreen Valley College": {"id": 2, "code": "EVERGRN"},
    "Los Angeles City College": {"id": 3, "code": "LACC"},
    "College of Marin": {"id": 4, "code": "MARIN"},
    "College of San Mateo": {"id": 5, "code": "MATEO"},
    "College of the Sequoias": {"id": 6, "code": "SEQUOIAS"},
    "University of California, San Diego": {"id": 7, "code": "UCSD"},
    "Butte College": {"id": 8, "code": "BUTTE"},
    "Cerro Coso Community College": {"id": 9, "code": "CERRO"},
    "Columbia College": {"id": 10, "code": "COLUMBIA"},
    "California Polytechnic University, San Luis Obispo": {"id": 11, "code": "CPSLO"},
    "California State University, Monterey Bay": {"id": 12, "code": "CSUMB"},
    "Merritt College": {"id": 13, "code": "MERRITT"},
    "Santa Ana College": {"id": 14, "code": "RSC"},
    "Cuesta College": {"id": 16, "code": "CUESTA"},
    "Merced College": {"id": 17, "code": "MERCED"},
    "Las Positas College": {"id": 18, "code": "POSITAS"},
    "Victor Valley College": {"id": 19, "code": "VVCC"},
    "Barstow Community College": {"id": 20, "code": "BARSTOW"},
    "California State University, East Bay": {"id": 21, "code": "CSUHAY"},
    "California State University, San Marcos": {"id": 23, "code": "CSUSM"},
    "California State University, Stanislaus": {"id": 24, "code": "CSUSTAN"},
    "Los Angeles Trade Technical College": {"id": 25, "code": "LATT"},
    "San Diego State University": {"id": 26, "code": "SDSU"},
    "American River College": {"id": 27, "code": "ARC"},
    "Contra Costa College": {"id": 28, "code": "CONTRA"},
    "California State University, Fresno": {"id": 29, "code": "CSUFRES"},
    "College of the Desert": {"id": 30, "code": "DESERT"},
    "Los Angeles Harbor College": {"id": 31, "code": "LAHC"},
    "Mission College": {"id": 32, "code": "MISSION"},
    "City College of San Francisco": {"id": 33, "code": "SFCITY"},
    "Compton College": {"id": 34, "code": "COMPTON"},
    "Fresno City College": {"id": 35, "code": "FRESNO"},
    "Reedley College": {"id": 36, "code": "KRC"},
    "Shasta College": {"id": 38, "code": "SHASTA"},
    "San Jose State University": {"id": 39, "code": "SJSU"},
    "Lake Tahoe Community College": {"id": 40, "code": "TAHOE"},
    "Cabrillo College": {"id": 41, "code": "CABRILLO"},
    "California State University, Northridge": {"id": 42, "code": "CSUN"},
    "Glendale Community College": {"id": 43, "code": "GLENDALE"},
    "Los Angeles Valley College": {"id": 44, "code": "LAVC"},
    "San Diego Miramar College": {"id": 45, "code": "MIRAMAR"},
    "University of California, Riverside": {"id": 46, "code": "UCR"},
    "Los Angeles Mission College": {"id": 47, "code": "LAMC"},
    "Ohlone College": {"id": 48, "code": "OHLONE"},
    "Pasadena City College": {"id": 49, "code": "PASADENA"},
    "California State University, Dominguez Hills": {"id": 50, "code": "CSUDH"},
    "Foothill College": {"id": 51, "code": "FOOTHILL"},
    "Modesto Junior College": {"id": 52, "code": "MODESTO"},
    "Mt. San Jacinto College": {"id": 53, "code": "MTSJC"},
    "San Diego City College": {"id": 54, "code": "SDCC"},
    "Golden West College": {"id": 55, "code": "GWC"},
    "Palomar College": {"id": 56, "code": "PALOMAR"},
    "Santa Rosa Junior College": {"id": 57, "code": "SRC"},
    "Berkeley City College": {"id": 58, "code": "VISTA"},
    "California State University, Sacramento": {"id": 60, "code": "CSUS"},
    "Los Medanos College": {"id": 61, "code": "MEDANOS"},
    "Mount San Antonio College": {"id": 62, "code": "MTSAC"},
    "Palo Verde College": {"id": 63, "code": "PALOVRDE"},
    "Rio Hondo College": {"id": 64, "code": "RIOHONDO"},
    "Saddleback College": {"id": 65, "code": "SADDLBK"},
    "Santiago Canyon College": {"id": 66, "code": "SANTIAGO"},
    "Coalinga College": {"id": 67, "code": "WHC"},
    "Canada College": {"id": 68, "code": "CANADA"},
    "Chaffey College": {"id": 69, "code": "CHAFFEY"},
    "Crafton Hills College": {"id": 70, "code": "CRAFTON"},
    "Cypress College": {"id": 71, "code": "CYPRESS"},
    "Gavilan College": {"id": 72, "code": "GAVILAN"},
    "Napa Valley College": {"id": 73, "code": "NAPA"},
    "Orange Coast College": {"id": 74, "code": "OCC"},
    "California Polytechnic University, Pomona": {"id": 75, "code": "CPP"},
    "California State University, Los Angeles": {"id": 76, "code": "CSULA"},
    "Laney College": {"id": 77, "code": "LANEY"},
    "Riverside City College": {"id": 78, "code": "RCC"},
    "University of California, Berkeley": {"id": 79, "code": "UCB"},
    "West Valley College": {"id": 80, "code": "WVC"},
    "California State University, Long Beach": {"id": 81, "code": "CSULB"},
    "Lassen Community College": {"id": 82, "code": "LASSEN"},
    "College of the Redwoods": {"id": 83, "code": "REDWOODS"},
    "Bakersfield College": {"id": 84, "code": "BAKERFLD"},
    "California State University, San Bernardino": {"id": 85, "code": "CSUSB"},
    "Los Angeles Pierce College": {"id": 86, "code": "LAPC"},
    "Oxnard College": {"id": 87, "code": "OXNARD"},
    "Sonoma State University": {"id": 88, "code": "SSU"},
    "University of California, Davis": {"id": 89, "code": "UCD"},
    "Yuba College": {"id": 90, "code": "YUBA"},
    "West Los Angeles College": {"id": 91, "code": "LAWC"},
    "Santa Barbara City College": {"id": 92, "code": "SBCC"},
    "Sierra College": {"id": 93, "code": "SIERRA"},
    "Solano Community College": {"id": 94, "code": "SOLANO"},
    "Ventura College": {"id": 95, "code": "VENTURA"},
    "Chabot College": {"id": 96, "code": "CHABOT"},
    "Citrus College": {"id": 97, "code": "CITRUS"},
    "California State University, Bakersfield": {"id": 98, "code": "CSUB"},
    "Cuyamaca College": {"id": 99, "code": "CUYAMACA"},
    "Mendocino College": {"id": 100, "code": "MENDOCIN"},
    "San Diego Mesa College": {"id": 101, "code": "MESA"},
    "College of the Siskiyous": {"id": 102, "code": "SISKIYOU"},
    "El Camino College": {"id": 103, "code": "CAMINO"},
    "Cerritos College": {"id": 104, "code": "CERRITOS"},
    "Coastline Community College": {"id": 105, "code": "COASTLIN"},
    "Grossmont College": {"id": 106, "code": "GMCC"},
    "Imperial Valley College": {"id": 107, "code": "IMPERIAL"},
    "MiraCosta College": {"id": 108, "code": "MIRACSTA"},
    "San Joaquin Delta College": {"id": 109, "code": "SJDELTA"},
    "Allan Hancock College": {"id": 110, "code": "AHC"},
    "College of Alameda": {"id": 111, "code": "ALAMEDA"},
    "Copper Mountain College": {"id": 112, "code": "COPPER"},
    "De Anza College": {"id": 113, "code": "DAC"},
    "Diablo Valley College": {"id": 114, "code": "DIABLO"},
    "California Polytechnic University, Humboldt": {"id": 115, "code": "HSU"},
    "San Francisco State University": {"id": 116, "code": "SFSU"},
    "University of California, Los Angeles": {"id": 117, "code": "UCLA"},
    "East Los Angeles College": {"id": 118, "code": "LAEC"},
    "Taft College": {"id": 119, "code": "TAFT"},
    "University of California, Irvine": {"id": 120, "code": "UCI"},
    "Antelope Valley College": {"id": 121, "code": "AVC"},
    "Feather River College": {"id": 122, "code": "FEATHER"},
    "Hartnell College": {"id": 123, "code": "HARTNELL"},
    "Irvine Valley College": {"id": 124, "code": "IRVINE"},
    "Porterville College": {"id": 125, "code": "PORTER"},
    "Sacramento City College": {"id": 126, "code": "SCC"},
    "Skyline College": {"id": 127, "code": "SKYLINE"},
    "University of California, Santa Barbara": {"id": 128, "code": "UCSB"},
    "California State University, Fullerton": {"id": 129, "code": "CSUFULL"},
    "Los Angeles Southwest College": {"id": 130, "code": "LASC"},
    "San Bernardino Valley College": {"id": 131, "code": "SBVC"},
    "University of California, Santa Cruz": {"id": 132, "code": "UCSC"},
    "Monterey Peninsula College": {"id": 133, "code": "MONTEREY"},
    "Fullerton College": {"id": 134, "code": "FULLRTON"},
    "Long Beach City College": {"id": 135, "code": "LBCC"},
    "San Jose City College": {"id": 136, "code": "SJCC"},
    "Santa Monica College": {"id": 137, "code": "SMC"},
    "Southwestern College": {"id": 138, "code": "SWSTRN"},
    "Moorpark College": {"id": 139, "code": "MOORPARK"},
    "College of the Canyons": {"id": 140, "code": "CANYONS"},
    "California State University, Chico": {"id": 141, "code": "CSUC"},
    "Cosumnes River College": {"id": 142, "code": "CRC"},
    "California State University, Channel Islands": {"id": 143, "code": "CSUCI"},
    "University of California, Merced": {"id": 144, "code": "UCM"},
    "Folsom Lake College": {"id": 145, "code": "FOLSOM"},
    "Lemoore College": {"id": 146, "code": "WHCL"},
    "Woodland Community College": {"id": 147, "code": "WCC"},
    "Norco College": {"id": 148, "code": "NORCO"},
    "Moreno Valley College": {"id": 149, "code": "MVC"},
    "Clovis Community College": {"id": 150, "code": "CLOVIS"},
    "El Camino College": {"id": 153, "code": "COMPTON"},
    "Madera Community College": {"id": 200, "code": "MCC"},
    "California Lutheran University": {"id": 201, "code": "CLU"},
    "Charles R. Drew University of Medicine and Science": {"id": 204, "code": "CDU"},
    "California Baptist University": {"id": 205, "code": "CBU"},
    "Fresno Pacific University": {"id": 206, "code": "FPU"},
    "Concordia University Irvine": {"id": 207, "code": "CUI"},
    "Laguna College of Art + Design": {"id": 208, "code": "LCAD"},
    "Loyola Marymount University": {"id": 209, "code": "LMU"},
    "Los Angeles Pacific University": {"id": 210, "code": "LAPU"},
    "Dominican University of California": {"id": 211, "code": "DUC"},
    "Mount Saint Mary's University Los Angeles": {"id": 212, "code": "MSMU"},
    "National University": {"id": 213, "code": "NU"},
    "Pepperdine University": {"id": 214, "code": "PEPRDN"},
    "Touro University Worldwide": {"id": 215, "code": "TUW"},
    "Menlo College": {"id": 216, "code": "MENLO"},
    "University of the Pacific": {"id": 217, "code": "UOP"},
    "University of La Verne": {"id": 218, "code": "ULV"},
    "Notre Dame de Namur University": {"id": 219, "code": "NDNU"},
    "University of Redlands": {"id": 220, "code": "UOFR"},
    "Palo Alto University": {"id": 222, "code": "PAU"},
    "Whittier College": {"id": 224, "code": "WC"},
    "Saint Mary's College of California": {"id": 225, "code": "SMCC"},
    "Santa Clara University": {"id": 227, "code": "SCU"},
    "Simpson University": {"id": 228, "code": "SU"}
}

def getCodeAndID(schoolInput):
    for school in schoolData:
        if school == schoolInput or schoolData[school]["id"] == schoolInput or schoolData[school]["code"] == schoolInput:
            return schoolData[school]["code"], schoolData[school]["id"]
    

def getListOfMajors(CCSchoolID, FYSchoolID, yearStart):
    yearID = yearStart - 1949
    urlMajors = requests.get(f"https://assist.org/api/agreements?receivingInstitutionId={FYSchoolID}&sendingInstitutionId={CCSchoolID}&academicYearId={yearID}&categoryCode=major")
    if urlMajors.status_code == 200:
        majorsList = urlMajors.json()["reports"]
        return majorsList
    else:
        raise ValueError('URL did not load')

def getArtCourseFromMajor(majorsList, majorInterested):
    for major in majorsList:
        if major["label"] == majorInterested:
            coursesURL = requests.get(f"https://assist.org/api/articulation/Agreements?Key={major['key']}").json()
            coursesMajor = json.loads(coursesURL["result"]["articulations"])
            return coursesMajor

def getFullNameOfReceivingCourse(articulatingCourse):
    if articulatingCourse["articulation"]["type"] == "Series":
        return articulatingCourse["articulation"]["series"]["name"]
    elif articulatingCourse["articulation"]["type"] == "Course":
        return articulatingCourse["articulation"]["course"]["prefix"] + " " + articulatingCourse["articulation"]["course"]["courseNumber"]
    elif articulatingCourse["articulation"]["type"] == "Requirement":
        return articulatingCourse["articulation"]["requirement"]["name"]
    else:
        print(articulatingCourse["articulation"]["type"])
        raise ValueError('Type of receiving course is not series or course.')

def getFullNameOfSendingCourse(articulatingCourse):
    sendingCoursesList = []
    if articulatingCourse["articulation"]["sendingArticulation"]["items"] != []:
        for subgroupOfCourses in articulatingCourse["articulation"]["sendingArticulation"]["items"]:
            subgroupCourseList = []
            for sendingCourse in subgroupOfCourses["items"]:
                subgroupCourseList += [sendingCourse["prefix"] + " " + sendingCourse["courseNumber"]]
            sendingCoursesList += [f' {subgroupOfCourses["courseConjunction"].lower()} '.join(subgroupCourseList)]

        return "\nor\n".join(sendingCoursesList)

def getAllArtCoursesFromSendingInstitution(year, sendingInstitution, interestedCampusesAndMajorDict, fileName):
    sendingInstitutionCode, sendingInstitutionID = getCodeAndID(sendingInstitution)
    artCoursesDict = {}
    headerRow1 = [None]
    headerRow2 = [sendingInstitutionCode]
    maxColumn = sum(len(value) for value in interestedCampusesAndMajorDict.values())

    columnIndex = 0

    for interestedCampus in interestedCampusesAndMajorDict:
        interestedCampusCode, interestedCampusID = getCodeAndID(interestedCampus)
        majorsList = getListOfMajors(sendingInstitutionID, interestedCampusID, year)
        for interestedMajor in interestedCampusesAndMajorDict[interestedCampus]:
            artCourseForMajor = getArtCourseFromMajor(majorsList, interestedMajor)
            headerRow1 += [interestedCampusCode]
            headerRow2 += [interestedMajor]
            for artCourse in artCourseForMajor:
                receivingCourseName = getFullNameOfReceivingCourse(artCourse)
                sendingCourseName = getFullNameOfSendingCourse(artCourse)
                if sendingCourseName != None:
                    if sendingCourseName not in artCoursesDict:
                        artCoursesDict[sendingCourseName] = [None] * maxColumn
                    artCoursesDict[sendingCourseName][columnIndex] = receivingCourseName
            columnIndex += 1
    
    with open(fileName, mode='w', newline='', encoding='utf-8') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(headerRow1)
        csvWriter.writerow(headerRow2)
        for artCourse in list(artCoursesDict.keys()):
            csvWriter.writerow([artCourse] + artCoursesDict[artCourse])


def getAllArtCoursesForReceivingInstitution(year, sendingInstitutionList, interestedCampus, interestedMajorList, fileName):
    interestedCampusCode, interestedCampusID = getCodeAndID(interestedCampus)
    sendingInstitutionCodeList = []
    artCoursesDict = {}
    for sendingInstitutionIndex, sendingInstitution in enumerate(sendingInstitutionList):
        sendingInstitutionCode, sendingInstitutionID = getCodeAndID(sendingInstitution)
        sendingInstitutionCodeList += [sendingInstitutionCode]
        majorsList = getListOfMajors(sendingInstitutionID, interestedCampusID, year)
        for interestedMajor in interestedMajorList:
            artCourseForMajor = getArtCourseFromMajor(majorsList, interestedMajor)
            for artCourse in artCourseForMajor:
                receivingCourseName = getFullNameOfReceivingCourse(artCourse)
                sendingCourseName = getFullNameOfSendingCourse(artCourse)
                if receivingCourseName not in artCoursesDict:
                    artCoursesDict[receivingCourseName] = {"majors":[], "articulations":[None]*len(sendingInstitutionList)}
                if interestedMajor not in artCoursesDict[receivingCourseName]["majors"]:
                    artCoursesDict[receivingCourseName]["majors"] += [interestedMajor]
                artCoursesDict[receivingCourseName]["articulations"][sendingInstitutionIndex] = sendingCourseName

    with open(fileName, mode='w', newline='', encoding='utf-8') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow([interestedCampusCode]+["For Majors"]+sendingInstitutionCodeList)
        for artCourse in list(artCoursesDict.keys()):
            csvWriter.writerow([artCourse.replace(", ",",\n")] +
                               ["\n".join(artCoursesDict[artCourse]["majors"])] +
                               artCoursesDict[artCourse]["articulations"])