import os
import cv2
import json
from camera_model1 import *
def cargar_datos(ruta):
    with open(ruta) as contenido:
        cursos =json.load(contenido)
        return (cursos.get('K'))
if __name__ == '__main__':
    path = 'C:\PRUEBA\Calibrar'
    path_file = os.path.join(path, 'calibration.json')
    # intrinsics parameters
    fx = 1000
    fy = 1000
    width = 585
    height = 1040
    cx = width / 2
    cy = height / 2
    K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1.0]])
    #K = cargar_datos(path_file)
    print(K)
    # extrinsics parameters
    h =2
    R = set_rotation(30, 0, 0)
    t = np.array([0, -3, h])

    # create camera
    camera = projective_camera(K, width, height, R, t)

    square_3D1 = np.array([[0.5, -0.5,0.5], [0.5, -0.5, -0.5], [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5]])
    square_2D1 = projective_camera_project(square_3D1, camera)

    square_3D2 = np.array([[0.5, 0.5,0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5]])  #cara frontal
    square_2D2 = projective_camera_project(square_3D2, camera)

    square_3D3 = np.array([[0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [-0.5, 0.5, 0.5], [-0.5, -0.5, 0.5]])
    square_2D3 = projective_camera_project(square_3D3, camera)

    square_3D4 = np.array([[0.5, 0.5, -0.5], [0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [-0.5, -0.5, -0.5]])
    square_2D4 = projective_camera_project(square_3D4, camera)

    image_projective = 255 * np.ones(shape=[camera.height, camera.width, 3], dtype=np.uint8)
    cv2.line(image_projective, (square_2D1[0][0], square_2D1[0][1]), (square_2D1[1][0], square_2D1[1][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D1[1][0], square_2D1[1][1]), (square_2D1[2][0], square_2D1[2][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D1[2][0], square_2D1[2][1]), (square_2D1[3][0], square_2D1[3][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D1[3][0], square_2D1[3][1]), (square_2D1[0][0], square_2D1[0][1]), (200, 1, 255), 3)

    cv2.line(image_projective, (square_2D2[0][0], square_2D2[0][1]), (square_2D2[1][0], square_2D2[1][1]), (0, 0, 255), 3)
    cv2.line(image_projective, (square_2D2[1][0], square_2D2[1][1]), (square_2D2[2][0], square_2D2[2][1]), (0, 0 ,255), 3)
    cv2.line(image_projective, (square_2D2[2][0], square_2D2[2][1]), (square_2D2[3][0], square_2D2[3][1]), (0, 0, 255), 3)
    cv2.line(image_projective, (square_2D2[3][0], square_2D2[3][1]), (square_2D2[0][0], square_2D2[0][1]), (0, 0, 255), 3)

    cv2.line(image_projective, (square_2D3[0][0], square_2D3[0][1]), (square_2D3[1][0], square_2D3[1][1]), (0, 0, 255), 3)
    cv2.line(image_projective, (square_2D3[2][0], square_2D3[2][1]), (square_2D3[3][0], square_2D3[3][1]), (0, 0, 255), 3)

    cv2.line(image_projective, (square_2D4[0][0], square_2D4[0][1]), (square_2D4[1][0], square_2D4[1][1]), (0, 0, 255), 3)
    cv2.line(image_projective, (square_2D4[2][0], square_2D4[2][1]), (square_2D4[3][0], square_2D4[3][1]), (0, 0, 255), 3)

    cv2.imshow("Image", image_projective)
    cv2.imwrite('Projective.png', image_projective)
    cv2.waitKey(0)