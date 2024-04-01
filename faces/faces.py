#Inputing and converting in main
def main():
    #inputing from user
    faces = input()
    #changing faces
    changed_faces = convert(faces)
    #sending faces
    print(changed_faces)

#converting faces using convert function
def convert(faces):
    #Converting :( to 🙂
    face1 = faces.replace(":)", "🙂")
    #Converting :( to 🙁
    face2 = face1.replace(":(", "🙁")
    #Returning face
    return face2

#Calling main function
main()
