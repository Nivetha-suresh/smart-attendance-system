# Smart Attendance System Using Face Recognition

## Project Description

The Smart Attendance System is an intelligent attendance management application developed to automate attendance recording through facial recognition. The system captures facial images using a webcam, identifies enrolled users through image matching, and records attendance automatically with date and time in a local database.

This project eliminates the need for manual attendance marking and improves reliability by integrating computer vision techniques into a simple user-friendly interface.

## Objective

The primary objective of this project is to develop an efficient attendance solution that can:

* Reduce manual effort in attendance tracking
* Minimize duplicate or proxy attendance
* Improve speed and accuracy in attendance recording
* Maintain attendance records digitally for easy retrieval

## Key Features

* Face enrollment using webcam capture
* Automated face recognition for attendance marking
* Attendance recording with timestamp
* Prevention of duplicate attendance entries for the same day
* Attendance report generation
* Lightweight local database integration
* Interactive web interface for user operation

## Technology Stack

* Python
* Streamlit
* OpenCV
* SQLite
* ORB Feature Matching Algorithm

## System Architecture

The system consists of three main modules:

### 1. Face Enrollment Module

Captures student facial images using webcam and stores them in the local enrolled image directory.

### 2. Face Recognition Module

Processes captured attendance images, detects facial regions, extracts facial features, and compares them with enrolled images.

### 3. Attendance Management Module

Stores recognized attendance records in a structured SQLite database with student name, date, time, and status.

## Module Details

### app.py

Main application interface developed using Streamlit. Responsible for:

* Student enrollment
* Attendance capture
* Attendance report display

### database.py

Handles database operations including:

* Student registration
* Attendance insertion
* Attendance retrieval

### face_utils.py

Contains facial recognition logic:

* Face detection
* Face preprocessing
* ORB feature extraction
* Feature matching
  
## Working Procedure

### Enrollment

Users enter their name and capture facial images through webcam for registration.

### Attendance Marking

Users capture a live image, and the system performs face recognition against enrolled records.

### Attendance Recording

Recognized users are marked present automatically and stored in the database.

## Advantages

* Fast attendance process
* Reduced manual errors
* Simple local deployment
* Easy database management
* Suitable for academic environments

## Limitations

* Accuracy may vary under poor lighting conditions
* Works best with frontal face images
* Local storage based implementation
