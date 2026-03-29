# import cv2
# import os
# import numpy as np
# import tempfile

# def preprocess_face(image_path):
#     img = cv2.imread(image_path)

#     if img is None:
#         return None

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     face_cascade = cv2.CascadeClassifier(
#         cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
#     )

#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     if len(faces) == 0:
#         return None

#     x, y, w, h = faces[0]
#     face = gray[y:y+h, x:x+w]

#     face = cv2.resize(face, (200, 200))

#     return face


# def compare_faces(face1, face2):
#     hist1 = cv2.calcHist([face1], [0], None, [256], [0, 256])
#     hist2 = cv2.calcHist([face2], [0], None, [256], [0, 256])

#     score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

#     return score


# def recognize_face(camera_image):
#     matched_names = []

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
#         temp_file.write(camera_image.getbuffer())
#         temp_path = temp_file.name

#     captured_face = preprocess_face(temp_path)

#     if captured_face is None:
#         raise ValueError("No face detected")

#     enrolled_images = [
#         f for f in os.listdir("enrolled_faces")
#         if f.endswith(".jpg")
#     ]

#     best_score = -1
#     best_match = "Unknown"

#     for img_file in enrolled_images:
#         img_path = os.path.join("enrolled_faces", img_file)

#         stored_face = preprocess_face(img_path)

#         if stored_face is None:
#             continue

#         score = compare_faces(captured_face, stored_face)

#         if score > best_score:
#             best_score = score
#             best_match = img_file.split('_')[0]

#     os.unlink(temp_path)

#     if best_score > 0.65:
#         matched_names.append(best_match)
#     else:
#         matched_names.append("Unknown")

#     return matched_names

import cv2
import os
import tempfile


def preprocess_face(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None

    x, y, w, h = faces[0]
    face = gray[y:y+h, x:x+w]

    face = cv2.resize(face, (200, 200))

    return face


def compare_faces(face1, face2):
    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(face1, None)
    kp2, des2 = orb.detectAndCompute(face2, None)

    if des1 is None or des2 is None:
        return 0

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)

    return len(matches)


def recognize_face(camera_image):
    matched_names = []

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(camera_image.getbuffer())
        temp_path = temp_file.name

    captured_face = preprocess_face(temp_path)

    if captured_face is None:
        raise ValueError("No face detected")

    enrolled_images = [
        f for f in os.listdir("enrolled_faces")
        if f.endswith(".jpg")
    ]

    best_score = 0
    best_match = "Unknown"

    for img_file in enrolled_images:
        img_path = os.path.join("enrolled_faces", img_file)

        stored_face = preprocess_face(img_path)

        if stored_face is None:
            continue

        score = compare_faces(captured_face, stored_face)

        if score > best_score:
            best_score = score
            best_match = img_file.split('_')[0]

    os.unlink(temp_path)

    if best_score > 35:
        matched_names.append(best_match)
    else:
        matched_names.append("Unknown")

    return matched_names