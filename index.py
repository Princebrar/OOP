# firstly create a class named Doctor.
class Doctor:
    def __init__(self,doctor_ID, name, specialization, working_time, qualification, room_number):
        # Assign the provided doctor ID to the instance variable doctor_ID, and similarly do all the rest.
        self.doctor_ID = doctor_ID
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    # This function returns the doctor's ID.
    def get_doctor_id(self):
        return self.doctor_ID
    
    # This function returns the name.
    def get_name(self):
        return self.name
    
    # This function returns the specializations.
    def get_specialization(self):
        return self.specialization
    
    # This function returns the working time.
    def get_working_time(self):
        return self.working_time
    
    # This function returns the qualifications.
    def get_qualification(self):
        return self.qualification
    
    # This function returns the room number.
    def get_room_number(self):
        return self.room_number
    
    # This function gives the doctor's ID to a new value.
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    # This function gives the name to a new value.
    def set_name(self, new_name):
        self.name = new_name

    # This function sets the doctor's specialization to a new value.
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    # This function sets the doctor's working time to a new value.
    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    # This function sets the doctor's qualifications to a new value.
    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    # This function sets the doctor's room number to a new value.
    def set_room_number(self, new_room_number):
        self.room_number = new_room_number
    
    # This function returns a formatted string representation of the Doctor object.
    # this function creates a list of property strings, each containing the attribute's name and value. 
    def __str__(self):
        properties = [
            f"Doctor ID: {self.doctor_id}",
            f"Name: {self.name}",
            f"Specialization: {self.specialization}",
            f"Working Time: {self.working_time}",
            f"Qualification: {self.qualification}",
            f"Room Number: {self.room_number}"
        ]
        return ", ".join(properties)
    
# now create a class named DoctorManager.
class DoctorManager:
     # Call this function to read doctors' information from a file.
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    # This method formats doctor information for storage or display.
    # Create a list of formatted attribute values for the given doctor.
    def format_dr_info(self, doctor):
        format_string = '{:<15}' * 6
        raj = ([
            doctor.get_doctor_id(),
            doctor.get_name(),
            doctor.get_specialization(),
            doctor.get_working_time(),
            doctor.get_qualification(),
            doctor.get_room_number()
        ])
        return format_string.format(*raj)
    
    # present doctor information for storage in a specific format.
    def format_dr_info2(self, doctor):
        return "_".join([
            doctor.get_doctor_id(),
            doctor.get_name(),
            doctor.get_specialization(),
            doctor.get_working_time(),
            doctor.get_qualification(),
            doctor.get_room_number()
        ])

    # This function expects from user to enter information for a new doctor.
    def enter_dr_info(self):
        self.doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Name: ")
        specialization = input("Enter Specialization: ")
        working_time = input("Enter Working Time(e.g., 7am-10pm): ")
        qualification = input("Enter Qualification: ")
        room_number = input("Enter Room Number: ")
        return Doctor(self.doctor_id, name, specialization, working_time, qualification, room_number)

    # this function tries to open the "doctors.txt" file for reading.
    def read_doctors_file(self):
        try:
            with open("doctors.txt", "r") as file:
                first_line_skipped = False
                for line in file:
                    if not first_line_skipped:
                        first_line_skipped = True
                        continue
                    data = line.strip().split("_")
                    if len(data) == 6:
                        doctor = Doctor(data[0], data[1], data[2], data[3], data[4], data[5])
                        self.doctors.append(doctor)
        except FileNotFoundError:
            # If the file is not found, do nothing and continue. 
            pass

    # this function tries to search for a doctor by ID and display their information.
    def search_doctor_by_id(self):
        doctor_id = input("Enter Doctor ID: ")
        format_string = '{:<15}' * 6
        print(format_string.format(*['Id','Name','Specilist','Timing','Qualification','Room Number']))
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                format_string = '{:<15}' * 6
                print(format_string.format(*['Id','Name','Specilist','Timing','Qualification','Room Number']))
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same ID on the system")

    # this function tries to search for a doctor by name and display their information.
    def search_doctor_by_name(self):
        doctor_name = input("Enter Doctor Name: ")
        format_string = '{:<15}' * 6
        for doctor in self.doctors:
            if doctor.get_name() == doctor_name:
                print(format_string.format(*['Id','Name','Specilist','Timing','Qualification','Room Number']))
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same name on the system")

    # this function tries to display formatted information for a given doctor.
    def display_doctor_info(self, doctor):
        print(self.format_dr_info(doctor))

    # this function tries to edit and update information for a doctor.
    def edit_doctor_info(self):
        doctor_id = input("Please enter the id of the doctor that you want to edit their information: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                doctor.set_name(input("Enter new Name: "))
                doctor.set_specialization(input("Enter new Specialization: "))
                doctor.set_working_time(input("Enter new Timing: "))
                doctor.set_qualification(input("Enter new Qualification: "))
                doctor.set_room_number(input("Enter new Room Number: "))
                self.write_list_of_doctors_to_file()
                print(f"Doctor whose ID is {doctor_id} has been edited")
                return
        print("Can't find the doctor with the same ID on the system")

    # this function tries to display a formatted list of all doctors.
    def display_doctors_list(self):
        format_string = '{:<15}' * 6
        print(format_string.format(*['Id','Name','Specilist','Timing','Qualification','Room Number']))
        for doctor in self.doctors:
            self.display_doctor_info(doctor)

    # this function tries to write the list of doctors to a file. 
    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as file:
            file.write('id_name_specilist_timing_qualification_roomNb\n')
            for doctor in self.doctors:
                file.write(self.format_dr_info2(doctor) + "\n")

    # this function tries to add a new doctor to the list and write to a file.
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        self.write_list_of_doctors_to_file()
        print(f"Doctor whose ID is {self.doctor_id} has been added")

# now create a class named Patient.
class Patient:
    # this function tries to 
    def __init__(self, pid=None, name=None, disease=None, gender=None, age=None):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    # Getters
    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age

    # Setters
    def set_pid(self, new_pid):
        self.pid = new_pid

    def set_name(self, new_name):
        self.name = new_name

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        properties = [
            f"PID: {self.pid}",
            f"Name: {self.name}",
            f"Disease: {self.disease}",
            f"Gender: {self.gender}",
            f"Age: {self.age}"
        ]
        return ", ".join(properties)

# now create a class named PatientManager.
class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    # this function tries to format patient information for storage in a specicial format.
    def format_patient_info_for_file(self, patient):
        format_string = '{:<15}' * 5
        raj=([
            patient.get_pid(),
            patient.get_name(),
            patient.get_disease(),
            patient.get_gender(),
            str(patient.get_age())
        ])
        return format_string.format(*raj)
    
    # this function tries to format patient information for storage in a another specicial format.
    def format_patient_info_for_file2(self, patient):
        return "_".join([
            patient.get_pid(),
            patient.get_name(),
            patient.get_disease(),
            patient.get_gender(),
            str(patient.get_age())
        ])

    # this function tries to collect and create a new Patient information based on input by the user.
    def enter_patient_info(self):
        self.pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        disease = input("Enter Disease: ")
        gender = input("Enter Gender: ")
        age = int(input("Enter Age: "))
        return Patient(self.pid, name, disease, gender, age)

    # this function tries to read patient information from a file and populate the list of patients.
    def read_patients_file(self):
        try:
            with open("patients.txt", "r") as file:
                first_line_skipped = False
                for line in file:
                    if not first_line_skipped:
                        first_line_skipped = True
                        continue
                    data = line.strip().split("_")
                    if len(data) == 5:
                        patient = Patient(data[0], data[1], data[2], data[3], data[4],)
                        self.patients.append(patient)
        except FileNotFoundError:
            pass

    # this function tries to search for a patient by ID and display their information.
    def search_patient_by_id(self):
        patient_id = input("Enter Patient ID to search: ")
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                format_string = '{:<15}' * 5
                print(format_string.format(*['Id','Name','Disease','Gender','Age',]))
                self.display_patient_info(patient)
                return
        print("Can't find the Patient with the same id on the system")

    # this function tries to display formatted information for a given patient.
    def display_patient_info(self, patient):
        print(self.format_patient_info_for_file(patient))

    # this function tries to edit and update information for a patient.
    def edit_patient_info_by_id(self):
        patient_id = input("Please enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                print(f"Editing details for Patient: {patient.get_name()}")
                patient.set_name(input("Enter new Name: "))
                patient.set_disease(input("Enter new disease: "))
                patient.set_gender(input("Enter new gender: "))
                patient.set_age(int(input("Enter new age: ")))
                self.write_list_of_patients_to_file()
                print(f"Patient whose ID is {patient_id} has been edited.")
                return
        print("Can't find the Patient with the same id on the system")

    # this function tries to display a formatted list of all patients.
    def display_patients_list(self):
        format_string = '{:<15}' * 5
        print(format_string.format(*['Id','Name','Disease','Gender','Age',]))
        for patient in self.patients:
            self.display_patient_info(patient)

    # this function tries to write the list of patients to a file.
    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            file.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                file.write(self.format_patient_info_for_file2(patient) + "\n")

    # this function tries to add a new patient to the list and write to a file.
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        self.write_list_of_patients_to_file()
        print(f"Patient whose ID is {self.pid} has been edited.")

# now create a class named Management.
class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    # this function tries to display the main menu and manage user interaction.
    def display_menu(self):
        while True:
            print("\nWelcome to Alberta Hospital (AH) Managment system \nSelect from the following options, or select 3 to stop: ")
            print("1. Doctors")
            print("2. Patients")
            print("3. Exit")

            choice = input(">>> ")

            if choice == '1':
                self.display_doctors_submenu()
            elif choice == '2':
                self.display_patients_submenu()
            elif choice == '3':
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    # this function tries to display the submenu for managing doctors.
    def display_doctors_submenu(self):
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors List")
            print("2 - Search for Doctor by ID")
            print("3 - Search for Doctor by name")
            print("4 - Add doctor")
            print("5 - Edit Doctor info")
            print("6 - Back to the Main Menu")

            choice = input(">>> ")

            if choice == '1':
                self.doctor_manager.display_doctors_list()
            elif choice == '2':
                self.doctor_manager.search_doctor_by_id()
            elif choice == '3':
                self.doctor_manager.search_doctor_by_name()
            elif choice == '4':
                self.doctor_manager.add_dr_to_file()
            elif choice == '5':
                self.doctor_manager.edit_doctor_info()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    # this function tries to display the submenu for managing patients.
    def display_patients_submenu(self):
        while True:
            print("\nPatients Menu:")
            print("1 - Display patients List")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient Info")
            print("5 - Back to the Main Menu")

            choice = input(">>> ")

            if choice == '1':
                self.patient_manager.display_patients_list()
            elif choice == '2':
                self.patient_manager.search_patient_by_id()
            elif choice == '3':
                self.patient_manager.add_patient_to_file()
            elif choice == '4':
                self.patient_manager.edit_patient_info_by_id()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a valid option.")
# finally complete this program by proceding as given below
management = Management()
management.display_menu()