import json

class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease
        self.doctor = None
        self.bill = 0

    def assign_doctor(self, doctor):
        self.doctor = doctor

    def generate_bill(self, amount):
        self.bill += amount

    def to_dict(self):
        return {
            "pid": self.pid,
            "name": self.name,
            "age": self.age,
            "disease": self.disease,
            "doctor": self.doctor,
            "bill": self.bill
        }

class Hospital:
    def __init__(self):
        self.patients = {}

    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")

        if pid in self.patients:
            print("Patient already exists!")
        else:
            patient = Patient(pid, name, age, disease)
            self.patients[pid] = patient
            print("✅ Patient added successfully!")

    def view_patients(self):
        if not self.patients:
            print("No patients found!")
            return

        for p in self.patients.values():
            print(f"\nID: {p.pid}")
            print(f"Name: {p.name}")
            print(f"Age: {p.age}")
            print(f"Disease: {p.disease}")
            print(f"Doctor: {p.doctor}")
            print(f"Bill: ₹{p.bill}")

    def assign_doctor(self):
        pid = input("Enter Patient ID: ")
        if pid in self.patients:
            doctor = input("Enter Doctor Name: ")
            self.patients[pid].assign_doctor(doctor)
            print("👨‍⚕️ Doctor assigned!")
        else:
            print("Patient not found!")

    def generate_bill(self):
        pid = input("Enter Patient ID: ")
        if pid in self.patients:
            amount = float(input("Enter Amount: "))
            self.patients[pid].generate_bill(amount)
            print("💰 Bill updated!")
        else:
            print("Patient not found!")

    def search_patient(self):
        pid = input("Enter Patient ID: ")
        if pid in self.patients:
            p = self.patients[pid]
            print(f"\nFound Patient: {p.name}, Disease: {p.disease}")
        else:
            print("Patient not found!")

    def save_data(self):
        data = {pid: p.to_dict() for pid, p in self.patients.items()}
        with open("hospital_data.json", "w") as f:
            json.dump(data, f)
        print("💾 Data saved!")

    def load_data(self):
        try:
            with open("hospital_data.json", "r") as f:
                data = json.load(f)
                for pid, info in data.items():
                    p = Patient(info['pid'], info['name'], info['age'], info['disease'])
                    p.doctor = info['doctor']
                    p.bill = info['bill']
                    self.patients[pid] = p
            print("📂 Data loaded!")
        except FileNotFoundError:
            print("No previous data found.")

def main():
    hospital = Hospital()
    hospital.load_data()

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Assign Doctor")
        print("4. Generate Bill")
        print("5. Search Patient")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            hospital.add_patient()
        elif choice == '2':
            hospital.view_patients()
        elif choice == '3':
            hospital.assign_doctor()
        elif choice == '4':
            hospital.generate_bill()
        elif choice == '5':
            hospital.search_patient()
        elif choice == '6':
            hospital.save_data()
        elif choice == '7':
            hospital.save_data()
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()