import cv2
import face_recognition
import numpy as np

known_face_encodings = []
known_face_names = []

srijan = cv2.imread("srijan.jpg")
alan = cv2.imread("alan.jpg")
hrishikesh = cv2.imread("hrishikesh.jpg")
sudhir_sir = cv2.imread("sudhir_sir.jpg")
tanmay = cv2.imread("tanmay.jpg")
sanjal = cv2.imread("sanjal.jpg")

srijan_encoding = face_recognition.face_encodings(srijan)
if srijan_encoding:
    srijan_encoding = srijan_encoding[0]
    known_face_encodings.append(srijan_encoding)
    known_face_names.append("Srijan")

alan_encoding = face_recognition.face_encodings(alan)
if alan_encoding:
    alan_encoding = alan_encoding[0]
    known_face_encodings.append(alan_encoding)
    known_face_names.append("Alan")

hrishikesh_encoding = face_recognition.face_encodings(hrishikesh)
if hrishikesh_encoding:
    hrishikesh_encoding = hrishikesh_encoding[0]
    known_face_encodings.append(hrishikesh_encoding)
    known_face_names.append("Hrishikesh")

sudhir_sir_encoding = face_recognition.face_encodings(sudhir_sir)
if sudhir_sir_encoding:
    sudhir_sir_encoding = sudhir_sir_encoding[0]
    known_face_encodings.append(sudhir_sir_encoding)
    known_face_names.append("Sudhir Sir")

tanmay_encoding = face_recognition.face_encodings(tanmay)
if tanmay_encoding:
    tanmay_encoding = tanmay_encoding[0]
    known_face_encodings.append(tanmay_encoding)
    known_face_names.append("Tanmay")

sanjal_encoding = face_recognition.face_encodings(sanjal)
if sanjal_encoding:
    petu_encoding = petu_encoding[0]
    known_face_encodings.append(sanjal_encoding)
    known_face_names.append("Sanjal")

known_face_encodings = np.array(known_face_encodings)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        if face_encoding.size > 0:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
