class Profile:
    def __init__(self, name, title, description, resume_path):
        self.name = name
        self.title = title
        self.description = description
        self.resume_path = resume_path

    def get_profile_data(self):
        return {
            "name": self.name,
            "title": self.title,
            "description": self.description,
            "resume_path": self.resume_path,
        }
