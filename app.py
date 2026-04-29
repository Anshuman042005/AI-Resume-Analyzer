def analyze_resume(resume_text):
    print("\n--- AI Resume Analysis ---\n")

    # Basic skill detection
    if "python" in resume_text.lower():
        print("✔ Good: Python detected")
    else:
        print("⚠ Missing: Python skill")

    if "machine learning" in resume_text.lower():
        print("✔ Good: Machine Learning knowledge detected")
    else:
        print("⚠ Missing: Machine Learning knowledge")

    # Suggested roles
    print("\nSuggested Roles:")
    print("- Data Analyst")
    print("- AI/ML Intern")

    # Skill gaps
    print("\nSkill Gaps:")
    print("- Machine Learning Projects")
    print("- Advanced Python Libraries (NumPy, Pandas)")
    print("- Real-world project experience")

    # Suggestions
    print("\nSuggestions:")
    print("- Add 1–2 AI/ML projects")
    print("- Upload projects to GitHub")
    print("- Learn ML basics (supervised learning)")
    print("- Improve resume with measurable achievements")


# Take input from user
resume = input("Paste your resume here:\n")

# Run analysis
analyze_resume(resume)
