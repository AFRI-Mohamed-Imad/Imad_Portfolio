from models.profile import Profile
import base64

def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def get_profile():
    profile = Profile(
        name="Imad",
        title="ML & Data Engineer",
        description=(
            "Data Engineer and Data Scientist passionate about process automation and "
            "data analysis. I create innovative solutions to transform data into a performance lever."
        ),
        resume_path="CV_AFRI_Imad_Data_Eng.pdf",
    )
    profile_data = profile.get_profile_data()
    profile_data["image"] = load_image_as_base64("static/images/profile.jpg")
    return profile_data
