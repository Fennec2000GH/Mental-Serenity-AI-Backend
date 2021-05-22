
import io, os
from dotenv import load_dotenv
from google.oauth2 import service_account
from google.cloud import vision

load_dotenv()
KEYDIR_PATH = os.getenv(key='KEYDIR_PATH')
credentials = service_account.Credentials.from_service_account_file(KEYDIR_PATH)
client = vision.ImageAnnotatorClient(credentials=credentials)

def detect_faces(path):
    """Detects faces in an image."""
    with io.open(file=path, mode='rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

if __name__ == '__main__':
	path = '/mnt/d/Users/qcaij/Desktop/unlimited_power.jpg'
	detect_faces(path=path)
