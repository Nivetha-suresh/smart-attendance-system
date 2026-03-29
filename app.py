import streamlit as st
import os
from PIL import Image
from datetime import datetime
from database import create_tables, insert_student, mark_attendance, get_attendance
from face_utils import recognize_face

create_tables()

if not os.path.exists("enrolled_faces"):
    os.makedirs("enrolled_faces")

st.title("Smart Attendance System using Webcam")

menu = ["Enroll Face", "Mark Attendance", "Attendance Report"]
choice = st.sidebar.selectbox("Menu", menu)

# ------------------ ENROLL ------------------
if choice == "Enroll Face":
    st.header("Enroll Student Face")

    name = st.text_input("Enter Student Name").strip()
    camera_image = st.camera_input("Capture Face")

    if camera_image is not None and name:

        # 🔥 Create multiple images per student
        existing_files = [f for f in os.listdir("enrolled_faces") if f.startswith(name)]
        count = len(existing_files) + 1

        path = f"enrolled_faces/{name}_{count}.jpg"

        with open(path, "wb") as f:
            f.write(camera_image.getbuffer())

        insert_student(name, path)

        st.success(f"{name} enrolled successfully (Image {count})")

        st.info("👉 Capture 3–5 images for better accuracy")

# ------------------ ATTENDANCE ------------------
elif choice == "Mark Attendance":
    st.header("Capture Image for Attendance")

    camera_image = st.camera_input("Take a photo")

    if camera_image is not None:
        image = Image.open(camera_image)
        st.image(image, caption="Captured Image", use_container_width=True)

        with st.spinner("Recognizing face..."):
            try:
                names = recognize_face(camera_image)
            except:
                st.error("❌ No face detected. Please face the camera clearly.")
                st.stop()
                    
        marked = False

        for name in names:
            if name != "Unknown":
                now = datetime.now()
                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")

                mark_attendance(name, date, time)
                st.success(f"{name} marked Present")
                marked = True

        if not marked:
            st.warning("Unknown face detected")

# ------------------ REPORT ------------------
elif choice == "Attendance Report":
    st.header("Attendance Records")

    records = get_attendance()

    for row in records:
        st.write(row)