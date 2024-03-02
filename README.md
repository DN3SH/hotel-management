# Hotel Management System

## Introduction
The **Hotel Management System** is a software application designed to streamline the operations of a hotel, including managing guest information, room reservations, billing, and more. This project utilizes __optical character recognition (OCR) technology__ to extract relevant information from scanned __Aadhaar cards__, facilitating seamless guest check-in processes.

## Features
- **OCR Integration**: Utilizes Tesseract OCR to extract data from Aadhaar cards, including name, gender, date of birth, mobile number, Aadhaar number, and address.
- **Guest Information Management**: Stores and manages guest information efficiently, enabling quick access and retrieval as needed.
- **Room Reservation System**: Facilitates the booking of rooms, allowing guests to reserve accommodations in advance.
- **Billing and Invoicing**: Generates bills and invoices for guest stays, providing accurate records of charges and payments.
- **User-Friendly Interface**: Intuitive interface for easy navigation and user interaction, enhancing the overall user experience.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hotel-management-system.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Tesseract OCR is installed and configured properly.
4. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Launch the application.
2. Scan the guest's Aadhaar card using the integrated OCR functionality.
3. Verify and confirm the extracted information.
4. Proceed with room reservation and billing as needed.

## Dependencies
- Python (>= 3.6)
- OpenCV
- Spacy
- NumPy
- pytesseract

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
- [DN3SH](https://github.com/DN3SH)