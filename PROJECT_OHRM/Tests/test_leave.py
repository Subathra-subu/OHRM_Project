import pytest

from Actions.LoginActions import LoginActions
from Actions.LeaveActions import LeaveActions
from Utilities.ReadConfig import get_config
from Utilities.CSVUtils import get_data
from Utilities.ExcelUtils import get_data as get_excel_data

@pytest.mark.usefixtures("test_setup_and_down")
class TestLeave:

    leave_data = get_data("test_data/leave_data.csv")

    @pytest.mark.parametrize("employee,leave_type,from_date,to_date,comments",[leave_data[0]])
    def test_assign_leave(self,employee,leave_type,from_date,to_date,comments):

        username = get_config("username and password","username")
        password = get_config("username and password","password")
        login = LoginActions(self.driver,self.wait)
        login.login(username,password)
        leave = LeaveActions(self.driver,self.wait)
        result = leave.assign_leave(employee,leave_type,from_date,to_date,comments)
        print(f"Assign Leave Result : {result}")
        assert "Successfully Saved" in result or "Failed to Submit" in result


    @pytest.mark.parametrize("employee,leave_type,from_date,to_date,comments",[leave_data[1]])
    def test_employee_name_required(self,employee,leave_type,from_date,to_date,comments):

        username = get_config("username and password","username")
        password = get_config("username and password","password")
        login = LoginActions(self.driver,self.wait)
        login.login(username,password)
        leave = LeaveActions(self.driver,self.wait)
        message = leave.assign_leave_employee_required(leave_type,from_date,to_date,comments)
        print(f"Validation Message : {message}")
        assert message == "Required"

    def test_all_fields_required(self):

        username = get_config("username and password","username")
        password = get_config("username and password","password")
        login = LoginActions(self.driver,self.wait)
        login.login(username,password)
        leave = LeaveActions(self.driver,self.wait)
        count = leave.assign_leave_all_fields_required()
        print(f"Required Validation Count : {count}")
        assert count == 4

    def test_leave_list_search(self):

        username = get_config("username and password", "username")
        password = get_config("username and password","password")
        login = LoginActions(self.driver,self.wait)
        login.login(username,password)
        leave = LeaveActions(self.driver,self.wait)
        data = get_excel_data("test_data/DirectoryData.xlsx","EmployeeSearch")
        employee_name = data[0][0]
        result = leave.search_leave_list(employee_name)
        assert "James Butler" in result
        assert "Scheduled" in result

    def test_leave_invalidUser_search(self):
        username = get_config("username and password", "username")
        password = get_config("username and password","password")
        login = LoginActions(self.driver,self.wait)
        login.login(username,password)
        leave = LeaveActions(self.driver,self.wait)
        data = get_excel_data("test_data/DirectoryData.xlsx","EmployeeSearch")
        employee_name = "qwErTY"
        result = leave.invalidEmployee_search(employee_name)


