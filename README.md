# AssistPlanner

Assist Planner helps students plan their schedule by showing which courses for their major transfer to their planned CSUs and UCs.

Usage
--------------------

getAllArtCoursesFromSendingInstitution(yearTakingClass, currentCommunityCollege, dictionaryWhereKeysAreUniversitysAndValuesIsListOfDesiredMajors, fileName)

getAllArtCoursesForReceivingInstitution(yearTakingClass, communityCollegeList, desiredUniversity, fileName)

    import AssistPlanner as ap
    ap.getAllArtCoursesFromSendingInstitution(2024,
                                           "Santa Monica College",
                                           {"UCB": ["Political Science, B.A."],
                                            "UCSB": ["Political Science, B.A.", "History, B.A."],
                                            "CSUS": ["Political Science, BA", "History, BA"],
                                            "CPSLO": ["POLITICAL SCIENCE, B.A.", "HISTORY, B.A."]},
                                            "articulationsFromSI.csv")
                                            
### Output
![image](https://github.com/user-attachments/assets/a86f3c55-845f-4923-8224-835eec67f9b7)

                                            
    ap.getAllArtCoursesForReceivingInstitution(2024,
                                            ["SJCC", "WVC", "MISSION", "DAC", "EVERGRN", "FOOTHILL"],
                                            "UCLA",
                                            ["Biology/B.S.", "Neuroscience/B.S."],
                                            "articulationsForRI.csv")
### Output
![image](https://github.com/user-attachments/assets/632d3824-8bca-452d-9061-be6fde845d7b)
