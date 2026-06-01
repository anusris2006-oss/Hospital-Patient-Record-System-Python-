```python
patients = []

while True:
    print("\n--- Hospital Patient Record Management System ---")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        disease = input("Enter disease: ")

        patient = {
            "Name": name,
            "Age": age,
            "Disease": disease
        }

        patients.append(patient)
        print("Patient record added successfully!")

    elif choice == '2':
        if len(patients) == 0:
            print("No patient records found.")
        else:
            print("\nPatient Records:")
            for patient in patients:
                print(patient)

    elif choice == '3':
        search_name = input("Enter patient name to search: ")

        found = False
        for patient in patients:
            if patient["Name"].lower() == search_name.lower():
                print("Patient Found:")
                print(patient)
                found = True

        if not found:
            print("Patient not found.")

    elif choice == '4':
        delete_name = input("Enter patient name to delete: ")

        found = False
        for patient in patients:
            if patient["Name"].lower() == delete_name.lower():
                patients.remove(patient)
                print("Patient record deleted successfully!")
                found = True
                break

        if not found:
            print("Patient not found.")

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
```
