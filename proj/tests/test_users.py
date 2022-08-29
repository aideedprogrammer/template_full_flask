import unittest

import pytest

from .. import intial_app
from proj.models.model import *
import time


class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = intial_app('testing')
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

        # db.drop_all()
        # db.create_all()

    def tearDown(self):

        # db.drop_all()
        # time.sleep(5)
        self.appctx.pop()
        self.app = None
        self.client = None

    def unit_test_calculate(self):
        pass

    @pytest.mark.order(1)
    @pytest.mark.integtest
    def test_call_add(self):
        data={"data": json.dumps(
                {
                    "name": "Zulkamaluddin Bin Pakharuddin",
                    "age": "28",
                    "date_birth": "2022-09-02",
                    "gender": "Male"
                }
            )}

        response = self.client.post('/user/add', data=data)
        user = User.query.filter_by(name="Zulkamaluddin Bin Pakharuddin").first()

        assert user.name == "Zulkamaluddin Bin Pakharuddin"
        assert response.status_code == 200

    @pytest.mark.order(2)
    def test_call_update(self):
        data={"data": json.dumps(
                {
                    "previous_name": "Zulkamaluddin Bin Pakharuddin",
                    "name": "Iqbal Aideed",
                    "age": "28",
                    "date_birth": "2022-09-02",
                    "gender": "Male"
                }
            )}

        response = self.client.post('/user/update', data=data)
        user = User.query.filter_by(name="Iqbal Aideed").first()

        assert user.name == "Iqbal Aideed"
        assert response.status_code == 200

    @pytest.mark.order(3)
    @pytest.mark.slow
    def test_call_list(self):
        response = self.client.get('/user/list')
        datas = json.loads(response.text)['data']
        
        for i in datas:
            # print(i['name'] )
            assert i['name'] == "Iqbal Aideed"

        assert response.status_code == 200

    @pytest.mark.order(4)
    def test_call_delete(self):
        data={"data": json.dumps(
                {
                    "name": "Iqbal Aideed"
                }
            )}

        response = self.client.post('/user/delete', data=data)
        user = User.query.filter_by(name="Iqbal Aideed").first()

        assert user == None
        assert response.status_code == 200

#pytest -s display all print
#pytest -v show test case
#"Pytest by default, it executes the steps randomly" <- randomly or alphabetically