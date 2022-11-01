from models.CourseModel import Course
from models.LearningJourneyModel import LearningJourney
from models.RegistrationModel import Registration
from models.RoleModel import Role
from models.SkillModel import Skill
from models.StaffModel import Staff
from models.UserTypeModel import UserType


#unit test for CourseModel
def test_course_model():
    course = Course('test_id', 'test_name', 'test_description', 'test_status', 'test_type', 'test_category')
    assert course.id == 'test_id'
    assert course.name == 'test_name'
    assert course.description == 'test_description'
    assert course.status == 'test_status'
    assert course.type == 'test_type'
    assert course.category == 'test_category'

#unit test for LearningJourneyModel
def test_learning_journey_model():
    learning_journey = LearningJourney('test_learning_journey', 1, 1)
    assert learning_journey.name == 'test_learning_journey'
    assert learning_journey.staff_id == 1
    assert learning_journey.role_id == 1
    # assert learning_journey.courses ==[]

#unit test for RegistrationModel
def test_registration_model():
    registration = Registration(1, 1, 'test_reg_status', 'test_completion_status')
    assert registration.course_id == 1
    assert registration.staff_id == 1
    assert registration.reg_status == 'test_reg_status'
    assert registration.completion_status == 'test_completion_status'

#unit test for RoleModel
def test_role_model():
    role = Role('test_role', 'test_description', True)
    assert role.name == 'test_role'
    assert role.description == 'test_description'
    assert role.active == True

#unit test for SkillModel
def test_skill_model():
    skill = Skill('test_skill', 'test_description', True)
    assert skill.name == 'test_skill'
    assert skill.description == 'test_description'
    assert skill.active == True

#unit test for StaffModel
def test_staff_model():
    staff = Staff('test_first_name', 'test_last_name', 'test_department', 'test_email', 1)
    assert staff.first_name == 'test_first_name'
    assert staff.last_name == 'test_last_name'
    assert staff.department == 'test_department'
    assert staff.email == 'test_email'
    assert staff.user_type_id == 1

#unit test for UserTypeModel
def test_user_type_model():
    user_type = UserType('test_user_type')
    assert user_type.type == 'test_user_type'





