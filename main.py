# kyc-kyc-test-data-generator by Agenics N.V.
# A simple tool to generate mock KYC profiles for testing sandbox environments.

import random
import json
from faker import Faker
import os

fake = Faker()


def generate_kyc_profile():
    return {
        "full_name": fake.name(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=75).strftime("%Y-%m-%d"),
        "address": fake.address().replace("\n", ", "),
        "national_id": fake.ssn(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "document_number": fake.bothify(text="??######"),
        "document_type": random.choice(["Passport", "Driver's License", "National ID"]),
        "document_issue_date": fake.date_between(start_date='-10y', end_date='-1y').strftime("%Y-%m-%d"),
        "document_expiry_date": fake.date_between(start_date='today', end_date='+10y').strftime("%Y-%m-%d")
    }


def generate_profiles(n=10):
    return [generate_kyc_profile() for _ in range(n)]


def save_to_file(profiles, filename="kyc_profiles.json"):
    with open(filename, 'w') as f:
        json.dump(profiles, f, indent=4)


def main():
    try:
        profilecount = int(input('Choose number of profiles to generate: '))
        print("Generating mock KYC profiles...")
        profiles = generate_profiles(profilecount)
        save_to_file(profiles)
        print(f"{profilecount} profiles saved to kyc_profiles.json in {os.getcwd()}")
    except:
        print('Invalid profile number input. Use digits.')


if __name__ == "__main__":
    main()
