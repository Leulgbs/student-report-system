Student Report System 📚

A comprehensive web-based application for managing student records and academic performance, built with Python and Streamlit.

Features 🌟

-  Student Management
  - Add new students with detailed academic records
  - View and search student information
  - Track student performance across multiple subjects

- Grading System
  - A (91-100%): 5.0
  - B+ (81-90%): 4.5
  - B (71-80%): 4.0
  - C+ (61-70%): 3.5
  - C (51-60%): 3.0
  - F (Below 50%): 2.0

- Student Categories
  - High Achiever (Average ≥ 85% and all subjects ≥ 80%)
  - Consistent Performer (Average ≥ 70% and all subjects ≥ 60%)
  - Average (Average ≥ 60% and all subjects ≥ 50%)
  - Needs Support (Average < 60% or any subject < 50%)
  - Under Review (Mixed performance)

- Performance Analysis
  - Subject-wise statistics
  - Grade distribution
  - Performance trends
  - Category-wise analysis
  - Custom recommendations for each category

- Data Export
  - Download student records as CSV
  - Export category-wise reports

Installation 

1. Clone the repository:
   ```bash
   git clone https://github.com/Leulgbs/student-report-system.git
   cd student-report-system
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Usage 

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

Project Structure 

```
student-report-system/
├── app.py              # Streamlit web application
├── student_report.py   # Core student management system
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore file
```

Features in Detail 

Dashboard
- Overview of student statistics
- Grade distribution visualization
- Performance trend analysis

Student Management
- Add new students with detailed information
- View all students with filtering options
- Search students by ID
- Export student records

Performance Analysis
- Subject-wise performance statistics
- Grade distribution charts
- Performance trend analysis
- Category-wise student distribution

Student Categories
- Automatic categorization based on performance
- Category-wise recommendations
- Detailed category statistics
- Export category reports



Acknowledgments 

- Built with [Streamlit](https://streamlit.io/)
- Data visualization using [Plotly](https://plotly.com/)
- Data manipulation with [Pandas](https://pandas.pydata.org/) 
