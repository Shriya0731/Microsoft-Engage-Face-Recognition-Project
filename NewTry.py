# Delete group if it already exists
# Import namespaces
import os
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
def Train_model():

    # Authenticate Face client
    credentials = CognitiveServicesCredentials('fb040f9506784f9589c861bc41e7490d')
    face_client = FaceClient("https://myengageproject.cognitiveservices.azure.com/", credentials)
    groups = face_client.person_group.list()
    group_id = 'newtry_123'
    for group in groups:
        if group.person_group_id == group_id:
            face_client.person_group.delete(group_id)

    # Create the group
    face_client.person_group.create(group_id, "check1")
    print ('Group created!')
    root = "C:\\Users\ADMIN\\PycharmProjects\\Microsoft Engage Project\\Images\\"
    dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
    # Add each person to the group
    print('Adding people to the group...')
    print(dirlist)
    image_folders = dirlist
    for person_name in image_folders:
        # Add the person
        person = face_client.person_group_person.create(group_id, person_name)
        # Add multiple photo's of the person
        path = "C:\\Users\ADMIN\\PycharmProjects\\Microsoft Engage Project\\Images"
        folder = os.path.join(path, person_name)
        person_pics = os.listdir(folder)
        for pic in person_pics:
            img_path = os.path.join(folder, pic)
            print("Path:",img_path)
            img_stream = open(img_path, "rb")
            try:
              p = face_client.person_group_person.add_face_from_stream(group_id, person.person_id, img_stream)
              print(p)
            except Exception as e:
                pass


    # Train the model
    print('Training model...')
    face_client.person_group.train(group_id)

    # Get the list of people in the group
    print('Facial recognition model trained with the following people:')
    people = face_client.person_group_person.list(group_id)
    for person in people:
        print('-', person.name)
    return group_id
def recognize_face(face_ids,group_id):
    credentials = CognitiveServicesCredentials('fb040f9506784f9589c861bc41e7490d')
    face_client = FaceClient("https://myengageproject.cognitiveservices.azure.com/", credentials)
    recognized_faces = face_client.face.identify(face_ids, group_id)
    print(recognized_faces)
    # Get names for recognized faces
    face_names = {}
    if len(recognized_faces) > 0:
        print(len(recognized_faces), 'faces recognized.')
        for face in recognized_faces:
            person_name = face_client.person_group_person.get(group_id, face.candidates[0].person_id).name
            print('-', person_name)
            face_names[face.face_id] = person_name
        return list(face_names.values())
