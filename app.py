import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from student_report import Student, StudentReportSystem

# Page config
st.set_page_config(
    page_title="Student Report System",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main content styling */
    .main {
        padding: 2rem;
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
        background-color: #2d2d2d;
        color: #ffffff;
        border: 1px solid #ffffff;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #ffffff;
        color: #1a1a1a;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Form submit button specific styling */
    .stForm .stButton>button {
        background-color: #ffffff;
        color: #1a1a1a;
        border: none;
    }
    
    .stForm .stButton>button:hover {
        background-color: #2d2d2d;
        color: #ffffff;
    }
    
    /* Metric card styling */
    .metric-card {
        background-color: #2d2d2d;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        color: #ffffff;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        padding-top: 2rem;
    }
    
    .sidebar .sidebar-content {
        background-color: #1a1a1a;
    }
    
    /* Menu item styling */
    .css-1v0mbdj.ebxwdo61 {
        background-color: #2d2d2d;
        border-radius: 5px;
        padding: 0.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        color: #ffffff;
    }
    
    .css-1v0mbdj.ebxwdo61:hover {
        background-color: #ffffff;
        color: #1a1a1a;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 600;
    }
    
    /* Form styling */
    .stForm {
        background-color: #2d2d2d;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        margin: 1rem 0;
        color: #ffffff;
    }
    
    /* Input field styling */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #ffffff;
        padding: 0.5rem;
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    .stTextInput>div>div>input:focus, 
    .stNumberInput>div>div>input:focus {
        border-color: #ffffff;
        box-shadow: 0 0 0 1px #ffffff;
    }
    
    /* Label styling */
    .stTextInput>label, 
    .stNumberInput>label {
        color: #ffffff;
        font-weight: 500;
    }
    
    /* Success message styling */
    .stSuccess {
        background-color: #27ae60;
        color: #ffffff;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        border: 1px solid #2ecc71;
    }
    
    /* Info message styling */
    .stInfo {
        background-color: #2d2d2d;
        color: #ffffff;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        border: 1px solid #1a1a1a;
    }
    
    /* Error message styling */
    .stError {
        background-color: #c0392b;
        color: #ffffff;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        border: 1px solid #e74c3c;
    }
    
    /* Section headers */
    .section-header {
        background-color: #2d2d2d;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        color: #ffffff;
    }
    
    /* Form section headers */
    .stForm h3 {
        color: #ffffff;
        margin-bottom: 1rem;
    }
    
    /* Form help text */
    .stForm .stMarkdown p {
        color: #ffffff;
    }
    
    /* Streamlit container styling */
    .stApp {
        background-color: #1a1a1a;
    }
    
    /* Remove white backgrounds from other elements */
    .stMarkdown, .stDataFrame, .stPlotlyChart {
        background-color: #2d2d2d;
        color: #ffffff;
    }
    
    /* Radio button styling */
    .stRadio > div {
        color: #ffffff;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Multiselect styling */
    .stMultiSelect > div > div {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Slider styling */
    .stSlider > div > div > div {
        background-color: #ffffff;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        background-color: #2d2d2d;
    }
    
    .stDataFrame td, .stDataFrame th {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Plotly chart styling */
    .js-plotly-plot {
        background-color: #2d2d2d;
    }
    
    /* Streamlit default styling overrides */
    .stMarkdown {
        color: #ffffff;
    }
    
    .stRadio > label {
        color: #ffffff;
    }
    
    .stSelectbox > label {
        color: #ffffff;
    }
    
    .stMultiSelect > label {
        color: #ffffff;
    }
    
    .stSlider > label {
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'system' not in st.session_state:
    st.session_state.system = StudentReportSystem()
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

def main():
    st.title("🧮 Student Report System")
    st.write("A comprehensive web-based application for managing student records and academic performance.")

    # Sidebar navigation with icons
    with st.sidebar:
        st.markdown("### 📚 Navigation")
        menu = st.radio(
            "",
            ["📊 Dashboard", "➕ Add Student", "👥 View All Students", "🔍 Search by ID", 
             "📈 Performance Analysis", "📊 Subject Statistics", "📋 Student Status",
             "🎯 Student Categories"],
            label_visibility="collapsed"
        )
        
        # Add grading system info in sidebar
        st.markdown("---")
        st.markdown("### 📝 Grading System")
        st.markdown("""
        - A (91-100%): 5.0
        - B+ (81-90%): 4.5
        - B (71-80%): 4.0
        - C+ (61-70%): 3.5
        - C (51-60%): 3.0
        - F (Below 50%): 2.0
        """)

    # Remove the "Menu" prefix from the selection
    menu = menu.replace("📊 ", "").replace("➕ ", "").replace("👥 ", "").replace("🔍 ", "").replace("📈 ", "").replace("📊 ", "").replace("📋 ", "").replace("🎯 ", "")

    if menu == "Dashboard":
        show_dashboard()
    elif menu == "Add Student":
        show_add_student()
    elif menu == "View All Students":
        show_all_students()
    elif menu == "Search by ID":
        show_search()
    elif menu == "Performance Analysis":
        show_performance_analysis()
    elif menu == "Subject Statistics":
        show_subject_statistics()
    elif menu == "Student Status":
        show_student_status()
    elif menu == "Student Categories":
        show_student_categories()

def show_dashboard():
    st.header("📊 Dashboard")
    
    # Get overall statistics
    stats = st.session_state.system.get_overall_statistics()
    
    # Display key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Students", stats['total_students'])
    with col2:
        st.metric("Average Grade", f"{stats['average_grade']}%")
    with col3:
        st.metric("Passing Rate", f"{stats['passing_rate']}%")
    with col4:
        st.metric("At Risk Students", 
                 len(st.session_state.system.get_students_by_status("At Risk")))

    # Grade Distribution Chart
    st.subheader("Grade Distribution")
    grade_df = pd.DataFrame({
        'Grade': list(stats['grade_distribution'].keys()),
        'Count': list(stats['grade_distribution'].values())
    })
    fig = px.pie(grade_df, values='Count', names='Grade', 
                 title='Distribution of Grades',
                 color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig, use_container_width=True)

    # Performance Trend Chart
    st.subheader("Performance Trends")
    perf_df = pd.DataFrame({
        'Performance': list(stats['performance_distribution'].keys()),
        'Count': list(stats['performance_distribution'].values())
    })
    fig = px.bar(perf_df, x='Performance', y='Count',
                 title='Student Performance Distribution',
                 color='Performance',
                 color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig, use_container_width=True)

def show_add_student():
    st.markdown('<div class="section-header">', unsafe_allow_html=True)
    st.header("➕ Add New Student")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Create a form for student input
    with st.form("add_student_form", clear_on_submit=True):
        # Basic Information Section
        st.markdown("### Basic Information")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Student Name", placeholder="Enter student's full name")
        with col2:
            student_id = st.text_input("Student ID", placeholder="Enter student ID number")
        
        # Subject Marks Section
        st.markdown("### Subject Marks")
        st.markdown("Enter marks for each subject (0-100)")
        
        # First row of subjects
        col1, col2, col3 = st.columns(3)
        with col1:
            advanced_prog = st.number_input(
                "Advanced Programming",
                min_value=0,
                max_value=100,
                value=0,
                help="Marks for Advanced Programming"
            )
        with col2:
            web_design = st.number_input(
                "Web Applications Design",
                min_value=0,
                max_value=100,
                value=0,
                help="Marks for Web Applications Design"
            )
        with col3:
            ui_design = st.number_input(
                "UI Design",
                min_value=0,
                max_value=100,
                value=0,
                help="Marks for UI Design"
            )
        
        # Second row of subjects
        col1, col2 = st.columns(2)
        with col1:
            systems_eng = st.number_input(
                "Systems Engineering",
                min_value=0,
                max_value=100,
                value=0,
                help="Marks for Systems Engineering"
            )
        with col2:
            azure_integration = st.number_input(
                "Azure Integration",
                min_value=0,
                max_value=100,
                value=0,
                help="Marks for Azure Integration"
            )
        
        # Form buttons in a row with consistent styling
        st.markdown("### Submit")
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("Add Student", use_container_width=True)
        with col2:
            add_another = st.form_submit_button("Add & Continue", use_container_width=True)
        
        if submitted or add_another:
            if not name:
                st.error("Name cannot be empty!")
            elif not student_id.isdigit():
                st.error("ID must be a number!")
            else:
                try:
                    student = st.session_state.system.add_student(
                        name, student_id, advanced_prog, web_design,
                        ui_design, systems_eng, azure_integration
                    )
                    st.success(f"Student added successfully! Grade: {student.grade} ({student.grade_points})")
                    
                    # If "Add & Continue" was clicked, don't clear the form
                    if not add_another:
                        st.session_state.form_submitted = True
                except ValueError as e:
                    st.error(str(e))

    # Show a message if student was added successfully
    if st.session_state.form_submitted:
        st.info("Student has been added to the system. You can add another student or navigate to other sections.")
        if st.button("Add Another Student", use_container_width=True):
            st.session_state.form_submitted = False
            st.experimental_rerun()

def show_all_students():
    st.header("👥 View All Students")
    if not st.session_state.system.students:
        st.info("No students in the system!")
    else:
        students_data = [student.to_dict() for student in st.session_state.system.get_all_students()]
        df = pd.DataFrame(students_data)
        
        # Add filters
        st.subheader("Filters")
        col1, col2, col3 = st.columns(3)
        with col1:
            grade_filter = st.multiselect("Filter by Grade", df['Grade'].unique())
        with col2:
            status_filter = st.multiselect("Filter by Status", df['Status'].unique())
        with col3:
            category_filter = st.multiselect("Filter by Category", df['Category'].unique())
        
        # Apply filters
        if grade_filter:
            df = df[df['Grade'].isin(grade_filter)]
        if status_filter:
            df = df[df['Status'].isin(status_filter)]
        if category_filter:
            df = df[df['Category'].isin(category_filter)]
        
        # Display data with category colors
        st.dataframe(
            df.style.applymap(
                lambda x: f"background-color: {st.session_state.system.categories[x]['color']}" 
                if x in st.session_state.system.categories else "",
                subset=['Category']
            ),
            use_container_width=True
        )
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            "Download Data",
            csv,
            "student_records.csv",
            "text/csv",
            key='download-csv'
        )

def show_search():
    st.header("🔍 Search Student")
    search_id = st.text_input("Enter Student ID to search")
    if search_id:
        student = st.session_state.system.get_student(search_id)
        if not student:
            st.error("Student not found!")
        else:
            data = student.to_dict()
            st.subheader("Student Details")
            
            # Display basic info
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Name", data['Name'])
                st.metric("ID", data['ID'])
                st.metric("Status", data['Status'])
            with col2:
                st.metric("Average", f"{data['Average']}%")
                st.metric("Grade", f"{data['Grade']} ({data['Grade Points']})")
                st.metric("Category", data['Category'])
            
            # Display category information
            category_info = st.session_state.system.categories[data['Category']]
            st.markdown(f"**Category Description:** {category_info['description']}")
            st.markdown(f"**Category Criteria:** {category_info['criteria']}")
            
            # Display recommendations
            st.markdown("### Recommendations")
            for i, rec in enumerate(st.session_state.system.get_category_recommendations(data['Category']), 1):
                st.markdown(f"{i}. {rec}")
            
            # Display subject marks
            st.subheader("Subject Performance")
            subjects = {
                'Advanced Programming': data['Advanced Programming'],
                'Web Design': data['Web Design'],
                'UI Design': data['UI Design'],
                'Systems Engineering': data['Systems Engineering'],
                'Azure Integration': data['Azure Integration']
            }
            
            # Create a bar chart for subject marks
            fig = go.Figure(data=[
                go.Bar(
                    x=list(subjects.keys()),
                    y=list(subjects.values()),
                    text=list(subjects.values()),
                    textposition='auto',
                )
            ])
            fig.update_layout(
                title="Subject-wise Performance",
                yaxis_title="Marks",
                yaxis_range=[0, 100]
            )
            st.plotly_chart(fig, use_container_width=True)

def show_performance_analysis():
    st.header("📈 Performance Analysis")
    
    if not st.session_state.system.students:
        st.info("No students in the system!")
        return
    
    # Get top students
    n = st.slider("Number of top students to display", 
                 1, len(st.session_state.system.students),
                 min(5, len(st.session_state.system.students)))
    
    top_students = st.session_state.system.get_top_students(n)
    students_data = [student.to_dict() for student in top_students]
    df = pd.DataFrame(students_data)
    
    # Display top students
    st.subheader(f"Top {n} Students")
    st.dataframe(df, use_container_width=True)
    
    # Performance comparison chart
    st.subheader("Performance Comparison")
    fig = go.Figure()
    for subject in ['Advanced Programming', 'Web Design', 'UI Design', 
                   'Systems Engineering', 'Azure Integration']:
        fig.add_trace(go.Box(
            y=df[subject],
            name=subject,
            boxpoints='all',
            jitter=0.3,
            pointpos=-1.8
        ))
    fig.update_layout(
        title="Subject-wise Performance Distribution",
        yaxis_title="Marks",
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)

def show_subject_statistics():
    st.header("📊 Subject Statistics")
    
    if not st.session_state.system.students:
        st.info("No students in the system!")
        return
    
    stats = st.session_state.system.get_subject_statistics()
    
    # Display subject-wise statistics
    for subject, data in stats.items():
        st.subheader(subject)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Average", f"{data['avg']}%")
        with col2:
            st.metric("Highest", f"{data['max']}%")
        with col3:
            st.metric("Lowest", f"{data['min']}%")
        with col4:
            st.metric("Passing Rate", f"{data['passing_rate']}%")
        
        # Create a gauge chart for passing rate with unique key
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=data['passing_rate'],
            title={'text': "Passing Rate"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 60], 'color': "red"},
                    {'range': [60, 80], 'color': "yellow"},
                    {'range': [80, 100], 'color': "green"}
                ]
            }
        ))
        # Add unique key for each subject's gauge chart
        st.plotly_chart(fig, use_container_width=True, key=f"gauge_{subject.replace(' ', '_')}")

    # Add overall subject comparison chart
    st.subheader("Subject Comparison")
    subject_data = {
        'Subject': [],
        'Average': [],
        'Passing Rate': []
    }
    
    for subject, data in stats.items():
        subject_data['Subject'].append(subject)
        subject_data['Average'].append(data['avg'])
        subject_data['Passing Rate'].append(data['passing_rate'])
    
    df = pd.DataFrame(subject_data)
    
    # Create bar chart for subject comparison
    fig = px.bar(df, 
                 x='Subject', 
                 y=['Average', 'Passing Rate'],
                 barmode='group',
                 title='Subject-wise Performance Comparison')
    st.plotly_chart(fig, use_container_width=True, key="subject_comparison")

def show_student_status():
    st.header("📋 Student Status Overview")
    
    if not st.session_state.system.students:
        st.info("No students in the system!")
        return
    
    # Get students by status
    passing_students = st.session_state.system.get_students_by_status("Passing")
    at_risk_students = st.session_state.system.get_students_by_status("At Risk")
    
    # Display status distribution
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Passing Students", len(passing_students))
        if passing_students:
            st.subheader("Passing Students")
            passing_data = [s.to_dict() for s in passing_students]
            st.dataframe(pd.DataFrame(passing_data), use_container_width=True)
    
    with col2:
        st.metric("At Risk Students", len(at_risk_students))
        if at_risk_students:
            st.subheader("At Risk Students")
            at_risk_data = [s.to_dict() for s in at_risk_students]
            st.dataframe(pd.DataFrame(at_risk_data), use_container_width=True)
    
    # Performance trend distribution
    st.subheader("Performance Trend Distribution")
    performance_data = {
        'Excellent': len(st.session_state.system.get_students_by_performance("Excellent")),
        'Good': len(st.session_state.system.get_students_by_performance("Good")),
        'Average': len(st.session_state.system.get_students_by_performance("Average")),
        'Needs Improvement': len(st.session_state.system.get_students_by_performance("Needs Improvement"))
    }
    
    fig = px.pie(
        values=list(performance_data.values()),
        names=list(performance_data.keys()),
        title='Student Performance Distribution',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig, use_container_width=True)

def show_student_categories():
    st.header("🎯 Student Categories")
    
    if not st.session_state.system.students:
        st.info("No students in the system!")
        return
    
    # Get category statistics
    category_stats = st.session_state.system.get_category_statistics()
    
    # Display category distribution
    st.subheader("Category Distribution")
    col1, col2 = st.columns(2)
    
    with col1:
        # Create pie chart for category distribution
        fig = px.pie(
            values=list(category_stats.values()),
            names=list(category_stats.keys()),
            title='Student Category Distribution',
            color=list(category_stats.keys()),
            color_discrete_map=st.session_state.system.categories
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Display category statistics
        for category, count in category_stats.items():
            st.metric(
                category,
                count,
                f"{round((count/len(st.session_state.system.students))*100, 1)}% of total"
            )
    
    # Category details
    st.subheader("Category Details")
    selected_category = st.selectbox(
        "Select Category to View Details",
        list(st.session_state.system.categories.keys())
    )
    
    # Get category information
    category_info = st.session_state.system.categories[selected_category]
    category_performance = st.session_state.system.get_category_performance(selected_category)
    recommendations = st.session_state.system.get_category_recommendations(selected_category)
    
    # Display category information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"### {selected_category}")
        st.markdown(f"**Description:** {category_info['description']}")
        st.markdown(f"**Criteria:** {category_info['criteria']}")
        
        if category_performance:
            st.markdown("### Performance Statistics")
            st.metric("Number of Students", category_performance['count'])
            st.metric("Average Score", f"{round(category_performance['average_score'], 1)}%")
            
            # Subject-wise averages
            st.markdown("### Subject Averages")
            for subject, avg in category_performance['subject_averages'].items():
                st.metric(subject, f"{round(avg, 1)}%")
    
    with col2:
        st.markdown("### Recommendations")
        for i, rec in enumerate(recommendations, 1):
            st.markdown(f"{i}. {rec}")
    
    # List students in selected category
    st.subheader(f"Students in {selected_category}")
    students = st.session_state.system.get_students_by_category(selected_category)
    if students:
        students_data = [student.to_dict() for student in students]
        df = pd.DataFrame(students_data)
        st.dataframe(df, use_container_width=True)
        
        # Download button for category data
        csv = df.to_csv(index=False)
        st.download_button(
            f"Download {selected_category} Data",
            csv,
            f"{selected_category.lower().replace(' ', '_')}_students.csv",
            "text/csv",
            key=f'download-{selected_category}'
        )
    else:
        st.info(f"No students in {selected_category} category")

if __name__ == "__main__":
    main() 