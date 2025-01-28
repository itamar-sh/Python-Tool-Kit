import requests
import datetime
import json
import PyPDF2  # Library for reading PDF content

def fetch_main_records(first_name: str, last_name: str, from_date: str, thru_date: str):
    # CriteriaSearch endpoint to get main data
    URL_CRITERIA_SEARCH = 'https://recording.seminoleclerk.org/DuProcessWebInquiry/Home/CriteriaSearch'
    criteria_array = [
        {
            "name_direction": True,
            "full_name": f"{last_name},{first_name}",
            "file_date_start": from_date,
            "file_date_end": thru_date,
            "greater_than_page": False,
            "q_NWNW": False,
            "q_NWNE": False,
            "q_NWSE": False,
            "q_NWSW": False,
            "q_NENW": False,
            "q_NENE": False,
            "q_NESW": False,
            "q_NESE": False,
            "q_SWNW": False,
            "q_SWNE": False,
            "q_SWSW": False,
            "q_SWSE": False,
            "q_SENW": False,
            "q_SENE": False,
            "q_SESW": False,
            "q_SESE": False,
            "q_q_search_type": False
        }
    ]

    response = requests.get(
        URL_CRITERIA_SEARCH,
        params={'criteria_array': json.dumps(criteria_array)},
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )
    response.raise_for_status()  # Check for request errors
    return response.json()

def fetch_detailed_pdf(first_name: str, last_name: str, from_date: str, thru_date: str):
    # ResultListDocument endpoint to get PDF response
    URL_DOCUMENT_LIST = 'https://recording.seminoleclerk.org/DuProcessWebInquiry/Home/ResultListDocument'
    criteria_array = [
        {
            "direction": "",
            "name_direction": False,
            "full_name": f"{last_name} {first_name}",
            "file_date_start": from_date,
            "file_date_end": thru_date,
            "greater_than_page": False,
            "q_NWNW": False,
            "q_NWNE": False,
            "q_NWSE": False,
            "q_NWSW": False,
            "q_NENW": False,
            "q_NENE": False,
            "q_NESW": False,
            "q_NESE": False,
            "q_SWNW": False,
            "q_SWNE": False,
            "q_SWSW": False,
            "q_SWSE": False,
            "q_SENW": False,
            "q_SENE": False,
            "q_SESW": False,
            "q_SESE": False,
            "q_q_search_type": False
        }
    ]
    column_list = ["inst_num", "book_reel", "page", "instrument_type", "file_date", "verified_status", "instrument_description", "from_party", "to_party"]

    response = requests.get(
        URL_DOCUMENT_LIST,
        params={
            'criteria_array': json.dumps(criteria_array),
            'column_list': json.dumps(column_list)
        },
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )
    response.raise_for_status()  # Check for request errors
    return response  # PDF response

def extract_pdf_content(pdf_response):
    # Extract content from PDF using PyPDF2
    with open("temp_document.pdf", "wb") as f:
        f.write(pdf_response.content)  # Save PDF response content to file for reading
    with open("temp_document.pdf", "rb") as file:
        reader = PyPDF2.PdfReader(file)
        pdf_text = ''
        for page in reader.pages:
            pdf_text += page.extract_text()
    return pdf_text

def analyze_pdf_for_party_data(pdf_text: str, records: list):
    # Compare PDF content with records to extract full "to" and "from" details
    pdf_lines = pdf_text.splitlines()
    for record in records:
        instrument_number = str(record["inst_num"])
        for line in pdf_lines:
            if instrument_number in line:  # Match by instrument number
                # Update "to" and "from" fields with additional party data from the PDF
                record["from_party_full"] = line.split("From:")[1].split("To:")[0].strip() if "From:" in line else ""
                record["to_party_full"] = line.split("To:")[1].strip() if "To:" in line else ""
    return records

def runner():
    # Define input parameters
    first_name = 'ben'
    last_name = 'smith'
    from_date = '01/10/2023'
    thru_date = '01/06/2024'

    # Fetch main records with partial data
    main_records = fetch_main_records(first_name, last_name, from_date, thru_date)
    import ipdb; ipdb.set_trace()

    # Fetch and extract PDF with full party details
    pdf_response = fetch_detailed_pdf(first_name, last_name, from_date, thru_date)
    pdf_text = extract_pdf_content(pdf_response)

    # Analyze PDF and add full "to" and "from" details to main records
    completed_records = analyze_pdf_for_party_data(pdf_text, main_records)

    # Display the fully combined results
    print(json.dumps(completed_records, indent=4))

if __name__ == "__main__":
    runner()
    
    """
        100 def analyze_pdf_for_party_data(pdf_text: str, records: list):
    101     # Compare PDF content with records to extract full "to" and "from" details
    102     pdf_lines = pdf_text.splitlines()
    103     for record in records:
    104         instrument_number = str(record["inst_num"])
    105         for line in pdf_lines:
    106             if instrument_number in line:  # Match by instrument number
    107                 # Update "to" and "from" fields with additional party data from the PDF
--> 108                 record["from_party_full"] = line.split("From:")[1].split("To:")[0].strip() if "From:" in line else ""
    109                 record["to_party_full"] = line.split("To:")[1].strip() if "To:" in line else ""
    110     return records
    111 

ipdb> pdf_text
'DuProcess® Official Records Search Results\nDate: Sunday, November 10, 2024 12:16 PMSearch Criteria: partydirectiondisplayed: False, party_name: smith ben%, file_date_start: 01/10/2023, file_date_end: 01/06/2024, greater_than_page: False, location_id: %, quarter_quarter_search_type: False, ShowSealedNames: N, \n \nInst Num File Date\n2023004567 1/18/2023 8:28:54 AM'
    """
