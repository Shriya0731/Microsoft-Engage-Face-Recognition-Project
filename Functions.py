from NewTry import recognize_face
from face import Face
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from Boarding_Info_Update import boarding
def detectface(image):
    try:
        # Create an authenticated FaceClient.
        KEY = 'fb040f9506784f9589c861bc41e7490d'
        ENDPOINT = "https://myengageproject.cognitiveservices.azure.com/"
        face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
        #group_id = Train_model()
        f = Face('newtry_123', face_client)
        faces, face_ids = f.detectFaces(image)
        person_identified = recognize_face(face_ids, 'newtry_123')
        for person in person_identified:
            boarding(person)
        return person_identified
    except Exception as e:
        print("Exception in detectface() :",e)