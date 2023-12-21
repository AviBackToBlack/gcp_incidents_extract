# Google Cloud Platform Incidents Extractor

## Overview
This Python script is designed to extract monitoring incidents from Google Cloud Platform (GCP) between two dates. Since there is no direct API available for this task, the script uses a workaround by mimicking the calls made by the GCP web console. 

## Features
- Retrieves a list of monitoring incidents for a specified GCP project between two dates
- Writes the retrieved incident data into a separate JSON file

## Prerequisites
Before running this script, you must have:
- Python installed on your system.
- Access to a Google Cloud Platform project.
- Network traffic sniffing tools (like browser developer tools) to capture the required authentication information.

## Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AviBackToBlack/gcp_indicents_extract.git
   cd gcp_indicents_extract
   ```

2. **Obtain GCP Project ID and Authentication Information:**
   - Log in to the Google Cloud Console.
   - Navigate to the Monitoring section and open the network tab in your browser's development tools.
   - Trigger an incident list retrieval in the console and look for the outgoing API request.
   - Inspect the request headers and copy the value of the parameters mentioned below.
   
   Note: These parameters are sensitive and should be kept secure.

3. **Configure the Script:**
   - Open `gcp_indicents_extract.py` in a text editor.
   - Replace 'your_project_id' with your actual GCP project ID.
   - Replace 'your_authorization' with **Authorization** header.
   - Replace 'your_key' with **key** HTTP GET parameter.
   - Replace 'your_cookie' with **Cookie** header.
   - Edit **DATE_FROM** and **DATE_TO** variablse by replacing two **YYYY-MM-DD** placeholders to set desired time range.

## Usage

### Run the script using Python:

```bash
python gcp_indicents_extract.py
```

The script will retrieve the incidents and save them in a file named *your_project_id*_incidents.json in the same directory.

## Security Note
The authentication information used in the script is sensitive. Ensure that it is stored securely and not exposed publicly.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is released under the MIT License.
