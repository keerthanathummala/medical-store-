import matplotlib.pyplot as plt
import numpy as np

class Border:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        lining = "=" * len(self.title)
        return f"{lining}\n| {self.title} |\n{lining}"
heading = Border(" project topic :- MEDICAL STORE MANAGEMENT ")
print(heading)

print("please fill the details below :- ")

# Initialize an empty list to store the user entered information
data = []

b = []  # creating a list to store BMI of multiple patients
a = []  # creating a list to store age of multiple patients

def i_p(count):
    count += 1
    name = input("Name : ")
    age = int(input("Age : "))
    gender = input("Gender(female/male) : ")
    height = float(input("enter your height in m: "))
    weight = float(input("weight in kg : "))
    BMI = weight / (height ** 2)

    symptoms = input("\nenter your symptoms : ").strip().split(",")  # removing additional space from start,end of the string and then spliting the string
    symptoms = [word.strip() for word in symptoms]  # if any space is present even after spliting then we are remove those additional spaces
    symptoms = [word.capitalize() for word in symptoms]  # making first letter of every element in symptoms

    priception = ""
    p = np.array(["Hypertension", "Diabetes1", "Diabetes2"])
    for i in range(len(symptoms)):
        for j in range(len(p)):
            if symptoms[i] == p[j]:
                print("medication for " + str(symptoms[i]) + " cant be prescibed without presception ")
                while (priception == ""):  # keep asking user till they enter the priception
                    priception = input("enter yourdoctors priception : ")

    priception = list(priception.split(","))  # split when u encounter ","
    priception = [word.strip() for word in priception]  # if any space is present even after spliting then we are remove those additional spaces
    priception = [word.capitalize() for word in priception]  # making first letter of every element in priception

    meds = {
        "Cold": "paracetamol 500mg  every 4 to 6 hours as necessary for relief",
        "Fever": "Dolo 650mg every 4 to 6 hours as necessary for relief",
        "Diarrhea": ["oral rehydration salts", "loperamide 4 mg (two capsules or tablets)"],
        "Bodypain": "Ibuprofen 200-400 mg every 4-6 hours as needed",
        "Headache": "Acetaminophen 500-1000 mg every 4-6 hours as needed, up to a maximum of 4000 mg per day.",
        "Acidity": "Antacids Calcium carbonate: 500 mg to 1000 mg as symptoms occur, up to a maximum of 3000 mg per day.",
        "Menstrual cramp": "Ibuprofen  200 to 400 mg every 4 to 6 hours as needed",
        "Cough": "cough syrup   10-20 mg every 4-6 hours as needed, not exceeding 120 mg in a 24-hour period.",
        "Constipation": "Docusate Sodium 50 to 360 milligrams (mg) per day, usually divided into 1 to 4 doses",
        "Sorethroat": "Paracetamol 325 mg to 1000 mg every 4 to 6 hours as needed",
        "Bp": "Lisinopril 10 mg once daily taken orally and can be taken with or without food",
        "High cholesterol": "Atorvastatin 10 to 20 mg once daily",
        "Asthma": "Fluticasone Propionate 88 to 440 micrograms (mcg) twice daily, administered via inhalation",
        "Skininfection": "Clindamycin Apply a thin layer of the topical gel or cream to the affected area(s) twice daily. The affected area should be clean and dry before applying the medication. Wash hands after application unless the hands are the area being treated",
        "Raches": "Clindamycin Apply a thin layer of the topical gel or cream to the affected area(s) twice daily. The affected area should be clean and dry before applying the medication. Wash hands after application unless the hands are the area being treated"
    }
    Hypertension = {
        "Enalapril": "5-40 mg once daily",
        "Lisinopril": "10-40 mg once daily",
        "Ramipril": "2.5-20 mg once daily",
        "Losartan": " 25-100 mg once daily",
        "Valsartan": "40-320 mg once daily",
        "Telmisartan": "20-80 mg once daily",
        "Amlodipine": "2.5-10 mg once daily",
        "Nifedipine ER": "30-90 mg once daily",
        "Diltiazem_ER": "120-360 mg once daily",
        "Hydrochlorothiazide (HCTZ)": "12.5-50 mg once daily",
        "Chlorthalidone": "12.5-25 mg once daily",
        "Indapamide": "1.25-2.5 mg once daily",
        "Atenolol": "25-100 mg once daily",
        "Metoprolol": "25-100 mg twice daily",
        "Bisoprolol": "2.5-10 mg once daily",
        "Doxazosin": "1-16 mg once daily",
        "Aliskiren": "150-300 mg once daily",
        "Clonidine": "0.1-0.3 mg twice daily",
        "Methyldopa": "250-1000 mg two to three times daily"
    }
    Diabetes1 = {
        "Insulin lispro": "Administered before meals to control postprandial glucose spikes",
        "Insulin": "30 minutes before meals to control postprandial glucose levels.",
        "Nph insulin": "0.2 to 0.6 units per kilogram of body weight per day , typically injected once or twice daily.",
        "Insulin glargine": "0.1 to 0.2 units per kilogram of body weight per day."
    }
    Diabetes2 = {
        "Metformin": " 500 mg or 850 mg once daily with meals",
        "Glipizide": "5 mg once daily, with adjustments up to 20 mg per day.",
        "Glyburide": "2.5 mg to 5 mg once daily, with adjustments up to 20 mg per day.",
        "Glimepiride": "1-2 mg once daily, with adjustments up to 8 mg per day.",
        "Sitagliptin": "The usual dose is 100 mg once daily.",
        "Saxagliptin": "The usual dose is 2.5 mg to 5 mg once daily.",
        "Linagliptin": "The usual dose is 5 mg once daily."
    }
    if 1 <= age <= 5 or BMI < 18:  # based on the age and BMI medication changes
        medication2 = {
            "Fever": "Acetaminophen dosage is 160 to 240 mg every 4 to 6 hours as needed. The maximum daily dosage should not exceed 960 mg",
            "Cold": "Acetaminophen dosage is 160 to 240 mg every 4 to 6 hours as needed. The maximum daily dosage should not exceed 960 mg",
            "Diarrhea": "Oral Rehydration Solution (ORS)",
            "Headache": "Acetaminophen dosage is 240 mg to 320 mg every 4 to 6 hours as needed, not exceeding 5 dosesin 24 hours.",
            "Acidity": "Famotidine Oral dosage: 0.5 mg/kg/dose, twice daily, up to a maximum of 40 mg per day",
            "Body pain": "Ibuprofen dosage ranges from 5 to 10 milligrams per kilogram (mg/kg) of body weight per dose. This dose can be given every 6 to 8 hours as needed for pain relief",
            "Cough": "Dextromethorphan dosage is 5 to 10 milligrams (mg) every 4 to 6 hours, not to exceed 60 mg in a 24-hour period.",
            "Contipation": "Polyethylene Glycol 3350 dosage is 0.5 to 1.5 grams per kilogram of body weight per day",
            "Sorethroat": "Acetaminophen 10 to 15 milligrams (mg) per kilogram (kg) of body weight, every 4 to 6 hours, as needed",
            "Asthma": "Albuterol dose is 1 to 2 puffs (90 mcg per puff) every 4 to 6 hours as needed",
            "Skin infection": "Mupirocin Apply a small amount of the ointment (approximately half an inch or 1.25 centimeters) to the affected area three times daily",
            "Raches": "Mupirocin Apply a small amount of the ointment (approximately half an inch or 1.25 centimeters) to the affected area three times daily"
        }
    if 6 <= age <= 11 or BMI < 18:
        medication2 = {
            "Fever": "Acetaminophen dosage is 320 to 480 mg every 4 to 6 hours as needed. The maximum daily dosage should notexceed 2,400 mg",
            "Cold": "Acetaminophen dosage is 320 to 480 mg every 4 to 6 hours as needed. The maximum daily dosage should not exceed 2,400 mg",
            "Diarrhea": "Oral Rehydration Solution (ORS)",
            "Headache": "Acetaminophen dosage is 320 mg to 480 mg every 4 to 6 hours as needed, not exceeding 5 doses in 24 hours",
            "Acidity": "Famotidine Oral dosage: 0.5 mg/kg/dose, twice daily, up to a maximum of 40 mg per day",
            "Body pain": "Ibuprofen dosage ranges from 5 to 10 milligrams per kilogram (mg/kg) of body weight per dose. This dose can be given every 6 to 8 hours as needed for pain relief",
            "Cough": "Dextromethorphan dosage is 10 to 20 milligrams (mg) every 4 to 6 hours, not to exceed 120 mg in a 24-hour period",
            "Contipation": "Polyethylene Glycol 3350 dosage is 0.5 to 1.5 grams per kilogram of body weight per day",
            "Sorethroat": "Acetaminophen 10 to 15 milligrams (mg) per kilogram (kg) of body weight, every 4 to 6 hours, as needed",
            "Asthma": "Albuterol dose is 1 to 2 puffs (90 mcg per puff) every 4 to 6 hours as needed",
            "Skin infection": "Mupirocin Apply a small amount of the ointment (approximately half an inch or 1.25 centimeters) to the affected area three times daily",
            "Raches": "Mupirocin Apply a small amount of the ointment (approximately half an inch or 1.25 centimeters) to the affected area three times daily"
        }
        print("\nmedication for your symptom : ")
    if BMI >= 18:
        for i in range(len(symptoms)): 
            for key, value in meds.items(): 
                if symptoms[i] == key:  # comparing values of symptoms with keys of medication
                    print(key + " : " + value)

    elif BMI < 18:
        for i in range(len(symptoms)):
            for key, value in medication2.items():
                if symptoms[i] == key:  # comparing values of symptoms with keys of medication
                    print(key + " : " + value)

    h = [Hypertension, Diabetes1, Diabetes2]  # inputting all the symptoms which require preception into a list
    for i in range(len(h)):
        for keys, values in (h[i].items()):  # h[i] is used to access element of list and elements of the list are dictionary
            for k in priception:
                if k == keys:  # comparing values in preception with keys of h[i](dictionary)
                    print(keys + " : " + values)

    print("\n")
    if age > 15:
        if BMI > 25:
            print("you are over weight , loose some weight")
        elif BMI < 18:
            print("you are under weight , gain some weight")
    print(" If the prescibed medication doesn't show any effect you are requested to consult the doctor ")

    # Asking the user if user want to exit the program

    
    f = open("C:\\Users\\KEERTHANA\\Desktop\\python\\python notes\\python_project\\patient_details.txt", "a")
    f.write("\nname : " + name + "\nage : " + str(age) + "\ngender: " + gender + "\nweight : " + str(weight) + "\nBMI : " + str(BMI)+"\n")
    f.close()

    b.append(BMI)
    a.append(age)
    exit = input("Do you want to exit the program? (y/n): ")
    if (exit.lower() == "n"):
        return i_p(count=count + 1)
    else:
        return (b, a)

i_p(0)
print("\n")
# asking user if he want to see data of patients
decision = input("want to check details of patiens who visited the store till now y/n : ")
if decision == "y":
    x = open("C:\\Users\\KEERTHANA\\Desktop\\python\\python notes\\python_project\\patient_details.txt", "r")
    print(x.read())

# ploting graph between age and BMI
plt.bar(a, b, align="center", alpha=0.1)
plt.xlabel("age")
plt.ylabel("BMI")
plt.title("BMI vs Age")
plt.show()